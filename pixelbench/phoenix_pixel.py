"""Phoenix pixel-art trace plugin.

Emits PixelBench REPL episodes as OpenInference OTel spans so the Arize
Phoenix UI (http://127.0.0.1:6006) shows, for every episode, the model
steps and tools *with the evolving pixel-art canvas rendered inline*.

Trace layout per episode::

    episode (AGENT, name = task id)
    ├── LLM step 1  (LLM, input = code + canvas frame as image part)
    │   └── run_code (TOOL, input = code, output = result text)
    ├── LLM step 2 ...
    └── ...

Images ride on the LLM input messages (``message_content`` image parts),
which is the one path the Phoenix frontend renders inline.

Two entry points:

* ``replay_run_to_phoenix(run_dir)`` — replay already-finished episodes
  from disk (``observations/turns.jsonl`` + ``trace.jsonl``) into Phoenix.
  CLI: ``python -m pixelbench phoenix-replay --run outputs/showcase_128``
* ``LivePhoenixHook`` — emit spans live while a REPLAgent runs (enabled
  with ``PIXELBENCH_TRACE_BACKEND=phoenix``; the hook is defensive and
  never breaks the agent loop).

All phoenix/openinference imports are optional and lazy: if the packages
or the server are missing, every function degrades to a no-op.
"""
from __future__ import annotations

import base64
import json
import os
import threading
from pathlib import Path
from typing import Any, Dict, List, Optional

# OTLP endpoint served by `phoenix serve` itself (HTTP OTLP on the UI port)
DEFAULT_ENDPOINT = os.environ.get("PIXELBENCH_PHOENIX_ENDPOINT", "http://127.0.0.1:6006/v1/traces")
DEFAULT_PROJECT = os.environ.get("PIXELBENCH_PHOENIX_PROJECT", "pixelbench-showcase")

_OTEL_READY = False
_OTEL_FAILED = False
_tracer = None
_lock = threading.Lock()


def phoenix_backend_enabled() -> bool:
    """Phoenix live tracing is ON **by default**.

    Explicitly disable with ``PIXELBENCH_TRACE_BACKEND=off`` (also
    accepted: ``0`` / ``false`` / ``none`` / empty string).  Anything
    else — unset, ``phoenix``, ``1``, ``true`` — enables it.
    """
    v = os.environ.get("PIXELBENCH_TRACE_BACKEND", "phoenix").strip().lower()
    return v not in ("", "off", "0", "false", "none", "no", "disabled")


# ----------------------------------------------------------------------
# otel bootstrap
# ----------------------------------------------------------------------
def _import_otel():
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from openinference.semconv.resource import ResourceAttributes
    from opentelemetry import trace as otel_trace

    return (
        OTLPSpanExporter,
        Resource,
        TracerProvider,
        BatchSpanProcessor,
        ResourceAttributes,
        otel_trace,
    )


def setup(endpoint: str = DEFAULT_ENDPOINT, project: str = DEFAULT_PROJECT):
    """Idempotently wire an OTel tracer that exports to a local Phoenix."""
    global _OTEL_READY, _OTEL_FAILED, _tracer
    with _lock:
        if _OTEL_READY:
            return _tracer
        if _OTEL_FAILED:
            return None
        try:
            (OTLPSpanExporter, Resource, TracerProvider,
             BatchSpanProcessor, ResourceAttributes, otel_trace) = _import_otel()
            provider = TracerProvider(
                resource=Resource.create({ResourceAttributes.PROJECT_NAME: project})
            )
            provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
            otel_trace.set_tracer_provider(provider)
            _tracer = otel_trace.get_tracer("pixelbench.phoenix_pixel")
            _OTEL_READY = True
            print(f"[phoenix-pixel] exporting OpenInference spans -> {endpoint} (project={project})")
            return _tracer
        except Exception as e:  # noqa: BLE001 - optional dependency
            _OTEL_FAILED = True
            print(f"[phoenix-pixel] WARNING: Phoenix tracing unavailable ({e}); continuing without")
            return None


