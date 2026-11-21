import math

W = H = 64
c = new_canvas(W, H, background='#35201a')

# ---------------- palette ----------------
CL      = '#0d0706'
K1      = '#1b100c'
WALL0   = '#2a1813'
WALL1   = '#35201a'
WALL2   = '#41281e'
WALL3   = '#4e3225'
PLANK   = '#231410'
PANEL   = '#180e0a'
WOOD0   = '#3a2418'
WOOD1   = '#533220'
WOOD2   = '#6d4426'
WOOD3   = '#8a5a30'
WOOD4   = '#a6703c'
WOOD5   = '#c08d52'
AMBER   = '#e0a445'
GOLD    = '#f6cb6d'
GLOW    = '#ffe9a8'
WHITE   = '#fff8e2'
METAL   = '#3d2e24'
METAL2  = '#5f4632'
GRN0    = '#1f3d2a'
GRN1    = '#2f5c3c'
GRN2    = '#4f8a52'
BRW0    = '#6e3a1c'
BRW1    = '#a85a25'
BLU0    = '#26405c'
BLU1    = '#3a6288'
RED0    = '#6e2626'
RED1    = '#9c3a34'
GLASS   = '#a9bdb4'
SMOKE   = '#4b423a'
SMOKE2  = '#2e2724'
FLOOR0  = '#241610'
FLOOR1  = '#33211a'
FLOOR2  = '#422b20'
FOAM    = '#f2e8cf'
CERAM   = '#cbb894'
CERAM2  = '#9d8a68'
BARREL  = '#6b4326'
BARREL2 = '#82552c'
BARRELD = '#4a2d18'
OLIVE   = '#8a7a3a'
OLIVEL  = '#c9b45a'

# ---------------- helpers ----------------
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def bey(x, y):
    return (BAYER[y & 3][x & 3] + 0.5) / 16.0


def haze(cx, cy, rx, ry, col, dens, box=None):
    bx0, by0, bx1, by1 = box if box else (0, 0, W - 1, H - 1)
    for y in range(max(by0, int(cy - ry)), min(by1, int(cy + ry)) + 1):
        for x in range(max(bx0, int(cx - rx)), min(bx1, int(cx + rx)) + 1):
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            if dx * dx + dy * dy <= 1.0 and bey(x, y) < dens:
                c.set(x, y, col)


def glit(cx, cy, r, col, dmax, box=None):
    """soft radial light: dithered with linear falloff"""
    bx0, by0, bx1, by1 = box if box else (0, 0, W - 1, H - 1)
    for y in range(max(by0, int(cy - r)), min(by1, int(cy + r)) + 1):
        for x in range(max(bx0, int(cx - r)), min(bx1, int(cx + r)) + 1):
            d = math.hypot(x - cx, y - cy)
            if d < r and bey(x, y) < dmax * (1.0 - d / r):
                c.set(x, y, col)


def fade(y0, y1, col, d0, d1, x0=0, x1=W - 1):
    span = max(1, y1 - y0)
    for y in range(y0, y1 + 1):
        d = d0 + (d1 - d0) * ((y - y0) / span)
        for x in range(x0, x1 + 1):
            if bey(x, y) < d:
                c.set(x, y, col)


def halo(cx, cy, bands, box=None):
    bx0, by0, bx1, by1 = box if box else (0, 0, W - 1, H - 1)
    rmax = bands[-1][0]
    for y in range(max(by0, int(cy - rmax)), min(by1, int(cy + rmax)) + 1):
        for x in range(max(bx0, int(cx - rmax)), min(bx1, int(cx + rmax)) + 1):
            d = math.hypot(x - cx, y - cy)
            for (r, col, dens) in bands:
                if d <= r:
                    if bey(x, y) < dens:
                        c.set(x, y, col)
                    break


# =========================================================
# 1. BACK WALL
# =========================================================
c.rect(0, 0, W, H, WALL1)
c.rect(0, 0, W, 3, K1)

for (y0, y1, col) in [(6, 12, WALL1), (13, 20, WALL2), (21, 27, WALL1), (28, 33, WALL2)]:
    c.rect(0, y0, W, y1 - y0 + 1, col)
    c.line(0, y1, W - 1, y1, WALL0)
