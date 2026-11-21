import random, math
random.seed(11)

W = H = 128
c = new_canvas(W, H, background=None, name="result")

# ---------- helpers ----------
def px(x, y, col):
    x = int(x); y = int(y)
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, col)

def geti(x, y):
    if 0 <= x < W and 0 <= y < H:
        return c.get(x, y)
    return -1

def dither(x0, y0, w, h, cols, density):
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            if random.random() < density:
                px(x, y, random.choice(cols))

def thick_line(x0, y0, x1, y1, w, col):
    c.line(int(x0), int(y0), int(x1), int(y1), col)
    for i in range(1, w):
        off = (i + 1) // 2 * (1 if i % 2 else -1)
        c.line(int(x0) + off, int(y0), int(x1) + off, int(y1), col)

# ---------- sky ----------
SKY = ["#150d2a", "#1d1338", "#261a46", "#2f2154", "#382862"]
horizon = 86
band_h = horizon / len(SKY)
for i, colr in enumerate(SKY):
    y0 = int(i * band_h); y1 = int((i + 1) * band_h)
    c.rect(0, y0, W, y1 - y0, colr)
for i in range(1, len(SKY)):
    yb = int(i * band_h)
    dither(0, yb - 2, W, 4, [SKY[i - 1], SKY[i]], 0.4)

# ---------- stars ----------
for _ in range(80):
    x = random.randint(0, W - 1); y = random.randint(0, horizon - 16)
    if (x - 97) ** 2 + (y - 24) ** 2 < 20 * 20:
        continue
    r = random.random()
    if r < 0.10:
        px(x, y, "#e8e0ff")
        px(x - 1, y, "#b8a8e8"); px(x + 1, y, "#b8a8e8")
        px(x, y - 1, "#b8a8e8"); px(x, y + 1, "#b8a8e8")
    elif r < 0.45:
        px(x, y, "#cfc4ee")
    else:
        px(x, y, "#8f80c0")

# ---------- moon ----------
c.circle(97, 24, 14, "#3a2c60")
c.circle(97, 24, 12, "#463670")
c.circle(97, 24, 10, "#52427e")
for y in range(6, 44):
    for x in range(79, 116):
        d2 = (x - 97) ** 2 + (y - 24) ** 2
        if 196 <= d2 <= 256 and random.random() < 0.3:
            px(x, y, "#3a2c60")
c.circle(97, 24, 8, "#f2ecd2")
c.circle(94, 22, 2, "#ddd2ac")
c.circle(100, 27, 1, "#ddd2ac")
c.circle(99, 20, 1, "#e4dab6")

