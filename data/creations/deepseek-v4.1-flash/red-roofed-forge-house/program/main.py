import math

W = H = 128
c = new_canvas(W, H, name="forge_house")

# ---------------------------------------------------------------- palette
INK    = '#191217'

R_HI   = '#f4795f'
R_LT   = '#de5a45'
R_MD   = '#c04236'
R_DK   = '#9a2d27'
R_DK2  = '#75211c'
R_SH   = '#551714'

P_HI   = '#f3e2bd'
P_LT   = '#e1ca9f'
P_MD   = '#c3aa7f'
P_SH   = '#8a7451'
P_SH2  = '#6d5b3d'

W_HI   = '#c99a5c'
W_LT   = '#a67b44'
W_MD   = '#82602f'
W_DK   = '#5f4422'
W_SH   = '#3f2b15'

S_HI   = '#d2ccc0'
S_LT   = '#b2ab9e'
S_MD   = '#8f887b'
S_DK   = '#6d675c'
S_SH   = '#4f4a43'

G_CORE = '#fffce8'
G_HI   = '#ffec96'
G_LT   = '#ffcb52'
G_MD   = '#ffa233'
G_DK   = '#e2741a'
G_EM   = '#a9520f'

WARM   = '#8c5a2e'
M_LT   = '#9c9ca6'
M_DK   = '#5e5e68'

# ---------------------------------------------------------------- geometry
OX, OY = 64.0, 68.0
HW, HH = 20.0, 10.0

ZP      = 6.0
ZW      = 40.0
Z_EAVE  = 43.0
Z_RIDGE = 62.0

UR0, UR1 = -0.20, 2.20
VR, VE   = 1.00, 2.25
UWALL = 2.0
VWALL = 2.0


def P(u, v, z=0.0):
    return (OX + (u - v) * HW, OY + (u + v) * HH - z)


def q(pts, colour):
    c.poly([P(*p) for p in pts], colour, fill=True)


def ln(a, b, colour):
    c.line(a[0], a[1], b[0], b[1], colour)


def rz(v):
    return Z_RIDGE - (Z_RIDGE - Z_EAVE) * (v - VR) / (VE - VR)


def arch_u(u_w, a, b, z0, z_flat, r, colour):
    n = max(2, int(round((b - a) * HW)))
    for i in range(n + 1):
        v = a + (b - a) * i / n
        t = (v - (a + b) * 0.5) / ((b - a) * 0.5)
        zt = z_flat + r * math.sqrt(max(0.0, 1.0 - t * t))
        ln(P(u_w, v, z0), P(u_w, v, zt), colour)


def arch_v(v_w, a, b, z0, z_flat, r, colour):
    n = max(2, int(round((b - a) * HW)))
    for i in range(n + 1):
        u = a + (b - a) * i / n
        t = (u - (a + b) * 0.5) / ((b - a) * 0.5)
        zt = z_flat + r * math.sqrt(max(0.0, 1.0 - t * t))
        ln(P(u, v_w, z0), P(u, v_w, zt), colour)


# ================================================================ PAD
PU0, PV0, PU1, PV1 = -0.25, -0.25, 2.25, 2.45

q([(PU0, PV0, ZP), (PU1, PV0, ZP), (PU1, PV1, ZP), (PU0, PV1, ZP)], S_LT)
q([(PU0, PV1, ZP), (PU1, PV1, ZP), (PU1, PV1, 0.0), (PU0, PV1, 0.0)], S_MD)
q([(PU1, PV0, ZP), (PU1, PV1, ZP), (PU1, PV1, 0.0), (PU1, PV0, 0.0)], S_DK)

for i in range(1, 7):
    uu = PU0 + (PU1 - PU0) * i / 7.0
    ln(P(uu, PV1, ZP), P(uu, PV1, 0.0), S_DK)
