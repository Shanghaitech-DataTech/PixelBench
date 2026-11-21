import random, math
from pixelbench_api import *

W = H = 256
rnd = random.Random(11)

bg = new_canvas(W, H)
tr = new_canvas(W, H)
fg = new_canvas(W, H)
fx = new_canvas(W, H)

def C(spec, name):
    return bg.color(spec, name)

# ---------------- palette (opaque) ----------------
SKY0 = C('#0a110a', 'sky0')
SKY1 = C('#0e1a0f', 'sky1')
SKY2 = C('#162616', 'sky2')
GL0  = C('#203818', 'gl0')
GL1  = C('#34502a', 'gl1')
GL2  = C('#4d6b36', 'gl2')
EAR0 = C('#1e180e', 'ear0')
EAR1 = C('#2f2413', 'ear1')
EAR2 = C('#453218', 'ear2')
EAR3 = C('#5d4826', 'ear3')
GRS0 = C('#192b12', 'grs0')
GRS1 = C('#26441b', 'grs1')
GRS2 = C('#3b5e28', 'grs2')
OUT  = C('#0a090c', 'out')
BD   = C('#2b1f15', 'bd')
BM   = C('#4a3622', 'bm')
BL   = C('#6f5030', 'bl')
BH   = C('#94683f', 'bh')
CRK  = C('#1a110c', 'crk')
KNT  = C('#150f0b', 'knt')
MSD  = C('#24421c', 'msd')
MS   = C('#3a6a2c', 'ms')
MSL  = C('#57923d', 'msl')
VIN  = C('#283c1c', 'vin')
ESK  = C('#072612', 'esk')
EYE  = C('#1d7e36', 'eye')
EYB  = '#6ce86c'
EYW  = '#e2ffd8'
RKC  = C('#3d3426', 'rkc')
RKL  = C('#574a36', 'rkl')

# ---------------- fx / translucent ----------------
RA1 = C((148, 168, 110, 70), 'ra1')
RA2 = C((200, 214, 160, 44), 'ra2')
EGL = C((96, 226, 120, 66), 'egl')
VG  = C((5, 8, 6, 104), 'vg')

# ---------------- helpers ----------------
def fill(c, pts, col):
    c.poly([(int(round(x)), int(round(y))) for x, y in pts], col)

def mir(pts):
    return [(W - x, y) for x, y in pts]

def bz(p0, p1, p2, n=22):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

def tube(pts, w0, w1, seed=0, jit=0.7):
    r = random.Random(seed)
    n = len(pts)
    left = []
    right = []
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        w = w0 + (w1 - w0) * t + r.uniform(-jit, jit)
        if i == 0:
            dx = pts[1][0] - x; dy = pts[1][1] - y
        elif i == n - 1:
            dx = x - pts[-2][0]; dy = y - pts[-2][1]
        else:
            dx = pts[i + 1][0] - pts[i - 1][0]; dy = pts[i + 1][1] - pts[i - 1][1]
        Ln = math.hypot(dx, dy) or 1
        left.append((min(max(x - dy / Ln * w, 0), 255), min(max(y + dx / Ln * w, 0), 255)))
        right.append((min(max(x + dy / Ln * w, 0), 255), min(max(y - dx / Ln * w, 0), 255)))
    return left + right[::-1]

def in_poly(px, py, poly):
    pts = [(int(round(a)), int(round(b))) for a, b in poly]
    inside = False
    j = len(pts) - 1
    for i in range(len(pts)):
        xi, yi = pts[i]; xj, yj = pts[j]
        if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside

def body_hw(y, phase):
    if y <= 36:
        return 1
    hw = 14 + 0.11 * (y - 36) + 2.6 * math.sin(y * 0.21 + phase)
    if 84 < y < 150:
        hw += 4.5 * math.sin(math.pi * (y - 84) / 66)
    return hw

