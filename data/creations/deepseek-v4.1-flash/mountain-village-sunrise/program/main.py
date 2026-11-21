import math
from math import pi, sin, cos, hypot

W = H = 128
c = new_canvas(W, H, background=None, name="result")

# ------------------------------------------------------------------ palette
COLS = {
    # sky gradient, top -> horizon
    "sky0": "#131a3e", "sky1": "#1d2452", "sky2": "#2c2a60", "sky3": "#3f2f6b",
    "sky4": "#58336f", "sky5": "#7a3c6d", "sky6": "#a04a63", "sky7": "#c46350",
    "sky8": "#e28748", "sky9": "#f4a955", "sky10": "#ffc879", "sky11": "#ffe3a8",
    "star": "#c6cff2", "sun_core": "#fffdf2", "sun_mid": "#fff3c4",
    # far mountains / mid mountains / valley hills
    "mA1": "#8c7fae", "mA2": "#6d6495", "mA_rim": "#cba9c1",
    "snow": "#eadfef", "snow2": "#d6c5dd",
    "mB1": "#544a78", "mB2": "#3f3760", "mB_rim": "#986f92",
    "mC1": "#332f4f", "mC2": "#26233c", "mC_rim": "#514269",
    # ground
    "gr1": "#2a332d", "gr2": "#1c2320", "gr3": "#3c4b3a", "gr_rim": "#66684a",
    # wood / roof / window
    "wd1": "#c89061", "wd2": "#96633f", "wd3": "#6d452b", "wd4": "#452a1c",
    "rf1": "#43344d", "rf2": "#2e2437", "rf_rim": "#ab7c88",
    "wn1": "#ffe291", "wn2": "#f2a93f", "door": "#3a2015",
    # pines: near = saturated green, far = hazy blue-green
    "pn0": "#6ba97b", "pn1": "#559166", "pn2": "#356c50", "pn3": "#22493c",
    "pn4": "#152e2a", "pn5": "#0c1c1b",
    "pnD1": "#3f6d78", "pnD2": "#2c4c58",
    # stone path / smoke / birds
    "st1": "#a99b9e", "st2": "#817383", "st3": "#5c5066", "st4": "#3d3449",
    "smoke": "#f0ddd2", "smoke2": "#c9ada6", "bird": "#241f33",
}
for _n, _h in COLS.items():
    c.color(_h, name=_n)

# ------------------------------------------------------------------ helpers
BAYER8 = [
    [0, 32, 8, 40, 2, 34, 10, 42],
    [48, 16, 56, 24, 50, 18, 58, 26],
    [12, 44, 4, 36, 14, 46, 6, 38],
    [60, 28, 52, 20, 62, 30, 54, 22],
    [3, 35, 11, 43, 1, 33, 9, 41],
    [51, 19, 59, 27, 49, 17, 57, 25],
    [15, 47, 7, 39, 13, 45, 5, 37],
    [63, 31, 55, 23, 61, 29, 53, 21],
]


def bv(x, y, seed=0):
    """ordered dither threshold in 0..1"""
    return (BAYER8[(y + seed * 3) & 7][(x + seed * 5) & 7] + 0.5) / 64.0


def mixd(x, y, ca, cb, t, seed=0):
    """ordered-dither blend between two palette names, t = weight of cb"""
    if t <= 0:
        return ca
    if t >= 1:
        return cb
    return cb if bv(x, y, seed) < t else ca


def rnd(x, y, seed=0):
    v = math.sin(x * 12.9898 + y * 4.1414 + seed * 78.233) * 43758.5453
    return v - math.floor(v)


def put(x, y, col):
    x = int(x); y = int(y)
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, col)


def ridge_top(pts, x, sharp=0.0):
    if x <= pts[0][0]:
        return pts[0][1]
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        if x0 <= x <= x1:
            t = (x - x0) / float(x1 - x0)
            ts = (1 - sharp) * ((1 - cos(pi * t)) / 2.0) + sharp * t
            return y0 + (y1 - y0) * ts
    return pts[-1][1]


# ------------------------------------------------------------------ 1. sky
SKY = [(0, "sky0"), (9, "sky1"), (18, "sky2"), (26, "sky3"), (33, "sky4"),
       (39, "sky5"), (44, "sky6"), (48, "sky7"), (52, "sky8"), (56, "sky9"),
       (60, "sky10"), (66, "sky11")]


