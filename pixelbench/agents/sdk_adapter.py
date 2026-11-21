"""Optional OpenAI Agents SDK adapter (experimental).

Limitation: the Agents SDK returns tool results as plain strings, so
rendered images cannot be injected into the model's context.  Use
:class:`REPLAgent` (custom loop) when multimodal observation matters;
this adapter is for setups that prefer the SDK and can work from text
feedback alone.

Tracing: the SDK traces every run natively.  With an ``OPENAI_API_KEY``
the traces appear in the official OpenAI platform Traces dashboard
(https://platform.openai.com/traces); additionally
:mod:`pixelbench.tracing` records every trace/span to the episode's
``sdk_trace.jsonl`` (works offline and with any OpenAI-compatible
endpoint), which the per-episode HTML viewer renders.
"""
from __future__ import annotations

import os
from typing import List, Optional

from pixelbench.agents.base import Agent, AgentResult, Budget
from pixelbench.agents.repl_agent import (
    DEFAULT_SYSTEM_PROMPT_TEXT,
    build_episode_user_content,
)
from pixelbench.repl.kernel import KernelSession
from pixelbench.tasks.specs import TaskSpec


def build_run_code_description(aligned: bool = False) -> str:
    """The ``run_code`` description for the SDK adapter.

    The SDK returns tool results as plain strings and cannot feed images
    back to the model, so the description is always the text-only variant
    (no 'image' observation modes, no render()).
    """
    from pixelbench.repl.tools import tool_docs
    if aligned:
        from pixelbench.repl.skill_docs import skill_tool_docs
        return skill_tool_docs(vision=False)

    return tool_docs("full", vision=False)


