"""The tool surface the model calls inside the REPL sandbox.

``SessionTools`` wraps a :class:`PixelCanvas` and exposes the drawing
software API described in the benchmark plan: color registration,
region observation (matrix / counts / canonical char-art / image),
painting tools, pixel-art helpers, undo/snapshots and (for replication
tasks) a reference viewer.  Every method returns a compact text feedback
string; image-producing methods additionally emit a PNG into the kernel
output so the harness can hand it to a vision-capable model.

Design rules:
- coordinates: x right, y down, origin top-left (0,0)
- named colors; hex/rgb values must be registered first
- no anti-aliasing anywhere; everything is integer-grid
- no official diff/score tool, even in replication tasks
"""
from __future__ import annotations

import functools
import json
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from pixelbench.core.canvas import CELL_CONVENTION
from pixelbench.repl.kernel import FINISH_SENTINEL


def _display_image(img) -> None:
    from IPython.display import display

    display(img)


# Tool calls that change canvas state (matrix and/or palette).  Each one
# records a checkpoint on the canvas so ``undo_step()`` can roll
# back exactly one function call.  Pure-observation calls (render /
# observe_region / summary / ...), episode control (finish) and the two
# undo tools themselves are deliberately excluded.
STATE_CHANGING_TOOLS = frozenset(
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
        "register_color",
        "replace_color",
        "mix_colors",
        "shade_color",
        "redraw",
        "undo",
        "snapshot",
        "restore",
    }
)


