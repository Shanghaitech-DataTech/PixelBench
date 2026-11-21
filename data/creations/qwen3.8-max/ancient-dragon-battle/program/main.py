# =====================================================================
#  ancient-dragon-battle  --  256x256 epic fantasy battlefield
#  sunset sky / burning castle / dragon / rampart knights / siege tower
# =====================================================================

W = H = 256
c = new_canvas(W, H, name="battlefield")

# ------------------------------------------------------------- utilities
def make_bayer(n):
    m = [[0, 2], [3, 1]]
    while len(m) < n:
        s = len(m)
        nw = [[0] * (s * 2) for _ in range(s * 2)]
        for y in range(s):
            for x in range(s):
                v = m[y][x]
                nw[y][x]         = 4 * v
                nw[y][x + s]     = 4 * v + 2
                nw[y + s][x]     = 4 * v + 3
                nw[y + s][x + s] = 4 * v + 1
        m = nw
    return m

B8 = make_bayer(8)

def bt(x, y):
    return (B8[y & 7][x & 7] + 0.5) / 64.0

def gradient(cv, stops, x0=0, x1=W - 1):
    cols = [cv.color(h) for _, h in stops]
    ys = [y for y, _ in stops]
    for y in range(ys[0], ys[-1] + 1):
        i = 0
        while i < len(ys) - 2 and y >= ys[i + 1]:
            i += 1
        span = max(1, ys[i + 1] - ys[i])
        t = (y - ys[i]) / float(span)
        if t < 0.0:
            t = 0.0
        if t > 1.0:
            t = 1.0
        lo, hi = cols[i], cols[i + 1]
        for x in range(x0, x1 + 1):
            cv.set(x, y, hi if bt(x, y) < t else lo)

def opoly(cv, pts, dx, dy, col):
    cv.poly([(int(px + dx), int(py + dy)) for px, py in pts], col)

def oline(cv, pts, dx, dy, col):
    for i in range(len(pts) - 1):
        cv.line(int(pts[i][0] + dx), int(pts[i][1] + dy),
                int(pts[i + 1][0] + dx), int(pts[i + 1][1] + dy), col)

# =====================================================================
# 1.  SKY
# =====================================================================
SKY_STOPS = [
    (0,   '#100a1c'),
    (14,  '#1a1030'),
    (30,  '#281541'),
    (46,  '#3d1a4b'),
    (62,  '#571f4c'),
    (78,  '#75294a'),
    (94,  '#96363f'),
    (110, '#b84c37'),
    (126, '#d46a30'),
    (140, '#ea8c2e'),
    (152, '#f8b246'),
    (164, '#fcd47e'),
]
gradient(c, SKY_STOPS, 0, W - 1)
# the sky rect only covers rows 0..164
for y in range(165, H):
    c.line(0, y, W - 1, y, c.color('#fcd47e'))

# stars in the deep upper sky
STAR = c.color('#e8dcff')
STAR2 = c.color('#9a86c0')
import random
import math
random.seed(7)
for i in range(70):
    x = random.randrange(0, W)
    y = random.randrange(0, 62)
    fade = 1.0 - y / 62.0
    if random.random() < fade * 0.9:
        c.set(x, y, STAR if random.random() < 0.45 else STAR2)

# =====================================================================
# 2.  CLOUDS  (streaky, lit from below-right by the setting sun)
# =====================================================================
CL_DARK = c.color('#2b1a3f')
CL_MID  = c.color('#4d2a53')
CL_WARM = c.color('#8e4550')
CL_LIT  = c.color('#d9764a')
CL_HOT  = c.color('#f7b069')

