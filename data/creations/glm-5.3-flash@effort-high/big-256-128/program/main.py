import numpy as np

c = input_canvas
out = c.copy(name='output')
W, H, rgba = out.to_rgba()
arr = np.array(rgba, dtype=np.float64).reshape(H, W, 4)
rgb = arr[..., :3]
alpha = arr[..., 3:4]


def rgb_to_hsv(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx = np.max(a, axis=-1)
    mn = np.min(a, axis=-1)
    diff = mx - mn
    safe = diff + 1e-9
    h = np.zeros_like(mx)
    m1 = (mx == r) & (diff > 0)
    h[m1] = ((g - b)[m1] / safe[m1]) % 6.0
    m2 = (mx == g) & (diff > 0) & ~m1
    h[m2] = (b - r)[m2] / safe[m2] + 2.0
    m3 = (mx == b) & (diff > 0) & ~m1 & ~m2
    h[m3] = (r - g)[m3] / safe[m3] + 4.0
    h = h * 60.0
    s = np.where(mx > 0, diff / (mx + 1e-9), 0.0)
    v = mx / 255.0
    return h, s, v


def hsv_to_rgb(h, s, v):
    i = np.floor(h / 60.0).astype(int) % 6
    f = h / 60.0 - np.floor(h / 60.0)
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r = np.choose(i, [v, q, p, p, t, v])
    g = np.choose(i, [t, v, v, q, p, p])
    b = np.choose(i, [p, p, t, v, v, q])
    return np.stack([r, g, b], axis=-1) * 255.0


h, s, v = rgb_to_hsv(rgb)

# ---- global hue compression: everything toward crimson / blood-red ----
h2 = (h * 0.10 + 340.0) % 360.0
yy = np.arange(H, dtype=np.float64).reshape(-1, 1)
xx = np.arange(W, dtype=np.float64).reshape(1, -1)

sky = yy < 42
bld = (yy >= 42) & (yy < 98)
gnd = yy >= 98

# sky: dramatic darkening toward the top, saturated blood tones
s2 = np.where(sky, np.clip(s * 1.45 + 0.10, 0, 1), s)
sky_dark = np.clip(0.42 + 0.58 * (yy / 42.0), 0.42, 1.0)
v2 = np.where(sky, v * sky_dark, v)

# buildings: desaturated dark stone with a crimson cast
s2 = np.where(bld, np.clip(s * 0.50 + 0.04, 0, 1), s2)
v2 = np.where(bld, v * 0.74, v2)

# foreground ground: near-black
s2 = np.where(gnd, np.clip(s * 0.40, 0, 1), s2)
v2 = np.where(gnd, v * 0.42, v2)

# keep near-blacks from going muddy
v2 = np.where(v < 0.06, v * 0.9, v2)

rgb2 = hsv_to_rgb(h2, s2, v2)

# ---- blood moon: repaint the bright blob as a hanging blood moon ----
mcx, mcy = 128.0, 22.0
dist = np.sqrt((xx - mcx) ** 2 + ((yy - mcy) * 1.0) ** 2)

moon_glow1 = dist < 26
moon_glow2 = dist < 21
moon_glow3 = dist < 17
moon_disc = dist < 13.5
moon_mid = dist < 10.5
moon_in = dist < 7.0
moon_core = dist < 4.0


def blend(base, over_mask, col, strength=1.0):
    col = np.array(col, dtype=np.float64)
    base[over_mask] = base[over_mask] * (1 - strength) + col * strength
    return base


# glow layers (subtle, over the sky)
rgb2 = blend(rgb2, moon_glow1, (46, 12, 20), 0.55)
rgb2 = blend(rgb2, moon_glow2, (74, 16, 24), 0.60)
rgb2 = blend(rgb2, moon_glow3, (108, 22, 28), 0.70)
# moon disc
rgb2 = blend(rgb2, moon_disc, (140, 30, 26), 1.0)
rgb2 = blend(rgb2, moon_mid, (176, 44, 32), 1.0)
rgb2 = blend(rgb2, moon_in, (210, 62, 40), 1.0)
rgb2 = blend(rgb2, moon_core, (238, 88, 52), 1.0)

# craters on the moon face
for (dx, dy, cr) in [(-5, -3, 2.2), (4, 2, 2.6), (-2, 5, 1.8), (6, -5, 1.6), (0, -7, 1.4)]:
    d2 = np.sqrt((xx - (mcx + dx)) ** 2 + (yy - (mcy + dy)) ** 2)
    rgb2 = blend(rgb2, d2 < cr, (120, 24, 22), 0.85)

# thin dark rim
rim = (dist >= 13.0) & (dist < 14.5)
rgb2 = blend(rgb2, rim, (70, 14, 18), 0.8)

# ---- demonic window / lava lights on the castle ----
rng_lights = []
for ly in range(48, 96, 3):
    for lx in range(4, 253, 5):
        seed = (lx * 7 + ly * 13 + (lx // 5) * 31) % 97
        if seed < 14:
            rng_lights.append((lx, ly))

for (lx, ly) in rng_lights:
    ix, iy = int(lx), int(ly)
    px = rgb2[iy, ix]
    val = px.max() / 255.0
    if val < 0.40:
        # warm demonic glow
        rgb2[iy, ix] = (232, 120, 52)
        if ix + 1 < W:
            rgb2[iy, ix + 1] = (198, 88, 44)

# a few brighter torch accents on the castle
for (tx, ty) in [(30, 62), (58, 70), (92, 58), (150, 66), (185, 60), (215, 72), (245, 64), (110, 78)]:
    if 0 <= tx < W and 0 <= ty < H:
        rgb2[ty, tx] = (245, 140, 60)
        rgb2[ty, tx + 1] = (210, 100, 48)

# ---- subtle red rim-light on the horizon silhouette ----
horizon = (yy >= 40) & (yy <= 43)
rgb2 = blend(rgb2, horizon, (90, 20, 26), 0.25)

out_arr = np.concatenate([rgb2, alpha], axis=-1)
out_arr = np.clip(out_arr, 0, 255).astype(np.uint8)

for y in range(H):
    for x in range(W):
        r, g, b, a = out_arr[y, x]
        if a == 0:
            out.set(x, y, None)
        else:
            out.set(x, y, (int(r), int(g), int(b), int(a)))

print(out.stats_text())
finish(out)