class SessionTools:
    """Tools bound to one episode canvas.  Also exposed as top-level
    functions in the kernel namespace (see prelude.py)."""

    def __init__(self, canvas, task: Optional[dict] = None, allow_reference: bool = False,
                 look_budget: Optional[int] = None) -> None:
        self.canvas = canvas
        self.task = task or {}
        self.allow_reference = bool(allow_reference)
        # Observation budget: None = unlimited; 1 = a single "look" at the canvas (restore uses
        # it to cap the cost and to make the model see everything at once, then paint from
        # memory). A look = a render, matrix, region view or single-pixel color pick.
        self.look_budget = look_budget
        self._looks_used = 0
        self.finished = False
        self._reference = None
        self._reference_image = None

    def _look_gate(self, what: str) -> Optional[str]:
        """Consume one look. Once the budget is used up, every "look" returns a refusal note
        (not an error), so the model can keep painting."""
        if self.look_budget is None:
            return None
        if self._looks_used >= int(self.look_budget):
            return (
                f"[observation disabled] You already used your single look at the canvas "
                f"({what} refused). You cannot view the canvas again - neither the original nor "
                f"your own drawing. Paint from what you saw on that first look, then call finish(). "
                f"stats()/summary()/list_palette() still work if you need numbers."
            )
        self._looks_used += 1
        left = int(self.look_budget) - self._looks_used
        return None

    def __getattribute__(self, name: str):
        """Intercept state-changing tool calls to record an undo_step()
        checkpoint (canvas state before the call).  Observation-only tools
        and the undo tools themselves pass through untouched."""
        attr = object.__getattribute__(self, name)
        if name in STATE_CHANGING_TOOLS and callable(attr):
            return functools.partial(
                object.__getattribute__(self, "_tracked_call"), name, attr
            )
        return attr

    def _tracked_call(self, op: str, fn, *args, **kwargs):
        try:
            self.canvas.mark_call()
        except Exception:  # pragma: no cover - never break the tool call
            pass
        return fn(*args, **kwargs)

    # ------------------------------------------------------------------
    # task / canvas info
    # ------------------------------------------------------------------
    def summary(self) -> str:
        return self.canvas.summary()

    def stats(self) -> str:
        st = self.canvas.stats()
        parts = [
            f"canvas {st['width']}x{st['height']}",
            f"version {st['version']}  steps {st['steps']}",
            f"used colors {st['used_colors']}  coverage {st['coverage_pct']:.1f}%  used pixels {st['used_pixels']}",
            f"content bbox {st['bbox']}",
        ]
        if st["color_counts"]:
            top = sorted(st["color_counts"].items(), key=lambda kv: -kv[1])[:10]
            parts.append("top colors: " + ", ".join(f"{n}={c}" for n, c in top))
        return "\n".join(parts)

    def observe_canvas(self, mode: str = "summary", color_as: str = "id",
                       block: int = 1) -> str:
        if mode == "matrix":
            gate = self._look_gate("observe_canvas(mode='matrix')")
            if gate:
                return gate
            return self.canvas.matrix_art(color_as=color_as, block=block)
        if mode == "stats":
            return self.stats()
        if mode == "summary":
            return self.summary()
        raise ValueError(f"observe_canvas mode must be 'summary'|'matrix'|'stats', got {mode!r}")

    # ------------------------------------------------------------------
    # palette
    # ------------------------------------------------------------------
    def register_color(self, name: str, color: Union[str, Tuple[int, int, int, int]]) -> int:
        cid = self.canvas.register_color(name, color)
        c = self.canvas.palette[cid]
        print(f"registered {name} -> id {cid} ({c.to_hex()})")
        return cid

    def list_palette(self) -> str:
        return self.canvas.list_palette()

    def replace_color(self, old, new: Union[str, Tuple[int, int, int, int]]) -> str:
        return self.canvas.replace_color(old, new)

    def mix_colors(self, name: str, c1, c2, t: float = 0.5) -> int:
        """Register a new color as the linear mix of two registered colors."""
        cid = self.canvas.mix_colors(name, c1, c2, t)
        c = self.canvas.palette[cid]
        print(f"registered {name} -> id {cid} ({c.to_hex()})")
        return cid

    def shade_color(self, name: str, c, amount: float = 0.0) -> int:
        """Register a lighter (amount>0) or darker (amount<0) shade of a color."""
        cid = self.canvas.shade_color(name, c, amount)
        c = self.canvas.palette[cid]
        print(f"registered {name} -> id {cid} ({c.to_hex()})")
        return cid

    def pick_color(self, x: int, y: int) -> str:
        gate = self._look_gate(f"pick_color({x},{y})")
        if gate:
            return gate
        return self.canvas.pick_color(x, y)

    # ------------------------------------------------------------------
    # observation
    # ------------------------------------------------------------------
    def observe_region(self, x: int, y: int, w: int, h: int, mode: str = "matrix",
                       color_as: str = "name", block: int = 1) -> str:
        gate = self._look_gate(f"observe_region({x},{y},{w},{h})")
        if gate:
            return gate
        if mode == "image":
            # crop at 1x first (raw pixel coords), then upscale the crop
            from PIL import Image

            img = self.canvas.render(scale=1)
            x0, y0 = max(0, x), max(0, y)
            x1, y1 = min(self.canvas.width, x + w), min(self.canvas.height, y + h)
            if x0 >= x1 or y0 >= y1:
                return f"(empty region {x},{y},{w},{h})"
            crop = img.crop((x0, y0, x1, y1)).resize(((x1 - x0) * 8, (y1 - y0) * 8), Image.NEAREST)
            _display_image(crop)
            return f"rendered region ({x0},{y0})-({x1 - 1},{y1 - 1}) as image"
        return self.canvas.observe_region(x, y, w, h, mode=mode, color_as=color_as, block=block)

    def render(self, scale: int = 8, grid: bool = False) -> str:
        gate = self._look_gate("render()")
        if gate:
            return gate
        img = self.canvas.render(scale=scale, grid=grid)
        _display_image(img)
        return (
            f"rendered {self.canvas.width}x{self.canvas.height} canvas at scale {scale} "
            f"(image above, {self.canvas.width * scale}x{self.canvas.height * scale}px)"
        )

    def reference(self, region: Optional[Tuple[int, int, int, int]] = None) -> str:
        """Show the reference image (replication tasks only).  No diff/score."""
        if not self.allow_reference or self._reference_image is None:
            return "reference is not available in this task"
        if region is not None:
            x, y, w, h = region
            from PIL import Image

            img = self._reference_image
            crop = img.crop((x, y, x + w, y + h)).resize((w * 8, h * 8), Image.NEAREST)
            _display_image(crop)
            return f"rendered reference region ({x},{y})-({x + w - 1},{y + h - 1})"
        _display_image(self._reference_image)
        return f"reference image shown ({self._reference.width}x{self._reference.height} @8x)"

    # ------------------------------------------------------------------
    # drawing
    # ------------------------------------------------------------------
    def _fmt(self, res: dict) -> str:
        bbox = res.get("bbox")
        extra = f", bbox={bbox}" if bbox else ""
        # some ops (undo, restore) report `restored` instead of `changed`
        changed = res.get("changed", res.get("restored", 0))
        return f"{res['op']}: changed {changed}px (v{res['version']}){extra}"

    def set_pixel(self, x: int, y: int, color) -> str:
        return self._fmt(self.canvas.set_pixel(x, y, color))

    def draw_line(self, x0: int, y0: int, x1: int, y1: int, color) -> str:
        return self._fmt(self.canvas.draw_line(x0, y0, x1, y1, color))

    def paint_rect(self, x: int, y: int, w: int, h: int, color) -> str:
        return self._fmt(self.canvas.paint_rect(x, y, w, h, color))

    def stroke_rect(self, x: int, y: int, w: int, h: int, color) -> str:
        return self._fmt(self.canvas.stroke_rect(x, y, w, h, color))

    def paint_circle(self, cx: int, cy: int, r: int, color) -> str:
        return self._fmt(self.canvas.paint_circle(cx, cy, r, color))

    def stroke_circle(self, cx: int, cy: int, r: int, color) -> str:
        return self._fmt(self.canvas.stroke_circle(cx, cy, r, color))

    def paint_ellipse(self, cx: int, cy: int, rx: int, ry: int, color) -> str:
        return self._fmt(self.canvas.paint_ellipse(cx, cy, rx, ry, color))

    def stroke_ellipse(self, cx: int, cy: int, rx: int, ry: int, color) -> str:
        return self._fmt(self.canvas.stroke_ellipse(cx, cy, rx, ry, color))

    def draw_polyline(self, points, color) -> str:
        return self._fmt(self.canvas.draw_polyline([(int(p[0]), int(p[1])) for p in points], color))

    def draw_polygon(self, points, color, filled: bool = False) -> str:
        return self._fmt(self.canvas.draw_polygon([(int(p[0]), int(p[1])) for p in points], color, filled=filled))

    def draw_path(self, d: str, color, filled: bool = False, origin: Tuple[int, int] = (0, 0)) -> str:
        return self._fmt(self.canvas.draw_path(d, color, filled=filled, origin=origin))

    def draw_text(self, x: int, y: int, text: str, color, spacing: int = 1) -> str:
        return self._fmt(self.canvas.draw_text(x, y, text, color, spacing=spacing))

    def flood_fill(self, x: int, y: int, color) -> str:
        return self._fmt(self.canvas.flood_fill(x, y, color))

    # ------------------------------------------------------------------
    # region / pixel-art helpers
    # ------------------------------------------------------------------
    def stamp(self, pattern: Sequence[Sequence], x: int, y: int) -> str:
        return self._fmt(self.canvas.stamp(pattern, x, y))

    def paint_region(self, x: int, y: int, rows: Sequence[Sequence]) -> str:
        return self._fmt(self.canvas.paint_region(x, y, rows))

    def clear_region(self, x: int, y: int, w: int, h: int, color=None) -> str:
        return self._fmt(self.canvas.clear_region(x, y, w, h, color))

    def redraw(self, rows: Sequence[Sequence]) -> str:
        """Full-canvas redraw: replace the ENTIRE canvas with ``rows``.

        ``rows`` must be a W x H matrix of cells following the shared cell
        convention (see ``CELL_CONVENTION``): a color name/id paints,
        'transparent' / None makes the pixel blank, KEEP leaves it
        unchanged.  This is the only drawing tool of the "redraw" agent
        surface.
        """
        return self._fmt(self.canvas.redraw(rows))

    def copy_region(self, src, dst_origin) -> str:
        return self._fmt(self.canvas.copy_region(tuple(src), tuple(dst_origin)))

    def mirror_region(self, src, axis: str, dst_origin=None) -> str:
        return self._fmt(self.canvas.mirror_region(tuple(src), axis, tuple(dst_origin) if dst_origin else None))

    def shift_region(self, x: int, y: int, w: int, h: int, dx: int, dy: int, fill=None) -> str:
        return self._fmt(self.canvas.shift_region(x, y, w, h, dx, dy, fill))

    def dither_region(self, x: int, y: int, w: int, h: int, colors, pattern: str = "checker") -> str:
        return self._fmt(self.canvas.dither_region(x, y, w, h, colors, pattern=pattern))

    def outline_region(self, x: int, y: int, w: int, h: int, color) -> str:
        return self._fmt(self.canvas.outline_region(x, y, w, h, color))

    # ------------------------------------------------------------------
    # history / undo
    # ------------------------------------------------------------------
    def undo(self, n: int = 1) -> str:
        return self._fmt(self.canvas.undo(n))

    def undo_step(self) -> str:
        """Undo the last single function call.

        Rolls the canvas back to the state just before the most recent
        state-changing tool call (including palette changes).  Repeated
        calls walk back one call at a time.
        """
        return self._fmt(self.canvas.undo_step())

    def undo_round(self) -> str:
        """Undo all operations of the previous round.

        A round is one executed code block (one ``run_code`` call from the
        harness).  Restores the canvas to the state at the start of the
        previous round, removing every tool call made in it.  Repeated
        calls walk back one round at a time.
        """
        return self._fmt(self.canvas.undo_round())

    def snapshot(self, name: str) -> str:
        return json.dumps(self.canvas.snapshot(name))

    def restore(self, name: str) -> str:
        return self._fmt(self.canvas.restore(name))

    def history(self, n: int = 20) -> str:
        return self.canvas.history(n)

    # ------------------------------------------------------------------
    # episode control
    # ------------------------------------------------------------------
    def finish(self) -> str:
        self.finished = True
        print(FINISH_SENTINEL)
        return "drawing marked complete"


