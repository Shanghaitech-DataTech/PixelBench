"""Realistic glossy heart, 64x64 pixel art.

Pipeline:
  1. Supersampled implicit heart curve  -> coverage / mask
  2. Exact-ish Euclidean distance field -> height field -> normals
  3. Key + fill + specular + subsurface + fresnel rim shading
  4. Backdrop with radial glow, cast shadow and ambient occlusion
  5. Median-cut quantisation to <= 76 colours, painted pixel by pixel
"""

import numpy as np

W = H = 64
SS = 7                      # supersampling factor for the silhouette
RNG = np.random.default_rng(1234)

# ---- heart placement -------------------------------------------------
SC = 21.3                   # canvas pixels per implicit unit
CX = 31.5                   # heart x = 0
CY = 31.2                   # heart y = 0 (y up in implicit space)

# ---- shading knobs ---------------------------------------------------
KEY_DIR = np.array([-0.44, -0.46, 0.77])
FILL_DIR = np.array([0.62, 0.42, 0.45])
PUFF = 2.55                 # how steep the rounded edge is
SPEC_POW = 90.0
SPEC_STR = 1.35
SHEEN_POW = 14.0
SHEEN_STR = 0.12
SSS_STR = 0.55
RIM_STR = 0.34
AMBIENT = 0.21
MAX_COLORS = 76


def heart_f(nx, ny):
    a = nx * nx + ny * ny - 1.0
    return a * a * a - nx * nx * ny * ny * ny


# ----------------------------------------------------------------------
# 1. coverage / mask
# ----------------------------------------------------------------------
xs_px = np.arange(W) + 0.5
ys_px = np.arange(H) + 0.5
offs = (np.arange(SS) + 0.5) / SS - 0.5

cov = np.zeros((H, W))
for oy in offs:
    for ox in offs:
        nx = (xs_px[None, :] + ox - CX) / SC
        ny = (CY - (ys_px[:, None] + oy)) / SC
        cov += (heart_f(nx, ny) <= 0.0).astype(float)
cov /= float(SS * SS)

inside = cov >= 0.5
n_in = int(inside.sum())

# ----------------------------------------------------------------------
# 2. distance field (brute force EDT against the opposite set)
# ----------------------------------------------------------------------
yy, xx = np.mgrid[0:H, 0:W]
flat_in = inside.ravel()


def edt(src_mask):
    """distance from every pixel to the nearest pixel where src_mask is True"""
    sy, sx = np.nonzero(src_mask)
    pts = np.stack([sx, sy], 1).astype(np.float64)
    out = np.full((H, W), 1e9)
    coords = np.stack([xx.ravel(), yy.ravel()], 1).astype(np.float64)
    for i in range(0, len(coords), 512):
        chunk = coords[i:i + 512]
        d = np.sqrt(((chunk[:, None, :] - pts[None, :, :]) ** 2).sum(-1))
        out.ravel()[i:i + 512] = d.min(1)
    return out


d_to_out = edt(~inside)     # for interior pixels
d_to_in = edt(inside)       # for exterior pixels

D = np.where(inside, np.maximum(d_to_out - 0.5, 0.05), 0.0)
Dout = np.where(inside, 0.0, np.maximum(d_to_in - 0.5, 0.0))

# sub-pixel nudge on the silhouette ring using coverage
ring = inside & (cov < 0.999)
D[ring] = np.minimum(D[ring], 0.25 + 0.55 * (1.0 - cov[ring]))

Rmax = max(D.max(), 1e-6)
t = np.clip(D / Rmax, 0.0, 1.0)

# circular (pillow) profile -> puffy rounded solid
prof = np.sqrt(np.clip(2 * t - t * t, 0.0, 1.0))
dprof = np.clip((1.0 - t) / np.sqrt(np.clip(2 * t - t * t, 1e-4, None)), 0.0, 5.0)

Dy, Dx = np.gradient(D)
glen = np.sqrt(Dx * Dx + Dy * Dy)
glen[glen < 1e-6] = 1e-6
ux, uy = Dx / glen, Dy / glen

slope = PUFF * dprof / Rmax
Nx = -slope * ux
Ny = -slope * uy
Nz = np.ones_like(slope)
nlen = np.sqrt(Nx * Nx + Ny * Ny + Nz * Nz)
Nx /= nlen
Ny /= nlen
Nz /= nlen

# smooth the normal field to kill distance-transform seams / cleft artefacts
def smooth3(a, r=1):
    out = np.zeros_like(a)
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out += np.roll(np.roll(a, (dy, dx), (0, 1)), 0)
    return out / ((2 * r + 1) ** 2)