for i in range(1, 7):
    vv = PV0 + (PV1 - PV0) * i / 7.0
    ln(P(PU1, vv, ZP), P(PU1, vv, 0.0), S_SH)
ln(P(PU0, PV1, 3.0), P(PU1, PV1, 3.0), S_DK)
ln(P(PU1, PV0, 3.0), P(PU1, PV1, 3.0), S_SH)
ln(P(PU0, PV1, ZP), P(PU1, PV1, ZP), S_HI)
ln(P(PU1, PV0, ZP), P(PU1, PV1, ZP), S_LT)

# ================================================================ LEFT WALL (v = 2) : shadowed
q([(0.0, VWALL, ZP), (2.0, VWALL, ZP), (2.0, VWALL, 15.0), (0.0, VWALL, 15.0)], S_DK)
q([(0.0, VWALL, 15.0), (2.0, VWALL, 15.0), (2.0, VWALL, ZW), (0.0, VWALL, ZW)], P_SH)
q([(0.0, VWALL, ZW - 6.0), (2.0, VWALL, ZW - 6.0), (2.0, VWALL, ZW), (0.0, VWALL, ZW)], P_SH2)

for i in range(1, 5):
    uu = 2.0 * i / 5.0
    ln(P(uu, VWALL, 7.0), P(uu, VWALL, 15.0), S_SH)
ln(P(0.0, VWALL, 11.0), P(2.0, VWALL, 11.0), S_SH)


def fv(u0, u1, z0, z1, col):
    q([(u0, VWALL, z0), (u1, VWALL, z0), (u1, VWALL, z1), (u0, VWALL, z1)], col)


fv(0.00, 0.14, ZP, ZW, W_DK)
fv(1.86, 2.00, ZP, ZW, W_DK)
fv(0.00, 2.00, 15.0, 17.5, W_DK)
fv(0.00, 2.00, 35.0, 37.5, W_DK)
ln(P(0.30, VWALL, 17.5), P(0.85, VWALL, 35.0), W_SH)
ln(P(1.05, VWALL, 35.0), P(1.55, VWALL, 17.5), W_SH)

# --- forge arch ---
arch_v(VWALL, 0.03, 0.90, ZP, 26.0, 7.0, WARM)
arch_v(VWALL, 0.08, 0.85, ZP, 25.0, 6.5, S_LT)
arch_v(VWALL, 0.12, 0.81, ZP, 23.0, 6.0, S_DK)
arch_v(VWALL, 0.17, 0.76, ZP, 21.5, 5.0, G_EM)
arch_v(VWALL, 0.21, 0.72, ZP, 19.5, 4.5, G_DK)
arch_v(VWALL, 0.26, 0.67, ZP, 16.5, 4.0, G_MD)
arch_v(VWALL, 0.31, 0.62, ZP, 13.0, 3.5, G_LT)
arch_v(VWALL, 0.36, 0.57, ZP, 9.5, 2.5, G_HI)
for (uu, zz, col) in ((0.42, 7.5, G_CORE), (0.46, 8.0, G_CORE),
                      (0.52, 7.5, G_CORE), (0.49, 10.5, G_CORE),
                      (0.38, 11.0, G_HI), (0.60, 11.5, G_HI)):
    pt = P(uu, VWALL, zz)
    c.set(pt[0], pt[1], col)

# ================================================================ RIGHT WALL (u = 2) : lit gable wall
q([(UWALL, 0.0, ZP), (UWALL, 2.0, ZP), (UWALL, 2.0, 15.0), (UWALL, 0.0, 15.0)], S_MD)
q([(UWALL, 0.0, 15.0), (UWALL, 2.0, 15.0), (UWALL, 2.0, ZW), (UWALL, 0.0, ZW)], P_LT)
q([(UWALL, 0.0, ZW - 5.0), (UWALL, 2.0, ZW - 5.0), (UWALL, 2.0, ZW), (UWALL, 0.0, ZW)], P_MD)

