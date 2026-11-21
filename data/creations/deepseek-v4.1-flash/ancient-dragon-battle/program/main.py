import math

W = H = 256
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def th(x, y):
    return (BAYER[y & 3][x & 3] + 0.5) / 16.0


def vgrad(c, stops, y0, y1, x0=0, x1=255):
    n = len(stops)
    for y in range(y0, y1 + 1):
        i = 0
        while i < n - 2 and y >= stops[i + 1][0]:
            i += 1
        ya, ca = stops[i]
        yb, cb = stops[i + 1]
        t = (y - ya) / max(1, yb - ya)
        for x in range(x0, x1 + 1):
            c.set(x, y, cb if t > th(x, y) else ca)


def soft(c, cx, cy, r, col, power=1.5):
    x0 = max(0, int(cx - r))
    x1 = min(W - 1, int(cx + r))
    y0 = max(0, int(cy - r))
    y1 = min(H - 1, int(cy + r))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            d = math.hypot(x - cx, y - cy)
            if d > r:
                continue
            if th(x, y) < (1.0 - d / r) * power:
                c.set(x, y, col)


def ridge(c, pts, base_y, col):
    poly = list(pts) + [(pts[-1][0], base_y), (pts[0][0], base_y)]
    c.poly(poly, col)


def flame(c, cx, by, w, h, layers):
    out = [(cx - w / 2, by), (cx - w * 0.46, by - h * 0.40), (cx - w * 0.30, by - h * 0.62),
           (cx - w * 0.05, by - h), (cx + w * 0.22, by - h * 0.62), (cx + w * 0.44, by - h * 0.34),
           (cx + w / 2, by)]
    for s, col in layers:
        p2 = [(round(cx + (x - cx) * s), round(by + (y - by) * s)) for (x, y) in out]
        c.poly(p2, col)


