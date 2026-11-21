import math
from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="result")


def P(h, n):
    return c.color(h, name=n)


# ============================ palette ============================
CEIL  = P('#c6d7e4', 'ceil')
CEIL2 = P('#b3c6d6', 'ceil2')
CEIL3 = P('#dbe8f2', 'ceil3')
CEILG = P('#bccfe0', 'ceil_g')
PW    = P('#ffffff', 'white')
PE    = P('#e4f2fa', 'panel_e')

WA  = P('#e9f5fb', 'wa')
WB  = P('#dceff8', 'wb')
WC  = P('#c8e5f2', 'wc')
WD  = P('#b4d9eb', 'wd')
WE  = P('#a3ccdf', 'we')
GR  = P('#b4cbd8', 'grout')
CL  = P('#fdfeff', 'col_l')
CM  = P('#e9f3fa', 'col_m')
CD  = P('#c9dce8', 'col_d')
CDD = P('#a3c1d2', 'col_dd')
CG  = P('#b2ccda', 'col_g')

DK  = P('#f1f9fd', 'deck')
DK2 = P('#e5f2fa', 'deck2')
DKG = P('#c6dae6', 'deck_g')
DKS = P('#a9c4d4', 'deck_s')

CP  = P('#fdffff', 'cope')
CPD = P('#d7e8f0', 'cope_d')
CPS = P('#b3cede', 'cope_s')

W0   = P('#f0fbfe', 'w0')
W1   = P('#e3f6fc', 'w1')
W2   = P('#d3f2fa', 'w2')
W3   = P('#c2ebf6', 'w3')
W4   = P('#b0e1f2', 'w4')
W5   = P('#9dd6eb', 'w5')
W6   = P('#89c9e1', 'w6')
WHI  = P('#feffff', 'w_hi')
WSH  = P('#5ea1b9', 'w_sh')
WMID = P('#97cddf', 'w_mid')

SHI = P('#fffffe', 'sl_hi')
SL  = P('#f2f8fc', 'sl_l')
SM  = P('#dde9f1', 'sl_m')
SD  = P('#bdd0de', 'sl_d')
SDD = P('#9ab0c3', 'sl_dd')
SE  = P('#7b91a6', 'sl_edge')

HAIR  = P('#423a52', 'hair')
HAIRL = P('#6c6290', 'hair_l')
SKIN  = P('#fbdcb4', 'skin')
SKIND = P('#dcae84', 'skin_d')
SUIT  = P('#2f7488', 'suit')

RY  = P('#ffd83f', 'ring_y')
RD  = P('#e2a428', 'ring_d')
RL  = P('#fff7b0', 'ring_l')
SPL = P('#eafaff', 'splash')

LIGHT = {W0: WHI, W1: W0, W2: W1, W3: W2, W4: W3, W5: W4, W6: W5}


# ============================ helpers ============================
def hspan(y, xa, xb, col):
    if y < 0 or y >= H:
        return
    a = int(round(xa))
    b = int(round(xb))
    if a < 0:
        a = 0
    if b > W - 1:
        b = W - 1
    if b >= a:
        c.line(a, y, b, y, col)


def dspan(y, xa, xb, col, par=0):
    if y < 0 or y >= H:
        return
    a = max(0, int(round(xa)))
    b = min(W - 1, int(round(xb)))
    for x in range(a, b + 1):
        if (x + y + par) % 2 == 0:
            c.set(x, y, col)


def dot(x, y, col):
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, col)


def br(x, y, k=1):
    if not (0 <= x < W and 0 <= y < H):
        return
    i = c.get(x, y)
    for _ in range(k):
        i = LIGHT.get(i, i)
    c.set(x, y, i)


def polyline(pts, col):
    for i in range(len(pts) - 1):
        c.line(int(round(pts[i][0])), int(round(pts[i][1])),
               int(round(pts[i + 1][0])), int(round(pts[i + 1][1])), col)


VPX, VPY = 64.0, 26.0


def through_vp(ax, ay, x):
    if abs(ax - VPX) < 1e-9:
        return ay
    t = (x - VPX) / (ax - VPX)
    return VPY + (ay - VPY) * t


# ============================ room shell ============================
c.poly([(0, 12), (24, 17), (103, 17), (127, 12), (127, 0), (0, 0)], CEIL, True)
for y in range(12, 17):
    t = (y - 12) / 4.0
    hspan(y, 24 * t, 127 - 24 * t, CEIL3)