# Method names exposed as top-level functions in the kernel prelude.
# Only callable class methods are bound, so plain data attributes
# (canvas, task, finished, ...) never shadow episode variables such as
# `reference` or `mask`.  `reference` is deliberately excluded: it is
# both a tool method and (in replication tasks) the reference canvas
# variable; the method stays available as tools.reference() /
# show_reference().
TOOL_NAMES: List[str] = sorted(
    n
    for n, v in vars(SessionTools).items()
    if callable(v) and not n.startswith("_") and n != "reference"
)

# Tool surfaces: which tools the prelude binds as top-level names.
# "full"   -> the complete REPL surface (all tools).
# "redraw" -> only full-canvas redraw + palette + full-canvas observation:
#             the model cannot touch individual pixels or regions, only
#             replace the whole picture (draw -> render -> redraw -> ...).
REDRAW_SURFACE: frozenset = frozenset(
    {
        "register_color",
        "list_palette",
        "replace_color",
        "mix_colors",
        "shade_color",
        "pick_color",
        "redraw",
        "render",
        "observe_canvas",
        "stats",
        "summary",
        "finish",
    }
)
SURFACES: Dict[str, frozenset] = {
    "full": frozenset(TOOL_NAMES),
    "redraw": REDRAW_SURFACE,
}

