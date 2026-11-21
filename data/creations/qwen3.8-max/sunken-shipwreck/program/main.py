import math

W = H = 64

# ======================= helpers =======================
def bres(x0, y0, x1, y1):
    pts = []
    dx = abs(x1 - x0); dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        pts.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy; x0 += sx
        if e2 < dx:
            err += dx; y0 += sy
    return pts


def opaque_set(cv):
    w, h, data = cv.to_rgba()
    return {(x, y) for y in range(h) for x in range(w)
            if data[4 * (y * w + x) + 3] > 0}


class Clip:
    def __init__(self, cv):
        self.s = opaque_set(cv)

    def has(self, x, y):
        return (x, y) in self.s

    def px(self, cv, x, y, col):
        if (x, y) in self.s:
            cv.set(int(x), int(y), col)

    def line(self, cv, x0, y0, x1, y1, col):
        for (x, y) in bres(int(x0), int(y0), int(x1), int(y1)):
            self.px(cv, x, y, col)

    def rect(self, cv, x, y, w, h, col):
        for j in range(int(y), int(y + h)):
            for i in range(int(x), int(x + w)):
                self.px(cv, i, j, col)


def branch(cv, x, y, ang, ln, col, depth, spread=0.6, wd=1):
    x2 = x + math.cos(ang) * ln
    y2 = y + math.sin(ang) * ln
    pts = bres(int(round(x)), int(round(y)), int(round(x2)), int(round(y2)))
    for k, (px, py) in enumerate(pts):
        if wd >= 2 and k < len(pts) - 1:
            cv.set(px, py + 1, col)
        cv.set(px, py, col)
    if depth > 0:
        branch(cv, x2, y2, ang - spread, ln * 0.66, col, depth - 1, spread, wd - 1)
        branch(cv, x2, y2, ang + spread, ln * 0.66, col, depth - 1, spread, wd - 1)


def fish(cv, cx, cy, col, dark, lite, eye, size=2, right=True):
    d = 1 if right else -1
    ry = max(1, size - 1)
    cv.ellipse(cx, cy, size, ry, col)
    for xx in range(cx - size + 1, cx + size):
        cv.set(xx, cy - ry, lite)
        cv.set(xx, cy + ry, dark)
    tx = cx - d * (size + 1)
    cv.set(tx, cy, col)
    cv.set(tx - d, cy - 1, col)
    cv.set(tx - d, cy + 1, col)
    if size >= 2:
        cv.set(tx - d, cy, dark)
        cv.set(tx - 2 * d, cy - 2, col)
        cv.set(tx - 2 * d, cy + 2, col)
    cv.set(cx - d, cy - ry - 1, dark)
    cv.set(cx, cy + ry + 1, dark)
    cv.set(cx + d * size, cy - (1 if ry >= 1 else 0), eye)


# ======================= palette =======================
WATER = ['#5fb6e0', '#4ca8d8', '#3b98cd', '#2d87bf', '#2276ae',
         '#1a659b', '#135689', '#0e4776', '#0a3a64', '#072d51',
         '#05233f', '#041b31']
RAYC = '#bfe9fb'

SAND_HI = '#e3cd95'
SAND_LIT = '#d0b67e'
SAND_MID = '#b89c65'
SAND_SH = '#96794c'
SAND_DK = '#75593a'
SAND_WET = '#5d4a35'

WOOD_LT = '#a97f52'
WOOD_MD = '#87603c'
WOOD_DK = '#654427'
WOOD_XD = '#452c17'
WOOD_BLK = '#2a1a0d'
HOLE = '#150c05'

PATINA = '#6d9c85'
PATINA_D = '#48705e'
RUST = '#9d5c2e'
RUST_D = '#77411f'
IRON = '#3b4a52'
IRON_D = '#26333a'

CLOTH = '#bdb69e'
CLOTH_D = '#8b8571'

