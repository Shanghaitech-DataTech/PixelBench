import math
from math import hypot, atan2, cos, sin, pi, exp, radians, degrees

W = H = 64
c = new_canvas(W, H, background=None, name="watch")

def reg(h):
    return c.color(h)

GOLD  = [reg(h) for h in ('#1a1006', '#2b1a08', '#40270c', '#5a3a11', '#774f17',
                          '#95651f', '#b3812b', '#cc9c3e', '#e3bb60', '#f5d98d', '#fff3c4')]
STEEL = [reg(h) for h in ('#080e13', '#131e26', '#22313b', '#354c5a', '#4f6d7d', '#7899a9', '#aac8d6')]
RUBY  = [reg(h) for h in ('#3a0710', '#77121f', '#b02331', '#e04a48', '#ff9a8a')]
INK   = [reg(h) for h in ('#05070a', '#0a0e12', '#10171c', '#17222a', '#1f2f39', '#2b404c')]

BAYER = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))

def ramp(colors, v, x, y):
    n = len(colors) - 1
    if v <= 0.0:
        return colors[0]
    if v >= 1.0:
        return colors[n]
    f = v * n
    i = int(f)
    if (f - i) > (BAYER[y & 3][x & 3] + 0.5) / 16.0:
        i += 1
    return colors[i if i < n else n]

def seg_d(px, py, x0, y0, x1, y1):
    vx = x1 - x0; vy = y1 - y0
    wx = px - x0; wy = py - y0
    L2 = vx * vx + vy * vy
    t = (wx * vx + wy * vy) / L2
    t = 0.0 if t < 0 else (1.0 if t > 1 else t)
    return hypot(px - (x0 + t * vx), py - (y0 + t * vy)), t

def wrap(a):
    return atan2(sin(a), cos(a))

CX, CY = 37.0, 35.0
R_OUT  = 20.9
R_BEZ  = 17.6
R_CH   = 14.5
LA     = -2.30


# ---------------------------------------------------------------- bezel
def bezel_px(px, py, x, y):
    dx = px - CX; dy = py - CY
    r = hypot(dx, dy); a = atan2(dy, dx)
    da = wrap(a - LA)
    lit = max(0.0, cos(da))
    drk = max(0.0, -cos(da))
    if r > R_OUT - 0.95:                      # outer silhouette rim
        v = 0.13 + 0.62 * lit * lit
        rl = 0.46 * exp(-(wrap(da - pi) ** 2) / 0.10)     # reflected rim light
        if r > R_OUT - 0.42:
            v = v * 0.50 + rl
        else:
            v = v + 0.45 * rl
        return ramp(GOLD, v, x, y)
    rr = (r - R_BEZ) / ((R_OUT - 0.95) - R_BEZ)
    v = 0.26 + 0.50 * (lit ** 0.9) + 0.10 * sin(pi * rr) - 0.10 * drk
    v += 0.50 * exp(-((rr - 0.50) ** 2) / 0.03) * (lit ** 3.0)
    v += 0.90 * exp(-(da * da) / 0.030 - ((rr - 0.50) ** 2) / 0.020)
    if rr < 0.13:
        v *= 0.45
    if rr > 0.93:
        v *= 0.60
    return ramp(GOLD, v, x, y)


# ---------------------------------------------------------------- chapter ring
def chapter_px(px, py, x, y):
    dx = px - CX; dy = py - CY
    r = hypot(dx, dy); a = atan2(dy, dx)
    da = wrap(a - LA)
    lit = max(0.0, cos(da))
    v = 0.04 + 0.62 * (lit ** 8) + 0.10 * lit
    base = ramp(INK, v, x, y)
    deg = (degrees(a) + 90.0) % 360.0
    k = int(round(deg / 6.0))
    d = abs(deg - 6.0 * k)
    arcw = radians(d) * r
    if k % 5 == 0:
        w = 0.95; r_in = R_CH + 0.50
    else:
        w = 0.24; r_in = R_CH + 1.10
    if arcw < w and r > r_in:
        tv = 0.52 + 0.44 * lit
        return ramp(GOLD, tv, x, y)
    if r < R_CH + 0.42:
        return ramp(GOLD, 0.16 + 0.56 * lit, x, y)   # gold flange round the movement
    return base


