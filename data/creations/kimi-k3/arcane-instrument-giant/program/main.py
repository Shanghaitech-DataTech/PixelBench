import math, random

W = H = 256
CX, CY = 128, 96   # orrery centre

# ---------------- helpers ----------------
def rgb(h):
    h = h.lstrip('#')
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def hx(t):
    return '#%02x%02x%02x' % t

def mix(a, b, t):
    x, y = rgb(a), rgb(b)
    return hx(tuple(round(x[i] + (y[i] - x[i]) * t) for i in range(3)))

INK = '#0e0a18'
B_DK = '#4a3413'; B_SH = '#6e4e1c'; B_MD = '#a3762a'; B_LT = '#d3a441'; B_HI = '#f2d27e'; B_WH = '#fff3c8'
RUNE = '#57ffc8'; RUNE_DK = '#1d6e58'
CORE_O = '#ff9c38'; CORE_Y = '#ffd977'; CORE_Y2 = '#ffe98a'; CORE_W = '#ffffff'
IR_DK = '#23232c'; IR_MD = '#454550'; IR_LT = '#626272'
ST_DK = '#24242e'; ST_SH = '#383844'; ST_MD = '#50505c'; ST_LT = '#6b6b7a'; ST_HI = '#8f8fa2'
FACE = '#152438'

bg = new_canvas(W, H, name='bg')
fx = new_canvas(W, H, name='fx')
m  = new_canvas(W, H, name='machine')
tp = new_canvas(W, H, name='topfx')

# ---------------- background: dark hall ----------------
wall = [hx((6, 6, 13)), hx((10, 10, 22)), hx((15, 14, 32)), hx((20, 17, 40))]
bg.rect(0, 0, 256, 64, wall[0])
bg.rect(0, 64, 256, 64, wall[1])
bg.rect(0, 128, 256, 52, wall[2])
bg.rect(0, 180, 256, 16, wall[3])
bg.dither(0, 58, 256, 10, [wall[0], wall[1]], 'bayer4')
bg.dither(0, 122, 256, 10, [wall[1], wall[2]], 'bayer4')
bg.dither(0, 174, 256, 10, [wall[2], wall[3]], 'bayer4')

# side gothic windows
for wx in (36, 220):
    bg.circle(wx, 56, 10, '#0b0a1c')
    bg.rect(wx - 10, 56, 20, 106, '#0b0a1c')
    bg.circle(wx, 60, 7, '#161439')
    bg.rect(wx - 7, 60, 14, 98, '#161439')
    bg.circle(wx, 62, 4, '#1c1a48')
    bg.rect(wx - 4, 62, 8, 92, '#1c1a48')
    bg.line(wx, 62, wx, 156, '#0b0a1c')
    bg.rect(wx - 11, 158, 22, 4, '#0c0b1a')

# columns at edges
bg.rect(0, 0, 15, 196, '#05050c')
bg.rect(241, 0, 15, 196, '#05050c')
bg.rect(15, 0, 3, 196, '#0c0b1a')
bg.rect(238, 0, 3, 196, '#0c0b1a')
bg.rect(0, 34, 18, 6, '#0c0b1a')
bg.rect(238, 34, 18, 6, '#0c0b1a')

# huge halo arch behind machine
bg.circle(128, 112, 106, '#0c0b1e', fill=False)
bg.circle(128, 112, 101, '#0c0b1e', fill=False)

# floor
fl = [hx((20, 15, 34)), hx((28, 20, 44)), hx((37, 27, 55))]
bg.rect(0, 196, 256, 24, fl[0])
bg.rect(0, 220, 256, 18, fl[1])
bg.rect(0, 238, 256, 18, fl[2])
bg.dither(0, 216, 256, 7, [fl[0], fl[1]], 'bayer4')
bg.dither(0, 234, 256, 7, [fl[1], fl[2]], 'bayer4')
grid = '#0b0817'
for yy in (203, 211, 221, 233, 247):
    bg.line(0, yy, 255, yy, grid)
for gx in range(0, 299, 42):
    bg.line(gx, 255, 128, 197, grid)
bg.ellipse(128, 254, 56, 5, '#0a0714')