for i in range(1, 5):
    vv = 2.0 * i / 5.0
    ln(P(UWALL, vv, 7.0), P(UWALL, vv, 15.0), S_DK)
ln(P(UWALL, 0.0, 11.0), P(UWALL, 2.0, 11.0), S_DK)


def fu(v0, v1, z0, z1, col):
    q([(UWALL, v0, z0), (UWALL, v1, z0), (UWALL, v1, z1), (UWALL, v0, z1)], col)


fu(0.00, 0.13, ZP, ZW, W_DK)
fu(1.87, 2.00, ZP, ZW, W_DK)
fu(0.00, 2.00, 15.0, 17.5, W_DK)
fu(0.00, 2.00, 35.0, 37.5, W_DK)

# --- door ---
arch_u(UWALL, 0.94, 1.76, ZP, 28.0, 4.0, S_MD)
arch_u(UWALL, 0.98, 1.72, ZP, 28.0, 3.6, W_SH)
arch_u(UWALL, 1.03, 1.67, ZP, 26.0, 3.2, W_MD)
arch_u(UWALL, 1.06, 1.64, ZP, 25.0, 2.8, W_LT)
for i in range(1, 5):
    vv = 1.03 + 0.64 * i / 5.0
    ln(P(UWALL, vv, 7.0), P(UWALL, vv, 27.5), W_MD)
ln(P(UWALL, 1.05, 12.0), P(UWALL, 1.45, 12.0), M_DK)
ln(P(UWALL, 1.05, 13.0), P(UWALL, 1.45, 13.0), M_DK)
ln(P(UWALL, 1.05, 21.0), P(UWALL, 1.45, 21.0), M_DK)
ln(P(UWALL, 1.05, 22.0), P(UWALL, 1.45, 22.0), M_DK)
pt = P(UWALL, 1.55, 16.0)
c.circle(pt[0], pt[1], 1, M_LT, fill=True)
# stone step
q([(1.94, 0.96, ZP), (2.28, 0.96, ZP), (2.28, 1.76, ZP), (1.94, 1.76, ZP)], S_LT)
q([(2.28, 0.96, ZP), (2.28, 1.76, ZP), (2.28, 1.76, ZP - 4.0), (2.28, 0.96, ZP - 4.0)], S_MD)
q([(1.94, 1.76, ZP), (2.28, 1.76, ZP), (2.28, 1.76, ZP - 4.0), (1.94, 1.76, ZP - 4.0)], S_DK)

# --- glowing window ---
fu(0.52, 0.94, 22.0, 36.0, W_DK)
fu(0.56, 0.90, 24.0, 34.0, G_EM)
fu(0.56, 0.90, 24.0, 30.0, G_DK)
fu(0.60, 0.86, 25.0, 28.0, G_MD)
ln(P(UWALL, 0.73, 24.0), P(UWALL, 0.73, 34.0), W_SH)
ln(P(UWALL, 0.56, 29.0), P(UWALL, 0.90, 29.0), W_SH)
ln(P(UWALL, 0.52, 22.0), P(UWALL, 0.94, 22.0), W_SH)

# ================================================================ GABLE TRIANGLE
c.poly([P(UWALL, 0.0, ZW), P(UWALL, 1.0, 60.5), P(UWALL, 2.0, ZW)], P_LT, fill=True)
fu(0.94, 1.06, ZW, 57.0, W_DK)
fu(0.34, 1.66, 46.0, 48.0, W_DK)
ln(P(UWALL, 0.34, 46.0), P(UWALL, 0.94, 58.0), W_DK)
ln(P(UWALL, 1.66, 46.0), P(UWALL, 1.06, 58.0), W_DK)
pt = P(UWALL, 1.0, 52.0)
c.circle(pt[0], pt[1], 2, W_SH, fill=True)
c.circle(pt[0], pt[1], 1, G_EM, fill=True)

