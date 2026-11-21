import math
import numpy as np

W = H = 64

# ---------------- shape parameters (shape units, y up) ----------------
R_LOBE = 0.64
LOBE = 0.43
LOBE_Y = 0.44
BODY_RX = 0.93
BODY_RY = 1.10
BODY_CY = 0.10
BODY_P = 1.20
CAP_Y = 0.44
ASPECT = 1.12
K_LOBE = 0.035
K_BODY = 0.13

xs = np.arange(W)
ys = np.arange(H)
X, Y = np.meshgrid(xs, ys)


def smin(a, b, k):
    return -k * np.log(np.exp(-a / k) + np.exp(-b / k))


def sd_circle(px, py, cx, cy, r):
    return np.sqrt((px - cx) ** 2 + (py - cy) ** 2) - r


def sd_super(px, py, cx, cy, rx, ry, p):
    qx = np.abs(px - cx) / rx
    qy = np.abs(py - cy) / ry
    g = (qx ** p + qy ** p) ** (1.0 / p) - 1.0
    return g * min(rx, ry)


def build(pu, pv):
    body = sd_super(pu, pv, 0.0, BODY_CY, BODY_RX, BODY_RY, BODY_P)
    body = np.maximum(body, pv - CAP_Y)
    lobes = smin(sd_circle(pu, pv, -LOBE, LOBE_Y, R_LOBE),
                 sd_circle(pu, pv, LOBE, LOBE_Y, R_LOBE), K_LOBE)
    return smin(body, lobes, K_BODY)


fg = np.linspace(-1.9, 1.9, 761)
GU, GV = np.meshgrid(fg, fg / ASPECT)
sdg = build(GU, GV)
inside = sdg < 0
umin, umax = GU[inside].min(), GU[inside].max()
vmin, vmax = GV[inside].min(), GV[inside].max()
wu, wv = umax - umin, vmax - vmin
MARGIN = 3.0
S = min((W - 2 * MARGIN) / wu, (H - 2 * MARGIN) / wv)
uc, vc = (umin + umax) / 2.0, (vmin + vmax) / 2.0

u = (X + 0.5 - W / 2.0) / S + uc
v = -(Y + 0.5 - H / 2.0) / S + vc
sdf = build(u, v / ASPECT)
mask = sdf < 0.0
s_in = -sdf

print("fit S=%.2f  u=[%.2f,%.2f] v=[%.2f,%.2f]  size %.1f x %.1f px" % (
    S, umin, umax, vmin, vmax, wu * S, wv * S))
print("MASK")
for yy in range(H):
    print(''.join('#' if mask[yy, xx] else '.' for xx in range(W)))
print("widths per row:")
print(' '.join(str(int(mask[yy].sum())) for yy in range(H)))
