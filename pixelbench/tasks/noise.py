"""Noise-based corruption for restoration tasks.

Whereas :mod:`pixelbench.tasks.masks` produces *boolean* erased regions
(the classic "missing block" damage), this module produces **noise
corruption** applied to an existing canvas: random colour swaps, gaussian
colour jitter, random blocks, or stripes.

Design rules
------------
* Every function takes a ``canvas`` (``PixelCanvas``) and returns a
  **copy** corrupted in place of the input — the input is never mutated.
* Corruption is limited to an optional ``mask`` region (bool array of the
  canvas shape, ``True`` = damage here).  ``mask=None`` corrupts the whole
  canvas.
* Colours are drawn from the canvas' **existing palette** (excluding
  transparent), so ``max_colors`` stays satisfied and the restored target
  palette is unchanged — the model's job is to undo noise, not to invent
  new colours.

Implemented on request (multiple damage/noise forms for different
difficulties); NOT yet wired into task generation — the user decides how
to apply them.
"""
from __future__ import annotations

import random
from typing import Optional

import numpy as np

from pixelbench.core.canvas import PixelCanvas


def _region(canvas: PixelCanvas, mask: Optional[np.ndarray]) -> np.ndarray:
    if mask is None:
        return np.ones((canvas.height, canvas.width), dtype=bool)
    mask = np.asarray(mask, dtype=bool)
    if mask.shape != (canvas.height, canvas.width):
        raise ValueError(
            f"mask shape {mask.shape} != canvas {canvas.width}x{canvas.height}"
        )
    return mask


def _palette_ids(canvas: PixelCanvas) -> list:
    """Colour ids available for noise (everything except transparent)."""
    return [
        cid
        for cid in canvas.palette.ids()
        if cid != canvas.transparent_id and canvas.palette[cid].rgba[3] > 0
    ]


def salt_pepper_noise(
    canvas: PixelCanvas,
    mask: Optional[np.ndarray] = None,
    amount: float = 0.1,
    seed: int = 0,
    pepper_only: bool = False,
) -> PixelCanvas:
    """Salt-and-pepper noise inside ``mask``.

    A random ``amount`` fraction of the region's pixels are flipped to a
    random *other* palette colour (pepper), or to transparent (salt) when
    ``pepper_only=False``.  Transparent pixels are never salted to keep the
    damage meaningful.  Returns a corrupted copy.
    """
    region = _region(canvas, mask)
    rng = random.Random(seed)
    out = canvas.copy()
    ids = _palette_ids(out)
    if not ids:
        return out
    ys, xs = np.nonzero(region)
    n = max(0, int(round(len(ys) * amount)))
    if n == 0:
        return out
    idx = rng.sample(range(len(ys)), min(n, len(ys)))
    for i in idx:
        y, x = int(ys[i]), int(xs[i])
        if pepper_only:
            out.matrix[y, x] = rng.choice(ids)
        else:
            # salt = transparent (only where a pixel currently exists),
            # pepper = random palette colour
            if out.matrix[y, x] == out.transparent_id or rng.random() < 0.5:
                out.matrix[y, x] = rng.choice(ids)
            else:
                out.matrix[y, x] = out.transparent_id
    return out


def gaussian_noise(
    canvas: PixelCanvas,
    mask: Optional[np.ndarray] = None,
    sigma: float = 20.0,
    seed: int = 0,
) -> PixelCanvas:
    """Gaussian colour jitter inside ``mask``.

    For each damaged pixel, its RGB is shifted by a gaussian draw
    ``N(0, sigma)`` per channel and snapped back to the **nearest** existing
    palette colour (so the palette never grows).  Transparent pixels are
    left untouched.  Returns a corrupted copy.
    """
    region = _region(canvas, mask)
    rng = np.random.default_rng(seed)
    out = canvas.copy()
    ids = _palette_ids(out)
    if not ids:
        return out
    rgba = {cid: np.asarray(out.palette[cid].rgba[:3], dtype=float) for cid in ids}
    id_list = ids
    ys, xs = np.nonzero(region)
    for y, x in zip(ys, xs):
        y, x = int(y), int(x)
        cid = int(out.matrix[y, x])
        if cid == out.transparent_id:
            continue
        base = rgba.get(cid)
        if base is None:
            continue
        noisy = base + rng.normal(0.0, sigma, size=3)
        # nearest palette colour by euclidean distance in RGB
        best, best_cid = None, None
        for pcid in id_list:
            d = float(np.sum((rgba[pcid] - noisy) ** 2))
            if best is None or d < best:
                best, best_cid = d, pcid
        out.matrix[y, x] = best_cid
    return out