# ================================================================ ROOF
NR = 5
vs = [VR + (VE - VR) * i / NR for i in range(NR + 1)]

q([(UR0, VR, Z_RIDGE), (UR1, VR, Z_RIDGE), (UR1, VE, Z_EAVE), (UR0, VE, Z_EAVE)], R_MD)
for i in range(NR):
    va, vb = vs[i], vs[i + 1]
    if i == 0:
        shade = R_LT
    elif i == NR - 1:
        shade = R_DK
    else:
        shade = R_MD
    q([(UR0, va, rz(va)), (UR1, va, rz(va)), (UR1, vb, rz(vb)), (UR0, vb, rz(vb))], shade)

# tile seams
for i in range(NR):
    va, vb = vs[i], vs[i + 1]
    off = 0.18 if i % 2 == 0 else 0.0
    k = 0
    while True:
        uk = UR0 + off + 0.36 * k
        if uk > UR1 - 0.02:
            break
        if uk > UR0 + 0.02:
            ln(P(uk, va, rz(va)), P(uk, vb, rz(vb)), R_DK)
        k += 1

# row lips: shadow line + lit edge of the row below
for i in range(1, NR):
    vb = vs[i]
    ln(P(UR0, vb, rz(vb)), P(UR1, vb, rz(vb)), R_DK)
    ln(P(UR0, vb, rz(vb) - 1.0), P(UR1, vb, rz(vb) - 1.0), R_LT)

# eave fascia
q([(UR0, VE, Z_EAVE), (UR1, VE, Z_EAVE), (UR1, VE, Z_EAVE - 3.0), (UR0, VE, Z_EAVE - 3.0)], R_DK2)
q([(UR0, VE, Z_EAVE - 3.0), (UR1, VE, Z_EAVE - 3.0), (UR1, VE, Z_EAVE - 4.5), (UR0, VE, Z_EAVE - 4.5)], R_SH)
# rake fascia (gable overhang)
q([(UR1, VR, Z_RIDGE), (UR1, VE, Z_EAVE), (UR1, VE, Z_EAVE - 3.0), (UR1, VR, Z_RIDGE - 3.0)], R_DK2)
# ridge cap
ln(P(UR0, VR, Z_RIDGE + 1.0), P(UR1, VR, Z_RIDGE + 1.0), R_HI)
ln(P(UR0, VR, Z_RIDGE), P(UR1, VR, Z_RIDGE), R_HI)
ln(P(UR0, VR, Z_RIDGE - 1.0), P(UR1, VR, Z_RIDGE - 1.0), R_LT)
ln(P(UR0, VR, Z_RIDGE - 2.0), P(UR1, VR, Z_RIDGE - 2.0), R_DK2)

# ================================================================ CHIMNEY
CU0, CU1, CV0, CV1 = 0.40, 0.68, 1.18, 1.46
CB, CT = 51.0, 70.0
q([(CU0, CV1, CB), (CU1, CV1, CB), (CU1, CV1, CT), (CU0, CV1, CT)], S_LT)
q([(CU1, CV0, CB), (CU1, CV1, CB), (CU1, CV1, CT), (CU1, CV0, CT)], S_MD)
q([(CU0, CV0, CT), (CU1, CV0, CT), (CU1, CV1, CT), (CU0, CV1, CT)], S_HI)
ln(P(CU0, CV1, 57.0), P(CU1, CV1, 57.0), S_MD)
ln(P(CU0, CV1, 63.0), P(CU1, CV1, 63.0), S_MD)
ln(P(CU1, CV0, 54.0), P(CU1, CV1, 54.0), S_DK)
ln(P(CU1, CV0, 61.0), P(CU1, CV1, 61.0), S_DK)
# cap
CU0b, CU1b, CV0b, CV1b = CU0 - 0.05, CU1 + 0.05, CV0 - 0.05, CV1 + 0.05
CTb = CT - 4.0
q([(CU0b, CV1b, CTb), (CU1b, CV1b, CTb), (CU1b, CV1b, CT), (CU0b, CV1b, CT)], S_HI)
q([(CU1b, CV0b, CTb), (CU1b, CV1b, CTb), (CU1b, CV1b, CT), (CU1b, CV0b, CT)], S_LT)
q([(CU0b, CV0b, CT), (CU1b, CV0b, CT), (CU1b, CV1b, CT), (CU0b, CV1b, CT)], S_HI)
q([(CU0 + 0.07, CV0 + 0.07, CT), (CU1 - 0.07, CV0 + 0.07, CT),
   (CU1 - 0.07, CV1 - 0.07, CT), (CU0 + 0.07, CV1 - 0.07, CT)], S_SH)

