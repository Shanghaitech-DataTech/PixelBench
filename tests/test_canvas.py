import numpy as np
import pytest

from pixelbench.core.canvas import ERASE, KEEP, CanvasError, PixelCanvas
from pixelbench.core.color import Color, Palette


def make_canvas(w=16, h=16):
    c = PixelCanvas(w, h)
    c.register_color("red", "#e0455a")
    c.register_color("blue", "#3f5fd9")
    return c


def test_init_and_palette():
    c = make_canvas()
    assert c.width == 16 and c.height == 16
    assert c.matrix.shape == (16, 16)
    assert c.matrix.min() == c.matrix.max() == c.transparent_id
    assert c.palette.color("red").rgba == (224, 69, 90, 255)


def test_transparent_id_must_be_transparent():
    p = Palette()
    p.register("red", (255, 0, 0, 255))
    with pytest.raises(CanvasError):
        PixelCanvas(8, 8, palette=p, transparent_id=0)


def test_set_pixel_and_feedback():
    c = make_canvas()
    r = c.set_pixel(3, 4, "red")
    assert r["changed"] == 1
    assert c.matrix[4, 3] == c.palette._resolve_id("red")
    assert c.pick_color(3, 4) == "red (id 1, #e0455aff)"
    # setting same color again -> 0 changed
    assert c.set_pixel(3, 4, "red")["changed"] == 0


def test_out_of_bounds_set_pixel():
    c = make_canvas()
    with pytest.raises(CanvasError):
        c.set_pixel(99, 99, "red")


def test_unknown_color_rejected():
    c = make_canvas()
    with pytest.raises(ValueError):
        c.paint_rect(0, 0, 4, 4, "neon_pink")


def test_paint_rect_and_clear():
    c = make_canvas()
    c.paint_rect(2, 2, 5, 4, "red")
    assert c.matrix[3, 3] == c.palette._resolve_id("red")
    c.clear_region(2, 2, 5, 4)
    assert c.matrix[3, 3] == c.transparent_id


def test_undo_snapshot_history():
    c = make_canvas()
    c.paint_rect(0, 0, 4, 4, "red")
    c.snapshot("stage1")
    c.paint_rect(2, 2, 4, 4, "blue")
    assert c.matrix[3, 3] == c.palette._resolve_id("blue")
    c.undo()
    assert c.matrix[3, 3] == c.palette._resolve_id("red")
    c.restore("stage1")
    assert c.matrix[3, 3] == c.palette._resolve_id("red")
    h = c.history(5)
    assert "paint_rect" in h and "undo" in h


def test_stamp_pattern():
    c = make_canvas()
    pattern = [
        ["red", KEEP, "red"],
        [KEEP, "red", KEEP],
    ]
    c.stamp(pattern, 1, 1)
    assert c.matrix[1, 1] == c.palette._resolve_id("red")
    assert c.matrix[1, 2] == c.transparent_id
    assert c.matrix[2, 2] == c.palette._resolve_id("red")  # pattern[1][1]
    assert c.matrix[2, 1] == c.transparent_id  # pattern[1][0] is KEEP


def test_keep_erase_sentinels():
    assert repr(KEEP) == "KEEP"
    assert repr(ERASE) == "ERASE"
    c = make_canvas()
    # KEEP is a cell symbol, not a color ref
    with pytest.raises(ValueError):
        c.set_pixel(0, 0, KEEP)
    # None / 'transparent' are the blank spellings in every color position
    c.set_pixel(1, 1, None)
    assert c.matrix[1, 1] == c.transparent_id
    c.set_pixel(2, 2, "transparent")
    assert c.matrix[2, 2] == c.transparent_id
    c.paint_region(0, 0, [[None]])
    assert c.matrix[0, 0] == c.transparent_id
    # ERASE stays as an alias anywhere a color is accepted
    c.set_pixel(3, 3, "red")
    c.set_pixel(3, 3, ERASE)
    assert c.matrix[3, 3] == c.transparent_id
    c.paint_rect(0, 0, 4, 4, "red")
    c.paint_rect(0, 0, 4, 4, ERASE)
    assert (c.matrix[:4, :4] == c.transparent_id).all()


def test_blank_spellings_map_directly():
    """'transparent'/None blank even when the transparent_id color has another name."""
    pal = Palette([Color(id=0, name="empty", rgba=(0, 0, 0, 0))])
    c = PixelCanvas(4, 4, palette=pal, transparent_id=0)
    c.register_color("red", "#e0455a")
    c.set_pixel(0, 0, "transparent")
    assert c.matrix[0, 0] == c.transparent_id
    c.set_pixel(1, 1, None)
    assert c.matrix[1, 1] == c.transparent_id
    c.paint_region(2, 0, [["transparent", None]])
    assert (c.matrix[0, 2:4] == c.transparent_id).all()
    c.paint_rect(1, 1, 2, 2, "red")
    assert (c.matrix[1:3, 1:3] == c.palette._resolve_id("red")).all()
    c.clear_region(1, 1, 2, 2)  # default color=None -> transparent
    assert (c.matrix[1:3, 1:3] == c.transparent_id).all()


