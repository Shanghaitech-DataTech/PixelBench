"""Serialization of the canonical PixelArt format.

Canonical form::

    {
      "version": "pixelbench-v0",
      "id": ...,
      "width", "height",
      "palette": [{"id", "name", "rgba": [r,g,b,a]}, ...],
      "transparent_id": 0,
      "canvas": [[id, ...], ...],   # canvas[y][x]
      "metadata": {...}
    }
"""
from __future__ import annotations

import json
from typing import Any, Dict, Optional

from pixelbench.core.canvas import CanvasError, PixelCanvas


def to_pixel_json(canvas: PixelCanvas, id_: Optional[str] = None, metadata: Optional[dict] = None) -> dict:
    d = canvas.to_dict()
    d["version"] = "pixelbench-v0"
    d["id"] = id_ or getattr(canvas, "_id", None)
    d["metadata"] = metadata or getattr(canvas, "_metadata", {})
    return d


def from_pixel_json(d: dict) -> PixelCanvas:
    if "canvas" not in d or "palette" not in d:
        raise CanvasError("pixel json must contain 'palette' and 'canvas'")
    canvas = PixelCanvas.from_dict(d)
    canvas._id = d.get("id")
    canvas._metadata = d.get("metadata", {})
    return canvas


def dumps_pixel_json(canvas: PixelCanvas, id_: Optional[str] = None, metadata: Optional[dict] = None, **kw) -> str:
    return json.dumps(to_pixel_json(canvas, id_=id_, metadata=metadata), **kw)


def loads_pixel_json(s: str) -> PixelCanvas:
    return from_pixel_json(json.loads(s))