# ----------------------------------------------------------------------
# attribute helpers (OpenInference flattened keys)
# ----------------------------------------------------------------------
def _data_uri(png: bytes) -> str:
    return "data:image/png;base64," + base64.b64encode(png).decode()


def _text_content_part(index: int, text: str) -> Dict[str, Any]:
    return {
        f"llm.input_messages.{index}.message.contents.0.message_content.type": "text",
        f"llm.input_messages.{index}.message.contents.0.message_content.text": text,
    }


def _image_content_part(index: int, image_index: int, data_uri: str) -> Dict[str, Any]:
    # OpenInference: message_content.image.image.url (MESSAGE_CONTENT_IMAGE="message_content.image"
    # + IMAGE_URL="image.url"); the frontend reads `(t?.image)?.image?.url`.
    return {
        f"llm.input_messages.{index}.message.contents.{image_index}.message_content.type": "image",
        f"llm.input_messages.{index}.message.contents.{image_index}.message_content.image.image.url": data_uri,
    }


def _input_message(index: int, role: str, parts: List[Dict[str, str]]) -> Dict[str, Any]:
    attrs = {f"llm.input_messages.{index}.message.role": role}
    for part in parts:
        attrs.update(part)
    return attrs


# ----------------------------------------------------------------------
# span emission
# ----------------------------------------------------------------------
def _set_kind(span, kind: str) -> None:
    span.set_attribute("openinference.span.kind", kind)


def _span_times(span, start_ns: int, end_ns: int) -> None:
    span.set_attribute("_pb_start_ns", str(start_ns))  # informational only



def _lookup_prompt(task_id: str) -> Optional[str]:
    """Best-effort prompt lookup for a task id (showcase tasks known statically)."""
    try:
        from examples.showcase_tasks import showcase_tasks

        for t in showcase_tasks():
            if t.id == task_id:
                return t.prompt
    except Exception:  # noqa: BLE001
        pass
    return None


