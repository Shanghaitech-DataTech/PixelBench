"""OpenAI Agents SDK trace integration.

The Agents SDK traces every ``Runner.run()`` / ``run_sync()`` call
automatically: one *trace* per run containing *agent*, *generation*
(LLM) and *function* (tool) spans.  Two observation paths are provided:

1. **Native viewer (cloud)** — with an ``OPENAI_API_KEY`` the SDK's
   default backend exporter uploads traces to the official OpenAI
   platform Traces dashboard at https://platform.openai.com/traces.
   Nothing extra is needed beyond setting ``workflow_name`` /
   ``trace_metadata`` (see :func:`build_run_config`) so runs are
   identifiable there.

2. **Local JSONL sink** — :class:`JsonlTraceProcessor` records every
   trace/span as one JSON line in the current episode's
   ``sdk_trace.jsonl``.  This works offline and with any OpenAI
   compatible endpoint (DeepSeek / vLLM / Ollama), and powers the
   local per-episode HTML viewer.

The local sink is registered once (idempotent) and routes each episode's
lines by the *current episode directory* set with
:func:`set_current_episode_dir`; the benchmark runner sets this around
``agent.run()`` (runs are sequential, so a module-level pointer is
safe).
"""
from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any, Dict, Optional

_episode_dir: Optional[Path] = None
_lock = threading.Lock()

#: metadata key used by the SDK adapter / runner to tag a run's episode
EPISODE_META_KEY = "pixelbench_episode_dir"


def set_current_episode_dir(path: Optional[str]) -> None:
    """Point the local trace sink at one episode directory."""
    global _episode_dir
    with _lock:
        _episode_dir = Path(path) if path else None


def get_current_episode_dir() -> Optional[Path]:
    with _lock:
        return _episode_dir


def register_pixelbench_tracing() -> "JsonlTraceProcessor":
    """Register the local JSONL trace sink (idempotent).

    Returns the (shared) processor instance.
    """
    from agents.tracing import add_trace_processor, get_trace_provider

    provider = get_trace_provider()
    multi = getattr(provider, "_multi_processor", None)
    existing = getattr(multi, "_processors", ()) if multi is not None else ()
    for p in existing:  # pragma: no cover - internal SDK attribute
        if isinstance(p, JsonlTraceProcessor):
            return p
    proc = JsonlTraceProcessor()
    add_trace_processor(proc)
    return proc


def build_run_config(workflow_name: str, episode_dir: str, **extra_meta: Any):
    """Build a ``RunConfig`` that tags the native trace for one episode.

    ``workflow_name`` shows up in the OpenAI Traces dashboard and in the
    local sink; ``trace_metadata`` carries the benchmark context
    (task id, agent, episode dir) on every span of the run.
    """
    from agents import RunConfig

    meta: Dict[str, Any] = {EPISODE_META_KEY: str(episode_dir)}
    meta.update(extra_meta)
    return RunConfig(workflow_name=workflow_name, trace_metadata=meta)


# ----------------------------------------------------------------------
# local JSONL sink
# ----------------------------------------------------------------------
def _span_data_export(span) -> Optional[Dict[str, Any]]:
    try:
        sd = span.span_data
        if sd is not None and hasattr(sd, "export"):
            return sd.export()
    except Exception:  # pragma: no cover
        pass
    return None


def _trace_event(item, kind: str) -> Dict[str, Any]:
    """Flatten a Trace / Span into one JSON-serializable line dict."""
    d: Dict[str, Any] = {"kind": kind}
    for attr in ("trace_id", "span_id", "parent_id", "name"):
        try:
            d[attr] = getattr(item, attr)
        except Exception:
            pass
    try:
        d["workflow_name"] = item.name
    except Exception:
        pass
    if kind.startswith("span"):
        sd = _span_data_export(item)
        if isinstance(sd, dict):
            d["span_data"] = sd
        try:
            d["error"] = item.error
        except Exception:
            pass
    try:
        meta = item.trace_metadata if kind == "trace" else item.metadata
        if isinstance(meta, dict):
            d["metadata"] = meta
    except Exception:
        pass
    # keep API keys out of the local log
    d.pop("tracing_api_key", None)
    return d