for (sx, sy0, sy1) in [(10, 6, 12), (39, 13, 20), (5, 21, 27), (53, 6, 12),
                       (45, 6, 12), (23, 13, 20), (30, 28, 33), (58, 21, 27)]:
    c.line(sx, sy0, sx, sy1, WALL0)

fade(0, 14, K1, 0.9, 0.0)

# ceiling beam
c.rect(0, 3, W, 3, WOOD0)
c.line(0, 3, W - 1, 3, WOOD1)
c.line(0, 5, W - 1, 5, CL)
c.line(0, 6, W - 1, 6, PLANK)
for bx in (16, 33, 50):
    c.line(bx, 3, bx, 5, WOOD1)

fade(27, 33, K1, 0.0, 0.22)

# lamp halos
BANDS = [(3.2, GOLD, 0.95), (5.2, AMBER, 0.55), (7.8, WOOD4, 0.45),
         (10.8, WOOD3, 0.28), (14.5, WALL3, 0.17)]
halo(8, 18, BANDS)
halo(56, 18, BANDS)
haze(32, 33, 26, 4, WOOD4, 0.11, (8, 29, 55, 34))

# smoke drifting in the dim parts of the room
haze(3, 12, 8, 6, SMOKE, 0.24, (0, 9, 12, 22))
haze(61, 13, 8, 6, SMOKE, 0.22, (51, 9, 63, 22))
haze(24, 9, 14, 2, SMOKE, 0.16, (10, 8, 38, 11))
haze(44, 26, 10, 3, SMOKE, 0.1, (34, 23, 54, 29))

# =========================================================
# 2. FLOOR
# =========================================================
c.rect(0, 49, W, H - 49, FLOOR0)
for y in (53, 57, 61):
    c.line(0, y, W - 1, y, FLOOR1)
for (sx, sy0, sy1) in [(16, 49, 53), (42, 49, 53), (8, 53, 57), (34, 53, 57),
                       (54, 53, 57), (22, 57, 61), (46, 57, 61), (10, 61, 63)]:
    c.line(sx, sy0, sx, sy1, FLOOR2)
c.line(0, 49, W - 1, 49, CL)
haze(32, 50, 33, 3, K1, 0.5, (2, 49, 61, 53))
glit(20, 58, 13, WOOD3, 0.3, (10, 55, 34, 63))
glit(46, 60, 11, WOOD3, 0.25, (36, 56, 56, 63))
fade(61, 63, K1, 0.0, 0.35)

# =========================================================
# 3. SHELF UNIT (behind the bar)
# =========================================================
for px, outer in ((14, 14), (47, 49)):
    c.rect(px, 7, 3, 22, WOOD1)
    c.line(outer, 7, outer, 28, CL)
    c.line(px + 1, 8, px + 1, 28, WOOD2)
c.rect(14, 7, 36, 1, WOOD3)
c.rect(14, 8, 36, 1, WOOD2)
c.rect(17, 9, 30, 19, PANEL)
c.line(24, 9, 24, 27, '#120a08')
c.line(38, 9, 38, 27, '#120a08')
c.rect(14, 27, 36, 1, WOOD1)
c.line(14, 28, 49, 28, CL)

for by in (16, 24):
    c.line(14, by, 49, by, WOOD4)
    c.line(14, by + 1, 49, by + 1, WOOD2)
    c.line(14, by + 2, 49, by + 2, PLANK)


def bottle(x, yb, w, h, body, lite, cap=WOOD5):
    yt = yb - h + 1
    nx = x + (w - 2) // 2
    c.rect(x, yt + 2, w, h - 2, body)
    c.rect(nx, yt + 1, 2, 1, body)
    c.rect(nx, yt, 2, 1, cap)
    c.line(x + 1, yt + 3, x + 1, yb - 1, lite)
    c.set(x + w - 1, yt + 2, CL)
    c.line(x, yb, x + w - 1, yb, CL)
    c.set(x, yt + 2, CL)


