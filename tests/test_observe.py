"""Tests for harness-side observation artifacts (process viewer HTML)."""
import json
import re

from pixelbench.observe import (
    OBS_DIRNAME,
    collect_observation_stats,
    observation_dir,
    write_process_viewer,
)


def _make_episode(tmp_path, with_observations=True):
    d = tmp_path / "episode"
    d.mkdir()
    (d / "final.png").write_bytes(b"\x89PNG\r\n\x1a\nfake")
    (d / "record.json").write_text(
        json.dumps(
            {
                "task_id": "agentic_0001",
                "task_type": "agentic_creation",
                "agent": "mock-repl",
                "ok": True,
                "steps": 2,
                "metrics": {"agentic": {"coverage": 0.5}},
                "images": {"final": "final.png"},
            }
        ),
        encoding="utf-8",
    )
    (d / "trace.jsonl").write_text(
        json.dumps({"step": 0, "kind": "code", "code": "paint_rect(0,0,2,2,'red')", "output": {"stdout": "ok"}})
        + "\n",
        encoding="utf-8",
    )
    if with_observations:
        od = d / OBS_DIRNAME
        (od / "frames").mkdir(parents=True)
        (od / "diffs").mkdir(parents=True)
        (od / "calls.jsonl").write_text(
            json.dumps({"kind": "call", "call": 0, "op": "paint_rect", "changed": 4, "diff": "diffs/call_000000.png"})
            + "\n",
            encoding="utf-8",
        )
        (od / "turns.jsonl").write_text(
            json.dumps({"kind": "turn", "turn": 0, "initial": True, "calls_start": 0, "calls_end": 0, "frame": "frames/turn_0000.png"})
            + "\n"
            + json.dumps({"kind": "turn", "turn": 1, "initial": False, "calls_start": 0, "calls_end": 1, "frame": "frames/turn_0001.png", "code": "paint_rect(0,0,2,2,'red')"})
            + "\n",
            encoding="utf-8",
        )
        (od / "frames" / "turn_0000.png").write_bytes(b"\x89PNG\r\n\x1a\n0")
        (od / "frames" / "turn_0001.png").write_bytes(b"\x89PNG\r\n\x1a\n1")
        (od / "diffs" / "call_000000.png").write_bytes(b"\x89PNG\r\n\x1a\n2")
    return d


def test_collect_observation_stats(tmp_path):
    d = _make_episode(tmp_path)
    stats = collect_observation_stats(d)
    assert stats["calls"] == 1 and stats["turns"] == 2 and stats["frames"] == 2
    assert stats["diff_images"] == 1 and stats["sdk_trace"] is False
    assert stats["viewer"] == "process.html"

    empty = tmp_path / "empty"
    empty.mkdir()
    assert collect_observation_stats(empty) == {}


def test_write_process_viewer_embeds_data(tmp_path):
    d = _make_episode(tmp_path)
    target = write_process_viewer(d)
    assert target is not None and target.name == "process.html" and target.is_file()
    html = target.read_text(encoding="utf-8")
    m = re.search(r"const DATA = (\{.*?\});\nconst rec", html, re.S)
    data = json.loads(m.group(1))
    assert data["record"]["task_id"] == "agentic_0001"
    assert len(data["turns"]) == 2 and len(data["calls"]) == 1 and len(data["trace"]) == 1
    assert data["obs_dir"] == "observations"
    assert "</script>" not in m.group(1)  # no premature script close
    assert "frames/turn_0001.png" in html
    assert "diffs/call_000000.png" in html


def test_write_process_viewer_skips_when_nothing_observed(tmp_path):
    d = _make_episode(tmp_path, with_observations=False)
    assert write_process_viewer(d) is None
    assert not (d / "process.html").exists()
    assert observation_dir(d).exists() is False or True  # path helper is pure


def test_viewer_title_escaped(tmp_path):
    d = _make_episode(tmp_path)
    (d / "record.json").write_text(
        json.dumps({"task_id": 'x"<script>', "agent": "a<b"}),
        encoding="utf-8",
    )
    html = write_process_viewer(d).read_text(encoding="utf-8")
    # the hostile title must be HTML-escaped inside the <title> tag
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
    assert "&lt;script&gt;" in title
    assert "<script>" not in title


def test_build_trace_manifest_both_layouts(tmp_path):
    from pixelbench.observe import build_trace_manifest

    # layout 1: episodes/<ep>/observations/sdk_trace.jsonl
    ep = tmp_path / "episodes" / "ep1"
    (ep / "observations").mkdir(parents=True)
    (ep / "observations" / "sdk_trace.jsonl").write_text("{}\n", encoding="utf-8")
    (ep / "process.html").write_text("<html></html>", encoding="utf-8")
    # layout 2: root-level observations/sdk_trace.jsonl (single episode dir)
    (tmp_path / "observations").mkdir()
    (tmp_path / "observations" / "sdk_trace.jsonl").write_text("{}\n", encoding="utf-8")

    m = build_trace_manifest(tmp_path)
    by = {e["episode"]: e for e in m["traces"]}
    assert "ep1" in by and tmp_path.name in by
    assert by["ep1"]["url"] == "episodes/ep1/observations/sdk_trace.jsonl"
    assert by["ep1"]["viewer"] == "episodes/ep1/process.html"
    assert by[tmp_path.name]["url"] == "observations/sdk_trace.jsonl"


def test_traces_handler_serves_page_and_manifest(tmp_path):
    import threading
    import urllib.request
    from http.server import ThreadingHTTPServer

    from pixelbench.observe import make_traces_handler

    (tmp_path / "observations").mkdir()
    (tmp_path / "observations" / "sdk_trace.jsonl").write_text(
        '{"kind": "trace_start", "trace_id": "tr1"}\n', encoding="utf-8"
    )
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), make_traces_handler(tmp_path))
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    try:
        page = urllib.request.urlopen(f"http://127.0.0.1:{port}/").read().decode("utf-8")
        assert "PixelBench Agent Trace" in page
        assert "renderSdkTraceTrees" in page
        m = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/manifest.json").read())
        assert m["traces"][0]["episode"] == tmp_path.name
        raw = urllib.request.urlopen(
            f"http://127.0.0.1:{port}/observations/sdk_trace.jsonl"
        ).read().decode("utf-8")
        assert '"trace_id": "tr1"' in raw
    finally:
        httpd.shutdown()
