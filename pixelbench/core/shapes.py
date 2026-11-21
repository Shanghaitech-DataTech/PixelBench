"""Deterministic integer rasterization primitives for pixel art.

All functions operate on an ``np.ndarray`` of int32 palette ids and
take the target ``color_id`` explicitly, so they are pure, reproducible
and free of anti-aliasing (pixel art must stay integer-grid).
"""
from __future__ import annotations

import math
import re
from typing import Iterable, List, Sequence, Tuple

import numpy as np

Point = Tuple[int, int]
Matrix = np.ndarray


def in_bounds(matrix: Matrix, x: int, y: int) -> bool:
    return 0 <= y < matrix.shape[0] and 0 <= x < matrix.shape[1]


def _put(matrix: Matrix, x: int, y: int, color_id: int) -> None:
    if in_bounds(matrix, x, y):
        matrix[y, x] = color_id


# ---------------------------------------------------------------------------
# lines
# ---------------------------------------------------------------------------
def bresenham(x0: int, y0: int, x1: int, y1: int) -> List[Point]:
    """Classic Bresenham line, endpoints inclusive."""
    pts: List[Point] = []
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    while True:
        pts.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy
    return pts


def draw_line(matrix: Matrix, x0: int, y0: int, x1: int, y1: int, color_id: int) -> int:
    n = 0
    for x, y in bresenham(x0, y0, x1, y1):
        if in_bounds(matrix, x, y):
            matrix[y, x] = color_id
            n += 1
    return n


def draw_polyline(matrix: Matrix, points: Sequence[Point], color_id: int) -> int:
    n = 0
    for i in range(len(points) - 1):
        n += draw_line(matrix, points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], color_id)
    return n


# ---------------------------------------------------------------------------
# rects
# ---------------------------------------------------------------------------
def _clip_rect(matrix: Matrix, x: int, y: int, w: int, h: int) -> Tuple[int, int, int, int]:
    x0 = max(0, x)
    y0 = max(0, y)
    x1 = min(matrix.shape[1], x + w)
    y1 = min(matrix.shape[0], y + h)
    return x0, y0, max(x0, x1), max(y0, y1)


def fill_rect(matrix: Matrix, x: int, y: int, w: int, h: int, color_id: int) -> int:
    if w <= 0 or h <= 0:
        return 0
    x0, y0, x1, y1 = _clip_rect(matrix, x, y, w, h)
    n = 0
    for yy in range(y0, y1):
        for xx in range(x0, x1):
            matrix[yy, xx] = color_id
            n += 1
    return n


def stroke_rect(matrix: Matrix, x: int, y: int, w: int, h: int, color_id: int) -> int:
    if w <= 0 or h <= 0:
        return 0
    n = 0
    n += draw_line(matrix, x, y, x + w - 1, y, color_id)
    n += draw_line(matrix, x, y + h - 1, x + w - 1, y + h - 1, color_id)
    if h > 1:
        n += draw_line(matrix, x, y, x, y + h - 1, color_id)
        n += draw_line(matrix, x + w - 1, y, x + w - 1, y + h - 1, color_id)
    return n


# ---------------------------------------------------------------------------
# circles / ellipses
# ---------------------------------------------------------------------------
def circle_points(cx: int, cy: int, r: int) -> List[Point]:
    """Midpoint circle, 8-way symmetric ring."""
    if r <= 0:
        return [(cx, cy)]
    pts: List[Point] = []
    x, y, err = r, 0, 1 - r
    while x >= y:
        pts.extend(
            [
                (cx + x, cy + y),
                (cx + y, cy + x),
                (cx - y, cy + x),
                (cx - x, cy + y),
                (cx - x, cy - y),
                (cx - y, cy - x),
                (cx + y, cy - x),
                (cx + x, cy - y),
            ]
        )
        y += 1
        if err < 0:
            err += 2 * y + 1
        else:
            x -= 1
            err += 2 * (y - x) + 1
    return pts