def trunk_pts(y0, y1, inset):
    left = []
    right = []
    for i in range(45):
        y = y0 + (y1 - y0) * i / 44
        hl = max(body_hw(y, 0.6) - inset, 0.5)
        hr = max(body_hw(y, 2.4) - inset, 0.5)
        left.append((128 - hl, y))
        right.append((128 + hr, y))
    return left + right[::-1]

# ---------------- background ----------------
for y in range(0, 150):
    col = SKY0 if y < 70 else (SKY1 if y < 110 else SKY2)
    bg.line(0, y, 255, y, col)
bg.ellipse(128, 128, 56, 64, GL0)
bg.ellipse(128, 108, 44, 46, GL1)
bg.ellipse(128, 30, 30, 20, GL2)
for y in range(150, 256):
    col = EAR0 if y < 178 else (EAR1 if y < 206 else (EAR2 if y < 236 else EAR3))
    bg.line(0, y, 255, y, col)

def far_tree(cx, cy, s, seed):
    r = random.Random(seed)
    for k in range(7):
        bg.ellipse(cx + r.uniform(-s, s * 1.5), cy + r.uniform(-s, s * 0.9),
                   r.uniform(1.1 * s, 1.8 * s), r.uniform(0.9 * s, 1.5 * s), GRS0)
        bg.ellipse(cx + r.uniform(-s, s * 0.8), cy + r.uniform(-s, s * 0.6), s * 0.65, s * 0.5, GRS1)
    fill(bg, [(cx - 4, cy), (cx + 4, cy), (cx + 3, 256), (cx - 3, 256)], SKY1)

far_tree(44, 168, 9, 1)
far_tree(72, 158, 8, 2)
far_tree(198, 160, 8, 3)
far_tree(230, 168, 9, 4)
far_tree(30, 178, 7, 5)
far_tree(244, 164, 6, 6)
far_tree(58, 148, 7, 7)
far_tree(210, 150, 7, 8)

for k in range(70):
    bg.ellipse(rnd.uniform(0, 256), rnd.uniform(160, 250), rnd.uniform(4, 12), rnd.uniform(3, 6), GRS1)

# ---------------- treant ----------------
# trunk mass
fill(tr, trunk_pts(40, 242, 0), OUT)
fill(tr, trunk_pts(42, 238, 5), BD)
fill(tr, trunk_pts(42, 238, 11), BM)
fill(tr, trunk_pts(42, 152, 17), BL)
fill(tr, trunk_pts(44, 120, 22), BH)

# crown crown
spikes = [(103, -5, 20), (110, 4, 12), (117, -3, 16), (124, 6, 8), (131, -6, 12),
         (138, 5, 5), (145, -4, 14), (152, 3, 10), (159, -6, 18)]

def crown_pts(inset):
    base = 52
    pts = [(99 + inset, 52)]
    for x, dx, h in spikes:
        pts.append((x - (3.5 + inset), base))
        pts.append((x + dx, base - h + inset))
        pts.append((x + (3.5 + inset), base))
    pts.append((157 - inset, 52))
    return pts

fill(tr, crown_pts(0), OUT)
fill(tr, crown_pts(3), BD)
for x, dx, h in spikes:
    tr.line(x + dx, 52 - h, x + 1, 52 - 3, BL)

# shoulders
for sx, ph in [(92, 118), (164, 118)]:
    tr.ellipse(sx, 118, 27, 21, OUT)
    tr.ellipse(sx, 118, 23, 17, BD)
    tr.ellipse(sx, 116, 19, 13, BM)
    tr.ellipse(sx, 114, 14, 9, BL)

# arms : left
Larm = bz((88, 120), (66, 82), (54, 40))
fill(tr, tube(Larm, 18, 7, seed=1), OUT)
fill(tr, tube(Larm, 14, 4.5, seed=2), BD)
fill(tr, tube(Larm, 10, 3, seed=3), BM)
fill(tr, tube(Larm, 6, 1.8, seed=4), BL)
Rarm = mir(Larm)
fill(tr, tube(Rarm, 18, 7, seed=5), OUT)
fill(tr, tube(Rarm, 14, 4.5, seed=6), BD)
fill(tr, tube(Rarm, 10, 3, seed=7), BM)
fill(tr, tube(Rarm, 6, 1.8, seed=8), BL)