# ================================================================ LIGHT SPILL ON THE LEDGE
q([(0.06, 2.02, ZP), (0.92, 2.02, ZP), (0.82, 2.45, ZP), (0.14, 2.45, ZP)], G_EM)
q([(0.20, 2.02, ZP), (0.78, 2.02, ZP), (0.68, 2.30, ZP), (0.28, 2.30, ZP)], G_DK)
q([(0.30, 2.02, ZP), (0.66, 2.02, ZP), (0.58, 2.16, ZP), (0.36, 2.16, ZP)], G_MD)

# ================================================================ pad contact shadow + stone detail
q([(2.00, 0.00, ZP), (2.00, 2.00, ZP), (2.13, 2.00, ZP), (2.13, 0.00, ZP)], S_MD)
for i in range(1, 4):
    vv = 0.34 * i
    ln(P(2.02, vv, ZP), P(2.12, vv, ZP), S_DK)
ln(P(1.30, 2.30, ZP), P(1.50, 2.30, ZP), S_DK)
ln(P(0.30, 2.36, ZP), P(0.52, 2.36, ZP), S_MD)
ln(P(-0.10, 2.20, ZP), P(0.05, 2.20, ZP), S_MD)

# ================================================================ BARRELS
def barrel(cx, by, r=5.5, h=13.0):
    top = by - h
    c.ellipse(cx, by - 1.0, r * 1.25, r * 0.55, S_SH)
    yy = int(math.floor(top))
    while yy <= by:
        t = (yy - top) / h
        w = r * (0.84 + 0.16 * math.sin(math.pi * t))
        ln((cx - w, yy), (cx + w, yy), W_MD)
        yy += 1
    yy = int(math.floor(top))
    while yy <= by:
        t = (yy - top) / h
        w = r * (0.84 + 0.16 * math.sin(math.pi * t))
        ln((cx - w, yy), (cx - w + 1.8, yy), W_LT)
        ln((cx - w + 0.4, yy), (cx - w + 0.9, yy), W_HI)
        ln((cx + w - 2.2, yy), (cx + w, yy), W_DK)
        yy += 1
    for t in (0.14, 0.86):
        yy = top + h * t
        w = r * (0.84 + 0.16 * math.sin(math.pi * t))
        ln((cx - w, yy), (cx + w, yy), M_DK)
    c.ellipse(cx, top, r * 0.98, r * 0.44, W_DK)
    c.ellipse(cx, top, r * 0.80, r * 0.34, W_LT)
    c.ellipse(cx, top, r * 0.46, r * 0.19, W_MD)


b1 = P(1.575, 2.325, ZP)
barrel(b1[0], b1[1], 5.5, 13.0)
barrel(b1[0], b1[1] - 12.5, 5.2, 12.5)
b2 = P(1.975, 2.125, ZP)
barrel(b2[0], b2[1], 5.5, 13.0)

# ================================================================ WOODEN SIGN
SV = 0.30
q([(2.00, SV - 0.05, 33.0), (2.52, SV - 0.05, 33.0),
   (2.52, SV - 0.05, 35.0), (2.00, SV - 0.05, 35.0)], W_MD)