# ---------------------------------------------------------------- gears
GEARS = [
    dict(cx=32.5, cy=39.0, r=7.0, tip=1.7, teeth=12, hub=2.2, spokes=5, hole=True,
         phase=0.10, sph=0.40, z=0),
    dict(cx=30.5, cy=28.5, r=4.2, tip=1.2, teeth=9,  hub=1.6, spokes=4, hole=False,
         phase=0.55, sph=0.20, z=1),
    dict(cx=36.0, cy=25.0, r=2.9, tip=1.0, teeth=7,  hub=1.2, spokes=3, hole=False,
         phase=1.10, sph=0.60, z=2),
    dict(cx=42.5, cy=32.5, r=5.2, tip=1.4, teeth=10, hub=1.8, spokes=4, hole=False,
         phase=0.30, sph=0.90, z=3),
    dict(cx=44.5, cy=41.5, r=3.8, tip=1.1, teeth=8,  hub=1.4, spokes=4, hole=False,
         phase=0.80, sph=0.30, z=4),
]
GEARS.sort(key=lambda g: g['z'])

def build_gear(g):
    cells = {}
    sil = set()
    R = g['r'] + g['tip'] + 0.9
    x0 = max(0, int(g['cx'] - R)); x1 = min(W - 1, int(g['cx'] + R) + 1)
    y0 = max(0, int(g['cy'] - R)); y1 = min(H - 1, int(g['cy'] + R) + 1)
    rt = g['r'] + g['tip']
    rimin = g['r'] * 0.58
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            px = x + 0.5; py = y + 0.5
            dx = px - g['cx']; dy = py - g['cy']
            r = hypot(dx, dy)
            if r > rt:
                continue
            a = atan2(dy, dx)
            per = 2 * pi / g['teeth']
            u = ((a + g['phase']) % per) / per
            tooth = u < 0.5
            if (not tooth) and r > g['r']:
                continue
            sil.add((x, y))
            if r <= g['hub']:
                mat = 0
            elif r < rimin and g['hole']:
                if abs(cos((g['spokes'] / 2.0) * (a + g['sph']))) > 0.52:
                    mat = 1
                else:
                    continue
            else:
                mat = 2
            cells[(x, y)] = (mat, r, a, tooth)
    outline = set()
    for (x, y) in sil:
        for (ox, oy) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (ox, oy) not in sil and 0 <= ox < W and 0 <= oy < H:
                outline.add((ox, oy))
    return cells, outline

def gear_colour(g, mat, r, a, tooth, x, y):
    lit = max(0.0, cos(wrap(a - LA)))
    v = 0.33 + 0.46 * (lit ** 0.85)
    rt = g['r'] + g['tip']; rimin = g['r'] * 0.58
    if mat == 2:
        band = (r - rimin) / max(0.001, rt - rimin)
        v += 0.10 * sin(pi * min(1.0, max(0.0, band)))
        v += 0.26 * exp(-((r - (rt - 1.15)) ** 2) / 0.55) * (lit ** 2.4)
        v -= 0.10 * exp(-((r - (rt - 2.4)) ** 2) / 0.35)
    elif mat == 0:
        v += 0.08
    else:
        v -= 0.05
    if tooth and r > g['r'] + 0.30:
        v += 0.20
    if r > rt - 0.70:
        v *= 0.55
    if r < g['hub'] * 0.45:
        v *= 0.35
    return ramp(GOLD, v, x, y)

GEARLIST = []
for g in GEARS:
    cells, outline = build_gear(g)
    GEARLIST.append((g, cells, outline))

PIVOTS = ((32.5, 39.0, 1), (42.5, 32.5, 1), (30.5, 28.5, 0), (36.0, 25.0, 0), (44.5, 41.5, 0))
SCREWS = ((46.0, 25.0), (26.0, 33.0))

def pivot_colour(px, py, x, y):
    for (pcx, pcy, isjewel) in PIVOTS:
        d = hypot(px - pcx, py - pcy)
        if d <= 2.20:
            a = atan2(py - pcy, px - pcx)
            lit = max(0.0, cos(wrap(a - LA)))
            if isjewel:
                if d <= 0.78:
                    return RUBY[0]
                if d <= 1.38:
                    return ramp(RUBY, 0.40 + 0.50 * lit, x, y)
                return ramp(GOLD, 0.40 + 0.45 * lit, x, y)
            if d <= 0.72:
                return STEEL[0]
            if d <= 1.38:
                return ramp(STEEL, 0.35 + 0.45 * lit, x, y)
    return None