def emit_replay_episode(episode_dir: Path, project: str = DEFAULT_PROJECT) -> bool:
    """Replay one finished episode directory into Phoenix as one trace."""
    tracer = setup(project=project)
    if tracer is None:
        return False
    episode_dir = Path(episode_dir)
    odir = episode_dir / "observations"
    record_path = episode_dir / "record.json"
    if not record_path.exists():
        return False

    record = _read_json(record_path) or {}
    turns = _read_jsonl(odir / "turns.jsonl")
    code_events = _read_jsonl(episode_dir / "trace.jsonl")
    code_events = [e for e in code_events if e.get("kind") == "code"]

    from opentelemetry import trace as otel_trace

    task_id = record.get("task_id", episode_dir.name.split("__")[0])
    agent = record.get("agent", "")
    model = agent.replace("-repl", "").replace("-direct", "") or "llm"
    prompt = _lookup_prompt(task_id) or str(record.get("task_type", ""))
    final_png = (episode_dir / "final.png").read_bytes() if (episode_dir / "final.png").exists() else None

    # turn -> frame PNG (turn 0 is the prelude frame; drawing turns start at 1)
    frames: Dict[int, Path] = {}
    for t in turns:
        fr = t.get("frame")
        if fr:
            p = odir / str(fr)
            if p.exists():
                frames[int(t.get("turn", 0))] = p

    # timestamps: turn.t (epoch seconds) as span start, next turn as end
    turn_times: Dict[int, float] = {}
    for t in turns:
        tt = t.get("t")
        if tt:
            turn_times[int(t.get("turn", 0))] = float(tt)
    all_ts = sorted(turn_times.values())
    t0 = all_ts[0] if all_ts else 0.0

    def duration(turn: int, default: float = 3.0) -> float:
        later = sorted(turn_times.get(k, 1e18) for k in turn_times if k > turn)
        return (later[0] - turn_times.get(turn, t0)) if later and later[0] < 1e17 else default

    start_ns = int((turn_times.get(1, t0) if all_ts else 0.0) * 1e9) or _now_ns() - 60_000_000_000
    end_ns = int((turn_times.get(max(turn_times, default=1), t0) + 3) * 1e9)

    root = tracer.start_span(f"{task_id} · {agent}", start_time=start_ns)
    with otel_trace.use_span(root, end_on_exit=False):
        _set_kind(root, "AGENT")
        root.set_attribute("metadata", json.dumps({
            "task_id": task_id,
            "task_type": record.get("task_type", ""),
            "agent": agent,
            "steps": record.get("steps"),
            "ok": record.get("ok"),
            "judge": (record.get("judge") or {}).get("overall"),
        }, ensure_ascii=False))
        root.set_attribute("input.value", prompt)
        root.set_attribute("input.mime_type", "text/plain")

        # one LLM + TOOL span per drawing turn
        turn_keys = sorted(k for k in turn_times if k > 0)
        for i, turn in enumerate(turn_keys):
            ce = code_events[i] if i < len(code_events) else None
            code = (ce or {}).get("code") or ""
            out = _result_text((ce or {}).get("output"))
            start = int(turn_times.get(turn, t0) * 1e9)
            end = int((turn_times.get(turn, t0) + duration(turn)) * 1e9)

            llm = tracer.start_span(f"LLM step {i + 1}", start_time=start)
            with otel_trace.use_span(llm, end_on_exit=False):
                _set_kind(llm, "LLM")
                llm.set_attribute("llm.model_name", model)
                attrs = _input_message(0, "user", [_text_content_part(0, code or "(no code)")])
                for k, v in attrs.items():
                    llm.set_attribute(k, v)
                img = frames.get(turn)
                if img is not None:
                    try:
                        png = img.read_bytes()
                        for k, v in _image_content_part(0, 1, _data_uri(png)).items():
                            llm.set_attribute(k, v)
                    except Exception:  # noqa: BLE001
                        pass
                llm.set_attribute("llm.output_messages.0.message.role", "assistant")
                llm.set_attribute("llm.output_messages.0.message.content", f"tool call: run_code (step {i + 1})")
                llm.set_attribute("llm.invocation_parameters", json.dumps({"temperature": 0.7}))

                tool = tracer.start_span("run_code", start_time=start)
                with otel_trace.use_span(tool, end_on_exit=False):
                    _set_kind(tool, "TOOL")
                    tool.set_attribute("tool.name", "run_code")
                    tool.set_attribute("input.value", code)
                    tool.set_attribute("input.mime_type", "text/plain")
                    tool.set_attribute("output.value", out)
                    tool.set_attribute("output.mime_type", "text/plain")
                tool.end(end_time=end)

            llm.end(end_time=end)

        # final image attached to the root if there were no drawing turns
        if final_png is not None and not turn_keys:
            root.set_attribute("output.value", _data_uri(final_png))
            root.set_attribute("output.mime_type", "image/png")
    root.end(end_time=end_ns)
    return True


def replay_run_to_phoenix(run_dir: Path, project: str = DEFAULT_PROJECT) -> int:
    run_dir = Path(run_dir)
    episodes = sorted(run_dir.glob("episodes/*"))
    n = 0
    for d in episodes:
        if not (d / "record.json").exists():
            continue
        print(f"[phoenix-pixel] replaying {d.name} ...", flush=True)
        try:
            if emit_replay_episode(d, project=project):
                n += 1
        except Exception as e:  # noqa: BLE001 - keep going
            print(f"  ! failed: {type(e).__name__}: {e}")
    print(f"[phoenix-pixel] replayed {n}/{len(episodes)} episodes into Phoenix (project={project})")
    return n