# arm twigs / claws
def claw(a, b, seed):
    mid = ((a[0] + b[0]) / 2 + 3, (a[1] + b[1]) / 2 + 3)
    pts = bz(a, mid, b)
    fill(tr, tube(pts, 5.5, 1.4, seed=seed), OUT)
    fill(tr, tube(pts, 3.4, 0.9, seed=seed + 10), BM)
    fill(tr, tube(pts, 2.0, 0.7, seed=seed + 20), BL)

for i, (a, b) in enumerate([((54, 40), (43, 16)), ((54, 40), (57, 8)), ((56, 42), (70, 14)),
                            ((58, 44), (66, 26))]):
    claw(a, b, 20 + i)
    claw(mir([a])[0], mir([b])[0], 30 + i)

mid_tw = [((86, 92), (60, 58), (50, 26)), ((60, 88), (44, 52), (40, 30)), ((78, 66), (90, 40), (86, 20))]
for i, (a, b) in enumerate([(m[0], m[2]) for m in mid_tw]):
    claw(a, b, 40 + i)
for i, (a, b) in enumerate([(mir([m[0]])[0], mir([m[2]])[0]) for m in mid_tw]):
    claw(a, b, 50 + i)

# roots
roots = [((86, 240), (62, 196), (40, 234)), ((66, 242), (46, 208), (24, 244)),
        ((104, 238), (96, 200), (120, 192)), ((118, 240), (140, 246), (156, 244))]
all_roots = roots + [mir(r) for r in roots[1:]]
for ri, (a, b, m0) in enumerate(roots):
    m = ((a[0] + m0[0]) / 2, (a[1] + m0[1]) / 2)
    pts = bz(a, m, b)
    fill(tr, tube(pts, 11.5, 5.5, seed=60 + ri), OUT)
    fill(tr, tube(pts, 8.5, 3.2, seed=61 + ri), BD)
    fill(tr, tube(pts, 6, 1.9, seed=62 + ri), BM)
for ri, (a, b, m0) in enumerate(roots[1:]):
    m = ((a[0] + m0[0]) / 2, (a[1] + m0[1]) / 2)
    pts = bz(mir([a])[0], m, mir([b])[0])
    fill(tr, tube(pts, 8.5, 3.2, seed=63 + ri), BD)
    fill(tr, tube(pts, 6, 1.9, seed=64 + ri), BM)
    fill(tr, tube(pts, 4, 1.4, seed=65 + ri), BM)
# root clumps
for (a, b) in [((40, 234), (44, 236)), ((24, 244), (22, 246)), ((120, 192), (122, 196)), ((156, 244), (154, 246)),
              (mir([(40, 234)])[0], mir([(44, 236)])[0]), (mir([(24, 244)])[0], mir([(22, 246)])[0]),
              (mir([(156, 244)])[0], mir([(154, 246)])[0])]:
    tr.ellipse(a[0], a[1], 5, 3.4, BD)
    tr.ellipse(a[0] - 1, a[1] - 1, 3, 2, BM)

# bark plates
for i, y in enumerate([140, 158, 176, 194, 212, 228]):
    x0 = 128 - body_hw(y, 0.6) + 6
    x1 = 128 + body_hw(y, 2.4) - 6
    fill(tr, tube(bz((x0, y), (128, y + 6), (x1, y)), 2.8, 2.8, seed=80 + i), BD)
    fill(tr, tube(bz((x0 + 3, y + 2), (128, y + 7), (x1 - 3, y + 2)), 1.5, 1.5, seed=90 + i), BL)
    fill(tr, tube(bz((x0 + 4, y - 2), (128, y + 1), (x1 - 4, y - 2)), 0.9, 0.9, seed=100 + i), BH)

