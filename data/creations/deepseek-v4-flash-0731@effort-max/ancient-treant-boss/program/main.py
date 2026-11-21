import math, random
from pixelbench_api import new_canvas, flatten, finish

W = H = 256
MIR = lambda x: 256 - x

OUT = "#0d100c"
B1 = "#241a11"; B2 = "#332414"; B3 = "#42301c"; B4 = "#533d26"; B5 = "#664c30"
B6 = "#7a5e3b"; B7 = "#917348"; B8 = "#a88455"
M1 = "#1d3d21"; M2 = "#2d5a2e"; M3 = "#3f7a3c"; M4 = "#57a04e"; M5 = "#77c25f"
E1 = "#06240f"; E2 = "#0f7a24"; E3 = "#1fb83c"; E4 = "#3df268"; E5 = "#a8ff9e"
V1 = "#2c4f26"; V2 = "#3d6b2f"; V3 = "#5d9440"
SKY = ["#0b1d24", "#102a2b", "#173a34", "#1f4b3f", "#285e4b", "#337459", "#418c67", "#52a676"]
FOR = ["#152f24", "#1c3f2e", "#245238", "#2e6844"]
GRD = ["#1f2b1d", "#283822", "#32472a", "#3e5834", "#4c6c40", "#5c824e", "#6f9a5e"]
DIRT = ["#3f2f20", "#4f3c29", "#614a33", "#755a3f"]
RAY1 = "#9fc798"; RAY2 = "#bcdba4"; RAY3 = "#d9eec0"; RAY4 = "#f2f7d8"
SPR = "#d6eeb0"

