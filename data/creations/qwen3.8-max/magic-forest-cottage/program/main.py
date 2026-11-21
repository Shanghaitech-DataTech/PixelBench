import random
from math import cos, sin

W = H = 128
c = new_canvas(W, H, name="cottage")
R = random.Random(7711)

# ================= PALETTE =================
SKY = ['#0d0616', '#150a24', '#1d0e31', '#26143e', '#2f194b',
       '#382058', '#412766', '#4a2e74', '#533682']
STAR = ['#ffffff', '#d9d2f2', '#a99fd0']
MGLOW = ['#402c61', '#4d3571', '#5b3f82', '#6a4a94']
MOON = ['#fdf7e2', '#efe6c8', '#ddd0ab', '#c6b78f']
MIST = ['#3b2c5a', '#4a3a6c', '#5a487e', '#6b5891', '#7d6aa4']
FAR = ['#1b1029', '#241636']
GROUND = ['#101a18', '#16231d', '#1d2c22', '#243627', '#2c402d', '#1a1526']
STONE = ['#332e3d', '#443e52', '#56506a', '#68617c', '#7a7290']
WOOD = ['#241708', '#33210f', '#452d15', '#5a3c1e', '#6f4c28']
THATCH = ['#241a2e', '#3a2b47', '#4d3a5c']
MOSS = ['#26381f', '#31481f', '#3d5c28', '#4a7032', '#5a863c']
LIGHT = ['#fff0c0', '#ffd478', '#ffb03a', '#e88a20']
WGLOW = ['#a85f2c', '#8a4a2c', '#6d3934', '#532c3e', '#3e2349']
LEAF = ['#3a1220', '#521a28', '#6e2534', '#8a3340',
        '#2c1436', '#42204e', '#5a2f66']
TRUNK = ['#150d1c', '#221527', '#31202f', '#452d38']
SHROOM = ['#5aa89c', '#8fd6c8']

# ================= HELPERS =================
def dither_row(y, ca, cb, level, x0=0, x1=W):
    c.rect(x0, y, x1 - x0, 1, ca)
    if level == 0:
        return
    if level >= 4:
        c.rect(x0, y, x1 - x0, 1, cb)
        return
    if level == 2:
        for x in range(x0, x1):
            if (x + y) % 2 == 0:
                c.set(x, y, cb)
    elif level == 1:
        for x in range(x0, x1):
            if x % 4 == (y % 4):
                c.set(x, y, cb)
    else:
        c.rect(x0, y, x1 - x0, 1, cb)
        for x in range(x0, x1):
            if x % 4 == (y % 4):
                c.set(x, y, ca)


def bez(p0, p1, p2, p3, steps=48):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        pts.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                    u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    return pts


def tapered(pts, w0, w1, color):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        w = w0 + (w1 - w0) * (i / max(1, n - 1))
        r = int(round(w / 2.0))
        c.circle(int(round(x)), int(round(y)), max(0, r), color)


def glow_disc(cx, cy, radii, colors):
    for r, col in zip(radii, colors):
        c.circle(cx, cy, r, col)


