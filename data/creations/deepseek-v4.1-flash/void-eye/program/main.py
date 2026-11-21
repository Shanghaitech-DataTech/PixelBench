import math
from math import sin, cos, atan2, hypot, sqrt

W = H = 64
c = new_canvas(W, H, name="void-eye")


def reg(k, spec):
    return c.color(spec, name=k)


P = {}
P['outline']  = reg('outline',  '#0a0612')
P['flesh0']   = reg('flesh0',   '#1e132e')
P['flesh1']   = reg('flesh1',   '#2d1944')
P['flesh2']   = reg('flesh2',   '#402459')
P['flesh3']   = reg('flesh3',   '#5c3780')
P['flesh4']   = reg('flesh4',   '#8355ab')
P['vein']     = reg('vein',     '#20122f')
P['socket']   = reg('socket',   '#0d0719')
P['sclera1']  = reg('sclera1',  '#9b93b5')
P['sclera2']  = reg('sclera2',  '#c2bad6')
P['sclera3']  = reg('sclera3',  '#e2dcee')
P['sclera4']  = reg('sclera4',  '#fbf8ff')
P['svein']    = reg('svein',    '#a889b8')
P['iris0']    = reg('iris0',    '#1c0736')
P['iris1']    = reg('iris1',    '#33105f')
P['iris2']    = reg('iris2',    '#4e1c92')
P['iris3']    = reg('iris3',    '#7b39d6')
P['iris4']    = reg('iris4',    '#a163f0')
P['pupil1']   = reg('pupil1',   '#c99aff')
P['pupil2']   = reg('pupil2',   '#e3bdff')
P['pupil3']   = reg('pupil3',   '#f2dcff')
P['spec']     = reg('spec',     '#ffffff')
P['tent1']    = reg('tent1',    '#2e1a45')
P['tent2']    = reg('tent2',    '#472a66')
P['tent3']    = reg('tent3',    '#6a4490')

FLESH = ['flesh0', 'flesh1', 'flesh2', 'flesh3', 'flesh4']

# ------------------------------------------------------------------ shadow
SH_LEVELS = [(0.80, 150), (0.60, 118), (0.42, 88), (0.24, 60), (0.10, 34)]
SH_COLS = []
for i, (thr, al) in enumerate(SH_LEVELS):
    SH_COLS.append((thr, c.color((11, 4, 20, al), name='shadow%d' % i)))

SHCX, SHCY, SHRX, SHRY = 32.0, 59.0, 20.5, 3.4
for y in range(H):
    for x in range(W):
        d = hypot((x + 0.5 - SHCX) / SHRX, (y + 0.5 - SHCY) / SHRY)
        if d >= 1.0:
            continue
        val = 1.0 - d
        for (thr, idx) in SH_COLS:
            if val > thr:
                c.set(x, y, idx)
                break

# --------------------------------------------------------------- tentacles
def bez(p0, p1, p2, t):
    mt = 1.0 - t
    x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
    y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
    return x, y


TENTS = [
    ((22, 38), (14, 45), (17, 50), 4.1, 1.7),   # far left
    ((28, 42), (23, 47), (27, 53), 3.5, 1.4),
    ((33, 43), (35, 48), (31, 54), 3.7, 1.5),   # centre
    ((38, 42), (43, 47), (39, 53), 3.5, 1.4),
    ((44, 38), (51, 45), (47, 50), 4.1, 1.7),   # far right
]

N = 34
for (p0, p1, p2, r0, r1) in TENTS:
    for i in range(N + 1):
        t = i / N
        x, y = bez(p0, p1, p2, t)
        r = r0 + (r1 - r0) * t
        c.circle(int(round(x)), int(round(y)), int(round(r)), P['outline'])
    for i in range(N + 1):
        t = i / N
        x, y = bez(p0, p1, p2, t)
        r = r0 + (r1 - r0) * t
        ix, iy = int(round(x)), int(round(y))
        ri = int(round(r))
        if ri >= 1:
            c.circle(ix, iy, ri - 1, P['tent1'])
        if ri >= 2:
            c.circle(ix - 1, iy - 1, ri - 2, P['tent2'])
        if ri >= 3:
            c.circle(ix - 1, iy - 1, ri - 3, P['tent3'])

