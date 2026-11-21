"""Kernel-side observer for the agent's painting process.

The observer runs *inside* the ipykernel sandbox (it wraps the
:class:`SessionTools` instance the model calls), and records two
granularities of the drawing process straight to the episode's
``observations/`` directory:

- **call granularity** — every drawing function call (``set_pixel``,
  ``paint_rect``, ``draw_line``, ``undo``, ...) as one JSON event line
  (op, args, changed px).  Per-call *before | after* diff images are OFF
  by default (the turn frames are the primary observation window); set
  ``PIXELBENCH_OBSERVE_DIFFS=1`` to re-enable them.
- **turn granularity** — every executed code block (one ``run_code`` /
  ``session.execute`` from the harness).  For each block we save a
  snapshot frame of the canvas state right after execution and one JSON
  event line with the call-index range the block produced.  The turn
  hook rides on IPython's ``post_execute`` event, so it fires exactly
  once per kernel execution regardless of which agent drives it.

Output layout (all under ``<episode>/observations/``)::

    calls.jsonl     one line per observed tool call
    turns.jsonl     one line per executed code block (+ initial frame)
    frames/turn_0000.png ...   canvas state after each block
    diffs/call_0000.png  ...   before|after diff per mutating call
                               (only with PIXELBENCH_OBSERVE_DIFFS=1)

The observer never feeds anything back into the model's context: it is
purely a logging/observation channel.  All writes are append-only JSONL
+ PNG files, so a kernel crash mid-episode does not lose earlier
observations.
"""
from __future__ import annotations

import functools
import io
import json
import time
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np
from PIL import Image, ImageDraw

from pixelbench.core.render import render_pil

# Tool methods that can change the rendered image (candidate call events).
# Observation-only methods (render / observe_region / summary / ...) are
# deliberately not observed as "calls": they do not change the picture.
MUTATING_TOOLS = frozenset(
    {
        "set_pixel",
        "draw_line",
        "paint_rect",
        "stroke_rect",
        "paint_circle",
        "stroke_circle",
        "paint_ellipse",
        "stroke_ellipse",
        "draw_polyline",
        "draw_polygon",
        "draw_path",
        "draw_text",
        "flood_fill",
        "stamp",
        "paint_region",
        "clear_region",
        "copy_region",
        "mirror_region",
        "shift_region",
        "dither_region",
        "outline_region",
        "undo",
        "undo_step",
        "undo_round",
        "snapshot",
        "restore",
        "replace_color",
        "register_color",
        "finish",
    }
)

_HIGHLIGHT = (255, 64, 128, 255)  # magenta-ish outline for changed cells


# ----------------------------------------------------------------------
# diff image rendering (pure, harness-side testable)
# ----------------------------------------------------------------------
def _canvas_like_to_pil(canvas) -> Image.Image:
    """Render a PixelCanvas at 1px-per-cell on a checkerboard so
    transparent pixels are visible."""
    return render_pil(canvas, scale=1, checker=True)


