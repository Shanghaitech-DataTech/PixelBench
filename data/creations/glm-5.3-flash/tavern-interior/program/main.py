# Cozy tavern interior - 64x64 pixel art
try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 64

# ---------------- palette ----------------
OUT = "#140b05"
CEIL, BEAM, BEAM_L = "#1c1109", "#2e1c0e", "#3d2714"
WALL, WALLD, WALLL, PLANK = "#3a2411", "#291808", "#4e3117", "#26160a"
SHELF, SHELFT, SHELFD = "#5e3c1d", "#7c5427", "#3a2410"
WOOD_L, WOOD_M, WOOD_D, WOOD_DD = "#9a6631", "#7a4e24", "#5c3919", "#42270f"
BAR_L, BAR_M, BAR_D = "#8a5c2c", "#6b4520", "#492c12"
HOOP, HOOP_L = "#434343", "#6e6e6e"
ST_T, ST_M, ST_D = "#86592c", "#5e3a1a", "#37200e"
GL_L, GL_M = "#d9e9ed", "#a7c4cd"
WINE, BEER, FOAM, WAX = "#7c2334", "#d8912f", "#f2e6c4", "#e9dcc0"
GRN, GRN_L = "#2f5c33", "#63a052"
BRN, BRN_L = "#6e3f1c", "#9c6a33"
BLU, BLU_L = "#305070", "#6b93b8"
AMB, AMB_L = "#8f4d1e", "#c88336"
RED, RED_L = "#7e2a26", "#b05a3c"
CORK = "#c9a06a"
LMET, LRIM, BULB, BULB_H = "#251711", "#8a5c2a", "#ffdf94", "#fff6d8"
FLOOR, FLOOR_D = "#201106", "#150b04"

# opaque atmosphere colours (no alpha -> no blending explosion)
HALO1 = "#5e3c1d"   # dim warm ring (same value as SHELF: reused)
HALO2 = "#7a5226"   # mid warm ring
HALO3 = "#b98a3e"   # hot inner ring
SMK1 = "#5a5344"    # smoke, lit
SMK2 = "#443e33"    # smoke, dim
MOTE = BULB         # dust motes reuse the bulb yellow

# ---------------- base layer ----------------
base = new_canvas(W, H, background=OUT, name="base")

# ---- ceiling ----
base.rect(0, 0, 64, 7, CEIL)
base.rect(0, 5, 64, 2, BEAM)
base.rect(0, 5, 64, 1, BEAM_L)
for jx in (5, 21, 39, 55):
    base.rect(jx, 0, 3, 5, BEAM)
    base.rect(jx, 0, 1, 5, BEAM_L)

# ---- back wall ----
base.rect(0, 7, 64, 34, WALL)


def wall_light(c, cx):
    c.rect(cx - 5, 9, 10, 14, WALLL)
    c.dither(cx - 8, 9, 3, 14, [WALLL, WALL], pattern="bayer4")
    c.dither(cx + 5, 9, 3, 14, [WALLL, WALL], pattern="bayer4")
    c.dither(cx - 8, 7, 16, 2, [WALLL, WALL], pattern="bayer4")
    c.dither(cx - 8, 23, 16, 2, [WALLL, WALL], pattern="bayer4")


wall_light(base, 21)
wall_light(base, 45)
for x in range(4, 64, 9):
    base.line(x, 9, x, 39, PLANK)
base.rect(0, 7, 64, 2, WALLD)

# ---- warm halos around the lamps (drawn before furniture) ----


def draw_glow(c, cx, cy):
    c.circle(cx, cy, 6, HALO1)
    c.circle(cx, cy, 4, HALO2)
    c.circle(cx, cy, 2, HALO3)


draw_glow(base, 21, 14)
draw_glow(base, 45, 14)

# ---- barrels (left, behind bar) ----


