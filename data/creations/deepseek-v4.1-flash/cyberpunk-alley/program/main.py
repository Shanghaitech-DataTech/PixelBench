# CYBERPUNK ALLEY - 128x128 pixel art
from math import sqrt, exp, sin, cos

W = H = 128
VPX, VPY = 64.0, 58.0
FLK = 62.0 / 64.0
RFK = 88.0 / 64.0

def lfl(x): return VPY + (VPX - x) * FLK
def rfl(x): return VPY + (x - VPX) * FLK
def lrf(x): return VPY - (VPX - x) * RFK
def rrf(x): return VPY - (x - VPX) * RFK

cv = new_canvas(W, H, name="alley")

HEX = {
 'ink':  '#05070d',
 'n0':   '#0a0e18', 'n1': '#101623', 'n2': '#17203a', 'n3': '#202b4a', 'n4': '#2b3859', 'n5': '#3a4a70',
 'sk0':  '#0b1020', 'sk1': '#131a33', 'sk2': '#1d2647', 'sk3': '#2b3660', 'sk4': '#414d7d',
 'hz0':  '#4a3a72', 'hz1': '#7a4e8e', 'hz2': '#b06aa0', 'hz3': '#e08aa8', 'hz4': '#ffc9a8',
 'cy0':  '#0a3540', 'cy1': '#10606e', 'cy2': '#19a3b8', 'cy3': '#38e0ec', 'cy4': '#b8feff',
 'mg0':  '#45102e', 'mg1': '#8c1650', 'mg2': '#d02a7c', 'mg3': '#ff63b0', 'mg4': '#ffb8dc',
 'am0':  '#3d1c08', 'am1': '#8a3f10', 'am2': '#d4701f', 'am3': '#ffab4a', 'am4': '#ffe2a8',
 'vi0':  '#2a1247', 'vi1': '#552583', 'vi2': '#8f4ac8', 'vi3': '#c98bff',
 'gn0':  '#10301a', 'gn1': '#1f6b2a', 'gn2': '#42c258', 'gn3': '#9dff8a',
 'gd0':  '#080b12', 'gd1': '#0e131d', 'gd2': '#151c29', 'gd3': '#1e2739', 'gd4': '#2a3651', 'gd5': '#3c4a6e',
 'wht':  '#eef4ff', 'wht2': '#b8c8e0',
 'rn0':  '#5f7f9a', 'rn1': '#8fb0c8', 'rn2': '#cfe4f2',
 'skin': '#c98a6a', 'skin2': '#7a4a38',
 'umb':  '#a8e8f0', 'umb2': '#6fc4d8', 'tint': '#2a5a6a',
 'wt0':  '#141a2a', 'wt1': '#1a2233', 'wt2': '#243049', 'wt3': '#31405e',
}
CL = {k: cv.color(v) for k, v in HEX.items()}

B4 = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

def clamp01(t): return 0.0 if t < 0 else (1.0 if t > 1 else t)
def dth(x, y): return (B4[y & 3][x & 3] + 0.5) / 16.0

def ramp(cols, t, x, y):
    t = clamp01(t)
    n = len(cols) - 1
    ft = t * n
    i = int(ft)
    if i >= n:
        i = n - 1; f = 1.0
    else:
        f = ft - i
    return cols[i + 1] if f > dth(x, y) else cols[i]

def hash01(x, y, s=0):
    v = (int(x) * 374761393 + int(y) * 668265263 + s * 1442695041) ^ 0x5bf03635
    v = (v ^ (v >> 13)) * 1274126177
    return ((v ^ (v >> 16)) % 10007) / 10007.0

def ok(x, y): return 0 <= x < W and 0 <= y < H

def S(x, y, col):
    x = int(x); y = int(y)
    if 0 <= x < W and 0 <= y < H:
        cv.set(x, y, col)

def F(x0, y0, x1, y1, col):
    for y in range(int(y0), int(y1) + 1):
        for x in range(int(x0), int(x1) + 1):
            S(x, y, col)

def m_poly(m, pts):
    m.update(poly_mask(pts))

def poly_mask(pts):
    m = set()
    n = len(pts)
    ys = [p[1] for p in pts]
    for y in range(int(min(ys)), int(max(ys)) + 1):
        xs = []
        for i in range(n):
            x1, y1p = pts[i]
            x2, y2p = pts[(i + 1) % n]
            if (y1p <= y < y2p) or (y2p <= y < y1p):
                t = (y - y1p) / (y2p - y1p)
                xs.append(x1 + (x2 - x1) * t)
        xs.sort()
        for i in range(0, len(xs) - 1, 2):
            for x in range(int(round(xs[i])), int(round(xs[i + 1])) + 1):
                if 0 <= x < W and 0 <= y < H:
                    m.add((x, y))
    return m