def cloud(cx, cy, rx, ry, bright=1.0):
    c.ellipse(cx, cy, rx, ry, CL_DARK)
    c.ellipse(cx + 1, cy + 1, max(1, rx - 2), max(1, ry - 1), CL_MID)
    c.ellipse(cx + 3, cy + 2, max(1, rx - 4), max(1, ry - 1), CL_WARM)
    if bright > 0.5:
        c.ellipse(cx + rx // 3, cy + ry, max(1, rx // 2), 1, CL_LIT)
    if bright > 0.8:
        c.line(cx - rx + 3, cy + ry, cx + rx - 2, cy + ry, CL_HOT)

cloud(38, 34, 30, 5, 0.4)
cloud(96, 24, 24, 4, 0.3)
cloud(178, 30, 34, 5, 0.6)
cloud(226, 52, 26, 4, 0.9)
cloud(60, 62, 40, 6, 0.7)
cloud(140, 74, 30, 5, 1.0)
cloud(24, 88, 26, 4, 1.0)
cloud(206, 92, 34, 5, 1.0)
cloud(112, 104, 44, 5, 1.0)
cloud(166, 118, 28, 3, 1.0)
cloud(44, 122, 30, 3, 1.0)

# thin high cirrus streaks
for (x0, y0, ln) in [(10, 18, 46), (70, 12, 34), (150, 16, 52), (210, 22, 40),
                     (120, 44, 40), (190, 62, 30), (14, 52, 34)]:
    c.line(x0, y0, x0 + ln, y0, CL_MID)
    c.line(x0 + 4, y0 + 1, x0 + ln - 6, y0 + 1, CL_DARK)

# =====================================================================
# 3.  SUN  +  glow
# =====================================================================
SUNX, SUNY, SUNR = 176, 118, 13
def sun_glow():
    ramp = [c.color('#f9a83c'), c.color('#e07a30'), c.color('#b85a34')]
    for y in range(SUNY - 62, SUNY + 63):
        for x in range(SUNX - 62, SUNX + 63):
            if x < 0 or y < 0 or x >= W or y >= H:
                continue
            d = ((x - SUNX) ** 2 + (y - SUNY) ** 2) ** 0.5
            if d > SUNR + 44:
                continue
            if d <= SUNR:
                continue
            inten = 1.0 - (d - SUNR) / 44.0
            inten = inten ** 1.5
            ci = 0 if inten > 0.55 else (1 if inten > 0.25 else 2)
            if bt(x, y) < inten * 0.95:
                c.set(x, y, ramp[ci])
sun_glow()
c.circle(SUNX, SUNY, SUNR, c.color('#ffc95e'))
c.circle(SUNX, SUNY - 1, SUNR - 4, c.color('#ffe08e'))
c.circle(SUNX, SUNY - 2, SUNR - 9, c.color('#fff3c4'))
c.circle(SUNX - 1, SUNY - 3, SUNR - 13, c.color('#fffbe8'))

# =====================================================================
# 4.  MOUNTAINS
# =====================================================================
FAR  = c.color('#4c3468')
FARR = c.color('#8a6090')
MID  = c.color('#33214c')
MIDR = c.color('#5d3d68')
NEAR = c.color('#241634')
NEARR= c.color('#452c4c')

far_peaks = [(0,138),(12,126),(24,133),(38,112),(50,124),(64,104),(78,122),
             (92,113),(106,128),(120,117),(134,130),(148,119),(162,131),
             (176,124),(190,137),(204,143),(218,136),(232,145),(246,138),(255,143)]
c.poly(far_peaks + [(255, 176), (0, 176)], FAR)
oline(c, far_peaks, 0, 0, FARR)

mid_peaks = [(0,153),(14,145),(28,151),(44,139),(58,149),(74,141),(90,151),
             (106,143),(122,153),(138,145),(154,155),(170,147),(186,157),
             (202,149),(218,159),(234,151),(250,158),(255,155)]
c.poly(mid_peaks + [(255, 186), (0, 186)], MID)
oline(c, mid_peaks, 0, 0, MIDR)

# snow / sunlit tips on the far range
for (px, py) in [(38,112),(64,104),(92,113),(120,117),(148,119)]:
    c.poly([(px - 5, py + 7), (px, py), (px + 5, py + 7), (px + 2, py + 6),
            (px, py + 4), (px - 2, py + 6)], c.color('#c9a8c8'))

# =====================================================================
# 5.  FIELD / PLAIN
# =====================================================================
gradient(c, [(160, '#3a2540'), (176, '#2c1c33'), (196, '#221527'), (256, '#170e1c')])
# warm bounce light from the burning castle on the left of the field
FIRE_GLOW = c.color('#6b3a30')
for y in range(162, 210):
    for x in range(0, 150):
        d = ((x - 70) ** 2 + (y - 165) ** 2 * 2.2) ** 0.5
        if d < 92 and bt(x, y) < (1.0 - d / 92.0) * 0.55:
            c.set(x, y, FIRE_GLOW)

# =====================================================================
# 6.  CRAG + CASTLE
# =====================================================================
CRAG   = c.color('#1d1229')
CRAG_L = c.color('#3b2740')
CRAG_R = c.color('#5d3a44')
crag = [(0,206),(0,170),(10,161),(26,151),(44,143),(64,138),(88,135),
        (112,137),(134,143),(152,152),(168,162),(180,174),(180,206)]
c.poly(crag, CRAG)
oline(c, crag[:14], 0, 0, CRAG_L)
# sunlit right edge of the crag
c.line(112, 137, 180, 174, CRAG_R)
c.line(134, 143, 180, 176, CRAG_R)
# rock striations
for i in range(9):
    x0 = 8 + i * 18
    c.line(x0, 176 + (i % 3) * 4, x0 + 12, 168 + (i % 4) * 5, c.color('#150d1e'))

ST_D  = c.color('#221b31')   # stone shadow
ST_M  = c.color('#38304d')   # stone mid
ST_L  = c.color('#514769')   # stone lit
ST_H  = c.color('#7a6c92')   # stone highlight
ST_W  = c.color('#a97a63')   # warm sunset rim on stone
ROOF  = c.color('#1a1327')
ROOFL = c.color('#332647')

def merlons(x0, x1, ytop, w=5, gap=4, col=ST_M, top=ST_L):
    x = x0
    while x <= x1 - w:
        c.rect(x, ytop, w, 6, col)
        c.line(x, ytop, x + w - 1, ytop, top)
        x += w + gap

def tower(x0, y0, x1, y1, lit_right=True):
    """round-ish wall tower"""
    c.rect(x0, y0, x1 - x0, y1 - y0, ST_M)
    c.rect(x0, y0, 3, y1 - y0, ST_D)
    if lit_right:
        c.rect(x1 - 4, y0, 4, y1 - y0, ST_L)
        c.line(x1 - 1, y0, x1 - 1, y1 - 1, ST_W)
    # coursing
    for yy in range(y0 + 5, y1, 7):
        c.line(x0, yy, x1 - 1, yy, ST_D)
    c.line(x0, y0, x1 - 1, y0, ST_L)

# --- curtain wall -------------------------------------------------
c.rect(14, 130, 130, 34, ST_M)
c.rect(14, 130, 130, 3, ST_L)
c.rect(14, 156, 130, 8, ST_D)
merlons(14, 144, 124, 5, 4, ST_M, ST_H)
for yy in range(136, 162, 6):
    c.line(14, yy, 143, yy, ST_D)
for xx in range(18, 142, 11):
    c.line(xx, 133, xx, 162, ST_D)
c.line(143, 124, 143, 163, ST_W)

# --- left round tower (roof on fire) ------------------------------
tower(20, 100, 46, 164)
c.poly([(17,100),(33,78),(49,100)], ROOF)
c.poly([(33,78),(49,100),(41,100),(33,88)], ROOFL)
c.line(33, 78, 33, 70, ST_D)
# broken / burning roof edge
c.poly([(17,100),(24,92),(28,100),(33,88),(38,100),(44,90),(49,100)], c.color('#120c1c'))

# --- gatehouse -----------------------------------------------------
tower(58, 108, 94, 164)
merlons(58, 94, 102, 6, 4, ST_M, ST_H)
c.rect(70, 140, 16, 24, c.color('#100b18'))          # gate arch
c.path("M70,140 A8,10 0 0 1 86,140 Z", c.color('#100b18'))
c.line(69, 140, 69, 163, ST_D)
c.line(86, 140, 86, 163, ST_D)
# portcullis
for xx in range(72, 86, 4):
    c.line(xx, 138, xx, 152, c.color('#4a3a2a'))
c.line(70, 144, 86, 144, c.color('#4a3a2a'))
c.line(70, 150, 86, 150, c.color('#4a3a2a'))

# --- great keep ----------------------------------------------------
tower(96, 72, 138, 164)
merlons(94, 140, 66, 6, 4, ST_M, ST_H)
c.rect(96, 72, 42, 4, ST_L)
# corner turret
tower(130, 58, 146, 100)
c.poly([(128,58),(138,40),(148,58)], ROOF)
c.poly([(138,40),(148,58),(143,58),(138,48)], ROOFL)
# collapsed corner + rubble
c.poly([(96,72),(104,72),(104,84),(110,84),(110,96),(96,96)], c.color('#150e20'))
c.poly([(92,160),(98,150),(104,158),(110,148),(118,160),(112,164),(100,164)], ST_D)

# windows: some glowing, some dark
WIN_L = c.color('#ffab3c')
WIN_H = c.color('#ffe08a')
WIN_D = c.color('#0e0a16')
for (wx, wy) in [(26,112),(36,112),(26,130),(36,130),(64,118),(86,118),
                 (102,86),(112,86),(122,86),(102,104),(112,104),(122,104),
                 (102,122),(112,122),(122,122),(134,68),(140,68),(134,84)]:
    glow = (wx + wy) % 3 != 0
    c.rect(wx, wy, 3, 5, WIN_H if glow else WIN_D)
    c.rect(wx, wy, 3, 2, WIN_L if glow else WIN_D)
    c.line(wx - 1, wy - 1, wx + 3, wy - 1, ST_D)

# banners on the wall
BAN_R = c.color('#8e2430')
BAN_G = c.color('#d9a13c')
for bx in (50, 100, 126):
    c.line(bx, 118, bx, 112, ST_D)
    c.poly([(bx - 4, 118), (bx + 4, 118), (bx + 4, 134), (bx, 130), (bx - 4, 134)], BAN_R)
    c.set(bx, 123, BAN_G)
    c.set(bx - 1, 124, BAN_G)
    c.set(bx + 1, 124, BAN_G)

# =====================================================================
# 7.  FIRE + SMOKE on the castle
# =====================================================================
F1 = c.color('#a82a10')
F2 = c.color('#e8541a')
F3 = c.color('#ff8c1e')
F4 = c.color('#ffc93c')
F5 = c.color('#fff0a8')
FIRE_COLS = [F1, F2, F3, F4, F5]

def flame(cx, base, w, h, cols=FIRE_COLS):
    n = len(cols)
    for i in range(n):
        ww = max(1, int(w * (1.0 - i * 0.8 / n)))
        hh = max(2, int(h * (1.0 - i * 0.75 / n)))
        jx = (i % 2) * 2 - 1
        c.poly([(cx - ww, base),
                (cx - ww + jx, base - int(hh * 0.45)),
                (cx - ww // 2, base - int(hh * 0.7)),
                (cx + jx, base - hh),
                (cx + ww // 2, base - int(hh * 0.62)),
                (cx + ww - jx, base - int(hh * 0.4)),
                (cx + ww, base)], cols[i])

def fire_glow_at(cx, cy, r, col, dens=0.5):
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            if x < 0 or y < 0 or x >= W or y >= H:
                continue
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if d > r:
                continue
            if bt(x, y) < (1.0 - d / r) * dens:
                c.set(x, y, col)

# great keep roof ablaze
fire_glow_at(116, 62, 30, F1, 0.35)
flame(104, 72, 9, 26)
flame(116, 70, 12, 38)
flame(128, 72, 9, 24)
flame(110, 74, 6, 16)
flame(124, 74, 6, 18)
# left tower roof ablaze
fire_glow_at(33, 88, 24, F1, 0.35)
flame(27, 96, 8, 24)
flame(36, 94, 10, 32)
flame(43, 98, 6, 16)
# fire through the gate and in the courtyard
fire_glow_at(78, 152, 20, F2, 0.3)
flame(74, 162, 7, 18)
flame(82, 162, 6, 14)
flame(48, 158, 6, 16)
flame(120, 158, 7, 18)
# a burning outbuilding to the right of the keep
c.rect(146, 146, 22, 18, ST_D)
c.poly([(144,146),(157,136),(170,146)], ROOF)
fire_glow_at(157, 140, 20, F2, 0.35)
flame(152, 146, 8, 22)
flame(161, 144, 9, 28)

# ---- smoke plume (behind + in front) ----
SM1 = c.color('#191226')
SM2 = c.color('#282038')
SM3 = c.color('#3d3350')
SM4 = c.color('#584a6b')
SM5 = c.color('#7d6480')
SMW = c.color('#9a6a5e')

def puff(x, y, r, col):
    c.circle(x, y, r, col)

def plume(ox, oy, puffs):
    for (dx, dy, r, col) in puffs:
        puff(ox + dx, oy + dy, r, col)

def plume_shape(pts, r0, r1, ox=0, oy=0, col=SM1, bump=False, wob=0.0, seed=0.0):
    n = len(pts)
    left = []
    right = []
    radii = []
    for i in range(n):
        t = i / float(n - 1)
        r = r0 + (r1 - r0) * t
        if wob:
            r *= 1.0 + wob * math.sin(i * 1.9 + seed)
        radii.append(r)
    for i, (x, y) in enumerate(pts):
        r = radii[i]
        if i == 0:
            dx, dy = pts[1][0] - x, pts[1][1] - y
        elif i == n - 1:
            dx, dy = x - pts[i - 1][0], y - pts[i - 1][1]
        else:
            dx, dy = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        L = (dx * dx + dy * dy) ** 0.5 or 1.0
        px, py = -dy / L, dx / L
        left.append((x + px * r + ox, y + py * r + oy))
        right.append((x - px * r + ox, y - py * r + oy))
    c.poly([(int(a), int(b)) for a, b in left + right[::-1]], col)
    if bump:
        for i, (x, y) in enumerate(pts):
            c.circle(int(x + ox), int(y + oy), max(2, int(radii[i] * 0.8)), col)
    return left, right, radii

def smoke_plume(pts, r0, r1, seed=0.0):
    left, right, radii = plume_shape(pts, r0, r1, 0, 0, SM1, bump=True, wob=0.22, seed=seed)
    plume_shape(pts, max(1, r0 - 3), max(1, r1 - 6), 2, 2, SM2, wob=0.22, seed=seed)
    # lit puffs along the lower-right flank
    for i in range(1, len(pts)):
        x, y = pts[i]
        r = radii[i]
        c.circle(int(x + r * 0.35), int(y + r * 0.35), max(1, int(r * 0.42)), SM3)
        if i % 2 == 0:
            c.circle(int(x + r * 0.5), int(y + r * 0.5), max(1, int(r * 0.24)), SM4)
    # dark core shadow on the upper-left flank
    for i in range(1, len(pts)):
        x, y = pts[i]
        r = radii[i]
        c.circle(int(x - r * 0.45), int(y - r * 0.45), max(1, int(r * 0.3)), SM1)
    # sunlit rim on the lower-right edge
    for i in range(len(right) - 1):
        c.line(int(right[i][0]), int(right[i][1]),
               int(right[i + 1][0]), int(right[i + 1][1]), SMW)

smoke_plume([(112,66),(118,54),(128,44),(142,36),(158,26),(176,18),(196,10),(218,2)],
            10, 24, seed=0.5)
# a second wisp off the keep roof
smoke_plume([(128,70),(140,60),(154,50),(170,40),(188,30)], 5, 13, seed=2.0)
# second smaller plume from the left tower
smoke_plume([(33,82),(26,70),(18,56),(10,42),(2,28),(-4,16)], 7, 14, seed=4.0)

# =====================================================================
# 8.  MID-GROUND: distant army, siege towers
# =====================================================================
SIL  = c.color('#150e1e')
SIL2 = c.color('#241832')
RIMW = c.color('#7d4a44')

# --- formation of soldiers marching on the plain (left) ---
def soldier_block(x0, x1, ybase, h, dens=1.0):
    for x in range(x0, x1):
        if bt(x, 3) > dens:
            continue
        hh = h + (B8[x & 7][(x * 3) & 7] % 4) - 2
        c.rect(x, ybase - hh, 1, hh, SIL)
        c.set(x, ybase - hh, SIL2)
    # pikes
    for x in range(x0, x1, 3):
        top = ybase - h - 12 - (x % 5)
        c.line(x, top, x, ybase - h + 3, c.color('#2a2036'))
        c.set(x, top, c.color('#5c5470'))

soldier_block(4, 74, 190, 12, 1.0)
soldier_block(70, 128, 194, 14, 1.0)
soldier_block(126, 176, 190, 11, 0.9)

# --- second siege tower, far, small ---
WOOD_D = c.color('#2b1e16')
WOOD_M = c.color('#4a3524')
WOOD_L = c.color('#6b4c31')
WOOD_H = c.color('#8a6c46')

def siege_tower(x0, y0, x1, y1, dark=False):
    wd, wm, wl, wh = (c.color('#191019'), c.color('#2b1e16'), c.color('#4a3524'), c.color('#6b4c31')) if dark else (WOOD_D, WOOD_M, WOOD_L, WOOD_H)
    w = x1 - x0
    h = y1 - y0
    # frame
    c.rect(x0, y0, w, h, wm)
    c.rect(x0, y0, 3, h, wd)
    c.rect(x1 - 4, y0, 4, h, wl)
    # levels
    levels = 5
    for i in range(levels + 1):
        yy = y0 + i * h // levels
        c.rect(x0, yy, w, 2, wl)
        c.line(x0, yy, x1 - 1, yy, wh)
    # uprights + braces
    for xx in range(x0 + 6, x1 - 4, 9):
        c.line(xx, y0, xx, y1 - 1, wd)
    for i in range(levels):
        yy = y0 + i * h // levels
        c.line(x0 + 2, yy + 2, x1 - 3, yy + h // levels - 2, wd)
        c.line(x1 - 3, yy + 2, x0 + 2, yy + h // levels - 2, wd)
    # roof
    c.poly([(x0 - 3, y0), (x0 + w // 2, y0 - 9), (x1 + 3, y0)], wd)
    c.poly([(x0 + w // 2, y0 - 9), (x1 + 3, y0), (x0 + w // 2 + 3, y0)], wl)
    # soldiers inside
    for i in range(levels):
        yy = y0 + i * h // levels + 2
        for xx in range(x0 + 4, x1 - 6, 7):
            c.circle(xx + 2, yy + 3, 2, SIL)
            c.rect(xx, yy + 5, 5, h // levels - 8, SIL2)
            c.line(xx + 2, yy - 6, xx + 2, yy + 4, c.color('#2a2036'))
    # bridge at the top front
    c.poly([(x0 - 2, y0 + 6), (x0 - 20, y0 + 14), (x0 - 20, y0 + 18), (x0 - 2, y0 + 12)], wl)
    for xx in range(x0 - 20, x0, 4):
        c.line(xx, y0 + 8, xx, y0 + 16, wd)
    # wheels
    wr = max(4, h // 12)
    for wx in (x0 + wr + 2, x1 - wr - 3):
        c.circle(wx, y1 - wr + 1, wr, wd)
        c.circle(wx, y1 - wr + 1, wr - 2, wm)
        for a in range(4):
            import math
            ang = a * 3.14159 / 4
            c.line(int(wx - (wr - 1) * math.cos(ang)), int(y1 - wr + 1 - (wr - 1) * math.sin(ang)),
                   int(wx + (wr - 1) * math.cos(ang)), int(y1 - wr + 1 + (wr - 1) * math.sin(ang)), wl)
    # banner
    c.line(x0 + w // 2, y0 - 9, x0 + w // 2, y0 - 20, wd)
    c.poly([(x0 + w // 2, y0 - 20), (x0 + w // 2 + 12, y0 - 17), (x0 + w // 2, y0 - 13)], BAN_R)

siege_tower(182, 116, 236, 198)
siege_tower(150, 146, 176, 194, dark=True)

# pushers around the near tower
soldier_block(176, 244, 200, 13, 1.0)

# --- a battering ram / cart ---
c.rect(158, 186, 20, 8, WOOD_M)
c.rect(158, 186, 20, 2, WOOD_L)
c.circle(162, 196, 3, WOOD_D)
c.circle(174, 196, 3, WOOD_D)
c.line(150, 190, 186, 190, WOOD_H)

# =====================================================================
# 9.  THE DRAGON
# =====================================================================
def paint_dragon(cv, col):
    # ---- far wing (up-left) ----
    cv.poly([(148,52),(128,28),(104,14),(84,18),(96,30),(90,42),(106,46),
             (102,58),(122,58),(138,64)], col)
    # ---- tail ----
    cv.poly([(192,50),(212,58),(230,66),(242,76),(250,88),(252,98),(244,96),
             (236,86),(224,76),(208,68),(192,64)], col)
    cv.poly([(244,84),(254,78),(253,92),(246,103),(238,96),(242,88)], col)
    # ---- hind leg ----
    cv.poly([(180,64),(196,66),(198,78),(205,88),(196,91),(189,80),(178,74)], col)
    cv.poly([(200,86),(208,88),(206,92),(198,92)], col)
    # ---- body ----
    cv.ellipse(142, 60, 16, 14, col)
    cv.ellipse(164, 60, 22, 13, col)
    cv.ellipse(186, 60, 15, 13, col)
    cv.ellipse(160, 68, 20, 8, col)
    # ---- front leg ----
    cv.poly([(138,66),(150,68),(152,80),(158,89),(149,91),(143,80),(134,74)], col)
    cv.poly([(154,87),(162,89),(160,93),(152,93)], col)
    # ---- neck ----
    cv.poly([(100,42),(114,39),(132,47),(142,58),(138,69),(120,62),(104,58),(97,53)], col)
    # ---- dorsal spines ----
    for sx in range(128, 196, 8):
        sy = 48 + (sx - 128) // 12
        cv.poly([(sx, sy + 4), (sx + 3, sy - 6), (sx + 7, sy + 4)], col)
    # ---- head ----
    cv.ellipse(97, 48, 11, 8, col)
    cv.poly([(92,41),(74,49),(66,53),(70,58),(88,56),(98,53)], col)      # upper jaw
    cv.poly([(88,57),(72,61),(67,64),(74,67),(92,62)], col)               # lower jaw
    cv.poly([(99,39),(116,27),(126,25),(112,38),(104,44)], col)           # horn 1
    cv.poly([(97,44),(112,35),(120,35),(104,47)], col)                    # horn 2
    cv.poly([(96,55),(110,59),(105,64),(94,59)], col)                     # cheek spike
    cv.poly([(70,52),(58,54),(66,58)], col)                               # snout tip
    # ---- near wing (up-right) ----
    cv.poly([(156,52),(180,26),(206,10),(234,14),(218,28),(226,42),(206,50),
             (210,64),(186,64),(170,70)], col)
    return cv

dg_a = new_canvas(W, H, name="dg_rim2")
dg_b = new_canvas(W, H, name="dg_rim1")
dg_c = new_canvas(W, H, name="dg_core")
paint_dragon(dg_a, '#2a1730')
paint_dragon(dg_b, '#8a4a34')
paint_dragon(dg_c, '#130d1b')
dg_a.shift(3, 3)
dg_b.shift(1, 2)
dragon = flatten([dg_a, dg_b, dg_c], name="dragon")

# interior detail on the dragon
DM = dragon.color('#241a2e')
DW = dragon.color('#3b2a44')
DH = dragon.color('#5e3a4a')
# wing membrane ribs (near wing)
for (ex, ey) in [(234,14),(226,42),(210,64)]:
    dragon.line(162, 54, ex, ey, DM)
    dragon.line(163, 55, ex, ey + 1, DW)
dragon.line(156, 52, 206, 10, DW)
dragon.line(206, 10, 234, 14, DW)
# sun rim along the trailing edge of the near wing
dragon.line(234, 14, 226, 42, dragon.color('#7a5a4a'))
dragon.line(226, 42, 210, 64, dragon.color('#7a5a4a'))
dragon.line(210, 64, 186, 64, dragon.color('#5e3a4a'))
# far wing ribs
for (ex, ey) in [(84,18),(90,42),(102,58)]:
    dragon.line(146, 54, ex, ey, DM)
dragon.line(148, 52, 104, 14, DM)
# belly plates
for i in range(7):
    bx = 136 + i * 8
    dragon.line(bx, 70, bx + 3, 74, DW)
# back highlight along the spine (light from lower right)
dragon.line(120, 62, 190, 66, DH)
dragon.line(196, 62, 240, 88, DH)
dragon.line(104, 57, 130, 60, DH)
# horns catch the light
dragon.line(104, 43, 122, 28, dragon.color('#a8846a'))
dragon.line(102, 46, 116, 37, dragon.color('#8a6a58'))
# eye
dragon.circle(93, 47, 2, dragon.color('#ff8c1e'))
dragon.set(93, 47, dragon.color('#fff0a8'))
dragon.set(94, 46, dragon.color('#ffe08a'))
# teeth
TEETH = dragon.color('#d8cdb8')
for tx in (72, 76, 80, 84):
    dragon.poly([(tx, 57), (tx + 2, 57), (tx + 1, 60)], TEETH)
for tx in (74, 79, 84):
    dragon.poly([(tx, 61), (tx + 2, 61), (tx + 1, 58)], TEETH)
# fire in the mouth
dragon.poly([(66,55),(90,56),(90,62),(68,63)], dragon.color('#ff8c1e'))
dragon.poly([(70,57),(90,58),(90,61),(72,61)], dragon.color('#ffe08a'))

dragon.outline('#0b0712')
c.blit(dragon, 0, 0)

# ---- fire breath streaming down onto the castle ----
def breath():
    pts_out = [(70,56),(58,66),(46,78),(38,90),(34,100),(44,102),(52,90),
               (62,76),(74,64),(76,58)]
    c.poly(pts_out, F2)
    c.poly([(70,58),(60,68),(50,80),(43,91),(41,97),(47,97),(54,86),(64,74),(73,63)], F3)
    c.poly([(70,59),(62,69),(54,80),(48,90),(47,94),(51,92),(58,82),(66,72),(72,62)], F4)
    c.poly([(70,60),(64,69),(58,78),(53,86),(54,88),(60,80),(67,70)], F5)
breath()
# impact burst on the left tower roof
fire_glow_at(38, 96, 26, F2, 0.45)
flame(30, 104, 10, 26)
flame(40, 106, 12, 34)
flame(50, 104, 8, 20)
for i in range(26):
    a = i * 0.7
    rr = 12 + (i % 4) * 6
    import math
    sx = int(40 + rr * math.cos(a))
    sy = int(98 + rr * math.sin(a) * 0.7)
    if 0 <= sx < W and 0 <= sy < H:
        c.set(sx, sy, F4 if i % 3 else F5)

# =====================================================================
# 10.  ARROWS
# =====================================================================
ARR_S = c.color('#6b5a48')
ARR_H = c.color('#e0d8e8')
ARR_F = c.color('#b0a8c0')
import math
def arrow(x, y, ang, ln=7):
    dx = math.cos(ang)
    dy = math.sin(ang)
    x2 = int(x - dx * ln)
    y2 = int(y - dy * ln)
    c.line(x, y, x2, y2, ARR_S)
    c.line(int(x - dx * 2), int(y - dy * 2), x, y, ARR_H)
    c.set(x, y, ARR_H)
    c.set(int(x2 + dx * 1), int(y2 + dy * 1), ARR_F)
    c.set(int(x2 + dx * 2 + dy * 2), int(y2 + dy * 2 - dx * 2), ARR_F)
    c.set(int(x2 + dx * 2 - dy * 2), int(y2 + dy * 2 + dx * 2), ARR_F)

random.seed(21)
# volley arcing from the right (siege) toward the left
for i in range(24):
    t = i / 24.0
    x = int(252 - t * 200 + random.randrange(-4, 5))
    y = int(96 + 70 * (2 * t - 1) ** 2 + random.randrange(-4, 5))
    ang = math.atan2(-140 * (2 * t - 1) / 200.0, -1.0)
    arrow(x, y, ang, 7)
# volley from the wall going right
for i in range(18):
    t = i / 18.0
    x = int(16 + t * 210 + random.randrange(-4, 5))
    y = int(150 - 52 * (4 * t * (1 - t)) + random.randrange(-3, 4))
    arrow(x, y, math.atan2(52 * (4 * t - 2) / 210.0, 1.0), 6)

# =====================================================================
# 11.  FOREGROUND RAMPART + KNIGHTS
# =====================================================================
kn = new_canvas(W, H, name="knights")

ARM_D = kn.color('#232838')
ARM_M = kn.color('#454e63')
ARM_L = kn.color('#6f7b92')
ARM_H = kn.color('#a3aec2')
ARM_W = kn.color('#d08a5e')      # warm sunset rim on armour
OUT   = kn.color('#0d0a14')
TAB_R = kn.color('#8e2430')
TAB_RL= kn.color('#b8393a')
TAB_B = kn.color('#2f4a72')
TAB_BL= kn.color('#4a6a96')
GOLD  = kn.color('#d9a13c')
WOODS = kn.color('#4a3524')
WOODSL= kn.color('#6b4c31')
STEEL = kn.color('#c8ccd8')
CAPE  = kn.color('#5a1f2a')
CAPE2 = kn.color('#7d2c34')

def knight(cx, top, pose=0, tabard=TAB_R, tablit=TAB_RL, flip=False):
    """full figure; (cx,top) = centre-x, top of helmet. ~72px tall."""
    s = -1 if flip else 1
    def X(v):
        return cx + s * v
    # ---- cape flowing behind ----
    kn.poly([(X(-4), top + 20), (X(-14), top + 30), (X(-20), top + 48),
             (X(-16), top + 66), (X(-8), top + 58), (X(-10), top + 38),
             (X(-6), top + 26)], CAPE)
    kn.poly([(X(-6), top + 22), (X(-12), top + 32), (X(-16), top + 48),
             (X(-13), top + 60), (X(-9), top + 50), (X(-9), top + 34)], CAPE2)
    # ---- spear ----
    if pose != 3:
        sx = X(9)
        tilt = 0 if pose != 2 else 6
        kn.line(sx, top - 34, sx - tilt, top + 66, WOODS)
        kn.line(sx + 1, top - 34, sx - tilt + 1, top + 66, WOODSL)
        # head
        kn.poly([(sx - 1, top - 34), (sx + 1, top - 44), (sx + 3, top - 34),
                 (sx + 1, top - 31)], ARM_H)
        kn.line(sx + 1, top - 43, sx + 1, top - 33, STEEL)
        kn.rect(sx - 3, top - 33, 8, 2, GOLD)
    # ---- legs ----
    kn.rect(X(-6), top + 48, 5, 24, ARM_D)
    kn.rect(X(1), top + 48, 5, 24, ARM_M)
    kn.rect(X(-6), top + 60, 5, 3, ARM_L)
    kn.rect(X(1), top + 60, 5, 3, ARM_L)
    # ---- torso / tabard ----
    kn.rect(X(-7), top + 22, 14, 28, ARM_M)
    kn.rect(X(-7), top + 22, 4, 28, ARM_D)
    kn.rect(X(4), top + 22, 3, 28, ARM_L)
    kn.rect(X(-6), top + 24, 12, 26, tabard)
    kn.rect(X(-6), top + 24, 4, 26, kn.color('#5e1620') if tabard == TAB_R else kn.color('#22385a'))
    kn.rect(X(3), top + 24, 3, 26, tablit)
    # heraldic charge: a dragon/wyvern glyph
    kn.poly([(X(-3), top + 30), (X(3), top + 28), (X(2), top + 34),
             (X(4), top + 38), (X(-1), top + 36), (X(-4), top + 40)], GOLD)
    # belt
    kn.rect(X(-8), top + 44, 16, 3, WOODS)
    kn.rect(X(-2), top + 44, 4, 3, GOLD)
    # ---- pauldrons ----
    kn.ellipse(X(0), top + 22, 12, 5, ARM_M)
    kn.ellipse(X(-1), top + 21, 11, 4, ARM_L)
    kn.line(X(-11), top + 20, X(10), top + 19, ARM_H)
    # ---- arms ----
    kn.rect(X(-11), top + 24, 5, 16, ARM_D)     # shield arm
    kn.rect(X(6), top + 24, 5, 16, ARM_M)       # spear arm
    kn.rect(X(6), top + 24, 2, 16, ARM_L)
    # ---- helmet ----
    kn.rect(X(-6), top + 2, 13, 17, ARM_M)
    kn.rect(X(-6), top + 2, 4, 17, ARM_D)
    kn.rect(X(3), top + 2, 4, 17, ARM_L)
    kn.rect(X(-7), top, 14, 5, ARM_L)
    kn.line(X(-7), top, X(7), top, ARM_H)
    # visor slit + breaths
    kn.rect(X(-7), top + 8, 8, 3, OUT)
    kn.rect(X(-7), top + 8, 8, 1, ARM_D)
    for i in range(3):
        kn.set(X(-5 + i * 2), top + 14, OUT)
        kn.set(X(-5 + i * 2), top + 16, OUT)
    kn.line(X(-7), top + 12, X(-7), top + 18, ARM_H)
    # plume / crest
    if pose != 2:
        kn.poly([(X(-1), top - 1), (X(-6), top - 8), (X(2), top - 6),
                 (X(9), top - 2), (X(12), top + 6), (X(6), top + 4),
                 (X(3), top + 1)], TAB_RL)
        kn.poly([(X(0), top - 2), (X(-4), top - 6), (X(2), top - 5),
                 (X(8), top - 1), (X(10), top + 4), (X(5), top + 3)], TAB_R)
    # ---- shield ----
    if pose != 1:
        shx = X(-18)
        kn.poly([(shx, top + 24), (shx + s * 15, top + 24),
                 (shx + s * 15, top + 42), (shx + s * 8, top + 52),
                 (shx, top + 42)], TAB_B if tabard == TAB_R else TAB_R)
        kn.poly([(shx + s * 2, top + 26), (shx + s * 13, top + 26),
                 (shx + s * 13, top + 41), (shx + s * 8, top + 49),
                 (shx + s * 2, top + 41)], TAB_BL if tabard == TAB_R else TAB_RL)
        # charge
        kn.line(shx + s * 8, top + 28, shx + s * 8, top + 46, STEEL)
        kn.line(shx + s * 4, top + 33, shx + s * 12, top + 33, STEEL)
        # boss + rim
        kn.circle(shx + s * 8, top + 36, 2, ARM_H)
        kn.line(shx, top + 24, shx, top + 42, ARM_D)
    # warm rim light on the right (sun side)
    kn.line(X(7), top + 1, X(7), top + 18, ARM_W)
    kn.line(X(7), top + 22, X(7), top + 50, ARM_W)
    kn.line(X(6), top + 50, X(6), top + 71, ARM_W)

knight(14, 158, pose=0, tabard=TAB_R, tablit=TAB_RL)
knight(48, 162, pose=1, tabard=TAB_B, tablit=TAB_BL, flip=True)
knight(82, 156, pose=2, tabard=TAB_R, tablit=TAB_RL)
knight(118, 164, pose=0, tabard=TAB_B, tablit=TAB_BL, flip=True)
knight(154, 158, pose=3, tabard=TAB_R, tablit=TAB_RL)
knight(190, 162, pose=1, tabard=TAB_R, tablit=TAB_RL, flip=True)
knight(226, 157, pose=0, tabard=TAB_B, tablit=TAB_BL)
knight(250, 163, pose=2, tabard=TAB_R, tablit=TAB_RL, flip=True)

kn.outline(OUT)
c.blit(kn, 0, 0)

# ---- the rampart wall itself (in front of the knights' legs) ----
WALL_D = c.color('#1c1729')
WALL_M = c.color('#322b45')
WALL_L = c.color('#4a4162')
WALL_H = c.color('#6a5f85')
WALL_W = c.color('#96685a')

# wall walk floor visible through the crenels
c.rect(0, 212, W, 44, WALL_D)
for x in range(0, W, 6):
    c.line(x, 214, x + 3, 255, c.color('#241d33'))

# parapet: solid from y=224 down, merlons up to y=200
c.rect(0, 224, W, 32, WALL_M)
PER = 36
MW = 22
x = -4
while x < W:
    c.rect(x, 200, MW, 26, WALL_M)
    c.rect(x, 200, MW, 3, WALL_L)
    c.line(x, 200, x + MW - 1, 200, WALL_H)
    c.line(x + MW - 1, 200, x + MW - 1, 225, WALL_D)
    c.line(x + MW - 2, 201, x + MW - 2, 225, WALL_W)
    x += PER
c.rect(0, 222, W, 3, WALL_L)
c.line(0, 222, W - 1, 222, WALL_H)

# stone courses on the inner face
for yy in range(228, 256, 9):
    c.line(0, yy, W - 1, yy, WALL_D)
    off = ((yy // 9) % 2) * 13
    for xx in range(off, W, 26):
        c.line(xx, yy, xx, min(255, yy + 8), WALL_D)
        c.line(xx + 1, yy + 1, xx + 1, min(255, yy + 8), WALL_L)
# warm light spilling on the wall from the fires
for y in range(224, 256):
    for x in range(0, W):
        if bt(x, y) < 0.05 * (1.0 - (y - 224) / 40.0):
            c.set(x, y, WALL_W)

# torches on the parapet
def torch(tx, ty):
    c.rect(tx - 1, ty, 3, 10, WOODS)
    c.rect(tx - 2, ty - 2, 5, 3, c.color('#3a2a1c'))
    fire_glow_at(tx, ty - 4, 16, F2, 0.4)
    flame(tx, ty + 1, 5, 15)
torch(30, 206)
torch(166, 206)

# hanging banner on the wall
c.poly([(96,226),(124,226),(124,254),(110,246),(96,254)], TAB_R)
c.poly([(98,228),(122,228),(122,250),(110,243),(98,250)], TAB_RL)
c.poly([(104,232),(116,230),(114,238),(118,244),(108,241),(102,246)], GOLD)
c.line(96, 226, 124, 226, c.color('#5e1620'))

# =====================================================================
# 12.  EMBERS, HAZE, VIGNETTE
# =====================================================================
EMB1 = c.color('#ffb347')
EMB2 = c.color('#ff7a2f')
EMB3 = c.color('#ffe08a')
random.seed(99)
for i in range(110):
    x = random.randrange(0, W)
    y = random.randrange(20, 250)
    # concentrate near the fires (left / centre) and the breath impact
    w = math.exp(-((x - 70) ** 2) / 9000.0) + 0.6 * math.exp(-((x - 150) ** 2) / 12000.0)
    if random.random() < w * (1.0 - y / 300.0):
        c.set(x, y, EMB3 if random.random() < 0.25 else (EMB1 if random.random() < 0.6 else EMB2))

# atmospheric haze band just above the horizon
HAZE = c.color('#c98a5e')
for y in range(150, 172):
    for x in range(0, W):
        t = 1.0 - abs(y - 160) / 12.0
        if t > 0 and bt(x, y) < t * 0.16:
            c.set(x, y, HAZE)

# vignette
VIG = c.color('#0b0714')
for y in range(H):
    for x in range(W):
        d = ((x - 128) / 150.0) ** 2 + ((y - 128) / 150.0) ** 2
        if d > 0.72 and bt(x, y) < (d - 0.72) * 1.5:
            c.set(x, y, VIG)

# =====================================================================
print(c.stats_text())
print("colours used:", c.stats()['colors_used'])
p = view(c)
print("preview:", p)
save("dragon_battle", c, indexed=True)
finish(c)