Nsm = np.stack([smooth3(Nx), smooth3(Ny), smooth3(Nz)], -1)
Nsm *= inside[..., None]
Nsm[..., 2] = np.where(inside, Nsm[..., 2], 1.0)
nl = np.sqrt((Nsm ** 2).sum(-1))
nl[nl < 1e-6] = 1e-6
Nsm /= nl[..., None]
Nx, Ny, Nz = Nsm[..., 0], Nsm[..., 1], Nsm[..., 2]

# centre crease: a soft vertical fold down the front of the heart
crease = np.exp(-((xx - 31.5) ** 2) / 6.0) * np.clip((yy - 12.0) / 26.0, 0.0, 1.0)
crease *= np.clip((44.0 - yy) / 10.0, 0.0, 1.0)

# ----------------------------------------------------------------------
# 3. lighting
# ----------------------------------------------------------------------
L = KEY_DIR / np.linalg.norm(KEY_DIR)
F = FILL_DIR / np.linalg.norm(FILL_DIR)
Vv = np.array([0.0, 0.0, 1.0])
Hv = L + Vv
Hv /= np.linalg.norm(Hv)

# groove tilt from the centre crease, then renormalise
Nx = Nx - 0.10 * (xx - 31.5) * crease
_nl = np.sqrt(Nx * Nx + Ny * Ny + Nz * Nz)
Nx, Ny, Nz = Nx / _nl, Ny / _nl, Nz / _nl

ndotl = np.clip(Nx * L[0] + Ny * L[1] + Nz * L[2], 0.0, 1.0)
ndotf = np.clip(Nx * F[0] + Ny * F[1] + Nz * F[2], 0.0, 1.0)
ndoth = np.clip(Nx * Hv[0] + Ny * Hv[1] + Nz * Hv[2], 0.0, 1.0)
spec = np.power(ndoth, SPEC_POW) * SPEC_STR
sheen = np.power(ndoth, SHEEN_POW) * SHEEN_STR
fres = np.power(1.0 - np.clip(Nz, 0.0, 1.0), 2.4)

# thin-edge translucency (light passing through the flesh)
thin = np.clip(1.0 - t * 2.4, 0.0, 1.0) ** 1.6
sss = thin * (0.30 + 0.70 * ndotl) * SSS_STR

# albedo: deeper/maroon low and to the lower-right, richer red up top
yn = np.clip((yy - 4.0) / 50.0, 0.0, 1.0)
xn = np.clip((xx - 5.0) / 54.0, 0.0, 1.0)
a = np.clip(0.40 * prof + 0.66 * (1.0 - yn) - 0.24 * xn + 0.06, 0.0, 1.0)

RAMP = np.array([
    [38, 4, 14],
    [74, 8, 20],
    [118, 12, 26],
    [156, 18, 30],
    [188, 28, 34],
    [212, 46, 42],
    [232, 84, 62],
], dtype=np.float64) / 255.0


def ramp(sample):
    s = np.clip(sample, 0.0, 1.0) * (len(RAMP) - 1)
    i0 = np.clip(np.floor(s).astype(int), 0, len(RAMP) - 2)
    fr = (s - i0)[..., None]
    return RAMP[i0] * (1 - fr) + RAMP[i0 + 1] * fr


albedo = ramp(a)