class AgentsSdkReplAgent(Agent):
    """openai-agents SDK based REPL agent."""

    requires_repl = True

    def __init__(
        self,
        name: str = "sdk-repl",
        model: str = "gpt-4o",
        system_prompt: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        temperature: float = 0.7,
    ) -> None:
        self.name = name
        self.model = model
        self.system_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT_TEXT
        self._custom_system_prompt = system_prompt is not None
        self.api_key = api_key
        self.base_url = base_url
        self.temperature = temperature
        self._session: Optional[KernelSession] = None
        self._budget: Optional[Budget] = None

    def _configure_sdk_client(self) -> Optional[str]:
        """Point the SDK's default OpenAI client at a custom endpoint
        (DeepSeek / vLLM / Ollama ...).  Returns an error string or None."""
        if not self.base_url and not self.api_key:
            return None  # use SDK defaults (OPENAI_API_KEY / official endpoint)
        try:
            import os

            from openai import AsyncOpenAI

            from agents import set_default_openai_client

            client = AsyncOpenAI(
                api_key=self.api_key or os.environ.get("OPENAI_API_KEY"),
                base_url=self.base_url,
            )
            set_default_openai_client(client)
            return None
        except Exception as e:  # pragma: no cover
            return f"could not configure SDK OpenAI client: {e}"

    def _run_code(self, code: str) -> str:
        assert self._session is not None and self._budget is not None
        r = self._session.execute(code, timeout=self._budget.max_code_seconds)
        self._finished = self._finished or r.finished
        self._transcript.append({'kind': 'code', 'code': code, 'output': r.to_dict()})
        text = r.combined() or "(no output)"
        if r.images:
            text += f"\n[rendered {len(r.images)} image(s); the SDK adapter cannot show them to the model]"
        return text

    def _file_action(self, name, args):
        self._transcript.append({'kind': 'tool_call', 'name': name, 'arguments': args})
        r = self._session.dispatch(name, args, self._budget.max_code_seconds)
        self._finished = self._finished or r.finished
        self._transcript.append({'kind': 'code', 'tool': name, 'arguments': args, 'output': r.to_dict()})
        return r.combined() or '(no output)'

    def _write_file(self, path: str, content: str) -> str:
        return self._file_action('write_file', dict(path=path, content=content))

    def _edit_file(self, path: str, old: str, new: str) -> str:
        return self._file_action('edit_file', dict(path=path, old=old, new=new))

    def _read_file(self, path: str) -> str:
        return self._file_action('read_file', dict(path=path))

    def _list_files(self) -> str:
        return self._file_action('list_files', {})

    def _run_file(self, path: str = 'main.py', submit: bool = False) -> str:
        return self._file_action('run', dict(path=path, submit=submit))

    def run(self, task: TaskSpec, session: Optional[KernelSession], budget: Budget) -> AgentResult:
        try:
            from agents import Agent as SDKAgent
            from agents import Runner, function_tool, RunHooks
            from agents.agent import ToolsToFinalOutputResult
        except ImportError as e:  # pragma: no cover
            return AgentResult(ok=False, error=f"openai-agents not installed: {e}")
        if session is None:
            return AgentResult(ok=False, error="AgentsSdkReplAgent requires a kernel session")
        err = self._configure_sdk_client()
        if err:
            return AgentResult(ok=False, error=err)
        self._session = session
        self._budget = budget
        self._finished = False
        from pixelbench.repl.event_log import EventLog
        self._transcript = EventLog(session.root / 'events.jsonl' if hasattr(session, 'root') else None)
        from pixelbench.repl.skill_runtime import uses_skill
        from pixelbench.repl.skill_docs import skill_system_prompt, skill_user_content
        aligned = uses_skill(task)
        from pixelbench.repl.file_session import FileSession
        from pixelbench.repl.file_docs import file_prompt, file_tools, file_submission_instructions
        file_mode = isinstance(session, FileSession)
        owner = self
        class LastRoundHook(RunHooks):
            rounds = 0
            async def on_llm_start(self, context, agent, system_prompt, input_items):
                self.rounds += 1
                if self.rounds == budget.max_steps:
                    notice = (f"This is your LAST ROUND. Regardless of completeness, call finish inside run_code now "
                              f"with exactly {max(1, task.num_frames or 1)} Canvas objects in task order.")
                    if file_mode:
                        notice = file_submission_instructions(task, last_round=True)
                    input_items.append({'role': 'user', 'content': notice})
                    owner._transcript.append({'kind': 'last_round_notice', 'content': notice})
        async def stop_after_submission(context, results):
            return ToolsToFinalOutputResult(is_final_output=owner._finished, final_output='submitted' if owner._finished else None)
        sdk_agent = SDKAgent(
            name="PixelArtist",
            tool_use_behavior=stop_after_submission,
            instructions=(skill_system_prompt(False) if aligned and not self._custom_system_prompt
                          else self.system_prompt),
            model=self.model,
            tools=[
                function_tool(
                    self._run_code,
                    name_override="run_code",
                    # the SDK returns tool results as plain strings and cannot
                    # feed images back to the model: always use the text-only docs
                    description_override=build_run_code_description(aligned),
                ),
            ],
        )
        if file_mode:
            sdk_agent.instructions = file_prompt(False) + ('\n' + self.system_prompt if self._custom_system_prompt else '')
            methods = [self._write_file, self._edit_file, self._read_file, self._list_files, self._run_file]
            sdk_agent.tools = [function_tool(method, name_override=spec['function']['name'],
                               description_override=spec['function']['description'])
                               for method, spec in zip(methods, file_tools(False))]
        content = (skill_user_content(task) if aligned else
                   build_episode_user_content(task, reference_png=None))
        text = "\n".join(p["text"] for p in content if isinstance(p.get("text"), str))

        if file_mode:
            text += '\n' + file_submission_instructions(task)

        # Native OpenAI Agents SDK tracing: tag the run so it is
        # identifiable in the OpenAI Traces dashboard and captured to the
        # episode's sdk_trace.jsonl by the local JSONL processor.
        from pixelbench import tracing

        tracing.register_pixelbench_tracing()
        episode_dir = tracing.get_current_episode_dir()
        run_config = None
        if episode_dir is not None:
            run_config = tracing.build_run_config(
                f"pixelbench/{task.task_type}/{task.id}",
                episode_dir=str(episode_dir),
                task_id=task.id,
                task_type=task.task_type,
                agent=self.name,
            )
        terminal_error = None
        try:
            result = Runner.run_sync(sdk_agent, input=text, run_config=run_config,
                                     max_turns=budget.max_steps, hooks=LastRoundHook())
            self._transcript.append({'kind': 'sdk', 'final_text': result.final_output})
        except Exception as exc:
            terminal_error = f'{type(exc).__name__}: {exc}'
            self._transcript.append({'kind': 'sdk_error', 'error': terminal_error})
        try:
            outputs, submission = session.extract_submission()
        except Exception as exc:
            outputs, submission = [], {'source': 'missing', 'reason': str(exc)}
        self._transcript.append({'kind': 'submission', **submission})
        return AgentResult(ok=bool(outputs) and terminal_error is None, final_canvas=outputs[-1] if outputs else None,
                           final_frames=outputs, submission=submission, transcript=self._transcript,
                           error=terminal_error or (None if outputs else 'could not recover output'),
                           steps_used=sum(row['kind'] == 'code' for row in self._transcript))
