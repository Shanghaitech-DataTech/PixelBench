"""PNG pixel-art image -> canonical character-art text converter.

This standardizes the "image -> character art" flow used whenever a
*text-only* model needs to "see" a pixel-art image (no vision).  It wraps
the three steps of the existing pipeline on top of the canonical two-level
symbol mapping (``pixelbench.core.symbols``):

1. **Extract colors** -- decode the PNG, collect the unique RGBA
   colors, order most-frequent-first (ties broken by first occurrence);
   fully-transparent pixels collapse into a single trailing "transparent"
   palette entry so a transparent background never wastes the best symbols.
   Optionally quantize down to a color budget (median cut).
2. **Register colors** -- palette id == symbol index (0..n-1);
   produce ``register_color("c0", "#RRGGBB")`` snippet lines for the REPL
   kernel, plus a human-readable legend.
3. **Convert to character art** -- ``symbols.palette_block()`` +
   ``symbols.image_block()`` into the canonical ::

       ```color
       0=1A1C2CFF
       ...
       ```
       ```image
       01a...
       ```

   block (``<= 86`` colors: one ASCII char 0-9a-zA-Z or lowercase Greek per
   pixel; ``87..256`` colors: two-char hex per pixel).

Webapp/benchmark constraints enforced here (see the console tool spec):

* input must be PNG
* width/height ``<= 256``
* unique colors (transparent background included) within ``max_colors``
  (default ``MAX_COLORS``)

The strict path raises :class:`CharArtError` on violations; callers may opt
into quantization with ``quantize=True`` + ``max_colors``.
"""
from __future__ import annotations

import io
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
from PIL import Image

from pixelbench.core import symbols as S

#: tool spec: pixel art is at most 256x256
MAX_SIDE = 256
#: default conversion color budget (transparent background counted); level-A
#: single-char encoding itself covers up to ``SINGLE_LEVEL_MAX`` = 86 colors
MAX_COLORS = 63
#: level-A single-char encoding needs <= S.MAX_SINGLE (86) palette entries
SINGLE_LEVEL_MAX = S.MAX_SINGLE


class CharArtError(ValueError):
    """Raised when the input image violates the char-art constraints."""


