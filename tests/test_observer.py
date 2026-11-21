"""Tests for the kernel-side painting-process observer."""
import json

import pytest

from pixelbench.core.canvas import PixelCanvas
from pixelbench.repl.observer import MUTATING_TOOLS, ObservedTools, render_diff_png

pytest.importorskip("ipykernel")

from pixelbench.repl.prelude import build_prelude
from pixelbench.tasks.smoke import smoke_tasks


def _agentic_task():
    return smoke_tasks()[2]


def test_mutating_tools_covered():
    # every mutating SessionTools method should be observed
    from pixelbench.repl.tools import TOOL_NAMES

    assert "set_pixel" in MUTATING_TOOLS
    assert "paint_rect" in MUTATING_TOOLS
    assert "undo" in MUTATING_TOOLS
    assert "finish" in MUTATING_TOOLS
    # observation-only tools must NOT be recorded as calls
    assert "render" not in MUTATING_TOOLS
    assert "observe_region" not in MUTATING_TOOLS
    assert "summary" not in MUTATING_TOOLS


def test_render_diff_png_shape_and_header():
    c = PixelCanvas(8, 8)
    c.register_color("red", "#e0455a")
    before = c.matrix.copy()
    c.set_pixel(2, 3, "red")
    changed = before != c.matrix
    png = render_diff_png(c, before, c.matrix, changed, "set_pixel", scale=4)
    assert png[:8] == b"\x89PNG\r\n\x1a\n"
    from PIL import Image

    img = Image.open(__import__("io").BytesIO(png))
    # before(8*4) + gap(10) + after(8*4) = 74 wide, header(30) + 8*4 + 8 = 70 tall
    assert img.size == (74, 70)


def test_observed_tools_proxy(kernel):
    t = _agentic_task()
    kernel.execute(
        build_prelude(task=t.public_task(), initial_state=t.initial_state(), observer_dir=None, seed=0),
        timeout=60,
    )
    r = kernel.execute(
        "from pixelbench.repl.observer import ObservedTools\n"
        "from pixelbench.repl.observer import CanvasObserver\n"
        "import tempfile\n"
        "_odir = tempfile.mkdtemp()\n"
        "from pixelbench import PixelCanvas\n"
        "from pixelbench.repl.tools import SessionTools\n"
        "canvas=PixelCanvas(8,8)\n"
        "plain=SessionTools(canvas)\n"
        "_obs = CanvasObserver(_odir, canvas)\n"
        "tools = ObservedTools(plain, _obs)\n"
        "red = plain.register_color('red', '#e0455a')\n"
        "plain.set_pixel(0, 0, red)\n"  # top-level binding still points at old tools
        "out = tools.set_pixel(1, 1, red)\n"
        "print(out)\n"
        "print('CALLS', _obs.call_index)\n",
        timeout=60,
    )
    assert r.ok, r.combined()
    # ObservedTools wraps mutating calls; render() must pass through
    assert "CALLS 1" in r.stdout


def test_observer_records_calls_and_turns(tmp_path, kernel):
    t = _agentic_task()
    obs_dir = tmp_path / "observations"
    kernel.execute(
        build_prelude(
            task=t.public_task(), initial_state=t.initial_state(),
            reference_state=None, mask_state=None, seed=0,
            observer_dir=str(obs_dir),
        ),
        timeout=60,
    )
    code = (
        "outline = input_canvas.color('#2b2b2b',name='outline')\n"
        "input_canvas.rect(1, 1, 6, 6, outline)\n"
        "view(input_canvas,scale=8)\n"
    )
    assert kernel.execute(code, timeout=60).ok
    # second block: set_pixel + undo; then extract (must not add a turn)
    assert kernel.execute("input_canvas.set(1, 1, 'transparent')\nundo(1)", timeout=60).ok
    final = kernel.extract_final_canvas()
    assert final is not None

    calls = [json.loads(l) for l in (obs_dir / "calls.jsonl").read_text().splitlines() if l.strip()]
    assert [c["op"] for c in calls] == ["color", "rect", "set", "undo_step"]
    assert calls[1]["changed"] == 36
    # per-call diff PNGs are OFF by default (turn frames are the primary
    # observation window); the call event still records op/args/changed
    assert calls[1]["diff"] is None
    # call events carry the turn (block) they executed in
    assert [c["turn"] for c in calls] == [1, 1, 2, 2]
    # render() is not recorded as a call
    assert all(c["op"] != "render" for c in calls)

    turns = [json.loads(l) for l in (obs_dir / "turns.jsonl").read_text().splitlines() if l.strip()]
    assert turns[0]["initial"] is True and turns[0]["frame"] is not None
    assert turns[1]["code"] and "rect" in turns[1]["code"]
    assert turns[1]["calls_start"] == 0 and turns[1]["calls_end"] == 2
    assert turns[2]["calls_start"] == 2 and turns[2]["calls_end"] == 4
    # extraction must not have created an extra turn
    assert len(turns) == 3
    frames = list((obs_dir / "frames").glob("*.png"))
    assert len(frames) == 6


def test_observer_render_diffs_when_enabled(tmp_path, kernel):
    t = _agentic_task()
    obs_dir = tmp_path / "observations"
    kernel.execute(
        build_prelude(
            task=t.public_task(), initial_state=t.initial_state(),
            reference_state=None, mask_state=None, seed=0,
            observer_dir=str(obs_dir),
        ),
        timeout=60,
    )
    # the env-var default cannot reach an already-started kernel process,
    # so flip the flag on the live observer directly
    r = kernel.execute("_pb_obs.render_diffs = True", timeout=30)
    assert r.ok, r.combined()
    code = "input_canvas.color('#2b2b2b',name='outline')\ninput_canvas.rect(1, 1, 6, 6, 'outline')"
    assert kernel.execute(code, timeout=60).ok
    calls = [json.loads(l) for l in (obs_dir / "calls.jsonl").read_text().splitlines() if l.strip()]
    assert [c["op"] for c in calls] == ["color", "rect"]
    assert calls[1]["diff"].startswith("diffs/call_")
    assert (obs_dir / calls[1]["diff"]).is_file()