hspan(17, 24, 103, CEIL2)

# dropped-ceiling tile grid
for y in (4, 8, 11, 14):
    if y < 12:
        a, b = 0, 127
    else:
        a = 24 * ((y - 12) / 4.0)
        b = 127 - 24 * ((y - 12) / 4.0)
    hspan(y, a, b, CEILG)
for xc in range(-42, 172, 13):
    x1 = 64 + (xc - 64) * 0.346
    c.line(xc, 0, int(round(x1)), 17, CEILG)

FIX = [((2, 6), 15, 41), ((2, 6), 87, 113),
       ((9, 12), 28, 49), ((9, 12), 79, 100),
       ((13, 15), 40, 56), ((13, 15), 72, 88)]
for ((y0, y1), x0, x1) in FIX:
    c.rect(x0 - 1, y0, (x1 - x0) + 2, (y1 - y0) + 1, PE)
    c.rect(x0, y0, x1 - x0, y1 - y0, PW)
    if y1 - y0 >= 3:
        hspan(y1 - 1, x0, x1 - 1, CEIL3)

# back wall mosaic
FX0, FX1, FY0, FY1 = 24, 103, 17, 44
for ty in range(FY0, FY1, 4):
    hgt = min(4, FY1 - ty)
    for tx in range(FX0, FX1, 4):
        w = min(4, FX1 - tx)
        ci, ri = (tx - FX0) // 4, (ty - FY0) // 4
        h = (ci * 7 + ri * 5) % 13
        if ty >= 39:
            col = WD if h % 3 else WC
        elif 27 <= ty < 31:
            col = WC if h % 3 else WB
        else:
            col = WA if h > 3 else WB
        c.rect(tx, ty, w, hgt, col)
for y in range(FY0, FY1, 4):
    c.line(FX0, y, FX1 - 1, y, GR)
for x in range(FX0, FX1, 4):
    c.line(x, FY0, x, FY1 - 1, GR)
hspan(FY0, FX0, FX1 - 1, WE)
hspan(43, FX0, FX1 - 1, GR)

# side walls
c.poly([(0, 12), (24, 17), (24, 44), (0, 55)], WA, True)
c.poly([(127, 12), (103, 17), (103, 44), (127, 55)], WA, True)
for yb in range(19, 44, 3):
    polyline([(24, yb), (0, through_vp(24, yb, 0))], GR)
    polyline([(103, yb), (127, through_vp(103, yb, 127))], GR)
for xj in [0, 4, 8, 11, 14, 16.6, 18.7, 20.4, 21.8, 22.9]:
    xi = int(round(xj))
    ytop = through_vp(24, 17, xi)
    ybot = through_vp(24, 44, xi)
    c.line(xi, int(round(ytop)) + 1, xi, int(round(ybot)) - 1, GR)
    c.line(127 - xi, int(round(ytop)) + 1, 127 - xi, int(round(ybot)) - 1, GR)
    for y in range(int(round(ytop)) + 1, int(round(ybot))):
        if (xi > 14) and ((y + xi) % 3 == 0):
            dot(xi, y, WB)
            dot(127 - xi, y, WB)
for x in range(0, 25):
    dot(x, int(round(through_vp(24, 17, x))), CEIL3)
    dot(127 - x, int(round(through_vp(24, 17, x))), CEIL3)
    ybot = int(round(through_vp(24, 44, x)))
    dot(x, ybot, WE)
    dot(127 - x, ybot, WE)
    dot(x, ybot - 1, WD)
    dot(127 - x, ybot - 1, WD)

