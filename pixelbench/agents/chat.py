"""Thin OpenAI-compatible chat client used by the agents.

Everything goes through ``openai`` so any OpenAI-compatible endpoint
(base_url) works: OpenAI, DeepSeek, vLLM, Ollama, etc.

Two request shapes are supported (``api_format``):

* ``"completions"`` (default) — the classic ``POST /chat/completions``.
  Works with nearly every OpenAI-compatible gateway.
* ``"responses"`` — the newer OpenAI Responses API (``POST /responses``).
  Some gateways expose models that only accept this shape; the returned
  object is normalized back into the chat-completions shape so the agent
  loops above are format-agnostic.
* ``"auto"`` — try ``completions`` first and transparently fall back to
  ``responses`` when the gateway reports that the model does not support
  the completions endpoint (e.g. 404 / "must use the Responses API").
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Dict, List, Optional


class LLMError(RuntimeError):
    """Request failure; ``retry_log`` lists every failed attempt."""

    def __init__(self, *args, retry_log: Optional[List[dict]] = None):
        super().__init__(*args)
        self.retry_log = retry_log or []


class LongRequestCut(LLMError):
    """A single request ran past ``request_cut_s``; the episode keeps its intermediate result
    instead of retrying the request (protocol: no time is spent on runaway requests)."""


def _dump(obj: Any) -> Any:
    """JSON-safe copy of an SDK object (pydantic model, namespace or plain)."""
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if isinstance(obj, SimpleNamespace):
        return dict(vars(obj))
    return obj


def _headers(raw: Any) -> Optional[Dict[str, str]]:
    """Response headers minus cookies; auth never appears in responses."""
    try:
        return {k: v for k, v in raw.headers.items() if k.lower() != "set-cookie"}
    except Exception:  # noqa: BLE001
        return None


def _request_digest(kwargs: dict) -> dict:
    body = {k: v for k, v in kwargs.items() if k not in ("extra_headers",)}
    blob = json.dumps(body, sort_keys=True, ensure_ascii=False, default=str).encode()
    return {"request_sha256": hashlib.sha256(blob).hexdigest(), "request_bytes": len(blob),
            "n_messages": len(kwargs.get("messages") or kwargs.get("input") or [])}


@dataclass
class ChatMessage:
    role: str
    content: Any
    tool_calls: Optional[List[dict]] = None
    tool_call_id: Optional[str] = None
    name: Optional[str] = None

    def to_dict(self) -> dict:
        d: dict = {"role": self.role, "content": self.content}
        if self.tool_calls:
            d["tool_calls"] = self.tool_calls
        if self.tool_call_id:
            d["tool_call_id"] = self.tool_call_id
        if self.name:
            d["name"] = self.name
        return d


# ----------------------------------------------------------------------
# tiny response shims so the Responses-API result exposes the same
# ``resp.choices[0].message`` surface the completions path returns
# (agents only read .content, .tool_calls, and tc.function.*/model_dump())
# ----------------------------------------------------------------------
class _ToolCallShim:
    def __init__(self, tid: str, name: str, arguments: str):
        self.id = tid
        self.function = type("F", (), {"name": name, "arguments": arguments})()

    def model_dump(self) -> dict:
        return {
            "id": self.id,
            "type": "function",
            "function": {"name": self.function.name, "arguments": self.function.arguments},
        }


class _MessageShim:
    def __init__(self, content: Optional[str], tool_calls: Optional[List[_ToolCallShim]] = None):
        self.content = content
        self.tool_calls = tool_calls


class _ChoiceShim:
    def __init__(self, message: _MessageShim, finish_reason: Optional[str] = None):
        self.message = message
        self.finish_reason = finish_reason


class _ResponseShim:
    def __init__(self, message: _MessageShim, usage: Any = None, finish_reason: Optional[str] = None):
        self.choices = [_ChoiceShim(message, finish_reason)]
        self.usage = usage


def _tc_id(tc: Any) -> str:
    return tc.id if hasattr(tc, "id") else tc["id"]


def _tc_name(tc: Any) -> str:
    if hasattr(tc, "function"):
        fn = tc.function
        return fn.name if hasattr(fn, "name") else fn["name"]
    return tc["function"]["name"]


def _tc_args(tc: Any) -> str:
    if hasattr(tc, "function"):
        fn = tc.function
        return fn.arguments if hasattr(fn, "arguments") else fn["arguments"]
    return tc["function"]["arguments"]


def _to_responses_content(content: Any) -> List[dict]:
    """Convert a completions-style content (str or part list) to Responses input items."""
    if isinstance(content, str):
        return [{"type": "input_text", "text": content}]
    if isinstance(content, list):
        out: List[dict] = []
        for part in content:
            if not isinstance(part, dict):
                out.append({"type": "input_text", "text": str(part)})
                continue
            ptype = part.get("type")
            if ptype in (None, "text"):
                out.append({"type": "input_text", "text": str(part.get("text", ""))})
            elif ptype == "image_url":
                url = part.get("image_url")
                detail = url.get("detail") if isinstance(url, dict) else None
                if isinstance(url, dict):
                    url = url.get("url")
                image = {"type": "input_image", "image_url": url}
                if detail is not None:
                    image["detail"] = detail
                out.append(image)
            else:
                out.append(part)
        return out
    return [{"type": "input_text", "text": str(content or "")}]


def _to_responses_input(messages: List[dict]) -> List[dict]:
    """Convert completions-style messages to a Responses-API ``input`` array."""
    items: List[dict] = []
    for m in messages:
        role = m.get("role")
        content = m.get("content")
        if role == "system":
            items.append({"role": role, "content": _to_responses_content(content)})
        elif role == "user":
            items.append({"role": "user", "content": _to_responses_content(content)})
        elif role == "assistant":
            # Replay native output items, including encrypted reasoning and
            # message channels, without duplicating their function calls.
            if m.get("_responses_output") is not None:
                items.extend(m["_responses_output"])
                continue
            if content:
                items.append({"role": "assistant", "content": content})
            for tc in m.get("tool_calls") or []:
                items.append(
                    {
                        "call_id": _tc_id(tc),
                        "type": "function_call",
                        "name": _tc_name(tc),
                        "arguments": _tc_args(tc),
                    }
                )
        elif role == "tool":
            out = content if isinstance(content, str) else json.dumps(content, ensure_ascii=False)
            items.append(
                {"type": "function_call_output",
                 "call_id": m.get("tool_call_id"), "output": out}
            )
        else:  # developer / other — pass through as-is
            items.append(m)
    return items


def _to_responses_tools(tools: Optional[List[dict]]) -> List[dict]:
    """Completions tools -> Responses-API tools (flat function schema)."""
    out: List[dict] = []
    for t in tools or []:
        if t.get("type") != "function":
            out.append(t)
            continue
        fn = t.get("function", {})
        out.append(
            {
                "type": "function",
                "name": fn.get("name", ""),
                "description": fn.get("description", ""),
                "parameters": fn.get("parameters", {"type": "object", "properties": {}}),
                "strict": False,
            }
        )
    return out


def _should_fallback_to_responses(e: LLMError) -> bool:
    """True when the completions error strongly suggests the model wants the
    Responses API (404 on the endpoint / explicit 'must use the Responses API')."""
    msg = str(e).lower()
    status = None
    for attr in ("status_code", "status"):
        if hasattr(e, attr):
            try:
                status = int(getattr(e, attr))
                break
            except (TypeError, ValueError):
                pass
    if status == 404:
        return True
    return any(
        k in msg
        for k in (
            "must use the responses api",
            "responses api",
            "does not support the chat",
            "not supported",
        )
    )


class LLMClient:
    def __init__(
        self,
        model: str,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        api_format: str = "completions",
        stream: bool = False,
        max_retries: int = 4,
        retry_backoff: float = 2.0,
        extra_body: Optional[dict] = None,
        trailing_user: bool = False,
        timeout: float = 600.0,
        stream_include_usage: bool = True,
        request_cut_s: Optional[float] = None,
        episode_cut_s: Optional[float] = None,
    ) -> None:
        # Wall-clock caps (seconds). A request past request_cut_s raises LongRequestCut (no
        # retry); the agent stops an episode past episode_cut_s. Both keep the intermediate result.
        self.request_cut_s = request_cut_s
        self.episode_cut_s = episode_cut_s
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.extra_headers = extra_headers
        self.extra_body = extra_body
        self.stream = stream
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff
        self.trailing_user = trailing_user
        # Ask streaming gateways for a final usage chunk; disabled automatically
        # (and recorded) if a gateway rejects the field.
        self.stream_include_usage = stream_include_usage
        if api_format not in ("completions", "responses", "auto"):
            raise ValueError(f"api_format must be 'completions'|'responses'|'auto', got {api_format!r}")
        self.api_format = api_format
        api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not api_key and base_url is None:
            raise LLMError("no API key: pass api_key= or set OPENAI_API_KEY")
        import openai

        kwargs: dict = {"api_key": api_key or "not-needed"}
        if base_url:
            kwargs["base_url"] = base_url
        if extra_headers:
            kwargs["default_headers"] = extra_headers
        # stream requests must not hang forever when a gateway stalls mid-
        # response: give the client a generous cap and let _chat_with_retry
        # fall back on a timeout (rather than blocking the worker forever).
        kwargs.setdefault("timeout", min(timeout, request_cut_s) if request_cut_s else timeout)
        if request_cut_s:
            # The SDK would otherwise re-send a timed-out request on its own (default 2 times).
            kwargs["max_retries"] = 0
        self.client = openai.OpenAI(**kwargs)

    # -- completions path ----------------------------------------------
    def _chat_completions(
        self,
        messages: List[dict],
        tools: Optional[List[dict]] = None,
        response_format: Optional[dict] = None,
        stream: bool = False,
    ) -> Any:
        kwargs: dict = {
            "model": self.model,
            "messages": [{k: v for k, v in m.items() if not k.startswith('_responses_')} for m in messages],
        }
        if self.temperature is not None:
            kwargs["temperature"] = self.temperature
        if tools:
            kwargs["tools"] = tools
        if self.max_tokens:
            kwargs["max_tokens"] = self.max_tokens
        if response_format:
            kwargs["response_format"] = response_format
        extra = {k: v for k, v in (self.extra_body or {}).items() if v is not None}
        if extra:
            kwargs["extra_body"] = extra
        try:
            response = self._chat_with_retry(kwargs, stream)
            response.request_metadata = {**self._request_metadata(kwargs, 'completions', stream),
                                         **_request_digest(kwargs)}
            return response
        except LLMError:
            raise
        except Exception as e:  # pragma: no cover
            raise LLMError(f"chat completion failed: {e}") from e

    @staticmethod
    def _retryable(e: Exception) -> bool:
        """Return True if this LLM error is worth retrying (network / 5xx /
        connection / timeout / 429 rate-limit), False for deterministic
        client errors (auth / schema)."""
        msg = f"{type(e).__name__}: {e}"
        low = msg.lower()
        # deterministic / auth / schema errors: don't retry
        for marker in (
            "400", "401", "403", "404", "422",
            "invalid", "bad request", "authentication", "not found",
            "does not support", "not supported", "no such model",
        ):
            if marker in low:
                return False
        # everything else (connection, timeout, 5xx, 429 rate-limit,
        # upstream failures) is retryable
        return True

    def _chat_with_retry(self, kwargs: dict, stream: bool) -> Any:
        last: Optional[Exception] = None
        retry_log: List[dict] = []
        for attempt in range(self.max_retries + 1):
            started = time.time()
            try:
                if not stream:
                    raw = self.client.chat.completions.with_raw_response.create(**kwargs)
                    response = raw.parse()
                    response.http_headers = _headers(raw)
                    msg = response.choices[0].message if getattr(response, "choices", None) else None
                    extra = getattr(msg, "model_extra", None) or {}
                    reasoning = extra.get("reasoning_content") or extra.get("reasoning")
                    if reasoning:
                        response.reasoning = {"content": reasoning}
                    response.raw_usage = _dump(getattr(response, "usage", None))
                    ended = time.time()
                    response.call_timing = {"started": started, "ended": ended,
                                            "latency_s": ended - started, "ttft_s": None}
                else:
                    response = self._chat_completions_stream(None, None, None, kwargs)
                    response.call_timing["started"] = started
                    response.call_timing["latency_s"] = response.call_timing["ended"] - started
                    if response.call_timing.get("first_chunk") is not None:
                        response.call_timing["ttft_s"] = response.call_timing["first_chunk"] - started
                response.retry_log = retry_log
                response.attempts = attempt + 1
                return response
            except Exception as e:  # noqa: BLE001
                last = e
                text = f"{type(e).__name__}: {e}"
                if isinstance(e, LongRequestCut) or (self.request_cut_s and "timeout" in type(e).__name__.lower()):
                    retry_log.append({"attempt": attempt, "started": started, "ended": time.time(),
                                      "error": text[:2000], "action": "long_request_cut"})
                    raise LongRequestCut(f"request exceeded {self.request_cut_s:.0f}s: {text[:300]}",
                                         retry_log=retry_log) from e
                if stream and self.stream_include_usage and "stream_options" in text.lower():
                    self.stream_include_usage = False
                    retry_log.append({"attempt": attempt, "started": started, "ended": time.time(),
                                      "error": text[:2000], "action": "disable_stream_include_usage"})
                    continue
                retryable = self._retryable(e) and attempt < self.max_retries
                delay = min(60.0, self.retry_backoff * (2 ** attempt)) if retryable else 0
                retry_log.append({"attempt": attempt, "started": started, "ended": time.time(),
                                  "error": text[:2000], "status": getattr(e, "status_code", None),
                                  "retry_delay_s": delay if retryable else None})
                if not retryable:
                    break
                time.sleep(delay)
        raise LLMError(f"chat completion failed: {last}", retry_log=retry_log) from last

    def _chat_completions_stream(
        self,
        messages: List[dict],
        tools: Optional[List[dict]],
        response_format: Optional[dict],
        kwargs: dict,
    ) -> Any:
        """Streaming chat completion, aggregated into a completions-style
        response (content + tool_calls + finish_reason).  This keeps REPL
        tool-call parsing identical whether or not the endpoint requires
        streaming.
        """
        stream_started = time.time()
        stream_kwargs = dict(kwargs, stream=True)
        if self.stream_include_usage:
            stream_kwargs["stream_options"] = {"include_usage": True}
        raw = self.client.chat.completions.with_raw_response.create(**stream_kwargs)
        http_headers = _headers(raw)
        stream = raw.parse()
        first_chunk = None
        system_fingerprint = None
        content_parts: List[str] = []
        # tool_calls arrive split by index; accumulate fragments per index
        tool_frags: Dict[int, Dict[str, str]] = {}
        finish_reason: Optional[str] = None
        usage = None
        chunk_count = 0
        reasoning_parts: List[str] = []
        response_id = response_model = None
        for chunk in stream:
            if first_chunk is None:
                first_chunk = time.time()
            if self.request_cut_s and time.time() - stream_started > self.request_cut_s:
                try:
                    stream.close()
                except Exception:  # noqa: BLE001
                    pass
                raise LongRequestCut(f"stream exceeded {self.request_cut_s:.0f}s after {chunk_count} chunks")
            system_fingerprint = getattr(chunk, 'system_fingerprint', None) or system_fingerprint
            response_id = getattr(chunk, 'id', None) or response_id
            response_model = getattr(chunk, 'model', None) or response_model
            chunk_count += 1
            # streaming gateways may report usage on the final chunk
            chunk_usage = getattr(chunk, "usage", None)
            if chunk_usage is not None:
                usage = chunk_usage
            if not getattr(chunk, "choices", None):
                continue
            choice = chunk.choices[0]
            if choice.finish_reason:
                finish_reason = choice.finish_reason
            delta = getattr(choice, "delta", None)
            if delta is None:
                continue
            reasoning_parts.append(getattr(delta, 'reasoning_content', None) or getattr(delta, 'reasoning', None) or '')
            if getattr(delta, "content", None):
                content_parts.append(delta.content)
            for tc in getattr(delta, "tool_calls", None) or []:
                idx = tc.index
                frag = tool_frags.setdefault(idx, {"id": "", "name": "", "args": ""})
                if tc.id:
                    frag["id"] += tc.id
                fn = getattr(tc, "function", None)
                if fn is not None:
                    if fn.name:
                        frag["name"] += fn.name
                    if fn.arguments:
                        frag["args"] += fn.arguments
        tool_calls: List[_ToolCallShim] = []
        for idx in sorted(tool_frags):
            f = tool_frags[idx]
            tool_calls.append(_ToolCallShim(f["id"] or f"call_{idx}", f["name"], f["args"] or "{}"))
        content = "".join(content_parts) or None
        message = _MessageShim(content, tool_calls or None)
        response = _ResponseShim(message, usage=usage, finish_reason=finish_reason)
        response.id, response.model = response_id, response_model
        reasoning_text = ''.join(reasoning_parts)
        reasoning_chars = len(reasoning_text)
        if reasoning_text:
            response.reasoning = {'content': reasoning_text}
        response.stream_diagnostics = {'chunks': chunk_count, 'reasoning_chars': reasoning_chars,
                                       'content_chars': len(content or ''), 'tool_calls': len(tool_calls),
                                       'include_usage_requested': 'stream_options' in stream_kwargs,
                                       'usage_received': usage is not None}
        response.raw_usage = _dump(usage)
        response.http_headers = http_headers
        response.system_fingerprint = system_fingerprint
        response.call_timing = {'first_chunk': first_chunk, 'ended': time.time()}
        return response

    # -- responses path ------------------------------------------------
    def _chat_responses(
        self,
        messages: List[dict],
        tools: Optional[List[dict]] = None,
        response_format: Optional[dict] = None,
        stream: bool = False,
    ) -> Any:
        kwargs: dict = {
            "model": self.model,
            "input": _to_responses_input(messages),
            "store": False,
            "include": ["reasoning.encrypted_content"],
        }
        if self.temperature is not None:
            kwargs["temperature"] = self.temperature
        extra = dict(self.extra_body or {})
        extra = {k: v for k, v in extra.items() if v is not None}
        effort = extra.pop("reasoning_effort", None)
        if effort is not None:
            reasoning = dict(extra.get("reasoning") or {})
            if reasoning.get("effort", effort) != effort:
                raise LLMError("conflicting reasoning effort settings")
            reasoning["effort"] = effort
            extra["reasoning"] = reasoning
        if extra:
            kwargs["extra_body"] = extra
        if tools:
            kwargs["tools"] = _to_responses_tools(tools)
        if self.max_tokens:
            kwargs["max_output_tokens"] = self.max_tokens
        if response_format and response_format.get("type") == "json_object":
            kwargs["text"] = {"format": {"type": "json_object"}}
        retry_log: List[dict] = []
        call_started = None
        for attempt in range(self.max_retries + 1):
            call_started = time.time()
            try:
                if stream:
                    raw = None
                    with self.client.responses.create(**kwargs, stream=True) as events:
                        for event in events:
                            if event.type in ('response.completed', 'response.incomplete'):
                                raw = event.response
                            elif event.type in ('error', 'response.failed'):
                                raise LLMError(f"Responses stream failed: {event.type}")
                    if raw is None:
                        raise LLMError('Responses stream ended without a terminal response')
                else:
                    raw = self.client.responses.create(**kwargs)
                break
            except Exception as e:
                retryable = self._retryable(e) and attempt < self.max_retries
                delay = min(30, self.retry_backoff * (2 ** attempt)) if retryable else None
                retry_log.append({"attempt": attempt, "started": call_started, "ended": time.time(),
                                  "error": f"{type(e).__name__}: {e}"[:2000],
                                  "status": getattr(e, "status_code", None), "retry_delay_s": delay})
                if not retryable:
                    raise LLMError(f"responses API failed: {e}", retry_log=retry_log) from e
                time.sleep(delay)

        # normalize output[] into a completions-style response
        text_parts: List[str] = []
        tool_calls: List[_ToolCallShim] = []
        finish_reason: Optional[str] = None
        for item in getattr(raw, "output", []) or []:
            itype = getattr(item, "type", None)
            if itype == "message":
                for part in getattr(item, "content", []) or []:
                    if getattr(part, "type", None) == "output_text":
                        text_parts.append(getattr(part, "text", "") or "")
            elif itype == "function_call":
                tool_calls.append(
                    _ToolCallShim(
                        getattr(item, "call_id", None),
                        getattr(item, "name", ""),
                        getattr(item, "arguments", "{}"),
                    )
                )
        content = "".join(text_parts) or None
        message = _MessageShim(content, tool_calls or None)
        message.responses_output = [item.model_dump(exclude_none=True) for item in raw.output]
        raw_usage = getattr(raw, 'usage', None)
        usage = None
        if raw_usage is not None:
            usage = SimpleNamespace(prompt_tokens=raw_usage.input_tokens,
                                    completion_tokens=raw_usage.output_tokens,
                                    total_tokens=raw_usage.total_tokens)
        response = _ResponseShim(message, usage=usage, finish_reason=getattr(raw, 'status', None))
        response.id, response.model = raw.id, raw.model
        response.raw_usage = raw_usage.model_dump() if raw_usage else None
        response.reasoning = raw.reasoning.model_dump() if getattr(raw, 'reasoning', None) else None
        response.request_metadata = {**self._request_metadata(kwargs, 'responses', stream),
                                     **_request_digest(kwargs)}
        ended = time.time()
        response.call_timing = {"started": call_started, "ended": ended,
                                "latency_s": ended - call_started, "ttft_s": None}
        response.retry_log = retry_log
        response.attempts = len(retry_log) + 1
        return response

    def _request_metadata(self, kwargs: dict, api_format: str, stream: bool) -> dict:
        """Non-secret request evidence; never record auth headers or keys."""
        body = {**kwargs, **kwargs.get('extra_body', {})}
        return {"api_format": api_format, "base_url": str(self.client.base_url),
                "model": body.get('model'), "stream": stream,
                "instruction_roles": [m['role'] for m in body.get('input', body.get('messages', []))
                                      if m.get('role') in ('system', 'developer')],
                "instruction_content_types": [type(m.get('content')).__name__
                                              for m in body.get('input', body.get('messages', []))
                                              if m.get('role') in ('system', 'developer')],
                "temperature": body.get('temperature'),
                "reasoning": body.get('reasoning'), "reasoning_effort": body.get('reasoning_effort'),
                "max_tokens": body.get('max_tokens', body.get('max_output_tokens')),
                "input_images": sum(1 for m in body.get('input', body.get('messages', []))
                                    if isinstance(m.get('content'), list) for part in m['content']
                                    if part.get('type') in ('input_image', 'image_url')),
                "reasoning_items": sum(m.get('type') == 'reasoning' for m in body.get('input', []))}

    # -- public entry --------------------------------------------------
    def chat(
        self,
        messages: List[dict],
        tools: Optional[List[dict]] = None,
        response_format: Optional[dict] = None,
        stream: Optional[bool] = None,
    ) -> Any:
        if stream is None:
            stream = self.stream
        # Some endpoints reject a conversation that ends on an assistant/tool
        # message ("must end with a user message"). When enabled, append a
        # lightweight user turn so the message list always ends on "user".
        if self.trailing_user and messages and messages[-1].get("role") != "user":
            messages = messages + [{"role": "user", "content": "[continue]"}]
        if self.api_format == "responses":
            return self._chat_responses(messages, tools, response_format, stream=stream)
        try:
            return self._chat_completions(messages, tools, response_format, stream=stream)
        except LLMError as e:  # pragma: no cover - depends on gateway
            if self.api_format == "auto" and _should_fallback_to_responses(e):
                return self._chat_responses(messages, tools, response_format, stream=stream)
            raise

    @staticmethod
    def from_config(cfg: dict) -> "LLMClient":
        return LLMClient(
            model=cfg.get("model", "gpt-4o"),
            base_url=cfg.get("base_url"),
            api_key=cfg.get("api_key"),
            temperature=cfg.get("temperature", 0.7),
            max_tokens=cfg.get("max_tokens"),
            api_format=cfg.get("api_format", "completions"),
            stream=bool(cfg.get("stream", False)),
            extra_body=cfg.get("extra_body"),
            extra_headers=cfg.get("extra_headers"),
            trailing_user=bool(cfg.get("trailing_user", False)),
            max_retries=cfg.get("max_retries", 4),
            timeout=cfg.get("timeout", 600.0),
            stream_include_usage=bool(cfg.get("stream_include_usage", True)),
            request_cut_s=cfg.get("request_cut_s"),
            episode_cut_s=cfg.get("episode_cut_s"),
        )