FISH_A = '#f7b23c'
FISH_B = '#ffd977'
FISH_C = '#d1762a'
FISH_D = '#8fe0ef'
FISH_E = '#3f9fb8'
EYE = '#1b1420'

CORAL_PK = '#e8617f'
CORAL_PKL = '#ff97ab'
CORAL_PKD = '#b23f5c'
CORAL_OR = '#e88a3c'
CORAL_PU = '#8f74c9'
CORAL_CR = '#f0d9a8'

WEED_1 = '#1f5c3c'
WEED_2 = '#2e7d51'
WEED_3 = '#41a468'
WEED_4 = '#63c489'

BUB_L = '#dff4ff'
BUB_M = '#9ed6ee'

# ======================= 1. water =======================
bg = new_canvas(W, H, name='water')
bands = [(0, 3, 0), (4, 7, 1), (8, 12, 2), (13, 17, 3), (18, 23, 4),
         (24, 29, 5), (30, 35, 6), (36, 42, 7), (43, 50, 8), (51, 57, 9),
         (58, 63, 10)]
for y0, y1, ci in bands:
    bg.rect(0, y0, W, y1 - y0 + 1, WATER[ci])
bg.rect(0, 62, W, 2, WATER[11])
for k in range(len(bands) - 1):
    ya = bands[k][1]; yb = bands[k + 1][0]
    ca = WATER[bands[k][2]]; cb = WATER[bands[k + 1][2]]
    for x in range(W):
        if (x + ya) % 4 == 0:
            bg.set(x, ya, cb)
        if x % 2 == 0:
            bg.set(x, ya + 1, cb)
        if (x + yb) % 4 != 0:
            bg.set(x, yb, ca)