q([(2.00, SV - 0.05, 34.4), (2.52, SV - 0.05, 34.4),
   (2.52, SV - 0.05, 35.0), (2.00, SV - 0.05, 35.0)], W_HI)
q([(2.52, SV - 0.05, 33.0), (2.52, SV + 0.10, 33.0),
   (2.52, SV + 0.10, 35.0), (2.52, SV - 0.05, 35.0)], W_SH)
ln(P(2.02, SV, 33.0), P(2.30, SV, 27.5), W_MD)
ln(P(2.14, SV, 33.0), P(2.14, SV, 30.2), M_LT)
ln(P(2.46, SV, 33.0), P(2.46, SV, 30.2), M_LT)
BU0, BU1, BZ0, BZ1 = 2.06, 2.50, 20.0, 30.5
q([(BU0, SV, BZ0), (BU1, SV, BZ0), (BU1, SV, BZ1), (BU0, SV, BZ1)], W_LT)
q([(BU0, SV, BZ0), (BU1, SV, BZ0), (BU1, SV, BZ0 + 1.2), (BU0, SV, BZ0 + 1.2)], W_HI)
q([(BU0, SV, BZ1 - 1.2), (BU1, SV, BZ1 - 1.2), (BU1, SV, BZ1), (BU0, SV, BZ1)], W_SH)
q([(BU1, SV, BZ0), (BU1, SV + 0.10, BZ0), (BU1, SV + 0.10, BZ1), (BU1, SV, BZ1)], W_SH)
c.poly([P(BU0 + 0.05, SV, 21.5), P(2.28, SV, 28.0), P(BU1 - 0.05, SV, 21.5)], G_MD, fill=True)
c.poly([P(BU0 + 0.12, SV, 21.5), P(2.28, SV, 26.2), P(BU1 - 0.12, SV, 21.5)], G_LT, fill=True)
pt = P(2.28, SV, 22.6)
c.set(pt[0], pt[1], G_HI)

# ================================================================ outline
c.outline(INK)

CH = {INK: '.',
      R_HI: '1', R_LT: '2', R_MD: '3', R_DK: '4', R_DK2: '5', R_SH: '6',
      P_HI: 'a', P_LT: 'b', P_MD: 'c', P_SH: 'd', P_SH2: 'e',
      W_HI: 'i', W_LT: 'j', W_MD: 'k', W_DK: 'l', W_SH: 'm',
      S_HI: 'n', S_LT: 'o', S_MD: 'p', S_DK: 'q', S_SH: 'r',
      G_CORE: 'A', G_HI: 'B', G_LT: 'C', G_MD: 'D', G_DK: 'E', G_EM: 'F',
      WARM: 'W', M_LT: 'x', M_DK: 'y'}


def dump(x0, y0, x1, y1, step=1):
    rows = []
    chmap = {}
    for p in c.palette():
        hx = c.color_name(p['index'])
        if isinstance(hx, str):
            hx = hx[:7]
        chmap[p['index']] = CH.get(hx, '?') if p['rgba'][3] > 0 else ' '
    for y in range(y0, y1 + 1, step):
        row = ''
        for x in range(x0, x1 + 1, step):
            row += chmap[c.get(x, y)]
        rows.append('%3d |%s|' % (y, row))
    n = len(rows[0]) - 6
    print('    |' + ''.join(str((x0 + i * step) // 100 % 10) for i in range(n)) + '|')
    print('    |' + ''.join(str((x0 + i * step) // 10 % 10) for i in range(n)) + '|')
    print('    |' + ''.join(str((x0 + i * step) % 10) for i in range(n)) + '|')
    for r in rows:
        print(r)


print(c.stats_text())
print("palette entries:", len(c.palette()))
dump(0, 0, 127, 127, 2)
info = save("red-roofed-forge-house", c)
print(info)
finish(c)
