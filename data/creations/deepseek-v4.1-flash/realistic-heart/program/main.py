"""Realistic glossy heart, 64x64 pixel art.

Pipeline: SDF silhouette (superellipse body + two lobe discs) -> membrane +
spherical-lobe height field -> per-pixel normals -> two-point light rig with
Blinn-Phong gloss -> mapped through a 17-anchor red ramp -> ordered dither.
"""
import math
import numpy as np

W = H = 64

# ---------------- silhouette parameters (shape units, y up) ----------------
R_LOBE = 0.66
LOBE = 0.44
LOBE_Y = 0.46
BODY_RX = 0.86
BODY_RY = 1.05
BODY_CY = 0.05
BODY_P = 1.20
CAP_Y = 0.46
ASPECT = 1.06
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
    body = np.maximum(body, pv - CAP_Y)            # flat cap, hidden by the lobes
    lobes = smin(sd_circle(pu, pv, -LOBE, LOBE_Y, R_LOBE),
                 sd_circle(pu, pv, LOBE, LOBE_Y, R_LOBE), K_LOBE)
    return smin(body, lobes, K_BODY)


def shape(pu, pv):
    return build(pu, pv / ASPECT)


# ---- fit the silhouette to the canvas
fg = np.linspace(-1.9, 1.9, 761)
GU, GV = np.meshgrid(fg, fg)
sdg = shape(GU, GV)
inside = sdg < 0
umin, umax = GU[inside].min(), GU[inside].max()
vmin, vmax = GV[inside].min(), GV[inside].max()
wu, wv = umax - umin, vmax - vmin
MARGIN = 2.6
S = min((W - 2 * MARGIN) / wu, (H - 2 * MARGIN) / wv)
uc, vc = (umin + umax) / 2.0, (vmin + vmax) / 2.0

u = (X + 0.5 - W / 2.0) / S + uc
v = -(Y + 0.5 - H / 2.0) / S + vc
sdf = shape(u, v)
mask = sdf < 0.0
s_in = -sdf
vs = v / ASPECT

def gauss(px, py, cx, cy, sx, sy):
    return np.exp(-(((px - cx) / sx) ** 2 + ((py - cy) / sy) ** 2))

# ---------------- height field: membrane balloon + lobe domes ----------------
press = 1.0 + 0.35 * (gauss(u, vs, -LOBE, LOBE_Y + 0.02, 0.40, 0.42) +
                      gauss(u, vs, LOBE, LOBE_Y + 0.02, 0.40, 0.42))
h = np.zeros((H, W))
for it in range(9000):                              # Jacobi solve of grad^2 h = -p
    hs = (np.roll(h, 1, 0) + np.roll(h, -1, 0) +
          np.roll(h, 1, 1) + np.roll(h, -1, 1)) * 0.25
    h = np.where(mask, hs + press * 0.25, 0.0)
h_mem = h / h.max()

DL_R, DL_A = 0.78, 1.04
dL = np.sqrt((u + LOBE) ** 2 + (vs - LOBE_Y) ** 2)
dR = np.sqrt((u - LOBE) ** 2 + (vs - LOBE_Y) ** 2)
domeL = DL_A * np.sqrt(np.clip(1.0 - (dL / DL_R) ** 2, 0.0, None))
domeR = DL_A * np.sqrt(np.clip(1.0 - (dR / DL_R) ** 2, 0.0, None))
P = 4.0
h = (h_mem ** P + domeL ** P + domeR ** P) ** (1.0 / P)

crease = gauss(u, vs, 0.0, 0.88, 0.115, 0.32) * np.clip((vs - 0.42) / 0.28, 0.0, 1.0)
h = h * (1.0 - 0.55 * crease)
h = np.clip(h, 0.0, None)
h = h / h.max() * mask

# ---------------- normals ----------------
gy, gx = np.gradient(h)
AMP = 0.80
nx = -AMP * gx * S
ny = AMP * gy * S
nz = np.ones_like(h)
nn = np.sqrt(nx * nx + ny * ny + nz * nz)
nx, ny, nz = nx / nn, ny / nn, nz / nn

# ---------------- two-point light rig ----------------
zpos = h * 0.62
KEY = (-1.30, 1.25, 2.20)
FILL = (1.50, -1.85, 1.15)
VIEW = (0.0, 0.0, 3.0)


