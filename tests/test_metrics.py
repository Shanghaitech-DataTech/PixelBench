import numpy as np
import pytest

from pixelbench.core.canvas import PixelCanvas
from pixelbench.eval.metrics import (
    agentic_metrics,
    palette_discipline,
    replication_metrics,
    restoration_metrics,
    validate_canvas,
)
from pixelbench.tasks.smoke import smoke_tasks


def test_validate_canvas():
    c = PixelCanvas(8, 8)
    c.register_color("red", "#e0455a")
    c.paint_rect(0, 0, 2, 2, "red")
    assert validate_canvas(c)["valid"] is True
    c.matrix[0, 0] = 999
    assert validate_canvas(c)["valid"] is False


def test_palette_discipline():
    c = PixelCanvas(8, 8)
    c.register_color("red", "#e0455a")
    c.register_color("blue", "#3f5fd9")
    c.paint_rect(0, 0, 2, 2, "red")
    c.paint_rect(4, 4, 2, 2, "blue")
    d = palette_discipline(c, 2)
    assert d["ok"] is True and d["used_colors"] == 2
    d2 = palette_discipline(c, 1)
    assert d2["ok"] is False


def test_replication_metrics_perfect_and_bad():
    t = smoke_tasks()[4]
    ref = t.reference
    perfect = ref.copy()
    m = replication_metrics(perfect, ref)
    assert m["pixel_accuracy"] == 1.0
    assert m["content_iou"] == 1.0
    assert m["palette_recall"] == 1.0
    empty = PixelCanvas(ref.width, ref.height)
    m2 = replication_metrics(empty, ref)
    assert m2["content_iou"] == 0.0
    assert m2["pixel_accuracy"] < m["pixel_accuracy"]


def test_restoration_metrics_protected_region():
    t = smoke_tasks()[6]
    ref = t.reference
    mask = t.mask
    corrupted = ref.copy()
    corrupted.matrix[mask] = corrupted.transparent_id
    # perfect restoration
    m = restoration_metrics(ref, ref, mask, corrupted)
    assert m["region_accuracy"] == 1.0
    assert m["protected_change_rate"] == 0.0
    # vandalizing the protected region must be caught
    bad = corrupted.copy()
    bad.matrix[~mask] = 1
    m2 = restoration_metrics(bad, ref, mask, corrupted)
    assert m2["protected_change_rate"] > 0.5


def test_agentic_metrics():
    c = PixelCanvas(16, 16)
    c.register_color("red", "#e0455a")
    c.paint_rect(0, 0, 8, 8, "red")
    c.snapshot("done")
    c.undo()  # back to empty; undo itself is recorded
    transcript = [{"kind": "code", "code": "x"}, {"kind": "code", "code": "y"}]
    m = agentic_metrics(c, transcript)
    assert m["steps"] == 2
    assert m["coverage_pct"] == 0.0  # canvas was undone to empty
    assert m["used_colors"] == 0
    assert "paint_rect" in m["tool_types"]
    assert m["undo_count"] == 1


def test_agentic_metrics_counts_undo_step_round():
    c = PixelCanvas(16, 16)
    c.register_color("red", "#e0455a")
    c.mark_call()
    c.paint_rect(0, 0, 8, 8, "red")
    c.mark_call()
    c.undo_step()  # reverts the rect; both ops land in the edit log
    c.mark_round()
    c.paint_rect(1, 1, 2, 2, "red")
    c.mark_round()
    c.undo_round()
    m = agentic_metrics(c, [])
    assert m["undo_count"] == 2  # undo_step + undo_round
    assert "undo_step" in m["tool_types"] and "undo_round" in m["tool_types"]


def test_agentic_metrics_from_observer_calls():
    # the observer call log is the authoritative tool-use source: it
    # records every model call (incl. palette registration) even after
    # the final canvas has been rebuilt from serialization (empty edit log)
    c = PixelCanvas(16, 16)
    c.register_color("red", "#e0455a")
    c.paint_rect(0, 0, 8, 8, "red")  # canvas edit log is NOT empty here,
    calls = [
        {"op": "register_color", "changed": 0},
        {"op": "paint_rect", "changed": 64},
        {"op": "paint_rect", "changed": 16},
        {"op": "undo_step", "changed": 0},
        {"op": "draw_line", "changed": 5},
    ]
    m = agentic_metrics(c, [{"kind": "code", "code": "x"}], obs_calls=calls)
    assert m["steps"] == 1
    assert m["tool_calls"] == 5
    assert m["tool_diversity"] == 4
    assert "register_color" in m["tool_types"]  # observer sees palette calls
    assert m["total_changed_px"] == 85
    assert m["undo_count"] == 1
    # a rebuilt canvas (empty edit log) still reports the observer stats
    rebuilt = PixelCanvas.from_dict(c.to_dict())
    assert rebuilt._edit_log == []
    m2 = agentic_metrics(rebuilt, [], obs_calls=calls)
    assert m2["tool_calls"] == 5 and m2["tool_diversity"] == 4