def sky_col(x, y):
    if y <= SKY[0][0]:
        return SKY[0][1]
    for i in range(len(SKY) - 1):
        y0, n0 = SKY[i]
        y1, n1 = SKY[i + 1]
        if y0 <= y < y1:
            return mixd(x, y, n0, n1, (y - y0) / float(y1 - y0))
    return SKY[-1][1]


for y in range(H):
    for x in range(W):
        c.set(x, y, sky_col(x, y))

# stars high in the dark part of the sky
STARS = [(10, 13, 1.0), (22, 7, 0.6), (35, 16, 0.9), (46, 9, 0.5), (57, 20, 0.4),
         (74, 6, 0.8), (86, 14, 0.6), (97, 8, 0.9), (108, 18, 0.5), (117, 10, 0.7),
         (27, 27, 0.35), (66, 25, 0.3), (103, 26, 0.35)]
for sx, sy, sb in STARS:
    if sb > 0.75:
        put(sx, sy, "star")
        put(sx - 1, sy, "star")
        put(sx + 1, sy, "star")
        put(sx, sy - 1, "star")
        put(sx, sy + 1, "star")
    elif sb > 0.45:
        put(sx, sy, "star")
        put(sx + 1, sy, "star")
    elif rnd(sx, sy, 3) < 0.8:
        put(sx, sy, "star")


# ------------------------------------------------------------------ 2. clouds
def cloud(cx, cy, rx, ry, col, p=0.6, seed=0):
    for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            e = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
            if e <= 1.0:
                q = p * (1.0 - e) ** 0.55
                if bv(x, y, seed) < q:
                    put(x, y, col)


cloud(24, 58, 26, 2.6, "sky11", 0.75, 1)
cloud(104, 61, 22, 2.4, "sky11", 0.70, 2)
cloud(92, 42, 17, 1.8, "sky10", 0.55, 3)
cloud(22, 38, 13, 1.6, "sky10", 0.45, 4)

# ------------------------------------------------------------------ 3. sun
SX, SY = 64, 52
for y in range(SY - 30, SY + 31):
    for x in range(SX - 30, SX + 31):
        d = hypot(x - SX, y - SY)
        if d <= 6.0:
            put(x, y, "sun_core")
        elif d <= 8.4:
            put(x, y, mixd(x, y, "sun_core", "sun_mid", (d - 6.0) / 2.4))
        elif d <= 28:
            if d <= 12.0:
                col, p = "sun_mid", 0.70 - (d - 8.4) * 0.13
            elif d <= 17.0:
                col, p = "sky11", 0.42 - (d - 12.0) * 0.05
            elif d <= 23.0:
                col, p = "sky10", 0.30 - (d - 17.0) * 0.03
            else:
                col, p = "sky9", 0.18 - (d - 23.0) * 0.025
            if bv(x, y) < p:
                put(x, y, col)


# ------------------------------------------------------------------ 4. ranges
def draw_range(pts, ctop, cbase, crim, seed, depth=13.0, jit=1.6, rim_p=0.4,
               base_back=None, sharp=0.0):
    for x in range(W):
        top = int(round(ridge_top(pts, x, sharp) + (rnd(x, 0, seed) - 0.5) * jit))
        for y in range(max(0, top), H):
            t = min(1.0, (y - top) / depth)
            if base_back is None:
                col = mixd(x, y, ctop, cbase, 0.10 + 0.90 * t, seed)
            else:
                # darker at the crest, hazier toward the valley floor
                col = mixd(x, y, ctop, cbase, 0.10 + 0.90 * t, seed)
                col = mixd(x, y, col, base_back, max(0.0, (y - top - 6) / 22.0), seed + 1)
            c.set(x, y, col)
        if 0 <= top < H - 1:
            c.set(x, top, crim)
            if bv(x, top, seed) < rim_p:
                c.set(x, top + 1, crim)


A_PTS = [(-4, 66), (6, 52), (16, 60), (26, 44), (36, 56), (44, 50), (50, 60),
         (58, 64), (66, 60), (74, 64), (82, 54), (90, 44), (100, 58),
         (108, 50), (118, 60), (126, 52), (132, 62)]