def test_unknown_color_error_hints_blank_spelling():
    c = make_canvas()
    with pytest.raises(ValueError) as ei:
        c.set_pixel(0, 0, "ERASE")
    msg = str(ei.value)
    assert "'transparent'" in msg and "no quotes" in msg
    with pytest.raises(ValueError) as ei2:
        c.paint_region(0, 0, [["KEEP"]])
    assert "no quotes" in str(ei2.value)


def test_paint_region_keep_erase():
    c = make_canvas()
    c.paint_rect(0, 0, 4, 4, "red")
    c.paint_region(1, 1, [
        [KEEP, "blue", ERASE],
        [ERASE, "blue", KEEP],
    ])
    red = c.palette._resolve_id("red")
    blue = c.palette._resolve_id("blue")
    assert c.matrix[1, 1] == red               # KEEP -> untouched
    assert c.matrix[2, 3] == red               # KEEP -> untouched
    assert c.matrix[1, 2] == blue
    assert c.matrix[2, 2] == blue
    assert c.matrix[1, 3] == c.transparent_id  # ERASE
    assert c.matrix[2, 1] == c.transparent_id  # ERASE


def test_stamp_keep_erase():
    c = make_canvas()
    c.paint_rect(0, 0, 5, 5, "red")
    c.stamp([
        [KEEP, ERASE, "blue"],
        ["blue", "blue", KEEP],
    ], 1, 1)
    red = c.palette._resolve_id("red")
    blue = c.palette._resolve_id("blue")
    assert c.matrix[1, 1] == red               # KEEP
    assert c.matrix[1, 2] == c.transparent_id  # ERASE
    assert c.matrix[1, 3] == blue
    assert c.matrix[2, 1] == blue
    assert c.matrix[2, 2] == blue
    assert c.matrix[2, 3] == red               # KEEP


def test_redraw_full_canvas():
    c = make_canvas()
    c.paint_rect(0, 0, 16, 16, "blue")  # pre-fill so KEEP has something to preserve
    rows = [
        [ERASE if (i + j) % 4 == 0 else ("red" if (i + j) % 2 == 0 else KEEP) for i in range(16)]
        for j in range(16)
    ]
    c.redraw(rows)
    red = c.palette._resolve_id("red")
    blue = c.palette._resolve_id("blue")
    assert c.matrix[0, 0] == c.transparent_id  # (0,0): ERASE
    assert c.matrix[0, 2] == red               # (2,0): red
    assert c.matrix[1, 0] == blue              # (0,1): KEEP -> unchanged


def test_redraw_requires_full_matrix():
    c = make_canvas()
    with pytest.raises(CanvasError):
        c.redraw([["red"]])                    # 1x1 != 16x16
    with pytest.raises(CanvasError):
        c.redraw([["red"] * 16] * 15)          # 15 rows != 16
    with pytest.raises(CanvasError):
        c.redraw([])                           # empty


def test_observe_region_modes():
    c = make_canvas()
    c.paint_rect(0, 0, 2, 2, "red")
    m = c.observe_region(0, 0, 4, 4, mode="matrix", color_as="id")
    assert "region (0,0)-(3,3)" in m
    with pytest.raises(CanvasError):
        c.observe_region(0, 0, 4, 4, mode="ascii")  # luminance ascii removed
    co = c.observe_region(0, 0, 4, 4, mode="counts")
    assert "red" in co
    out = c.observe_region(0, 0, 100, 100, mode="matrix", max_cells=100)
    assert "too large" in out


def test_stats_and_bbox():
    c = make_canvas()
    assert c.stats()["used_pixels"] == 0
    c.paint_rect(2, 3, 4, 5, "red")
    st = c.stats()
    assert st["used_pixels"] == 20
    assert st["bbox"] == [2, 3, 5, 7]
    assert st["color_counts"] == {"red": 20}


def test_to_dict_roundtrip():
    c = make_canvas()
    c.paint_circle(8, 8, 5, "blue")
    d = c.to_dict()
    c2 = PixelCanvas.from_dict(d)
    assert np.array_equal(c.matrix, c2.matrix)
    assert c2.palette.names() == c.palette.names()


def test_from_dict_rejects_bad_size():
    d = {"width": 4, "height": 4, "palette": [{"id": 0, "name": "transparent", "rgba": [0, 0, 0, 0]}],
         "transparent_id": 0, "canvas": [[0, 0], [0, 0]]}
    with pytest.raises(CanvasError):
        PixelCanvas.from_dict(d)