# ---------------- fx: translucent light ----------------
fx.poly([(118, 0), (138, 0), (162, 118), (94, 118)], '#ffe6a41c')
fx.circle(CX, CY, 38, '#ffd97716')
fx.circle(CX, CY, 23, '#ffdf8a34')
fx.ellipse(128, 230, 52, 11, '#ffd98a1c')
fx.rect(122, 184, 12, 13, '#ffe9a82e')
fx.rect(126, 184, 4, 13, '#fff3c44a')

# ---------------- machine ----------------
def ept(rx, ry, rot, t):
    a = math.radians(t); th = math.radians(rot)
    x0 = rx * math.cos(a); y0 = ry * math.sin(a)
    return (CX + x0 * math.cos(th) - y0 * math.sin(th),
            CY + x0 * math.sin(th) + y0 * math.cos(th))

def p_ellipse(rx, ry, rot):
    x0, y0 = ept(rx, ry, rot, 0); x1, y1 = ept(rx, ry, rot, 180)
    return ('M %.1f %.1f A %.1f %.1f %s 1 1 %.1f %.1f A %.1f %.1f %s 1 1 %.1f %.1f Z'
            % (x0, y0, rx, ry, rot, x1, y1, rx, ry, rot, x0, y0))

def p_arc(rx, ry, rot, t0, t1):
    large = 1 if (t1 - t0) > 180 else 0
    x0, y0 = ept(rx, ry, rot, t0); x1, y1 = ept(rx, ry, rot, t1)
    return 'M %.1f %.1f A %.1f %.1f %s %d 1 %.1f %.1f' % (x0, y0, rx, ry, rot, large, x1, y1)

def arcline(c, rx, ry, rot, t0, t1, col):
    c.path(p_arc(rx, ry, rot, t0, t1), col, fill=False)

def band(c, rx, ry, rot, th, t0, t1, col):
    if (t1 - t0) >= 360:
        c.path(p_ellipse(rx, ry, rot) + ' ' + p_ellipse(rx - th, ry - th, rot), col)
    else:
        large = 1 if (t1 - t0) > 180 else 0
        X0, Y0 = ept(rx, ry, rot, t0); X1, Y1 = ept(rx, ry, rot, t1)
        x1, y1 = ept(rx - th, ry - th, rot, t1); x0, y0 = ept(rx - th, ry - th, rot, t0)
        d = ('M %.1f %.1f A %.1f %.1f %s %d 1 %.1f %.1f L %.1f %.1f A %.1f %.1f %s %d 0 %.1f %.1f Z'
             % (X0, Y0, rx, ry, rot, large, X1, Y1, x1, y1, rx - th, ry - th, rot, large, x0, y0))
        c.path(d, col)

def ring(c, rx, ry, rot, th, t0=0, t1=360, eng=True):
    band(c, rx, ry, rot, th, t0, t1, B_MD)
    if (t1 - t0) >= 360:
        c.path(p_ellipse(rx, ry, rot), INK, fill=False)
        c.path(p_ellipse(rx - th, ry - th, rot), INK, fill=False)
    else:
        arcline(c, rx, ry, rot, t0, t1, INK)
        arcline(c, rx - th, ry - th, rot, t0, t1, INK)
        for tt in (t0, t1):
            X, Y = ept(rx, ry, rot, tt); x, y = ept(rx - th, ry - th, rot, tt)
            c.line(round(X), round(Y), round(x), round(y), INK)
    if eng:
        mr, my = rx - th / 2, ry - th / 2
        tt = t0 + 4
        while tt < t1 - 4:
            arcline(c, mr, my, rot, tt, min(tt + 5, t1 - 2), B_SH)
            tt += 16

def stroke_full(c, rx, ry, rot, col):
    c.path(p_ellipse(rx, ry, rot), col, fill=False)