# bark texture
mask = trunk_pts(44, 236, 8)
for k in range(330):
    y = rnd.uniform(50, 232)
    x = 128 + rnd.uniform(-body_hw(y, 0.6) + 8, body_hw(y, 2.4) - 8)
    a = (x, y)
    b = (x + rnd.uniform(-3, 4), y + rnd.uniform(2, 13))
    if in_poly(a[0], a[1], mask) and in_poly(b[0], b[1], mask):
        tr.line(a[0], a[1], b[0], b[1], [CRK, BD, BL, BH][k % 4])
for k in range(46):
    x = rnd.uniform(108, 148)
    y0 = rnd.uniform(50, 160)
    a = (x, y0)
    b = (x + rnd.uniform(-4, 4), y0 + rnd.uniform(26, 44))
    if in_poly(a[0], a[1], mask) and in_poly(b[0], b[1], mask):
        tr.line(a[0], a[1], b[0], b[1], CRK)

# knots
for (kx, ky) in [(116, 158), (140, 176), (120, 204), (138, 222), (112, 64), (150, 140), (124, 214), (106, 160)]:
    if in_poly(kx, ky, mask):
        tr.ellipse(kx, ky, 4, 5, OUT)
        tr.ellipse(kx, ky, 2.6, 3.5, CRK)
        tr.ellipse(kx, ky - 1, 1.6, 2.2, KNT)
        tr.ellipse(kx + 1, ky - 2, 0.8, 1.2, BH)

# bark scratch cuts along silhouette
for k in range(26):
    y = 52 + k * 7
    x = 128 - body_hw(y, 0.6) + 2.5
    tr.line(x, y, x + 6, y - 3, BL)

# face
tr.poly([(96, 84), (104, 80), (126, 88), (122, 94), (98, 92)], OUT)
tr.poly([(160, 84), (152, 80), (130, 88), (134, 94), (158, 92)], OUT)
for ex, ey in [(110, 98), (146, 98)]:
    tr.ellipse(ex, ey, 9, 10, OUT)
    tr.ellipse(ex, ey, 7, 8, ESK)
    tr.ellipse(ex, ey, 4.6, 5.4, EYE)
    tr.ellipse(ex, ey, 2.6, 3.2, EYB)
    tr.ellipse(ex, ey, 1, 1.4, EYW)
    tr.line(ex - 2, ey + 5, ex - 4, ey + 9, ESK)
tr.line(128, 84, 128, 96, CRK)
mouth = [(106, 124), (114, 120), (122, 126), (130, 120), (138, 126), (146, 121), (150, 129),
         (143, 137), (134, 131), (126, 138), (118, 133), (110, 139), (104, 131)]
fill(tr, mouth, OUT)
fill(tr, [(110, 126), (118, 123), (126, 128), (134, 124), (142, 127), (145, 132),
         (135, 130), (127, 134), (119, 131), (112, 133), (110, 131)], CRK)
for tx, ty in [(113, 124), (125, 125), (137, 124), (145, 126)]:
    tr.ellipse(tx, ty, 1.6, 2, MSL)
for tx, ty in [(118, 130), (130, 133), (140, 130)]:
    tr.ellipse(tx, ty, 1, 1.4, EYE)
tr.line(106, 102, 100, 108, CRK)
tr.line(150, 102, 156, 108, CRK)
tr.line(112, 104, 114, 112, ESK)
tr.line(144, 104, 142, 112, ESK)

# moss on treant
moss = [((98, 120), 13, 9), ((158, 120), 13, 9), ((84, 88), 10, 6), ((172, 88), 10, 6),
       ((106, 156), 9, 12), ((150, 156), 9, 12), ((116, 196), 7, 8), ((140, 196), 7, 8),
       ((104, 220), 11, 8), ((152, 220), 11, 8), ((70, 70), 8, 5), ((186, 70), 8, 5),
       ((80, 92), 9, 5), ((176, 92), 9, 5), ((112, 62), 7, 4), ((144, 62), 7, 4)]
