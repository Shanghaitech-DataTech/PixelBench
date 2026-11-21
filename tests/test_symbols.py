"""Tests for the two-level palette symbol format (see palette_symbols_design_zh.md)."""
import random

import numpy as np
import pytest

from pixelbench.core import symbols as S


def _rand_palette(n):
    rng = random.Random(7)
    return [(0, 0, 0, 0)] + [
        (rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255), 255)
        for _ in range(n - 1)
    ]


def _rand_matrix(h, w, n_colors):
    rng = random.Random(3)
    return [[rng.randrange(n_colors) for _ in range(w)] for _ in range(h)]


def test_symbol_bounds():
    assert S.MAX_SINGLE == 86  # 62 ASCII (0-9 a-z A-Z) + 24 lowercase Greek
    assert S.symbol_for_id(0) == "0"
    assert S.symbol_for_id(9) == "9"
    assert S.symbol_for_id(10) == "a"
    assert S.symbol_for_id(35) == "z"
    assert S.symbol_for_id(36) == "A"
    assert S.symbol_for_id(61) == "Z"
    # ids 62..85 are lowercase Greek (first is alpha, last is omega)
    assert S.symbol_for_id(62) == "α"
    assert S.symbol_for_id(85) == "ω"
    assert S.symbol_for_id(86) == "56"
    assert S.symbol_for_id(255) == "ff"
    for i in range(256):
        assert S.id_for_symbol(S.symbol_for_id(i)) == i
    with pytest.raises(ValueError):
        S.symbol_for_id(256)
    with pytest.raises(ValueError):
        S.id_for_symbol("gg")


def test_legacy_36_single_char_round_trip():
    rgba = _rand_palette(36)
    mat = _rand_matrix(8, 10, 36)
    txt = S.encode_canvas(rgba, mat)
    # legacy format: every symbol is a single char, ids are 0-9a-z
    pal_block = txt.split("```color\n")[1].split("\n```")[0]
    syms = [ln.split("=")[0] for ln in pal_block.splitlines()]
    assert all(len(s) == 1 for s in syms)
    assert all(c in "0123456789abcdefghijklmnopqrstuvwxyz" for c in syms)
    img_line = txt.split("```image\n")[1].split("\n```")[0].splitlines()[0]
    assert len(img_line) == 10  # one char per pixel
    rgba2, mat2 = S.decode_canvas(txt)
    assert rgba2 == rgba
    assert mat2 == mat


def test_86_boundary_stays_single_char():
    rgba = _rand_palette(86)
    mat = _rand_matrix(6, 6, 86)
    txt = S.encode_canvas(rgba, mat)
    pal_block = txt.split("```color\n")[1].split("\n```")[0]
    assert all(len(ln.split("=")[0]) == 1 for ln in pal_block.splitlines())
    rgba2, mat2 = S.decode_canvas(txt)
    assert rgba2 == rgba and mat2 == mat


def _det_palette(n):
    """n unique colors (deterministic)."""
    return [(0, 0, 0, 0)] + [(i * 7 % 256, i * 13 % 256, i * 29 % 256, 255) for i in range(1, n)]


def test_level_b_uniform_two_char_hex():
    rgba = _det_palette(87)
    mat = _rand_matrix(5, 6, 87)
    txt = S.encode_canvas(rgba, mat)
    pal_block = txt.split("```color\n")[1].split("\n```")[0]
    syms = [ln.split("=")[0] for ln in pal_block.splitlines()]
    assert all(len(s) == 2 for s in syms), "level B palette must be uniformly 2-char"
    assert syms[0] == "00" and syms[86] == "56"
    img_line = txt.split("```image\n")[1].split("\n```")[0].splitlines()[0]
    assert len(img_line) == 12  # 6 pixels x 2 chars
    rgba2, mat2 = S.decode_canvas(txt)
    assert rgba2 == rgba and mat2 == mat


def test_max_256_colors_round_trip():
    rgba = _det_palette(256)
    # 16x16 matrix covering every id exactly once
    mat = [[r * 16 + c for c in range(16)] for r in range(16)]
    txt = S.encode_canvas(rgba, mat)
    rgba2, mat2 = S.decode_canvas(txt)
    assert rgba2 == rgba and mat2 == mat
    assert sorted({v for row in mat2 for v in row}) == list(range(256))


def test_mixed_ids_in_level_b():
    rgba = _rand_palette(90)
    mat = [[86 if (i + j) % 3 == 0 else 1 for j in range(8)] for i in range(6)]
    txt = S.encode_canvas(rgba, mat)
    rgba2, mat2 = S.decode_canvas(txt)
    assert mat2 == mat and rgba2 == rgba


def test_parse_rejects_mixed_width_palette():
    # hand-crafted mixed-width palette must be rejected by the parser
    with pytest.raises(ValueError):
        S.parse_image_block("01\n02", {"0": 0, "01": 1})