# gears
def gear(c, cx, cy, r, teeth=8, brass=False):
    dark = B_DK if brass else INK
    mid = B_MD if brass else IR_MD
    lt = B_LT if brass else IR_LT
    for i in range(teeth):
        a = 2 * math.pi * i / teeth + math.pi / teeth
        tx = round(cx + (r - 1) * math.cos(a)) - 1
        ty = round(cy + (r - 1) * math.sin(a)) - 1
        c.rect(tx, ty, 3, 3, dark)
    c.circle(cx, cy, r, dark)
    c.circle(cx, cy, r - 1, mid)
    c.circle(cx, cy, r - 3, lt)
    for i in range(4):
        a = math.radians(i * 90)
        c.line(round(cx + 2 * math.cos(a)), round(cy + 2 * math.sin(a)),
               round(cx + (r - 3) * math.cos(a)), round(cy + (r - 3) * math.sin(a)), dark)
    c.circle(cx, cy, 3, dark, fill=False)
    c.circle(cx, cy, 2, B_MD if not brass else B_DK)
    c.set(cx, cy, INK)

gear(m, 86, 156, 14, 8)
gear(m, 170, 152, 12, 8)
gear(m, 128, 170, 16, 10)
gear(m, 108, 141, 9, 8, brass=True)
gear(m, 150, 139, 9, 8, brass=True)

# spindle
m.rect(126, 30, 4, 40, B_DK)
m.rect(127, 30, 2, 40, B_LT)
m.circle(128, 27, 6, INK)
m.circle(128, 27, 5, '#7a5cc0')
m.circle(127, 26, 3, '#b78cff')
m.set(126, 24, '#ffffff')
m.circle(128, 46, 5, B_DK, fill=False)
m.rect(126, 150, 4, 18, B_DK)
m.rect(127, 150, 2, 18, B_LT)

# ---- back rings ----
ring(m, 88, 88, 0, 5, 180, 360)          # R2 big circle, back (upper)
arcline(m, 87, 87, 0, 200, 258, B_LT)
arcline(m, 87, 87, 0, 216, 236, B_HI)
ring(m, 112, 34, 0, 5, 180, 360)         # R1 equatorial, back
arcline(m, 111, 33, 0, 200, 340, B_LT)
ring(m, 100, 30, 27, 4, 0, 360)          # R3 tilted +
arcline(m, 99, 29, 27, 190, 260, B_LT)
ring(m, 100, 30, -27, 4, 0, 360)         # R4 tilted -
arcline(m, 99, 29, -27, 200, 270, B_LT)
ring(m, 22, 86, 14, 4, 0, 360)           # R5 vertical edge-on
arcline(m, 21, 85, 14, 190, 250, B_LT)
ring(m, 42, 42, 0, 4, 0, 360)            # R6 inner halo
stroke_full(m, 39, 39, 0, '#ffdf8a')
ring(m, 48, 15, -18, 3, 0, 360)          # R7 inner tilt
stroke_full(m, 45, 12, -18, '#caa15a')