def m_rect(m, x0, y0, x1, y1):
    for y in range(int(y0), int(y1) + 1):
        for x in range(int(x0), int(x1) + 1):
            if 0 <= x < W and 0 <= y < H:
                m.add((x, y))

def m_ellipse(m, cx, cy, rx, ry):
    for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            dx = (x - cx) / (rx if rx else 1)
            dy = (y - cy) / (ry if ry else 1)
            if dx * dx + dy * dy <= 1.0 and 0 <= x < W and 0 <= y < H:
                m.add((x, y))

def m_line(m, x0, y0, x1, y1, w=0):
    n = int(max(abs(x1 - x0), abs(y1 - y0)))
    for i in range(n + 1):
        t = i / n if n else 0
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        for dy in range(-w, w + 1):
            for dx in range(-w, w + 1):
                X = int(round(x + dx)); Y = int(round(y + dy))
                if 0 <= X < W and 0 <= Y < H:
                    m.add((X, Y))

def paint(m, fn):
    for (x, y) in m:
        c = fn(x, y)
        if c is not None:
            cv.set(x, y, c)

def paint_c(m, col):
    for (x, y) in m:
        cv.set(x, y, col)

def glow_rect(x0, y0, x1, y1, r, cols, dens=0.85, seed=0, pw=2.0):
    for y in range(int(y0 - r), int(y1 + r) + 1):
        for x in range(int(x0 - r), int(x1 + r) + 1):
            if not ok(x, y):
                continue
            dx = max(x0 - x, 0, x - x1)
            dy = max(y0 - y, 0, y - y1)
            d = sqrt(dx * dx + dy * dy)
            if d > r:
                continue
            f = 1.0 - d / r
            k = int(clamp01(1.0 - d / (r + 1)) * (len(cols) - 1) + 0.0001)
            if hash01(x, y, seed) < (f ** pw) * dens + 0.05:
                S(x, y, cols[k])

def vstreak(x0, x1, y0, y1, cols, dens=0.8, seed=1, wob=1.5):
    n = len(cols) - 1
    for y in range(int(y0), int(y1) + 1):
        f = 1.0 - (y - y0) / float(max(1, y1 - y0))
        off = int(round(wob * sin(y * 0.55 + seed * 1.7)))
        for x in range(int(x0), int(x1) + 1):
            h = hash01((x + off) >> 1, y, seed)
            if h < f * f * dens:
                k = int(clamp01(1.0 - f) * n + 0.4)
                S(x + off, y, cols[k])

# ============================================================
# 1. SKY
# ============================================================
SKY = [CL['sk1'], CL['sk2'], CL['sk3'], CL['hz0'], CL['hz1'], CL['hz2'], CL['hz3'], CL['hz4']]

def sky_fn(x, y):
    g = exp(-((((x - 65) / 30.0) ** 2 + ((y - 56) / 24.0) ** 2)) * 0.95)
    v = clamp01((y + 14) / 78.0)
    cg = exp(-(((x - 60) / 56.0) ** 2 + ((y + 10) / 30.0) ** 2))
    t = clamp01(0.86 * g + 0.36 * v + 0.26 * cg)
    return ramp(SKY, t, x, y)

for y in range(H):
    for x in range(W):
        cv.set(x, y, sky_fn(x, y))

SKYM = poly_mask([(21.8, 0), (106.2, 0), (64.0, 58.0)])

# horizon haze band
for y in range(20, 44):
    for x in range(0, W):
        if (x, y) not in SKYM:
            continue
        f = exp(-(((x - 65) / 34.0) ** 2 + ((y - 40) / 13.0) ** 2))
        if hash01(x, y, 2) < f * 0.30:
            S(x, y, CL['hz1'] if f < 0.55 else CL['hz2'])