def light(pos, katt):
    lx, ly, lz = pos[0] - u, pos[1] - v, pos[2] - zpos
    d = np.sqrt(lx * lx + ly * ly + lz * lz) + 1e-6
    lx, ly, lz = lx / d, ly / d, lz / d
    lam = np.clip(nx * lx + ny * ly + nz * lz, 0, 1)
    att = 1.0 / (1.0 + katt * d * d)
    hx, hy, hz = lx + VIEW[0], ly + VIEW[1], lz + VIEW[2]
    hn = np.sqrt(hx * hx + hy * hy + hz * hz) + 1e-6
    nh = np.clip(nx * hx / hn + ny * hy / hn + nz * hz / hn, 0, 1)
    return lam * att, nh, att

key_lam, nh_key, key_att = light(KEY, 0.055)
fill_lam, nh_fill, fill_att = light(FILL, 0.055)

ao = 1.0 - 0.34 * np.exp(-np.clip(s_in, 0, None) / 0.100)   # thin rim darkening
occ = 1.0 - 0.48 * crease                                    # cleft occlusion
depth = np.clip(s_in / 0.55, 0, 1)
tone = ao * occ * (0.12 + 0.03 * nz + 0.94 * key_lam)
tone = tone + 0.30 * fill_lam * (0.26 + 0.74 * depth)
tone = tone + 0.50 * nh_key ** 95.0 * key_att + 0.22 * nh_key ** 600.0 * key_att
tone = tone + 0.16 * nh_fill ** 90.0 * fill_att
tone = np.clip(tone, 0.0, 1.0)

# ---------------- colour ramp (deep maroon -> crimson -> coral -> glint) ------
anchors = [
    (0.00, (0x17, 0x04, 0x0a)),
    (0.05, (0x2b, 0x06, 0x11)),
    (0.12, (0x47, 0x09, 0x1a)),
    (0.20, (0x65, 0x10, 0x1f)),
    (0.28, (0x83, 0x16, 0x27)),
    (0.36, (0xa0, 0x1d, 0x2c)),
    (0.44, (0xb8, 0x26, 0x32)),
    (0.52, (0xcc, 0x31, 0x38)),
    (0.60, (0xdc, 0x40, 0x40)),
    (0.68, (0xe8, 0x54, 0x50)),
    (0.75, (0xf1, 0x6a, 0x60)),
    (0.81, (0xf7, 0x84, 0x7a)),
    (0.86, (0xfb, 0x9c, 0x93)),
    (0.91, (0xfd, 0xb3, 0xac)),
    (0.95, (0xff, 0xcb, 0xc6)),
    (0.98, (0xff, 0xdf, 0xdc)),
    (1.00, (0xff, 0xf2, 0xf1)),
]


def ramp_at(t):
    t = min(max(t, 0.0), 1.0)
    for i in range(len(anchors) - 1):
        t0, c0 = anchors[i]
        t1, c1 = anchors[i + 1]
        if t0 <= t <= t1:
            k = 0.0 if t1 == t0 else (t - t0) / (t1 - t0)
            return tuple(int(round(c0[j] + (c1[j] - c0[j]) * k)) for j in range(3))
    return anchors[-1][1]

# ---------------- ordered dither + quantise ----------------
bayer = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]], float)
bth = (bayer + 0.5) / 16.0 - 0.5
NLEV = 56
td = np.clip(tone + bth[np.arange(H)[:, None] % 4, np.arange(W)[None, :] % 4] * (1.0 / NLEV), 0, 1)
tone_q = np.round(td * NLEV) / NLEV

# ---------------- draw ----------------
heart = new_canvas(W, H, background=None, name="heart")
used = set()
for yy in range(H):
    for xx in range(W):
        if mask[yy, xx]:
            r, g, b = ramp_at(float(tone_q[yy, xx]))
            heart.set(xx, yy, '#%02x%02x%02x' % (r, g, b))
            used.add((r, g, b))

print("S=%.2f size %.1f x %.1f px" % (S, wu * S, wv * S))
print("inside:", int(mask.sum()), "colours:", len(used))
print(heart.stats_text())
vis = tone[mask]
print("tone pct 5/25/50/75/95: %.2f %.2f %.2f %.2f %.2f" % tuple(
    np.percentile(vis, [5, 25, 50, 75, 95])))
print("frac>0.92: %.3f  frac<0.18: %.3f  clipped: %d" % (
    float((vis > 0.92).mean()), float((vis < 0.18).mean()), int((vis >= 0.999).sum())))

ramp = ".:-=+*oO#%@"
for yy in range(H):
    print(''.join((' ' if not mask[yy, xx] else
                   ramp[min(max(int(round(tone[yy, xx] * 10)), 0), 10)])
                  for xx in range(W)))

save("heart_realistic", heart)
finish(heart)