def _ellipse_span(cx: int, cy: int, rx: int, ry: int) -> Iterable[Tuple[int, int, int]]:
    """Yield (y, x0, x1) horizontal spans for a filled ellipse."""
    if rx <= 0 or ry <= 0:
        return
    for dy in range(-ry, ry + 1):
        half = int(round(rx * math.sqrt(max(0.0, 1.0 - (dy * dy) / (ry * ry)))))
        yield cy + dy, cx - half, cx + half


def draw_circle(matrix: Matrix, cx: int, cy: int, r: int, color_id: int, filled: bool = False) -> int:
    if r < 0:
        return 0
    n = 0
    if filled:
        for y, x0, x1 in _ellipse_span(cx, cy, r, r):
            for xx in range(x0, x1 + 1):
                if in_bounds(matrix, xx, y):
                    matrix[y, xx] = color_id
                    n += 1
        return n
    for x, y in circle_points(cx, cy, r):
        if in_bounds(matrix, x, y):
            matrix[y, x] = color_id
            n += 1
    return n


def draw_ellipse(
    matrix: Matrix, cx: int, cy: int, rx: int, ry: int, color_id: int, filled: bool = False
) -> int:
    if rx <= 0 or ry <= 0:
        return 0
    if rx == ry:
        return draw_circle(matrix, cx, cy, rx, color_id, filled=filled)
    n = 0
    if filled:
        for y, x0, x1 in _ellipse_span(cx, cy, rx, ry):
            for xx in range(x0, x1 + 1):
                if in_bounds(matrix, xx, y):
                    matrix[y, xx] = color_id
                    n += 1
        return n
    # stroke: dense deterministic sampling of the ellipse boundary
    steps = max(64, 4 * (rx + ry))
    pts = [
        (
            cx + int(round(rx * math.cos(2 * math.pi * i / steps))),
            cy + int(round(ry * math.sin(2 * math.pi * i / steps))),
        )
        for i in range(steps)
    ]
    return draw_polyline(matrix, pts, color_id)


# ---------------------------------------------------------------------------
# polygons
# ---------------------------------------------------------------------------
def fill_polygon(matrix: Matrix, points: Sequence[Point], color_id: int) -> int:
    """Scanline polygon fill (even-odd)."""
    if len(points) < 3:
        return draw_polyline(matrix, points + [points[0]], color_id) if points else 0
    ys = [p[1] for p in points]
    ymin, ymax = min(ys), max(ys)
    n = 0
    m = len(points)
    for y in range(max(0, ymin), min(matrix.shape[0], ymax + 1)):
        xs: List[int] = []
        for i in range(m):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % m]
            if (y1 <= y < y2) or (y2 <= y < y1):
                xs.append(int(round(x1 + (y - y1) * (x2 - x1) / (y2 - y1))))
        xs.sort()
        for k in range(0, len(xs) - 1, 2):
            for xx in range(xs[k], xs[k + 1] + 1):
                if 0 <= xx < matrix.shape[1]:
                    matrix[y, xx] = color_id
                    n += 1
    return n


def draw_polygon(matrix: Matrix, points: Sequence[Point], color_id: int, filled: bool = False) -> int:
    if not points:
        return 0
    if filled:
        return fill_polygon(matrix, points, color_id)
    return draw_polyline(matrix, points + [points[0]], color_id)


# ---------------------------------------------------------------------------
# flood fill
# ---------------------------------------------------------------------------
def flood_fill(matrix: Matrix, x: int, y: int, color_id: int) -> int:
    """Replace the 4-connected region at (x, y) with ``color_id``."""
    h, w = matrix.shape
    if not (0 <= x < w and 0 <= y < h):
        raise ValueError(f"flood_fill origin ({x},{y}) out of bounds ({w}x{h})")
    target = int(matrix[y, x])
    if target == color_id:
        return 0
    stack = [(x, y)]
    n = 0
    while stack:
        px, py = stack.pop()
        if not (0 <= px < w and 0 <= py < h):
            continue
        if int(matrix[py, px]) != target:
            continue
        matrix[py, px] = color_id
        n += 1
        stack.append((px + 1, py))
        stack.append((px - 1, py))
        stack.append((px, py + 1))
        stack.append((px, py - 1))
    return n


