"""PNG / PIL rendering of a PixelCanvas (nearest-neighbour, no AA)."""
from __future__ import annotations

import io
from typing import Optional, Sequence, Tuple

import numpy as np
from PIL import Image

from pixelbench.core.color import Palette


def _palette_to_image(canvas) -> Image.Image:
    """Render the integer-id matrix to an RGBA PIL image (1px per cell)."""
    pal = canvas.palette
    h, w = canvas.height, canvas.width
    data = np.zeros((h, w, 4), dtype=np.uint8)
    for cid in pal.ids():
        c = pal[cid]
        mask = canvas.matrix == cid
        if c.rgba[3] == 0:
            data[mask] = (0, 0, 0, 0)
        else:
            data[mask] = c.rgba
    return Image.fromarray(data, "RGBA")


def render_pil(canvas, scale: int = 8, grid: bool = False, checker: bool = False) -> Image.Image:
    """Upscale the canvas with NEAREST (crisp pixel edges, no smoothing).

    ``checker`` draws a light checkerboard behind transparent pixels so
    holes are visible in previews; the returned image stays RGBA.
    """
    if scale < 1:
        raise ValueError("scale must be >= 1")
    img = _palette_to_image(canvas)
    if scale > 1:
        img = img.resize((canvas.width * scale, canvas.height * scale), Image.NEAREST)
    if checker:
        base = checkerboard(canvas.width * scale, canvas.height * scale, cell=scale)
        base.alpha_composite(img)
        img = base
    if grid:
        img = _draw_grid(img, canvas, scale)
    return img


def render_png_bytes(canvas, scale: int = 8, grid: bool = False, checker: bool = False) -> bytes:
    buf = io.BytesIO()
    render_pil(canvas, scale=scale, grid=grid, checker=checker).save(buf, format="PNG")
    return buf.getvalue()