class JsonlTraceProcessor:
    """Writes every trace/span as one JSON line per episode.

    Lines go to ``<episode_dir>/sdk_trace.jsonl``; the episode dir is
    taken from :func:`get_current_episode_dir` at write time.  All
    handlers are defensive: tracing failures must never break the agent
    run.
    """

    def __init__(self, max_line_chars: int = 200_000) -> None:
        self.max_line_chars = max_line_chars
        self._fh_cache: Dict[str, Any] = {}

    # -- helpers -------------------------------------------------------
    def _target(self) -> Optional[Path]:
        base = get_current_episode_dir()
        if base is None:
            return None
        return Path(base) / "sdk_trace.jsonl"

    def _write(self, item: Any, kind: str) -> None:
        try:
            target = self._target()
            if target is None:
                return
            line = json.dumps(_trace_event(item, kind), ensure_ascii=False, default=str)
            if len(line) > self.max_line_chars:
                line = json.dumps(
                    {"kind": kind, "truncated": True, "preview": line[:2000]},
                    ensure_ascii=False,
                )
            fh = self._fh_cache.get(str(target))
            if fh is None:
                target.parent.mkdir(parents=True, exist_ok=True)
                fh = target.open("a", encoding="utf-8")
                self._fh_cache[str(target)] = fh
            fh.write(line + "\n")
            fh.flush()
        except Exception:  # pragma: no cover - tracing must never break runs
            pass

    # -- TracingProcessor interface -------------------------------------
    def on_trace_start(self, trace) -> None:
        self._write(trace, "trace_start")

    def on_trace_end(self, trace) -> None:
        self._write(trace, "trace_end")

    def on_span_start(self, span) -> None:
        self._write(span, "span_start")

    def on_span_end(self, span) -> None:
        self._write(span, "span_end")

    def shutdown(self) -> None:
        for fh in self._fh_cache.values():
            try:
                fh.close()
            except Exception:  # pragma: no cover
                pass
        self._fh_cache.clear()

    def force_flush(self) -> None:
        for fh in self._fh_cache.values():
            try:
                fh.flush()
            except Exception:  # pragma: no cover
                pass


# ----------------------------------------------------------------------
# Arize Phoenix integration (open-source, fully-local trace viewer)
# ----------------------------------------------------------------------
DEFAULT_PHOENIX_ENDPOINT = "http://127.0.0.1:6006/v1/traces"
_phoenix_instrumented = False


def enable_phoenix_tracing(endpoint: str = DEFAULT_PHOENIX_ENDPOINT) -> bool:
    """Mirror every OpenAI Agents SDK trace/span to Arize Phoenix via OTLP.

    Phoenix is an open-source, 100% local LLM observability platform
    (https://github.com/Arize-ai/phoenix) with a proper trace-tree UI.
    Run ``phoenix serve`` (or ``python -m pixelbench serve-phoenix``),
    then open the UI.  Idempotent; returns True when instrumentation is
    active, False when the packages are not installed.
    """
    global _phoenix_instrumented
    if _phoenix_instrumented:
        return True
    try:
        from openinference.instrumentation.openai_agents import OpenAIAgentsInstrumentor
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk import trace as trace_sdk
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    except ImportError:  # pragma: no cover - optional dependency
        return False
    tracer_provider = trace_sdk.TracerProvider()
    tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
    OpenAIAgentsInstrumentor().instrument(tracer_provider=tracer_provider)
    _phoenix_instrumented = True
    return True


def maybe_enable_phoenix_from_env() -> bool:
    """Enable Phoenix tracing (ON by default; opt out with
    ``PIXELBENCH_TRACE_BACKEND=off`` / ``0`` / ``false`` / ``none``)."""
    import os

    from pixelbench.phoenix_pixel import phoenix_backend_enabled

    if not phoenix_backend_enabled():
        return False
    endpoint = os.environ.get("PIXELBENCH_PHOENIX_ENDPOINT", DEFAULT_PHOENIX_ENDPOINT)
    ok = enable_phoenix_tracing(endpoint)
    if ok:
        print(f"[pixelbench] OpenAI Agents SDK traces -> Arize Phoenix ({endpoint})")
    else:
        print("[pixelbench] WARNING: Phoenix tracing requested but packages not installed; "
              "run: pip install arize-phoenix openinference-instrumentation-openai-agents")
    return ok


