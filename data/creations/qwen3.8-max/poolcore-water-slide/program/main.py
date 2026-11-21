from pixelbench_api import *
import math, random

W = H = 128
c = new_canvas(W, H, name="poolcore")

# ---------------------------------------------------------------- geometry
VPX, VPY = 64.0, 44.0          # vanishing point (eye level)
BX0, BX1 = 22.0, 106.0         # back wall left / right
BY0, BY1 = 28.0, 60.0          # back wall top (ceiling) / bottom (waterline)
CH = VPY - BY0                 # 16  ceiling rise per scale unit
FH = BY1 - VPY                 # 16  floor drop per scale unit
RD = 0.04                      # depth step of the tile module
SEDGE = VPX / (VPX - BX0)      # scale where the side walls reach x=0 / x=128

def sn(n):      return 1.0 / (1.0 - RD * n)     # depth scale series
def cy_(s):     return VPY - CH * s             # ceiling y at scale s
def fy_(s):     return VPY + FH * s             # floor y at scale s
def lx_(s):     return VPX - (VPX - BX0) * s    # left wall x at scale s
def rx_(s):     return min(127.0, VPX + (BX1 - VPX) * s)
def bwx(x, s):  return VPX + (x - VPX) * s      # scale a back-wall x to depth s

def R(v): return int(round(v))

def ray_clip(px, py, dx, dy):
    t = 1e9
    if dx > 1e-9:   t = min(t, (127.5 - px) / dx)
    elif dx < -1e-9:t = min(t, (-0.5 - px) / dx)
    if dy > 1e-9:   t = min(t, (127.5 - py) / dy)
    elif dy < -1e-9:t = min(t, (-0.5 - py) / dy)
    return (min(127.4, max(0.4, px + dx * t)), min(127.4, max(0.4, py + dy * t)))

# ---------------------------------------------------------------- colours
CEIL_FAR  = '#c4d4e1'
CEIL_NEAR = '#a9c0d1'
CEIL_GRID = '#9db9ca'
LAMP      = '#ffffff'
LAMP_LO   = '#bcd9e8'
LAMP_GLOW = '#eef7fc'

GROUT     = '#a8c6d6'
TILE_W    = '#f4fbfd'
TILE_P    = '#e2eff6'
TILE_B    = '#cfe3ee'
ACC       = '#8dc3de'
ACC2      = '#6dabcb'
LBAND     = ['#f2f9fc', '#e6f1f7', '#d9e7f0', '#ccdee9', '#bfd4e1']

DARK      = '#101c26'
DARK2     = '#1b3140'
DARK3     = '#2c5164'
DARK4     = '#3f6f88'

WAT = ['#d8eef8', '#bde2ef', '#a0d5e7', '#83c6dd', '#68b4d3', '#52a3c9', '#4294bd']
GRID_L  = '#a5d8ea'
GRID_D  = '#6fb4d2'
RIP_HI  = '#e6f7ff'
RIP_HI2 = '#ffffff'
RIP_LO  = '#4796bf'
WLINE   = '#f2fcff'

SLIDE_L   = '#f4fafc'
SLIDE_S   = '#d3e3ec'
SLIDE_OUT = '#8fa9b8'
SLIDE_D   = '#6d8794'
MOUTH     = '#22404f'

FOAM2     = '#dff2fb'

RING_Y    = '#ffd23f'
RING_HI   = '#ffee9c'
RING_LO   = '#e5a91f'
RING_D    = '#b57d12'
RING_GL   = '#fff6c9'
SKIN      = '#eab48d'
SKIN_SH   = '#c98f68'
HAIR      = '#3f2b21'
HAIR_HI   = '#654433'
SUIT      = '#e0556f'
SUIT_SH   = '#b23a52'

ARCH_R    = '#4d84a3'
COL_R     = '#d8eef8'

def wcol(y):
    t = (y - 60) / 67.0
    t = max(0.0, min(1.0, t))
    return WAT[min(len(WAT) - 1, int(round(t * (len(WAT) - 1))))]

def water_xrange(y):
    if y < 60: return None
    if y <= 68:
        d = 22.0 * (y - 60) / 8.0
        return (R(22 - d), R(106 + d))
    return (0, 127)

def wline(x0, x1, y, col):
    r = water_xrange(y)
    if r is None: return
    a = max(x0, r[0]); b = min(x1, r[1])
    if a <= b: c.line(a, y, b, y, col)