# ----------------------------------------------------------------------
# live hook for REPLAgent
# ----------------------------------------------------------------------
class LivePhoenixHook:
    """Emit live OpenInference spans around a REPLAgent run.

    Enabled when ``PIXELBENCH_TRACE_BACKEND=phoenix``.  All methods are
    defensive: a tracing failure must never break the agent loop.
    """

    def __init__(self, project: str = DEFAULT_PROJECT) -> None:
        self.tracer = setup(project=project)
        self._root = None
        self.model_name = "unknown"

    @property
    def enabled(self) -> bool:
        return self.tracer is not None and phoenix_backend_enabled()

    def start_episode(self, task, agent_name: str) -> None:
        try:
            self.model_name = (
                agent_name.replace("-repl", "").replace("-direct", "").replace("-agent", "")
                or "llm"
            )
            self._root = self.tracer.start_as_current_span(
                f"{task.id} · {agent_name}",
                attributes={
                    "openinference.span.kind": "AGENT",
                    "metadata": json.dumps({
                        "task_id": task.id, "task_type": task.task_type,
                        "agent": agent_name, "prompt": task.prompt,
                    }, ensure_ascii=False),
                    "input.value": task.prompt,
                    "input.mime_type": "text/plain",
                },
            )
            self._root.__enter__()
        except Exception:  # noqa: BLE001
            self._root = None

    def step(self, step: int, code: str, result, images: List[bytes]) -> None:
        """One run_code step: LLM span (with render images) + TOOL span."""
        if self._root is None:
            return
        try:
            root_ctx = self.tracer.start_as_current_span  # placeholder, unused
            with self.tracer.start_as_current_span(f"LLM step {step}") as llm:
                llm.set_attribute("openinference.span.kind", "LLM")
                llm.set_attribute("llm.model_name", self.model_name)
                attrs = _input_message(0, "user", [_text_content_part(0, code or "(no code)")])
                for k, v in attrs.items():
                    llm.set_attribute(k, v)
                for j, png in enumerate(images[:6]):
                    for k, v in _image_content_part(0, 1 + j, _data_uri(png)).items():
                        llm.set_attribute(k, v)
                out = ""
                try:
                    out = result.combined() or ""
                except Exception:  # noqa: BLE001
                    pass
                llm.set_attribute("llm.output_messages.0.message.role", "assistant")
                llm.set_attribute("llm.output_messages.0.message.content", out[:4000] or "(no output)")
                with self.tracer.start_as_current_span("run_code") as tool:
                    tool.set_attribute("openinference.span.kind", "TOOL")
                    tool.set_attribute("tool.name", "run_code")
                    tool.set_attribute("input.value", code)
                    tool.set_attribute("input.mime_type", "text/plain")
                    tool.set_attribute("output.value", out[:4000])
                    tool.set_attribute("output.mime_type", "text/plain")
        except Exception:  # noqa: BLE001
            pass

    def finish(self, final_canvas=None) -> None:
        try:
            if self._root is None:
                return
            if final_canvas is not None:
                try:
                    self._root.set_attribute("output.value", _data_uri(final_canvas.render_png_bytes(scale=4)))
                    self._root.set_attribute("output.mime_type", "image/png")
                except Exception:  # noqa: BLE001
                    pass
            self._root.__exit__(None, None, None)
            self._root = None
        except Exception:  # noqa: BLE001
            self._root = None


# ----------------------------------------------------------------------
# small file helpers
# ----------------------------------------------------------------------
def _read_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    out = []
    try:
        with Path(path).open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:  # noqa: BLE001
                    continue
                if isinstance(obj, dict):
                    out.append(obj)
    except FileNotFoundError:
        pass
    return out


def _result_text(output: Any) -> str:
    if not isinstance(output, dict):
        return str(output or "")
    parts = []
    if output.get("stdout"):
        parts.append(str(output["stdout"]))
    if output.get("stderr"):
        parts.append("STDERR: " + str(output["stderr"]))
    for e in output.get("errors") or []:
        parts.append(f"{e.get('ename', 'Error')}: {e.get('evalue', '')}")
    return "\n".join(parts) if parts else "(no output)"


def _now_ns() -> int:
    import time
    return int(time.time() * 1e9)
