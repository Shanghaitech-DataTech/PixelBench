# ==================================================================
#  red-roofed-forge-house  -  128x128 isometric RTS sprite
#
#  Parallel 2:1 iso projection (no perspective distortion):
#      screen = (64 + u - v , 73 + (u+v)/2 - h)
#  house footprint u,v in [0,32]; wall top h=36
#  roof: pitch 0.5 -> ridge h=56 (v=0), eave h=38 (v=36)
#  rake lines are exact 45-degree diagonals; ridge/eave are 2:1
# ==================================================================
import math
import random

c = new_canvas(128, 128, background=None, name="forge_house")
OUT = "#241a14"


def P(u, v, h):
    return (int(round(64 + u - v)), int(round(73 + (u + v) / 2.0 - h)))


def linep(a, b, col):
    c.line(a[0], a[1], b[0], b[1], col)


def on_plate(x, y, m=0.94):
    return abs(x - 64) / 60.0 + abs(y - 89) / 30.0 <= m


# ------------------------------------------------------------------
# ground plate (floating RTS tile)
# ------------------------------------------------------------------
c.poly([(4, 89), (64, 59), (124, 89), (124, 93), (64, 123), (4, 93)], "#2a1f16", True)
c.poly([(64, 59), (124, 89), (64, 119), (4, 89)], "#3f7a33", True)
linep((4, 89), (64, 59), "#4f8a3c")
linep((64, 59), (124, 89), "#4f8a3c")
linep((4, 89), (64, 119), "#2c4a24")
linep((64, 119), (124, 89), "#2c4a24")

rnd = random.Random(7)
for _ in range(300):
    x = rnd.randint(5, 123)
    y = rnd.randint(60, 118)
    if not on_plate(x, y):
        continue
    r = rnd.random()
    c.set(x, y, "#35682b" if r < 0.45 else ("#4a8a39" if r < 0.85 else "#59994a"))
for (uu, vv) in [(8, 40), (24, 44), (-6, 30), (40, 36), (-10, 18), (44, 20),
                 (28, 44), (46, 30), (2, 46), (20, -6), (44, 2), (-12, 8),
                 (36, -8), (-4, 38)]:
    x, y = P(uu, vv, 0)
    c.set(x, y, "#2c4a24")
    c.set(x, y - 1, "#35682b")
    c.set(x + 1, y - 1, "#2c4a24")

# ------------------------------------------------------------------
# dirt path from the yard to the front-left edge
# ------------------------------------------------------------------
c.poly([P(36, 26, 0), P(42, 26, 0), P(25, 46, 0), P(13, 46, 0)], "#9a7b54", True)
for _ in range(50):
    t = rnd.random()
    uu = 39 - 22 * t + rnd.uniform(-2.5, 2.5)
    vv = 26 + 20 * t + rnd.uniform(-2.0, 2.0)
    x, y = P(uu, vv, 0)
    if on_plate(x, y, 0.97):
        c.set(x, y, "#8a6b48" if rnd.random() < 0.6 else "#b3987a")

# ------------------------------------------------------------------
# forge yard (trampled dirt in front of the furnace)
# ------------------------------------------------------------------
c.poly([P(32, 6, 0), P(44, 6, 0), P(44, 26, 0), P(32, 26, 0)], "#8a6b48", True)
for _ in range(110):
    uu = rnd.uniform(32.5, 43.5)
    vv = rnd.uniform(6.5, 25.5)
    x, y = P(uu, vv, 0)
    c.set(x, y, "#7a5c3c" if rnd.random() < 0.55 else "#9a7b54")

# ------------------------------------------------------------------
# cast shadow (light from the upper left)
# ------------------------------------------------------------------
c.poly([P(-2, -2, 0), P(40, -2, 0), P(40, 34, 0), P(-2, 34, 0)], "#35682b", True)
c.poly([P(0, 0, 0), P(38, 0, 0), P(38, 32, 0), P(0, 32, 0)], "#2c4a24", True)