def block_noise(
    canvas: PixelCanvas,
    mask: Optional[np.ndarray] = None,
    block_size: int = 4,
    n_blocks: Optional[int] = None,
    seed: int = 0,
) -> PixelCanvas:
    """Random solid blocks of wrong colours inside ``mask``.

    ``n_blocks`` solid ``block_size`` squares are dropped at random
    positions within the region, each filled with a random palette colour
    (distinct from its originals).  Defaults to enough blocks to cover
    roughly 20% of the region.  Returns a corrupted copy.
    """
    region = _region(canvas, mask)
    rng = random.Random(seed)
    out = canvas.copy()
    ids = _palette_ids(out)
    if not ids:
        return out
    region_pts = np.nonzero(region)
    if n_blocks is None:
        n_blocks = max(1, int(round(0.2 * len(region_pts[0]) / (block_size * block_size))))
    for _ in range(n_blocks):
        # pick an anchor point inside the region
        j = rng.randrange(len(region_pts[0]))
        x0 = int(region_pts[1][j])
        y0 = int(region_pts[0][j])
        colour = rng.choice(ids)
        for dy in range(block_size):
            for dx in range(block_size):
                x, y = x0 + dx, y0 + dy
                if 0 <= x < out.width and 0 <= y < out.height and region[y, x]:
                    out.matrix[y, x] = colour
    return out


def stripe_noise(
    canvas: PixelCanvas,
    mask: Optional[np.ndarray] = None,
    axis: str = "h",
    count: int = 4,
    thickness: int = 2,
    seed: int = 0,
) -> PixelCanvas:
    """Horizontal (``axis='h'``) or vertical (``axis='v'``) stripes of
    wrong colours inside ``mask``.

    ``count`` stripes each ``thickness`` px wide, spaced roughly evenly
    across the damaged region, each filled with a random palette colour.
    Returns a corrupted copy.
    """
    if axis not in ("h", "v"):
        raise ValueError(f"axis must be 'h' or 'v', got {axis!r}")
    region = _region(canvas, mask)
    rng = random.Random(seed)
    out = canvas.copy()
    ids = _palette_ids(out)
    if not ids:
        return out
    if axis == "h":
        for y in range(out.height):
            if (y // thickness) % max(1, count * 2) < count and region[y, :].any():
                colour = rng.choice(ids)
                out.matrix[y, region[y, :]] = colour
    else:
        for x in range(out.width):
            if (x // thickness) % max(1, count * 2) < count and region[:, x].any():
                colour = rng.choice(ids)
                out.matrix[region[:, x], x] = colour
    return out


def corrupt_canvas(
    canvas: PixelCanvas,
    kind: str,
    mask: Optional[np.ndarray] = None,
    seed: int = 0,
    **kwargs,
) -> PixelCanvas:
    """Dispatch helper: corrupt ``canvas`` with noise of the given ``kind``.

    Supported kinds: ``salt_pepper``, ``gaussian``, ``block``, ``stripe``.
    Extra keyword args are forwarded to the specific function.  Returns a
    corrupted copy (never mutates the input).
    """
    fn = {
        "salt_pepper": salt_pepper_noise,
        "gaussian": gaussian_noise,
        "block": block_noise,
        "stripe": stripe_noise,
    }.get(kind)
    if fn is None:
        raise ValueError(
            f"unknown noise kind {kind!r}; choose from "
            f"{sorted(('salt_pepper', 'gaussian', 'block', 'stripe'))}"
        )
    return fn(canvas, mask=mask, seed=seed, **kwargs)
