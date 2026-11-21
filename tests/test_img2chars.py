"""Tests for image -> character-art conversion (pixelbench.core.img2chars)."""
import io

import numpy as np
import pytest
from PIL import Image

from pixelbench.core import img2chars as C
from pixelbench.core import symbols as S


def _png_bytes(rgba_hw: np.ndarray) -> bytes:
    img = Image.fromarray(np.asarray(rgba_hw, dtype=np.uint8), "RGBA")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def _rgb_img(w: int, h: int, fill=(120, 130, 140)) -> bytes:
    img = Image.new("RGB", (w, h), fill)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def test_basic_conversion_and_roundtrip():
    data = np.zeros((5, 5, 4), dtype=np.uint8)
    data[:] = (255, 255, 255, 0)  # transparent background
    data[1:4, 1:4] = (27, 42, 53, 255)
    data[2, 2] = (228, 59, 68, 255)

    ca = C.convert_image(_png_bytes(data))
    assert (ca.width, ca.height) == (5, 5)
    assert ca.level == "single"
    assert ca.n_colors == 3
    # transparent background must be the trailing (worst-symbol) entry
    assert ca.colors[-1] == (0, 0, 0, 0)
    assert ca.colors[0] == (27, 42, 53, 255)  # most frequent first
    # chars grid: transparent = '2', navy = '0', red dot = '1'
    assert ca.chars().splitlines() == ["22222", "20002", "20102", "20002", "22222"]
    # canonical block round-trips exactly through the standard parser
    rgba, matrix = S.decode_canvas(ca.canonical())
    assert [tuple(int(v) for v in c) for c in rgba] == ca.colors
    assert matrix == ca.matrix
    # text artifacts exist and mention the colors
    assert "#1B2A35" in ca.legend() and "transparent" in ca.legend()
    assert 'register_color("c0", "#1B2A35")' in ca.register_code()
    assert ca.preview_png_bytes().startswith(b"\x89PNG")


def test_opaque_only_no_transparent_entry():
    ca = C.convert_image(_rgb_img(4, 3, fill=(10, 20, 30)))
    assert ca.n_colors == 1
    assert ca.colors == [(10, 20, 30, 255)]
    assert ca.chars() == "0000\n0000\n0000"


def test_not_png_rejected():
    img = Image.new("RGB", (4, 4), (1, 2, 3))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    with pytest.raises(C.CharArtError, match="PNG"):
        C.convert_image(buf.getvalue())


def test_too_large_rejected():
    big = np.zeros((300, 16, 4), dtype=np.uint8)
    big[..., 3] = 255
    with pytest.raises(C.CharArtError, match="256"):
        C.convert_image(_png_bytes(big))


def test_color_limit_strict_then_quantize():
    rng = np.random.RandomState(0)
    img64 = rng.randint(0, 256, size=(8, 8, 4)).astype(np.uint8)
    img64[..., 3] = 255
    unique = len(np.unique(img64[..., :3].reshape(-1, 3), axis=0))
    assert unique >= 64
    with pytest.raises(C.CharArtError, match="colors, more than the limit"):
        C.convert_image(_png_bytes(img64))
    ca = C.convert_image(_png_bytes(img64), quantize=True, max_colors=20)
    assert ca.n_colors <= 20
    assert ca.level == "single"
    # quantized result is still parseable
    S.decode_canvas(ca.canonical())


def test_87_color_hex_level():
    # 87 distinct colors -> level B (two-char hex), still parseable
    rng = np.random.RandomState(3)
    colors = rng.randint(0, 256, size=(87, 3)).astype(np.uint8)
    img = np.zeros((16, 16, 4), dtype=np.uint8)
    idx = (np.arange(256).reshape(16, 16)) % 87  # ids 0..86
    assert len(np.unique(idx)) == 87
    img[..., :3] = colors[idx]
    img[..., 3] = 255
    ca = C.convert_image(_png_bytes(img), max_colors=None)
    assert ca.n_colors == 87
    assert ca.level == "hex"
    assert all(len(s) == 2 for s in ca.symbols)
    rgba, matrix = S.decode_canvas(ca.canonical())
    assert len(rgba) == 87 and matrix == ca.matrix


def test_86_color_single_level_greek():
    # 86 distinct colors -> level A single char; the 24 extra symbols beyond
    # ASCII (ids 62..85) are lowercase Greek and must round-trip
    rng = np.random.RandomState(5)
    colors = rng.randint(0, 256, size=(86, 3)).astype(np.uint8)
    img = np.zeros((16, 16, 4), dtype=np.uint8)
    idx = (np.arange(256).reshape(16, 16)) % 86  # ids 0..85
    assert len(np.unique(idx)) == 86
    img[..., :3] = colors[idx]
    img[..., 3] = 255
    ca = C.convert_image(_png_bytes(img), max_colors=None)
    assert ca.n_colors == 86
    assert ca.level == "single"
    assert all(len(s) == 1 for s in ca.symbols)
    assert ca.symbols[62] == "α" and ca.symbols[85] == "ω"
    rgba, matrix = S.decode_canvas(ca.canonical())
    assert len(rgba) == 86 and matrix == ca.matrix


def test_image_object_input_and_path():
    ca = C.convert_image(Image.new("RGB", (6, 6), (200, 100, 50)), require_png=False)
    assert (ca.width, ca.height) == (6, 6)