def checkerboard(w: int, h: int, cell: int = 8) -> Image.Image:
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    px = img.load()
    for y in range(0, h, cell):
        for x in range(0, w, cell):
            if ((x // cell) + (y // cell)) % 2 == 0:
                for yy in range(min(cell, h - y)):
                    for xx in range(min(cell, w - x)):
                        px[x + xx, y + yy] = (220, 220, 220, 255)
    return img


def _draw_grid(img: Image.Image, canvas, scale: int) -> Image.Image:
    from PIL import ImageDraw

    draw = ImageDraw.Draw(img, "RGBA")
    color = (120, 120, 120, 120)
    for i in range(1, canvas.width):
        x = i * scale
        draw.line([(x, 0), (x, img.height)], fill=color, width=1)
    for j in range(1, canvas.height):
        y = j * scale
        draw.line([(0, y), (img.width, y)], fill=color, width=1)
    return img


def load_png_as_canvas(
    path_or_img: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    max_colors: Optional[int] = None,
    transparent_rgba: Tuple[int, int, int, int] = (0, 0, 0, 0),
) -> "PixelCanvas":
    """Load a PNG (or PIL image) into a PixelCanvas.

    - The image is nearest-resized to ``(width, height)`` if given.
    - Pixels whose alpha == 0 become ``transparent``.
    - If the unique color count exceeds ``max_colors``, near-duplicate
      colors are greedily merged until the limit is satisfied.
    - Color names are auto-generated (``c0``, ``c1``, ...); callers that
      need semantic names should rebuild the palette afterwards.
    """
    from pixelbench.core.canvas import PixelCanvas

    if isinstance(path_or_img, (bytes, bytearray)):
        img = Image.open(io.BytesIO(bytes(path_or_img)))
    elif isinstance(path_or_img, str):
        img = Image.open(path_or_img)
    else:
        img = path_or_img
    img = img.convert("RGBA")
    if width is not None and height is not None:
        img = img.resize((int(width), int(height)), Image.NEAREST)
    w, h = img.size
    arr = np.asarray(img, dtype=np.int32).reshape(h, w, 4)

    # collect unique non-fully-transparent colors
    alpha = arr[:, :, 3]
    opaque = alpha > 0
    unique: list[Tuple[int, int, int, int]] = []
    counts: list[int] = []
    lookup: dict[Tuple[int, int, int, int], int] = {}
    for j in range(h):
        for i in range(w):
            if not opaque[j, i]:
                continue
            rgba = tuple(arr[j, i])
            if rgba in lookup:
                counts[lookup[rgba]] += 1
            else:
                lookup[rgba] = len(unique)
                unique.append(rgba)
                counts.append(1)

    if max_colors is not None and len(unique) > max_colors:
        merged_unique, _ = _merge_colors(unique, counts, max_colors)
        # original-color index -> merged-color index (nearest by distance;
        # merged colors are weighted averages so exact keys may not exist)
        index_map = [
            min(range(len(merged_unique)), key=lambda m, c=c: _rgba_dist(c, merged_unique[m]))
            for c in unique
        ]
        unique = merged_unique
    else:
        index_map = None

    return _build(width=w, height=h, arr=arr, unique=unique, orig_lookup=lookup, index_map=index_map)


def _build(width, height, arr, unique, orig_lookup, index_map) -> "PixelCanvas":
    from pixelbench.core.canvas import PixelCanvas
    from pixelbench.core.color import Color, Palette

    pal = Palette()
    trans_id = 0
    pal._add(Color(id=trans_id, name="transparent", rgba=(0, 0, 0, 0)))
    for k, rgba in enumerate(unique):
        pal._add(Color(id=k + 1, name=f"c{k}", rgba=tuple(int(c) for c in rgba)))
    canvas = PixelCanvas(width, height, palette=pal, transparent_id=trans_id)
    # arr has original (pre-merge) colors; remap via original index -> merged index
    for j in range(height):
        for i in range(width):
            rgba = tuple(arr[j, i])
            if rgba[3] == 0:
                canvas.matrix[j, i] = trans_id
            else:
                oi = orig_lookup[rgba]
                mi = index_map[oi] if index_map is not None else oi
                canvas.matrix[j, i] = mi + 1  # palette ids start at 1
    return canvas


def _merge_colors(colors: list, counts: list, limit: int) -> Tuple[list, list]:
    """Quantize to <= ``limit`` colors with median cut (O(N log N)).

    Replaces the old greedy nearest-pair merge (O(N^3)), which stalled on
    high-color images (e.g. 300+ colors).  Colors are split recursively on
    the widest RGBA channel's median until there are ``limit`` buckets;
    each bucket's representative is the pixel-count-weighted average.
    """
    if len(colors) <= limit:
        return list(colors), list(counts)
    buckets = [[(c, n) for c, n in zip(colors, counts)]]
    while len(buckets) < limit:
        # pick the bucket with the widest channel range that can still split
        best_i = -1
        best_key = (-1, -1)  # (range, size)
        for i, b in enumerate(buckets):
            if len(b) < 2:
                continue
            rng = _bucket_widest_range(b)
            if rng[0] > best_key[0]:
                best_key = (rng[0], len(b))
                best_i = i
        if best_i < 0:
            break  # nothing left to split
        b = buckets[best_i]
        channel = _bucket_widest_channel(b)
        b_sorted = sorted(b, key=lambda cn: cn[0][channel])
        mid = len(b_sorted) // 2
        buckets[best_i : best_i + 1] = [b_sorted[:mid], b_sorted[mid:]]
    merged = []
    merged_counts = []
    for b in buckets:
        tot = sum(n for _, n in b)
        rep = tuple(round(sum(c[k] * n for c, n in b) / tot) for k in range(4))
        merged.append(rep)
        merged_counts.append(tot)
    return merged, merged_counts


def _bucket_widest_channel(bucket: list) -> int:
    chans = [0, 1, 2, 3]
    return max(chans, key=lambda k: max(c[k] for c, _ in bucket) - min(c[k] for c, _ in bucket))


def _bucket_widest_range(bucket: list) -> Tuple[int, int]:
    chans = [0, 1, 2, 3]
    return max(max(c[k] for c, _ in bucket) - min(c[k] for c, _ in bucket) for k in chans), len(bucket)


def _rgba_dist(a: Sequence[int], b: Sequence[int]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b))