# upper shelf: bottles stand on board at y=16
bottle(19, 15, 4, 6, GRN1, GRN2, WOOD5)
bottle(23, 15, 4, 4, BRW0, BRW1, CERAM)
bottle(27, 15, 4, 6, BLU0, BLU1, METAL2)
bottle(31, 15, 4, 5, BRW1, GOLD, WOOD5)
bottle(35, 15, 4, 6, RED0, RED1, WOOD5)
bottle(40, 15, 4, 4, GRN0, GRN2, CERAM)
bottle(44, 15, 4, 5, OLIVE, OLIVEL, WOOD5)
# lower shelf: bottles stand on board at y=24
bottle(19, 23, 4, 5, BLU0, BLU1, WOOD5)
bottle(24, 23, 5, 5, GRN1, GRN2, CERAM)
bottle(30, 23, 4, 4, BRW0, BRW1, METAL2)
bottle(35, 23, 4, 5, RED0, RED1, WOOD5)
bottle(40, 23, 4, 4, OLIVE, OLIVEL, WOOD5)
bottle(44, 23, 4, 5, GRN0, GRN1, CERAM)

# =========================================================
# 4. HANGING LAMPS
# =========================================================
for cx in (8, 56):
    cy = 18
    c.rect(cx - 1, 3, 3, 2, METAL)
    c.line(cx, 5, cx, 9, METAL2)
    c.circle(cx, cy, 3, GOLD)
    c.circle(cx, cy, 2, GLOW)
    c.rect(cx - 1, cy - 2, 2, 2, WHITE)
    for i, y in enumerate(range(10, 16)):
        hw = 2 + i // 2
        c.line(cx - hw, y, cx + hw, y, WOOD0)
        c.set(cx - hw, y, METAL2 if i < 4 else CL)
        c.set(cx + hw, y, CL)
        c.set(cx - hw + 1, y, WOOD1)
    c.line(cx - 5, 15, cx + 5, 15, METAL)
    c.set(cx - 4, 15, CL)
    c.set(cx + 4, 15, CL)
    for dx in (-3, -1, 1, 3):
        c.set(cx + dx, 14, WOOD1)

# =========================================================
# 5. BAR COUNTER
# =========================================================
c.poly([(8, 34), (55, 34), (61, 38), (2, 38)], WOOD3)
c.line(8, 34, 55, 34, WOOD5)
c.line(9, 35, 54, 35, WOOD4)
for gx in (14, 22, 30, 38, 46, 53):
    c.set(gx, 36, WOOD2)
for gx in (10, 26, 34, 42, 50):
    c.set(gx, 37, WOOD2)
glit(10, 35, 15, AMBER, 0.35, (6, 34, 57, 37))
glit(53, 35, 14, AMBER, 0.3, (6, 34, 57, 37))
c.line(2, 38, 61, 38, CL)

c.rect(2, 39, 60, 10, WOOD1)
c.line(2, 39, 61, 39, WOOD0)
for gx in range(6, 62, 7):
    c.line(gx, 40, gx, 48, WOOD0)
    c.set(gx + 1, 41, WOOD2)
    c.set(gx + 1, 42, WOOD2)
c.line(2, 47, 61, 47, WOOD0)
c.line(2, 48, 61, 48, CL)
glit(9, 41, 17, WOOD2, 0.6, (2, 39, 61, 48))
glit(55, 41, 17, WOOD2, 0.55, (2, 39, 61, 48))
fade(44, 47, CL, 0.0, 0.22, 2, 61)
c.line(3, 45, 60, 45, METAL2)
c.line(3, 46, 60, 46, METAL)


def mug(x, yb, w=4, h=4):
    c.rect(x, yb - h + 1, w, h, CERAM)
    c.line(x, yb - h + 1, x, yb - 1, CERAM2)
    c.set(x + 1, yb - h + 2, WHITE)
    c.set(x - 1, yb - h + 2, CERAM)
    c.set(x - 1, yb - h + 3, CERAM2)
    c.line(x, yb, x + w - 1, yb, K1)
    c.set(x + w - 1, yb - h + 1, CL)


def glass(x, yb, w=4):
    c.rect(x, yb - 4, w, 5, AMBER)
    c.rect(x, yb - 5, w, 1, FOAM)
    c.line(x, yb - 4, x, yb, GOLD)
    c.line(x + w - 1, yb - 4, x + w - 1, yb, BRW1)
    c.line(x, yb, x + w - 1, yb, K1)
    c.set(x + w - 1, yb - 5, CERAM)


mug(10, 36)
glass(16, 36)
bottle(26, 36, 3, 5, GRN1, GRN2)
glass(44, 36)
mug(50, 36)