def render_diff_png(
    canvas,
    before: np.ndarray,
    after: np.ndarray,
    changed: np.ndarray,
    op: str,
    scale: int = 8,
) -> bytes:
    """Render a *before | after* diff image for one mutating call.

    ``canvas`` is the current :class:`PixelCanvas` (its palette defines
    the colors for both panels); ``before`` / ``after`` are the integer
    matrices around the call; ``changed`` is a bool mask of the cells
    that differ.  Changed cells get a bright 1px outline in both panels.
    The op name and pixel-change count are drawn in a header strip so
    thumbnails can be scanned quickly.
    """
    if scale < 1:
        raise ValueError("scale must be >= 1")
    before_canvas = canvas.copy()
    after_canvas = canvas.copy()
    before_canvas.matrix[:] = before
    after_canvas.matrix[:] = after
    before_img = _canvas_like_to_pil(before_canvas)
    after_img = _canvas_like_to_pil(after_canvas)
    if scale > 1:
        before_img = before_img.resize(
            (before_img.width * scale, before_img.height * scale), Image.NEAREST
        )
        after_img = after_img.resize(
            (after_img.width * scale, after_img.height * scale), Image.NEAREST
        )
    _outline_changed(before_img, changed, scale)
    _outline_changed(after_img, changed, scale)

    gap = 10
    header_h = 30
    w = before_img.width + gap + after_img.width
    h = header_h + max(before_img.height, after_img.height) + 8
    out = Image.new("RGBA", (w, h), (26, 26, 32, 255))
    draw = ImageDraw.Draw(out)
    changed_n = int(changed.sum())
    caption = f"{op}  ->  {changed_n} px changed"
    draw.text((8, 8), caption, fill=(235, 235, 245, 255))
    draw.text((w // 2 - 30, 8), "before", fill=(150, 160, 175, 255))
    draw.text((w - 60, 8), "after", fill=(150, 160, 175, 255))
    out.alpha_composite(before_img, (0, header_h))
    out.alpha_composite(after_img, (before_img.width + gap, header_h))
    buf = io.BytesIO()
    out.convert("RGB").save(buf, format="PNG")
    return buf.getvalue()


def _outline_changed(img: Image.Image, changed: np.ndarray, scale: int) -> None:
    draw = ImageDraw.Draw(img, "RGBA")
    ys, xs = np.nonzero(changed)
    for y, x in zip(ys.tolist(), xs.tolist()):
        x0, y0 = x * scale, y * scale
        draw.rectangle(
            [x0 + 1, y0 + 1, x0 + scale - 1, y0 + scale - 1], outline=_HIGHLIGHT, width=1
        )


def _sanitize_args(args: Dict[str, Any]) -> Dict[str, Any]:
    """Make call args JSON-safe and compact (drop huge payloads)."""
    def _clean(v: Any, depth: int = 0) -> Any:
        if depth > 4:
            return "..."
        if hasattr(v, "item") and hasattr(v, "shape"):  # numpy scalar/array
            v = v.item() if v.ndim == 0 else v.tolist()
        if isinstance(v, (str, int, float, bool)) or v is None:
            return v
        if isinstance(v, (list, tuple)):
            return [_clean(x, depth + 1) for x in v[:64]]
        if isinstance(v, dict):
            return {str(k)[:64]: _clean(x, depth + 1) for k, x in list(v.items())[:32]}
        return str(v)[:200]

    return {str(k): _clean(v) for k, v in args.items()}


# ----------------------------------------------------------------------
# the observer
# ----------------------------------------------------------------------
class CanvasObserver:
    """Records tool calls and per-execution turn boundaries to disk."""

    def __init__(self, out_dir: Path, canvas, scale: int = 8, render_diffs: Optional[bool] = None) -> None:
        self.out_dir = Path(out_dir)
        self.canvas = canvas
        self.scale = scale
        # when False, per-call before|after diff PNGs are skipped (still
        # record calls.jsonl / turns.jsonl / frames).  OFF by default: the
        # turn (agent-step) frames are the primary observation window, and
        # pixel-by-pixel painters would otherwise produce tens of
        # thousands of near-zero-information diff images.  Set the env var
        # PIXELBENCH_OBSERVE_DIFFS=1 to re-enable per-call diffs.
        if render_diffs is None:
            import os

            render_diffs = os.environ.get("PIXELBENCH_OBSERVE_DIFFS", "0") == "1"
        self.render_diffs = bool(render_diffs)
        (self.out_dir / "frames").mkdir(parents=True, exist_ok=True)
        (self.out_dir / "diffs").mkdir(parents=True, exist_ok=True)
        self._calls_fh = (self.out_dir / "calls.jsonl").open("a", encoding="utf-8")
        self._turns_fh = (self.out_dir / "turns.jsonl").open("a", encoding="utf-8")
        self.call_index = 0
        self.turn_index = 0
        self._turn_start_call = 0
        self.active = True

    # -- lifecycle ------------------------------------------------------
    def set_active(self, active: bool) -> None:
        self.active = bool(active)

    def close(self) -> None:
        try:
            self._calls_fh.close()
        except Exception:
            pass
        try:
            self._turns_fh.close()
        except Exception:
            pass

    # -- call granularity ----------------------------------------------
    def observe_call(self, op: str, args: Dict[str, Any], before: np.ndarray) -> None:
        """Record one tool call.  ``before`` is the matrix snapshot taken
        right before the call; the current ``canvas.matrix`` is the after
        state.  Safe to call even when inactive (no-op fast path)."""
        if not self.active:
            return
        after = self.canvas.matrix
        changed = (before != after)
        changed_n = int(changed.sum())
        version = int(getattr(self.canvas, "_version", 0))
        diff_path = None
        if self.render_diffs and changed_n > 0:
            try:
                png = render_diff_png(
                    self.canvas, before, after, changed, op, scale=self.scale
                )
                diff_path = f"diffs/call_{self.call_index:06d}.png"
                (self.out_dir / diff_path).write_bytes(png)
            except Exception:  # pragma: no cover - never break the agent loop
                diff_path = None
        event = {
            "kind": "call",
            "call": self.call_index,
            "turn": self.turn_index,  # block currently executing (recorded as this turn)
            "op": op,
            "args": _sanitize_args(args),
            "changed": changed_n,
            "version": version,
            "diff": diff_path,
            "t": time.time(),
        }
        self._calls_fh.write(json.dumps(event, ensure_ascii=False) + "\n")
        self._calls_fh.flush()
        self.call_index += 1

    # -- turn granularity ----------------------------------------------
    def on_execute_done(self) -> None:
        """IPython ``post_execute`` hook: one code block just finished.
        Records the block as a turn (with its frame, code and call range).

        Turn 0 is the prelude itself (initial canvas state); its code is
        intentionally not recorded.
        """
        if not self.active:
            return
        frame_path = f"frames/turn_{self.turn_index:04d}.png"
        try:
            self.canvas.render(scale=self.scale).convert("RGB").save(
                self.out_dir / frame_path, format="PNG"
            )
        except Exception:  # pragma: no cover
            frame_path = None
        code = None
        if self.turn_index > 0:
            try:
                from IPython import get_ipython

                ip = get_ipython()
                # `_ih[-1]` is the input that just ran; `_i` lags one cell
                # behind at post_execute time.
                ih = (ip.user_ns or {}).get("_ih") or []
                code = ih[-1] if ih else None
                if isinstance(code, str):
                    code = code if len(code) <= 2000 else code[:2000] + "\n...[truncated]"
                else:
                    code = None
            except Exception:  # pragma: no cover
                code = None
        event = {
            "kind": "turn",
            "turn": self.turn_index,
            "calls_start": self._turn_start_call,
            "calls_end": self.call_index,
            "frame": frame_path,
            "code": code,
            "initial": self.turn_index == 0,
            "version": int(getattr(self.canvas, "_version", 0)),
            "t": time.time(),
        }
        self._turns_fh.write(json.dumps(event, ensure_ascii=False) + "\n")
        self._turns_fh.flush()
        self.turn_index += 1
        self._turn_start_call = self.call_index


# ----------------------------------------------------------------------
# SessionTools proxy that injects the observer
# ----------------------------------------------------------------------
class ObservedTools:
    """Proxy around :class:`SessionTools` that records every mutating
    tool call on a :class:`CanvasObserver`.

    Non-mutating methods are passed through untouched.  The proxy keeps
    all normal attribute access working (``tools.canvas``,
    ``tools.finished``, ...), so it is a drop-in replacement for the
    plain SessionTools instance in the prelude.
    """

    def __init__(self, inner, observer: CanvasObserver) -> None:
        object.__setattr__(self, "_inner", inner)
        object.__setattr__(self, "_observer", observer)

    def __getattr__(self, name: str):
        inner = object.__getattribute__(self, "_inner")
        attr = getattr(inner, name)
        if callable(attr) and name in MUTATING_TOOLS:
            return functools.partial(self._observed, name, attr)
        return attr

    def _observed(self, op: str, fn, *args, **kwargs):
        before = self._inner.canvas.matrix.copy()
        try:
            return fn(*args, **kwargs)
        finally:
            try:
                call_args = {"positional": list(args), "keyword": dict(kwargs)}
                self._observer.observe_call(op, call_args, before)
            except Exception:  # pragma: no cover - never break the agent loop
                pass


# ----------------------------------------------------------------------
# prelude helper
# ----------------------------------------------------------------------
def install_observer(canvas, tools, out_dir: Path, scale: int = 8) -> "CanvasObserver":
    """Wrap ``tools`` with an observer writing to ``out_dir``.

    Returns the observer instance.  The caller (prelude) is responsible
    for registering the IPython ``post_execute`` hook.

    Per-call diff PNGs can be disabled with the env var
    ``PIXELBENCH_OBSERVE_DIFFS=0`` (frames / calls / turns are kept).
    """
    import os

    render_diffs = os.environ.get("PIXELBENCH_OBSERVE_DIFFS", "1") != "0"
    obs = CanvasObserver(out_dir, canvas, scale=scale, render_diffs=render_diffs)
    return obs


def register_post_execute_hook(observer: CanvasObserver) -> None:
    """Register the per-execution turn hook on the running IPython shell."""
    try:
        from IPython import get_ipython

        ip = get_ipython()
        if ip is not None:
            ip.events.register(
                "post_execute", functools.partial(_safe_execute_done, observer)
            )
    except Exception:  # pragma: no cover
        pass


def _safe_execute_done(observer: CanvasObserver) -> None:
    try:
        observer.on_execute_done()
    except Exception:  # pragma: no cover - never break the agent loop
        pass


class WorkspaceObserver(CanvasObserver):
    """Record each canvas independently; the turn preview shows the whole workspace."""

    def __init__(self, out_dir, drawing):
        super().__init__(out_dir, None)
        self.drawing = drawing

    def observe_canvas(self, op, canvas, before, after, changed):
        if not self.active:
            return
        event = {'kind': 'call', 'call': self.call_index, 'turn': self.turn_index,
                 'op': op, 'args': {}, 'canvas_id': self.drawing.canvas_id(canvas),
                 'canvas_name': canvas.name, 'changed': changed,
                 'version': self.drawing.version, 'diff': None, 't': time.time()}
        if self.render_diffs and changed:
            try:
                # RGBA rendering compares palette changes correctly too.
                from PIL import Image
                left, right = before.render(scale=self.scale), after.render(scale=self.scale)
                sheet = Image.new('RGBA', (left.width + right.width, max(left.height, right.height)))
                sheet.paste(left, (0, 0)); sheet.paste(right, (left.width, 0))
                event['diff'] = f'diffs/call_{self.call_index:06d}.png'
                sheet.save(self.out_dir / event['diff'])
            except Exception:
                event['diff'] = None
        self._calls_fh.write(json.dumps(event, ensure_ascii=False) + '\n')
        self._calls_fh.flush()
        self.call_index += 1

    def observe_workspace(self, op):
        event = {'kind': 'call', 'call': self.call_index, 'turn': self.turn_index,
                 'op': op, 'args': {}, 'changed': 0, 'version': self.drawing.version,
                 'canvas_id': None, 'diff': None, 't': time.time()}
        self._calls_fh.write(json.dumps(event) + '\n'); self._calls_fh.flush()
        self.call_index += 1

    def on_execute_done(self):
        if not self.active:
            return
        from PIL import Image
        entries, previews = [], []
        for c in self.drawing.known:
            cid = self.drawing.canvas_id(c)
            path = f'frames/turn_{self.turn_index:04d}_{cid}.png'
            im = self.drawing.to_pixel_canvas(c).render(scale=self.scale)
            im.save(self.out_dir / path)
            entries.append({'canvas_id': cid, 'name': c.name, 'frame': path})
            previews.append(im)
        frame = None
        if previews:
            # Contact sheet is only a preview, never a submission candidate.
            cols = min(4, len(previews)); cw = max(im.width for im in previews); ch = max(im.height for im in previews)
            sheet = Image.new('RGBA', (cw * cols, ch * ((len(previews)+cols-1)//cols)))
            for i, im in enumerate(previews):
                sheet.paste(im, ((i % cols)*cw, (i//cols)*ch))
            frame = f'frames/turn_{self.turn_index:04d}.png'
            sheet.save(self.out_dir / frame)
        from IPython import get_ipython
        shell = get_ipython()
        history = shell.user_ns.get('_ih', []) if shell else []
        event = {'kind': 'turn', 'turn': self.turn_index, 'calls_start': self._turn_start_call,
                 'calls_end': self.call_index, 'frame': frame, 'canvases': entries,
                 'code': getattr(self, 'source_code', None) or (history[-1][:2000] if history and self.turn_index else None),
                 'initial': self.turn_index == 0, 'version': self.drawing.version, 't': time.time()}
        self._turns_fh.write(json.dumps(event, ensure_ascii=False) + '\n'); self._turns_fh.flush()
        self.turn_index += 1
        self._turn_start_call = self.call_index
