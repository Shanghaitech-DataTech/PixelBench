"""Procedural pixel-art reference generators.

These produce deterministic, clean pixel art used as replication
references, restoration targets and direct-generation hints.  They are
*not* meant to be artistic masterpieces — they are readable, palette
disciplined, and cover several asset classes (character / item / tile /
icon / prop).
"""
from __future__ import annotations

import math
import random
from typing import Callable, Dict, List, Tuple

from pixelbench.core.canvas import PixelCanvas
from pixelbench.core.color import parse_hex

RGBA = Tuple[int, int, int, int]


def _c(hex_: str) -> RGBA:
    return parse_hex(hex_)


class _Ctx:
    """Scales normalized (0..1) coordinates to a target canvas."""

    def __init__(self, canvas: PixelCanvas) -> None:
        self.canvas = canvas
        self.w = canvas.width
        self.h = canvas.height
        self.rng = random.Random()

    def seed(self, seed: int) -> None:
        self.rng.seed(seed)

    def nx(self, u: float) -> int:
        return max(0, min(self.w - 1, int(round(u * (self.w - 1)))))

    def ny(self, v: float) -> int:
        return max(0, min(self.h - 1, int(round(v * (self.h - 1)))))

    def nw(self, u: float) -> int:
        return max(1, int(round(u * self.w)))

    def nh(self, v: float) -> int:
        return max(1, int(round(v * self.h)))


def _make_canvas(width: int, height: int) -> PixelCanvas:
    return PixelCanvas(width, height, transparent_id=0)