# floor
c.poly([(0, 55), (24, 44), (103, 44), (127, 55), (127, 127), (0, 127)], DK, True)
for y in range(44, 49):
    for x in range(24, 104):
        if ((x // 5) + (y // 3)) % 2 == 0:
            c.set(x, y, DK2)
        if x % 5 == 0 or y == 47:
            c.set(x, y, DKG)

# perspective floor grid: rays to the vanishing point + level courses
for y in range(45, 118):
    s = (y - VPY) / (44.0 - VPY)
    tw = 4.6 * s
    j0 = int(math.floor((0 - VPX) / tw)) - 1
    j1 = int(math.ceil((127 - VPX) / tw)) + 1
    for j in range(j0, j1 + 1):
        x = VPX + j * tw
        if 0 <= x < W:
            dot(int(round(x)), y, DKG)
for yb in (48, 53, 59, 66, 74, 84, 96, 110):
    for x in range(0, W):
        dot(x, yb, DKG)
for (cx, cw) in ((26, 10), (92, 10)):
    for y in range(44, 56):
        for x in range(cx - 5, cx + cw + 5):
            if (x + y) % 3 == 0:
                dot(x, y, DKS)

# ============================ pool water ============================
FAR_Y, NEAR_Y = 52, 117
FXL, FXR = 39.0, 89.0
NXL, NXR = 0.0, 128.0


def wb(y):
    t = (y - FAR_Y) / float(NEAR_Y - FAR_Y)
    t = max(0.0, min(1.0, t))
    return (FXL + (NXL - FXL) * t, FXR + (NXR - FXR) * t)


# far coping lip
for y in (49, 50, 51):
    hspan(y, 33, 95, CP)
hspan(49, 34, 94, PW)
for x in range(34, 95, 6):
    dot(x, 50, CPS)
hspan(51, 34, 94, CPS)

# side coping rims
for y in range(FAR_Y, NEAR_Y + 4):
    yy = min(y, NEAR_Y)
    xa, xb = wb(yy)
    hspan(y, xa - 2.4, xa - 0.6, CP)
    hspan(y, xb + 0.6, xb + 2.4, CP)
    dot(int(round(xa - 3.0)), y, CPD)
    dot(int(round(xb + 3.0)), y, CPD)

# water bands
BANDS = [(52, 57, W1), (57, 63, W2), (63, 70, W3), (70, 79, W4),
         (79, 90, W5), (90, NEAR_Y, W6)]
for (y0, y1, col) in BANDS:
    for y in range(y0, y1):
        xa, xb = wb(y)
        hspan(y, xa, xb, col)
for i in range(1, len(BANDS)):
    y0, _, col = BANDS[i]
    prev = BANDS[i - 1][2]
    xa, xb = wb(y0)
    dspan(y0 - 1, xa, xb, col)
    dspan(y0, xa, xb, prev)
    dspan(y0 + 1, xa, xb, col, 1)

# reflection of the lit far wall
xa, xb = wb(52)
hspan(52, xa, xb, WHI)
dspan(53, *wb(53), WHI)
for y in range(54, 60):
    xa, xb = wb(y)
    for x in range(int(xa), int(xb) + 1):
        if (x * 3 + y) % 7 < 2:
            br(x, y, 1)

# waterline trace + contact shadow
for y in range(FAR_Y, NEAR_Y):
    xa, xb = wb(y)
    dot(int(round(xa)), y, WSH)
    dot(int(round(xb)), y, WSH)
    dot(int(round(xa + 1)), y, WMID)
    dot(int(round(xb - 1)), y, WMID)
    if y < 62:
        dot(int(round(xa)), y - 1, WMID)
        dot(int(round(xb)), y - 1, WMID)

# faint pool-floor joints
for y in range(58, NEAR_Y, 1):
    if y % 11 in (0, 1):
        xa, xb = wb(y)
        for x in range(int(xa) + 2, int(xb) - 1):
            if (x * 2 + y) % 5 == 0:
                dot(x, y, WMID)
for xf in range(30, 106, 11):
    for y in range(58, NEAR_Y, 2):
        t = (y - VPY) / (58.0 - VPY)
        x = VPX + (xf - VPX) * t
        xa, xb = wb(y)
        if xa + 2 < x < xb - 2:
            dot(int(round(x)), y, WMID)


# ---- reflections of the ceiling lights ----
def streak(xc, y0, y1, hw, wob=1.0, freq=0.5, dash=5, duty=2, k=1, core=0):
    for y in range(y0, y1):
        w = hw * (0.7 + 0.6 * (y - y0) / max(1.0, (y1 - y0)))
        off = math.sin((y - y0) * freq) * wob
        if (y - y0) % dash < duty:
            a = max(0, int(round(xc - w + off)))
            b = min(W - 1, int(round(xc + w + off)))
            for x in range(a, b + 1):
                br(x, y, k)
            if core:
                cc = int(round(xc + off))
                for x in range(max(0, cc - core + 1), min(W, cc + core)):
                    br(x, y, 2)


streak(40, 52, 98, 3.2, wob=1.3, freq=0.42, dash=6, duty=2, core=1)
streak(88, 52, 98, 3.2, wob=1.3, freq=0.38, dash=6, duty=2, core=1)
streak(64, 52, 88, 2.2, wob=1.0, freq=0.55, dash=7, duty=2, core=1)
streak(52, 52, 68, 1.4, wob=0.8, freq=0.62, dash=6, duty=2)
streak(76, 52, 68, 1.4, wob=0.8, freq=0.58, dash=6, duty=2)
for (xc, dash) in ((31, 3), (97, 3)):
    for y in range(52, 80):
        w = 1.6 + 0.9 * (y - 52) / 28.0
        off = math.sin((y - 52) * 1.1) * 0.9
        if (y - 52) % dash < 2:
            a = max(0, int(round(xc - w + off)))
            b = min(W - 1, int(round(xc + w + off)))
            for x in range(a, b + 1):
                i = c.get(x, y)
                if i in (W1, W2, W3):
                    c.set(x, y, WSH if abs(x - xc) < 1 else WMID)


# ---- ripple lines ----
def ripple(y, amp, phase, dash=9, duty=3, freq=0.26, k=1):
    xa, xb = wb(y)
    for x in range(max(0, int(xa)), min(W, int(xb) + 1)):
        yy = y + int(round(math.sin((x + phase) * freq) * amp))
        if (x + phase) % dash < duty:
            br(x, yy, k)


for (y, amp, ph, d) in ((55, 0.3, 3, 9), (59, 0.4, 27, 10), (64, 0.5, 11, 11),
                        (70, 0.6, 49, 12), (76, 0.7, 21, 13), (83, 0.9, 63, 14),
                        (91, 1.1, 7, 15), (102, 1.3, 39, 17), (111, 1.5, 71, 19)):
    ripple(y, amp, ph, dash=d, duty=max(2, d // 3), k=1)

for i in range(60):
    x = 32 + ((i * 47) % 66)
    y = 56 + ((i * 23) % 56)
    xa, xb = wb(y)
    if xa + 1 < x < xb - 1 and (i % 3):
        br(x, y, 2)

# ============================ columns ============================
def column(x0, w, y0, y1):
    for y in range(y0, y1):
        for x in range(x0, x0 + w):
            rel = (x - x0) / float(w - 1)
            if rel < 0.16:
                col = CL
            elif rel < 0.40:
                col = CM
            elif rel < 0.74:
                col = CD
            else:
                col = CDD
            c.set(x, y, col)
    for y in range(y0, y1, 3):
        c.line(x0, y, x0 + w - 1, y, CG)
    for x in range(x0, x0 + w + 1, 3):
        c.line(x, y0, x, y1 - 1, CG)
    c.line(x0, y0, x0, y1 - 1, CL)
    c.line(x0 + 1, y0, x0 + 1, y1 - 1, CL)
    c.line(x0 + w - 1, y0, x0 + w - 1, y1 - 1, CDD)
    c.line(x0, y0, x0 + w - 1, y0, PW)
    c.rect(x0 - 1, y1 - 4, w + 2, 5, CM)
    c.line(x0 - 1, y1 - 4, x0 + w, y1 - 4, CL)
    c.line(x0 - 1, y1 - 1, x0 + w, y1 - 1, CDD)
    c.line(x0 - 1, y1, x0 + w, y1, CDD)
    for x in range(x0 - 1, x0 + w + 1, 3):
        dot(x, y1 - 2, CG)


column(26, 10, 13, 51)
column(92, 10, 13, 51)

# ============================ water slide ============================
WAY = [(139.0, 1.0), (127.0, 9.0), (115.0, 25.0), (108.0, 43.0),
       (106.0, 60.0), (100.0, 72.0), (91.0, 82.0), (86.0, 87.0)]


def catmull(pts, samples=30):
    ext = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for s in range(samples):
            u = s / float(samples)
            u2, u3 = u * u, u * u * u
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * u +
                       (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * u2 +
                       (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * u3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * u +
                       (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * u2 +
                       (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * u3)
            out.append((x, y))
    out.append(pts[-1])
    return out


PATH = catmull(WAY, 34)
NP = len(PATH)
NORM = []
for i in range(NP):
    j = min(i + 1, NP - 1)
    dx, dy = PATH[j][0] - PATH[i][0], PATH[j][1] - PATH[i][1]
    L = math.hypot(dx, dy) or 1.0
    NORM.append((-dy / L, dx / L))


def tube_r(t):
    return 3.4 + 4.6 * t


LX, LY = -0.42, -0.91


def shade_of(v):
    if v > 0.80:
        return SHI
    if v > 0.30:
        return SL
    if v > -0.16:
        return SM
    if v > -0.60:
        return SD
    return SDD


for i in range(0, NP, 2):
    t = i / float(NP - 1)
    x, y = PATH[i]
    nx, ny = NORM[i]
    hw = tube_r(t)
    for d in (-hw - 3.6, -hw - 2.0, hw + 2.0, hw + 3.6):
        px = int(round(x + d * nx)) + 5
        py = int(round(y + d * ny)) + 4
        if not (0 <= px < W and 0 <= py < H):
            continue
        if py < 17:
            dot(px, py, CEIL2)
        elif py < 44:
            dot(px, py, WE)
        elif py < 49:
            dot(px, py, DKS)
        elif py < FAR_Y:
            dot(px, py, CPS)
        else:
            dot(px, py, WSH if abs(d) > hw + 3 else WMID)

for i in range(NP):
    t = i / float(NP - 1)
    x, y = PATH[i]
    nx, ny = NORM[i]
    hw = tube_r(t) + 0.9
    d = -hw
    while d <= hw:
        dot(int(round(x + d * nx)), int(round(y + d * ny)), SE)
        d += 0.3

for i in range(NP):
    t = i / float(NP - 1)
    if t > 0.972:
        break
    x, y = PATH[i]
    nx, ny = NORM[i]
    hw = tube_r(t)
    lit = 1.0 if (nx * LX + ny * LY) > 0 else -1.0
    d = -hw
    while d <= hw:
        dot(int(round(x + d * nx)), int(round(y + d * ny)), shade_of((d / hw) * lit))
        d += 0.3

for i in range(NP):
    t = i / float(NP - 1)
    if t > 0.972:
        break
    x, y = PATH[i]
    nx, ny = NORM[i]
    hw = tube_r(t)
    s = 1.0 if (nx * LX + ny * LY) > 0 else -1.0
    if i % 2 == 0:
        d = hw * s * 0.55
        dot(int(round(x + d * nx)), int(round(y + d * ny)), SHI)
    d = -hw * s * 0.88
    dot(int(round(x + d * nx)), int(round(y + d * ny)), SDD)

SX, SY = 86, 87

# reflection of the flume in the water
for y in range(SY + 2, NEAR_Y):
    t = (y - SY) / float(NEAR_Y - SY)
    xc = SX - 10.0 * t * t + math.sin((y - SY) * 0.7) * 1.6
    w = 4.5 - 2.6 * t
    if (y - SY) % 5 < 3:
        for x in range(int(xc - w), int(xc + w) + 1):
            br(x, y, 1)

# ============================ splash ============================
for a in range(0, 360, 2):
    ar = math.radians(a)
    rr = 13.0 + math.sin(a * 0.2) * 1.6
    dot(int(round(SX + rr * math.cos(ar))),
        int(round(SY + 1 + rr * 0.45 * math.sin(ar))), WSH if a % 6 else WMID)
for (rx, ry, col) in ((11, 5, WMID), (9, 4, SPL), (6, 2, WHI), (3, 1, PW)):
    c.ellipse(SX, SY + 1, rx, ry, col)
for a in range(0, 360, 2):
    ar = math.radians(a)
    rr = 10.5 + math.sin(a * 0.2) * 1.4
    dot(int(round(SX + rr * math.cos(ar))),
        int(round(SY + 1 + rr * 0.45 * math.sin(ar))),
        PW if (a // 2) % 3 else WHI)
for k in range(16):
    ar = math.radians(k * 22.5 + 6)
    r = 6 + (k % 4) * 1.8
    dot(int(round(SX + math.cos(ar) * r)),
        int(round(SY + 1 + math.sin(ar) * r * 0.5)), PW if k % 3 else WHI)
for (rr, dy, duty) in ((14, 6, 2), (19, 9, 2), (25, 12, 3)):
    for a in range(0, 360, 3):
        if (a // 3) % 7 < duty:
            ar = math.radians(a)
            dot(int(round(SX + rr * math.cos(ar))),
                int(round(SY + dy + rr * 0.52 * math.sin(ar))),
                WHI if duty < 3 else SPL)

# ============================ girl in the swim ring ============================
GX, GY = 47, 101
ORX, ORY = 15.5, 7.2
IRX, IRY = 9.0, 3.6


def band(y, rxo, ryo, rxi, ryi, col):
    dyo = (y - GY) / ryo
    if abs(dyo) >= 1.0:
        return
    hwo = rxo * math.sqrt(1 - dyo * dyo)
    dyi = (y - GY) / ryi
    if abs(dyi) >= 1.0:
        hspan(y, GX - hwo, GX + hwo, col)
        return
    hwi = rxi * math.sqrt(1 - dyi * dyi)
    hspan(y, GX - hwo, GX - hwi, col)
    hspan(y, GX + hwi, GX + hwo, col)


def ring(y0, y1, hi=True):
    for y in range(y0, y1 + 1):
        band(y, ORX, ORY, ORX - 1.2, ORY - 0.6, RD)
        band(y, ORX - 1.2, ORY - 0.6, IRX + 1.2, IRY + 0.5, RY)
        if hi and y < GY:
            band(y, ORX - 1.8, ORY - 0.9, ORX - 4.0, ORY - 2.1, RL)
        band(y, IRX + 1.2, IRY + 0.5, IRX, IRY, RD)


# disturbed water around the ring
for y in range(GY - 11, GY + 12):
    if not (0 <= y < H):
        continue
    dy = (y - (GY + 2)) / 9.5
    if abs(dy) >= 1:
        continue
    hw = 19 * math.sqrt(1 - dy * dy)
    for x in range(int(GX - hw), int(GX + hw) + 1):
        i = c.get(x, y)
        if i in (W5, W6):
            c.set(x, y, W5)
c.ellipse(GX, GY + 3, 16, 7, W5)

# water inside the ring hole
c.ellipse(GX, GY, int(IRX), int(IRY), W5)
c.ellipse(GX, GY - 1, int(IRX) - 3, int(IRY) - 1, W4)
for a in range(0, 360, 4):
    ar = math.radians(a)
    dot(int(round(GX + (IRX - 1) * math.cos(ar))),
        int(round(GY + (IRY - 0.4) * math.sin(ar))), W4)

# ---------- the whole ring ----------
ring(GY - 7, GY + 7)

# ---------- the girl, seen from behind ----------
c.circle(GX, GY - 8, 4, HAIR)
for (dx, dy) in ((-4, 0), (4, 0), (-4, 1), (4, 1), (-3, 3), (3, 3), (-2, 4), (2, 4)):
    dot(GX + dx, GY - 8 + dy, HAIR)
dot(GX - 2, GY - 11, HAIRL)
dot(GX - 1, GY - 11, HAIRL)
dot(GX - 2, GY - 10, HAIRL)
dot(GX - 3, GY - 9, HAIRL)
dot(GX + 2, GY - 10, HAIRL)
dot(GX + 1, GY - 9, HAIRL)
dot(GX + 2, GY - 4, HAIRL)
dot(GX + 1, GY - 3, HAIRL)
for y in (GY - 4, GY - 3):
    dot(GX - 1, y, SKIND)
    dot(GX, y, SKIND)
for (y, xa, xb) in ((GY - 2, GX - 4, GX + 4), (GY - 1, GX - 5, GX + 5),
                    (GY, GX - 5, GX + 5), (GY + 1, GX - 4, GX + 4)):
    c.line(xa, y, xb, y, SKIN)
dot(GX - 5, GY - 1, SKIND)
dot(GX + 5, GY - 1, SKIND)
dot(GX - 5, GY, SKIND)
dot(GX + 5, GY, SKIND)
dot(GX - 4, GY + 1, SKIND)
dot(GX + 4, GY + 1, SKIND)
c.line(GX - 3, GY + 1, GX + 3, GY + 1, SUIT)
c.line(GX - 3, GY + 2, GX + 3, GY + 2, SUIT)
dot(GX - 2, GY, SKIND)
dot(GX + 2, GY, SKIND)
for (x0, y0, x1, y1) in ((GX - 5, GY - 2, GX - 9, GY), (GX + 5, GY - 2, GX + 9, GY)):
    c.line(x0, y0, x1, y1, SKIN)
    c.line(x0, y0 + 1, x1, y1 + 1, SKIND)
dot(GX - 10, GY + 1, SKIN)
dot(GX + 10, GY + 1, SKIN)

# near rim over her lower body
for y in range(GY + 1, GY + 8):
    band(y, ORX, ORY, ORX - 1.2, ORY - 0.6, RD)
    band(y, ORX - 1.2, ORY - 0.6, IRX + 1.2, IRY + 0.5, RY)
    band(y, IRX + 1.2, IRY + 0.5, IRX, IRY, RD)

# contact shadow at the waterline
for a in range(0, 181, 2):
    ar = math.radians(a)
    dot(int(round(GX + (ORX + 1.4) * math.cos(ar))),
        int(round(GY + (ORY + 1.5) * math.sin(ar))), WSH)
# inner rim shadow of the ring
for a in range(0, 360, 2):
    ar = math.radians(a)
    dot(int(round(GX + (IRX + 0.3) * math.cos(ar))),
        int(round(GY + (IRY + 0.1) * math.sin(ar))), RD)

# legs sinking in the water
for lx in (GX - 3, GX + 2):
    for y in range(GY + 5, GY + 13):
        k = y - (GY + 5)
        col = SKIND if k < 2 else (W4 if k < 5 else W5)
        dot(lx, y, col)
        dot(lx + 1, y, col)

# ripple rings spreading from her
for (rr, dy, col, duty) in ((18, 5, WHI, 2), (22, 7, WHI, 2), (27, 10, SPL, 3),
                            (33, 13, WHI, 3)):
    for a in range(0, 360, 3):
        if (a // 3) % 6 < duty:
            ar = math.radians(a)
            dot(int(round(GX + rr * math.cos(ar))),
                int(round(GY + dy + rr * 0.50 * math.sin(ar))), col)

# ============================ near coping + foreground deck ============================
c.rect(0, NEAR_Y, W, 4, CP)
c.line(0, NEAR_Y, W - 1, NEAR_Y, PW)
c.line(0, NEAR_Y + 1, W - 1, NEAR_Y + 1, CPD)
for x in range(0, W, 6):
    dot(x, NEAR_Y + 2, CPS)
c.line(0, NEAR_Y + 3, W - 1, NEAR_Y + 3, DKS)

DECK_Y = NEAR_Y + 4
for y in range(DECK_Y, H):
    for x in range(0, W):
        c.set(x, y, DK2 if (y // 5) % 2 == 0 else DK)
for y in range(DECK_Y, H, 5):
    c.line(0, y, W - 1, y, DKG)
for x in range(0, W, 9):
    c.line(x, DECK_Y, x, H - 1, DKG)

# ============================ finishing ============================
for (cx, rx) in ((38, 6), (64, 9), (89, 6)):
    c.ellipse(cx, 47, rx, 1, CP)
c.line(24, 48, 103, 48, CP)

# warm reflection of the yellow ring on the water in front of it
RYP = P('#f4e7a8', 'ring_ref')
RYQ = P('#e3d089', 'ring_ref2')
for y in range(GY + 9, NEAR_Y):
    t = (y - (GY + 9)) / float(NEAR_Y - (GY + 9))
    hw = 9.0 * (1.0 - 0.60 * t)
    xc = GX + math.sin((y - GY) * 0.9) * 1.6
    for x in range(int(round(xc - hw)), int(round(xc + hw)) + 1):
        if (x + y) % 2 == 0 and (y - GY) % 5 != 4:
            dot(x, y, RYP if abs(x - xc) < hw * 0.55 else RYQ)
for k in range(5):
    yy = GY + 11 + k * 2
    if yy < NEAR_Y:
        dot(int(round(GX + ((-1) ** k) * (2 + k))), yy, RYP)

# a last breath of light on the water and the foreground
dspan(56, 30, 98, WHI, 0)
for x in range(24, 104, 3):
    dot(x, 47, CP)

c.stats_text()
print('colours:', len(c.palette()))
save('poolcore-water-slide', c)
views = view(c)
print('preview:', views)
finish(c)