def screw_colour(px, py, x, y):
    for (scx, scy) in SCREWS:
        d = hypot(px - scx, py - scy)
        if d <= 1.75:
            a = atan2(py - scy, px - scx)
            lit = max(0.0, cos(wrap(a - LA)))
            if d <= 0.95:
                return STEEL[1]
            return ramp(STEEL, 0.30 + 0.50 * lit, x, y)
    return None


# ---------------------------------------------------------------- hands
HANDS = ((62.0, 13.3), (298.0, 8.5))

def hands_px(px, py, x, y):
    d0 = hypot(px - CX, py - CY)
    if d0 <= 1.00:
        return GOLD[9]
    if d0 <= 1.70:
        return GOLD[5]
    for (ang, ln) in HANDS:
        th = radians(ang)
        ex = CX + ln * sin(th); ey = CY - ln * cos(th)
        d, t = seg_d(px, py, CX, CY, ex, ey)
        w = 0.50 + 0.70 * (1.0 - t) ** 2
        if d <= w:
            ux = ex - CX; uy = ey - CY
            nl = hypot(ux, uy)
            nx = -uy / nl; ny = ux / nl
            side = (px - CX) * nx + (py - CY) * ny
            dot = nx * (-0.71) + ny * (-0.71)
            bright = (side * dot) >= 0
            v = 0.70 if bright else 0.22
            if t > 0.90:
                v = 1.0
            return ramp(STEEL, v, x, y)
    return None


# ---------------------------------------------------------------- lid
LTH = radians(-10.0)
LC_, LS_ = cos(LTH), sin(LTH)
LCX, LCY = 9.0, 35.0
LRX, LRY = 7.2, 19.5

def lid_px(px, py, x, y):
    dx = px - LCX; dy = py - LCY
    lx = LC_ * dx + LS_ * dy
    ly = -LS_ * dx + LC_ * dy
    qx = lx / LRX; qy = ly / LRY
    e = qx * qx + qy * qy
    if e > 1.0:
        return None
    a = atan2(qy, qx)
    lit = max(0.0, cos(wrap(a - (LA - LTH))))
    if e > 0.80:
        v = 0.24 + 0.58 * (lit ** 1.05) + 0.12 * sin(pi * (e - 0.80) / 0.20)
        return ramp(GOLD, v, x, y)
    rr = e / 0.80
    v = 0.23 + 0.34 * lit - 0.06 * rr
    if abs(rr - 0.66) < 0.055:
        v -= 0.20
    if rr < 0.30:
        v += 0.12
    v += 0.38 * exp(-((lx + 4.4) / 1.1) ** 2)
    v -= 0.12 * exp(-((lx - 4.2) / 1.2) ** 2)
    return ramp(GOLD, max(0.0, v), x, y)


# ---------------------------------------------------------------- bow
def bow_px(px, py, x, y):
    dx = px - CX; dy = py - 8.0
    q = (dx / 3.2) ** 2 + (dy / 3.7) ** 2
    if q > 1.0 or q < 0.36:
        return None
    a = atan2(dy, dx)
    lit = max(0.0, cos(wrap(a - LA)))
    return ramp(GOLD, 0.24 + 0.52 * (lit ** 1.2), x, y)


# ---------------------------------------------------------------- base layer
def base_pixel(x, y):
    px = x + 0.5; py = y + 0.5
    b = bow_px(px, py, x, y)
    if b is not None:
        return b
    dx = px - CX; dy = py - CY
    r = hypot(dx, dy)
    if r <= R_OUT:
        if r > R_BEZ:
            return bezel_px(px, py, x, y)
        if r > R_CH:
            return chapter_px(px, py, x, y)
        n = 0.5 + 0.5 * sin(px * 1.9 + py * 0.8) * cos(py * 1.5 - px * 0.6)
        return ramp(INK, 0.09 + 0.15 * n - 0.05 * (r / R_CH), x, y)
    r2 = hypot(px - (CX - 1.0), py - (CY - 1.0))
    if r2 <= R_OUT:
        return ramp(INK, 0.08, x, y)
    return lid_px(px, py, x, y)

buf = [[base_pixel(x, y) for x in range(W)] for y in range(H)]

def in_movement(x, y):
    return hypot(x + 0.5 - CX, y + 0.5 - CY) < R_CH - 0.10

# gears with dark contour (front gears cut dark haloes over the back ones)
DARK_EDGE = GOLD[0]
for (g, cells, outline) in GEARLIST:
    for (x, y) in outline:
        if in_movement(x, y):
            buf[y][x] = DARK_EDGE
    for (x, y) in cells:
        if in_movement(x, y):
            mat, r, a, tooth = cells[(x, y)]
            buf[y][x] = gear_colour(g, mat, r, a, tooth, x, y)