for (mxy, rx, ry) in moss:
    (mx, my) = mxy
    tr.ellipse(mx, my, rx + 1.5, ry + 1.5, OUT)
    tr.ellipse(mx, my, rx, ry, MSD)
    tr.ellipse(mx - 1, my - 1, rx - 2.4, ry - 2.2, MS)
    tr.ellipse(mx - 2, my - 2, rx - 4, ry - 3.4, MSL)

# hanging vines (treant layer)
def vine(a, b, seed):
    r = random.Random(seed)
    pts = [a]
    for i in range(1, 8):
        pts.append((a[0] + (b[0] - a[0]) * i / 8 + r.uniform(-1.8, 1.8) , a[1] + (b[1] - a[1]) * i / 8))
    pts.append(b)
    fill(tr, tube(pts, 2.3, 2.3, seed=seed + 1, jit=0.5), OUT)
    fill(tr, tube(pts, 1.0, 1.0, seed=seed + 2, jit=0.3), VIN)
    for i in (2, 4, 6):
        lx, ly = pts[i]
        tr.ellipse(lx + 1.8, ly, 1.6, 1.1, MS)
        tr.ellipse(lx + 0.8, ly - 0.8, 0.8, 0.7, MSL)

vstart = [((100, 60), (103, 106)), ((86, 96), (92, 132)), ((72, 108), (78, 150)),
         ((60, 64), (66, 100)), ((52, 48), (58, 86)), ((112, 120), (114, 158)), ((94, 118), (96, 164))]
for i, (a, b) in enumerate(vstart):
    vine(a, b, 140 + i)
    vine(mir([a])[0], mir([b])[0], 150 + i)

tr.outline(OUT)

# ---------------- foreground ----------------
for cx in range(6, 252, 14):
    r = random.Random(cx)
    bx = cx + r.uniform(-4, 4)
    by = 250 + r.uniform(-6, 0)
    for k in range(4):
        gx = bx + r.uniform(-7, 7)
        gy = by + r.uniform(-10, 0)
        fg.line(gx, by, gx + r.uniform(-2, 2), gy - r.uniform(2, 9), GRS1)
        fg.line(gx, by, gx + r.uniform(-1, 1), gy - r.uniform(1, 4), GRS2)
for rx, ry in [(52, 246), (204, 246), (120, 250), (150, 252), (30, 250), (226, 248)]:
    fg.ellipse(rx, ry, 7, 4, RKC)
    fg.ellipse(rx - 2, ry - 2, 4, 2, RKL)

# ---------------- fx ----------------
fx.ellipse(128, 238, 96, 30, RA2)
fx.ellipse(110, 98, 16, 18, EGL)
fx.ellipse(146, 98, 16, 18, EGL)
beams = [((118, -12), (134, -12), (196, 256), (150, 256)), ((102, -12), (114, -12), (138, 256), (120, 256)),
        ((136, -12), (142, -12), (178, 256), (158, 256)), ((92, -12), (102, -12), (118, 256), (104, 256))]
for q in beams:
    fx.poly(q, RA1)
cores = [((120, -12), (128, -12), (168, 256), (146, 256)), ((108, -10), (116, -12), (130, 256), (122, 256)),
        ((124, -8), (130, -8), (150, 256), (138, 256))]
for q in cores:
    fx.poly(q, RA2)
fx.poly([(0, 0), (64, 0), (0, 64)], VG)
fx.poly([(256, 0), (256, 64), (192, 0)], VG)
fx.poly([(0, 256), (0, 200), (56, 256)], VG)
fx.poly([(256, 256), (256, 200), (200, 256)], VG)
for k in range(26):
    fx.ellipse(rnd.uniform(70, 186), rnd.uniform(150, 248), 1.5, 1.5, RA2)

# ---------------- composite ----------------
result = flatten([bg, tr, fg, fx])
print(result.stats_text())
print('bbox', result.stats()['bbox'])
finish(result)