# ---------------------------------------------------------------------------
# SVG-style path subset (M L H V C S Q T A Z, absolute & relative)
# ---------------------------------------------------------------------------
_NUM = r"[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?"
_TOKEN_RE = re.compile(rf"({_NUM}|[MmLlHhVvCcSsQqTtAaZz])")
_CMD_RE = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]")


class PathError(ValueError):
    pass


def parse_path(d: str) -> List[tuple]:
    """Parse an SVG path ``d`` into command tuples (case preserved).

    Commands::

        ('M'|'m', x, y) ('L'|'l', x, y) ('H'|'h', x) ('V'|'v', y)
        ('C'|'c', x1,y1,x2,y2,x,y) ('S'|'s', x2,y2,x,y)
        ('Q'|'q', x1,y1,x,y) ('T'|'t', x,y)
        ('A'|'a', rx, ry, phi, large_arc, sweep, x, y)
        ('Z',)
    """
    toks = _TOKEN_RE.findall(d)
    if not toks:
        raise PathError("empty path")
    segs: List[tuple] = []
    i = 0
    while i < len(toks):
        tok = toks[i]
        if not _CMD_RE.match(tok):
            raise PathError(f"expected command at token {i}: {tok!r}")
        cmd = tok
        i += 1
        nums: List[float] = []
        while i < len(toks) and not _CMD_RE.match(toks[i]):
            nums.append(float(toks[i]))
            i += 1
        n = len(nums)
        if cmd in "Mm":
            if n < 2 or n % 2 != 0:
                raise PathError(f"{cmd} needs pairs of coordinates, got {n}")
            for k in range(0, n, 2):
                segs.append((cmd, nums[k], nums[k + 1]))
        elif cmd in "Ll":
            if n % 2 != 0:
                raise PathError(f"{cmd} needs pairs of coordinates, got {n}")
            segs.extend((cmd, nums[k], nums[k + 1]) for k in range(0, n, 2))
        elif cmd in "HhVv":
            for k in range(n):
                segs.append((cmd, nums[k]))
        elif cmd in "Cc":
            if n % 6 != 0:
                raise PathError(f"{cmd} needs sextuples, got {n}")
            segs.extend((cmd,) + tuple(nums[k : k + 6]) for k in range(0, n, 6))
        elif cmd in "Ss":
            if n % 4 != 0:
                raise PathError(f"{cmd} needs quadruples, got {n}")
            segs.extend((cmd,) + tuple(nums[k : k + 4]) for k in range(0, n, 4))
        elif cmd in "Qq":
            if n % 4 != 0:
                raise PathError(f"{cmd} needs quadruples, got {n}")
            segs.extend((cmd,) + tuple(nums[k : k + 4]) for k in range(0, n, 4))
        elif cmd in "Tt":
            if n % 2 != 0:
                raise PathError(f"{cmd} needs pairs, got {n}")
            segs.extend((cmd, nums[k], nums[k + 1]) for k in range(0, n, 2))
        elif cmd in "Aa":
            if n % 7 != 0:
                raise PathError(f"{cmd} needs 7-tuples, got {n}")
            segs.extend((cmd,) + tuple(nums[k : k + 7]) for k in range(0, n, 7))
        elif cmd in "Zz":
            if n:
                raise PathError("Z takes no arguments")
            segs.append(("Z",))
        else:  # pragma: no cover
            raise PathError(f"unknown command {cmd!r}")
    return segs