# ----------------------------------------------------------------------
# result container
# ----------------------------------------------------------------------
@dataclass
class CharArt:
    """Result of converting a PNG pixel-art image into character art.

    ``colors[r]`` is the RGBA of palette id ``r`` (id == symbol index),
    ordered most-frequent-first except that a fully-transparent entry is
    always last.  ``counts`` mirrors ``colors``.
    """

    width: int
    height: int
    colors: List[Tuple[int, int, int, int]] = field(default_factory=list)
    counts: List[int] = field(default_factory=list)
    matrix: List[List[int]] = field(default_factory=list)
    level: str = "single"  # 'single' | 'hex'  (see symbols.py)

    # -- text views -----------------------------------------------------
    @property
    def n_colors(self) -> int:
        return len(self.colors)

    @property
    def symbols(self) -> List[str]:
        """The symbol used for each palette id (id -> symbol).

        Uniform per palette level: single chars at 'single' level, two-char
        hex for every id at 'hex' level (matches ``palette_block`` so the
        palette width always equals the image block width).
        """
        wide = self.level == "hex"
        return [
            f"{i:02x}" if wide else S.symbol_for_id(i) for i in range(self.n_colors)
        ]

    def palette_block(self) -> str:
        """Canonical `````color````` lines (symbol=RRGGBBAA, no '#' prefix)."""
        return S.palette_block(self.colors)

    def image_block(self) -> str:
        """Canonical image lines (symbols wide: 1 or 2 chars per cell)."""
        return S.image_block(self.matrix, wide=(self.level == "hex"))

    def canonical(self) -> str:
        """The full `````color````` + `````image````` interchange block."""
        return S.encode_canvas(self.colors, self.matrix)

    def chars(self) -> str:
        """Plain grid of the char-art (one char per pixel when 'single')."""
        return S.image_block(self.matrix, wide=(self.level == "hex"))

    def legend(self) -> str:
        """Human/model readable palette legend: ``symbol=#rrggbbaa name count``."""
        lines = []
        for i, (rgba, cnt) in enumerate(zip(self.colors, self.counts)):
            sym = S.symbol_for_id(i)
            r, g, b, a = rgba
            alpha = "" if a == 255 else f"{a:02x}"
            label = "transparent" if a == 0 else self.name(i)
            lines.append(f"{sym}=#{r:02X}{g:02X}{b:02X}{alpha}  {label}  x{cnt}")
        return "\n".join(lines)

    def name(self, cid: int) -> str:
        return f"c{cid}"

    def register_code(self) -> str:
        """register_color() snippet so the palette can be re-created in a kernel."""
        lines = []
        for i, (r, g, b, a) in enumerate(self.colors):
            hexv = f"#{r:02X}{g:02X}{b:02X}" + ("" if a == 255 else f"{a:02X}")
            lines.append(f'register_color("{self.name(i)}", "{hexv}")')
        return "\n".join(lines)

    def preview_png_bytes(self, max_side: int = 512) -> bytes:
        """Render the palette+matrix at NEAREST scale (crisp pixels, no AA)."""
        h, w = self.height, self.width
        m = np.asarray(self.matrix, dtype=np.int32)
        rgba = np.zeros((h, w, 4), dtype=np.uint8)
        for i, c in enumerate(self.colors):
            rgba[m == i] = np.asarray(c, dtype=np.uint8)
        img = Image.fromarray(rgba, "RGBA")
        scale = max(1, min(8, max_side // max(w, h)))
        if scale > 1:
            img = img.resize((w * scale, h * scale), Image.NEAREST)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()


# ----------------------------------------------------------------------
# conversion
# ----------------------------------------------------------------------
def convert_image(
    source: Union[bytes, bytearray, str, Path, Image.Image],
    *,
    require_png: bool = True,
    max_side: int = MAX_SIDE,
    max_colors: Optional[int] = MAX_COLORS,
    quantize: bool = False,
) -> CharArt:
    """Convert a PNG pixel-art image into :class:`CharArt`.

    Parameters
    ----------
    source:
        PNG bytes / a path to a PNG / an already-open PIL image.
    require_png:
        Reject non-PNG inputs (default True; the webapp tool spec forces PNG).
    max_side:
        Reject images wider/taller than this (default 256).
    max_colors:
        Maximum palette size (default ``MAX_COLORS`` = 63).  ``None``
        disables the limit for callers that want the full 256-color level.
        Level-A single-char encoding covers up to 86 colors (``SINGLE_LEVEL_MAX``);
        above that the image block falls back to two-char hex per pixel.
    quantize:
        When the unique color count exceeds ``max_colors``, quantize down to
        the budget with median cut instead of raising.  Transparency is
        preserved and never quantized away.
    """
    img = _open(source)
    if require_png and (img.format or "").upper() != "PNG":
        raise CharArtError(
            f"image must be in PNG format (got {img.format or 'unknown'})"
        )
    img = img.convert("RGBA")
    w, h = img.size
    if w > max_side or h > max_side:
        raise CharArtError(
            f"image size {w}x{h} exceeds the {max_side}x{max_side} limit (use pixel art "
            f"no larger than {max_side}x{max_side})"
        )

    arr = np.asarray(img, dtype=np.int32).reshape(h, w, 4)
    alpha = arr[:, :, 3]
    opaque = alpha > 0

    # -- step 1: extract colors ----------------------------------------
    colors: List[Tuple[int, int, int, int]] = []
    counts: List[int] = []
    lookup: Dict[Tuple[int, int, int, int], int] = {}
    transparent_count = 0
    for j in range(h):
        for i in range(w):
            if not opaque[j, i]:
                transparent_count += 1
                continue
            rgba = tuple(int(v) for v in arr[j, i])
            if rgba not in lookup:
                lookup[rgba] = len(colors)
                colors.append(rgba)
                counts.append(0)
            counts[lookup[rgba]] += 1

    # most frequent first (ties keep first-occurrence order, stable sort)
    # -> the most common colors get the leading symbols '0','1',...
    idx = sorted(range(len(colors)), key=lambda k: -counts[k])
    colors = [colors[k] for k in idx]
    counts = [counts[k] for k in idx]

    # transparent background goes LAST (it is usually the largest area and
    # must not hog the leading symbols '0','1',...)
    if transparent_count:
        colors.append((0, 0, 0, 0))
        counts.append(transparent_count)

    # remember original opaque colors (pre-quantize) for nearest remapping
    orig_opaque: List[Tuple[int, int, int, int]] = list(colors)

    # -- optional step: quantize to the budget ---------------------------
    if max_colors is not None and len(colors) > max_colors:
        if not quantize:
            raise CharArtError(
                f"image has {len(colors)} colors, more than the limit of {max_colors}; "
                "reduce the number of colors or allow automatic color reduction (quantize)"
            )
        colors, counts = _quantize(colors, counts, max_colors)

    # -- step 2+3: register ids (symbol index) & encode -------------------
    if not colors:
        raise CharArtError("image has no pixels to convert")
    level = "hex" if len(colors) > SINGLE_LEVEL_MAX else "single"

    # after quantization, final colors are weighted averages, so map each
    # original color to its nearest final palette entry (identity when the
    # palette was untouched)
    trans_rgba = (0, 0, 0, 0)
    final_set = {c: i for i, c in enumerate(colors)}
    if trans_rgba in final_set:
        trans_id = final_set[trans_rgba]
    else:
        trans_id = -1
        final_set[trans_rgba] = -1
    nearest: Dict[Tuple[int, int, int, int], int] = {}
    for c in orig_opaque:
        if c in final_set:
            nearest[c] = final_set[c]
        else:
            nearest[c] = min(
                range(len(colors)),
                key=lambda m, cc=c: _dist(cc, colors[m]),
            )

    matrix = [
        [
            (nearest[tuple(int(v) for v in arr[j, i])] if opaque[j, i] else trans_id)
            for i in range(w)
        ]
        for j in range(h)
    ]
    return CharArt(
        width=w,
        height=h,
        colors=colors,
        counts=counts,
        matrix=matrix,
        level=level,
    )


def _open(source) -> Image.Image:
    if isinstance(source, (bytes, bytearray)):
        try:
            img = Image.open(io.BytesIO(bytes(source)))
            img.load()  # trigger decode so format detection is reliable
        except Exception as e:  # noqa: BLE001
            raise CharArtError(f"cannot decode image: {e}") from None
        return img
    if isinstance(source, (str, Path)):
        try:
            img = Image.open(source)
            img.load()
        except Exception as e:  # noqa: BLE001
            raise CharArtError(f"cannot open image {source}: {e}") from None
        return img
    return source


def _dist(a: Sequence[int], b: Sequence[int]) -> float:
    """Squared euclidean distance between two rgba colors."""
    return sum((x - y) ** 2 for x, y in zip(a, b))


def _quantize(
    colors: List[Tuple[int, int, int, int]],
    counts: List[int],
    limit: int,
) -> Tuple[List[Tuple[int, int, int, int]], List[int]]:
    """Median-cut quantize opaque colors down to ``limit`` (transparent last).

    Transparency is excluded from the buckets and appended back afterwards.
    """
    from pixelbench.core.render import _merge_colors

    trans_rgba = (0, 0, 0, 0)
    has_trans = bool(colors) and colors[-1] == trans_rgba
    opaque_colors = colors[:-1] if has_trans else colors
    opaque_counts = counts[:-1] if has_trans else counts
    # transparency is never quantized away: give it its own slot in the budget
    opaque_limit = max(1, limit - (1 if has_trans else 0))
    merged, merged_counts = _merge_colors(opaque_colors, opaque_counts, opaque_limit)
    out_colors: List[Tuple[int, int, int, int]] = [
        tuple(int(v) for v in c) for c in merged
    ]
    out_counts: List[int] = [int(v) for v in merged_counts]
    if has_trans:
        out_colors.append(trans_rgba)
        out_counts.append(int(counts[-1]))
    return out_colors, out_counts