# Canonical tool documentation, embedded verbatim in the `run_code`
# function description so the model sees the full API every step without
# needing an in-kernel help() call.  Keep this in sync with the methods
# above; signatures here are the ones the model should write.
#
# The description is generated per (surface, vision) pair: multimodal
# models are told about the 'image' observation modes and that rendered
# PNGs are fed into their vision module; text-only models are never shown
# the image options (they cannot see them).
def tool_docs(surface: str, vision: bool, look_budget: Optional[int] = None) -> str:
    """Return the ``run_code`` description for a tool surface + vision flag.

    ``look_budget=1``: each episode allows a single "look" at the canvas (render / matrix /
    region view / single-pixel pick); afterwards those tools all return a refusal note, and
    the docs must tell the model so.
    """
    doc = _redraw_doc(vision) if surface == "redraw" else _full_doc(vision)
    if look_budget == 1:
        look = ("render()" if vision else "observe_canvas(mode='matrix', color_as='char')")
        doc += (
            "\n\nLOOK ONCE: this episode gives you a SINGLE look at the canvas. Use it to view "
            f"the WHOLE image on your first step - {look} - because afterwards every observation "
            "tool (render / observe_canvas / observe_region / pick_color) is disabled: you will "
            "not be able to see the canvas again, neither the original nor your own drawing. "
            "stats(), summary() and list_palette() keep working. Paint from what you saw."
        )
    return doc