def _normalize(segs: List[tuple]) -> List[tuple]:
    """Convert all relative commands to absolute; lowercase z to Z.

    Per the SVG spec the first 'm' is treated as absolute; after 'Z' the
    current point returns to the subpath start.
    """
    out: List[tuple] = []
    cx = cy = 0.0
    subpath_start = (0.0, 0.0)
    for seg in segs:
        cmd = seg[0]
        if cmd in "Zz":
            out.append(("Z",))
            cx, cy = subpath_start
            continue
        if cmd in "Mm":
            x, y = seg[1], seg[2]
            if cmd == "m":
                x, y = cx + x, cy + y
            out.append(("M", x, y))
            cx, cy = x, y
            subpath_start = (x, y)
        elif cmd in "Ll":
            x, y = seg[1], seg[2]
            if cmd == "l":
                x, y = cx + x, cy + y
            out.append(("L", x, y))
            cx, cy = x, y
        elif cmd in "Hh":
            x = cx + seg[1] if cmd == "h" else seg[1]
            out.append(("L", x, cy))
            cx = x
        elif cmd in "Vv":
            y = cy + seg[1] if cmd == "v" else seg[1]
            out.append(("L", cx, y))
            cy = y
        elif cmd in "Cc":
            a1, a2, a3, a4, a5, a6 = seg[1:]
            if cmd == "c":
                a1, a2, a3, a4, a5, a6 = a1 + cx, a2 + cy, a3 + cx, a4 + cy, a5 + cx, a6 + cy
            out.append(("C", a1, a2, a3, a4, a5, a6))
            cx, cy = a5, a6
        elif cmd in "Ss":
            a1, a2, a3, a4 = seg[1:]
            if cmd == "s":
                a1, a2, a3, a4 = a1 + cx, a2 + cy, a3 + cx, a4 + cy
            out.append(("S", a1, a2, a3, a4))
            cx, cy = a3, a4
        elif cmd in "Qq":
            a1, a2, a3, a4 = seg[1:]
            if cmd == "q":
                a1, a2, a3, a4 = a1 + cx, a2 + cy, a3 + cx, a4 + cy
            out.append(("Q", a1, a2, a3, a4))
            cx, cy = a3, a4
        elif cmd in "Tt":
            x, y = seg[1], seg[2]
            if cmd == "t":
                x, y = cx + x, cy + y
            out.append(("T", x, y))
            cx, cy = x, y
        elif cmd in "Aa":
            rx, ry, phi, la, sw, x, y = seg[1:]
            if cmd == "a":
                x, y = x + cx, y + cy
            out.append(("A", rx, ry, phi, la, sw, x, y))
            cx, cy = x, y
        else:  # pragma: no cover
            raise PathError(f"unknown command {cmd!r}")
    return out


def _bezier(p0, p1, p2, p3, steps: int) -> List[Tuple[float, float]]:
    out = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        out.append((x, y))
    return out


def _quad(p0, p1, p2, steps: int) -> List[Tuple[float, float]]:
    out = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt**2 * p0[0] + 2 * mt * t * p1[0] + t**2 * p2[0]
        y = mt**2 * p0[1] + 2 * mt * t * p1[1] + t**2 * p2[1]
        out.append((x, y))
    return out


def _arc_to_center(p0, rx, ry, phi_deg, large_arc, sweep, p1):
    """SVG endpoint-to-center arc parameterization."""
    rx, ry = abs(rx), abs(ry)
    phi = math.radians(phi_deg % 360.0)
    x1p = math.cos(phi) * (p0[0] - p1[0]) / 2 + math.sin(phi) * (p0[1] - p1[1]) / 2
    y1p = -math.sin(phi) * (p0[0] - p1[0]) / 2 + math.cos(phi) * (p0[1] - p1[1]) / 2
    lam = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry)
    if lam > 1:
        s = math.sqrt(lam)
        rx, ry = rx * s, ry * s
    num = max(0.0, rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p)
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    coef = math.sqrt(num / den) if den else 0.0
    if large_arc == sweep:
        coef = -coef
    cxp = coef * (rx * y1p / ry)
    cyp = coef * (-ry * x1p / rx)
    cx = math.cos(phi) * cxp - math.sin(phi) * cyp + (p0[0] + p1[0]) / 2
    cy = math.sin(phi) * cxp + math.cos(phi) * cyp + (p0[1] + p1[1]) / 2
    theta1 = math.atan2((y1p - cyp) / ry, (x1p - cxp) / rx)
    theta2 = math.atan2((-y1p - cyp) / ry, (-x1p - cxp) / rx)
    delta = (theta2 - theta1) % (2 * math.pi)
    if sweep == 0 and delta > 0:
        delta -= 2 * math.pi
    elif sweep == 1 and delta < 0:
        delta += 2 * math.pi
    return cx, cy, rx, ry, phi, theta1, delta