def puff(c, cx, cy, r, dark, mid, light):
    r = max(1, int(r))
    c.circle(int(cx), int(cy), r, dark)
    c.circle(int(cx), int(cy) - max(1, r // 3), max(1, int(r * 0.76)), mid)
    c.circle(int(cx) - max(1, r // 4), int(cy) - max(1, int(r * 0.62)), max(1, int(r * 0.42)), light)


def tapered(c, p0, p1, p2, r0, r1, col, n=50):
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        c.circle(int(round(x)), int(round(y)), max(0, int(round(r))), col)


# ------------------------------------------------------------------ SKY
sky = new_canvas(W, H, '#080616', name='sky')
SKY_STOPS = [(0, '#070514'), (14, '#110d29'), (34, '#1d1440'), (54, '#2b1a52'), (76, '#3c2160'),
             (96, '#51285f'), (112, '#692f5e'), (128, '#833858'), (144, '#9c464f'), (158, '#b45546'),
             (170, '#c96840'), (182, '#dd7f3f'), (196, '#eda046')]
vgrad(sky, SKY_STOPS, 0, 200)

# sun low on the left, behind the ridge
SUNX, SUNY = 48, 164
soft(sky, SUNX, SUNY, 62, '#b65340', 1.15)
soft(sky, SUNX, SUNY, 44, '#d9702f', 1.25)
soft(sky, SUNX, SUNY, 30, '#f0963a', 1.35)
soft(sky, SUNX, SUNY, 22, '#ffbe57', 1.5)
sky.circle(SUNX, SUNY, 17, '#ffc961')
sky.circle(SUNX, SUNY, 13, '#ffe08c')
sky.circle(SUNX, SUNY, 8, '#fff6cc')
soft(sky, SUNX, SUNY, 90, '#c05c3a', 0.7)

# thin high clouds lit from below
sky.dither(0, 40, 256, 5, '#3c2160', '#51285f', pattern='bayer4')
for (cx, cy, w, h) in [(70, 52, 60, 3), (150, 38, 80, 3), (30, 74, 46, 3), (200, 70, 70, 3),
                       (110, 88, 90, 2), (210, 96, 60, 2), (24, 110, 54, 2)]:
    sky.ellipse(cx, cy, w // 2, h, '#5c2a56')
    sky.ellipse(cx + 2, cy + 1, w // 2 - 6, max(1, h - 1), '#7a3559')

# ------------------------------------------------------------------ MOUNTAINS
mtn = new_canvas(W, H, None, name='mtn')
FAR = [(0, 150), (10, 134), (18, 143), (28, 148), (36, 155), (46, 158), (56, 150), (64, 138),
       (74, 146), (86, 154), (98, 146), (110, 159), (124, 156), (138, 163), (152, 156),
       (166, 164), (180, 156), (192, 149), (202, 141), (212, 149), (224, 136), (234, 145),
       (244, 132), (255, 142)]
ridge(mtn, FAR, 200, '#5b3563')
NEAR = [(0, 172), (14, 160), (26, 170), (38, 177), (50, 173), (62, 179), (74, 167), (86, 176),
        (100, 183), (114, 173), (128, 182), (142, 175), (156, 184), (170, 174), (184, 183),
        (196, 170), (210, 179), (222, 164), (236, 175), (248, 162), (255, 171)]
ridge(mtn, NEAR, 200, '#3a2149')
# lit slopes facing the sun
rim = [(0, 150), (10, 134), (18, 143)]
mtn.line(0, 150, 10, 134, '#8c4a63')
mtn.line(10, 134, 18, 143, '#8c4a63')
mtn.line(28, 148, 36, 155, '#6d3b57')
mtn.line(0, 172, 14, 160, '#58314a')
mtn.line(14, 160, 26, 170, '#58314a')
mtn.dither(0, 168, 256, 18, '#3a2149', '#4a2a4a', pattern='bayer4')

# ------------------------------------------------------------------ GROUND
plain = new_canvas(W, H, None, name='plain')
PG = [(186, '#4a2b46'), (194, '#3a2340'), (204, '#2a1a34'), (218, '#1c1228'),
      (234, '#140d1e'), (255, '#0c0714')]
for y in range(186, 256):
    i = 0
    while i < len(PG) - 2 and y >= PG[i + 1][0]:
        i += 1
    ya, ca = PG[i]
    yb, cb = PG[i + 1]
    t = (y - ya) / max(1, yb - ya)
    for x in range(W):
        plain.set(x, y, cb if t > th(x, y) else ca)
# hazy horizon band
plain.dither(0, 184, 256, 4, '#4a2b46', '#5c3550', pattern='bayer4')
plain.dither(0, 186, 256, 3, '#4a2b46', '#63394f', pattern='bayer4')
plain.line(0, 185, 255, 185, '#6b3d55')

# ------------------------------------------------------------------ CASTLE
cast = new_canvas(W, H, None, name='castle')
SD = '#1c1529'
SM = '#251c36'
SL = '#332643'
SDD = '#100b19'
SW = '#3d2630'
RIMW = '#8a5040'


def block(c, x0, y0, x1, y1):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, SD)
    c.line(x0, y0, x0, y1, SL)
    c.line(x1, y0, x1, y1, SDD)


# curtain wall
block(cast, 84, 150, 216, 212)
for yy in (160, 169, 178, 187, 196, 204):
    cast.line(86, yy, 214, yy, SM)
for x in range(90, 214, 11):
    cast.line(x, 151, x, 159, SM)
    cast.line(x + 5, 161, x + 5, 168, SM)
# wall walk crenellations
for x in range(86, 214, 11):
    cast.rect(x, 141, 6, 10, SD)
    cast.line(x, 141, x + 5, 141, SL)
    cast.line(x + 5, 141, x + 5, 150, SDD)


def tower(c, x0, x1, ytop, ybase, apex=None, over=3):
    block(c, x0, ytop, x1, ybase)
    if apex is not None:
        cx = (x0 + x1) // 2
        c.poly([(x0 - over, ytop + 1), (cx, apex), (x1 + over, ytop + 1)], SM)
        c.line(cx, apex, x1 + over, ytop + 1, SDD)
        c.line(x0 - over + 1, ytop, x0 - over + 2, ytop - 6, SL)
    c.line(x0 + 2, ytop + 4, x0 + 2, ybase, SM)


tower(cast, 84, 110, 126, 212, apex=98)
tower(cast, 116, 134, 116, 212, apex=88)
# keep
block(cast, 140, 104, 196, 212)
for x in range(142, 196, 9):
    cast.rect(x, 96, 6, 9, SD)
    cast.line(x, 96, x + 5, 96, SL)
cast.line(142, 112, 194, 112, SM)
cast.line(142, 122, 194, 122, SM)
tower(cast, 156, 176, 78, 104, apex=52)
tower(cast, 198, 222, 134, 212, apex=106)
# small turret
tower(cast, 130, 142, 128, 152, apex=112, over=2)

# windows with fire inside
for (wx, wy, ww, wh) in [(90, 140, 3, 6), (100, 140, 3, 6), (146, 118, 3, 7), (154, 118, 3, 7),
                         (176, 118, 3, 7), (184, 118, 3, 7), (162, 86, 3, 6), (204, 150, 3, 6),
                         (212, 150, 3, 6), (122, 132, 3, 6), (134, 142, 3, 5), (46 + 100, 160, 3, 6)]:
    cast.rect(wx, wy, ww, wh, '#ff9a2e')
    cast.rect(wx + 1, wy + 1, max(1, ww - 2), max(1, wh - 2), '#ffd257')

# --------------------------------------------------- fire on the castle
F_OUT = '#ef5320'
F_MID = '#ff8c22'
F_IN = '#ffc347'
F_HOT = '#fff0b0'
GLOW = '#7a3524'

soft(cast, 158, 96, 46, GLOW, 1.0)
soft(cast, 96, 132, 34, GLOW, 0.9)
soft(cast, 172, 196, 52, '#8a3a22', 1.0)

flame(cast, 158, 106, 26, 30, [(1.0, F_OUT), (0.72, F_MID), (0.42, F_IN), (0.18, F_HOT)])
flame(cast, 146, 104, 12, 18, [(1.0, F_OUT), (0.66, F_MID), (0.34, F_IN)])
flame(cast, 176, 104, 10, 14, [(1.0, F_OUT), (0.6, F_MID), (0.3, F_IN)])
flame(cast, 96, 128, 20, 24, [(1.0, F_OUT), (0.7, F_MID), (0.38, F_IN), (0.16, F_HOT)])
flame(cast, 86, 130, 9, 13, [(1.0, F_OUT), (0.6, F_MID)])
flame(cast, 166, 54, 9, 14, [(1.0, F_OUT), (0.6, F_MID), (0.3, F_IN)])
flame(cast, 124, 152, 14, 14, [(1.0, F_OUT), (0.66, F_MID), (0.3, F_IN)])
flame(cast, 210, 138, 12, 16, [(1.0, F_OUT), (0.66, F_MID), (0.3, F_IN)])
flame(cast, 168, 208, 44, 34, [(1.0, F_OUT), (0.74, F_MID), (0.46, F_IN), (0.2, F_HOT)])
flame(cast, 148, 208, 20, 22, [(1.0, F_OUT), (0.7, F_MID), (0.36, F_IN)])
flame(cast, 190, 208, 22, 24, [(1.0, F_OUT), (0.7, F_MID), (0.36, F_IN)])

# --------------------------------------------------- knights on the ramparts
K_D = '#0e0a16'
K_R = '#c25b2e'
K_S = '#3a2a20'
K_M = '#8f97a8'


def knight(c, x, fy):
    # fy = feet y
    c.rect(x - 2, fy - 8, 5, 8, K_D)          # body
    c.circle(x, fy - 10, 2, K_D)              # head/helm
    c.set(x - 1, fy - 10, '#2a2036')
    c.rect(x - 2, fy - 9, 1, 3, '#2a2036')
    c.line(x, fy - 2, x, fy + 1, K_D)
    c.line(x + 1, fy - 2, x + 1, fy + 1, K_D)
    # shield
    c.ellipse(x - 3, fy - 5, 2, 3, '#5e1f28')
    c.set(x - 4, fy - 6, '#b8452f')
    c.set(x - 3, fy - 3, '#8a2c2c')
    # spear
    c.line(x + 3, fy + 1, x + 3, fy - 18, '#2f2216')
    c.line(x + 3, fy - 18, x + 3, fy - 21, K_M)
    c.set(x + 2, fy - 20, '#c8cdd8')
    # rim light
    c.line(x + 2, fy - 8, x + 2, fy - 1, K_R)


for (kx, ky) in [(78, 141), (92, 141), (128, 141), (146, 142), (166, 142), (188, 142),
                 (204, 141), (70, 141), (150, 141), (196, 141)]:
    knight(cast, kx, ky)

# ------------------------------------------------------------------ ASSEMBLE
res = flatten([sky, mtn, plain, cast], name='result')
print(res.stats_text())

ramp = " .:-=+*#%@"


def ascii_view(c, x0=0, y0=0, x1=255, y1=255, step=4):
    lut = {p['index']: p['rgba'] for p in c.palette()}
    lines = []
    for y in range(y0, y1 + 1, step):
        row = ''
        for x in range(x0, x1 + 1, step):
            r, g, b, a = lut[c.get(x, y)]
            if a == 0:
                row += ' '
                continue
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
            row += ramp[min(len(ramp) - 1, int(lum * len(ramp)))]
        lines.append('%3d|%s' % (y, row))
    print('\n'.join(lines))


ascii_view(res, step=4)
