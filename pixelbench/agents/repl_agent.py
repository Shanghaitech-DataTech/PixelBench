"""Shared file-edit/run agent loop with image feedback for CLI and Web.

The historical REPLAgent name and explicit legacy KernelSession support remain
for existing integrations; production hosts use FileSession and file tools.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import time
from typing import Any, Dict, List, Optional, Protocol, runtime_checkable

from pixelbench.agents.base import Agent, AgentResult, Budget
from pixelbench.agents.chat import LLMClient, LongRequestCut
from pixelbench.core.canvas import CELL_CONVENTION, PixelCanvas
from pixelbench.repl.kernel import KernelResult, KernelSession
from pixelbench.tasks.specs import TaskSpec


@runtime_checkable
class EpisodeEvents(Protocol):
    """Optional host callbacks fired by :meth:`REPLAgent.run`.

    A host (e.g. the web console) implements this to observe the shared
    agent loop.  Every method has a default no-op so a bare object works.
    """

    def on_llm_response(self, step: int, content: str, tool_calls: List[Any], usage: Optional[dict] = None) -> None: ...
    def on_no_tool_calls(self, step: int, content: str) -> None: ...
    def on_finish_tool(self, step: int, tc_id: str) -> None: ...
    def on_code_call(self, step: int, tc_id: str, code: str) -> None: ...
    def on_code_result(self, step: int, tc_id: str, code: str, result: KernelResult, session: KernelSession) -> None: ...
    def on_round_end(self, step: int) -> bool:
        """Called at the end of each round; return False to abort the run.
        The web console blocks here in step mode until the user advances."""
        return True
    def should_stop(self) -> bool: return False
    def on_llm_error(self, step: int, exc: Exception) -> None: ...
    def on_run_end(self, result: AgentResult) -> None: ...


def run_code_tool(surface: str = "full", vision: bool = True, aligned: bool = False) -> Dict[str, Any]:
    """The ``run_code`` tool schema, documented from the canonical tool docs.

    ``vision`` decides which parts of the tool docs the model sees:
    multimodal models are told the 'image' observation modes exist and that
    rendered PNGs are fed into their vision module; text-only models get a
    description with every image option removed.
    """
    from pixelbench.repl.tools import SURFACES, tool_docs

    if surface not in SURFACES:
        raise ValueError(f"unknown tool surface {surface!r}; known: {sorted(SURFACES)}")
    from pixelbench.repl.skill_docs import skill_tool_docs
    return {
        "type": "function",
        "function": {
            "name": "run_code",
            "description": skill_tool_docs(vision, surface=surface),
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "Python code to run in the session."}
                },
                "required": ["code"],
            },
        },
    }

from pixelbench.repl.skill_docs import skill_system_prompt, skill_user_content

DEFAULT_SYSTEM_PROMPT = skill_system_prompt(True)
DEFAULT_SYSTEM_PROMPT_TEXT = skill_system_prompt(False)
REDRAW_SYSTEM_PROMPT = DEFAULT_SYSTEM_PROMPT + " For this task, paint using redraw(canvas, rows) with the entire pixel matrix."
REDRAW_SYSTEM_PROMPT_TEXT = DEFAULT_SYSTEM_PROMPT_TEXT + " For this task, paint using redraw(canvas, rows) with the entire pixel matrix."


def build_episode_user_content(task, reference_png=None, vision=True):
    content = skill_user_content(task)
    if vision and reference_png is not None and task.task_type != 'restoration':
        content.append({'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + base64.b64encode(reference_png).decode()}})
    return content


def _usage_breakdown(raw: Optional[dict]) -> Dict[str, int]:
    """Reasoning and cached-prompt tokens from either completions or Responses usage."""
    raw = raw or {}
    out_details = raw.get("completion_tokens_details") or raw.get("output_tokens_details") or {}
    in_details = raw.get("prompt_tokens_details") or raw.get("input_tokens_details") or {}
    return {"reasoning_tokens": int(out_details.get("reasoning_tokens") or 0),
            "cached_tokens": int(in_details.get("cached_tokens") or raw.get("prompt_cache_hit_tokens") or 0)}


def _save_messages(messages: List[dict], root) -> None:
    """Persist the exact final context, with inline images moved to sent_images/<sha256>.png."""
    image_dir = root / "sent_images"

    def strip(value):
        if isinstance(value, dict):
            url = value.get("url")
            if isinstance(url, str) and url.startswith("data:image/") and ";base64," in url:
                data = base64.b64decode(url.split(";base64,", 1)[1])
                digest = hashlib.sha256(data).hexdigest()
                image_dir.mkdir(exist_ok=True)
                target = image_dir / f"{digest}.png"
                if not target.exists():
                    target.write_bytes(data)
                return {**{k: v for k, v in value.items() if k != "url"}, "url_sha256": digest}
            return {k: strip(v) for k, v in value.items()}
        if isinstance(value, list):
            return [strip(v) for v in value]
        return value

    (root / "messages_final.json").write_text(json.dumps(strip(messages), ensure_ascii=False, indent=1, default=str))


class REPLAgent(Agent):
    requires_repl = True

    def __init__(
        self,
        name: str = "repl",
        llm: Optional[LLMClient] = None,
        system_prompt: Optional[str] = None,
        vision: bool = True,
        max_steps: Optional[int] = None,
        surface: str = "full",
        instruction_role: Optional[str] = None,
    ) -> None:
        from pixelbench.repl.tools import SURFACES

        if surface not in SURFACES:
            raise ValueError(f"unknown tool surface {surface!r}; known: {sorted(SURFACES)}")
        self.name = name
        self.llm = llm
        self.surface = surface
        instruction_role = instruction_role or ('developer' if getattr(llm, 'api_format', None) == 'responses' else 'system')
        if instruction_role not in ('system', 'developer'):
            raise ValueError('instruction_role must be system or developer')
        self.instruction_role = instruction_role
        # which tool surface the runner should bind in the prelude
        self.prelude_surface = surface
        self._custom_system_prompt = system_prompt is not None
        self.system_prompt = system_prompt or (
            (REDRAW_SYSTEM_PROMPT if vision else REDRAW_SYSTEM_PROMPT_TEXT)
            if surface == "redraw"
            else (DEFAULT_SYSTEM_PROMPT if vision else DEFAULT_SYSTEM_PROMPT_TEXT)
        )
        self.vision = vision
        self.max_steps_override = max_steps

    # -- helpers -------------------------------------------------------
    @staticmethod
    def _tool_call_fields(tc: Any):
        """Normalize an openai tool call object or a plain dict."""
        if hasattr(tc, "id"):
            return tc.id, tc.function.name, tc.function.arguments
        return tc["id"], tc["function"]["name"], tc["function"]["arguments"]

    def _extract(self, session: KernelSession) -> Optional[PixelCanvas]:
        try:
            return session.extract_final_canvas()
        except Exception:
            return None

    def _extract_frames(self, session: KernelSession) -> List[PixelCanvas]:
        try:
            return session.extract_final_frames()
        except Exception:
            return []

    # -- main loop -----------------------------------------------------
    def run(
        self,
        task: TaskSpec,
        session: Optional[KernelSession],
        budget: Budget,
        events: Optional[EpisodeEvents] = None,
        language: str = "",
        instruction: str = "",
    ) -> AgentResult:
        """Run one episode against a ready kernel session.

        ``events`` (optional): a host observer (e.g. the web console) that
        receives per-step callbacks — assistant text, tool calls, code
        results and round boundaries — without reimplementing the loop.
        ``language``/``instruction`` (optional, web console): extra context
        appended to the first user message.  CLI/runner callers omit them
        and pass no events; behaviour is unchanged.
        """
        if session is None:
            return AgentResult(ok=False, error="REPLAgent requires a kernel session")
        if self.llm is None:
            return AgentResult(ok=False, error="REPLAgent requires an LLMClient")
        from pixelbench.repl.file_session import FileSession
        from pixelbench.repl.file_docs import file_prompt, file_tools, file_submission_instructions
        file_mode = isinstance(session, FileSession)
        max_steps = self.max_steps_override or budget.max_steps

        # live Phoenix tracing is ON by default (opt out: PIXELBENCH_TRACE_BACKEND=off)
        hook = None
        try:
            from pixelbench.phoenix_pixel import LivePhoenixHook, phoenix_backend_enabled

            if phoenix_backend_enabled():
                hook = LivePhoenixHook()
                if hook.enabled:
                    hook.start_episode(task, self.name)
        except Exception:  # noqa: BLE001 - tracing must never break the run
            hook = None

        from pixelbench.repl.skill_runtime import uses_skill
        from pixelbench.repl.skill_docs import skill_system_prompt, skill_user_content
        aligned = uses_skill(task, self.surface)
        system_prompt = (skill_system_prompt(self.vision, surface=self.surface)
                         if aligned and not self._custom_system_prompt else self.system_prompt)
        if file_mode:
            system_prompt = file_prompt(self.vision, self.surface) + ('\n' + self.system_prompt if self._custom_system_prompt else '')
        messages: List[dict] = [
            {"role": self.instruction_role, "content": system_prompt},
        ]
        reference_png = None
        # only a vision model can see the reference as an image; text-only
        # models get the textual pointer added by build_episode_user_content
        if self.vision and task.reference_visible and task.reference is not None:
            reference_png = task.reference.render_png_bytes(scale=8)
        user_content = (skill_user_content(task) if aligned else
                        build_episode_user_content(task, reference_png, vision=self.vision))
        # make the step budget explicit up front: the model cannot count
        # reliably on its own (LLMs are stateless), and it is never told
        # when the harness truncates it at the step cap
        user_content = user_content + [
            {
                "type": "text",
                "text": (
                    f"You have at most {max_steps} model rounds total. "
                    "Plan your work so you finish within the budget; call finish(canvas_or_list) inside run_code when the "
                    "drawing is complete."
                ),
            }
        ]
        if file_mode:
            user_content[-1]['text'] = f'You may make at most {max_steps} write_file/edit_file calls. Reads and run calls do not consume this budget. After the last edit, run your file with submit=True. ' + file_submission_instructions(task)
        if language:
            lang_note = {
                "zh-CN": "请使用中文进行推理和回复。",
                "en-US": "Please reason and respond in English.",
                "ja-JP": "推論と返答は日本語で行ってください。",
            }.get(language)
            if lang_note:
                user_content.append({"type": "text", "text": f"[语言] {lang_note}"})
        messages.append({"role": "user", "content": user_content})

        if instruction:
            messages.append({"role": "user", "content": str(instruction)})

        from pixelbench.repl.event_log import EventLog
        transcript = EventLog(session.root / 'events.jsonl' if file_mode else None)
        if file_mode:
            (session.root / 'initial_context.json').write_text(json.dumps({
                'messages': messages, 'tools': file_tools(self.vision, self.surface)
            }, ensure_ascii=False, indent=2))
        terminal_error = None
        terminal_reason = None
        usage_totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "steps_with_usage": 0,
                        "reasoning_tokens": 0, "cached_tokens": 0, "llm_calls": 0, "llm_seconds": 0.0,
                        "retries": 0, "tool_seconds": 0.0}
        finished = False
        # In file mode, a model round is spent editing source only when it
        # mutates a source file.  Running a program is an execution/submit
        # action and must remain possible after the final write.  The generous
        # model-round guard prevents a read/run-only loop from being unbounded.
        steps = 0
        mutation_steps = 0
        last_round_notice_sent = False
        max_model_rounds = max(max_steps * 3, max_steps + 3) if file_mode else max_steps

        episode_started = time.time()
        episode_cut_s = getattr(self.llm, 'episode_cut_s', None)
        for step in range(max_model_rounds):
            if episode_cut_s and time.time() - episode_started > episode_cut_s:
                transcript.append({"step": step, "kind": "episode_time_cut",
                                   "content": f"episode exceeded {episode_cut_s:.0f}s; keeping the intermediate result"})
                break
            if ((mutation_steps >= max_steps - 1) if file_mode else (step == max_steps - 1)) and not last_round_notice_sent:
                notice = (f"This is your LAST ROUND. There will be no further model round. "
                          f"Regardless of completeness, you MUST call finish inside run_code now, "
                          f"submitting exactly {max(1, task.num_frames or 1)} Canvas object(s) in task order. "
                          "Use finish(result) for one image or finish([f1, f2, ...]) for multiple images. "
                          "Submit your best existing work even if unfinished; do not just describe it.")
                if file_mode:
                    notice = file_submission_instructions(task, last_round=True)
                messages.append({'role': 'user', 'content': notice})
                transcript.append({'step': step, 'kind': 'last_round_notice', 'content': notice})
                last_round_notice_sent = True
            if events is not None and events.should_stop():
                transcript.append({"step": step, "kind": "stopped", "content": "stop requested"})
                break
            try:
                empty_attempts = max(1, min(12, int(os.environ.get('PIXELBENCH_EMPTY_RESPONSE_ATTEMPTS', '4'))))
                for attempt in range(empty_attempts):
                    transcript.append({'step': step, 'kind': 'llm_request', 'attempt': attempt})
                    resp = self.llm.chat(messages, tools=file_tools(self.vision, self.surface) if file_mode else [run_code_tool(self.surface, self.vision, aligned)])
                    reply = resp.choices[0].message
                    if reply.tool_calls or (reply.content or '').strip():
                        break
                    delay = min(30, 2 ** (attempt + 1)) if attempt < empty_attempts - 1 else 0
                    usage = getattr(resp, 'usage', None)
                    transcript.append({'step': step, 'kind': 'empty_response', 'attempt': attempt,
                                       'finish_reason': getattr(resp.choices[0], 'finish_reason', None),
                                       'usage': usage.model_dump() if hasattr(usage, 'model_dump') else None,
                                       'stream_diagnostics': getattr(resp, 'stream_diagnostics', None),
                                       'retry_delay_seconds': delay})
                    if delay:
                        time.sleep(delay)
                else:
                    raise RuntimeError(f'model returned an empty response after {empty_attempts} attempts with unchanged context')

            except LongRequestCut as e:  # runaway request: keep the intermediate result, not an error
                retry_log = getattr(e, 'retry_log', None)
                usage_totals["retries"] += len(retry_log or [])
                transcript.append({"step": step, "kind": "long_request_cut", "content": f"{type(e).__name__}: {e}",
                                   "retry_log": retry_log})
                break
            except Exception as e:  # Preserve the request failure even when a canvas can be recovered.
                terminal_error = f'{type(e).__name__}: {e}'
                terminal_reason = 'llm_error'
                retry_log = getattr(e, 'retry_log', None)
                usage_totals["retries"] += len(retry_log or [])
                if events is not None:
                    events.on_llm_error(step, e)
                    transcript.append({"step": step, "kind": "llm_error", "content": f"{type(e).__name__}: {e}",
                                       "retry_log": retry_log})
                    break
                transcript.append({'step': step, 'kind': 'llm_error', 'content': f'{type(e).__name__}: {e}',
                                   'retry_log': retry_log})
                break
            msg = resp.choices[0].message
            tool_calls = msg.tool_calls or []
            # accumulate usage (token counts) from the response
            step_usage = None
            resp_usage = getattr(resp, "usage", None)
            raw_usage = getattr(resp, 'raw_usage', None)
            if raw_usage is None and resp_usage is not None and hasattr(resp_usage, 'model_dump'):
                raw_usage = resp_usage.model_dump()
            timing = getattr(resp, 'call_timing', None) or {}
            usage_totals["llm_calls"] += 1
            usage_totals["llm_seconds"] += float(timing.get("latency_s") or 0)
            usage_totals["retries"] += len(getattr(resp, 'retry_log', None) or [])
            if resp_usage is not None:
                pt = getattr(resp_usage, "prompt_tokens", None) or 0
                ct = getattr(resp_usage, "completion_tokens", None) or 0
                step_usage = {"prompt_tokens": pt, "completion_tokens": ct, "total_tokens": pt + ct,
                              **_usage_breakdown(raw_usage)}
                usage_totals["prompt_tokens"] += pt
                usage_totals["completion_tokens"] += ct
                usage_totals["total_tokens"] += pt + ct
                usage_totals["reasoning_tokens"] += step_usage["reasoning_tokens"]
                usage_totals["cached_tokens"] += step_usage["cached_tokens"]
                usage_totals["steps_with_usage"] += 1
            if events is not None:
                events.on_llm_response(step, msg.content or "", tool_calls, step_usage)
            transcript.append(
                {"step": step, "kind": "llm_response", "content": msg.content or "", "usage": step_usage,
                 "request": getattr(resp, 'request_metadata', None),
                 "response_id": getattr(resp, 'id', None), "response_model": getattr(resp, 'model', None),
                 "response_reasoning": getattr(resp, 'reasoning', None),
                 "raw_usage": raw_usage,
                 "finish_reason": getattr(resp.choices[0], 'finish_reason', None),
                 "system_fingerprint": getattr(resp, 'system_fingerprint', None),
                 "call_timing": timing or None,
                 "attempts": getattr(resp, 'attempts', None),
                 "retry_log": getattr(resp, 'retry_log', None),
                 "http_headers": getattr(resp, 'http_headers', None),
                 "stream_diagnostics": getattr(resp, 'stream_diagnostics', None),
                 "tool_calls": [tc.model_dump() if hasattr(tc, "model_dump") else tc for tc in tool_calls]}
            )
            if not tool_calls:
                transcript.append({"step": step, "kind": "final_text", "content": msg.content or ""})
                if events is not None:
                    events.on_no_tool_calls(step, msg.content or "")
                break

            messages.append(
                {
                    "role": "assistant",
                    "content": msg.content or "",
                    "tool_calls": [
                        tc.model_dump() if hasattr(tc, "model_dump") else tc for tc in tool_calls
                    ],
                }
            )
            if getattr(msg, 'responses_output', None) is not None:
                messages[-1]['_responses_output'] = msg.responses_output
            images_this_step: List[bytes] = []
            for tc in tool_calls:
                tc_id, fn, raw_args = self._tool_call_fields(tc)
                try:
                    args = json.loads(raw_args or "{}")
                except json.JSONDecodeError:
                    args = {}
                if file_mode and fn in ('write_file', 'edit_file'):
                    if mutation_steps >= max_steps:
                        messages.append({'role': 'tool', 'tool_call_id': tc_id,
                                         'content': 'Source edit budget exhausted. Run your existing file with submit=True now; run calls do not consume the edit budget.'})
                        transcript.append({'step': step, 'kind': 'write_budget_exhausted', 'name': fn})
                        continue
                    mutation_steps += 1
                    steps = mutation_steps
                elif not file_mode:
                    steps += 1
                if not file_mode and fn != 'run_code':
                    messages.append({'role': 'tool', 'tool_call_id': tc_id,
                                     'content': 'Use run_code with finish(canvas) or finish([c1, c2, ...]); submission requires explicit Canvas objects.'})
                    continue
                code = json.dumps({"tool": fn, **args}, ensure_ascii=False) if file_mode else str(args.get("code", ""))
                transcript.append({'step': step, 'kind': 'tool_call', 'id': tc_id, 'name': fn, 'arguments': args})
                if events is not None:
                    events.on_code_call(step, tc_id, code)
                tool_started = time.time()
                try:
                    result: KernelResult = session.dispatch(fn, args, budget.max_code_seconds) if file_mode else session.execute(code, timeout=budget.max_code_seconds)
                except Exception as exc:
                    terminal_error = f'{type(exc).__name__}: {exc}'
                    terminal_reason = 'execution_error'
                    transcript.append({'step': step, 'kind': 'kernel_error', 'code': code,
                                       'error': f'{type(exc).__name__}: {exc}'})
                    break
                if hook is not None and hook.enabled:
                    hook.step(step, code, result, result.images)
                tool_seconds = time.time() - tool_started
                usage_totals["tool_seconds"] += tool_seconds
                transcript.append(
                    {
                        "step": step,
                        "kind": "code",
                        "code": code,
                        "output": result.to_dict(),
                        "tool_seconds": tool_seconds,
                        "image_sha256": [hashlib.sha256(png).hexdigest() for png in result.images],
                        "mutation_steps": mutation_steps,
                    }
                )
                images_this_step.extend(result.images)
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tc_id,
                        "content": result.combined() or "(no output)",
                    }
                )
                if events is not None:
                    events.on_code_result(step, tc_id, code, result, session)
                if result.finished:  # model called finish() inside the code
                    finished = True
                    transcript.append({"step": step, "kind": "finish", "content": "program run accepted" if file_mode else "finish() called from code"})
                    break
                if not result.ok and result.timed_out:
                    break
            if finished or not session.is_alive():
                break

            if images_this_step:
                parts: List[dict] = [
                    {
                        "type": "text",
                        "text": f"Canvas observations from step {step} ({len(images_this_step)} image(s)):",
                    }
                ]
                for png in images_this_step[-8:]:
                    parts.append(
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{base64.b64encode(png).decode()}"},
                        }
                    )
                if self.vision:
                    messages.append({"role": "user", "content": parts})
                else:
                    messages.append(
                        {
                            "role": "user",
                            "content": f"[the agent rendered {len(images_this_step)} image(s) this step; "
                            "this model does not see images]",
                        }
                    )
            # host round-boundary hook (web step mode blocks here until the
            # user advances; returning False aborts the run)
            if events is not None and not events.on_round_end(step):
                transcript.append({"step": step, "kind": "stopped", "content": "round hook aborted run"})
                break
        else:
            transcript.append({"kind": "max_steps", "content": f"reached step cap {max_steps}"})

        try:
            final_frames, submission = session.extract_submission()
        except Exception as exc:
            final_frames, submission = [], {'source': 'missing', 'reason': str(exc)}
        final = final_frames[-1] if final_frames else None
        if file_mode:
            try:
                _save_messages(messages, session.root)
            except Exception as exc:  # noqa: BLE001 - evidence must never break the run
                transcript.append({'kind': 'save_messages_error', 'content': f'{type(exc).__name__}: {exc}'})
        usage_totals["mutation_steps"] = mutation_steps
        usage_totals["model_rounds"] = sum(1 for r in transcript if r.get('kind') == 'llm_response')
        submission['termination_reason'] = ('submitted' if finished else terminal_reason if terminal_error else
                                             next((r['kind'] for r in reversed(transcript) if r['kind'] in ('max_steps','stopped','final_text','long_request_cut','episode_time_cut')), 'no_submission'))
        transcript.append({'kind': 'submission', **submission})
        if hook is not None:
            hook.finish(final)
        result_obj = AgentResult(
            ok=bool(final_frames) and terminal_error is None,
            final_canvas=final,
            final_frames=final_frames,
            submission=submission,
            transcript=transcript,
            error=terminal_error or (None if final_frames else "no submitted or recoverable output; see episode events"),
            steps_used=steps,
            # Always returned: timing and call counts matter even when an endpoint reports no tokens.
            usage=usage_totals,
        )
        if events is not None:
            events.on_run_end(result_obj)
        return result_obj
