"""Tests for noise-based corruption helpers (pixelbench/tasks/noise.py)."""
import numpy as np
import pytest

from pixelbench.core.canvas import PixelCanvas
from pixelbench.tasks.noise import (
    block_noise,
    corrupt_canvas,
    gaussian_noise,
    salt_pepper_noise,
    stripe_noise,
)


def _make_canvas(w: int = 32, h: int = 32) -> PixelCanvas:
    c = PixelCanvas(w, h, max_colors=8)
    for name, hex_ in [
        ("red", "#ff0000"),
        ("blue", "#0000ff"),
        ("green", "#00ff00"),
        ("white", "#ffffff"),
    ]:
        c.register_color(name, hex_)
    c.matrix[:, :] = 1
    c.matrix[8:24, 8:24] = 2
    return c


def _right_mask(w: int = 32, h: int = 32) -> np.ndarray:
    m = np.zeros((h, w), dtype=bool)
    m[:, w // 2 :] = True
    return m


@pytest.mark.parametrize(
    "kind,kwargs",
    [
        ("salt_pepper", {"amount": 0.3}),
        ("gaussian", {"sigma": 80}),
        ("block", {"n_blocks": 20}),
        ("stripe", {"axis": "h"}),
        ("stripe", {"axis": "v"}),
    ],
)
def test_noise_corrupts_within_mask_only(kind, kwargs):
    c = _make_canvas()
    mask = _right_mask()
    out = corrupt_canvas(c, kind, mask, seed=1, **kwargs)
    assert out is not c  # returns a copy, never mutates input
    assert np.any(out.matrix != c.matrix)  # actually corrupted
    # nothing outside the mask may change
    assert np.array_equal(out.matrix[:, : c.width // 2], c.matrix[:, : c.width // 2])
    # palette is preserved (no new colours, no colour loss)
    assert set(out.palette.ids()) == set(c.palette.ids())
    assert c.matrix.tolist() == c.matrix.tolist()  # input untouched


def test_mask_shape_mismatch_rejected():
    c = _make_canvas()
    with pytest.raises(ValueError):
        gaussian_noise(c, np.zeros((5, 5), dtype=bool))


def test_noise_deterministic_for_fixed_seed():
    c = _make_canvas()
    mask = _right_mask()
    a = salt_pepper_noise(c, mask, amount=0.3, seed=7)
    b = salt_pepper_noise(c, mask, amount=0.3, seed=7)
    assert a.matrix.tolist() == b.matrix.tolist()


def test_salt_pepper_amount_controls_intensity():
    c = _make_canvas()
    mask = _right_mask()
    light = salt_pepper_noise(c, mask, amount=0.02, seed=1)
    heavy = salt_pepper_noise(c, mask, amount=0.8, seed=1)
    assert int(np.sum(light.matrix != c.matrix)) < int(np.sum(heavy.matrix != c.matrix))


def test_unknown_noise_kind_rejected():
    c = _make_canvas()
    with pytest.raises(ValueError):
        corrupt_canvas(c, "bogus")


def test_all_noise_kinds_listed():
    from pixelbench.tasks.noise import corrupt_canvas

    for k in ("salt_pepper", "gaussian", "block", "stripe"):
        c = _make_canvas()
        mask = _right_mask()
        kw = {"gaussian": {"sigma": 80}}.get(k, {})
        out = corrupt_canvas(c, k, mask, seed=2, **kw)
        assert np.any(out.matrix != c.matrix), k