def _full_doc(vision: bool) -> str:
    region_modes = "'matrix'|'counts'" + ("|'image'" if vision else "")
    canvas_modes = "'summary'|'matrix'|'stats'"
    lines = [
        "Persistent pixel-art canvas session; canvas state survives between calls. "
        "Coordinates: x right, y down, origin top-left (0,0). "
        "Register a color before painting: register_color(name, '#rrggbb') returns its id; "
        "after that, colors can be referenced by name, id, hex or rgba. "
        "All tools return a short text like 'paint_rect: changed 40px (v3)'.",
    ]
    if vision:
        lines.append(
            "You are a multimodal model: every PNG you render via render() / "
            "observe_region(mode='image') is captured and fed into your vision "
            "module after the step. You may also read the canvas as text "
            "(observe_canvas(mode='matrix') with list_palette()) whenever you "
            "need exact pixel coordinates or color ids — choose per situation."
        )
    lines.append("Tools (top-level functions):")
    lines.append("- summary() / stats()             canvas size, used colors, coverage, steps, top colors")
    lines.append(
        "- register_color(name, '#rrggbb')   returns a color id; "
        "mix_colors(name, c1, c2, t=0.5) registers c1/c2's mix as a new color (t=0 -> c1, t=1 -> c2); "
        "shade_color(name, c, amount) registers a lighter (amount>0) or darker (amount<0) shade of c; "
        "list_palette() / pick_color(x, y) / replace_color(old, new)"
    )
    lines.append(
        f"- observe_region(x, y, w, h, mode={region_modes}, color_as='name')   local view; "
        "matrix=grid of color labels, counts=color histogram"
        + (", image=PNG fed to your vision" if vision else "")
    )
    lines.append(
        f"- observe_canvas(mode={canvas_modes})   whole-canvas view; summary=compact stats, "
        "matrix=full color grid with coordinates "
        "(color_as='name'|'id'|'hex'|'char', default 'id' — pair with list_palette() to map ids "
        "to hex; color_as='char' prints one character per pixel plus a colour key, i.e. the WHOLE "
        "canvas as a picture in a single call, and the output is not truncated — pass block=N for "
        "one character per NxN block if you want a coarser look), "
        "stats=full stats"
    )
    if vision:
        lines.append(
            "- render(scale=8, grid=False)   whole canvas as a PNG fed to your vision"
        )
    lines.append("- set_pixel(x, y, color)")
    lines.append("- draw_line(x0, y0, x1, y1, color)")
    lines.append("- paint_rect / stroke_rect(x, y, w, h, color)")
    lines.append("- paint_circle / stroke_circle(cx, cy, r, color)")
    lines.append("- paint_ellipse / stroke_ellipse(cx, cy, rx, ry, color)")
    lines.append("- draw_polyline(points, color) / draw_polygon(points, color, filled=False)")
    lines.append(
        "- draw_path('M0 0 L10 0 C...', color, filled=False, origin=(0,0))   "
        "SVG path subset M/L/H/V/C/S/Q/T/A/Z"
    )
    lines.append("- draw_text(x, y, 'TEXT', color, spacing=1)   built-in 5x7 pixel font")
    lines.append("- flood_fill(x, y, color)")
    lines.append(
        "- stamp(rows, x, y) / paint_region(x, y, rows) / redraw(rows)   "
        "write a 2D pattern or replace the whole canvas with the full WxH matrix; "
        + CELL_CONVENTION
    )
    lines.append("- clear_region(x, y, w, h, color=None)   fill with transparent or a color")
    lines.append(
        "- copy_region((sx,sy,sw,sh), (dx,dy)) / mirror_region((x,y,w,h), 'h'|'v') / "
        "shift_region(x, y, w, h, dx, dy)"
    )
    lines.append("- dither_region(x, y, w, h, [c1, c2], pattern='checker'|'bayer4')")
    lines.append("- outline_region(x, y, w, h, color)")
    lines.append(
        "- undo(n=1) / undo_step() (undo the last function call, incl. palette) / "
        "undo_round() (undo all calls of the previous round)"
    )
    lines.append("- snapshot(name) / restore(name) / history(n=20)")
    if vision:
        lines.append("- reference(region=None)   show the reference image (replication tasks only; no diff/score tool)")
    else:
        lines.append(
            "- reference (a PixelCanvas variable, replication tasks)   read reference.matrix / "
            "reference.observe_region(...) for text views; no diff/score tool"
        )
    lines.append("- finish()   mark the drawing complete and stop the episode")
    if vision:
        lines.append(
            "Rendered images are shown back to you after the step. "
            "Call finish() when the drawing is complete."
        )
    else:
        lines.append("Call finish() when the drawing is complete.")
    return "\n".join(lines)