grain = (RNG.random((H, W, 1)) - 0.5) * 0.016
mottle = (RNG.random((H // 5 + 2, W // 5 + 2, 1)) - 0.5)
mottle = np.kron(mottle, np.ones((5, 5, 1)))[:H, :W, :] * 0.022
albedo = np.clip(albedo * (1.0 + mottle) + grain, 0.0, 1.0)

amb_col = np.array([0.40, 0.24, 0.30])
key_col = np.array([1.12, 0.76, 0.66])
fill_col = np.array([0.30, 0.14, 0.20])
sss_col = np.array([1.00, 0.14, 0.07])
spec_col = np.array([1.00, 0.97, 0.95])
rim_col = np.array([0.88, 0.22, 0.19])

B = np.array([0.0, 0.55, 0.38])
B /= np.linalg.norm(B)
ndotb = np.clip(Nx * B[0] + Ny * B[1] + Nz * B[2], 0.0, 1.0)

lit = albedo * (AMBIENT * amb_col
                + ndotl[..., None] * key_col
                + ndotf[..., None] * fill_col * 0.55
                + ndotb[..., None] * np.array([0.55, 0.16, 0.12]) * 0.6)
lit = lit + sss[..., None] * sss_col
lit = lit + (spec[..., None] + sheen[..., None] * 0.6) * spec_col
lit = lit + (np.power(ndoth, 16.0) * 0.22)[..., None] * spec_col
cleft = np.exp(-((xx - 31.5) ** 2) / 2.4) * np.clip((17.0 - yy) / 9.0, 0.0, 1.0) * inside
lit = lit * (1.0 - 0.38 * cleft)[..., None]
lit = lit + (fres * RIM_STR)[..., None] * rim_col
lit = lit + albedo * sheen[..., None] * np.array([0.5, 0.18, 0.16])
lit = lit * (1.0 - 0.22 * crease)[..., None]

# soft tone map, then to 8-bit
lit = lit / (1.0 + 0.22 * lit)
heart_rgb = np.clip(lit, 0.0, 1.0) * 255.0

# ----------------------------------------------------------------------
# 4. backdrop: gradient + glow + cast shadow + AO
# ----------------------------------------------------------------------
dxs = (xx - 27.0) / 40.0
dys = (yy - 26.0) / 40.0
glow = np.exp(-(dxs * dxs + dys * dys) * 0.85)
vig = np.clip(1.0 - 0.30 * ((xx - 31.5) ** 2 + (yy - 31.5) ** 2) / (44.0 ** 2), 0.0, 1.0)

top = np.array([34, 29, 38], dtype=np.float64)
bot = np.array([13, 11, 17], dtype=np.float64)
bg = (top[None, None, :] * (1 - yn[..., None]) + bot[None, None, :] * yn[..., None])
bg = bg * (0.55 + 0.45 * vig)[..., None]
bg = bg + glow[..., None] * np.array([46, 20, 16])


def box_blur(img, r, passes=2):
    a = img.astype(np.float64)
    for _ in range(passes):
        pad = np.pad(a, ((r, r), (0, 0), (0, 0)), mode="edge")
        c = np.cumsum(pad, axis=0)
        a = (c[2 * r:, :, :] - c[:-2 * r, :, :]) / (2 * r + 1)
        pad = np.pad(a, ((0, 0), (r, r), (0, 0)), mode="edge")
        c = np.cumsum(pad, axis=1)
        a = (c[:, 2 * r:, :] - c[:, :-2 * r, :]) / (2 * r + 1)
    return a


mask3 = inside[..., None].astype(np.float64)
shifted = np.zeros_like(mask3)
sy, sx = 7, 6
shifted[sy:, sx:, :] = mask3[:H - sy, :W - sx, :]
shadow = box_blur(shifted, 3, 3)[..., 0]
ao = box_blur(mask3, 2, 2)[..., 0]

bg = bg * (1.0 - 0.72 * np.clip(shadow, 0, 1))[..., None]
bg = bg * (1.0 - 0.45 * np.clip(ao - 0.15, 0, 1))[..., None]
bg = np.clip(bg, 0, 255)

# ----------------------------------------------------------------------
# composite with a touch of silhouette anti-aliasing
# ----------------------------------------------------------------------
img = bg.copy()
w = np.clip(cov, 0.0, 1.0)
w = np.where(inside, np.maximum(w, 0.55), w)
img = img * (1 - w[..., None]) + heart_rgb * w[..., None]
img = np.clip(img, 0, 255)

# ----------------------------------------------------------------------
# 5. median-cut quantisation
# ----------------------------------------------------------------------


def median_cut(img_u8, max_colors):
    px = img_u8.reshape(-1, 3).astype(np.float64)
    uniq, counts = np.unique(px, axis=0, return_counts=True)
    boxes = [[uniq, counts.astype(np.float64)]]
    while len(boxes) < max_colors:
        best, best_score = -1, -1.0
        for i, (cs, ws) in enumerate(boxes):
            if len(cs) < 2:
                continue
            rng = cs.max(0) - cs.min(0)
            score = rng.max() * (ws.sum() ** 0.5)
            if score > best_score:
                best_score, best = score, i
        if best < 0:
            break
        cs, ws = boxes.pop(best)
        axis = int(np.argmax(cs.max(0) - cs.min(0)))
        order = np.argsort(cs[:, axis], kind="stable")
        cs, ws = cs[order], ws[order]
        cw = np.cumsum(ws)
        k = int(np.searchsorted(cw, cw[-1] * 0.5))
        k = max(1, min(len(cs) - 1, k))
        boxes.append([cs[:k], ws[:k]])
        boxes.append([cs[k:], ws[k:]])
    pal = np.array([(cs * ws[:, None]).sum(0) / ws.sum() for cs, ws in boxes])
    pal = np.clip(np.round(pal), 0, 255)
    d = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1)
    idx = d.argmin(1)
    return np.clip(np.round(pal[idx]), 0, 255).astype(np.uint8).reshape(img_u8.shape)


final = median_cut(np.clip(np.round(img), 0, 255).astype(np.uint8), MAX_COLORS)
used = np.unique(final.reshape(-1, 3), axis=0)
print("distinct colours:", len(used), "| heart px:", n_in, "| Rmax:", round(Rmax, 2))

c = new_canvas(W, H, name="heart")
for y in range(H):
    for x in range(W):
        r, g, b = final[y, x]
        c.set(x, y, "#%02x%02x%02x" % (int(r), int(g), int(b)))

view(c)
save("realistic_heart", c)
finish(c)