# ---------------------------------------------------------------- 1. shell
c.poly([(0,0),(127,0),(127,20),(106,28),(22,28),(0,20)], CEIL_FAR)
c.poly([(0,19),(22,28),(22,60),(0,69)], LBAND[2])
c.poly([(127,19),(106,28),(106,60),(127,69)], LBAND[2])
c.rect(22, 28, 85, 33, GROUT)

# ceiling depth shading (slightly darker toward the viewer)
for y in range(0, 29):
    s = (VPY - y) / CH
    if s <= 1.0: continue
    col = CEIL_FAR if s < 1.9 else CEIL_NEAR
    a = max(0, R(lx_(s))); b = min(127, R(rx_(s)))
    if a <= b: c.line(a, y, b, y, col)

# ---------------------------------------------------------------- 2. back wall tiles
def hsh(i, j):
    v = (i * 73856093) ^ (j * 19349663)
    v = (v * 2654435761) & 0xffffffff
    return (v >> 11) & 0xff

for j in range(8):
    for i in range(21):
        x = 22 + i * 4; y = 28 + j * 4
        if j >= 6:
            col = ACC if (i + j) % 2 == 0 else ACC2
        else:
            h = hsh(i, j)
            col = TILE_W if h < 150 else (TILE_P if h < 225 else TILE_B)
        c.rect(x + 1, y + 1, 3, 3, col)

# ---------------------------------------------------------------- 3. side walls
svals = [sn(n) for n in (0, 2, 4, 6, 8)] + [SEDGE]
for k in range(5):
    sa, sb = svals[k], svals[k+1]
    c.poly([(R(lx_(sa)), R(cy_(sa))), (R(lx_(sb)), R(cy_(sb))),
            (R(lx_(sb)), R(fy_(sb))), (R(lx_(sa)), R(fy_(sa)))], LBAND[k])
    c.poly([(R(rx_(sa)), R(cy_(sa))), (R(rx_(sb)), R(cy_(sb))),
            (R(rx_(sb)), R(fy_(sb))), (R(rx_(sa)), R(fy_(sa)))], LBAND[k])

for s in svals:
    c.line(R(lx_(s)), R(cy_(s)), R(lx_(s)), R(fy_(s)), GROUT)
    c.line(R(rx_(s)), R(cy_(s)), R(rx_(s)), R(fy_(s)), GROUT)
for y0 in range(28, 61, 4):
    ye = R(VPY + (y0 - VPY) * SEDGE)
    c.line(22, y0, 0, ye, GROUT)
    c.line(106, y0, 127, ye, GROUT)

# ---------------------------------------------------------------- 4. ceiling grid + lamps
for n in range(0, 18, 2):
    s = sn(n); y = R(cy_(s))
    if y < 0: break
    a = max(0, R(lx_(s))); b = min(127, R(rx_(s)))
    if a <= b: c.line(a, y, b, y, CEIL_GRID)
for xb in range(22, 107, 8):
    ex, ey = ray_clip(float(xb), BY0, xb - VPX, BY0 - VPY)
    c.line(xb, R(BY0), R(ex), R(ey), CEIL_GRID)

STRIPS = [(30, 38), (46, 54), (74, 82), (90, 98)]
for (a, b) in STRIPS:                       # glow pass
    for y in range(R(BY0), -1, -1):
        s = (VPY - y) / CH
        if s < 1.0: continue
        xa = R(bwx(a, s)) - 2; xb = R(bwx(b, s)) + 2
        c.line(xa, y, xb, y, LAMP_GLOW)
for (a, b) in STRIPS:                       # lamp pass
    for y in range(R(BY0), -1, -1):
        s = (VPY - y) / CH
        if s < 1.0: continue
        xa = R(bwx(a, s)); xb = R(bwx(b, s))
        c.line(xa, y, xb, y, LAMP)
        c.line(xa, y, xa, y, LAMP_LO)
        c.line(xb, y, xb, y, LAMP_LO)
# ---------------------------------------------------------------- 5. archway (slide tunnel)
AX0, AX1, AY0 = 28, 44, 33
c.rect(AX0 - 1, AY0 - 1, (AX1 - AX0) + 3, (60 - AY0) + 2, TILE_P)
c.rect(AX0, AY0, AX1 - AX0 + 1, 60 - AY0 + 1, DARK)
for y in range(AY0, 61):
    t = (y - AY0) / float(60 - AY0)
    col = DARK if t < 0.45 else (DARK2 if t < 0.75 else DARK3)
    c.line(AX0, y, AX1, y, col)