# ------------------------------------------------------------------ sky + forest
bg = new_canvas(W, H)
for y in range(160):
    bg.line(0, y, 255, y, SKY[min(7, y // 20)])

r = random.Random(11)
for x in range(256):
    if x < 110 or x > 146:
        far = (x < 70 or x > 186)
        t = r.randint(92, 150) if far else r.randint(122, 153)
        col = FOR[0] if (x < 58 or x > 198) else FOR[1]
        bg.line(x, t, x, 158, col)
        if r.random() < 0.3 and (x < 44 or x > 212):
            bg.line(x, t, x + 1, t, FOR[0])
for y in range(158, 256):
    bg.line(0, y, 255, y, GRD[min(6, (y - 158) * 6 // 97)])
bg.ellipse(128, 204, 92, 30, GRD[4])
bg.ellipse(128, 210, 70, 22, GRD[5])
bg.ellipse(128, 216, 46, 14, GRD[6])
bg.ellipse(128, 224, 38, 9, DIRT[2])
bg.ellipse(128, 228, 24, 6, DIRT[3])
bg.ellipse(128, 242, 82, 13, "#161c14")
bg.ellipse(10, 226, 34, 44, GRD[0])
bg.ellipse(246, 226, 34, 44, GRD[0])
# dead trees on the flanks
for (tx, ty, side) in [(30, 88, -1), (52, 106, 1), (150, 118, -1), (120, 122, 1),
                     (206, 102, -1), (226, 90, 1), (74, 124, 1)]:
    bg.line(tx, ty, tx, 156, FOR[0])
    bg.line(tx, ty, tx + side * 7, ty + 9, FOR[0])
    bg.line(tx, ty + 14, tx + side * 8, ty + 12, FOR[0])

# ------------------------------------------------------------------ god rays
rays = new_canvas(W, H)
def ray(x0, x1, x2, x3, col):
    rays.poly([(x0, 0), (x1, 0), (x2, 156), (x3, 156)], col)
ray(6, 40, 82, 138, RAY1)
ray(38, 70, 120, 84, RAY2)
ray(66, 96, 146, 116, RAY3)
ray(92, 120, 172, 146, RAY2)
ray(116, 138, 192, 156, RAY1)
rays.ellipse(128, 88, 62, 44, RAY1)
rays.ellipse(128, 82, 42, 30, RAY2)
rays.ellipse(128, 76, 26, 18, RAY3)
rays.ellipse(128, 72, 14, 10, RAY4)

# ------------------------------------------------------------------ treant
tb = new_canvas(W, H)
def limb(pts, w0, w1, col):
    left = []; right = []; n = len(pts)
    for i, (x, y) in enumerate(pts):
        if i < n - 1:
            dx = pts[i + 1][0] - x; dy = pts[i + 1][1] - y
        else:
            dx = x - pts[i - 1][0]; dy = y - pts[i - 1][1]
        L = math.hypot(dx, dy) or 1e-9
        nx, ny = -dy / L, dx / L
        t = i / (n - 1) if n > 1 else 0.0
        w = w0 + (w1 - w0) * t
        left.append((round(x + nx * w), round(y + ny * w)))
        right.append((round(x - nx * w), round(y + ny * w)))
    tb.poly(left + right[::-1], col)

# --- body silhouette -------------------------------------------------
tb.ellipse(128, 58, 32, 26, B2)
tb.circle(109, 42, 13, B1); tb.circle(147, 40, 14, B1)
tb.circle(124, 26, 12, B2); tb.circle(141, 29, 11, B2)
tb.circle(100, 55, 12, B2); tb.circle(156, 53, 12, B2)
limb([(112, 30), (103, 19)], 7, 3, B2); limb([(103, 19), (95, 10)], 4, 2, B1)
limb([(127, 22), (126, 12)], 6, 3, B2)
limb([(143, 24), (149, 14)], 7, 3, B2); limb([(149, 14), (156, 8)], 4, 2, B1)
limb([(97, 46), (88, 33), (80, 23)], 6, 3, B1)
limb([(159, 45), (168, 32), (176, 22)], 6, 3, B1)
tb.ellipse(128, 84, 52, 23, B3)
tb.circle(90, 88, 16, B3); tb.circle(166, 88, 16, B3)
tb.poly([(84, 96), (172, 96), (168, 136), (150, 166), (128, 180), (106, 166), (88, 136)], B4)
tb.ellipse(128, 176, 42, 18, B3)
tb.poly([(98, 112), (158, 112), (152, 140), (138, 162), (128, 170), (118, 162), (104, 140)], B5)
tb.poly([(110, 120), (146, 120), (142, 138), (132, 152), (128, 156), (124, 152), (114, 138)], B6)
tb.poly([(96, 168), (122, 168), (120, 236), (104, 246), (92, 238), (88, 204)], B4)
tb.poly([(160, 168), (134, 168), (136, 236), (152, 246), (164, 238), (168, 204)], B4)
tb.poly([(100, 176), (118, 176), (116, 228), (104, 236), (96, 228), (94, 206)], B5)
tb.poly([(156, 176), (138, 176), (140, 228), (152, 236), (160, 228), (162, 206)], B5)
limb([(86, 96), (72, 86), (62, 74), (54, 60), (48, 46)], 13, 8, B4)
limb([(48, 46), (42, 34), (34, 22)], 8, 5, B3)
limb([(34, 22), (23, 12)], 5, 2, B2)
limb([(34, 22), (37, 9)], 5, 2, B2)
limb([(38, 24), (48, 12)], 4, 2, B2)
limb([(46, 40), (36, 44)], 3, 1, B2)
limb([(56, 52), (46, 58)], 3, 1, B2)
limb([(170, 96), (184, 86), (194, 74), (202, 60), (208, 46)], 13, 8, B4)
limb([(208, 46), (214, 34), (222, 22)], 8, 5, B3)
limb([(222, 22), (233, 12)], 5, 2, B2)
limb([(222, 22), (219, 9)], 5, 2, B2)
limb([(218, 24), (208, 12)], 4, 2, B2)
limb([(210, 40), (220, 44)], 3, 1, B2)
limb([(200, 52), (210, 58)], 3, 1, B2)
tb.poly([(94, 238), (76, 226), (60, 212), (47, 196), (55, 186), (68, 198), (84, 214), (93, 226)], B3)
tb.poly([(162, 238), (180, 226), (196, 212), (209, 196), (201, 186), (188, 198), (172, 214), (163, 226)], B3)
tb.poly([(96, 244), (88, 232), (93, 220), (103, 230), (110, 244)], B2)
tb.poly([(160, 244), (168, 232), (163, 220), (153, 230), (146, 244)], B2)
tb.poly([(72, 236), (62, 224), (66, 214), (76, 224)], B2)
tb.poly([(184, 236), (194, 224), (190, 214), (180, 224)], B2)
tb.poly([(74, 80), (66, 68), (84, 78)], B3)
tb.poly([(182, 80), (190, 68), (172, 78)], B3)
for (x0, y0) in [(88, 10), (104, 12), (120, 14), (136, 14), (152, 12), (168, 10)]:
    tb.poly([(x0, 240), (x0 - 6, 252), (x0 + 4, 252)], B3)
    tb.poly([(x0, 240), (x0 + 4, 252), (x0 + 10, 252)], B2)
# surface root across the clearing floor
tb.poly([(58, 230), (80, 242), (104, 248), (128, 244), (104, 236), (82, 232)], B3)
tb.poly([(64, 236), (82, 242), (102, 244), (98, 241), (82, 238)], B5)
tb.poly([(198, 230), (176, 242), (152, 248), (128, 244), (152, 236), (174, 232)], B3)
tb.poly([(192, 236), (174, 242), (154, 244), (158, 241), (174, 238)], B5)
# moss clumps (merged, so they get the dark outline)
tb.ellipse(92, 92, 11, 6, M3); tb.ellipse(164, 92, 11, 6, M2)
tb.ellipse(100, 60, 9, 6, M2); tb.ellipse(150, 58, 9, 6, M3)
tb.ellipse(128, 30, 9, 6, M3)
tb.ellipse(100, 178, 9, 5, M2); tb.ellipse(156, 178, 9, 5, M2)
tb.ellipse(116, 238, 14, 6, M3); tb.ellipse(140, 238, 14, 6, M4)
tb.ellipse(52, 50, 7, 4, M2); tb.ellipse(196, 50, 7, 4, M2)
tb.circle(48, 48, 6, B3); tb.circle(208, 48, 6, B3)
tb.outline(OUT)

# --- face -----------------------------------------------------------
tb.ellipse(117, 113, 11, 9, E2); tb.ellipse(139, 113, 11, 9, E2)
tb.ellipse(117, 113, 8, 7, B1); tb.ellipse(139, 113, 8, 7, B1)
tb.ellipse(117, 113, 5, 4, E3); tb.ellipse(139, 113, 5, 4, E3)
tb.ellipse(117, 114, 3, 2, E4); tb.ellipse(139, 114, 3, 2, E4)
tb.ellipse(117, 114, 1, 1, E5); tb.ellipse(139, 114, 1, 1, E5)
tb.line(109, 103, 124, 107, B1)
tb.line(132, 107, 147, 103, B1)
tb.poly([(123, 122), (131, 121), (130, 133), (127, 139), (129, 148), (126, 156), (124, 162)], B1)
tb.line(126, 128, 128, 136, E3)
tb.line(126, 146, 127, 152, E4)
tb.set(125, 158, E2)

# --- bark texture ----------------------------------------------------
rng = random.Random(7)
for _ in range(170):
    t = rng.random()
    if t < 0.48:
        x0 = rng.randint(92, 164); y0 = rng.randint(100, 170)
        zx = (92, 164); wy = (98, 172); n = 8
    elif t < 0.70:
        if rng.random() < 0.5:
            x0 = rng.randint(96, 118); y0 = rng.randint(174, 232)
            zx = (90, 124); wy = (170, 240)
        else:
            x0 = rng.randint(138, 160); y0 = rng.randint(174, 232)
            zx = (132, 166); wy = (170, 240)
        n = 7
    else:
        x0 = rng.randint(94, 162); y0 = rng.randint(72, 100)
        zx = (86, 170); wy = (66, 104); n = 6
    x = x0; y = y0
    colc = B1 if rng.random() < 0.8 else B2
    for _s in range(n):
        x2 = min(max(x + rng.randint(-2, 2), zx[0]), zx[1])
        y2 = min(max(y + rng.randint(-1, 2), wy[0]), wy[1])
        tb.line(x, y, x2, y2, colc)
        x, y = x2, y2

hl = random.Random(23)
for _ in range(95):
    t = hl.random()
    if t < 0.5:
        x0 = hl.randint(92, 164); y0 = hl.randint(100, 168)
        zx = (92, 164); wy = (98, 172); n = 5
    else:
        x0 = hl.randint(96, 160); y0 = hl.randint(174, 230)
        zx = (92, 164); wy = (172, 238); n = 5
    x = x0; y = y0
    for _s in range(n):
        x2 = min(max(x + hl.randint(-1, 2), zx[0]), zx[1])
        y2 = min(max(y + hl.randint(-1, 1), wy[0]), wy[1])
        tb.line(x, y, x2, y2, B7)
        x, y = x2, y2

# knots
for (kx, ky) in [(108, 128), (142, 149), (118, 158), (126, 140), (100, 164),
                (154, 128), (112, 146), (136, 122), (104, 186), (150, 190)]:
    tb.circle(kx, ky, 2, B1)
    tb.circle(kx + 1, ky - 1, 1, B6)
# rim light (light from upper left)
tb.line(86, 100, 84, 124, B7); tb.line(84, 126, 90, 150, B6)
tb.line(70, 87, 62, 76, B7)
tb.line(96, 172, 94, 214, B7); tb.line(94, 216, 96, 234, B6)
tb.line(168, 104, 166, 132, B1)
# extra twigs on the crown
tb.line(100, 36, 91, 29, B2); tb.line(94, 44, 83, 36, B1)
tb.line(158, 36, 168, 28, B2); tb.line(162, 44, 172, 36, B1)
# claw twigs at the raised arm tips
for (ax, ay, sx) in [(23, 12, -1), (37, 9, 1), (48, 12, 1), (233, 12, -1), (219, 9, -1), (208, 12, -1)]:
    tb.line(ax, ay, ax - 5, ay - 7, B1)
    tb.line(ax, ay, ax + sx * 4, ay - 6, B2)
    tb.line(ax, ay, ax + sx * 6, ay - 2, B2)
# gnarled branch texture in the crown
cr = random.Random(31)
for _ in range(60):
    x0 = cr.randint(96, 160); y0 = cr.randint(18, 70)
    x = x0; y = y0
    for _s in range(5):
        x2 = min(max(x + cr.randint(-2, 2), 88), 168)
        y2 = min(max(y + cr.randint(-2, 2), 8), 74)
        tb.line(x, y, x2, y2, B1 if cr.random() < 0.75 else B3)
        x, y = x2, y2

# --- vines ----------------------------------------------------------
def vine(x0, y0, ln, col, phase):
    pts = [(x0, y0)]
    for k in range(1, ln):
        pts.append((x0 + round(2.4 * math.sin(k * 0.55 + phase) + 0.8 * math.sin(k * 0.21)), y0 + k))
    for i in range(len(pts) - 1):
        tb.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], col)
    for k in range(1, ln, 3):
        x2, y2 = pts[k]
        tb.rect(x2 + 1, y2, 2, 1, V3)

vine(80, 90, 60, V2, 0.4)
vine(74, 102, 50, V1, 1.6)
vine(86, 92, 38, V2, 2.2)
vine(168, 94, 44, V1, 2.8)
vine(176, 90, 58, V2, 0.9)
vine(58, 56, 44, V2, 1.2)
vine(198, 56, 44, V2, 0.3)
vine(48, 44, 26, V1, 2.5)
vine(208, 44, 26, V1, 1.0)
vine(120, 180, 24, V2, 2.0)
vine(136, 182, 30, V1, 0.8)
# glow lichen on chest
for (gx, gy) in [(118, 148), (136, 140), (124, 158), (112, 134), (146, 148)]:
    tb.set(gx, gy, E2)
    tb.set(gx + 1, gy + 1, E3)

# ------------------------------------------------------------------ foreground
fg = new_canvas(W, H)
fg.ellipse(16, 244, 28, 13, "#1a3327")
fg.ellipse(240, 244, 28, 13, "#1a3327")
fg.ellipse(44, 248, 18, 9, "#22402d")
fg.ellipse(212, 248, 18, 9, "#22402d")
r2 = random.Random(3)
for _ in range(160):
    x = r2.randint(3, 252); y = r2.randint(238, 254); h = r2.randint(3, 8)
    fg.line(x, 255, x + r2.randint(-3, 3), 255 - h, "#45673c")
    fg.line(x, 255, x - r2.randint(0, 3), 255 - h + 2, "#31492a")
r3 = random.Random(9)
for _ in range(70):
    x = r3.randint(10, 245); y = r3.randint(16, 148)
    fg.set(x, y, SPR)
    if r3.random() < 0.35:
        fg.set(x + 1, y, RAY4)

# ------------------------------------------------------------------ vignette
vig = new_canvas(W, H)
vig.circle(0, 0, 112, (13, 24, 15, 120))
vig.circle(256, 0, 112, (13, 24, 15, 120))
vig.circle(0, 256, 112, (13, 24, 15, 120))
vig.circle(256, 256, 112, (13, 24, 15, 120))
vig.circle(64, 256, 120, (13, 24, 15, 120))

final = flatten([bg, rays, tb, fg, vig])
print(final.stats_text())
finish(final)