draw_range(A_PTS, "mA2", "mA1", "mA_rim", 1, depth=16.0, jit=1.8, rim_p=0.5,
           base_back="mA1", sharp=0.35)


def snow_cap(pts, px, span, depth, seed=0):
    for dx in range(-span, span + 1):
        x = px + dx
        if not (0 <= x < W):
            continue
        top = int(round(ridge_top(pts, x, 0.35) + (rnd(x, 0, seed) - 0.5) * 1.2))
        h = depth * max(0.0, 1.0 - abs(dx) / float(span + 1)) ** 1.1
        h += (rnd(x, 1, seed) - 0.5) * 1.6
        hi = int(round(h))
        for k in range(max(0, hi)):
            y = top + k
            if 0 <= y < H:
                c.set(x, y, "snow" if k < hi - 2 else "snow2")


snow_cap(A_PTS, 26, 9, 7, 1)
snow_cap(A_PTS, 90, 10, 8, 2)
snow_cap(A_PTS, 118, 7, 5, 3)
snow_cap(A_PTS, 6, 6, 4, 4)

B_PTS = [(-4, 84), (8, 72), (18, 82), (28, 68), (38, 80), (46, 86), (54, 78),
         (62, 84), (70, 82), (78, 86), (86, 78), (94, 70), (104, 82),
         (112, 74), (122, 84), (132, 76)]
draw_range(B_PTS, "mB1", "mB2", "mB_rim", 2, depth=14.0, jit=1.8, rim_p=0.4,
           base_back="mB1")

C_PTS = [(-4, 102), (10, 97), (24, 99), (38, 95), (52, 98), (64, 96),
         (78, 98), (92, 94), (106, 98), (120, 96), (132, 101)]
draw_range(C_PTS, "mC2", "mC1", "mC_rim", 3, depth=12.0, jit=1.4, rim_p=0.3)