def draw_barrel(c, x, y, w, h, head=True):
    half = (h - 1) / 2.0
    ins = [int(round(2.3 * ((abs(i - half) / half) ** 2))) for i in range(h)]
    for i in range(h):
        k = ins[i]
        c.rect(x + k - 1, y + i, w - 2 * k + 2, 1, OUT)
    for i in range(h):
        k = ins[i]
        bw = w - 2 * k
        c.rect(x + k, y + i, bw, 1, BAR_M)
        c.set(x + k, y + i, BAR_L)
        c.set(x + k + 1, y + i, BAR_L)
        c.set(x + k + bw - 1, y + i, BAR_D)
        for dx in (bw // 3, (2 * bw) // 3):
            c.set(x + k + dx, y + i, BAR_D)
    for hy in (y + 3, y + h - 6):
        for i in (hy, hy + 1):
            if y <= i < y + h:
                k = ins[i - y]
                bw = w - 2 * k
                c.rect(x + k, i, bw, 1, HOOP)
                c.set(x + k + 1, i, HOOP_L)
                c.set(x + k + 2, i, HOOP_L)
    if head:
        ccx = x + w // 2
        c.ellipse(ccx, y + 1, w // 2 - 1, 2, OUT)
        c.ellipse(ccx, y + 1, w // 2 - 2, 1, BAR_L)


draw_barrel(base, 1, 28, 15, 19)
draw_barrel(base, 2, 11, 13, 17)

# ---- shelves ----
base.rect(16, 25, 48, 2, SHELF)
base.rect(16, 25, 48, 1, SHELFT)
base.rect(16, 27, 48, 1, SHELFD)
base.rect(16, 25, 1, 2, SHELFD)
for bx in (20, 30):
    base.rect(bx, 28, 2, 2, SHELFD)

base.rect(38, 33, 26, 2, SHELF)
base.rect(38, 33, 26, 1, SHELFT)
base.rect(38, 35, 26, 1, SHELFD)
base.rect(38, 33, 1, 2, SHELFD)

# ---- bottles ----


def draw_bottle(c, cx, ybot, bw, bh, glass, light, neck=1, nh=3, cork=None):
    body_h = bh - nh
    bx = cx - bw // 2
    by = ybot - body_h + 1
    nx = cx - neck // 2
    c.rect(bx - 1, by - 1, bw + 2, body_h + 2, OUT)
    c.rect(nx - 1, by - nh - 1, neck + 2, nh + 1, OUT)
    c.rect(bx, by, bw, body_h, glass)
    c.rect(nx, by - nh, neck, nh, glass)
    if cork:
        c.rect(nx, by - nh - 1, neck, 1, cork)
    c.set(bx + 1, by + 1, light)
    c.set(bx + 1, by + 2, light)
    if body_h > 4:
        c.set(bx + 1, by + 3, light)
    if neck >= 2:
        c.set(nx, by - nh, light)


def draw_up_glass(c, cx, ybot, w, h):
    x0 = cx - w // 2
    c.rect(x0 - 1, ybot - h, w + 2, h + 1, OUT)
    c.rect(x0, ybot - h + 1, w, h - 1, GL_M)
    c.rect(x0, ybot - h + 1, w, 1, GL_L)


upper = [
    (19, 3, 10, GRN, GRN_L, 1, 3, CORK),
    (23, 4, 8, BRN, BRN_L, 2, 2, None),
    (27, 3, 11, BLU, BLU_L, 1, 3, CORK),
    (31, 4, 9, AMB, AMB_L, 2, 2, None),
    (36, 3, 12, GRN, GRN_L, 1, 4, CORK),
    (40, 4, 8, RED, RED_L, 2, 2, None),
    (44, 3, 10, BLU, BLU_L, 1, 3, CORK),
    (48, 4, 9, BRN, BRN_L, 2, 2, None),
    (53, 3, 11, GRN, GRN_L, 1, 3, CORK),
    (57, 4, 8, AMB, AMB_L, 2, 2, None),
    (61, 3, 9, RED, RED_L, 1, 3, CORK),
]
for (cx, bw, bh, g, l, nk, nh, ck) in upper:
    draw_bottle(base, cx, 24, bw, bh, g, l, nk, nh, ck)

draw_bottle(base, 42, 32, 3, 5, GRN, GRN_L, 1, 2, None)
draw_bottle(base, 46, 32, 4, 5, AMB, AMB_L, 2, 2, None)
draw_up_glass(base, 51, 32, 4, 4)
draw_bottle(base, 56, 32, 3, 5, BLU, BLU_L, 1, 2, None)
draw_up_glass(base, 60, 32, 4, 4)

# ---- bar counter ----
base.rect(0, 40, 64, 4, WOOD_M)
base.rect(0, 40, 64, 1, WOOD_L)
base.rect(0, 43, 64, 1, WOOD_D)
base.dither(15, 41, 13, 2, [WOOD_L, WOOD_M], pattern="checker")
base.dither(39, 41, 13, 2, [WOOD_L, WOOD_M], pattern="checker")
base.rect(0, 44, 64, 12, WOOD_D)
base.rect(0, 44, 64, 1, WOOD_DD)
for x in range(5, 64, 10):
    base.line(x, 46, x, 54, WOOD_DD)
base.rect(0, 55, 64, 1, WOOD_DD)
base.rect(0, 56, 64, 1, OUT)

# ---- floor ----
base.rect(0, 57, 64, 7, FLOOR)
base.line(0, 59, 63, 59, FLOOR_D)
base.line(0, 62, 63, 62, FLOOR_D)
for fx in (14, 34, 52):
    base.line(fx, 57, fx, 58, FLOOR_D)
    base.line(fx + 7, 60, fx + 7, 61, FLOOR_D)

# ---- items on the counter ----
# beer mug
base.rect(16, 33, 7, 8, OUT)
base.rect(17, 34, 5, 6, GL_M)
base.rect(17, 34, 5, 2, FOAM)
base.rect(17, 36, 5, 4, BEER)
base.set(17, 36, GL_L)
base.set(17, 37, GL_L)
base.set(19, 37, FOAM)
for (hx, hy) in ((23, 35), (24, 36), (24, 37), (23, 38)):
    base.set(hx, hy, OUT)
# wine glass
base.rect(25, 33, 5, 5, OUT)
base.set(27, 38, OUT)
base.set(27, 39, OUT)
base.rect(25, 40, 5, 1, OUT)
base.rect(26, 34, 3, 1, GL_L)
base.rect(26, 35, 3, 2, WINE)
# candle
base.circle(33, 34, 3, HALO2)
base.circle(33, 34, 1, HALO3)
base.rect(31, 36, 5, 5, OUT)
base.rect(32, 37, 3, 4, WAX)
base.set(33, 35, OUT)
base.set(33, 34, BULB)
base.set(33, 33, BULB_H)
# tumbler
base.rect(37, 35, 5, 6, OUT)
base.rect(38, 36, 3, 2, GL_M)
base.rect(38, 38, 3, 2, AMB)
base.set(38, 36, GL_L)

# ---- hanging lamps ----


def draw_lamp(c, cx):
    c.rect(cx, 6, 1, 3, OUT)
    for i, wd in enumerate((3, 5, 7, 9)):
        y = 9 + i
        c.rect(cx - wd // 2 - 1, y, wd + 2, 1, OUT)
        c.rect(cx - wd // 2, y, wd, 1, LMET)
    c.rect(cx - 4, 12, 9, 1, LRIM)
    c.rect(cx - 1, 13, 2, 2, BULB)
    c.set(cx - 1, 13, BULB_H)


draw_lamp(base, 21)
draw_lamp(base, 45)

# ---- bar stools ----


def draw_stool(c, cx):
    c.line(cx - 4, 52, cx - 6, 62, OUT)
    c.line(cx - 3, 52, cx - 5, 62, ST_M)
    c.line(cx + 4, 52, cx + 6, 62, OUT)
    c.line(cx + 3, 52, cx + 5, 62, ST_M)
    c.line(cx - 5, 58, cx + 5, 58, ST_D)
    c.line(cx - 3, 47, cx + 3, 47, OUT)
    c.line(cx - 4, 48, cx + 4, 48, OUT)
    c.line(cx - 5, 49, cx + 5, 49, OUT)
    c.line(cx - 5, 50, cx + 5, 50, OUT)
    c.line(cx - 4, 51, cx + 4, 51, OUT)
    c.rect(cx - 2, 47, 5, 1, ST_T)
    c.rect(cx - 3, 48, 7, 1, ST_T)
    c.rect(cx - 4, 49, 9, 1, ST_T)
    c.rect(cx - 4, 50, 9, 1, ST_M)


draw_stool(base, 10)
draw_stool(base, 32)
draw_stool(base, 53)

# ---------------- atmosphere layer (all opaque) ----------------
atmo = new_canvas(W, H, name="atmo")


def bres(x0, y0, x1, y1):
    pts = []
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        pts.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return pts


def wisp(c, pts, colour, gap=4):
    seq = []
    for i in range(len(pts) - 1):
        seg = bres(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1])
        seq.extend(seg[1:] if seq else seg)
    for k, (px, py) in enumerate(seq):
        if k % gap != gap - 1:
            c.set(px, py, colour)


curls = [
    [(6, 30), (8, 27), (6, 24), (9, 21), (7, 18), (9, 15), (8, 12)],
    [(30, 26), (32, 23), (30, 20), (33, 17), (31, 14), (33, 11), (32, 8)],
    [(56, 28), (58, 25), (56, 22), (59, 19), (57, 16)],
    [(2, 5), (10, 4), (18, 6), (26, 4), (34, 6), (42, 4), (50, 6), (58, 4), (62, 5)],
]
for pts in curls:
    wisp(atmo, [(x + 1, y) for (x, y) in pts], SMK2)
    wisp(atmo, pts, SMK1)

for (mx, my) in [(16, 20), (27, 18), (38, 22), (51, 19), (24, 31), (47, 29)]:
    atmo.set(mx, my, MOTE)


def corner(c, x0, y0, sx, sy, n=7):
    for i in range(n):
        for j in range(n - i):
            if (i + j) % 2 == 0:
                c.set(x0 + sx * i, y0 + sy * j, OUT)


corner(atmo, 0, 0, 1, 1)
corner(atmo, 63, 0, -1, 1)
corner(atmo, 0, 63, 1, -1)
corner(atmo, 63, 63, -1, -1)

# ---------------- composite ----------------
result = flatten([base, atmo], name="tavern")
print(result.stats_text())
print(result.matrix_text(region=(0, 4, 36, 24)))
finish(result)