def test_region_ops_copy_mirror_shift():
    c = make_canvas()
    c.paint_rect(0, 0, 3, 3, "red")
    c.copy_region((0, 0, 3, 3), (5, 5))
    assert c.matrix[6, 6] == c.palette._resolve_id("red")
    c2 = make_canvas()
    c2.paint_rect(0, 0, 2, 2, "blue")
    c2.mirror_region((0, 0, 2, 2), "h", (0, 0))
    assert c2.matrix[1, 0] == c2.matrix[1, 1]
    c3 = make_canvas()
    c3.paint_rect(1, 1, 2, 2, "red")
    c3.shift_region(0, 0, 5, 5, 1, 1)
    assert c3.matrix[2, 2] == c3.palette._resolve_id("red")
    assert c3.matrix[1, 1] == c3.transparent_id


def test_dither_and_outline():
    c = make_canvas()
    c.paint_rect(2, 2, 6, 6, "red")
    c.dither_region(2, 2, 6, 6, ["red", "blue"], pattern="checker")
    assert c.matrix[2, 2] != c.matrix[2, 3]
    c2 = make_canvas()
    c2.paint_rect(3, 3, 6, 6, "red")
    c2.outline_region(0, 0, 16, 16, "blue")
    assert c2.matrix[3, 3] == c2.palette._resolve_id("blue")  # top-left corner outlined
    assert c2.matrix[5, 5] == c2.palette._resolve_id("red")  # interior untouched


def test_flood_fill():
    c = make_canvas()
    c.paint_rect(4, 4, 8, 8, "red")
    res = c.flood_fill(5, 5, "blue")
    assert res["changed"] == 64
    assert c.matrix[5, 5] == c.palette._resolve_id("blue")
    assert c.matrix[2, 2] == c.transparent_id  # outside untouched


# ----------------------------------------------------------------------
# undo_step / undo_round
# ----------------------------------------------------------------------
def test_undo_step_reverts_last_call():
    c = make_canvas()
    c.mark_call()  # state before the call
    c.paint_rect(0, 0, 4, 4, "red")
    assert c.matrix[2, 2] == c.palette._resolve_id("red")
    r = c.undo_step()
    assert r["op"] == "undo_step" and r["restored"] == 1
    assert c.matrix[2, 2] == c.transparent_id  # rect gone


def test_undo_step_nothing_to_undo():
    c = make_canvas()
    r = c.undo_step()
    assert r["restored"] == 0


def test_undo_step_reverts_palette_call():
    c = make_canvas()
    c.mark_call()
    cid = c.register_color("leaf", "#3f9b4f")
    assert cid in c.palette.ids()
    c.undo_step()
    assert cid not in c.palette.ids()  # palette-only call is reverted too
    assert "leaf" not in c.palette.names()


def test_undo_step_walks_back_one_call_at_a_time():
    c = make_canvas()
    c.mark_call()
    c.paint_rect(0, 0, 2, 2, "red")
    c.mark_call()
    c.paint_rect(5, 5, 2, 2, "blue")
    c.undo_step()
    assert c.matrix[6, 6] == c.transparent_id  # second rect gone
    assert c.matrix[1, 1] == c.palette._resolve_id("red")  # first rect kept
    c.undo_step()
    assert c.matrix[1, 1] == c.transparent_id  # first rect gone too


def test_undo_round_reverts_previous_round():
    c = make_canvas()
    # the harness records mark_round() at the *start* of every executed
    # block; here we simulate three blocks:
    c.mark_round()  # round 1 starts (state = initial)
    c.mark_call()
    c.paint_rect(0, 0, 2, 2, "red")  # round 1's work
    c.mark_round()  # round 2 starts (state after round 1)
    c.mark_call()
    c.paint_rect(6, 6, 2, 2, "blue")  # round 2's work
    c.mark_round()  # round 3 starts (state after round 2; current round)
    # undo_round() reverts the *previous* round (round 2) -> blue rect gone
    r = c.undo_round()
    assert r["op"] == "undo_round" and r["restored"] == 1
    assert c.matrix[7, 7] == c.transparent_id  # round-2 rect gone
    assert c.matrix[1, 1] == c.palette._resolve_id("red")  # round-1 rect kept


def test_undo_round_nothing_to_undo():
    c = make_canvas()
    c.mark_round()  # only the initial boundary
    r = c.undo_round()
    assert r["restored"] == 0
    assert c.undo_round()["restored"] == 0  # still nothing


def test_undo_round_walks_back_one_round_at_a_time():
    c = make_canvas()
    c.mark_round()  # boundary 0 (initial)
    c.mark_call()
    c.paint_rect(0, 0, 2, 2, "red")  # round 1
    c.mark_round()  # boundary 1
    c.mark_call()
    c.paint_rect(6, 6, 2, 2, "blue")  # round 2
    c.mark_round()  # boundary 2 (current)
    c.undo_round()
    assert c.matrix[7, 7] == c.transparent_id
    assert c.matrix[1, 1] == c.palette._resolve_id("red")
    c.undo_round()
    assert c.matrix[1, 1] == c.transparent_id  # round 1 also reverted