# ============================================================
# 2. distant skyline
# ============================================================
buildings = [(24, 33, 3), (34, 43, 9), (44, 51, 16), (52, 60, 6), (68, 76, 12), (78, 86, 5), (88, 99, 10), (100, 105, 2)]
for (bx0, bx1, bh) in buildings:
    top = max(0, bh)
    bot = int(min(lrf(bx0), rrf(bx1))) - 1
    if bot <= top:
        continue
    for y in range(top, bot + 1):
        for x in range(bx0, bx1 + 1):
            if (x, y) not in SKYM:
                continue
            col = CL['n1'] if hash01(x, y, 3) < 0.88 else CL['n0']
            if y == top:
                col = CL['n0']
            S(x, y, col)
    for y in range(top + 2, bot - 1, 3):
        for x in range(bx0 + 1, bx1, 2):
            if (x, y) not in SKYM:
                continue
            h = hash01(x, y, 9)
            if h < 0.22:
                S(x, y, CL['am2'] if h < 0.08 else (CL['cy2'] if h < 0.15 else CL['mg1']))

# ============================================================
# 3. FAR END  - flooding light / fog
# ============================================================
FOG = [CL['hz4'], CL['hz3'], CL['hz2'], CL['hz1'], CL['hz0']]

def fog_fn(x, y):
    d = sqrt(((x - 65) / 15.0) ** 2 + ((y - 66) / 27.0) ** 2)
    t = clamp01(1.02 - 0.60 * d)
    col = ramp([CL['sk2'], CL['hz0'], CL['hz1'], CL['hz2'], CL['hz3'], CL['hz4']], t, x, y)
    h = hash01(x, y, 4)
    if h < 0.10:
        col = CL['hz1']
    elif h > 0.94:
        col = CL['hz3']
    return col

for y in range(26, 73):
    for x in range(48, 81):
        S(x, y, fog_fn(x, y))

# dark overhang of the far building
for y in range(26, 36):
    for x in range(48, 81):
        col = CL['n1'] if (x * 7 + y * 3) % 11 < 8 else CL['n2']
        S(x, y, col)
for x in range(48, 81):
    S(x, 36, CL['n0'])
# magenta neon strip under the overhang
for x in range(50, 80):
    S(x, 37, CL['mg2'])
    S(x, 38, CL['mg3'])
    S(x, 39, CL['mg1'])
S(50, 37, CL['n0']); S(79, 37, CL['n0'])
glow_rect(50, 36, 79, 40, 7, [CL['mg3'], CL['mg2'], CL['mg1']], dens=0.42, seed=13)

# dark posts framing the bright far area
for (px0, px1) in ((51, 53), (73, 75)):
    for y in range(40, 72):
        for x in range(px0, px1 + 1):
            S(x, y, CL['n0'] if hash01(x, y, 5) < 0.8 else CL['n1'])
    for y in range(40, 72):
        S(px0, y, CL['n1'])

# bright doorway core
DW0, DW1, DYT = 58, 70, 51
for y in range(DYT, 73):
    for x in range(DW0, DW1):
        t = clamp01((y - DYT) / 22.0)
        col = CL['am4'] if t < 0.5 else (CL['am3'] if t < 0.8 else CL['am2'])
        if x == DW0 or x == DW1 - 1:
            col = CL['am2']
        S(x, y, col)
for x in range(DW0 - 1, DW1 + 1):
    S(x, DYT - 1, CL['am1'])
for y in range(DYT - 1, 73):
    S(DW0 - 1, y, CL['am1']); S(DW1, y, CL['am1'])
glow_rect(DW0 - 1, DYT - 1, DW1, 72, 12, [CL['am4'], CL['am3'], CL['am2'], CL['am1']], dens=0.55, seed=17, pw=1.5)

# a few silhouetted details far away
F(63, 44, 65, 46, CL['n0'])
F(63, 40, 63, 43, CL['n0'])

# ============================================================
# 4. NEAR WALLS
# ============================================================
LWM = poly_mask([(0, 0), (21.8, 0), (50, lrf(50)), (50, lfl(50)), (0, 120)])
RWM = poly_mask([(106.2, 0), (128, 0), (128, 120), (78, rfl(78)), (78, rrf(78))])

def lwall_fn(x, y):
    fl = lfl(x)
    d = fl - y
    if d < 3:
        return CL['wt0']
    base = CL['wt1']
    if x > 30 and hash01(x, y, 1) < 0.30:
        base = CL['wt2']
    h = hash01(x, y, 2)
    if h < 0.11:
        base = CL['wt0']
    elif h > 0.93:
        base = CL['wt2']
    if x in (2, 11, 20, 30, 40, 45):
        base = CL['wt0']
    for bh, bc in ((44, 'wt0'), (70, 'wt0'), (86, 'wt2'), (12, 'wt2')):
        yy = fl - bh * (VPX - x) / VPX
        if abs(y - yy) < 0.6:
            base = CL[bc]
    if d < 1.5:
        base = CL['wt2']
    return base