# ------------------------------------------------------------------- body
BCX, BCY = 32.0, 26.0
BRX, BRY = 24.0, 21.0
Lx, Ly, Lz = -0.50, -0.62, 0.60
_ln = sqrt(Lx * Lx + Ly * Ly + Lz * Lz)
Lx, Ly, Lz = Lx / _ln, Ly / _ln, Lz / _ln


def brad(th):
    return (1.0
            + 0.062 * sin(3 * th + 0.75)
            + 0.036 * sin(5 * th + 2.20)
            + 0.020 * sin(7 * th + 4.30))


def flesh_band(lam):
    if lam > 0.86:
        return 4
    if lam > 0.63:
        return 3
    if lam > 0.38:
        return 2
    if lam > 0.10:
        return 1
    return 0


SCX, SCY = 32.0, 25.0
SRX, SRY = 15.0, 13.5

body = {}
for y in range(H):
    for x in range(W):
        dx = x + 0.5 - BCX
        dy = y + 0.5 - BCY
        u = dx / BRX
        v = dy / BRY
        q = hypot(u, v)
        th = atan2(v, u) if q > 1e-9 else 0.0
        br = brad(th)
        qr = q / br
        if qr <= 1.0:
            nz = sqrt(max(0.0, 1.0 - min(1.0, qr * qr)))
            lam = u * Lx + v * Ly + nz * Lz
            body[(x, y)] = (u, v, qr, lam)

for (x, y) in sorted(body):
    u, v, qr, lam = body[(x, y)]
    band = flesh_band(lam)
    if qr > 0.925 and v > 0.20:
        band = max(band, 2)            # rim light along the lower edge
    qe = hypot((x + 0.5 - SCX) / SRX, (y + 0.5 - SCY) / SRY)
    if qe <= 1.0:
        continue                       # eyeball paints here later
    if qe <= 1.13:
        # faint violet halo where the eye's glow leaks into the socket
        c.set(x, y, P['iris0'] if qe <= 1.05 else P['socket'])
        continue
    if qe < 1.36:
        band = max(0, band - 1)        # ambient occlusion around the socket
    gq = hypot((x + 0.5 - 31.5) / 8.6, (y + 0.5 - 40.0) / 6.4)
    if gq <= 1.0 and v > 0.18:         # light spilling down from the eye
        band = max(band, 1 if gq > 0.58 else 2)
    c.set(x, y, P[FLESH[band]])

# silhouette outline
for (x, y) in sorted(body):
    edge = False
    for (ax, ay) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if (ax, ay) not in body:
            edge = True
            break
    if edge:
        c.set(x, y, P['outline'])

# flesh creases and wrinkles
def is_edge(x, y):
    for (ax, ay) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if (ax, ay) not in body:
            return True
    return False


def qe_of(x, y):
    return hypot((x + 0.5 - SCX) / SRX, (y + 0.5 - SCY) / SRY)


def safe_dot(x, y, col):
    if (x, y) in body and not is_edge(x, y) and qe_of(x, y) > 1.30:
        c.set(x, y, col)


def safe_line(x0, y0, x1, y1, col):
    dx = x1 - x0
    dy = y1 - y0
    n = max(abs(dx), abs(dy))
    if n == 0:
        safe_dot(x0, y0, col)
        return
    for i in range(n + 1):
        safe_dot(int(round(x0 + dx * i / n)), int(round(y0 + dy * i / n)), col)


for (x0, y0, x1, y1) in [(13, 20, 17, 26), (51, 19, 47, 26), (16, 34, 20, 38),
                         (48, 33, 44, 37)]:
    safe_line(x0, y0, x1, y1, P['vein'])