# ------------------------------------------------------------------
# furnace light spill on the yard
# ------------------------------------------------------------------
c.poly([P(32, 6, 0), P(36, 6, 0), P(36, 26, 0), P(32, 26, 0)], "#ffb545", True)
c.poly([P(36, 6, 0), P(40, 6, 0), P(40, 26, 0), P(36, 26, 0)], "#e8934a", True)
c.poly([P(40, 6, 0), P(44, 6, 0), P(44, 26, 0), P(40, 26, 0)], "#b06a34", True)

# ------------------------------------------------------------------
# dressing: pine, bushes, rocks
# ------------------------------------------------------------------
c.ellipse(14, 89, 8, 3, "#2c4a24", True)
c.rect(13, 82, 2, 7, "#6b4527")
c.set(13, 84, "#5f3c20")
for (x0, x1, yb, yt) in [(6, 22, 84, 72), (8, 20, 78, 67), (10, 18, 72, 61)]:
    c.poly([(x0, yb), (x1, yb), (14, yt)], "#2e5c26", True)
    c.poly([(x0, yb), (14, yb), (14, yt)], "#3f7a33", True)
    c.poly([(x0, yb), (x1, yb), (14, yt)], OUT, False)
c.set(11, 80, "#2e5c26")
c.set(17, 75, "#2e5c26")
c.set(13, 69, "#2e5c26")