def rwall_fn(x, y):
    fl = rfl(x)
    d = fl - y
    if d < 3:
        return CL['wt0']
    base = CL['wt1']
    h = hash01(x, y, 4)
    if h < 0.11:
        base = CL['wt0']
    elif h > 0.93:
        base = CL['wt2']
    if x in (82, 92, 102, 112, 122):
        base = CL['wt0']
    for bh, bc in ((40, 'wt0'), (62, 'wt0'), (14, 'wt2')):
        yy = fl - bh * (x - VPX) / VPX
        if abs(y - yy) < 0.6:
            base = CL['wt0']
    if d < 1.5:
        base = CL['wt2']
    return base

paint(LWM, lwall_fn)
paint(RWM, rwall_fn)

# wall vertical pipes
for (px, w) in ((18, 1), (44, 1)):
    for y in range(0, 120):
        if (px, y) in LWM:
            S(px, y, CL['n0'])
            S(px + 1, y, CL['wt2'])
for y in range(0, 120):
    for px in (110, 111):
        if (px, y) in RWM:
            S(px, y, CL['n0'] if px == 110 else CL['wt2'])

# light spill on walls from neon signs (drawn after signs below)

# ============================================================
# 5. FLOOR
# ============================================================
FLM = poly_mask([(0, 120), (50, lfl(50)), (78, rfl(78)), (128, 120), (128, 128), (0, 128)])

def floor_fl(x):
    if x < 50:
        return lfl(x)
    if x > 78:
        return rfl(x)
    return 71.6

def floor_fn(x, y):
    d = y - floor_fl(x)
    t = clamp01(d / 56.0)
    col = ramp([CL['gd4'], CL['gd3'], CL['gd2'], CL['gd1']], t * 1.02, x, y)
    h = hash01(x, y, 7)
    if h < 0.09:
        col = CL['gd2']
    elif h > 0.93:
        col = CL['gd4']
    return col

paint(FLM, floor_fn)

# perspective lines on floor
for k in range(11):
    tx = 64 + (k - 5) * 7.5
    x0, y0 = 64.0, 71.6
    x1, y1 = 64 + (tx - 64) * 3.8, 127
    for i in range(71):
        t = i / 70.0
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        if hash01(int(x), int(y), 12) < 0.5:
            S(x, y, CL['gd1'])

# ============================================================
# 6. WET FLOOR REFLECTIONS
# ============================================================
# big mirror of the far light on the wet street
vstreak(40, 90, 72, 118, [CL['hz4'], CL['hz3'], CL['hz2'], CL['hz1'], CL['hz0']], dens=0.95, seed=31, wob=1.6)
vstreak(52, 78, 72, 108, [CL['am4'], CL['am3'], CL['am2'], CL['am1']], dens=0.80, seed=32, wob=1.0)
vstreak(30, 100, 76, 128, [CL['hz2'], CL['hz1'], CL['hz0']], dens=0.30, seed=38, wob=2.4)
# reflections of the side neon
vstreak(2, 16, 84, 128, [CL['cy3'], CL['cy2'], CL['cy1'], CL['cy0']], dens=0.75, seed=33, wob=1.8)
vstreak(16, 40, 86, 128, [CL['mg3'], CL['mg2'], CL['mg1'], CL['mg0']], dens=0.45, seed=34, wob=1.8)
vstreak(96, 127, 92, 128, [CL['am4'], CL['am3'], CL['am2'], CL['am1']], dens=0.60, seed=35, wob=1.4)
vstreak(84, 98, 80, 120, [CL['cy2'], CL['cy1'], CL['cy0']], dens=0.35, seed=36, wob=1.2)
vstreak(96, 127, 34, 70, [CL['mg2'], CL['mg1'], CL['mg0']], dens=0.22, seed=37, wob=1.0)
# horizontal ripple glints
for i, yy in enumerate(range(74, 128, 3)):
    for x in range(0, 128):
        if (x, yy) not in FLM:
            continue
        if hash01(x, yy, 40 + i) < 0.13:
            S(x, yy, CL['gd5'] if hash01(x, yy, 44) < 0.6 else CL['hz1'])