# pivots and screws
for jx in range(W):
    for jy in range(H):
        if in_movement(jx, jy):
            cc = pivot_colour(jx + 0.5, jy + 0.5, jx, jy)
            if cc is None:
                cc = screw_colour(jx + 0.5, jy + 0.5, jx, jy)
            if cc is not None:
                buf[jy][jx] = cc

# hands with a soft contact shadow
mask = {}
for y in range(H):
    for x in range(W):
        hh = hands_px(x + 0.5, y + 0.5, x, y)
        if hh is not None:
            mask[(x, y)] = hh
for (x, y) in mask:
    if (x + 1, y + 1) not in mask and 0 <= x + 1 < W and 0 <= y + 1 < H:
        if buf[y + 1][x + 1] is not None and in_movement(x + 1, y + 1):
            buf[y + 1][x + 1] = DARK_EDGE
for (x, y), hh in mask.items():
    buf[y][x] = hh

for y in range(H):
    for x in range(W):
        if buf[y][x] is not None:
            c.set(x, y, buf[y][x])

# ---------------------------------------------------------------- crown
for i in range(7):
    xx = 34 + i
    v = 0.94 - 0.055 * i + (0.10 if i % 2 == 0 else -0.10)
    c.rect(xx, 10, 1, 4, ramp(GOLD, v, xx, 10))
c.rect(34, 10, 7, 1, GOLD[9])
c.rect(34, 13, 7, 1, GOLD[3])
c.rect(35, 14, 5, 1, GOLD[6])

# ---------------------------------------------------------------- hinges
for hy in (26, 45):
    c.rect(16, hy - 1, 3, 3, GOLD[4])
    c.rect(16, hy - 1, 3, 1, GOLD[7])
    c.set(17, hy - 1, GOLD[9])

# ---------------------------------------------------------------- chain
P0 = (37.0, 3.4); Pc = (52.0, 0.6); P1 = (62.0, 15.0)
samples = []
for i in range(400):
    t = i / 399.0
    xx = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * Pc[0] + t * t * P1[0]
    yy = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * Pc[1] + t * t * P1[1]
    samples.append((xx, yy))
acc = 0.0
prev = samples[0]
marks = [samples[0]]
for p in samples[1:]:
    acc += hypot(p[0] - prev[0], p[1] - prev[1])
    prev = p
    if acc >= 2.1:
        marks.append(p)
        acc = 0.0
for i, (mx, my) in enumerate(marks):
    ix = int(round(mx)); iy = int(round(my))
    if i % 2 == 0:
        c.set(ix, iy, GOLD[8])
        c.set(ix + 1, iy, GOLD[4])
    else:
        c.set(ix, iy, GOLD[8])
        c.set(ix, iy + 1, GOLD[4])

# ---------------------------------------------------------------- inspect
pal = c.palette()
legend = {}
for i in range(len(GOLD)):
    legend[GOLD[i]] = "0123456789A"[i]
for i in range(len(STEEL)):
    legend[STEEL[i]] = "abcdefg"[i]
for i in range(len(RUBY)):
    legend[RUBY[i]] = "RSTUV"[i]
for i in range(len(INK)):
    legend[INK[i]] = ".,:-=+"[i]
print("   " + "".join(str(i % 10) for i in range(W)))
out = []
for y in range(H):
    row = ""
    for x in range(W):
        i = c.get(x, y)
        row += " " if (i is None or i == 0) else legend.get(i, "?")
    out.append("%2d %s" % (y, row))
print("\n".join(out))
lum = {}
for i in range(len(pal)):
    r_, g_, b_, a_ = pal[i]['rgba']
    lum[i] = (0.30 * r_ + 0.59 * g_ + 0.11 * b_) / 255.0
tchars = " .:-=+*#%@"
print("thumbnail 32x32")
for yy in range(0, H, 2):
    row = ""
    for xx in range(0, W, 2):
        s = 0.0; n = 0
        for dy in (0, 1):
            for dx in (0, 1):
                i = c.get(xx + dx, yy + dy)
                if i is not None and i != 0:
                    s += lum[i]; n += 1
        row += " " if n == 0 else tchars[min(9, int(s / n * 10))]
    print("%2d %s" % (yy, row))
print(c.stats_text())
save("watch", c)
finish(c)
