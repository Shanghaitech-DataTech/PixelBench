"""The persistent pixel-art canvas: palette + integer-id matrix + tools.

This class is the single object the model interacts with inside the
REPL sandbox.  Every mutating tool records an entry in the edit log and
pushes an undo snapshot, so episodes can be replayed and audited.
"""
from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import numpy as np

from pixelbench.core import shapes
from pixelbench.core.color import Color, Palette, hex_of, parse_hex
from pixelbench.core.font5x7 import draw_text as _draw_text
from pixelbench.core.font5x7 import text_width as _text_width

ColorRef = Union[int, str, Tuple[int, int, int, int]]

MAX_UNDO = 200
MAX_CHECKPOINTS = 200  # cap for undo_step()/undo_round() state snapshots


class _CellSymbol:
    """A named sentinel used as a region-matrix cell (or color ref).

    Sentinels are objects, so they can never collide with palette names,
    ids or hex strings — a user could register a color called ``"erase"``
    without breaking ``ERASE``.
    """

    __slots__ = ("_name",)

    def __init__(self, name: str) -> None:
        self._name = name

    def __repr__(self) -> str:  # noqa: D105
        return self._name

    def __str__(self) -> str:  # noqa: D105
        return self._name


KEEP = _CellSymbol("KEEP")
"""Region-matrix cell: leave the pixel unchanged."""

ERASE = _CellSymbol("ERASE")
"""Region-matrix cell / color ref: set the pixel to transparent."""

# Canonical model-facing wording for region-matrix cells (stamp /
# paint_region / redraw).  Embedded verbatim in the tool docs and agent
# prompts so every surface says exactly the same thing.  The one rule:
# a color paints, 'transparent'/None blank, KEEP leaves unchanged.
CELL_CONVENTION = (
    "each cell is a color name/id that paints that pixel; 'transparent' "
    "(the blank color, or None) makes the pixel blank; KEEP (bare constant, "
    "no quotes) leaves it unchanged"
)


class CanvasError(ValueError):
    pass


