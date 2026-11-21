import numpy as np

from pixelbench.core.font5x7 import GLYPH_H, GLYPH_W, draw_text, glyph, text_width


def test_glyph_a_shape():
    rows = glyph("A")
    assert len(rows) == GLYPH_H
    assert rows[0] == 0x0E  # .XXX.
    assert rows[3] == 0x1F  # XXXXX (middle row is the crossbar)


def test_glyph_lowercase_maps_to_upper():
    assert glyph("a") == glyph("A")


def test_text_width():
    assert text_width("A") == 5
    assert text_width("AB", spacing=1) == 5 + 1 + 5


def test_draw_text_pixels():
    c = np.zeros((12, 30), dtype=np.int32)
    n = draw_text(c, 2, 2, "HI", 7)
    assert n > 0
    assert c[2, 2] == 7  # 'H' left stem, top row
    assert c[2, 6] == 7  # 'H' right stem, top row
    assert c[2, 2 + GLYPH_W + 1 + 1] == 7  # 'I' first painted column (col 1)


def test_draw_text_clips_off_canvas():
    c = np.zeros((6, 6), dtype=np.int32)
    n = draw_text(c, -2, -2, "ABC", 1)  # mostly off-canvas, must not crash
    assert n >= 0


def test_fallback_block():
    assert glyph("©") == (0x1F,) * GLYPH_H
