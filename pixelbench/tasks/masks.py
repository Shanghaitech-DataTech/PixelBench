"""Mask generation for restoration tasks.

Two families of generators:

* **Boolean masks** (``*_mask``) — ``True`` marks the erased/damaged
  region that the model may repair.  These plug straight into
  ``TaskSpec.mask`` and ``apply_mask``.
* **Noise / corruption** lives in :mod:`pixelbench.tasks.noise`
  (``salt_pepper_noise`` / ``gaussian_noise`` / ``block_noise`` /
  ``stripe_noise``) and operates on a *copy* of a canvas, so the
  palette and the visible region stay under the caller's control.

The mask helpers here span several difficulty regimes:

* small localised damage — :func:`rect_mask`, :func:`circle_mask`,
  :func:`blob_mask` (existing);
* MAE-style very-large-coverage masks — :func:`mae_mask`,
  :func:`large_blob_mask`, :func:`scattered_mask` (added for the
  "hard / MAE-style" difficulty tier; implemented but not yet wired
  into task generation).
"""
from __future__ import annotations

import math
import random
from typing import List, Optional, Tuple

import numpy as np


def rect_mask(width: int, height: int, box: Tuple[int, int, int, int]) -> np.ndarray:
    x, y, w, h = box
    mask = np.zeros((height, width), dtype=bool)
    mask[max(0, y) : min(height, y + h), max(0, x) : min(width, x + w)] = True
    return mask


def circle_mask(width: int, height: int, cx: int, cy: int, r: int) -> np.ndarray:
    ys, xs = np.mgrid[0:height, 0:width]
    return (xs - cx) ** 2 + (ys - cy) ** 2 <= r * r


def blob_mask(width: int, height: int, cx: int, cy: int, r: int, seed: int = 0, n_arms: int = 5) -> np.ndarray:
    """Irregular blob: center circle plus a few random arms."""
    rng = random.Random(seed)
    ys, xs = np.mgrid[0:height, 0:width]
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    mask = dist <= r
    for _ in range(n_arms):
        ang = rng.uniform(0, 2 * np.pi)
        arm_len = r * rng.uniform(0.6, 1.3)
        ex = cx + int(round(arm_len * np.cos(ang)))
        ey = cy + int(round(arm_len * np.sin(ang)))
        mask |= circle_mask(width, height, ex, ey, max(1, int(r * 0.45)))
    return mask


def border_mask(width: int, height: int, thickness: int) -> np.ndarray:
    mask = np.zeros((height, width), dtype=bool)
    mask[:thickness, :] = True
    mask[-thickness:, :] = True
    mask[:, :thickness] = True
    mask[:, -thickness:] = True
    return mask


def mask_bbox(mask: np.ndarray) -> Optional[List[int]]:
    ys, xs = np.nonzero(mask)
    if len(ys) == 0:
        return None
    return [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]


# ---------------------------------------------------------------------------
# MAE-style large-coverage masks ("hard" difficulty tier)
#
# Implemented on request (multiple mask forms for different difficulties);
# NOT yet wired into task generation — the user decides how to apply them.
# ---------------------------------------------------------------------------


def mae_mask(
    width: int,
    height: int,
    mask_ratio: float = 0.75,
    patch_size: int = 16,
    seed: int = 0,
) -> np.ndarray:
    """MAE-style mask: split the canvas into a non-overlapping patch grid and
    randomly keep a small fraction of patches, masking the rest.

    Following He et al. (MAE), the default keeps only ``1 - mask_ratio`` of
    the patches visible (e.g. 25% visible / 75% masked) — a very large,
    "hard" erased area.  Trailing patches are clipped to the canvas edge.

    Returns a bool array of shape ``(height, width)`` with ``True`` = erased.
    """
    rng = random.Random(seed)
    npx = max(1, math.ceil(width / patch_size))
    npy = max(1, math.ceil(height / patch_size))
    n_total = npx * npy
    n_keep = max(1, int(round(n_total * (1 - mask_ratio))))
    keep = set(rng.sample(range(n_total), n_keep))
    mask = np.zeros((height, width), dtype=bool)
    for iy in range(npy):
        for ix in range(npx):
            if (iy * npx + ix) in keep:
                continue
            y0, y1 = iy * patch_size, min(height, (iy + 1) * patch_size)
            x0, x1 = ix * patch_size, min(width, (ix + 1) * patch_size)
            mask[y0:y1, x0:x1] = True
    return mask


def large_blob_mask(
    width: int,
    height: int,
    frac: float = 0.5,
    seed: int = 0,
    n_arms: int = 8,
) -> np.ndarray:
    """A single large irregular blob covering roughly ``frac`` of the canvas.

    The blob is a big center disc plus several random arms (reuses
    :func:`blob_mask` internals but targets a much larger coverage than the
    original small-region use).  Useful as an "MAE-style but contiguous"
    hard mask.  Returns a bool array of shape ``(height, width)``.
    """
    rng = random.Random(seed)
    area = frac * width * height
    r = max(1, int(round(math.sqrt(area / math.pi))))
    cx = rng.randint(0, max(0, width - 1))
    cy = rng.randint(0, max(0, height - 1))
    return blob_mask(width, height, cx, cy, r, seed=seed, n_arms=n_arms)


def scattered_mask(
    width: int,
    height: int,
    n_regions: int = 6,
    total_frac: float = 0.5,
    seed: int = 0,
) -> np.ndarray:
    """Several medium-to-large scattered blobs whose combined coverage is
    roughly ``total_frac`` of the canvas.

    Each region is an irregular blob (reuses :func:`blob_mask`) placed at a
    random position; this mimics "damage spread over many disconnected large
    areas".  Returns a bool array of shape ``(height, width)``.
    """
    rng = random.Random(seed)
    mask = np.zeros((height, width), dtype=bool)
    per = total_frac / n_regions
    for i in range(n_regions):
        area = per * width * height
        r = max(1, int(round(math.sqrt(area / math.pi))))
        cx = rng.randint(0, max(0, width - 1))
        cy = rng.randint(0, max(0, height - 1))
        mask |= blob_mask(
            width,
            height,
            cx,
            cy,
            r,
            seed=seed * 100 + i,
            n_arms=rng.randint(3, 7),
        )
    return mask


def content_mask(canvas, transparent_id: int = 0) -> np.ndarray:
    return canvas.matrix != transparent_id


def apply_mask(canvas, mask: np.ndarray, fill_id: int = 0) -> None:
    """Erase (in place) the masked region of a canvas."""
    canvas.matrix[mask] = fill_id