def bush(cx, cy, w=7, h=4):
    c.ellipse(cx, cy, w // 2, h // 2, "#2e5c26", True)
    c.ellipse(cx - 1, cy - 1, max(1, w // 2 - 1), max(1, h // 2 - 1), "#3f7a33", True)


bush(*P(8, 40, 0))
bush(*P(-8, 34, 0))
bush(*P(30, 40, 0))


def rock(cx, cy, w, h):
    c.poly([(cx - w // 2, cy), (cx - w // 2 + 1, cy - h // 2),
            (cx + w // 2 - 1, cy - h // 2 + 1), (cx + w // 2, cy)], "#6a6a74", True)
    c.poly([(cx - w // 2, cy), (cx - w // 2 + 1, cy - h // 2),
            (cx - 1, cy - h // 2 + 1), (cx - 1, cy)], "#9c9ca6", True)
    c.poly([(cx - w // 2, cy), (cx - w // 2 + 1, cy - h // 2),
            (cx + w // 2 - 1, cy - h // 2 + 1), (cx + w // 2, cy)], OUT, False)


rock(*P(0, 38, 0), 6, 4)
rock(*P(36, 36, 0), 5, 3)
rock(*P(44, 14, 0), 4, 3)

# ------------------------------------------------------------------
# right gable wall (u = 32) - the forge wall
# ------------------------------------------------------------------
gable = [P(32, 0, 0), P(32, 32, 0), P(32, 32, 40), P(32, 0, 56)]
c.poly(gable, "#b3987a", True)
c.poly([P(32, 0, 0), P(32, 32, 0), P(32, 32, 6), P(32, 0, 6)], "#7b7b85", True)
linep(P(32, 0, 6), P(32, 32, 6), "#9c9ca6")
linep(P(32, 0, 0), P(32, 32, 0), "#5c5c66")
c.poly([P(32, 0, 0), P(32, 4, 0), P(32, 4, 54), P(32, 0, 56)], "#5f4128", True)
c.poly([P(32, 28, 0), P(32, 32, 0), P(32, 32, 40), P(32, 28, 42)], "#5f4128", True)
c.poly([P(32, 0, 56), P(32, 32, 40), P(32, 32, 37), P(32, 0, 53)], "#5f4128", True)


def arch(v0, v1, hb, ha, n=12):
    pts = []
    for i in range(n + 1):
        v = v0 + (v1 - v0) * i / float(n)
        h = hb + ha * math.sin(math.pi * (v - v0) / (v1 - v0))
        pts.append(P(32, v, h))
    return pts


# --- stone furnace with a glowing arch -----------------------------
outer = [P(32, 6, 0)] + arch(6, 26, 13, 3) + [P(32, 26, 0)]
c.poly(outer, "#8a8a94", True)
for (av, ah) in [(8, 5), (12, 10), (20, 10), (24, 5)]:
    x, y = P(32, av, ah)
    c.set(x, y, "#6a6a74")
    c.set(x, y + 1, "#6a6a74")
inner = [P(32, 10, 0)] + arch(10, 22, 9, 3, 6) + [P(32, 22, 0)]
c.poly(inner, "#2a1e1a", True)
for (col, dy) in [("#e8641a", 3), ("#f8821e", 5), ("#ffb545", 7), ("#ffe08a", 9)]:
    c.poly([P(32, 10, 0)] + [(x, y + dy) for (x, y) in arch(10, 22, 9, 3, 6)]
           + [P(32, 22, 0)], col, True)
c.poly([P(32, 14, 4), P(32, 18, 4), P(32, 18, 0), P(32, 14, 0)], "#fff4c8", True)
c.set(81, 91, "#fff4c8")
c.set(79, 93, "#fff4c8")
c.poly(outer, OUT, False)

# --- gable window (warm light from the forge) ----------------------
c.poly([P(32, 4, 32), P(32, 12, 32), P(32, 12, 22), P(32, 4, 22)], "#4a3220", True)
c.poly([P(32, 6, 30), P(32, 10, 30), P(32, 10, 24), P(32, 6, 24)], "#c06a28", True)
c.poly([P(32, 6, 27), P(32, 10, 27), P(32, 10, 24), P(32, 6, 24)], "#e8934a", True)
linep(P(32, 8, 30), P(32, 8, 24), "#4a3220")
c.poly([P(32, 4, 22), P(32, 14, 22), P(32, 14, 20), P(32, 4, 20)], "#9c9ca6", True)
c.poly(gable, OUT, False)

# ------------------------------------------------------------------
# left wall (v = 32) - lit plaster, door, wooden sign
# ------------------------------------------------------------------
wall = [P(0, 32, 0), P(32, 32, 0), P(32, 32, 36), P(0, 32, 36)]
c.poly(wall, "#dcc7a0", True)
c.poly([P(0, 32, 0), P(32, 32, 0), P(32, 32, 6), P(0, 32, 6)], "#8a8a94", True)
linep(P(0, 32, 6), P(32, 32, 6), "#a9a9b2")
linep(P(0, 32, 0), P(32, 32, 0), "#6a6a74")
for uu in (22, 26):
    x, y = P(uu, 32, 3)
    c.set(x, y, "#6a6a74")
    c.set(x, y + 1, "#6a6a74")
c.poly([P(0, 32, 0), P(4, 32, 0), P(4, 32, 36), P(0, 32, 36)], "#5f4128", True)
c.poly([P(28, 32, 0), P(32, 32, 0), P(32, 32, 36), P(28, 32, 36)], "#5f4128", True)
c.poly([P(16, 32, 0), P(18, 32, 0), P(18, 32, 32), P(16, 32, 32)], "#5f4128", True)
c.poly([P(0, 32, 36), P(32, 32, 36), P(32, 32, 32), P(0, 32, 32)], "#5f4128", True)

# --- plank door ----------------------------------------------------
c.poly([P(3, 32, 0), P(17, 32, 0), P(17, 32, 19), P(3, 32, 19)], "#5f4128", True)
c.poly([P(4, 32, 0), P(16, 32, 0), P(16, 32, 18), P(4, 32, 18)], "#8a5f38", True)
c.poly([P(4, 32, 0), P(6, 32, 0), P(6, 32, 18), P(4, 32, 18)], "#a9763f", True)
for uu in (9, 12, 15):
    linep(P(uu, 32, 1), P(uu, 32, 17), "#6b4527")
x, y = P(14, 32, 9)
c.set(x, y, "#3d2a1a")
c.set(x, y - 1, "#3d2a1a")
c.poly([P(3, 32, 0), P(17, 32, 0), P(17, 32, 19), P(3, 32, 19)], OUT, False)

# --- hanging wooden sign with a painted flame ----------------------
linep(P(20, 32, 32), P(20, 32, 29), "#3d2a1a")
linep(P(26, 32, 32), P(26, 32, 29), "#3d2a1a")
sign = [P(18, 32, 29), P(28, 32, 29), P(28, 32, 20), P(18, 32, 20)]
c.poly(sign, "#9a7042", True)
linep(P(18, 32, 29), P(28, 32, 29), "#b98a52")
linep(P(18, 32, 20), P(28, 32, 20), "#6b4a2e")
c.poly([(55, 74), (58, 78), (57, 82), (55, 84), (53, 82), (52, 78)], "#f07a1e", True)
c.poly([(55, 78), (57, 81), (55, 83), (53, 81)], "#ffe08a", True)
c.poly([(55, 74), (58, 78), (57, 82), (55, 84), (53, 82), (52, 78)], OUT, False)
c.poly(sign, OUT, False)
c.poly(wall, OUT, False)

# ------------------------------------------------------------------
# roof - one visible slope, red tile courses, 45-degree rakes
# ------------------------------------------------------------------
roof = [P(-4, 0, 56), P(36, 0, 56), P(36, 36, 38), P(-4, 36, 38)]
band_cols = ["#cd4f33", "#c74a30", "#c2462e", "#bc402c", "#b53c2a", "#a83326"]
for k in range(6):
    v0 = 6 * k
    h0 = 56 - 3 * k
    c.poly([P(-4, v0, h0), P(36, v0, h0), P(36, v0 + 6, h0 - 3), P(-4, v0 + 6, h0 - 3)],
           band_cols[k], True)
for k in range(1, 6):
    linep(P(-4, 6 * k, 56 - 3 * k), P(36, 6 * k, 56 - 3 * k), "#7e241a")
for k in range(6):                                                      # tile joints
    v0 = 6 * k
    h0 = 56 - 3 * k
    for j in range(5):
        uu = 1 + 8 * j + (((k * 3) % 5) - 2)
        linep(P(uu, v0, h0), P(uu, v0 + 3, h0 - 1.5), "#7e241a")
c.poly([P(-4, -2, 58), P(36, -2, 58), P(36, 2, 56), P(-4, 2, 56)], "#e07a52", True)
linep(P(-4, -2, 58), P(36, -2, 58), "#f0926a")
c.poly([P(-4, 36, 38), P(36, 36, 38), P(36, 36, 35), P(-4, 36, 35)], "#6e2418", True)
c.poly(roof, OUT, False)

# ------------------------------------------------------------------
# small chimney straddling the ridge
# ------------------------------------------------------------------
c.poly([P(14, 5, 53.5), P(24, 5, 53.5), P(24, 5, 66), P(14, 5, 66)], "#9c9ca6", True)
c.poly([P(24, -5, 58.5), P(24, 5, 53.5), P(24, 5, 66), P(24, -5, 66)], "#6f6f78", True)
for hh in (58, 62):
    linep(P(14, 5, hh), P(24, 5, hh), "#82828c")
    linep(P(24, 5, hh), P(24, -3, hh), "#5c5c66")
c.poly([P(12, 6, 64), P(26, 6, 64), P(26, 6, 69), P(12, 6, 69)], "#9c9ca6", True)
c.poly([P(26, -6, 64), P(26, 6, 64), P(26, 6, 69), P(26, -6, 69)], "#6f6f78", True)
c.poly([P(12, -6, 69), P(26, -6, 69), P(26, 6, 69), P(12, 6, 69)], "#b6b6c0", True)
c.poly([P(16, -2, 69), P(22, -2, 69), P(22, 2, 69), P(16, 2, 69)], "#2a2428", True)
c.poly([P(12, -6, 69), P(26, -6, 69), P(26, 6, 69), P(12, 6, 69)], OUT, False)
c.poly([P(12, 6, 64), P(26, 6, 64), P(26, 6, 69), P(12, 6, 69)], OUT, False)
c.poly([P(26, -6, 64), P(26, 6, 64), P(26, 6, 69), P(26, -6, 69)], OUT, False)
c.poly([P(14, 5, 53.5), P(24, 5, 53.5), P(24, 5, 66), P(14, 5, 66)], OUT, False)
c.poly([P(24, -5, 58.5), P(24, 5, 53.5), P(24, 5, 66), P(24, -5, 66)], OUT, False)

# ------------------------------------------------------------------
# smoke
# ------------------------------------------------------------------
c.circle(82, 10, 1, "#c9ced6", True)
c.circle(80, 6, 2, "#c9ced6", True)
c.circle(77, 2, 2, "#c9ced6", True)
for (sx, sy) in [(81, 9), (79, 5), (76, 1)]:
    c.set(sx, sy, "#e8ecf0")


# ------------------------------------------------------------------
# stacked barrels
# ------------------------------------------------------------------
def barrel(cx, base_y, w, h):
    rx = w // 2
    ry = max(2, w // 4)
    top = base_y - h
    y1 = top + ry + 2
    y2 = base_y - 3
    pts = [(cx - rx, top + ry), (cx - rx - 1, y1), (cx - rx - 1, y2), (cx - rx, base_y),
           (cx, base_y + 1), (cx + rx, base_y), (cx + rx + 1, y2), (cx + rx + 1, y1),
           (cx + rx, top + ry)]
    c.poly(pts, "#8a5a33", True)
    c.poly([(cx - rx, top + ry), (cx - rx - 1, y1), (cx - rx - 1, y2), (cx - rx, base_y),
            (cx - rx + 2, base_y + 1), (cx - rx + 2, top + ry)], "#a9763f", True)
    c.poly([(cx + rx, top + ry), (cx + rx + 1, y1), (cx + rx + 1, y2), (cx + rx, base_y),
            (cx + rx - 2, base_y + 1), (cx + rx - 2, top + ry)], "#5f3c20", True)
    for sx in (cx - 3, cx, cx + 3):
        c.line(sx, top + ry + 1, sx, base_y - 1, "#7a4e2b")
    for hy in (y1, y2):
        for dx in range(-rx - 1, rx + 2):
            dip = 1 if abs(dx) <= rx - 2 else 0
            c.set(cx + dx, hy + dip, "#3d3d46")
            c.set(cx + dx, hy + dip + 1, "#2c2c33")
    c.ellipse(cx, top + ry, rx, ry, "#5f3c20", True)
    c.ellipse(cx, top + ry, rx - 1, max(1, ry - 1), "#a9763f", True)
    c.ellipse(cx, top + ry, max(1, rx - 4), max(1, ry - 2), "#8a5a33", True)
    c.set(cx + 1, top + ry, "#4a2e18")
    c.poly(pts, OUT, False)
    c.ellipse(cx, top + ry, rx, ry, OUT, False)


c.ellipse(103, 94, 8, 2, "#2c4a24", True)
c.ellipse(114, 90, 7, 2, "#2c4a24", True)
barrel(101, 93, 13, 15)          # stack bottom
barrel(101, 78, 11, 13)          # stack top
barrel(112, 89, 12, 14)          # beside the stack
for dx in range(-6, 7):          # rim of the lower lid, peeking out
    dy = int(round(3 * math.sqrt(max(0.0, 1 - (dx / 6.0) ** 2))))
    c.set(101 + dx, 81 + dy, "#4a2e18")
# warm furnace light on the barrels' left sides
for (x, y) in [(95, 84), (95, 87), (96, 85), (106, 82), (106, 85)]:
    c.set(x, y, "#e8934a")

# a little more smoke drifting from the chimney
c.circle(74, 6, 1, "#c9ced6", True)
c.set(73, 5, "#e8ecf0")

# a few sunlit grass highlights
for (gx, gy) in [(20, 78), (26, 84), (90, 74), (100, 80), (44, 96), (56, 100), (14, 96)]:
    if c.get(gx, gy) is not None:
        c.set(gx, gy, "#59994a")

print(c.stats_text())
finish(c)