# short wrinkles radiating out from the socket
WRINKLES = [
    (-2.62, 0.016), (-2.05, -0.015), (-1.48, 0.018),
    (3.58, -0.015), (2.92, 0.016), (0.55, -0.018),
]
for (ang, curl) in WRINKLES:
    pts = []
    for i in range(8):
        t = 1.26 + 0.034 * i
        a = ang + curl * i
        pts.append((int(round(SCX + SRX * t * cos(a))),
                    int(round(SCY + SRY * t * sin(a)))))
    for i in range(len(pts) - 1):
        safe_line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], P['vein'])

# ------------------------------------------------------------------ sclera
for y in range(H):
    for x in range(W):
        dx = x + 0.5 - SCX
        dy = y + 0.5 - SCY
        u = dx / SRX
        v = dy / SRY
        q = hypot(u, v)
        if q > 1.0:
            continue
        lum = 1.0
        lum -= 0.70 * max(0.0, (q - 0.55)) / 0.45
        lum -= 0.18 * max(0.0, v)
        if -v > 0.60:
            lum -= 0.55 * ((-v) - 0.60) / 0.40
        lum += 0.08 * max(0.0, -u)
        if lum > 0.80:
            col = 'sclera4'
        elif lum > 0.58:
            col = 'sclera3'
        elif lum > 0.34:
            col = 'sclera2'
        else:
            col = 'sclera1'
        c.set(x, y, P[col])

# faint blood vessels on the sclera
for (x0, y0, x1, y1) in [
    (18, 31, 24, 29),
    (46, 21, 41, 25),
    (47, 31, 43, 29),
]:
    c.line(x0, y0, x1, y1, P['svein'])

# -------------------------------------------------------------------- iris
ICX, ICY, IRR = 32.0, 25.6, 9.0
IBANDS = ['iris0', 'iris1', 'iris2', 'iris3', 'iris4']
for y in range(H):
    for x in range(W):
        dx = x + 0.5 - ICX
        dy = y + 0.5 - ICY
        r = hypot(dx, dy)
        if r > IRR:
            continue
        th = atan2(dy, dx)
        streak = sin(11.0 * th + 0.9) * 0.5 + 0.5
        if r > 8.0:
            band = 0
        elif r > 6.7:
            band = 1
        elif r > 5.2:
            band = 2
        elif r > 3.6:
            band = 3
        else:
            band = 4
        if 3.6 < r <= 7.8 and band < 3 and streak > 0.70:
            band += 1
        if dy < -4.6 and band > 0:
            band = max(0, band - 1)     # upper-lid shadow across the iris
        c.set(x, y, P[IBANDS[band]])

# ------------------------------------------------------------------- pupil
PCX, PCY = 32.0, 25.8
PRX, PRY = 2.4, 3.2
for y in range(H):
    for x in range(W):
        pe = hypot((x + 0.5 - PCX) / PRX, (y + 0.5 - PCY) / PRY)
        if pe > 1.0:
            continue
        if pe <= 0.40:
            col = 'pupil3'
        elif pe <= 0.70:
            col = 'pupil2'
        else:
            col = 'pupil1'
        c.set(x, y, P[col])

# specular reflection on the wet sclera, upper-left
SPEC_HALO = [(23, 16), (22, 17), (23, 17), (24, 17), (25, 17),
             (21, 18), (22, 18), (23, 18), (24, 18), (25, 18), (26, 18),
             (21, 19), (22, 19), (23, 19), (24, 19),
             (22, 20), (23, 20)]
SPEC_HOT = [(23, 17), (24, 17), (22, 18), (23, 18), (24, 18),
            (22, 19), (23, 19)]
for (x, y) in SPEC_HALO:
    c.set(x, y, P['sclera4'])
for (x, y) in SPEC_HOT:
    c.set(x, y, P['spec'])

print(c.stats_text())
print(c.matrix_text(region=(9, 4, 56, 47)))
finish(c)