c.line(AX0, 60, AX1, 60, DARK4)

# ---------------------------------------------------------------- 6. columns
def column(cx_bw, s, w_bw):
    x0 = R(bwx(cx_bw - w_bw / 2.0, s)); x1 = R(bwx(cx_bw + w_bw / 2.0, s))
    yt = R(cy_(s)); yb = R(fy_(s))
    c.rect(x0 - 1, yt, x1 - x0 + 3, yb - yt + 1, SLIDE_D)
    c.rect(x0, yt, x1 - x0 + 1, yb - yt + 1, TILE_P)
    for y0 in range(28, 61, 4):
        yy = R(VPY + (y0 - VPY) * s)
        if yt <= yy <= yb: c.line(x0, yy, x1, yy, GROUT)
    step = max(3, (x1 - x0 + 1) // 2)
    for xx in range(x0 + step, x1, step):
        c.line(xx, yt, xx, yb, GROUT)
    c.rect(x1 - 1, yt, 2, yb - yt + 1, SLIDE_S)
    c.rect(x0, yt, 1, yb - yt + 1, LAMP)
    c.rect(x0 - 1, yt, (x1 - x0) + 3, 2, LAMP)
    c.rect(x0 - 1, yb - 2, (x1 - x0) + 3, 3, SLIDE_S)
    return (x0, x1, yt, yb)

colA = column(52, sn(3), 7)
colB = column(96, sn(3), 7)

# ---------------------------------------------------------------- 7. water base
for y in range(60, 128):
    r = water_xrange(y)
    c.line(r[0], y, r[1], y, wcol(y))

wline(22, 106, 60, WLINE)
wline(22, 106, 61, RIP_HI)
for y in range(60, 69):
    d = 22.0 * (y - 60) / 8.0
    c.set(R(22 - d), y, WLINE); c.set(R(106 + d), y, WLINE)

# submerged floor grid
for xb in range(22, 107, 8):
    ex, ey = ray_clip(float(xb), 60.0, xb - VPX, 16.0)
    yend = min(127, R(ey))
    for y in range(61, yend + 1):
        t = (y - 60) / max(1e-6, (ey - 60))
        xx = R(xb + (ex - xb) * t)
        rr_ = water_xrange(y)
        if rr_ and rr_[0] <= xx <= rr_[1]:
            c.set(xx, y, GRID_D if y > 84 else GRID_L)
for n in range(0, 26, 2):
    y = R(fy_(sn(n)))
    if y < 61 or y > 127: continue
    r = water_xrange(y)
    c.line(r[0], y, r[1], y, GRID_L if y < 80 else GRID_D)

# ---------------------------------------------------------------- 8. reflections
def refl(X0, X1, y0, y1, col, dens=0.6, wob=1, seed=3):
    rr = random.Random(seed)
    s0 = (y0 - VPY) / FH
    B0 = VPX + (X0 - VPX) / s0 if s0 else X0
    B1 = VPX + (X1 - VPX) / s0 if s0 else X1
    for y in range(max(61, y0), y1 + 1):
        if rr.random() > dens: continue
        s = (y - VPY) / FH
        xa = R(bwx(B0, s)) + rr.randint(-wob, wob)
        xb = R(bwx(B1, s)) + rr.randint(-wob, wob)
        wline(xa, xb, y, col)

refl(22, 106, 61, 68, RIP_HI, dens=0.4, wob=1, seed=21)
refl(AX0, AX1, 61, 72, ARCH_R, dens=0.5, wob=1, seed=22)
refl(colA[0], colA[1], colA[3] + 1, 92, COL_R, dens=0.55, wob=1, seed=23)
refl(colB[0], colB[1], colB[3] + 1, 92, COL_R, dens=0.55, wob=1, seed=24)
for (a, b) in STRIPS:
    refl(a, b, 61, 96, RIP_HI, dens=0.2, wob=2, seed=30 + a)

# ---------------------------------------------------------------- 9. ripples
rr = random.Random(7)
for i in range(150):
    y = rr.randint(62, 127)
    if y < 70 and rr.random() < 0.5: continue
    s = (y - VPY) / FH
    r = water_xrange(y)
    L = max(2, int(rr.uniform(1.2, 3.0) * s))
    if r[1] - r[0] < L + 2: continue
    x = rr.randint(r[0] + 1, r[1] - L - 1)
    p = rr.random()
    col = RIP_HI if p < 0.62 else (RIP_HI2 if p < 0.8 else RIP_LO)
    for k in range(L):
        off = 0
        f = k / float(L - 1) if L > 1 else 0
        if 0.25 < f < 0.75: off = -1 if rr.random() < 0.4 else 0
        c.set(x + k, y + off, col)

# a few long gentle swell lines
for y in (68, 76, 88, 104, 118):
    r = water_xrange(y)
    x = r[0] + rr.randint(2, 10)
    while x < r[1] - 6:
        L = min(rr.randint(8, 18), r[1] - x)
        for k in range(L):
            off = -1 if L // 3 <= k <= 2 * L // 3 else 0
            c.set(x + k, y + off, RIP_HI)
        x += L + rr.randint(8, 20)

# ---------------------------------------------------------------- 10. water slide
def catmull(p0, p1, p2, p3, t):
    t2 = t * t; t3 = t2 * t
    out = []
    for i in range(2):
        out.append(0.5 * ((2*p1[i]) + (-p0[i] + p2[i]) * t +
                   (2*p0[i] - 5*p1[i] + 4*p2[i] - p3[i]) * t2 +
                   (-p0[i] + 3*p1[i] - 3*p2[i] + p3[i]) * t3))
    return tuple(out)

def spline(pts, per=26):
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        for j in range(per):
            out.append(catmull(P[i-1], P[i], P[i+1], P[i+2], j / float(per)))
    out.append(tuple(pts[-1]))
    return out

SL = spline([(34, 42), (50, 38), (66, 46), (77, 59), (84, 72), (92, 83)], 30)
N = len(SL)

# support pillar under the slide
c.rect(74, 62, 3, 18, SLIDE_S)
c.rect(74, 62, 1, 18, LAMP)
c.rect(76, 62, 1, 18, SLIDE_OUT)
refl(74, 77, 80, 92, COL_R, dens=0.45, wob=1, seed=41)

# slide reflection in the water (drawn before the tube)
for i in range(int(N * 0.55), N):
    x, y = SL[i]
    if y < 61: continue
    ry = min(127, R(y + (y - 60) * 0.30) + 4)
    for yy in range(R(y), ry + 1):
        if rr.random() < 0.5: continue
        wline(R(x) - 3, R(x) + 3, yy, COL_R)

for i in range(N):                                   # outline / underside
    x, y = SL[i]; u = i / float(N - 1)
    r = 3.2 + 4.0 * u
    c.ellipse(R(x), R(y) + 2, R(r) + 1, R(r * 0.8) + 1, SLIDE_OUT)
for i in range(N):                                   # body
    x, y = SL[i]; u = i / float(N - 1)
    r = 3.2 + 4.0 * u
    c.ellipse(R(x), R(y), R(r), R(r * 0.8), SLIDE_L)
for i in range(N):                                   # top highlight
    x, y = SL[i]; u = i / float(N - 1)
    r = 3.2 + 4.0 * u
    c.ellipse(R(x), R(y) - max(1, R(r * 0.45)), max(1, R(r * 0.45)), max(1, R(r * 0.22)), LAMP)
for i in range(N):                                   # bottom shade inside tube
    x, y = SL[i]; u = i / float(N - 1)
    r = 3.2 + 4.0 * u
    c.ellipse(R(x), R(y) + max(1, R(r * 0.45)), max(1, R(r * 0.66)), max(1, R(r * 0.24)), SLIDE_S)
for i in range(0, N, 7):                             # seam rings
    x, y = SL[i]; u = i / float(N - 1)
    r = 3.2 + 4.0 * u
    c.set(R(x), R(y) + R(r * 0.72), SLIDE_S)
    c.set(R(x) - 1, R(y) + R(r * 0.66), SLIDE_S)
    c.set(R(x) + 1, R(y) + R(r * 0.66), SLIDE_S)

# flume mouth at the arch
c.ellipse(34, 43, 4, 4, SLIDE_D)
c.ellipse(34, 43, 3, 3, MOUTH)

# splash at entry
sx, sy = SL[-1]
for i in range(10):
    a = rr.uniform(0, math.pi * 2); d = rr.uniform(2, 8)
    c.set(R(sx + math.cos(a) * d), R(sy + math.sin(a) * d * 0.45), FOAM2)
for rx_, ry_ in ((9, 4), (14, 6)):
    c.ellipse(R(sx), R(sy) + 2, rx_, ry_, FOAM2, fill=False)
c.ellipse(R(sx), R(sy) + 1, 6, 3, LAMP, fill=False)

# ---------------------------------------------------------------- 11. girl in swim ring
GCX, GCY, GRX, GRY = 46, 102, 14, 8
GIX, GIY = 8, 4

for rx_, ry_ in ((19, 11), (24, 14), (30, 17)):
    for t in range(0, 360, 4):
        if (t // 4 + rx_) % 3 == 0: continue
        a = math.radians(t)
        c.set(R(GCX + rx_ * math.cos(a)), R(GCY + ry_ * math.sin(a)), RIP_HI)
c.ellipse(GCX, GCY + 9, 13, 4, WAT[6])

def ring_rows(y0, y1):
    for y in range(y0, y1 + 1):
        dy = (y - GCY) / float(GRY)
        if abs(dy) > 1: continue
        xo = GRX * math.sqrt(1 - dy * dy)
        dyi = (y - GCY) / float(GIY)
        xi = GIX * math.sqrt(1 - dyi * dyi) if abs(dyi) <= 1 else 0.0
        if y <= GCY - 5:   col = RING_HI
        elif y <= GCY - 1: col = RING_Y
        elif y <= GCY + 3: col = RING_LO
        else:              col = RING_D
        a, b = R(GCX - xo), R(GCX + xo)
        ia, ib = R(GCX - xi), R(GCX + xi)
        if xi <= 0.01:
            c.line(a, y, b, y, col)
        else:
            c.line(a, y, ia - 1, y, col)
            c.line(ib + 1, y, b, y, col)
        if y <= GCY - 3:
            c.set(a + 1, y, RING_GL); c.set(b - 1, y, RING_GL)

ring_rows(GCY - GRY, GCY)                 # far half of the ring

c.ellipse(GCX, GCY, GIX, GIY, WAT[5])
c.ellipse(GCX, GCY + 1, GIX - 2, GIY - 1, WAT[6])

# --- the girl (seen from behind) ---
c.line(40, 96, 34, 101, SKIN); c.line(41, 97, 35, 102, SKIN)
c.line(52, 96, 58, 101, SKIN); c.line(51, 97, 57, 102, SKIN)
c.set(34, 101, SKIN_SH); c.set(58, 101, SKIN_SH)
c.poly([(40, 95), (52, 95), (53, 100), (52, 105), (40, 105), (39, 100)], SKIN)
c.poly([(50, 95), (52, 95), (53, 100), (52, 105), (49, 105)], SKIN_SH)
c.poly([(40, 99), (52, 99), (52, 105), (40, 105)], SUIT)
c.poly([(49, 99), (52, 99), (52, 105), (49, 105)], SUIT_SH)
c.rect(41, 95, 2, 5, SUIT)
c.rect(49, 95, 2, 5, SUIT)
c.rect(44, 92, 4, 3, SKIN_SH)
c.circle(GCX, 88, 5, HAIR)
c.poly([(41, 88), (51, 88), (50, 98), (46, 99), (42, 98)], HAIR)
c.circle(GCX, 87, 4, HAIR)
c.path('M42 85 Q46 82 50 85', HAIR_HI, fill=False)
c.line(43, 90, 43, 97, HAIR_HI)
c.set(48, 92, HAIR_HI); c.set(49, 95, HAIR_HI)
c.set(44, 99, HAIR); c.set(48, 99, HAIR)

ring_rows(GCY, GCY + GRY)                 # near half of the ring over her

c.set(GCX - 10, GCY - 4, RING_LO); c.set(GCX + 10, GCY - 4, RING_LO)
c.set(GCX - 12, GCY + 2, RING_D);  c.set(GCX + 12, GCY + 2, RING_D)

# her reflection
for y in range(GCY + 10, 122):
    if random.Random(y * 7).random() < 0.5: continue
    hw = max(2, int(6 * (0.6 + (y - GCY) * 0.03)))
    off = int(round(1.6 * math.sin((y - GCY) * 0.7)))
    wline(GCX - hw + off, GCX + hw + off, y, RING_LO if y % 3 else RING_D)

# ---------------------------------------------------------------- 12. atmosphere
for y in range(61, 66):
    r = water_xrange(y)
    for x in range(r[0], r[1] + 1):
        if (x * 7 + y * 13) % 6 == 0:
            c.set(x, y, RIP_HI)

print(c.stats_text())
view(c)
save("poolcore", c, indexed=True)
finish(c)