# ---------- distant silhouette trees ----------
SIL = "#1c1430"
def conifer(cx, base, w, h, colr):
    c.poly([(cx, base - h), (cx - w // 2, base), (cx + w // 2, base)], colr)
    c.rect(cx - 1, base - 4, 3, 5, colr)
conifer(2, 86, 12, 24, SIL)
conifer(18, 86, 9, 16, SIL)
conifer(84, 86, 10, 18, SIL)
conifer(72, 86, 7, 12, SIL)

# ---------- mist band ----------
MIST = ["#4a3a6e", "#56467c", "#63537f"]
for y in range(64, 88):
    dens = 0.55 if y > 74 else 0.28
    x = 0
    while x < W:
        if random.random() < dens:
            ln = random.randint(3, 14)
            colr = random.choice(MIST)
            for xx in range(x, min(x + ln, W)):
                px(xx, y, colr)
            x += ln + random.randint(1, 4)
        else:
            x += random.randint(1, 3)

# ---------- ground ----------
GROUND = "#262036"
c.rect(0, 86, W, 42, GROUND)
dither(0, 86, W, 42, ["#2e2840", "#1f1a2c"], 0.18)
g_set = {c.color(x) for x in [GROUND, "#2e2840", "#1f1a2c"]}
dither(0, 86, W, 2, ["#332a4a"], 0.4)

# ---------- stone-slab path ----------
PATH = ["#55505c", "#655f6c", "#4a4552"]
y = 95
while y < H:
    width = 10 + int((y - 95) * 0.55)
    cxp = 56 + int((y - 95) * 0.10)
    x0 = cxp - width // 2
    x1 = x0 + width
    x = x0
    while x < x1:
        sw = min(random.randint(4, 8), x1 - x)
        sh = min(random.randint(3, 5), H - y)
        colr = random.choice(PATH)
        c.rect(x, y, sw, sh, colr)
        for xx in range(x, x + sw):
            px(xx, y, "#716b7d")
        x += sw + 1
    y += random.randint(4, 5)

# ---------- cottage ----------
# walls (wood planks)
c.rect(34, 56, 42, 26, "#4a3527")
for yy in range(60, 82, 4):
    c.line(34, yy, 75, yy, "#3a2a1e")
dither(34, 56, 42, 26, ["#54402e", "#5e4834"], 0.14)
c.rect(34, 56, 42, 2, "#33241a")          # top beam
c.line(34, 56, 34, 81, "#33241a")          # corner beams
c.line(75, 56, 75, 81, "#33241a")

# window glow on walls (drawn before windows)
dither(33, 59, 19, 19, ["#6e4426", "#7e5230"], 0.30)
dither(63, 59, 19, 19, ["#6e4426", "#7e5230"], 0.30)

# door
c.rect(49, 77, 14, 18, "#54402e")          # frame
c.rect(50, 78, 12, 17, "#3a2a1e")
c.rect(51, 76, 10, 2, "#3a2a1e")
c.rect(52, 75, 8, 1, "#3a2a1e")            # arch
for xx in (53, 56, 59):
    c.line(xx, 78, xx, 94, "#2c1f16")
px(60, 86, "#c8a050")

# windows
def window(wx, wy):
    c.rect(wx - 1, wy - 1, 11, 11, "#33241a")
    c.rect(wx, wy, 9, 9, "#e07820")
    c.rect(wx + 1, wy + 1, 7, 7, "#ffb347")
    c.rect(wx + 3, wy + 3, 3, 3, "#ffd27a")
    c.line(wx + 4, wy, wx + 4, wy + 8, "#33241a")
    c.line(wx, wy + 4, wx + 8, wy + 4, "#33241a")
    # flower box
    c.rect(wx - 1, wy + 10, 11, 2, "#4a3527")
    for fx in (wx, wx + 3, wx + 6):
        px(fx, wy + 9, "#b04868")
        px(fx + 2, wy + 9, "#8a3854")
window(37, 63)
window(67, 63)

# stone base
c.rect(33, 82, 44, 13, "#38333f")
yb = 82; row = 0
while yb < 95:
    xb = 33 + (random.randint(0, 2) if row % 2 else 0)
    while xb < 77:
        sw = random.randint(4, 7)
        c.rect(xb, yb, min(sw, 77 - xb), 4, random.choice(["#5a5460", "#6a6470", "#4e4854"]))
        xb += sw + 1
    yb += 5; row += 1

# steep mossy roof
c.poly([(54, 24), (26, 58), (84, 58)], "#2e4428")
roof_idx = c.color("#2e4428")
MOSS = ["#3e5a34", "#4e6c40", "#5f7e4c", "#35502c"]
for yy in range(24, 59):
    for xx in range(26, 85):
        if geti(xx, yy) == roof_idx and random.random() < 0.55:
            px(xx, yy, random.choice(MOSS))
# moss clumps near ridge
for (mx, my) in [(48, 32), (58, 36), (44, 40), (62, 44), (52, 28)]:
    c.rect(mx, my, 3, 2, "#5f7e4c")
c.line(54, 24, 26, 58, "#243620")
c.line(54, 24, 84, 58, "#243620")
c.rect(25, 56, 60, 3, "#243620")           # eave board
for _ in range(30):                         # dangling moss
    ex = random.randint(26, 83)
    if random.random() < 0.6:
        px(ex, 59, random.choice(MOSS))

# chimney + smoke
c.rect(64, 28, 7, 12, "#5a5460")
c.rect(63, 26, 9, 2, "#454050")
c.rect(66, 31, 2, 1, "#454050"); c.rect(64, 35, 2, 1, "#454050")
c.circle(68, 22, 2, "#6a5a84")
c.circle(71, 17, 3, "#7a6a94")
c.circle(76, 11, 4, "#7a6a94")
c.circle(81, 6, 3, "#6a5a84")

# ---------- stone well with wooden winch ----------
c.poly([(104, 58), (88, 73), (120, 73)], "#3a2a1e")
wroof_idx = c.color("#3a2a1e")
for yy in range(58, 74):
    for xx in range(88, 121):
        if geti(xx, yy) == wroof_idx and random.random() < 0.35:
            px(xx, yy, random.choice(["#3e5a34", "#4e6c40"]))
c.line(88, 73, 120, 73, "#241a12")
c.rect(95, 72, 3, 21, "#4a3527")
c.rect(114, 72, 3, 21, "#4a3527")
# stone well wall behind the bucket
c.rect(96, 84, 20, 9, "#38333f")
yb2 = 84; row2 = 0
while yb2 < 93:
    xb2 = 96 + (random.randint(0, 2) if row2 % 2 else 0)
    while xb2 < 116:
        sw2 = random.randint(4, 7)
        c.rect(xb2, yb2, min(sw2, 116 - xb2), 4, random.choice(["#5a5460", "#6a6470", "#4e4854"]))
        xb2 += sw2 + 1
    yb2 += 4; row2 += 1
c.rect(96, 84, 20, 1, "#2a2632")
c.rect(95, 75, 22, 2, "#5c4232")
c.rect(102, 73, 7, 6, "#6e5240")
c.line(102, 75, 108, 75, "#4a3527"); c.line(102, 77, 108, 77, "#4a3527")
c.line(109, 76, 112, 76, "#8a7040"); c.line(112, 76, 112, 73, "#8a7040")
c.line(105, 79, 105, 88, "#8a7040")
c.rect(102, 88, 7, 5, "#54402e"); c.rect(102, 88, 7, 1, "#3a2a1e")
c.rect(92, 92, 26, 10, "#38333f")
yb = 92; row = 0
while yb < 102:
    xb = 92 + (random.randint(0, 2) if row % 2 else 0)
    while xb < 118:
        sw = random.randint(4, 7)
        c.rect(xb, yb, min(sw, 118 - xb), 4, random.choice(["#5a5460", "#6a6470", "#4e4854"]))
        xb += sw + 1
    yb += 4; row += 1
c.rect(97, 92, 16, 2, "#141020")

# ---------- twisted ancient trees ----------
TRUNK = "#2e1f28"; TRUNK_L = "#3e2c34"
LEAF = ["#4a1f2a", "#5c2a30", "#3a1a30", "#6b3540"]
def canopy(cx, cy, r):
    c.circle(cx, cy, r, random.choice(LEAF))
    for _ in range(r * 3):
        ang = random.random() * 6.283
        rr = r * (0.3 + 0.8 * random.random())
        px(cx + math.cos(ang) * rr, cy + math.sin(ang) * rr * 0.8, random.choice(LEAF))
    for _ in range(r):
        px(cx - random.randint(0, r), cy - random.randint(0, r), "#7a4450")
    for _ in range(r):
        px(cx + random.randint(0, r), cy + random.randint(0, r), "#2e1424")

def tree(points, widths, branches, clusters):
    for i in range(len(points) - 1):
        thick_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], widths[i], TRUNK)
        c.line(points[i][0] + 1, points[i][1], points[i + 1][0] + 1, points[i + 1][1], TRUNK_L)
    for (bx0, by0, bx1, by1, bw) in branches:
        thick_line(bx0, by0, bx1, by1, bw, TRUNK)
    for (cx, cy, r) in clusters:
        canopy(cx, cy, r)

# left tree
tree([(10, 130), (8, 112), (13, 96), (9, 80), (14, 64), (12, 50), (16, 40)],
     [7, 6, 5, 5, 4, 3],
     [(9, 80, 1, 72, 3), (14, 64, 24, 56, 3), (12, 50, 20, 44, 2), (16, 40, 10, 32, 2),
      (13, 96, 22, 90, 2)],
     [(14, 32, 7), (24, 40, 6), (4, 44, 6), (20, 26, 5), (28, 50, 5), (0, 54, 5), (10, 44, 6)])
c.line(10, 128, 3, 124, TRUNK); c.line(9, 128, 16, 125, TRUNK)

# right tree
tree([(122, 130), (124, 112), (120, 96), (124, 80), (121, 66), (124, 54)],
     [6, 5, 5, 4, 3],
     [(121, 66, 112, 58, 3), (124, 54, 118, 46, 2)],
     [(120, 44, 6), (110, 52, 5), (127, 58, 5), (124, 34, 5), (114, 62, 4), (127, 44, 4)])
c.line(122, 128, 116, 125, TRUNK); c.line(123, 128, 127, 124, TRUNK)

# ---------- warm light spill on ground ----------
dither(44, 95, 26, 11, ["#5a4030", "#6a4c34"], 0.35)
dither(33, 95, 12, 6, ["#5a4030"], 0.30)
dither(65, 95, 12, 6, ["#5a4030"], 0.30)

# ---------- grass tufts & mushrooms ----------
for _ in range(70):
    gx = random.randint(0, 127); gy = random.randint(97, 127)
    if geti(gx, gy) in g_set:
        px(gx, gy, "#3a4a3a")
        if geti(gx, gy - 1) in g_set:
            px(gx, gy - 1, "#2e3c30")
def mushroom(mx, my):
    c.rect(mx, my - 2, 1, 2, "#d8cfc0")
    c.rect(mx - 1, my - 3, 3, 1, "#a03040")
    px(mx, my - 4, "#a03040")
    px(mx - 1, my - 3, "#e8e0d0")
mushroom(40, 101); mushroom(78, 108); mushroom(24, 112)

# ---------- fireflies ----------
for (fx, fy) in [(30, 98), (80, 92), (90, 80), (22, 70), (72, 48), (42, 42), (112, 98)]:
    px(fx, fy, "#ffd27a")
    px(fx + 1, fy, "#a06a30"); px(fx - 1, fy, "#a06a30")
    px(fx, fy + 1, "#a06a30"); px(fx, fy - 1, "#a06a30")

# ---------- falling leaves ----------
for _ in range(12):
    lx = random.randint(8, 120); ly = random.randint(36, 92)
    px(lx, ly, random.choice(["#6b3540", "#5c2a30", "#7a4450"]))

# ---------- foreground mist ----------
for y in range(100, 122):
    x = 0
    while x < W:
        if random.random() < 0.10:
            ln = random.randint(4, 12)
            colr = random.choice(["#4a3a6e", "#56467c"])
            for xx in range(x, min(x + ln, W)):
                px(xx, y, colr)
            x += ln + random.randint(2, 6)
        else:
            x += random.randint(1, 4)

# ---------- vignette ----------
dither(0, 0, 22, 22, ["#100a20"], 0.15)
dither(106, 0, 22, 22, ["#100a20"], 0.15)
dither(0, 106, 22, 22, ["#100a20"], 0.15)
dither(106, 106, 22, 22, ["#100a20"], 0.15)

print(c.stats_text())
save("result", c)
finish(c)