# ============================================================
# 7. puddles
# ============================================================
puddles = [(40, 114, 18, 4.5), (90, 108, 15, 3.5), (62, 124, 26, 4.5), (20, 128, 16, 3.0), (110, 124, 14, 3.0), (74, 96, 12, 2.5)]
for (px, py, rx, ry) in puddles:
    mm = set()
    m_ellipse(mm, px, py, rx, ry)
    for (x, y) in mm:
        d = abs(y - py) / ry
        if hash01(x, y, 21) < 0.6:
            S(x, y, CL['gd3'] if d > 0.5 else CL['gd2'])
    for (x, y) in mm:
        if (x, y - 1) not in mm:
            S(x, y, CL['gd5'] if hash01(x, y, 22) < 0.65 else CL['gd4'])
    for (x, y) in mm:
        h = hash01(x, y, 23)
        if h < 0.30:
            S(x, y, CL['hz2'] if h < 0.10 else (CL['cy1'] if h < 0.18 else CL['gd4']))

# neon reflections inside the foreground puddle
for y in range(112, 128):
    for x in range(46, 82):
        if (x, y) in FLM:
            h = hash01(x, y, 31)
            if h < 0.24:
                S(x, y, CL['mg1'] if h < 0.11 else CL['cy1'])

# ============================================================
# 8. SIGN HELPERS
# ============================================================
def wql(xa, xb, hlo, hhi):
    pts = []
    for x, h in ((xa, hlo), (xb, hlo), (xb, hhi), (xa, hhi)):
        s = (VPX - x) / VPX
        pts.append((x, lfl(x) - h * s))
    return pts

def wqr(xa, xb, hlo, hhi):
    pts = []
    for x, h in ((xa, hlo), (xb, hlo), (xb, hhi), (xa, hhi)):
        s = (x - VPX) / VPX
        pts.append((x, rfl(x) - h * s))
    return pts

def quad_fill(q, col):
    cv.poly([(int(round(p[0])), int(round(p[1]))) for p in q], col)

def quad_frame(q, col):
    n = len(q)
    for i in range(n):
        x0, y0 = q[i]; x1, y1 = q[(i + 1) % n]
        cv.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), col)

GL = [
 ["11111", "00100", "00100", "01110", "00100", "00100", "11111"],
 ["11111", "10001", "10101", "10101", "11111", "00100", "11111"],
 ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
 ["10101", "10101", "11111", "10101", "10101", "10101", "10101"],
]

def glyph(x, y, g, col, hot=None):
    pat = GL[g % len(GL)]
    for j, row in enumerate(pat):
        for i, ch in enumerate(row):
            if ch == '1':
                S(x + i, y + j, hot if (hot is not None and (i + j) % 5 == 0) else col)

# ---- LEFT vertical sign "NEON"
q = wql(2, 14, 28, 80)
glow_rect(2, 40, 14, 91, 9, [CL['cy2'], CL['cy1'], CL['cy0']], dens=0.40, seed=41, pw=1.6)
quad_fill(q, CL['n0'])
quad_fill(wql(3, 13, 30, 78), CL['cy0'])
for i, ch in enumerate("NEON"):
    cv.text(6, 47 + i * 10, ch, CL['cy2'], font="5x7")
    cv.text(5, 46 + i * 10, ch, CL['cy3'], font="5x7")
for i, ch in enumerate("NEON"):
    if ch in "EO":
        cv.text(5, 46 + i * 10, ch, CL['cy4'], font="5x7")
quad_frame(q, CL['cy1'])

# ---- LEFT fire escape
for (h0, h1) in ((26, 30), (48, 52)):
    # platform
    for i in range(21):
        x = 24 + i
        y = lfl(x) - (h0 + h1) * 0.5 * (VPX - x) / VPX
        S(x, y, CL['n0'])
        S(x, y - 1, CL['n2'] if i % 3 else CL['n0'])
    # railings
    for i in range(0, 21, 5):
        x = 24 + i
        ytop = lfl(x) - (h1 + 12) * (VPX - x) / VPX
        ybot = lfl(x) - h1 * (VPX - x) / VPX
        for y in range(int(ytop), int(ybot) + 1):
            S(x, y, CL['n0'])
    for i in range(21):
        x = 24 + i
        y = lfl(x) - (h1 + 12) * (VPX - x) / VPX
        S(x, y, CL['n0'])

# ---- LEFT windows / door
for (wx, wy, ww, wh, col) in [(23, 62, 7, 9, CL['am1']), (32, 67, 5, 7, CL['vi1']), (7, 34, 8, 10, CL['vi1']), (7, 50, 6, 7, CL['cy1'])]:
    for yy in range(wy, wy + wh):
        for xx in range(wx, wx + ww):
            S(xx, yy, col if hash01(xx, yy, 51) < 0.85 else CL['n0'])
    for xx in range(wx - 1, wx + ww + 1):
        S(xx, wy - 1, CL['n0'])
    for yy in range(wy - 1, wy + wh + 1):
        S(wx - 1, yy, CL['n0']); S(wx + ww, yy, CL['n0'])