# ------------------------------------------------------------------ 5. pines
def pine_tree(cx, top_y, base_y, maxw, lit, mid, dark, tiers=3, jag=1.0,
              trunk=None):
    hgt = max(1, base_y - top_y)
    lit_right = cx >= SX
    for y in range(top_y, base_y + 1):
        t = (y - top_y) / float(hgt)
        half = (maxw / 2.0) * (0.28 + 0.72 * t) * (0.66 + 0.34 * ((t * tiers) % 1.0))
        x0 = int(round(cx - half)) + int(round((rnd(cx, y, 11) - 0.5) * 2 * jag))
        x1 = int(round(cx + half)) + int(round((rnd(cx, y, 12) - 0.5) * 2 * jag))
        if x1 < x0:
            x0, x1 = x1, x0
        for x in range(x0, x1 + 1):
            fx = (x - x0) / float(max(1, x1 - x0))
            dl = (1.0 - fx) if lit_right else fx
            if dl < 0.26:
                col = lit if rnd(x, y, 13) < 0.5 else mid
            elif dl < 0.68:
                col = mid
            else:
                col = dark
            put(x, y, col)
    if trunk:
        tw = max(1, maxw // 9)
        c.rect(int(cx - tw // 2), base_y - 1, tw, 4, trunk)


G_PTS = [(-4, 118), (10, 113), (22, 114), (34, 116), (46, 112), (54, 111),
         (64, 111), (74, 112), (84, 113), (96, 113), (108, 115), (120, 117),
         (132, 120)]

# small hazy pines on the far valley ridge
for px, ptop, pw in [(5, 84, 8), (12, 87, 7), (20, 83, 9), (98, 84, 9),
                     (105, 88, 7), (113, 85, 8), (122, 88, 7)]:
    pine_tree(px, ptop, int(ridge_top(C_PTS, px)) + 3, pw, "pnD1", "pnD2", "pnD2",
              tiers=4, jag=0.7)

# ------------------------------------------------------------------ 6. village
def draw_window(wx, wy, ww, wh):
    c.rect(wx, wy, ww, wh, "wn1")
    c.rect(wx, wy + wh - 2, ww, 2, "wn2")
    c.rect(wx - 1, wy - 1, ww + 2, 1, "wd4")
    c.rect(wx - 1, wy + wh, ww + 2, 1, "wd4")
    c.rect(wx - 1, wy - 1, 1, wh + 2, "wd4")
    c.rect(wx + ww, wy - 1, 1, wh + 2, "wd4")
    c.line(wx + ww // 2, wy, wx + ww // 2, wy + wh - 1, "wd3")


def draw_house(x0, w, wall_top, apex_y, door_w=6, chimney=None, wins=()):
    wall_bot = 124
    ax = x0 + w / 2.0
    eL, eR = x0 - 2, x0 + w + 1

    # ---- wall
    c.rect(x0, wall_top, w, wall_bot - wall_top + 1, "wd2")
    for px in range(x0 + 2, x0 + w - 1, 3):
        c.line(px, wall_top + 3, px, wall_bot, "wd3")
    c.line(x0, wall_top, x0, wall_bot, "wd3")
    c.line(x0 + w - 1, wall_top, x0 + w - 1, wall_bot, "wd4")
    # warm sunrise edge just under the eaves, plus a timber beam
    for x in range(x0, x0 + w):
        c.set(x, wall_top + 1, "wd1")
    c.line(x0 + 1, wall_top + 6, x0 + w - 2, wall_top + 6, "wd3")

    # ---- door (its base sits on the ground line)
    dx = x0 + (w - door_w) // 2
    dg = int(round(ridge_top(G_PTS, dx + door_w // 2)))
    dy = dg - 9
    c.rect(dx - 1, dy - 1, door_w + 2, dg - dy + 2, "wd4")
    c.rect(dx, dy, door_w, dg - dy + 1, "door")
    c.line(dx, dy, dx, dg, "wd1")
    c.rect(dx + door_w // 2 - 1, dy + 4, 2, 2, "wn2")

    # ---- windows
    for wx, wy, ww, wh in wins:
        draw_window(wx, wy, ww, wh)

    # ---- roof
    c.poly([(ax, apex_y), (eR, wall_top + 1), (eL, wall_top + 1)], "rf1", fill=True)
    rh = float(max(1, wall_top - apex_y))
    for y in range(apex_y, wall_top + 1):
        for x in range(int(eL), int(eR) + 1):
            if c.get(x, y) != c.color("rf1"):
                continue
            t = (y - apex_y) / rh
            if (y - apex_y) % 4 == 3:
                c.set(x, y, "rf2")                       # shingle course
            elif t > 0.55:
                if rnd(x, y, 21) < 0.26 * (t - 0.55) / 0.45:
                    c.set(x, y, "rf2")
    c.line(int(round(ax)), apex_y, eL, wall_top, "rf_rim")
    c.line(int(round(ax)), apex_y, eR, wall_top, "rf_rim")

    # ---- chimney
    if chimney:
        chx, chw, chtop = chimney
        if chx > ax:
            chend = int(apex_y + (chx + chw / 2.0 - ax) * (wall_top + 1 - apex_y) /
                        max(1.0, eR - ax)) + 1
        else:
            chend = int(apex_y + (ax - chx - chw / 2.0) * (wall_top + 1 - apex_y) /
                        max(1.0, ax - eL)) + 1
        c.rect(chx, chtop, chw, max(4, chend - chtop + 2), "wd3")
        c.rect(chx, chtop, chw, 1, "wd1")
        c.line(chx, chtop, chx, chend, "wd2")
        c.line(chx + chw - 1, chtop, chx + chw - 1, chend, "wd4")


# left house
draw_house(26, 17, 98, 90, door_w=5,
           wins=[(29, 103, 4, 4), (39, 103, 3, 4)],
           chimney=(37, 3, 88))
# right house
draw_house(84, 16, 96, 88, door_w=5,
           wins=[(87, 101, 4, 4), (95, 101, 3, 4)],
           chimney=(85, 3, 86))
# centre house - the focal point, biggest and brightest
draw_house(50, 27, 90, 81, door_w=6,
           wins=[(54, 96, 6, 5), (67, 96, 6, 5)],
           chimney=(67, 4, 77))

# ------------------------------------------------------------------ 7. ground
for x in range(W):
    top = int(round(ridge_top(G_PTS, x) + (rnd(x, 5, 21) - 0.5) * 1.0))
    for y in range(max(0, top), H):
        t = min(1.0, (y - top) / 15.0)
        c.set(x, y, mixd(x, y, "gr1", "gr2", 0.05 + 0.95 * t))
    if 0 <= top < H:
        c.set(x, top, "gr_rim" if (x // 4) % 3 == 0 else "gr3")
        if top + 1 < H and bv(x, top + 1, 2) < 0.22:
            c.set(x, top + 1, "gr3")

# grass tufts and shrubs along the ground line
TUFT = [(5, 1), (9, 2), (16, 1), (20, 3), (31, 1), (35, 1), (44, 2), (47, 4),
        (80, 3), (82, 1), (92, 1), (100, 3), (105, 1), (110, 2), (117, 1),
        (24, 1), (62, 1), (69, 1), (76, 2), (120, 2), (124, 3), (2, 2), (58, 1)]
HOUSE_SPAN = [(26, 43), (50, 77), (84, 99)]
TUFT = [t for t in TUFT
        if not any(lo - 1 <= t[0] <= hi + 1 for lo, hi in HOUSE_SPAN)]
for tx, th in TUFT:
    base = int(round(ridge_top(G_PTS, tx)))
    for k in range(th):
        put(tx, base - 1 - k, "gr3")
        if k == 0:
            put(tx - 1, base - 1, "gr3")
            put(tx + 1, base - 1, "gr3")
for bx, bw in [(44, 4), (81, 4), (94, 3), (30, 3), (70, 3)]:
    base = int(round(ridge_top(G_PTS, bx)))
    for y in range(base - 3, base + 1):
        for x in range(bx - bw // 2, bx + bw // 2 + 1):
            if hypot(x - bx, (y - base) * 1.4) <= bw / 2.0 + 0.4:
                put(x, y, "pn4" if rnd(x, y, 17) < 0.5 else "pn3")

# mid-distance pines flanking the village (green, living trees)
pine_tree(18, 91, 114, 16, "pn1", "pn2", "pn3", tiers=4, jag=1.0, trunk="wd4")
pine_tree(26, 100, 116, 10, "pn1", "pn2", "pn3", tiers=3, jag=1.0)
pine_tree(111, 89, 116, 17, "pn1", "pn2", "pn3", tiers=4, jag=1.0, trunk="wd4")
pine_tree(102, 99, 115, 10, "pn1", "pn2", "pn3", tiers=3, jag=1.0)
pine_tree(45, 102, 113, 8, "pn1", "pn2", "pn3", tiers=3, jag=0.8)
pine_tree(81, 103, 113, 7, "pn1", "pn2", "pn3", tiers=3, jag=0.8)

# ------------------------------------------------------------------ 8. stone path
PY0 = int(round(ridge_top(G_PTS, 63)))
for y in range(PY0, H):
    t = (y - PY0) / float(H - PY0)
    cx = 63 + 13 * (t ** 1.7)
    half = 1.8 + 9.0 * t
    x0 = int(round(cx - half))
    x1 = int(round(cx + half))
    for x in range(x0, x1 + 1):
        if x == x0 or x == x1:
            col = "st4"
        else:
            mortar = (x % 3 == 0) or ((y + 2 * ((x // 3) % 2)) % 3 == 0)
            if mortar:
                col = "st3"
            else:
                h = rnd(x // 3, y // 3, 5)
                col = "st1" if h < 0.30 else ("st2" if h < 0.78 else "st3")
        put(x, y, col)

# loose stones on the grass either side of the path
for rx, ry, rw in [(50, 120, 3), (55, 125, 2), (86, 121, 3), (91, 126, 2),
                   (46, 114, 2), (60, 116, 2)]:
    c.rect(rx, ry, rw, 2, "st2")
    c.rect(rx, ry, rw, 1, "st1")

# ------------------------------------------------------------------ 9. smoke
def plume(x0, y0, x1, y1, r0, r1, dens, steps=90, sway=3.0):
    for i in range(steps + 1):
        t = i / float(steps)
        cx = x0 + (x1 - x0) * t + sway * sin(t * 5.5) * t
        cy = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        p = dens * (1.0 - t) ** 0.85 + 0.05
        for yy in range(int(cy - r), int(cy + r) + 1):
            for xx in range(int(cx - r), int(cx + r) + 1):
                dd = hypot(xx - cx, yy - cy)
                if dd <= r:
                    pp = p * (1.0 - 0.6 * dd / max(0.6, r))
                    if rnd(xx, yy, 31) < pp:
                        put(xx, yy, "smoke" if rnd(xx, yy, 32) < 0.7 else "smoke2")


plume(69, 76, 86, 55, 1.2, 3.4, 0.95)
plume(38, 87, 31, 70, 0.9, 2.2, 0.8, sway=2.0)
plume(86, 85, 95, 73, 0.8, 1.7, 0.7, sway=1.5)

# ------------------------------------------------------------------ 10. birds
for bx, by in [(30, 30), (37, 25), (43, 34), (78, 22)]:
    put(bx - 1, by - 1, "bird")
    put(bx, by, "bird")
    put(bx + 1, by - 1, "bird")

# ------------------------------------------------------------------ 11. foreground silhouettes
pine_tree(-6, 94, 128, 28, "pn4", "pn5", "pn5", tiers=4, jag=1.2)
pine_tree(7, 107, 128, 16, "pn5", "pn5", "pn5", tiers=3, jag=1.2)
pine_tree(134, 91, 128, 30, "pn4", "pn5", "pn5", tiers=4, jag=1.2)
pine_tree(119, 105, 128, 16, "pn5", "pn5", "pn5", tiers=3, jag=1.2)

# mottled grass in the foreground
for y in range(112, H):
    for x in range(W):
        if bv(x, y, 9) < 0.10 and rnd(x, y, 4) < 0.6:
            if c.get(x, y) in (c.color("gr1"), c.color("gr2")):
                c.set(x, y, "gr3" if rnd(x, y, 8) < 0.45 else "gr2")

# ------------------------------------------------------------------ checks
pal = c.palette()
print("palette entries:", len(pal))
print(c.stats_text())

GROUP = [
    (("sky0", "sky1", "sky2", "sky3", "sky4", "sky5", "sky6", "sky7", "sky8",
      "sky9", "sky10", "sky11"), "."),
    (("star",), "*"),
    (("sun_core", "sun_mid"), "O"),
    (("mA1", "mA2", "mA_rim"), "a"),
    (("mB1", "mB2", "mB_rim"), "b"),
    (("mC1", "mC2", "mC_rim"), "c"),
    (("gr1", "gr2", "gr3", "gr_rim"), "g"),
    (("wd1", "wd2", "wd3", "wd4"), "W"),
    (("rf1", "rf2", "rf_rim"), "R"),
    (("wn1", "wn2"), "w"),
    (("door",), "d"),
    (("pn0", "pn1", "pn2", "pn3", "pn4", "pn5"), "T"),
    (("pnD1", "pnD2"), "t"),
    (("st1", "st2", "st3", "st4"), "="),
    (("smoke", "smoke2"), "s"),
    (("bird",), "^"),
]
name_of = {p["index"]: p["name"] for p in pal}
ch_of = {}
for names, ch in GROUP:
    for n in names:
        ch_of[n] = ch
lines = []
for y in range(0, H, 2):
    row = []
    for x in range(0, W, 2):
        n = name_of.get(c.get(x, y), "?")
        row.append(ch_of.get(n, "?"))
    lines.append("%3d %s" % (y, "".join(row)))
print("\n".join(lines))

DETAIL = {"wd1": "W", "wd2": "w", "wd3": "x", "wd4": "k", "rf1": "R", "rf2": "r",
          "rf_rim": "i", "wn1": "O", "wn2": "o", "door": "D", "st1": "=",
          "st2": "=", "st3": "-", "st4": "_", "gr1": ",", "gr2": ",", "gr3": "'",
          "gr_rim": "q", "smoke": "s", "smoke2": "s", "bird": "^", "pn0": "T",
          "pn1": "T", "pn2": "T", "pn3": "T", "pn4": "T", "pn5": "T",
          "pnD1": "t", "pnD2": "t"}


def detail(x0, y0, x1, y1):
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            n = name_of.get(c.get(x, y), ".")
            row.append(DETAIL.get(n, "."))
        print("%3d %s" % (y, "".join(row)))


# ------------------------------------------------------------------ output
result = c
print("visible colours used:", c.stats()["colors_used"])
save("mountain-village-sunrise", result, indexed=True)
finish(result)