# ======================= 2. light shafts (sparse shimmer) =======================
rays = new_canvas(W, H, name='rays')
for xt in (2, 14, 26, 40, 52):
    for y in range(0, 42):
        if (y + xt) % 2:
            continue
        x = xt + int(y * 0.3) + ((y // 2) % 3) - 1
        if 0 <= x < W:
            rays.set(x, y, RAYC)
        if y < 22 and (y + xt) % 4 == 0 and 0 <= x + 2 < W:
            rays.set(x + 2, y, RAYC)
for (cx, cy) in [(6, 1), (20, 2), (34, 1), (48, 2), (60, 1), (12, 0), (44, 0)]:
    rays.set(cx, cy, RAYC)
    rays.set(cx + 1, cy, RAYC)

# ======================= 3. distant seabed =======================
far = new_canvas(W, H, name='far')
far.path('M -2 50 Q 8 45 16 47 Q 26 49 34 44 Q 44 39 54 43 Q 60 45 63 42 '
         'L 63 63 L -2 63 Z', '#0a3f5c')
far.path('M -2 54 Q 10 50 20 52 Q 32 54 42 50 Q 54 46 63 50 L 63 63 L -2 63 Z',
         '#0d4a5e')

# ======================= 4. sand (behind wreck) =======================
sand = new_canvas(W, H, name='sand')
sand.path('M -2 52 Q 6 48 14 50 Q 22 52 30 49 Q 40 45 50 48 Q 58 50 63 47 '
          'L 63 63 L -2 63 Z', SAND_MID)
sc = Clip(sand)
sc.rect(sand, 0, 56, W, 8, SAND_SH)
sc.rect(sand, 0, 61, W, 3, SAND_DK)
sc.rect(sand, 0, 63, W, 1, SAND_WET)
sand.rect(0, 63, W, 1, SAND_WET)
sc.line(sand, 0, 55, 63, 54, SAND_SH)
sc.line(sand, 0, 60, 63, 59, SAND_DK)
for (x0, x1, y) in [(2, 12, 50), (14, 22, 51), (30, 40, 47), (42, 52, 47),
                    (54, 62, 48), (6, 16, 53), (24, 34, 51), (44, 58, 50)]:
    sc.line(sand, x0, y, x1, y, SAND_LIT)
for (x0, x1, y) in [(4, 10, 49), (32, 38, 46), (46, 54, 46)]:
    sc.line(sand, x0, y, x1, y, SAND_HI)
for (x, y) in [(5, 57), (17, 56), (31, 58), (44, 60), (58, 61), (27, 55),
               (49, 54), (13, 62), (35, 62), (55, 63)]:
    sc.px(sand, x, y, SAND_DK); sc.px(sand, x + 1, y, SAND_DK)
    sc.px(sand, x, y + 1, SAND_SH); sc.px(sand, x, y - 1, SAND_LIT)

# ======================= 5. hull =======================
hull = new_canvas(W, H, name='hull')
hull.path('M 3 31 L 5 25 L 8 26 L 11 30 Q 22 33 33 32 Q 43 31 49 28 '
          'L 52 23 L 56 21 L 60 25 L 61 34 L 59 44 Q 50 52 34 55 '
          'Q 18 53 8 48 L 4 40 Z', WOOD_MD)
hc = Clip(hull)
rowbands = [(21, 27, WOOD_MD, WOOD_DK), (28, 31, WOOD_LT, WOOD_MD),
            (32, 35, WOOD_MD, WOOD_LT), (36, 39, WOOD_MD, WOOD_DK),
            (40, 43, WOOD_DK, WOOD_MD), (44, 47, WOOD_XD, WOOD_DK)]
ribx = [8, 15, 23, 31, 39, 47, 54]
for y0, y1, col, alt in rowbands:
    hc.rect(hull, 0, y0, W, y1 - y0 + 1, col)
    for ci in range(len(ribx) - 1):
        if (ci + y0) % 2 == 0:
            hc.rect(hull, ribx[ci] + 2, y0, ribx[ci + 1] - ribx[ci] - 2,
                    y1 - y0 + 1, alt)
for y in (27, 31, 35, 39, 43, 47):
    hc.line(hull, 0, y, 63, y, WOOD_XD)
for y in (29, 33, 37):
    hc.line(hull, 0, y, 63, y, WOOD_LT if y < 36 else WOOD_MD)
for rx in ribx:
    hc.line(hull, rx, 20, rx - 1, 60, WOOD_XD)
    hc.line(hull, rx + 1, 20, rx, 60, WOOD_DK)
# stem & stern posts
hc.line(hull, 5, 25, 7, 50, WOOD_XD)
hc.line(hull, 60, 25, 58, 48, WOOD_XD)
# lower hull in shadow
for y in range(48, 64):
    for x in range(W):
        if hc.has(x, y):
            hc.px(hull, x, y, WOOD_BLK if y > 52 else WOOD_XD)
# wale strake above the gunports
hc.line(hull, 0, 32, 63, 32, WOOD_LT)
hc.line(hull, 0, 33, 63, 33, WOOD_MD)
# gunports
for px in (12, 20, 28, 36, 44):
    py = 34
    hc.rect(hull, px, py, 4, 4, HOLE)
    hc.line(hull, px, py, px + 3, py, IRON)
    hc.line(hull, px, py + 3, px + 3, py + 3, IRON_D)
    hc.line(hull, px, py, px, py + 3, IRON)
    hc.line(hull, px + 3, py, px + 3, py + 3, IRON_D)
    hc.px(hull, px + 1, py + 1, IRON_D)
# breach in the side
hull.path('M 44 38 L 49 35 L 54 38 L 56 44 L 52 50 L 46 48 L 43 43 Z', HOLE)
hull.path('M 46 40 L 50 38 L 53 42 L 51 47 L 46 46 Z', WOOD_BLK)
for (bx, by) in [(43, 37), (48, 34), (54, 37), (57, 43), (53, 50), (45, 49),
                 (41, 42)]:
    hull.set(bx, by, WOOD_LT); hull.set(bx, by + 1, WOOD_DK)
for (sx, sy, ex, ey) in [(42, 36, 40, 33), (49, 33, 50, 30), (57, 42, 60, 40),
                         (54, 51, 56, 54), (43, 50, 41, 53)]:
    hull.line(sx, sy, ex, ey, WOOD_DK); hull.set(ex, ey, WOOD_LT)
# corrosion
rust_cols = [RUST, RUST_D, PATINA, PATINA_D]
for i, rx in enumerate([9, 16, 24, 33, 41, 50, 56]):
    col = rust_cols[i % 4]
    yt = 32 + (i % 3)
    hc.line(hull, rx, yt, rx + (1 if i % 2 else -1), 50, col)
    hc.line(hull, rx + 1, yt + 2, rx + 2, 48, RUST_D)
for (cx, cy, cr, col) in [(13, 42, 2, PATINA_D), (25, 39, 3, PATINA),
                          (35, 45, 2, PATINA_D), (19, 47, 2, PATINA),
                          (41, 36, 2, PATINA), (10, 37, 1, PATINA_D),
                          (30, 50, 2, PATINA_D), (52, 32, 2, PATINA_D)]:
    hc.rect(hull, cx - cr, cy - 1, cr * 2 + 1, 3, col)
    hc.px(hull, cx - cr, cy - 2, col); hc.px(hull, cx + cr, cy - 2, col)
for x in range(6, 58, 3):
    hc.px(hull, x, 31, IRON); hc.px(hull, x + 1, 31, IRON_D)
# broken sheer: gaps knocked out of the top edge
for (nx, ny, nw, nh) in [(14, 30, 5, 4), (25, 30, 4, 4), (40, 29, 4, 4)]:
    hull.clear(nx, ny, nw, nh)
for (sx, sy) in [(13, 30), (19, 31), (24, 30), (29, 31), (39, 29), (44, 30),
                 (6, 26), (10, 28), (22, 31), (36, 30), (47, 26), (51, 24),
                 (55, 22), (58, 24)]:
    hull.set(sx, sy, WOOD_LT); hull.set(sx, sy + 1, WOOD_DK)

# ======================= 6. superstructure =======================
sup = new_canvas(W, H, name='super')
sup.path('M 46 28 L 48 20 L 52 17 L 58 18 L 61 23 L 60 30 L 52 31 Z', WOOD_DK)
sup.path('M 48 21 L 52 18 L 57 19 L 59 23 L 58 28 L 51 29 L 48 26 Z', WOOD_MD)
spc = Clip(sup)
spc.line(sup, 46, 25, 62, 25, WOOD_XD)
spc.line(sup, 46, 21, 62, 21, WOOD_XD)
spc.line(sup, 48, 18, 60, 18, WOOD_LT)
spc.line(sup, 46, 30, 62, 30, WOOD_BLK)
for wx in (51, 55):
    spc.rect(sup, wx, 22, 2, 2, HOLE)
    spc.px(sup, wx, 21, PATINA_D)
sup.rect(58, 12, 2, 3, IRON_D)
sup.set(59, 13, CLOTH)
sup.set(58, 11, IRON); sup.set(59, 11, IRON)
# forecastle
sup.path('M 7 33 L 9 27 L 14 25 L 18 27 L 19 32 L 12 34 Z', WOOD_DK)
sup.path('M 9 28 L 14 26 L 17 28 L 17 31 L 10 32 Z', WOOD_MD)
spc2 = Clip(sup)
spc2.line(sup, 7, 30, 20, 30, WOOD_XD)
spc2.line(sup, 9, 26, 18, 26, WOOD_LT)
# main mast, snapped and leaning
for (mx, my) in bres(30, 32, 40, 12):
    sup.set(mx, my, WOOD_MD); sup.set(mx + 1, my, WOOD_DK)
    sup.set(mx - 1, my, WOOD_LT)
for (sx, sy, ex, ey) in [(40, 12, 42, 9), (39, 13, 37, 10), (41, 14, 44, 12)]:
    sup.line(sx, sy, ex, ey, WOOD_DK)
sup.set(42, 9, WOOD_LT); sup.set(37, 10, WOOD_LT)
# yard + torn sail
sup.line(33, 20, 45, 17, WOOD_XD)
sup.line(33, 19, 45, 16, WOOD_DK)
sup.path('M 34 20 L 44 18 L 43 25 L 41 23 L 39 27 L 37 24 L 35 26 Z', CLOTH_D)
sup.path('M 35 20 L 43 19 L 42 23 L 40 22 L 38 25 L 36 23 Z', CLOTH)
# fore mast stub
for (mx, my) in bres(14, 28, 10, 18):
    sup.set(mx, my, WOOD_MD); sup.set(mx - 1, my, WOOD_DK)
sup.set(9, 18, WOOD_LT); sup.set(11, 18, WOOD_LT)
# bowsprit
for (bx, by) in bres(6, 34, 0, 28):
    sup.set(bx, by, WOOD_DK); sup.set(bx, by + 1, WOOD_XD)
# rigging
for (x0, y0, x1, y1) in [(40, 13, 56, 22), (40, 13, 22, 30), (10, 19, 4, 32)]:
    sup.line(x0, y0, x1, y1, IRON_D)

# ======================= 7. sand drifts burying the hull =======================
drift = new_canvas(W, H, name='drift')
drift.path('M -2 50 Q 6 45 14 48 Q 22 51 30 48 Q 40 44 50 48 Q 58 51 63 47 '
           'L 63 63 L -2 63 Z', SAND_MID)
dc = Clip(drift)
dc.rect(drift, 0, 56, W, 8, SAND_SH)
dc.rect(drift, 0, 61, W, 3, SAND_DK)
dc.rect(drift, 0, 63, W, 1, SAND_WET)
drift.rect(0, 63, W, 1, SAND_WET)
dc.line(drift, 0, 55, 63, 54, SAND_SH)
dc.line(drift, 0, 60, 63, 59, SAND_DK)
for (x0, x1, y) in [(1, 11, 47), (15, 23, 50), (31, 39, 46), (43, 51, 49),
                    (55, 63, 50), (5, 13, 52), (25, 35, 53), (45, 58, 53)]:
    dc.line(drift, x0, y, x1, y, SAND_LIT)
for (x0, x1, y) in [(3, 9, 46), (33, 38, 45), (47, 53, 48)]:
    dc.line(drift, x0, y, x1, y, SAND_HI)
drift.path('M 1 48 Q 6 43 11 46 Q 15 49 19 47 L 19 56 L 1 56 Z', SAND_MID)
drift.path('M 50 49 Q 55 44 59 47 Q 62 49 63 47 L 63 57 L 50 57 Z', SAND_MID)
dc2 = Clip(drift)
dc2.line(drift, 2, 46, 18, 46, SAND_LIT)
dc2.line(drift, 51, 47, 62, 46, SAND_LIT)
dc2.px(drift, 5, 44, SAND_HI); dc2.px(drift, 55, 45, SAND_HI)
for (x, y) in [(8, 58), (22, 62), (34, 57), (46, 61), (56, 58), (14, 55),
               (28, 59), (40, 62), (50, 55), (60, 62), (4, 62), (30, 62)]:
    dc2.px(drift, x, y, SAND_DK); dc2.px(drift, x + 1, y, SAND_SH)
    dc2.px(drift, x, y - 1, SAND_LIT)
# ripple arcs on the drifts
for (x0, x1, y) in [(6, 14, 57), (20, 30, 59), (36, 46, 57), (48, 58, 60),
                    (10, 20, 62), (40, 52, 62), (2, 8, 53), (54, 62, 54)]:
    dc2.line(drift, x0, y, x1, y, SAND_SH)
    dc2.line(drift, x0 + 1, y - 1, x1 - 1, y - 1, SAND_LIT)

# ======================= 8. seaweed =======================
weed = new_canvas(W, H, name='weed')


def blade(cv, x, ybase, hgt, sway, cols, w=1):
    for k in range(hgt):
        y = ybase - k
        t = k / float(max(1, hgt - 1))
        xoff = int(round(sway * math.sin(t * 3.4 + x * 0.4) * (t ** 1.2) * 3))
        ci = min(len(cols) - 1, int(t * len(cols)))
        for j in range(w):
            cv.set(x + xoff + j, y, cols[ci])


CA = [WEED_1, WEED_2, WEED_3, WEED_4]
CB = [WEED_1, WEED_2, WEED_3]
CC = ['#17452f', WEED_1, WEED_2, WEED_3]
for (x, yb, h, sw, cols, w) in [
        (1, 62, 24, 1.1, CA, 2), (5, 63, 18, -0.9, CB, 2),
        (9, 61, 26, 1.3, CA, 2), (13, 63, 15, -1.0, CC, 1),
        (20, 62, 15, 0.6, CB, 2), (26, 63, 11, -0.8, CC, 2),
        (36, 62, 12, 0.7, CB, 2),
        (50, 62, 20, 1.2, CA, 2), (54, 63, 14, -1.1, CB, 2),
        (58, 61, 25, 1.0, CA, 2), (62, 63, 17, -0.9, CC, 2),
        (17, 61, 12, 0.9, CB, 2), (41, 61, 12, -0.9, CB, 2),
        (47, 62, 9, 1.1, CC, 1), (31, 62, 9, -0.7, CC, 2),
        (60, 62, 11, -0.8, CB, 2)]:
    blade(weed, x, yb, h, sw, cols, w)

# ======================= 9. coral =======================
coral = new_canvas(W, H, name='coral')
coral.ellipse(8, 57, 4, 3, CORAL_OR)
cc = Clip(coral)
cc.line(coral, 5, 56, 11, 56, CORAL_CR)
cc.line(coral, 5, 58, 11, 58, RUST_D)
cc.px(coral, 6, 55, CORAL_CR); cc.px(coral, 10, 55, CORAL_CR)
for (tx, th, col, col2) in [(15, 7, CORAL_PU, '#6f55a8'), (18, 5, CORAL_PU, '#6f55a8'),
                            (46, 6, CORAL_PKD, '#9c4169'), (60, 7, CORAL_PU, '#6f55a8')]:
    coral.rect(tx, 60 - th, 2, th, col)
    coral.rect(tx, 60 - th, 1, th, col2)
    coral.set(tx, 59 - th, CORAL_CR); coral.set(tx + 1, 59 - th, col)
branch(coral, 56, 60, -1.55, 5, CORAL_PK, 2, 0.6, 2)
branch(coral, 54, 60, -1.9, 4, CORAL_PKD, 2, 0.6, 1)
branch(coral, 61, 60, -1.2, 4, CORAL_PK, 1, 0.6, 1)
cc2 = Clip(coral)
cc2.px(coral, 55, 52, CORAL_PKL); cc2.px(coral, 58, 51, CORAL_PKL)
cc2.px(coral, 52, 55, CORAL_PKL); cc2.px(coral, 61, 55, CORAL_PKL)
coral.ellipse(30, 60, 4, 2, CORAL_PKD)
cc3 = Clip(coral)
cc3.line(coral, 27, 59, 33, 59, CORAL_PK)
cc3.px(coral, 28, 58, CORAL_PKL); cc3.px(coral, 31, 58, CORAL_PKL)
for (ax, ay) in [(24, 60), (36, 60), (43, 61), (13, 61), (40, 58)]:
    coral.set(ax, ay, CORAL_CR); coral.set(ax + 1, ay - 1, CORAL_PKL)

# ======================= 10. fish =======================
fishes = new_canvas(W, H, name='fish')
school = [
    (8, 9, FISH_A, FISH_C, FISH_B, 2, True),
    (15, 7, FISH_B, FISH_C, FISH_B, 2, True),
    (22, 10, FISH_A, FISH_C, FISH_B, 2, True),
    (29, 7, FISH_B, FISH_C, FISH_B, 2, True),
    (36, 9, FISH_A, FISH_C, FISH_B, 2, True),
    (45, 6, FISH_B, FISH_C, FISH_B, 2, True),
    (50, 9, FISH_A, FISH_C, FISH_B, 2, True),
    (57, 7, FISH_B, FISH_C, FISH_B, 2, True),
    (11, 16, FISH_A, FISH_C, FISH_B, 2, True),
    (18, 18, FISH_B, FISH_C, FISH_B, 1, True),
    (25, 15, FISH_A, FISH_C, FISH_B, 2, True),
    (46, 12, FISH_B, FISH_C, FISH_B, 2, True),
    (57, 12, FISH_A, FISH_C, FISH_B, 1, True),
    (61, 20, FISH_B, FISH_C, FISH_B, 1, True),
    (6, 23, FISH_A, FISH_C, FISH_B, 1, True),
    (14, 25, FISH_B, FISH_C, FISH_B, 1, True),
    (22, 22, FISH_A, FISH_C, FISH_B, 1, True),
    (50, 24, FISH_B, FISH_C, FISH_B, 1, True),
    (58, 22, FISH_A, FISH_C, FISH_B, 1, True),
    (26, 4, FISH_B, FISH_C, FISH_B, 1, True),
    (40, 4, FISH_A, FISH_C, FISH_B, 1, True),
]
for (fx2, fy, c1, c2, c3, sz, rt) in school:
    fish(fishes, fx2, fy, c1, c2, c3, EYE, sz, rt)
# fish slipping through the breach
fish(fishes, 48, 43, FISH_A, FISH_C, FISH_B, EYE, 2, True)
fish(fishes, 45, 40, FISH_B, FISH_C, FISH_B, EYE, 1, False)
# larger fish cruising the other way along the hull
fish(fishes, 54, 34, FISH_D, FISH_E, BUB_L, EYE, 3, False)
fish(fishes, 36, 30, FISH_D, FISH_E, BUB_L, EYE, 2, False)
fish(fishes, 60, 42, FISH_D, FISH_E, BUB_L, EYE, 2, False)

# ======================= 11. bubbles + snow =======================
fxl = new_canvas(W, H, name='fx')
for (bx, by, n) in [(49, 34, 9), (8, 26, 6), (58, 16, 5), (30, 24, 4)]:
    for k in range(n):
        yy = by - k * 3
        xx = bx + int(round(math.sin(k * 1.1 + bx) * 1.6))
        if yy < 1 or xx < 1 or xx > 62:
            continue
        if k % 3 == 0:
            fxl.circle(xx, yy, 1, BUB_M)
            fxl.set(xx - 1, yy - 1, BUB_L)
        else:
            fxl.set(xx, yy, BUB_L)
            fxl.set(xx - 1, yy, BUB_M)
snow_pts = [(3, 8), (11, 4), (19, 19), (27, 6), (35, 22), (43, 5), (51, 19),
            (59, 7), (7, 33), (15, 40), (23, 34), (31, 45), (39, 36), (47, 47),
            (55, 42), (62, 38), (2, 48), (20, 50), (36, 52), (52, 33),
            (16, 30), (28, 38), (44, 40), (60, 48), (8, 18), (48, 27),
            (34, 33), (12, 47), (26, 55), (41, 55), (58, 57)]
for i, (sx, sy) in enumerate(snow_pts):
    fxl.set(sx, sy, BUB_M if i % 3 else RAYC)

# ======================= 12. composite =======================
result = flatten([bg, rays, far, sand, hull, sup, drift, weed, coral, fishes, fxl],
                 name='result', background=WATER[11])
view(result)
print(result.stats_text())
finish(result)