glow_rect(23, 62, 29, 70, 5, [CL['am2'], CL['am1']], dens=0.30, seed=52)

# metal shutter door
for y in range(84, 112):
    for x in range(20, 33):
        if (x, y) not in LWM:
            continue
        S(x, y, CL['n1'] if (y % 3) else CL['n0'])
for x in range(20, 33):
    S(x, 83, CL['n0'])
    S(x, 84, CL['n2'])

# ---- LEFT protruding sign "BAR"
cv.line(14, 45, 24, 33, CL['n2'])
cv.line(14, 46, 24, 34, CL['n0'])
glow_rect(24, 22, 46, 36, 8, [CL['mg2'], CL['mg1'], CL['mg0']], dens=0.42, seed=61, pw=1.6)
for y in range(22, 37):
    for x in range(24, 47):
        S(x, y, CL['n0'] if not (x == 24 or x == 46 or y == 22 or y == 36) else CL['mg1'])
cv.text(27, 25, "BAR", CL['mg4'], spacing=1, font="5x7")
for x in range(25, 46, 2):
    S(x, 34, CL['mg1'])

# ---- RIGHT big sign "OPEN"
q = wqr(96, 126, 50, 86)
glow_rect(96, 34, 127, 70, 9, [CL['mg2'], CL['mg1'], CL['mg0']], dens=0.35, seed=71, pw=1.6)
quad_fill(q, CL['n0'])
quad_fill(wqr(98, 124, 52, 84), CL['mg0'])
quad_frame(q, CL['mg1'])
cv.text(100, 50, "OPEN", CL['mg2'], font="5x7")
cv.text(100, 49, "OPEN", CL['mg4'], spacing=1, font="5x7")
for x in range(99, 124, 3):
    S(x, 58, CL['mg1'])
    S(x, 59, CL['mg2'])

# ---- RIGHT small cyan sign
q = wqr(88, 95, 18, 56)
glow_rect(87, 58, 96, 79, 6, [CL['cy2'], CL['cy1'], CL['cy0']], dens=0.40, seed=81, pw=1.6)
quad_fill(q, CL['n0'])
quad_frame(q, CL['cy1'])
for i in range(3):
    glyph(89, 62 + i * 5, i, CL['cy3'], CL['cy4'])