# crystal spheres
def sphere(c, cx, cy, r, mid):
    dk = mix(mid, '#000000', 0.55)
    lt = mix(mid, '#ffffff', 0.55)
    c.circle(cx, cy, r, INK)
    c.circle(cx, cy, r - 1, dk)
    c.circle(cx - 1, cy - 1, r - 1, mid)
    c.circle(cx - 1, cy - 1, max(1, r - 3), lt)
    c.set(cx - max(1, r // 2), cy - max(1, r // 2), '#ffffff')

AMBER = '#e8a54c'; CYAN = '#4cc6e0'; VIOLET = '#a77ee8'; EMER = '#54d68c'; ROSE = '#e87ea0'; GOLD = '#e8cf5a'

# back spheres
for (rx, ry, rot, t, r, col) in [
    (112, 34, 0, 205, 4, AMBER), (112, 34, 0, 335, 4, CYAN),
    (88, 88, 0, 232, 4, EMER), (88, 88, 0, 306, 5, CYAN),
    (100, 30, 27, 255, 5, GOLD), (100, 30, -27, 285, 5, EMER),
    (42, 42, 0, 215, 3, CYAN),
]:
    x, y = ept(rx - 2, ry - 2, rot, t)
    sphere(m, round(x), round(y), r, col)

# central radiant core
m.circle(CX, CY, 14, CORE_O)
m.circle(CX, CY, 11, CORE_Y)
m.circle(CX, CY, 8, CORE_Y2)
m.circle(CX, CY, 5, CORE_W)
for ang in range(0, 360, 45):
    a = math.radians(ang)
    m.line(round(CX + 15 * math.cos(a)), round(CY + 15 * math.sin(a)),
           round(CX + 23 * math.cos(a)), round(CY + 23 * math.sin(a)), CORE_Y)
for ang in (0, 90, 180, 270):
    a = math.radians(ang)
    m.line(round(CX + 15 * math.cos(a)), round(CY + 15 * math.sin(a)),
           round(CX + 29 * math.cos(a)), round(CY + 29 * math.sin(a)), CORE_Y2)
    m.set(round(CX + 30 * math.cos(a)), round(CY + 30 * math.sin(a)), CORE_W)

# front spheres
front_spheres = [
    (112, 34, 0, 32, 6, VIOLET), (112, 34, 0, 148, 5, EMER),
    (88, 88, 0, 58, 6, AMBER), (88, 88, 0, 122, 5, VIOLET),
    (100, 30, 27, 75, 6, CYAN), (100, 30, -27, 105, 6, VIOLET),
    (48, 15, -18, 345, 3, GOLD), (42, 42, 0, 20, 3, AMBER),
]
for (rx, ry, rot, t, r, col) in front_spheres:
    x, y = ept(rx - 2, ry - 2, rot, t)
    sphere(m, round(x), round(y), r, col)

# ---- front ring arcs ----
ring(m, 100, 30, 27, 4, 15, 165)
arcline(m, 97, 27, 27, 25, 155, '#ffdf8a')
ring(m, 100, 30, -27, 4, 15, 165)
arcline(m, 97, 27, -27, 25, 155, '#ffdf8a')
ring(m, 112, 34, 0, 5, 5, 175)
arcline(m, 108, 30, 0, 15, 165, '#ffdf8a')
arcline(m, 111, 33, 0, 60, 120, B_SH)
ring(m, 88, 88, 0, 5, 5, 175)
arcline(m, 84, 84, 0, 15, 165, '#ffdf8a')
arcline(m, 87, 87, 0, 60, 120, B_SH)

# rivets on R1 band
for t in (0, 45, 90, 135, 180, 225, 270, 315):
    x, y = ept(109.5, 31.5, 0, t)
    m.circle(round(x), round(y), 1, INK)
    m.set(round(x), round(y), B_HI)

# runes
RUNES = [
    ["#..", "##.", "#.#", "##.", "#.."],
    ["#.#", "#.#", "#.#", "#.#", ".##"],
    [".##", "#.#", "##.", "#.#", "#.#"],
    ["##.", "#.#", "##.", "#.#", "#.#"],
    ["..#", ".#.", "#..", ".#.", "..#"],
    [".#.", "#.#", ".#.", ".#.", ".#."],
    ["##.", "#.#", "##.", "#.#", "##."],
    ["#.#", "#.#", ".#.", "#.#", "#.#"],
]

def draw_rune(c, x, y, i, col=RUNE):
    g = RUNES[i % len(RUNES)]
    for ry_, row in enumerate(g):
        for cx_, ch in enumerate(row):
            if ch == '#':
                c.set(x + cx_ + 1, y + ry_ + 1, RUNE_DK)
    for ry_, row in enumerate(g):
        for cx_, ch in enumerate(row):
            if ch == '#':
                c.set(x + cx_, y + ry_, col)

rune_centers = []
idx = 0
for t in (25, 55, 85, 115, 145, 170):
    x, y = ept(99, 21, 0, t)
    draw_rune(m, round(x) - 1, round(y) - 2, idx)
    rune_centers.append((round(x), round(y)))
    idx += 1
for t in (40, 70, 100, 130, 160):
    x, y = ept(75, 75, 0, t)
    draw_rune(m, round(x) - 1, round(y) - 2, idx)
    rune_centers.append((round(x), round(y)))
    idx += 1
for (ax, ay) in ((54, 118), (204, 124), (198, 66)):
    draw_rune(m, ax, ay, idx)
    rune_centers.append((ax + 1, ay + 2))
    idx += 1

# ---------------- pedestal ----------------
m.poly([(90, 196), (166, 196), (172, 202), (172, 209), (84, 209), (84, 202)], INK)
m.poly([(92, 197), (164, 197), (169, 201), (87, 201)], ST_LT)
m.line(92, 197, 164, 197, ST_LT)
m.rect(85, 203, 86, 5, ST_MD)
m.line(85, 203, 85, 207, ST_LT)
m.rect(94, 209, 68, 33, INK)
m.rect(95, 210, 66, 31, ST_SH)
m.line(95, 210, 95, 240, ST_LT)
m.line(98, 211, 98, 240, ST_DK)
m.line(158, 211, 158, 240, ST_DK)
m.rect(102, 214, 52, 22, INK)
m.rect(103, 215, 50, 20, ST_MD)
m.line(103, 215, 152, 215, ST_LT)
m.line(103, 215, 103, 234, ST_LT)
m.line(103, 234, 152, 234, ST_DK)
m.line(152, 215, 152, 234, ST_DK)
# base steps
m.rect(88, 242, 80, 5, INK)
m.rect(89, 243, 78, 3, ST_MD)
m.rect(80, 247, 96, 5, INK)
m.rect(81, 248, 94, 3, ST_SH)
m.rect(74, 252, 108, 4, INK)
m.rect(75, 253, 106, 2, ST_DK)
# cracks
m.line(118, 244, 121, 246, ST_DK)
m.line(90, 205, 93, 207, ST_DK)

# alchemical dial
m.circle(128, 224, 9, INK)
m.circle(128, 224, 8, B_DK)
m.circle(128, 224, 7, FACE)
for i in range(12):
    a = math.radians(i * 30)
    m.set(round(128 + 6 * math.cos(a)), round(224 + 6 * math.sin(a)), B_LT)
m.line(128, 224, 132, 220, B_HI)
m.line(128, 224, 126, 226, B_SH)
m.set(128, 224, B_HI)
draw_rune(m, 108, 220, 3)
draw_rune(m, 140, 220, 5)

# floating shards in the gap
for (sx, sy) in ((112, 188), (145, 186), (136, 191)):
    m.rect(sx, sy, 2, 2, INK)
    m.set(sx, sy, ST_LT)

# ---------------- top fx ----------------
for (x, y) in rune_centers[:6]:
    tp.circle(x, y, 3, '#57ffc826')
for (rx, ry, rot, t, r, col) in front_spheres:
    if r >= 5:
        x, y = ept(rx - 2, ry - 2, rot, t)
        tp.circle(round(x), round(y), r + 2, '#bfe0ff22')

# sparkles
for (sx, sy) in [(128, 14), (96, 52), (163, 44), (74, 96),
                 (186, 92), (110, 150), (152, 156), (52, 60), (208, 150)]:
    tp.set(sx, sy, '#ffffff')
    tp.set(sx - 1, sy, '#fff3c4b8'); tp.set(sx + 1, sy, '#fff3c4b8')
    tp.set(sx, sy - 1, '#fff3c4b8'); tp.set(sx, sy + 1, '#fff3c4b8')

random.seed(11)
for _ in range(14):
    tp.set(random.randint(48, 208), random.randint(6, 170), '#ffd99840')
for _ in range(5):
    tp.set(random.randint(48, 208), random.randint(6, 170), '#7fd8f036')
for (bx, by) in ((124, 190), (131, 186), (127, 193), (133, 189)):
    tp.set(bx, by, '#fff3c490')
for (fx_, fy_) in ((108, 234), (150, 238), (128, 246)):
    tp.set(fx_, fy_, '#ffe9a855')

# vignette corners
tp.rect(0, 0, 34, 34, '#05051030')
tp.rect(222, 0, 34, 34, '#05051030')
tp.rect(0, 222, 30, 34, '#05051030')
tp.rect(226, 222, 30, 34, '#05051030')

# ---------------- compose ----------------
flat = flatten([bg, fx, m, tp], name='arcane')
print(flat.stats_text())
view(flat)
save('arcane-instrument-giant', flat)
finish(flat)