def _redraw_doc(vision: bool) -> str:
    canvas_modes = "'summary'|'matrix'|'stats'"
    tools = [
        "register_color(name, '#rrggbb')",
        "mix_colors(name, c1, c2, t=0.5) (register c1/c2's mix as a new color)",
        "shade_color(name, c, amount) (register a lighter/darker shade of c)",
        "list_palette()",
        "replace_color(old, new)",
        "pick_color(x, y)",
        "redraw(rows)",
    ]
    if vision:
        tools.append("render(scale=8, grid=False)")
    tools.append(f"observe_canvas(mode={canvas_modes})")
    tools.append("stats()")
    tools.append("summary()")
    tools.append("finish()")
    lines = [
        "Persistent pixel-art canvas session; canvas state survives between calls. "
        "Coordinates: x right, y down, origin top-left (0,0). "
        "The ONLY way to change the canvas is redraw(rows) with the complete WxH matrix; "
        + CELL_CONVENTION + ".",
    ]
    if vision:
        lines.append(
            "You are a multimodal model: the PNG you render via render() is captured and fed "
            "into your vision module after the step. Look at the picture (render() once at the "
            "start) instead of reading the canvas as numbers; fall back to "
            "observe_canvas(mode='matrix') only when you need exact pixel ids."
        )
    else:
        lines.append(
            "observe_canvas(mode='matrix') prints the whole canvas as a color grid with "
            "coordinates (default color_as='id'; pair with list_palette() to map ids to hex). "
            "To see the WHOLE image in ONE call use "
            "observe_canvas(mode='matrix', color_as='char') — one character per pixel plus a "
            "colour key, printed in full (the output is not truncated, a 256x256 canvas included). "
            "Do that once at the start, then get to work: do NOT page through the canvas region by "
            "region, re-inspect every turn, or write your own parser for the numeric matrix."
        )
    lines.append("Tools (top-level functions): " + ", ".join(tools) + ".")
    if vision:
        lines.append(
            "Rendered images are shown back to you after the step. "
            "Call finish() when the drawing is complete."
        )
    else:
        lines.append("Call finish() when the drawing is complete.")
    return "\n".join(lines)