class PixelCanvas:
    """A W x H integer-id matrix with a :class:`Palette`."""

    def __init__(
        self,
        width: int,
        height: int,
        palette: Optional[Palette] = None,
        transparent_id: int = 0,
        initial: Optional[np.ndarray] = None,
        max_colors: Optional[int] = None,
    ) -> None:
        if width <= 0 or height <= 0:
            raise CanvasError(f"canvas size must be positive, got {width}x{height}")
        self.width = int(width)
        self.height = int(height)
        self.palette = palette if palette is not None else Palette(max_colors=max_colors)
        self.transparent_id = int(transparent_id)
        if self.transparent_id in self.palette.ids():
            existing = self.palette[self.transparent_id]
            if existing.rgba[3] != 0:
                raise CanvasError(
                    f"transparent_id {self.transparent_id} maps to non-transparent color "
                    f"{existing.name} ({existing.to_hex()})"
                )
        else:
            self.palette._add(
                Color(id=self.transparent_id, name="transparent", rgba=(0, 0, 0, 0))
            )
        self.matrix = np.full((self.height, self.width), self.transparent_id, dtype=np.int32)
        if initial is not None:
            arr = np.asarray(initial, dtype=np.int32)
            if arr.shape != (self.height, self.width):
                raise CanvasError(
                    f"initial matrix shape {arr.shape} does not match {self.height}x{self.width}"
                )
            self.matrix[:] = arr
        self._version = 0
        self._edit_log: List[dict] = []
        self._history: List[np.ndarray] = []  # pre-mutation matrices, for undo
        self._snapshots: Dict[str, np.ndarray] = {}
        # undo_step(): one full-state snapshot per state-changing tool call
        # (matrix + palette + log lengths), so we can roll back exactly one
        # function call.  undo_round(): one snapshot at the start of every
        # executed code block, so we can roll back a whole round of calls.
        self._call_marks: List[dict] = []
        self._round_marks: List[dict] = []
        self._mark_seq = 0
        # undo_step(): one snapshot per mutating tool call, so we can roll
        # back exactly one function call (matrix + palette + version).
        self._call_marks: List[dict] = []
        # undo_round(): a snapshot at the start of every executed code
        # block, so we can roll back a whole turn of operations.
        self._round_marks: List[dict] = []

    # ------------------------------------------------------------------
    # mutation plumbing
    # ------------------------------------------------------------------
    def _mutate(self, op: str, args: dict, changed: int) -> dict:
        """Record a mutation; returns a compact feedback dict for the REPL."""
        self._version += 1
        entry = {"op": op, "args": args, "changed": int(changed), "version": self._version}
        self._edit_log.append(entry)
        return {
            "op": op,
            "changed": int(changed),
            "version": self._version,
            "bbox": self.content_bbox(),
        }

    def _push_history(self) -> None:
        self._history.append(self.matrix.copy())
        if len(self._history) > MAX_UNDO:
            self._history.pop(0)

    # ------------------------------------------------------------------
    # call / round checkpoints (undo_step / undo_round)
    # ------------------------------------------------------------------
    def _snapshot(self) -> dict:
        """Full-state snapshot: matrix + palette + log lengths + version.

        Restoring a snapshot reverts *everything* about the drawing state,
        including palette-only calls (register_color / replace_color) that
        never touch the undo history.
        """
        self._mark_seq += 1
        return {
            "seq": self._mark_seq,
            "matrix": self.matrix.copy(),
            "palette": self.palette.copy(),
            "version": self._version,
            "edit_len": len(self._edit_log),
            "hist_len": len(self._history),
        }

    def mark_call(self) -> None:
        """Record a checkpoint before the next state-changing tool call."""
        self._call_marks.append(self._snapshot())
        if len(self._call_marks) > MAX_CHECKPOINTS:
            self._call_marks.pop(0)

    def mark_round(self) -> None:
        """Record a checkpoint at the start of a round (one run_code block)."""
        self._round_marks.append(self._snapshot())
        if len(self._round_marks) > MAX_CHECKPOINTS:
            self._round_marks.pop(0)

    def _restore_snapshot(self, snap: dict) -> None:
        self.matrix[:] = snap["matrix"]
        self.palette = snap["palette"].copy()
        del self._edit_log[snap["edit_len"]:]
        del self._history[snap["hist_len"]:]

    def undo_step(self) -> dict:
        """Undo the last single function call.

        Rolls the canvas back to the state just before the most recent
        state-changing tool call (matrix, palette, edit log and undo
        history).  Nothing to undo when no call checkpoint exists.
        """
        if not self._call_marks:
            return {"op": "undo_step", "restored": 0, "version": self._version}
        snap = self._call_marks.pop()
        self._restore_snapshot(snap)
        # any round boundary recorded after this call is now stale
        self._round_marks = [m for m in self._round_marks if m["seq"] <= snap["seq"]]
        self._version = snap["version"] + 1
        self._edit_log.append(
            {"op": "undo_step", "args": {}, "changed": 0, "version": self._version}
        )
        return {"op": "undo_step", "restored": 1, "version": self._version}

    def undo_round(self) -> dict:
        """Undo all operations of the previous round.

        A round is one executed code block (one ``run_code`` call from the
        harness).  Restores the canvas to the state recorded at the start
        of the previous round, removing every tool call made in it.
        Repeated calls walk back one round at a time.
        """
        if len(self._round_marks) < 2:
            return {"op": "undo_round", "restored": 0, "version": self._version}
        # last mark = start of the *current* (in-progress) round; the one
        # before it is the start of the previous round we want to revert.
        snap = self._round_marks[-2]
        self._round_marks.pop()
        self._restore_snapshot(snap)
        # drop call checkpoints recorded during the reverted round(s)
        self._call_marks = [m for m in self._call_marks if m["seq"] <= snap["seq"]]
        self._version = snap["version"] + 1
        self._edit_log.append(
            {"op": "undo_round", "args": {}, "changed": 0, "version": self._version}
        )
        return {"op": "undo_round", "restored": 1, "version": self._version}

    # ------------------------------------------------------------------
    # color API
    # ------------------------------------------------------------------
    def register_color(self, name: str, color: Union[str, Tuple[int, int, int, int], Tuple[int, int, int]]) -> int:
        rgba = parse_hex(color) if isinstance(color, str) else tuple(int(c) for c in color)
        if len(rgba) == 3:
            rgba = (rgba[0], rgba[1], rgba[2], 255)
        return self.palette.register(name, rgba)

    def add_palette_color(self, name: str, hex_: str) -> int:
        return self.register_color(name, hex_)

    def list_palette(self) -> str:
        return self.palette.summary()

    def replace_color(self, old: ColorRef, new: Union[str, Tuple[int, int, int, int]]) -> str:
        cid = self.palette._resolve_id(old)
        old_c = self.palette[cid]
        rgba = parse_hex(new) if isinstance(new, str) else tuple(int(c) for c in new)
        self.palette.replace(cid, rgba)
        self._version += 1
        self._edit_log.append({"op": "replace_color", "args": {"old": old_c.to_hex(), "new": hex_of(rgba)}, "changed": 0, "version": self._version})
        return f"color {old_c.name} (id {cid}) changed to {hex_of(rgba)}"

    def mix_colors(self, name: str, c1: ColorRef, c2: ColorRef, t: float = 0.5) -> int:
        """Register a new color as the linear RGB mix of two registered colors.

        ``t=0.0`` -> exactly ``c1``, ``t=1.0`` -> exactly ``c2`` (alpha is
        interpolated too).  Returns the new color id; the palette change is
        undoable like any other tool call.
        """
        t = float(t)
        if not 0.0 <= t <= 1.0:
            raise CanvasError(f"mix ratio t must be in [0, 1], got {t!r}")
        a = self.palette.color(c1).rgba
        b = self.palette.color(c2).rgba
        rgba = tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(4))
        cid = self.palette.register(name, rgba)
        self._version += 1
        self._edit_log.append(
            {"op": "mix_colors", "args": {"name": name, "t": t}, "changed": 0, "version": self._version}
        )
        return cid

    def shade_color(self, name: str, c: ColorRef, amount: float = 0.0) -> int:
        """Register a lighter or darker shade of a registered color.

        ``amount`` in ``[-1, 1]``: ``0`` keeps the color, ``>0`` lightens
        toward white, ``<0`` darkens toward black (alpha is preserved).
        Returns the new color id.
        """
        amount = float(amount)
        if not -1.0 <= amount <= 1.0:
            raise CanvasError(f"shade amount must be in [-1, 1], got {amount!r}")
        r, g, b, a = self.palette.color(c).rgba
        if amount >= 0:
            target = (255, 255, 255)
        else:
            target = (0, 0, 0)
        f = abs(amount)
        rgb = tuple(int(round(v + (tv - v) * f)) for v, tv in zip((r, g, b), target))
        rgba = (rgb[0], rgb[1], rgb[2], a)
        cid = self.palette.register(name, rgba)
        self._version += 1
        self._edit_log.append(
            {"op": "shade_color", "args": {"name": name, "amount": amount}, "changed": 0, "version": self._version}
        )
        return cid

    def pick_color(self, x: int, y: int) -> str:
        self._check_xy(x, y)
        c = self.palette[int(self.matrix[y, x])]
        return f"{c.name} (id {c.id}, {c.to_hex()})"

    def _resolve_color(self, ref: ColorRef) -> int:
        """Resolve a color reference to a palette id.

        ``ERASE``, ``None`` and the string ``'transparent'`` all resolve to
        the transparent id (the canonical blank spellings); anything else
        goes through palette lookup.
        """
        if ref is ERASE or ref is None or (isinstance(ref, str) and ref == "transparent"):
            return self.transparent_id
        try:
            return self.palette._resolve_id(ref)
        except ValueError as e:
            # the classic trap: quoting the KEEP/ERASE constants as color names.
            # Point blank-pixel users at the canonical spellings instead.
            if str(e).startswith("unknown color name"):
                raise ValueError(
                    f"{e} - for blank pixels use 'transparent' (or None); "
                    "KEEP/ERASE are bare constants (no quotes), not color names"
                ) from None
            raise

    def _resolve_cell(self, cell) -> Optional[int]:
        """Map one region-matrix cell to a palette id, or ``None`` to skip.

        Region-matrix convention (shared by :meth:`stamp`,
        :meth:`paint_region` and :meth:`redraw`):

        - ``KEEP``  -> skip: leave the pixel unchanged (returns ``None``)
        - ``ERASE`` / ``None`` / ``'transparent'`` -> transparent pixel
        - anything else -> resolve as a color ref (name/id/hex/rgba)
        """
        if cell is KEEP:
            return None
        return self._resolve_color(cell)

    # ------------------------------------------------------------------
    # pixel / drawing tools
    # ------------------------------------------------------------------
    def set_pixel(self, x: int, y: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._check_xy(x, y)
        self._push_history()
        old = int(self.matrix[y, x])
        changed = 0 if old == cid else 1
        if changed:
            self.matrix[y, x] = cid
        return self._mutate("set_pixel", {"x": x, "y": y, "color": self.palette[cid].name}, changed)

    def draw_line(self, x0: int, y0: int, x1: int, y1: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_line(self.matrix, x0, y0, x1, y1, cid)
        return self._mutate("draw_line", {"x0": x0, "y0": y0, "x1": x1, "y1": y1}, n)

    def paint_rect(self, x: int, y: int, w: int, h: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.fill_rect(self.matrix, x, y, w, h, cid)
        return self._mutate("paint_rect", {"x": x, "y": y, "w": w, "h": h}, n)

    def stroke_rect(self, x: int, y: int, w: int, h: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.stroke_rect(self.matrix, x, y, w, h, cid)
        return self._mutate("stroke_rect", {"x": x, "y": y, "w": w, "h": h}, n)

    def paint_circle(self, cx: int, cy: int, r: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_circle(self.matrix, cx, cy, r, cid, filled=True)
        return self._mutate("paint_circle", {"cx": cx, "cy": cy, "r": r}, n)

    def stroke_circle(self, cx: int, cy: int, r: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_circle(self.matrix, cx, cy, r, cid, filled=False)
        return self._mutate("stroke_circle", {"cx": cx, "cy": cy, "r": r}, n)

    def paint_ellipse(self, cx: int, cy: int, rx: int, ry: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_ellipse(self.matrix, cx, cy, rx, ry, cid, filled=True)
        return self._mutate("paint_ellipse", {"cx": cx, "cy": cy, "rx": rx, "ry": ry}, n)

    def stroke_ellipse(self, cx: int, cy: int, rx: int, ry: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_ellipse(self.matrix, cx, cy, rx, ry, cid, filled=False)
        return self._mutate("stroke_ellipse", {"cx": cx, "cy": cy, "rx": rx, "ry": ry}, n)

    def draw_polyline(self, points: Sequence[Tuple[int, int]], color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_polyline(self.matrix, points, cid)
        return self._mutate("draw_polyline", {"points": list(points)}, n)

    def draw_polygon(self, points: Sequence[Tuple[int, int]], color: ColorRef, filled: bool = False) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_polygon(self.matrix, points, cid, filled=filled)
        return self._mutate("draw_polygon", {"points": list(points), "filled": filled}, n)

    def draw_path(self, d: str, color: ColorRef, filled: bool = False, origin: Tuple[int, int] = (0, 0)) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.draw_path(self.matrix, d, cid, filled=filled, origin=origin)
        return self._mutate("draw_path", {"d": d, "filled": filled, "origin": list(origin)}, n)

    def draw_text(self, x: int, y: int, text: str, color: ColorRef, spacing: int = 1) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = _draw_text(self.matrix, x, y, text, cid, spacing=spacing)
        return self._mutate("draw_text", {"x": x, "y": y, "text": text}, n)

    def text_width(self, text: str, spacing: int = 1) -> int:
        return _text_width(text, spacing)

    def flood_fill(self, x: int, y: int, color: ColorRef) -> dict:
        cid = self._resolve_color(color)
        self._push_history()
        n = shapes.flood_fill(self.matrix, x, y, cid)
        return self._mutate("flood_fill", {"x": x, "y": y, "color": self.palette[cid].name}, n)

    # ------------------------------------------------------------------
    # region tools
    # ------------------------------------------------------------------
    def stamp(self, pattern: Sequence[Sequence], x: int, y: int) -> dict:
        """Stamp a 2D pattern at (x, y).

        Each cell follows the shared region-matrix convention (see
        :meth:`_resolve_cell`): a color name/id paints the pixel,
        ``'transparent'`` / ``None`` (or the ``ERASE`` constant) makes it
        blank, ``KEEP`` leaves it untouched.
        """
        self._push_history()
        rows = list(pattern)
        n = 0
        for dy, row in enumerate(rows):
            for dx, cell in enumerate(row):
                px, py = x + dx, y + dy
                if not (0 <= px < self.width and 0 <= py < self.height):
                    continue
                cid = self._resolve_cell(cell)
                if cid is None:
                    continue
                if int(self.matrix[py, px]) != cid:
                    self.matrix[py, px] = cid
                    n += 1
        return self._mutate("stamp", {"x": x, "y": y, "shape": (len(rows), len(rows[0]) if rows else 0)}, n)

    def paint_region(self, x: int, y: int, region: Sequence[Sequence]) -> dict:
        """Write a matrix of color refs into a region anchored at (x, y).

        Each cell follows the shared region-matrix convention (see
        :meth:`_resolve_cell`): a color name/id paints the pixel,
        ``'transparent'`` / ``None`` (or the ``ERASE`` constant) makes it
        blank, ``KEEP`` leaves it untouched.
        """
        self._push_history()
        rows = list(region)
        n = 0
        for dy, row in enumerate(rows):
            for dx, cell in enumerate(row):
                px, py = x + dx, y + dy
                if not (0 <= px < self.width and 0 <= py < self.height):
                    continue
                cid = self._resolve_cell(cell)
                if cid is None:
                    continue
                if int(self.matrix[py, px]) != cid:
                    self.matrix[py, px] = cid
                    n += 1
        return self._mutate("paint_region", {"x": x, "y": y}, n)

    def redraw(self, rows: Sequence[Sequence]) -> dict:
        """Full-canvas redraw: ``rows`` must cover the whole W x H matrix.

        The cell convention is identical to :meth:`paint_region` (see
        :meth:`_resolve_cell`); cells are written at ``(0, 0)``.
        Used by the "redraw" agent surface, where the ONLY way to change
        the canvas is replacing the whole picture.
        """
        rows = list(rows)
        got_w = len(rows[0]) if rows else 0
        if len(rows) != self.height or got_w != self.width:
            raise CanvasError(
                f"redraw needs a full {self.width}x{self.height} matrix, "
                f"got {len(rows)}x{got_w}; every cell of the canvas must be given"
            )
        return self.paint_region(0, 0, rows)

    def clear_region(self, x: int, y: int, w: int, h: int, color: Optional[ColorRef] = None) -> dict:
        cid = self._resolve_color(color)  # None -> transparent
        self._push_history()
        n = shapes.fill_rect(self.matrix, x, y, w, h, cid)
        return self._mutate("clear_region", {"x": x, "y": y, "w": w, "h": h}, n)

    def copy_region(self, src: Tuple[int, int, int, int], dst_origin: Tuple[int, int]) -> dict:
        """Copy src box (x, y, w, h) to dst_origin (dx, dy)."""
        sx, sy, sw, sh = src
        dx, dy = dst_origin
        self._push_history()
        sub = self.matrix[sy : sy + sh, sx : sx + sw].copy()
        n = 0
        for j in range(sub.shape[0]):
            for i in range(sub.shape[1]):
                px, py = dx + i, dy + j
                if 0 <= px < self.width and 0 <= py < self.height:
                    if int(self.matrix[py, px]) != int(sub[j, i]):
                        self.matrix[py, px] = sub[j, i]
                        n += 1
        return self._mutate("copy_region", {"src": list(src), "dst": list(dst_origin)}, n)

    def mirror_region(
        self, src: Tuple[int, int, int, int], axis: str, dst_origin: Optional[Tuple[int, int]] = None
    ) -> dict:
        """Mirror src box horizontally ('h') or vertically ('v').

        If ``dst_origin`` is given the mirrored copy is written there,
        otherwise the source box is mirrored in place.
        """
        sx, sy, sw, sh = src
        if axis not in ("h", "v"):
            raise CanvasError(f"axis must be 'h' or 'v', got {axis!r}")
        self._push_history()
        sub = self.matrix[sy : sy + sh, sx : sx + sw].copy()
        if axis == "h":
            sub = sub[:, ::-1]
        else:
            sub = sub[::-1, :]
        if dst_origin is None:
            dst_origin = (sx, sy)
        dx, dy = dst_origin
        n = 0
        for j in range(sub.shape[0]):
            for i in range(sub.shape[1]):
                px, py = dx + i, dy + j
                if 0 <= px < self.width and 0 <= py < self.height:
                    if int(self.matrix[py, px]) != int(sub[j, i]):
                        self.matrix[py, px] = sub[j, i]
                        n += 1
        return self._mutate("mirror_region", {"src": list(src), "axis": axis}, n)

    def shift_region(self, x: int, y: int, w: int, h: int, dx: int, dy: int, fill: Optional[ColorRef] = None) -> dict:
        """Shift a region's content by (dx, dy); vacated cells become ``fill``."""
        fill_cid = self._resolve_color(fill)  # None -> transparent
        self._push_history()
        sub = self.matrix[y : y + h, x : x + w].copy()
        self.matrix[y : y + h, x : x + w] = fill_cid
        n = 0
        for j in range(sub.shape[0]):
            for i in range(sub.shape[1]):
                px, py = x + i + dx, y + j + dy
                if 0 <= px < self.width and 0 <= py < self.height:
                    self.matrix[py, px] = sub[j, i]
                    n += 1
        return self._mutate("shift_region", {"x": x, "y": y, "w": w, "h": h, "dx": dx, "dy": dy}, n)

    def dither_region(self, x: int, y: int, w: int, h: int, colors: Sequence[ColorRef], pattern: str = "checker") -> dict:
        """Fill a region with a deterministic dither pattern of two colors.

        ``pattern``: 'checker' (alternating by parity) or 'bayer4' (a
        4x4 ordered Bayer matrix).
        """
        if len(colors) != 2:
            raise CanvasError("dither_region takes exactly 2 colors")
        a = self._resolve_color(colors[0])
        b = self._resolve_color(colors[1])
        if pattern not in ("checker", "bayer4"):
            raise CanvasError(f"pattern must be 'checker' or 'bayer4', got {pattern!r}")
        bayer4 = np.array(
            [
                [0, 8, 2, 10],
                [12, 4, 14, 6],
                [3, 11, 1, 9],
                [15, 7, 13, 5],
            ]
        )
        self._push_history()
        n = 0
        for j in range(h):
            for i in range(w):
                px, py = x + i, y + j
                if not (0 <= px < self.width and 0 <= py < self.height):
                    continue
                if pattern == "checker":
                    cid = a if (i + j) % 2 == 0 else b
                else:
                    cid = a if bayer4[j % 4, i % 4] < 8 else b
                if int(self.matrix[py, px]) != cid:
                    self.matrix[py, px] = cid
                    n += 1
        return self._mutate("dither_region", {"x": x, "y": y, "w": w, "h": h, "pattern": pattern}, n)

    def outline_region(self, x: int, y: int, w: int, h: int, outline_color: ColorRef) -> dict:
        """Outline the non-transparent content inside a box.

        Every content pixel that touches a transparent (or outside-box)
        pixel is repainted with ``outline_color``.
        """
        oid = self._resolve_color(outline_color)
        self._push_history()
        x0, y0 = max(0, x), max(0, y)
        x1, y1 = min(self.width, x + w), min(self.height, y + h)
        content = self.matrix[y0:y1, x0:x1] != self.transparent_id
        # boundary = content & (at least one 4-neighbor is NOT content,
        # i.e. transparent or outside the clipped box)
        padded = np.pad(content, 1, constant_values=False)
        all_neigh = (
            padded[:-2, 1:-1]
            & padded[2:, 1:-1]
            & padded[1:-1, :-2]
            & padded[1:-1, 2:]
        )
        boundary = content & ~all_neigh
        n = 0
        for j in range(boundary.shape[0]):
            for i in range(boundary.shape[1]):
                if boundary[j, i]:
                    self.matrix[y0 + j, x0 + i] = oid
                    n += 1
        return self._mutate("outline_region", {"x": x, "y": y, "w": w, "h": h}, n)

    # ------------------------------------------------------------------
    # undo / snapshots / history
    # ------------------------------------------------------------------
    def undo(self, n: int = 1) -> dict:
        if n < 1:
            raise CanvasError("undo count must be >= 1")
        restored = 0
        for _ in range(n):
            if not self._history:
                break
            self.matrix[:] = self._history.pop()
            self._edit_log.append({"op": "undo", "args": {}, "changed": 0, "version": self._version + 1})
            restored += 1
        if restored:
            self._version += 1
        return {"op": "undo", "restored": restored, "version": self._version}

    def snapshot(self, name: str) -> dict:
        self._snapshots[name] = self.matrix.copy()
        return {"op": "snapshot", "name": name, "stored": True}

    def restore(self, name: str) -> dict:
        if name not in self._snapshots:
            raise CanvasError(f"no snapshot named {name!r}; known: {sorted(self._snapshots)}")
        self._push_history()
        self.matrix[:] = self._snapshots[name]
        return self._mutate("restore", {"name": name}, 0)

    def history(self, n: int = 20) -> str:
        ops = self._edit_log[-n:]
        lines = [f"history (last {len(ops)} of {len(self._edit_log)} ops):"]
        for e in ops:
            args = {k: v for k, v in e["args"].items() if k not in ("d",)}
            lines.append(f"  v{e['version']:>4} {e['op']:<14} changed={e['changed']:<5} {args}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # observation
    # ------------------------------------------------------------------
    def _check_xy(self, x: int, y: int) -> None:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise CanvasError(f"({x},{y}) out of bounds for {self.width}x{self.height} canvas")

    def summary(self) -> str:
        st = self.stats()
        return (
            f"canvas {self.width}x{self.height} | version {self._version} | "
            f"{st['used_colors']} used colors | coverage {st['coverage_pct']:.1f}% | "
            f"steps {len(self._edit_log)} | content bbox {st['bbox']}"
        )

    def stats(self) -> dict:
        m = self.matrix
        non_transparent = m != self.transparent_id
        if getattr(self, "_alpha_visibility", False) or hasattr(self, "_drawing_state"):
            non_transparent = np.isin(m, [c.id for c in self.palette if c.rgba[3] > 0])
        total = m.size
        used = int(non_transparent.sum())
        ids, counts = np.unique(m[non_transparent], return_counts=True)
        color_counts = {}
        for cid, cnt in zip(ids.tolist(), counts.tolist()):
            color_counts[self.palette[int(cid)].name] = int(cnt)
        bbox = None
        if used:
            ys, xs = np.nonzero(non_transparent)
            bbox = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
        return {
            "width": self.width,
            "height": self.height,
            "version": self._version,
            "used_pixels": used,
            "coverage_pct": 100.0 * used / total if total else 0.0,
            "used_colors": len(color_counts),
            "color_counts": color_counts,
            "bbox": bbox,
            "steps": len(self._edit_log),
        }

    def observe_region(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        mode: str = "matrix",
        color_as: str = "name",
        max_cells: Optional[int] = None,
        block: int = 1,
    ) -> str:
        """Human-readable view of a region.

        mode: 'matrix' (grid of color labels), 'counts' (color usage
        histogram).  For pixel-exact views use observe_region(mode='image')/
        render() which return images.

        ``max_cells``: optional safety cap on the number of cells a
        matrix view may print (None = no limit).  Text-only models
        routinely view whole 128x128 canvases as matrix text, so
        the view is unbounded by default.

        ``block``: only for ``color_as='char'``.  ``1`` (default) prints one
        character per pixel, i.e. the full-resolution shape view; ``N>1``
        prints one character per NxN block (majority colour) for a coarser,
        shorter look at very large canvases.
        """
        if mode not in ("matrix", "counts"):
            raise CanvasError(f"mode must be matrix|counts, got {mode!r}")
        if color_as not in ("name", "id", "hex", "char"):
            raise CanvasError(f"color_as must be name|id|hex|char, got {color_as!r}")
        x0, y0 = max(0, x), max(0, y)
        x1, y1 = min(self.width, x + w), min(self.height, y + h)
        if x0 >= x1 or y0 >= y1:
            return f"(empty region {x},{y},{w},{h} on {self.width}x{self.height})"
        cells = (x1 - x0) * (y1 - y0)
        if max_cells is not None and mode == "matrix" and cells > max_cells:
            return (
                f"region too large for a text view ({x1 - x0}x{y1 - y0} = {cells} cells, "
                f"limit {max_cells}); use mode='counts' or observe_region(mode='image')/render()"
            )
        if mode == "counts":
            sub = self.matrix[y0:y1, x0:x1]
            ids, counts = np.unique(sub, return_counts=True)
            parts = [f"region ({x0},{y0})-({x1 - 1},{y1 - 1}) color counts:"]
            for cid, cnt in zip(ids.tolist(), counts.tolist()):
                c = self.palette[int(cid)]
                label = {"name": c.name, "id": str(c.id), "hex": c.to_hex()}[color_as]
                parts.append(f"  {label:<16} {int(cnt):>6}")
            return "\n".join(parts)

        header = f"region ({x0},{y0})-({x1 - 1},{y1 - 1})"
        if color_as == "char":
            # "Shape view" for text-only models: one char per pixel (or per block),
            # plus a char -> id -> hex legend, so ONE call is a complete, self-contained
            # picture of the whole canvas + palette.
            #
            # 1:1 by default (one char per pixel) and NOT length-capped: a 256x256
            # canvas is ~66k chars, which the model can read in one call now that
            # kernel.MAX_TEXT is None.  Pass ``block=N`` for a coarser view.
            ids_sorted = self.palette.ids()
            slot = {cid: k for k, cid in enumerate(ids_sorted)}
            alphabet = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

            def _ch(cid: int) -> str:
                if cid == self.transparent_id:
                    return "."
                return alphabet[slot[cid] % len(alphabet)]

            sub = self.matrix[y0:y1, x0:x1]

            # legend first: it must survive even if the grid part is long
            tally = {}
            for cid in np.unique(sub).tolist():
                chx = _ch(int(cid))
                hit = tally.setdefault(chx, [int(cid), 0])
                hit[1] += int((sub == cid).sum())
            ordered = sorted(tally.items(), key=lambda kv: -kv[1][1])
            shown, cap = ordered[:48], 48
            legend = " ".join(
                f"{chx}={cid}({self.palette[cid].to_hex()})" for chx, (cid, _) in shown
            )
            more = f" +{len(ordered) - len(shown)} more colours" if len(ordered) > cap else ""
            legend_line = (f"colour key ({len(ordered)} colours, most-used first): "
                           f"{legend}{more}")

            def _render(block: int):
                rows_out = []
                if block <= 1:
                    grid_ids = sub
                else:
                    bh = -(-sub.shape[0] // block)
                    bw = -(-sub.shape[1] // block)
                    padded = np.full((bh * block, bw * block), -1, dtype=np.int64)
                    padded[: sub.shape[0], : sub.shape[1]] = sub
                    blocks = (padded.reshape(bh, block, bw, block)
                              .transpose(0, 2, 1, 3).reshape(bh * bw, block * block))
                    grid_ids = np.empty((bh, bw), dtype=np.int64)
                    for bi, row in enumerate(blocks):
                        valid = row[row >= 0]
                        vals, counts = np.unique(valid, return_counts=True)
                        grid_ids[bi // bw, bi % bw] = vals[int(np.argmax(counts))]
                cols = [" "] * grid_ids.shape[1]
                for k in range(grid_ids.shape[1]):
                    xx = x0 + k * block
                    if xx % 10 == 0:
                        for t, chx in enumerate(str(xx)):
                            if k + t < len(cols):
                                cols[k + t] = chx
                rows_out.append("    " + "".join(cols))
                for r in range(grid_ids.shape[0]):
                    rows_out.append(f"{y0 + r * block:>3} "
                                    + "".join(_ch(int(cid)) for cid in grid_ids[r]))
                return rows_out

            block = max(1, int(block))
            grid_rows = _render(block)
            note = ("1 char per pixel" if block == 1
                    else f"1 char per {block}x{block} block (majority colour)")
            lines = [header + f" char view: {note}, '.' = transparent",
                     f"canvas is {self.width}x{self.height}; this view is complete "
                     f"({len(grid_rows)} rows, one per {'pixel row' if block == 1 else 'block row'})",
                     legend_line,
                     "use color_as='id' on a small region for exact pixel ids"]
            lines += grid_rows
            return "\n".join(lines)
        rows = []
        width = {"name": 8, "id": 3, "hex": 7}[color_as]
        sep = " "
        rows.append("    " + sep.join(f"{i:>{width}}" for i in range(x0, x1)))
        for j in range(y0, y1):
            cells_txt = []
            for i in range(x0, x1):
                c = self.palette[int(self.matrix[j, i])]
                if color_as == "name":
                    txt = c.name[:width].ljust(width)
                elif color_as == "id":
                    txt = f"{c.id:>{width}}"
                else:
                    txt = c.to_hex()[:width].rjust(width)
                cells_txt.append(txt)
            rows.append(f"{j:>3} " + sep.join(cells_txt))
        return header + "\n" + "\n".join(rows)

    # ------------------------------------------------------------------
    # rendering hooks (see render.py for the actual image code)
    # ------------------------------------------------------------------
    def render(self, scale: int = 8, grid: bool = False, checker: bool = False):
        from pixelbench.core.render import render_pil

        return render_pil(self, scale=scale, grid=grid, checker=checker)

    def render_png_bytes(self, scale: int = 8, grid: bool = False, checker: bool = False) -> bytes:
        from pixelbench.core.render import render_png_bytes

        return render_png_bytes(self, scale=scale, grid=grid, checker=checker)

    # ------------------------------------------------------------------
    # misc helpers
    # ------------------------------------------------------------------
    def content_bbox(self) -> Optional[List[int]]:
        return self.stats()["bbox"]

    def matrix_art(self, color_as: str = "id", block: int = 1) -> str:
        """Whole-canvas matrix view with row/column coordinates.

        Every cell is labelled by color ``name`` / ``id`` / ``hex`` so a
        text-only model can locate and repaint exact pixels.  Default
        ``color_as='id'``: imported input images often have no meaningful
        color names, so the stable palette id is the safe common label
        (pair with ``list_palette()`` for id->hex).
        """
        return self.observe_region(
            0, 0, self.width, self.height, mode="matrix", color_as=color_as, block=block
        )

    def to_dict(self) -> dict:
        result = {
            "width": self.width,
            "height": self.height,
            "palette": self.palette.to_dict(),
            "transparent_id": self.transparent_id,
            "canvas": self.matrix.tolist(),
        }
        if hasattr(self, "_drawing_state"):
            result["drawing_state"] = copy.deepcopy(self._drawing_state)
        return result

    @classmethod
    def from_dict(cls, d: dict) -> "PixelCanvas":
        pal = Palette.from_dict(d["palette"])
        canvas = cls(
            width=int(d["width"]),
            height=int(d["height"]),
            palette=pal,
            transparent_id=int(d.get("transparent_id", 0)),
        )
        rows = d["canvas"]
        if len(rows) != canvas.height:
            raise CanvasError(f"canvas rows {len(rows)} != height {canvas.height}")
        arr = np.zeros((canvas.height, canvas.width), dtype=np.int32)
        for j, row in enumerate(rows):
            if len(row) != canvas.width:
                raise CanvasError(f"row {j} length {len(row)} != width {canvas.width}")
            for i, v in enumerate(row):
                v = int(v)
                if v not in pal.ids() and v != canvas.transparent_id:
                    raise CanvasError(f"cell ({i},{j}) has unknown palette id {v}")
                arr[j, i] = v
        canvas.matrix = arr
        if "drawing_state" in d:
            canvas._drawing_state = copy.deepcopy(d["drawing_state"])
        return canvas

    def copy(self) -> "PixelCanvas":
        c = PixelCanvas(self.width, self.height, palette=self.palette.copy(), transparent_id=self.transparent_id)
        c.matrix = self.matrix.copy()
        if hasattr(self, "_drawing_state"):
            c._drawing_state = copy.deepcopy(self._drawing_state)
        return c

    def __repr__(self) -> str:  # noqa: D105
        return f"PixelCanvas({self.width}x{self.height}, v{self._version}, {len(self.palette)} colors)"
