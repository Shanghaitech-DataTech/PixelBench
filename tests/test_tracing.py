"""Tests for the OpenAI Agents SDK trace integration (local JSONL sink)."""
import json
from types import SimpleNamespace

import pytest

from pixelbench.tracing import (
    JsonlTraceProcessor,
    build_run_config,
    get_current_episode_dir,
    register_pixelbench_tracing,
    set_current_episode_dir,
)

pytest.importorskip("agents")


class FakeSpanData:
    def __init__(self, d):
        self._d = d

    def export(self):
        return self._d


class FakeSpan:
    def __init__(self, span_id, trace_id, parent_id=None, name="f", span_data=None, error=None):
        self.span_id = span_id
        self.trace_id = trace_id
        self.parent_id = parent_id
        self.name = name
        self.span_data = span_data or FakeSpanData({"type": "function", "name": "run_code"})
        self.error = error
        self.metadata = {"m": 1}

    def export(self):
        return {"object": "trace.span", "id": self.span_id}


class FakeTrace:
    def __init__(self, trace_id, name="w"):
        self.trace_id = trace_id
        self.name = name
        self.metadata = {"pixelbench_episode_dir": "/x", "task_id": "t1"}

    def export(self):
        return {"object": "trace", "id": self.trace_id, "workflow_name": self.name}


def test_jsonl_processor_routes_to_episode_dir(tmp_path):
    set_current_episode_dir(str(tmp_path))
    proc = JsonlTraceProcessor()
    trace = FakeTrace("tr-1", "pixelbench/agentic_creation/t1")
    proc.on_trace_start(trace)
    proc.on_span_start(FakeSpan("s-1", "tr-1"))
    proc.on_span_end(FakeSpan("s-1", "tr-1", span_data=FakeSpanData({"type": "function", "name": "run_code", "input": "print(1)", "output": "1"})))
    proc.on_trace_end(trace)
    proc.force_flush()

    target = tmp_path / "sdk_trace.jsonl"
    assert target.is_file()
    lines = [json.loads(l) for l in target.read_text().splitlines() if l.strip()]
    kinds = [l["kind"] for l in lines]
    assert kinds == ["trace_start", "span_start", "span_end", "trace_end"]
    assert lines[0]["trace_id"] == "tr-1"
    assert lines[2]["span_data"]["name"] == "run_code"
    assert "tracing_api_key" not in lines[0]
    # no episode dir -> silent no-op
    set_current_episode_dir(None)
    proc.on_trace_start(trace)  # must not raise
    assert get_current_episode_dir() is None


def test_build_run_config_tags_episode(tmp_path):
    set_current_episode_dir(str(tmp_path))
    cfg = build_run_config("pixelbench/replication/r1", str(tmp_path), task_id="r1", agent="sdk")
    assert cfg.workflow_name == "pixelbench/replication/r1"
    assert cfg.trace_metadata["task_id"] == "r1"
    assert cfg.trace_metadata["agent"] == "sdk"
    assert cfg.trace_metadata["pixelbench_episode_dir"] == str(tmp_path)


def test_register_pixelbench_tracing_idempotent():
    from agents.tracing import get_trace_provider

    p1 = register_pixelbench_tracing()
    p2 = register_pixelbench_tracing()
    assert p1 is p2
    provider = get_trace_provider()
    processors = provider._multi_processor._processors
    assert any(isinstance(p, JsonlTraceProcessor) for p in processors)


def test_maybe_enable_phoenix_from_env_gating(monkeypatch):
    from pixelbench import tracing

    # Phoenix tracing is ON by default (env unset -> attempts to enable)
    monkeypatch.delenv("PIXELBENCH_TRACE_BACKEND", raising=False)
    try:
        ok = tracing.maybe_enable_phoenix_from_env()
    finally:
        monkeypatch.delenv("PIXELBENCH_TRACE_BACKEND", raising=False)
    # packages installed in this env -> returns True and instruments
    assert ok in (True, False)
    # explicit opt-out: off / 0 / false / none / empty all disable
    for off in ("off", "0", "false", "none", ""):
        monkeypatch.setenv("PIXELBENCH_TRACE_BACKEND", off)
        assert tracing.maybe_enable_phoenix_from_env() is False
    monkeypatch.delenv("PIXELBENCH_TRACE_BACKEND", raising=False)


def test_write_sample_sdk_trace(tmp_path):
    from pixelbench.tracing import write_sample_sdk_trace

    d = tmp_path / "sample_ep"
    target = write_sample_sdk_trace(str(d))
    assert target.name == "process.html" and target.is_file()
    lines = [json.loads(l) for l in (d / "observations" / "sdk_trace.jsonl").read_text().splitlines() if l.strip()]
    kinds = [l["kind"] for l in lines]
    assert "trace_start" in kinds and "span_end" in kinds and "trace_end" in kinds
    ends = [l for l in lines if l["kind"] == "span_end"]
    # spans form a tree: agent span at top, generation/function under it
    assert any(l["span_data"]["type"] == "agent" for l in ends)
    assert any(l["span_data"]["type"] == "function" for l in ends)
    assert any(l["span_data"]["type"] == "generation" for l in ends)
    parented = [l for l in ends if l["parent_id"]]
    assert len(parented) == len(ends)  # every span has a parent (agent/trace)
    # viewer embeds the trace data + the tree renderer
    html = target.read_text(encoding="utf-8")
    assert "renderSdkTraceTrees" in html  # tree renderer wired in
    assert "sample_trace_0001" in html    # embedded trace data