# ----------------------------------------------------------------------
# sample trace (preview the viewer without an API key)
# ----------------------------------------------------------------------
def write_sample_sdk_trace(episode_dir: str) -> Path:
    """Write a realistic synthetic ``sdk_trace.jsonl`` + viewer into an
    episode directory, for previewing the local trace viewer without an
    OpenAI API key or an actual SDK run.

    The event lines follow exactly the shape :class:`JsonlTraceProcessor`
    writes (kind ``trace_start`` / ``span_start`` / ``span_end`` /
    ``trace_end`` with ``span_data``).
    """
    import datetime

    from pixelbench.observe import write_process_viewer

    d = Path(episode_dir)
    odir = d / "observations"
    odir.mkdir(parents=True, exist_ok=True)

    def iso(dt):
        return dt.astimezone(datetime.timezone.utc).isoformat()

    t0 = datetime.datetime.now(datetime.timezone.utc)
    trace_id = "sample_trace_0001"
    lines = []
    lines.append({
        "kind": "trace_start", "trace_id": trace_id, "workflow_name": "pixelbench/agentic_creation/sample",
        "metadata": {"pixelbench_episode_dir": str(d), "task_id": "agentic_sample", "task_type": "agentic_creation", "agent": "sdk-repl-demo"},
    })

    def span(span_id, parent, name, data, start, dur_ms, output=None):
        sd = dict(data)
        if output is not None:
            sd["output"] = output
        start_dt = start
        end_dt = start_dt + datetime.timedelta(milliseconds=dur_ms)
        lines.append({"kind": "span_start", "span_id": span_id, "trace_id": trace_id, "parent_id": parent, "name": name, "span_data": dict(data), "started_at": iso(start_dt)})
        lines.append({"kind": "span_end", "span_id": span_id, "trace_id": trace_id, "parent_id": parent, "name": name, "span_data": sd, "started_at": iso(start_dt), "ended_at": iso(end_dt)})

    # agent span wrapping two turns
    agent_id = "span_agent"
    span(agent_id, trace_id, "PixelArtist", {"type": "agent", "name": "PixelArtist", "tools": ["run_code", "finish"]}, t0, 6200)

    # turn 1: generation + run_code
    span("span_gen_1", agent_id, "generation", {
        "type": "generation", "model": "gpt-4o",
        "input": [{"type": "message", "role": "user", "content": "Draw a small red heart on the canvas."}],
        "usage": {"input_tokens": 412, "output_tokens": 96},
    }, t0 + datetime.timedelta(milliseconds=50), 1800)
    span("span_fn_1", agent_id, "run_code", {"type": "function", "name": "run_code", "input": "outline = register_color('outline', '#2b2b2b')\nred = register_color('red', '#e0455a')\ndraw_polygon(pts, red, filled=True)"},
         t0 + datetime.timedelta(milliseconds=2000), 900, output="registered outline -> id 1\nregistered red -> id 2\npolygon: changed 112px (v3)")

    # turn 2: generation + run_code + finish
    span("span_gen_2", agent_id, "generation", {
        "type": "generation", "model": "gpt-4o",
        "input": [{"type": "message", "role": "user", "content": "Add an outline and finish."}],
        "usage": {"input_tokens": 1180, "output_tokens": 61},
    }, t0 + datetime.timedelta(milliseconds=3100), 1500)
    span("span_fn_2", agent_id, "run_code", {"type": "function", "name": "run_code", "input": "draw_polygon(pts, outline)\nrender(scale=8)"},
         t0 + datetime.timedelta(milliseconds=4800), 700, output="polygon: changed 40px (v4)\nrendered 32x32 canvas at scale 8")
    span("span_fn_3", agent_id, "finish", {"type": "function", "name": "finish"},
         t0 + datetime.timedelta(milliseconds=5700), 300, output="drawing marked complete")

    lines.append({"kind": "trace_end", "trace_id": trace_id, "workflow_name": "pixelbench/agentic_creation/sample",
                  "metadata": {"task_id": "agentic_sample", "task_type": "agentic_creation", "agent": "sdk-repl-demo"}})

    with (odir / "sdk_trace.jsonl").open("w", encoding="utf-8") as fh:
        for l in lines:
            fh.write(json.dumps(l, ensure_ascii=False) + "\n")

    if not (d / "record.json").exists():
        (d / "record.json").write_text(json.dumps({
            "task_id": "agentic_sample", "task_type": "agentic_creation", "agent": "sdk-repl-demo",
            "ok": True, "steps": 2, "metrics": {}, "images": {"final": "final.png"},
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    if not (d / "trace.jsonl").exists():
        (d / "trace.jsonl").write_text(json.dumps({"kind": "sdk", "final_text": "drawing marked complete"}) + "\n", encoding="utf-8")

    write_process_viewer(d)
    return d / "process.html"