def stone_fill(x0, y0, x1, y1, tones, mortar, seed=5, bh=4, bw=8):
    rnd = random.Random(seed)
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, mortar)
    y = y0
    row = 0
    while y + bh - 1 <= y1:
        off = (row % 2) * (bw // 2)
        x = x0 - off
        while x <= x1:
            a = max(x0, x + 1)
            b = min(x1, x + bw - 1)
            if b > a:
                c.rect(a, y, b - a + 1, bh - 1, rnd.choice(tones))
            x += bw
        y += bh
        row += 1


def leafmass(cx, cy, rx, ry, seed, dark, mid, hi, dens=1.0):
    rnd = random.Random(seed)
    c.ellipse(cx, cy, rx, ry, dark)
    n = int(rx * ry * 0.55 * dens)
    for _ in range(n):
        a = rnd.random() * 6.2831
        rr = rnd.random() ** 0.6
        x = int(round(cx + cos(a) * rr * rx))
        y = int(round(cy + sin(a) * rr * ry * 0.9))
        c.circle(x, y, rnd.choice([1, 1, 2]), mid)
    for _ in range(int(n * 0.45)):
        a = rnd.uniform(2.6, 5.0)
        rr = rnd.random() ** 0.7
        x = int(round(cx + cos(a) * rr * rx * 0.9))
        y = int(round(cy + sin(a) * rr * ry * 0.8))
        c.set(x, y, hi)


def glow_soft(cx, cy, stops):
    """stops: list of (radius, color) outer->inner; transitions dithered."""
    for i, (r, col) in enumerate(stops):
        c.circle(cx, cy, r, col)
        if i > 0:
            pr = stops[i - 1][0]
            pcol = stops[i - 1][1]
            r0 = r - 2
            for yy in range(cy - pr, cy + pr + 1):
                for xx in range(cx - pr, cx + pr + 1):
                    d2 = (xx - cx) ** 2 + (yy - cy) ** 2
                    if r0 * r0 <= d2 <= r * r and (xx + yy) % 2 == 0:
                        c.set(xx, yy, pcol)


def mist_band(y, thick, color, seed, cover=0.75):
    rnd = random.Random(seed)
    for j in range(thick):
        yy = y + j
        for x in range(W):
            v = sin(x * 0.09 + j * 0.7 + seed) * 0.5 + 0.5
            if rnd.random() < cover * (0.4 + 0.6 * v):
                c.set(x, yy, color)

# ================= 1. SKY =================
HORIZON = 80
n = len(SKY)
for y in range(HORIZON):
    t = y / (HORIZON - 1)
    f = t * (n - 1)
    i = min(int(f), n - 2)
    lvl = int(round((f - i) * 4))
    dither_row(y, SKY[i], SKY[i + 1], lvl)

# ================= 2. STARS =================
for _ in range(240):
    x = R.randrange(W)
    y = R.randrange(0, 74)
    if (x - 92) ** 2 + (y - 30) ** 2 < 28 ** 2:
        continue
    b = R.random() * (1.0 - y / 110.0)
    col = STAR[0] if b > 0.80 else (STAR[1] if b > 0.45 else STAR[2])
    c.set(x, y, col)
for (sx, sy) in [(18, 12), (60, 8), (112, 50), (40, 40), (76, 16), (8, 52)]:
    c.set(sx, sy, STAR[0])
    c.set(sx - 1, sy, STAR[1]); c.set(sx + 1, sy, STAR[1])
    c.set(sx, sy - 1, STAR[1]); c.set(sx, sy + 1, STAR[1])

# ================= 3. MOON =================
MX, MY, MR = 92, 30, 13
glow_soft(MX, MY, [(30, MGLOW[0]), (25, MGLOW[1]), (20, MGLOW[2])])
c.circle(MX, MY, MR, MOON[1])
c.circle(MX + 1, MY - 1, MR - 1, MOON[0])
for (cx, cy, r) in [(87, 25, 2), (96, 35, 3), (93, 21, 1), (88, 37, 2)]:
    c.circle(cx, cy, r, MOON[2])
    c.set(cx, cy + 1, MOON[3])
c.circle(MX - 4, MY + 4, MR - 6, MOON[1])

# ================= 4. DISTANT TREELINE =================
def distant(y_base, color, seed, rmin, rmax, ylo, yhi):
    rnd = random.Random(seed)
    x = -8
    while x < W + 8:
        r = rnd.randint(rmin, rmax)
        cy = y_base - rnd.randint(ylo, yhi)
        c.circle(x, cy, r, color)
        x += rnd.randint(5, 11)
    c.rect(0, y_base - 1, W, 6, color)

distant(78, FAR[0], 31, 5, 11, 3, 13)
distant(81, FAR[1], 92, 4, 9, 1, 8)

# ================= 5. MIST (BACK) =================
mist_band(70, 4, MIST[1], 3, 0.5)
mist_band(74, 5, MIST[2], 8, 0.45)
mist_band(79, 4, MIST[3], 13, 0.3)

# ================= 6. GROUND =================
gn = len(GROUND)
for y in range(HORIZON - 2, H):
    t = (y - (HORIZON - 2)) / (H - (HORIZON - 2) - 1)
    f = t * (gn - 1)
    i = min(int(f), gn - 2)
    lvl = int(round((f - i) * 4))
    dither_row(y, GROUND[i], GROUND[i + 1], lvl)
for x in range(W):
    if (x + 80) % 3:
        c.set(x, HORIZON - 2, MIST[3])

rnd = random.Random(5)
for _ in range(1300):
    x = rnd.randrange(W)
    y = rnd.randrange(HORIZON, H)
    d = (y - HORIZON) / (H - HORIZON)
    col = GROUND[4] if rnd.random() < 0.35 * (1 - d) else (GROUND[5] if rnd.random() < 0.3 else None)
    if col:
        c.set(x, y, col)

# ================= 7. MID TREES (behind cottage) =================
tapered(bez((10, 100), (4, 78), (20, 62), (12, 34), 40), 11, 4, TRUNK[0])
tapered(bez((12, 60), (22, 50), (28, 44), (40, 36), 24), 5, 2, TRUNK[0])
tapered(bez((12, 66), (4, 56), (0, 48), (-4, 40), 20), 4, 2, TRUNK[0])
leafmass(38, 30, 16, 11, 21, LEAF[4], LEAF[5], LEAF[6])
leafmass(8, 28, 14, 11, 22, LEAF[0], LEAF[1], LEAF[2])
leafmass(22, 18, 13, 9, 23, LEAF[4], LEAF[0], LEAF[1])

tapered(bez((116, 104), (122, 82), (110, 66), (118, 40), 40), 10, 4, TRUNK[0])
tapered(bez((116, 62), (106, 54), (100, 48), (92, 44), 22), 4, 2, TRUNK[0])
leafmass(114, 34, 14, 11, 41, LEAF[4], LEAF[5], LEAF[6])
leafmass(126, 50, 11, 11, 42, LEAF[0], LEAF[1], LEAF[3])

# ================= 8. WARM GLOW POOL (behind cottage) =================
glow_soft(52, 92, [(34, WGLOW[4]), (27, WGLOW[3]), (21, WGLOW[2]), (15, WGLOW[1])])

# ================= 9. COTTAGE =================
# --- roof ---
c.path("M 52 18 C 46 34 28 52 8 68 L 8 76 L 96 76 L 96 68 C 76 52 58 34 52 18 Z",
       THATCH[0])
# lit right slope
c.path("M 52 18 C 58 34 76 52 96 68 L 96 76 L 52 76 Z", THATCH[1])
# thatch courses: short dashes following horizontal rows
rnd = random.Random(11)
for y in range(24, 74, 3):
    t = (y - 18) / 52.0
    xL = int(52 - 45 * t)
    xR = int(52 + 45 * t)
    x = xL + rnd.randint(0, 3)
    while x < xR:
        ln = rnd.randint(3, 7)
        if x + ln > 52 and x < 52:
            x = 52
        col = THATCH[1] if x + ln <= 52 else THATCH[2]
        if rnd.random() < 0.75:
            c.rect(max(9, x), y, min(ln, xR - x), 1, col)
        x += ln + rnd.randint(2, 5)
# ridge cap
for i in range(-2, 3):
    c.circle(52 + i, 19 + abs(i) // 2, 1, THATCH[2])
# moonlit right roof edge
epts = bez((52, 18), (58, 34), (76, 52), (96, 68), 46)
for i, (x, y) in enumerate(epts):
    c.set(int(round(x)), int(round(y)), MIST[3] if i % 2 == 0 else THATCH[2])
# scalloped eave
for x in range(9, 97, 4):
    c.circle(x, 75, 2, THATCH[1] if x > 52 else THATCH[0])

# moss patches on roof (irregular clumps)
moss_spots = [(18, 66, 6, 3), (29, 56, 5, 3), (39, 46, 4, 2), (46, 35, 4, 2),
              (52, 24, 4, 2), (60, 38, 4, 2), (70, 50, 5, 3), (82, 62, 6, 3),
              (91, 70, 5, 2), (64, 64, 4, 2), (34, 68, 4, 2), (47, 48, 3, 2)]
rnd = random.Random(17)
for (mx, my, rx, ry) in moss_spots:
    c.ellipse(mx, my, rx, ry, MOSS[1])
    c.ellipse(mx - 1, my - 1, max(1, rx - 2), max(1, ry - 1), MOSS[2])
    for _ in range(rx + 2):
        c.set(mx + rnd.randint(-rx, rx), my - rnd.randint(ry - 1, ry + 1), MOSS[3])
    for _ in range(rx):
        c.set(mx + rnd.randint(-rx, rx), my + rnd.randint(ry, ry + 1), MOSS[0])
    for _ in range(rx):
        c.set(mx + rnd.randint(-rx - 2, rx + 2), my + rnd.randint(-1, 1), MOSS[2])

# eave shadow band
c.rect(8, 74, 89, 1, THATCH[0])
c.rect(8, 73, 89, 1, WOOD[0])

# --- walls ---
WX0, WY0, WX1, WY1 = 22, 74, 82, 98
stone_fill(WX0, WY0, WX1, WY1, STONE[1:4], STONE[0], seed=5, bh=4, bw=9)
for y in range(WY0, WY1 + 1):
    for x in range(WX0, WX0 + 6):
        if (x + y) % 3 == 0:
            c.set(x, y, STONE[0])
for x in [WX0, WX0 + 1, 41, 42, 62, 63, WX1 - 1, WX1]:
    c.rect(x, WY0, 1, WY1 - WY0 + 1, WOOD[1])
c.rect(WX0, WY0, WX1 - WX0 + 1, 2, WOOD[1])
c.rect(WX0, WY1 - 1, WX1 - WX0 + 1, 2, WOOD[0])
c.line(24, 96, 40, 78, WOOD[1])
c.line(80, 96, 64, 78, WOOD[1])

# gable planks
for y in range(58, 76):
    half = int((y - 56) * 1.0)
    x0 = max(WX0, 52 - half)
    x1 = min(WX1, 52 + half)
    if x1 > x0:
        c.rect(x0, y, x1 - x0 + 1, 1, WOOD[2] if (y % 4) < 2 else WOOD[1])

# --- door ---
DX0, DX1, DY1 = 46, 58, 98
c.rect(DX0, 80, DX1 - DX0 + 1, DY1 - 80 + 1, WOOD[0])
c.path("M 46 84 A 6 6 0 0 1 58 84 L 58 98 L 46 98 Z", WOOD[2])
for x in range(DX0 + 1, DX1, 3):
    c.line(x, 82, x, DY1, WOOD[1])
c.rect(DX0, 80, DX1 - DX0 + 1, 1, WOOD[3])
c.line(DX0 - 1, 84, DX0 - 1, DY1, WOOD[0])
c.line(DX1 + 1, 84, DX1 + 1, DY1, WOOD[0])
c.rect(DX0 + 1, DY1 - 1, DX1 - DX0 - 1, 1, LIGHT[2])
c.set(57, 90, LIGHT[2])

# --- windows ---
def window(x0, y0, w, h):
    c.rect(x0 - 1, y0 - 1, w + 2, h + 2, WOOD[0])
    c.rect(x0, y0, w, h, LIGHT[3])
    c.rect(x0, y0, w, h - 2, LIGHT[2])
    c.rect(x0 + 1, y0 + 1, w - 2, h - 4, LIGHT[1])
    c.rect(x0 + 1, y0 + 1, w - 3, h - 5, LIGHT[0])
    c.rect(x0 + w // 2, y0, 1, h, WOOD[0])
    c.rect(x0, y0 + h // 2, w, 1, WOOD[0])
    c.rect(x0 - 2, y0 + h + 1, w + 4, 1, STONE[3])

window(27, 79, 12, 11)
window(65, 79, 12, 11)

# warm halo on walls around windows
rnd = random.Random(43)
for (wx, wy) in [(33, 84), (71, 84)]:
    for _ in range(70):
        a = rnd.random() * 6.2831
        rr = rnd.uniform(7, 10)
        x = int(wx + cos(a) * rr)
        y = int(wy + sin(a) * rr * 0.8)
        if WX0 <= x <= WX1 and WY0 <= y <= WY1 and rnd.random() < 0.7:
            c.set(x, y, WGLOW[1])
    for _ in range(40):
        a = rnd.random() * 6.2831
        rr = rnd.uniform(10, 13)
        x = int(wx + cos(a) * rr)
        y = int(wy + sin(a) * rr * 0.8)
        if WX0 <= x <= WX1 and WY0 <= y <= WY1 and rnd.random() < 0.3:
            c.set(x, y, WGLOW[2])

# --- lantern beside the door ---
c.line(43, 76, 43, 79, WOOD[0])
c.rect(41, 80, 4, 5, WOOD[0])
c.rect(42, 81, 2, 3, LIGHT[1])
c.set(42, 81, LIGHT[0])
c.set(43, 82, LIGHT[0])
c.rect(41, 79, 4, 1, WOOD[3])
rnd = random.Random(47)
for _ in range(14):
    c.set(43 + rnd.randint(-3, 3), 86 + rnd.randint(0, 3), WGLOW[1])

# gable round window
c.circle(52, 66, 4, WOOD[0])
c.circle(52, 66, 3, LIGHT[2])
c.circle(52, 65, 2, LIGHT[0])
c.set(52, 66, WOOD[0])

# --- chimney ---
stone_fill(68, 34, 78, 60, STONE[1:4], STONE[0], seed=19, bh=4, bw=6)
c.rect(66, 32, 15, 3, STONE[3])
c.rect(66, 32, 15, 1, STONE[4])
c.rect(69, 35, 9, 2, WOOD[0])
rnd = random.Random(23)
for i in range(52):
    t = i / 52.0
    yy = int(30 - t * 26)
    xx = int(73 + sin(t * 4.5) * (2 + t * 9))
    col = MIST[3] if t < 0.4 else (MIST[2] if t < 0.75 else MIST[1])
    spread = 1 + int(t * 3)
    for _ in range(6):
        c.set(xx + rnd.randint(-spread, spread),
              yy + rnd.randint(-1, 1), col)
    if t < 0.35:
        c.set(xx + rnd.randint(-1, 1), yy, MIST[4])

# ================= 10. LIGHT SPILL ON GROUND =================
def spill(cx, cy, rx, ry, colors):
    for i, col in enumerate(colors):
        c.ellipse(cx, cy + i, max(1, rx - i * 3), max(1, ry - i), col)

spill(33, 100, 10, 3, [WGLOW[2], WGLOW[3], WGLOW[4]])
spill(71, 100, 10, 3, [WGLOW[2], WGLOW[3], WGLOW[4]])
spill(52, 101, 10, 4, [WGLOW[1], WGLOW[2], WGLOW[3], WGLOW[4]])
# warm kiss on slabs nearest the door (applied after path below)
rnd = random.Random(29)
for _ in range(18):
    c.set(rnd.randint(26, 40), rnd.randint(98, 101), WGLOW[2])
    c.set(rnd.randint(64, 78), rnd.randint(98, 101), WGLOW[2])

# ================= 11. STONE SLAB PATH =================
rnd = random.Random(37)
def path_row(cy, cx, halfw, h):
    x = cx - halfw
    while x < cx + halfw:
        w = rnd.randint(6, 11)
        a = max(cx - halfw, x)
        b = min(cx + halfw, x + w - 2)
        if b > a:
            col = rnd.choice([STONE[2], STONE[2], STONE[3]])
            c.rect(a, cy, b - a + 1, h, col)
            c.rect(a, cy, b - a + 1, 1, STONE[4])
            for _ in range(3):
                c.set(rnd.randint(a, b), rnd.randint(cy + 1, cy + h - 1), STONE[1])
        x += w

rows = [(99, 52, 9, 3), (103, 54, 11, 3), (107, 56, 13, 4),
        (112, 59, 15, 4), (117, 62, 18, 4), (122, 66, 21, 5)]
for (cy, cx, hw, h) in rows:
    path_row(cy, cx, hw, h)

# warm light fading down the path from the door
for (y0, y1, p1, p2, x0, x1) in [(99, 102, 0.9, 0.5, 44, 60),
                                 (103, 106, 0.5, 0.25, 43, 65),
                                 (107, 111, 0.28, 0.1, 44, 70)]:
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            d = abs(x - 52) / 10.0
            p = (p1 + (p2 - p1) * (y - y0) / max(1, y1 - y0)) * max(0.0, 1 - d)
            r = rnd.random()
            if r < p * 0.35:
                c.set(x, y, WGLOW[1])
            elif r < p:
                c.set(x, y, WGLOW[2])

# ================= 12. STONE WELL + WOODEN WINCH =================
WCX, WCY = 101, 112
c.ellipse(WCX, WCY + 6, 16, 4, GROUND[0])
stone_fill(WCX - 12, WCY - 5, WCX + 12, WCY + 6, STONE[2:5], STONE[1], seed=53, bh=4, bw=7)
c.ellipse(WCX, WCY - 5, 12, 4, STONE[3])
c.ellipse(WCX, WCY - 6, 11, 3, STONE[4])
c.ellipse(WCX, WCY - 5, 9, 3, '#150d1c')
c.ellipse(WCX, WCY - 4, 8, 2, GROUND[0])
rnd = random.Random(61)
for _ in range(34):
    x = rnd.randint(WCX - 12, WCX + 12)
    y = rnd.randint(WCY - 6, WCY + 5)
    c.set(x, y, rnd.choice([MOSS[1], MOSS[2], MOSS[0]]))
# posts
c.rect(WCX - 12, WCY - 28, 3, 24, WOOD[2])
c.rect(WCX - 12, WCY - 28, 1, 24, WOOD[3])
c.rect(WCX + 9, WCY - 28, 3, 24, WOOD[1])
c.rect(WCX + 11, WCY - 28, 1, 24, WOOD[0])
# crossbeam
c.rect(WCX - 14, WCY - 31, 29, 3, WOOD[2])
c.rect(WCX - 14, WCY - 31, 29, 1, WOOD[3])
c.rect(WCX - 14, WCY - 29, 29, 1, WOOD[0])
# winch drum
c.rect(WCX - 9, WCY - 25, 18, 4, WOOD[3])
c.rect(WCX - 9, WCY - 25, 18, 1, WOOD[4])
c.rect(WCX - 9, WCY - 22, 18, 1, WOOD[0])
c.rect(WCX - 11, WCY - 26, 2, 6, WOOD[1])
c.rect(WCX + 9, WCY - 26, 2, 6, WOOD[1])
c.line(WCX + 11, WCY - 23, WCX + 16, WCY - 20, WOOD[3])
c.rect(WCX + 15, WCY - 22, 2, 4, WOOD[4])
# rope + bucket
c.line(WCX - 1, WCY - 21, WCX - 1, WCY - 12, WOOD[4])
c.rect(WCX - 4, WCY - 12, 6, 6, WOOD[2])
c.rect(WCX - 4, WCY - 12, 6, 1, WOOD[3])
c.line(WCX - 4, WCY - 13, WCX + 1, WCY - 13, WOOD[1])
c.rect(WCX + 12, WCY - 5, 1, 12, STONE[4])
# cool moonlight pool around the well
c.ellipse(WCX, WCY + 8, 18, 5, MIST[0])
rnd = random.Random(67)
for _ in range(60):
    x = rnd.randint(WCX - 17, WCX + 17)
    y = rnd.randint(WCY + 4, WCY + 12)
    if ((x - WCX) / 18.0) ** 2 + ((y - WCY - 8) / 5.0) ** 2 <= 1 and rnd.random() < 0.5:
        c.set(x, y, MIST[1])
# moonlit top of right post and beam end
c.rect(WCX + 11, WCY - 28, 1, 10, WOOD[3])
c.rect(WCX + 8, WCY - 31, 7, 1, WOOD[4])

# ================= 13. FOREGROUND TREES (framing) =================
ptsL = bez((-2, 130), (10, 104), (2, 78), (16, 44), 60)
tapered(ptsL, 20, 7, TRUNK[1])
tapered(ptsL, 14, 4, TRUNK[2])
rnd = random.Random(71)
for i in range(58):
    x, y = ptsL[i]
    for _ in range(3):
        c.set(int(x) + rnd.randint(-5, 4), int(y) + rnd.randint(-1, 1),
              TRUNK[3] if rnd.random() < .4 else TRUNK[0])
for (p0, p1, p2, p3, w0, w1) in [
        ((10, 92), (22, 84), (30, 74), (42, 64), 6, 2),
        ((6, 74), (-4, 62), (-8, 52), (-10, 40), 5, 2),
        ((14, 56), (26, 46), (38, 40), (50, 28), 5, 2),
        ((16, 46), (14, 32), (20, 20), (30, 8), 4, 2)]:
    tapered(bez(p0, p1, p2, p3, 26), w0, w1, TRUNK[1])

ptsR = bez((128, 130), (120, 106), (126, 84), (116, 56), 50)
tapered(ptsR, 15, 6, TRUNK[1])
tapered(ptsR, 9, 3, TRUNK[2])
for (p0, p1, p2, p3, w0, w1) in [
        ((122, 96), (112, 90), (104, 84), (94, 80), 5, 2),
        ((120, 74), (112, 66), (104, 62), (96, 56), 4, 2),
        ((117, 60), (122, 46), (126, 36), (128, 24), 4, 2)]:
    tapered(bez(p0, p1, p2, p3, 24), w0, w1, TRUNK[1])

# moonlit rim on right side of left tree trunk
for i in range(0, 60, 2):
    x, y = ptsL[i]
    w = 20 + (7 - 20) * (i / 59.0)
    c.set(int(round(x + w / 2.0 - 1)), int(round(y)), TRUNK[3])
# moonlit rim on right tree
for i in range(0, 50, 2):
    x, y = ptsR[i]
    w = 15 + (6 - 15) * (i / 49.0)
    c.set(int(round(x - w / 2.0 + 1)), int(round(y)), TRUNK[3])

# ================= 14. LEAF CANOPIES (framing corners) =================
leafmass(14, 12, 18, 13, 101, LEAF[4], LEAF[0], LEAF[1])
leafmass(34, 4, 14, 9, 102, LEAF[0], LEAF[1], LEAF[2])
leafmass(2, 30, 13, 11, 103, LEAF[4], LEAF[5], LEAF[6])
leafmass(122, 10, 15, 12, 111, LEAF[4], LEAF[0], LEAF[1])
leafmass(104, 2, 12, 8, 112, LEAF[0], LEAF[1], LEAF[3])
leafmass(126, 32, 12, 11, 113, LEAF[4], LEAF[5], LEAF[6])
leafmass(112, 60, 10, 8, 115, LEAF[4], LEAF[0], LEAF[3])
leafmass(96, 54, 9, 6, 117, LEAF[0], LEAF[1], LEAF[2])

# moonlight kiss on canopy edges facing the moon
rnd = random.Random(141)
for (cx, cy, rx, ry, hi, a0, a1) in [
        (122, 10, 15, 12, LEAF[3], 2.3, 4.0), (126, 32, 12, 11, LEAF[3], 2.3, 4.0),
        (112, 60, 10, 8, LEAF[3], 2.3, 4.0), (96, 54, 9, 6, LEAF[2], 2.3, 4.0),
        (34, 4, 14, 9, LEAF[2], -0.9, 0.9), (14, 12, 18, 13, LEAF[6], -0.9, 0.9),
        (2, 30, 13, 11, LEAF[6], -0.9, 0.9)]:
    for _ in range(int(rx * 1.8)):
        a = rnd.uniform(a0, a1)
        x = int(cx + cos(a) * rx * rnd.uniform(0.7, 1.0))
        y = int(cy + sin(a) * ry * rnd.uniform(0.7, 1.0))
        c.set(x, y, hi)

# hanging leaf sprigs on the sides only
rnd = random.Random(131)
for _ in range(90):
    side = rnd.choice([0, 1])
    x = rnd.randrange(0, 46) if side == 0 else rnd.randrange(84, 128)
    y = rnd.randrange(0, 34 if side == 0 else 26)
    c.set(x, y, rnd.choice([LEAF[1], LEAF[2], LEAF[0], LEAF[5]]))

# ================= 15. FOREGROUND BUSHES / FERNS =================
rnd = random.Random(151)
for bx in range(-4, W + 4, 7):
    by = H - rnd.randint(0, 5)
    for _ in range(9):
        a = rnd.uniform(3.4, 6.0)
        rr = rnd.uniform(2, 9)
        x = int(bx + cos(a) * rr)
        y = int(by + sin(a) * rr * 0.7)
        c.set(x, y, rnd.choice([MOSS[0], MOSS[1], GROUND[5], LEAF[4]]))
for i in range(14):
    x0 = rnd.randint(0, 34)
    for j in range(8):
        c.set(x0 + j, H - 2 - j * 2 + rnd.randint(-1, 1), MOSS[1] if j % 2 else MOSS[0])

def mushroom(x, y, s=1):
    c.rect(x, y, 1, 3, SHROOM[1])
    c.ellipse(x, y - 1, 2 + s, 2, SHROOM[0])
    c.set(x - 1, y - 2, SHROOM[1])
    c.set(x + 1, y - 2, SHROOM[1])
    c.set(x, y - 3, SHROOM[1])

for (mx, my, s) in [(24, 118, 1), (30, 122, 0), (86, 122, 1), (92, 126, 0),
                    (14, 108, 0), (118, 104, 0), (76, 116, 0)]:
    mushroom(mx, my, s)

# ================= 16. FRONT MIST =================
mist_band(94, 3, MIST[2], 173, 0.22)
mist_band(103, 3, MIST[1], 181, 0.22)
mist_band(116, 4, MIST[2], 191, 0.16)
mist_band(86, 3, MIST[3], 197, 0.18)

# ================= 17. FIREFLIES =================
rnd = random.Random(211)
placed = 0
while placed < 14:
    x = rnd.randrange(4, 124)
    y = rnd.randrange(70, 124)
    if 20 <= x <= 84 and 72 <= y <= 100:
        continue
    c.set(x, y, LIGHT[0])
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if rnd.random() < 0.5:
            c.set(x + dx, y + dy, LIGHT[2])
    placed += 1

# ================= 18. MOONLIT RIM HIGHLIGHTS =================
for (x, y) in [(96, 70), (95, 68), (94, 66), (93, 64), (92, 62)]:
    c.set(x, y, MIST[3])
c.rect(82, 74, 1, 25, STONE[3])
for y in range(74, 99, 3):
    c.set(82, y, STONE[4])
# cool moonlight streak across right roof slope
rnd = random.Random(83)
for i in range(40):
    t = rnd.uniform(0.15, 0.95)
    x = int(52 + t * 44)
    y = int(18 + t * 50 + rnd.uniform(0, 6))
    if rnd.random() < 0.5:
        c.set(x, y, MIST[2])
# faint warm edge along left roof slope (light from windows below)
for i in range(30):
    t = rnd.uniform(0.4, 1.0)
    x = int(52 - t * 44)
    y = int(18 + t * 50 + rnd.uniform(-1, 2))
    if rnd.random() < 0.35:
        c.set(x, y, WGLOW[3])

print(c.stats_text())
view(c)
save("magic_forest_cottage", c)
finish(c)
