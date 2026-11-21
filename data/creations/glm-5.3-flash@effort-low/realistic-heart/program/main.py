from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="heart")

# Realistic heart via implicit curve with shaded gradient
def heart_f(x, y):
    # normalized heart implicit, y up
    return (x*x + y*y - 1)**3 - x*x * y**3

# ramp from deep shadow to bright
ramp = [
    (58, 4, 12), (94, 8, 22), (138, 12, 32), (178, 18, 42),
    (212, 30, 58), (234, 56, 82), (246, 96, 116), (252, 150, 168),
    (255, 200, 210),
]
spec = (255, 240, 244)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def quant(col):
    best, bd = ramp[0], 1e9
    for r in ramp + [spec]:
        d = sum((r[i]-col[i])**2 for i in range(3))
        if d < bd:
            bd, best = d, r
    return best

# highlight center (upper-left lobe) in heart coords
hx, hy = -0.42, 0.62
sx, sy = -0.35, 0.78  # specular

pts = {}
for py in range(64):
    for px in range(64):
        # map pixel to heart coords, y flipped
        X = (px - 32) / 26.0
        Y = (36 - py) / 26.0
        f = heart_f(X, Y)
        if f > 0:
            continue
        # depth: how far inside (normalized)
        depth = min(1.0, (-f) / 1.6)
        # base gradient: light from upper-left, so shade falls to lower-right
        light = 0.5 + 0.5 * ((-X) * 0.8 + Y * 0.6)
        light = max(0.0, min(1.0, light))
        t = depth * 0.55 + light * 0.45
        t = max(0.0, min(1.0, t))
        pos = t * (len(ramp) - 1)
        i = min(int(pos), len(ramp) - 2)
        col = lerp(ramp[i], ramp[i+1], pos - i)
        # rim darkening near edge
        if depth < 0.10:
            col = lerp(ramp[0], col, depth / 0.10 * 0.7 + 0.3)
        # highlight lobe
        dh = ((X-hx)**2 + (Y-hy)**2) ** 0.5
        if dh < 0.55:
            col = lerp(col, ramp[7], (1 - dh/0.55) * 0.55)
        # specular
        ds = ((X-sx)**2 + (Y-sy)**2) ** 0.5
        if ds < 0.16:
            col = lerp(col, spec, (1 - ds/0.16) * 0.9)
        pts[(px, py)] = quant(col)

# subtle reflected light on bottom-right rim
for (px, py), col in list(pts.items()):
    X = (px - 32) / 26.0
    Y = (36 - py) / 26.0
    f = heart_f(X, Y)
    depth = min(1.0, (-f) / 1.6)
    if depth < 0.12 and X > 0.1 and Y < 0:
        pts[(px, py)] = ramp[4]

for (px, py), col in pts.items():
    c.set(px, py, col)

print(c.stats_text())
save("realistic_heart", c)
finish(c)