# candle in the middle of the bar
haze(34, 32, 5, 4, AMBER, 0.3, (29, 29, 40, 34))
c.rect(33, 33, 3, 4, CERAM)
c.line(33, 33, 33, 36, CERAM2)
c.line(35, 33, 35, 36, CERAM2)
c.line(33, 36, 35, 36, K1)
c.rect(34, 32, 1, 1, GOLD)
c.set(34, 31, GOLD)
c.set(34, 30, GLOW)

# =========================================================
# 6. BARRELS
# =========================================================


def barrel(cx, ytop, ybot, rx):
    h = ybot - ytop
    for y in range(ytop, ybot + 1):
        t = (y - ytop) / h
        w = rx * (1.0 + 0.13 * math.sin(math.pi * t))
        x0 = int(round(cx - w))
        x1 = int(round(cx + w))
        c.line(x0, y, x1, y, BARREL)
        c.set(x1, y, BARRELD)
        c.set(x0, y, CL)
        c.set(x0 + 1, y, BARREL2)
        c.set(x0 + 2, y, BARREL2 if (y % 4) else BARREL)
    c.ellipse(cx, ytop, int(rx * 0.92), 2, BARREL2)
    c.ellipse(cx, ytop, int(rx * 0.55), 1, WOOD3)
    for by in (int(ytop + h * 0.3), int(ytop + h * 0.72)):
        t = (by - ytop) / h
        w = rx * (1.0 + 0.13 * math.sin(math.pi * t))
        c.line(int(round(cx - w)), by, int(round(cx + w)), by, BARRELD)
        c.line(int(round(cx - w)), by + 1, int(round(cx + w)), by + 1, METAL)
    c.line(int(cx - rx), ybot, int(cx + rx), ybot, CL)


barrel(8, 41, 59, 6)
barrel(56, 43, 61, 5)
# tap on the left barrel
c.rect(13, 47, 3, 2, METAL)
c.set(13, 47, METAL2)
c.set(16, 48, METAL2)

# =========================================================
# 7. BAR STOOLS
# =========================================================
def stool(cx, sy):
    for dx, dr in ((-4, -2), (4, 2)):
        c.line(cx + dx, sy + 2, cx + dx + dr, 63, WOOD1)
        c.line(cx + dx + (1 if dr > 0 else -1), sy + 3, cx + dx + dr, 62, WOOD0)
        c.set(cx + dx + dr, 63, CL)
    c.line(cx, sy + 2, cx, 63, WOOD0)
    c.line(cx - 5, 59, cx + 5, 59, WOOD2)
    c.line(cx - 4, 60, cx + 4, 60, WOOD1)
    c.ellipse(cx, sy + 1, 5, 2, WOOD1)
    c.ellipse(cx, sy, 5, 2, WOOD3)
    c.line(cx - 3, sy - 2, cx + 3, sy - 2, WOOD4)
    c.line(cx - 4, sy - 1, cx - 4, sy, WOOD4)
    c.set(cx - 5, sy, CL)
    c.set(cx + 5, sy, CL)
    c.set(cx - 5, sy + 1, CL)
    c.set(cx + 5, sy + 1, CL)


stool(23, 51)
stool(41, 52)

# =========================================================
# 8. FINAL ATMOSPHERE
# =========================================================
fade(62, 63, K1, 0.0, 0.3)

# =========================================================
# debug dump
# =========================================================
CH = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
pal = c.palette()
i2ch = {}
ch2hex = {}
for i, p in enumerate(pal):
    ch = CH[i % len(CH)]
    i2ch[p['index']] = ch
    ch2hex[ch] = '#%02x%02x%02x' % tuple(p['rgba'][:3])


def dump(x0, y0, x1, y1):
    ruler = ''.join(str(x % 10) if x % 8 == 0 else (' ' if x % 2 else '.') for x in range(x0, x1 + 1))
    print('     ' + ruler)
    for y in range(y0, y1 + 1):
        s = ''
        for x in range(x0, x1 + 1):
            s += i2ch.get(c.get(x, y), '?')
            if x % 8 == 7:
                s += '|'
        print('%3d  %s' % (y, s))


print(c.stats_text())
dump(0, 0, 63, 33)
dump(0, 34, 63, 63)
print('LEGEND', ch2hex)
save('tavern', c)
finish(c)