# ---------------------------------------------------------------------------
# assets
# ---------------------------------------------------------------------------
def heart(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#3a1d2e"))
    red = c.register_color("red", _c("#e0455a"))
    dark = c.register_color("dark_red", _c("#a92c40"))
    shine = c.register_color("shine", _c("#ffd9de"))

    cx, cy = ctx.nx(0.5), ctx.ny(0.52)
    r = max(2, min(ctx.nw(0.34), ctx.nh(0.36)))
    # heart curve: (16 sin^3 t, 13 cos t - 5 cos 2t - 2 cos 3t - cos 4t)
    pts = []
    for i in range(96):
        t = 2 * math.pi * i / 96
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((int(round(cx + x * r / 16)), int(round(cy - y * r / 16))))
    c.draw_polygon(pts, red, filled=True)
    c.draw_polygon(pts, outline)
    # shading: bottom darker
    c.paint_ellipse(cx, cy + r // 2, r // 2, r // 4, dark)
    # highlight
    for i in range(max(2, r // 5)):
        c.set_pixel(cx - r // 2 + i, cy - r // 3, shine)
    return c


def coin(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    gold = c.register_color("gold", _c("#f2c14e"))
    gold_dark = c.register_color("gold_dark", _c("#b8862e"))
    gold_light = c.register_color("gold_light", _c("#ffe9a3"))
    outline = c.register_color("outline", _c("#5b4316"))

    cx, cy = ctx.nx(0.5), ctx.ny(0.5)
    r = max(3, min(ctx.nw(0.4), ctx.nh(0.42)))
    c.paint_circle(cx, cy, r, gold_dark)
    c.paint_circle(cx, cy, r - 1, gold)
    c.stroke_circle(cx, cy, r - 1, outline)
    c.stroke_circle(cx, cy, max(1, r // 3), outline)
    # star emboss
    pts = _star_points(cx, cy, max(1, r // 3), max(1, r // 6), 5, 0.0)
    c.draw_polygon(pts, outline, filled=True)
    # shine
    for i in range(max(1, r // 4)):
        c.set_pixel(cx - r + 1 + i, cy - r // 2, gold_light)
    return c


def mushroom(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#4a2c17"))
    cap = c.register_color("cap_red", _c("#d94b4b"))
    cap_dark = c.register_color("cap_dark", _c("#a83030"))
    spot = c.register_color("spot", _c("#fdf2e3"))
    stem = c.register_color("stem", _c("#f0ddc2"))
    stem_dark = c.register_color("stem_dark", _c("#c9ab8a"))

    cx = ctx.nx(0.5)
    cap_cy = ctx.ny(0.42)
    rx, ry = ctx.nw(0.36), ctx.nh(0.26)
    c.paint_ellipse(cx, cap_cy, rx, ry, cap)
    c.paint_ellipse(cx, cap_cy + ry // 3, rx, ry // 2, cap_dark)
    c.stroke_ellipse(cx, cap_cy, rx, ry, outline)
    # stem
    sw, sh = ctx.nw(0.14), ctx.nh(0.36)
    c.paint_rect(cx - sw // 2, cap_cy + ry // 3, sw, sh, stem)
    c.stroke_rect(cx - sw // 2, cap_cy + ry // 3, sw, sh, outline)
    c.paint_rect(cx - sw // 2, cap_cy + ry // 3 + sh - ctx.nh(0.08), sw, ctx.nh(0.08), stem_dark)
    # spots
    for i in range(4):
        sx = cx + ctx.rng.randint(-rx + 2, rx - 2)
        sy = cap_cy + ctx.rng.randint(-ry + 2, ry // 3 - 1)
        if ctx.rng.random() < 0.5:
            c.set_pixel(sx, sy, spot)
        else:
            c.paint_rect(sx, sy, 2, 1, spot)
    return c


def potion(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#2b2b2b"))
    glass = c.register_color("glass", _c("#cfe8ef"))
    liquid = c.register_color("liquid", _c("#d94848"))
    liquid_light = c.register_color("liquid_light", _c("#ff8a8a"))
    cork = c.register_color("cork", _c("#a97b4d"))

    cx = ctx.nx(0.5)
    top = ctx.ny(0.18)
    bw, bh = ctx.nw(0.4), ctx.nh(0.52)
    bx, by = cx - bw // 2, top + ctx.nh(0.14)
    # bottle body
    c.paint_rect(bx, by, bw, bh, glass)
    c.stroke_rect(bx, by, bw, bh, outline)
    # liquid inside
    ly = by + bh - ctx.nh(0.22)
    c.paint_rect(bx + 1, ly, bw - 2, bh - 1 - (ly - by - 1), liquid)
    # liquid highlight
    for i in range(max(1, bw // 4)):
        c.set_pixel(bx + 2 + i, ly + 1, liquid_light)
    # neck
    nw_, nh_ = ctx.nw(0.14), ctx.nh(0.12)
    c.paint_rect(cx - nw_ // 2, by - nh_, nw_, nh_, glass)
    c.stroke_rect(cx - nw_ // 2, by - nh_, nw_, nh_, outline)
    # cork
    c.paint_rect(cx - nw_ // 2 - 1, by - nh_ - ctx.nh(0.07), nw_ + 2, ctx.nh(0.07), cork)
    c.stroke_rect(cx - nw_ // 2 - 1, by - nh_ - ctx.nh(0.07), nw_ + 2, ctx.nh(0.07), outline)
    return c


def tree(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#3a2a16"))
    trunk = c.register_color("trunk", _c("#8a5a33"))
    leaf = c.register_color("leaf", _c("#3f9b4f"))
    leaf_dark = c.register_color("leaf_dark", _c("#2c7238"))

    cx = ctx.nx(0.5)
    tw, th = ctx.nw(0.12), ctx.nh(0.34)
    ty = ctx.ny(0.62)
    c.paint_rect(cx - tw // 2, ty, tw, th, trunk)
    c.stroke_rect(cx - tw // 2, ty, tw, th, outline)
    # foliage: three overlapping circles
    r1 = ctx.nw(0.3)
    cy1 = ty - r1
    c.paint_circle(cx, cy1, r1, leaf)
    c.paint_circle(cx - r1 // 2, cy1 + r1 // 3, int(r1 * 0.8), leaf_dark)
    c.paint_circle(cx + r1 // 2, cy1 + r1 // 3, int(r1 * 0.8), leaf)
    c.stroke_circle(cx, cy1, r1, outline)
    # fruit dots
    for i in range(3):
        fx = cx + ctx.rng.randint(-r1 + 2, r1 - 2)
        fy = cy1 + ctx.rng.randint(-r1 + 2, r1 - 2)
        c.set_pixel(fx, fy, outline)
    return c


def knight(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#222222"))
    armor = c.register_color("armor", _c("#9aa5b1"))
    armor_dark = c.register_color("armor_dark", _c("#6b7686"))
    helmet = c.register_color("helmet", _c("#c8d0da"))
    skin = c.register_color("skin", _c("#e8b98a"))
    cape = c.register_color("cape", _c("#3f5fd9"))
    blade = c.register_color("blade", _c("#e8eef4"))

    cx = ctx.nx(0.5)
    # cape (back layer)
    c.draw_polygon([(cx + 4, ctx.ny(0.3)), (cx + 12, ctx.ny(0.55)), (cx + 4, ctx.ny(0.8))], cape, filled=True)
    # legs
    c.paint_rect(cx - 6, ctx.ny(0.62), 5, ctx.nh(0.2), armor_dark)
    c.paint_rect(cx + 1, ctx.ny(0.62), 5, ctx.nh(0.2), armor_dark)
    # torso
    c.paint_rect(cx - 6, ctx.ny(0.4), 12, ctx.nh(0.22), armor)
    c.stroke_rect(cx - 6, ctx.ny(0.4), 12, ctx.nh(0.22), outline)
    # arms
    c.paint_rect(cx - 9, ctx.ny(0.42), 3, ctx.nh(0.16), armor_dark)
    c.paint_rect(cx + 6, ctx.ny(0.42), 3, ctx.nh(0.16), armor_dark)
    # head + helmet
    hy = ctx.ny(0.3)
    c.paint_rect(cx - 4, hy, 8, ctx.nh(0.1), skin)
    c.paint_rect(cx - 4, hy - ctx.nh(0.05), 8, ctx.nh(0.06), helmet)
    c.paint_rect(cx - 6, hy - ctx.nh(0.09), 12, ctx.nh(0.05), helmet)
    c.stroke_rect(cx - 6, hy - ctx.nh(0.09), 12, ctx.nh(0.05), outline)
    # sword
    sx = cx + 8
    c.draw_line(sx, ctx.ny(0.2), sx + 2, ctx.ny(0.42), blade)
    c.draw_line(sx + 1, ctx.ny(0.2), sx + 3, ctx.ny(0.42), blade)
    c.paint_rect(sx - 1, ctx.ny(0.42), 5, ctx.nh(0.03), outline)  # guard
    # shield
    c.paint_rect(cx - 12, ctx.ny(0.42), 5, ctx.nh(0.16), armor_dark)
    c.stroke_rect(cx - 12, ctx.ny(0.42), 5, ctx.nh(0.16), outline)
    return c


def star(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    gold = c.register_color("gold", _c("#ffd94a"))
    gold_dark = c.register_color("gold_dark", _c("#d19a1f"))
    outline = c.register_color("outline", _c("#6b4a00"))

    cx, cy = ctx.nx(0.5), ctx.ny(0.5)
    r_outer = max(3, min(ctx.nw(0.42), ctx.nh(0.42)))
    r_inner = max(1, int(r_outer * 0.42))
    pts = _star_points(cx, cy, r_outer, r_inner, 5, -math.pi / 2)
    c.draw_polygon(pts, gold, filled=True)
    c.draw_polygon(pts, outline)
    c.draw_polygon(_star_points(cx, cy, r_outer - 1, r_inner, 5, -math.pi / 2 + math.pi / 5), gold_dark, filled=True)
    return c


def flower(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#2e2e2e"))
    petal = c.register_color("petal", _c("#f06a8a"))
    petal_dark = c.register_color("petal_dark", _c("#c14a68"))
    center = c.register_color("center", _c("#f7c948"))
    stem = c.register_color("stem", _c("#3f9b4f"))

    cx = ctx.nx(0.5)
    cy = ctx.ny(0.4)
    r = max(2, min(ctx.nw(0.24), ctx.nh(0.24)))
    c.paint_rect(cx - 1, cy + r, 2, ctx.nh(0.4), stem)
    # petals
    for i in range(8):
        ang = 2 * math.pi * i / 8
        px = cx + int(round(2 * r * math.cos(ang)))
        py = cy + int(round(2 * r * math.sin(ang)))
        c.paint_circle(px, py, r, petal if i % 2 == 0 else petal_dark)
    c.paint_circle(cx, cy, r, center)
    c.stroke_circle(cx, cy, r, outline)
    return c


def chest(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#3a2410"))
    wood = c.register_color("wood", _c("#b0783a"))
    wood_dark = c.register_color("wood_dark", _c("#8a5a28"))
    metal = c.register_color("metal", _c("#d8c390"))
    metal_dark = c.register_color("metal_dark", _c("#a8935f"))

    cx = ctx.nx(0.5)
    bw, bh = ctx.nw(0.6), ctx.nh(0.34)
    bx, by = cx - bw // 2, ctx.ny(0.58)
    # lid
    lid_h = ctx.nh(0.14)
    c.paint_rect(bx, by - lid_h, bw, lid_h, wood_dark)
    c.stroke_rect(bx, by - lid_h, bw, lid_h, outline)
    # body
    c.paint_rect(bx, by, bw, bh, wood)
    c.stroke_rect(bx, by, bw, bh, outline)
    # planks
    c.draw_line(bx, by + bh // 2, bx + bw - 1, by + bh // 2, outline)
    c.draw_line(bx + bw // 2, by, bx + bw // 2, by + bh - 1, outline)
    # lock
    c.paint_rect(cx - 2, by - ctx.nh(0.02), 4, ctx.nh(0.1), metal)
    c.paint_rect(cx - 1, by - ctx.nh(0.02), 2, ctx.nh(0.06), metal_dark)
    c.stroke_rect(cx - 2, by - ctx.nh(0.02), 4, ctx.nh(0.1), outline)
    # bands
    c.paint_rect(bx, by, 2, bh, metal)
    c.paint_rect(bx + bw - 2, by, 2, bh, metal)
    return c


def sword(width: int, height: int, seed: int = 0) -> PixelCanvas:
    c = _make_canvas(width, height)
    ctx = _Ctx(c)
    ctx.seed(seed)
    outline = c.register_color("outline", _c("#222222"))
    blade = c.register_color("blade", _c("#dfe8f0"))
    blade_edge = c.register_color("blade_edge", _c("#9fb2c2"))
    guard = c.register_color("guard", _c("#c9973f"))
    grip = c.register_color("grip", _c("#6b4a2a"))

    cx = ctx.nx(0.5)
    tip_y = ctx.ny(0.12)
    base_y = ctx.ny(0.62)
    c.draw_polygon(
        [(cx, tip_y), (cx + ctx.nw(0.05), base_y), (cx - ctx.nw(0.05), base_y)], blade, filled=True
    )
    c.draw_line(cx, tip_y + 1, cx, base_y - 1, blade_edge)
    c.draw_polygon(
        [(cx, tip_y), (cx + ctx.nw(0.05), base_y), (cx - ctx.nw(0.05), base_y)], outline
    )
    # guard
    g = ctx.nw(0.14)
    c.paint_rect(cx - g // 2, base_y, g, ctx.nh(0.04), guard)
    # grip
    gr = ctx.nw(0.04)
    c.paint_rect(cx - gr // 2, base_y + ctx.nh(0.04), gr, ctx.nh(0.14), grip)
    # pommel
    c.paint_circle(cx, base_y + ctx.nh(0.19), max(1, ctx.nw(0.03)), guard)
    return c


def _star_points(cx: int, cy: int, r_outer: int, r_inner: int, n: int, rot: float) -> List[Tuple[int, int]]:
    pts = []
    for i in range(2 * n):
        ang = rot + math.pi * i / n
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((int(round(cx + r * math.cos(ang))), int(round(cy + r * math.sin(ang)))))
    return pts


# ---------------------------------------------------------------------------
# library
# ---------------------------------------------------------------------------
ASSET_KINDS = ["heart", "coin", "mushroom", "potion", "tree", "knight", "star", "flower", "chest", "sword"]

_GENERATORS: Dict[str, Callable[..., PixelCanvas]] = {
    "heart": heart,
    "coin": coin,
    "mushroom": mushroom,
    "potion": potion,
    "tree": tree,
    "knight": knight,
    "star": star,
    "flower": flower,
    "chest": chest,
    "sword": sword,
}


class AssetLibrary:
    def __init__(self, seed: int = 0) -> None:
        self.seed = seed

    def list_kinds(self) -> List[str]:
        return list(ASSET_KINDS)

    def generate(self, kind: str, width: int, height: int, seed: Optional[int] = None) -> PixelCanvas:
        if kind not in _GENERATORS:
            raise ValueError(f"unknown asset kind {kind!r}; available: {ASSET_KINDS}")
        return _GENERATORS[kind](width, height, seed if seed is not None else self.seed)

    def describe(self, kind: str) -> str:
        descriptions = {
            "heart": "a small red pixel heart with outline and a shine highlight",
            "coin": "a round gold coin with embossed star and highlight",
            "mushroom": "a red-capped mushroom with white spots and a cream stem",
            "potion": "a glass potion bottle with a red liquid and a cork",
            "tree": "a round green tree with a brown trunk and fruit dots",
            "knight": "a side-view knight with helmet, sword, shield and blue cape",
            "star": "a five-point gold star with dark outline",
            "flower": "an eight-petal pink flower with yellow center and green stem",
            "chest": "a wooden treasure chest with metal bands and a lock",
            "sword": "a straight-blade sword with golden guard and brown grip",
        }
        return descriptions.get(kind, kind)
