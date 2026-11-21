"""Standard preprocessing for all LLM-judge image inputs.

Pipeline (all canvas sizes):
  1. pad the canvas by ``pad`` CANVAS pixels (transparent), on ``sides``
  2. NEAREST-resize to 512x512
  3. (caller) attach prompt and feed to the judge model

There is no separate "render layer" in the pipeline: the pipeline starts from
the canvas, and the on-disk PNG is just that canvas stored at
``RENDER_SCALE`` (8x) magnification. Padding is therefore specified in canvas
pixels and multiplied by ``RENDER_SCALE`` internally.

Rationale: see docs/LLM_JUDGE_PADDING_FINDING.md. On 16x16 canvases the
default (top-left, 1 canvas px) gave the best judge-human agreement of the
variants tried; four-sided padding performed slightly worse than top-left
only.
"""
from __future__ import annotations

import io

from PIL import Image

DEFAULT_SIZE = 512
# outputs are written with render_png_bytes(scale=8); this is a storage
# magnification, NOT a pipeline stage.
RENDER_SCALE = 8


def judge_image(
    png: bytes,
    pad: int = 1,
    sides: str = "top-left",
    size: int = DEFAULT_SIZE,
    render_scale: int = RENDER_SCALE,
) -> bytes:
    """Pad ``pad`` canvas pixels (``sides``) then NEAREST-resize to ``size``.

    Args:
        png: canvas image bytes, stored at ``render_scale`` magnification.
        pad: padding in CANVAS pixels (0 disables padding).
        sides: ``"top-left"`` (content pushed to bottom-right) or ``"ring"``
            (all four sides, content centred).
        size: output square size.
        render_scale: magnification of the stored PNG relative to the canvas.
    """
    if sides not in ("top-left", "ring"):
        raise ValueError(f"sides must be 'top-left'|'ring', got {sides!r}")
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    w, h = im.size
    if pad > 0:
        p = pad * render_scale
        if sides == "top-left":
            out = Image.new("RGBA", (w + p, h + p), (0, 0, 0, 0))
            out.paste(im, (p, p))
        else:  # ring
            out = Image.new("RGBA", (w + 2 * p, h + 2 * p), (0, 0, 0, 0))
            out.paste(im, (p, p))
        im = out
    if im.size != (size, size):
        im = im.resize((size, size), Image.NEAREST)
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    return buf.getvalue()