def _arc_points(p0, rx, ry, phi_deg, large_arc, sweep, p1, steps: int) -> List[Tuple[float, float]]:
    cx, cy, rx, ry, phi, theta1, delta = _arc_to_center(p0, rx, ry, phi_deg, large_arc, sweep, p1)
    pts = []
    for i in range(steps + 1):
        t = theta1 + delta * i / steps
        x = cx + rx * math.cos(phi) * math.cos(t) - ry * math.sin(phi) * math.sin(t)
        y = cy + rx * math.sin(phi) * math.cos(t) + ry * math.cos(phi) * math.sin(t)
        pts.append((x, y))
    return pts


def flatten_path(d: str, curve_steps: int = 24) -> List[Tuple[float, float]]:
    """Flatten a path into a dense polyline (absolute coordinates)."""
    segs = _normalize(parse_path(d))
    pts: List[Tuple[float, float]] = []
    cx, cy = 0.0, 0.0
    start: Tuple[float, float] = (0.0, 0.0)
    prev_cubic_ctrl: Tuple[float, float] | None = None
    prev_quad_ctrl: Tuple[float, float] | None = None

    for seg in segs:
        cmd = seg[0]
        if cmd == "M":
            cx, cy = seg[1], seg[2]
            start = (cx, cy)
            pts.append((cx, cy))
            prev_cubic_ctrl = prev_quad_ctrl = None
        elif cmd == "L":
            cx, cy = seg[1], seg[2]
            pts.append((cx, cy))
            prev_cubic_ctrl = prev_quad_ctrl = None
        elif cmd == "C":
            p0 = (cx, cy)
            pts.extend(_bezier(p0, (seg[1], seg[2]), (seg[3], seg[4]), (seg[5], seg[6]), curve_steps)[1:])
            cx, cy = seg[5], seg[6]
            prev_cubic_ctrl = (seg[3], seg[4])
            prev_quad_ctrl = None
        elif cmd == "S":
            p0 = (cx, cy)
            if prev_cubic_ctrl is not None:
                c1 = (2 * cx - prev_cubic_ctrl[0], 2 * cy - prev_cubic_ctrl[1])
            else:
                c1 = p0
            pts.extend(_bezier(p0, c1, (seg[1], seg[2]), (seg[3], seg[4]), curve_steps)[1:])
            cx, cy = seg[3], seg[4]
            prev_cubic_ctrl = (seg[1], seg[2])
            prev_quad_ctrl = None
        elif cmd == "Q":
            p0 = (cx, cy)
            pts.extend(_quad(p0, (seg[1], seg[2]), (seg[3], seg[4]), curve_steps)[1:])
            cx, cy = seg[3], seg[4]
            prev_quad_ctrl = (seg[1], seg[2])
            prev_cubic_ctrl = None
        elif cmd == "T":
            p0 = (cx, cy)
            if prev_quad_ctrl is not None:
                c1 = (2 * cx - prev_quad_ctrl[0], 2 * cy - prev_quad_ctrl[1])
            else:
                c1 = p0
            pts.extend(_quad(p0, c1, (seg[1], seg[2]), curve_steps)[1:])
            cx, cy = seg[1], seg[2]
            prev_quad_ctrl = c1
            prev_cubic_ctrl = None
        elif cmd == "A":
            pts.extend(
                _arc_points((cx, cy), seg[1], seg[2], seg[3], int(seg[4]), int(seg[5]), (seg[6], seg[7]), curve_steps)[1:]
            )
            cx, cy = seg[6], seg[7]
            prev_cubic_ctrl = prev_quad_ctrl = None
        elif cmd == "Z":
            pts.append(start)
            cx, cy = start
            prev_cubic_ctrl = prev_quad_ctrl = None
    return pts


def draw_path(
    matrix: Matrix, d: str, color_id: int, filled: bool = False, origin: Point = (0, 0)
) -> int:
    """Rasterize an SVG-style path ``d`` onto the matrix.

    Coordinates are float path coordinates shifted by ``origin``; the
    result is snapped to the integer grid (no anti-aliasing).
    """
    ox, oy = origin
    pts = flatten_path(d)
    grid = [(int(round(ox + px)), int(round(oy + py))) for px, py in pts]
    if not grid:
        return 0
    if filled:
        return fill_polygon(matrix, grid, color_id)
    return draw_polyline(matrix, grid, color_id)