# ============================================================
# 9. VENDING MACHINES
# ============================================================
def vending(xa, xb, htop, framecol, panelcol, cancols, seed):
    q = wqr(xa, xb, 0, htop)
    quad_fill(q, CL['n0'])
    qi = wqr(xa + 2, xb - 1, 4, htop - 4)
    quad_fill(qi, panelcol)
    xs = [p[0] for p in qi]; ys = [p[1] for p in qi]
    x0 = int(min(xs)); x1 = int(max(xs)); y0 = int(min(ys)); y1 = int(max(ys))
    for yy in range(y0 + 1, y1):
        for xx in range(x0 + 1, x1):
            if (xx - x0) % 3 == 2 or (yy - y0) % 3 == 2:
                S(xx, yy, CL['n0'])
            else:
                h = hash01((xx - x0) // 3, (yy - y0) // 3, seed)
                S(xx, yy, cancols[int(h * 5) % len(cancols)])
    qd = wqr(xa + 2, xb - 1, 0, 2)
    quad_fill(qd, CL['ink'])
    F(x0, y0 - 1, x1, y0 - 1, framecol)
    quad_frame(q, framecol)
    glow_rect(xa, y0 - 2, xb, y1, 7, [panelcol, cancols[0]], dens=0.30, seed=seed + 5)

vending(99, 112, 42, CL['am2'], CL['am1'], [CL['am3'], CL['mg2'], CL['cy2'], CL['gn2'], CL['am4']], 91)
vending(114, 126, 45, CL['cy2'], CL['cy1'], [CL['cy3'], CL['mg3'], CL['am3'], CL['cy4'], CL['gn3']], 95)
# floor light spill in front of vending machines
for y in range(96, 128):
    for x in range(94, 128):
        if (x, y) in FLM:
            h = hash01(x, y, 99)
            if h < 0.30:
                S(x, y, CL['am1'] if h < 0.16 else CL['am2'])

# ============================================================
# 10. CABLES + LAMPS
# ============================================================
def cable(x0, y0, x1, y1, sag, col, w=0, hi=None):
    n = int(max(abs(x1 - x0), abs(y1 - y0), 1))
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + sag * 4 * t * (1 - t)
        for d in range(-w, w + 1):
            S(x, y + d, col)
        if hi is not None:
            S(x, y - w - 1, hi)

cable(18, 6, 110, 2, 20, CL['n0'], 0, CL['n3'])
cable(22, 18, 106, 12, 14, CL['ink'], 0, CL['n4'])
cable(-2, 32, 130, 24, 17, CL['ink'], 1, CL['n4'])
cable(38, 30, 98, 40, 10, CL['n0'], 0, CL['n3'])
cable(30, 10, 34, 38, 0, CL['ink'], 0)
cable(86, 16, 90, 40, 0, CL['ink'], 0)
cable(58, 4, 62, 24, 0, CL['ink'], 0)

# hanging lamp on the left wall
for yy in range(26, 40):
    S(43, yy, CL['n2'])
glow_rect(43, 39, 45, 42, 8, [CL['am4'], CL['am3'], CL['am2'], CL['am1']], dens=0.80, seed=101)
F(43, 39, 45, 41, CL['am3'])
S(44, 40, CL['am4'])
F(43, 42, 45, 42, CL['am0'])

# ============================================================
# 11. PERSON + TRANSPARENT UMBRELLA
# ============================================================
P = set()
m_line(P, 52, 94, 56, 86, 1)
m_rect(P, 45, 82, 51, 90)
m_ellipse(P, 48, 79, 6, 7)
m_poly(P, [(42, 86), (56, 86), (59, 104), (61, 112), (35, 112), (37, 104)])
m_rect(P, 42, 112, 47, 123)
m_rect(P, 51, 112, 57, 123)
m_rect(P, 40, 120, 48, 124)
m_rect(P, 51, 120, 59, 124)

for y in range(120, 128):
    for x in range(34, 66):
        dx = (x - 50) / 16.0
        dy = (y - 124) / 4.5
        if dx * dx + dy * dy < 1 and hash01(x, y, 111) < 0.75:
            S(x, y, CL['gd0'])

paint_c(P, CL['ink'])
for (x, y) in list(P):
    if (x - 1, y) not in P:
        S(x, y, CL['cy3'] if y < 104 else CL['cy1'])
    if (x + 1, y) not in P:
        S(x, y, CL['mg2'] if y < 100 else CL['mg1'])
    if (x, y - 1) not in P and y < 92:
        S(x, y, CL['cy2'])
S(45, 78, CL['skin2']); S(45, 80, CL['skin2']); S(50, 79, CL['skin'])

# umbrella shaft
for y in range(51, 88):
    S(56, y, CL['n2'])
    S(55, y, CL['wht2'])
S(56, 50, CL['wht'])

UCX, UHW, UTOP, URIM = 56.0, 19.0, 52.0, 67.0

def utop(x):
    t = (x - UCX) / UHW
    return UTOP + 15.0 * t * t

def ubot(x):
    t = (x - UCX) / UHW
    if abs(t) >= 1:
        return URIM
    return URIM + 6.0 * sqrt(1 - t * t)

CAN = set()
for x in range(int(UCX - UHW), int(UCX + UHW) + 1):
    for y in range(int(round(utop(x))), int(round(ubot(x))) + 1):
        if ok(x, y):
            CAN.add((x, y))

# glass: sparse tint so the light behind shows through
for (x, y) in CAN:
    edge = min(y - utop(x), ubot(x) - y)
    h = hash01(x, y, 121)
    if edge < 1.0:
        S(x, y, CL['umb2'] if h < 0.7 else CL['tint'])
    elif h < 0.13:
        S(x, y, CL['tint'])
    elif h < 0.18:
        S(x, y, CL['umb2'])

# dome outline
for x in range(int(UCX - UHW), int(UCX + UHW) + 1):
    y = utop(x)
    if abs(x - UCX) < UHW - 0.5:
        S(x, y, CL['umb'] if hash01(x, int(y), 123) < 0.75 else CL['umb2'])
# ribs
for xr in (-13.5, -7, 0, 7, 13.5):
    for i in range(24):
        t = i / 23.0
        x = UCX + xr * t
        y = UTOP + 15.0 * t * t
        S(x, y, CL['umb2'] if 0.15 < t < 0.9 else CL['umb'])
# front rim (bright)
for x in range(int(UCX - UHW), int(UCX + UHW) + 1):
    y = ubot(x)
    h = hash01(x, int(y), 131)
    S(x, y, CL['wht'] if h < 0.25 else CL['umb'])
    if abs(x - UCX) > 13:
        S(x, y + 1, CL['umb2'])
# neon tint on the rim
for x in range(int(UCX - UHW), int(UCX + UHW) + 1):
    y = int(round(ubot(x)))
    if x < UCX - 8 and hash01(x, y, 141) < 0.55:
        S(x, y, CL['cy4'])
    elif x > UCX + 8 and hash01(x, y, 142) < 0.55:
        S(x, y, CL['mg4'])
S(56, 51, CL['wht'])
# drips
for (dx, dl) in [(-16, 5), (-9, 3), (9, 4), (15, 6), (3, 3), (-4, 4)]:
    xx = int(UCX + dx)
    yy = int(round(ubot(xx))) + 1
    for k in range(dl):
        if ok(xx, yy + k):
            S(xx, yy + k, CL['umb'] if k < dl - 1 else CL['cy3'])
# highlight arcs on the glass
for i in range(13):
    t = i / 12.0
    x = 41 + 14 * t
    S(x, utop(x) + 1.6 + 1.2 * (1 - t), CL['umb2'])
for i in range(9):
    t = i / 8.0
    x = 63 + 11 * t
    S(x, utop(x) + 2.4, CL['tint'])

# ============================================================
# 12. RAIN
# ============================================================
class RNG:
    def __init__(self, s): self.s = s
    def r(self):
        self.s = (self.s * 1103515245 + 12345) & 0x7fffffff
        return self.s / 2147483648.0

rng = RNG(2024)
for i in range(120):
    x = int(rng.r() * 128)
    y = int(rng.r() * 70)
    L = 2 + int(rng.r() * 3)
    c = CL['rn0'] if rng.r() < 0.7 else CL['rn1']
    for k in range(L):
        S(x - int(k * 0.4), y + k, c)
for i in range(45):
    x = int(rng.r() * 138) - 5
    y = 8 + int(rng.r() * 104)
    L = 5 + int(rng.r() * 7)
    c = CL['rn1'] if rng.r() < 0.45 else CL['rn2']
    for k in range(L):
        S(x - int(k * 0.45), y + k, c)
# splash rings
for (px, py) in [(40, 114), (90, 108), (62, 124), (20, 128), (110, 124), (74, 96), (30, 104), (100, 116)]:
    for a in range(12):
        ang = a * 0.5236
        xx = int(px + 4 * cos(ang))
        yy = int(py + 1.4 * sin(ang))
        if hash01(xx, yy, 151) < 0.6:
            S(xx, yy, CL['wht2'])
    for a in range(10):
        ang = a * 0.6283 + 0.3
        xx = int(px + 2 * cos(ang))
        yy = int(py + 0.8 * sin(ang))
        if hash01(xx, yy, 152) < 0.6:
            S(xx, yy, CL['gd5'])

# ============================================================
# 13. vignette
# ============================================================
for y in range(H):
    for x in range(W):
        dx = (x - 64) / 66.0
        dy = (y - 64) / 74.0
        d = sqrt(dx * dx + dy * dy)
        if d > 1.06 and hash01(x, y, 161) < (d - 1.06) * 2.6:
            S(x, y, CL['ink'])

# ============================================================
# 14. last accents: wet sheen on the umbrella + rim light on person
# ============================================================
for i in range(20):
    t = i / 19.0
    x = 39 + 34 * t
    y = utop(x) + 0.5 + 0.9 * abs(t - 0.5) * 2
    if hash01(int(x), int(y), 171) < 0.55:
        S(x, y, CL['wht'])

# tiny red/cyan highlight specks on the wet street
for i in range(90):
    x = int(hash01(i, 1, 181) * 128)
    y = int(74 + hash01(i, 2, 182) * 54)
    if (x, y) in FLM:
        h = hash01(i, 3, 183)
        if h < 0.33:
            S(x, y, CL['cy3'] if h < 0.1 else CL['cy1'])
        elif h < 0.66:
            S(x, y, CL['mg3'] if h < 0.43 else CL['mg1'])
        else:
            S(x, y, CL['am3'] if h < 0.76 else CL['am1'])

print(cv.stats_text())
used_colors = cv.stats()['colors_used']
assert used_colors <= 86, "too many colors: %d" % used_colors

save("cyberpunk_alley", cv, indexed=True)
finish(cv)
