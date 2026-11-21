from pixelbench_api import *

W = H = 64
import math

def sd_circle(px, py, cx, cy, r):
    return math.hypot(px - cx, py - cy) - r

def sd_ellipse(px, py, cx, cy, rx, ry, rot=0.0):
    xr = px - cx
    yr = py - cy
    if rot:
        ca = math.cos(rot); sa = math.sin(rot)
        a = xr * ca + yr * sa
        b = -xr * sa + yr * ca
        xr, yr = a, b
    return math.hypot(xr / rx, yr / ry) - 1.0

def sd_seg(px, py, x0, y0, x1, y1):
    vx = x1 - x0; vy = y1 - y0
    l2 = vx * vx + vy * vy
    t = 0.0 if l2 == 0 else max(0.0, min(1.0, ((px - x0) * vx + (py - y0) * vy) / l2))
    return math.hypot(px - (x0 + t * vx), py - (y0 + t * vy))

def sdf_heart(px, py):
    d = 1e9
    d = min(d, sd_circle(px, py, 27, 30, 12.8))
    d = min(d, sd_circle(px, py, 37, 30, 12.6))
    d = min(d, sd_ellipse(px, py, 32, 45, 16.0, 14.5))
    d = min(d, sd_ellipse(px, py, 25, 54, 9.2, 8.2, math.radians(-30)))
    d = min(d, sd_ellipse(px, py, 41, 51, 8.6, 9.2, math.radians(20)))
    d = min(d, sd_circle(px, py, 19.5, 39, 5.4))
    return d

def sdf_vessels(px, py):
    d = 1e9
    d = min(d, sd_seg(px, py, 34, 3, 36, 17) - 4.0)   # ascending aorta
    d = min(d, sd_seg(px, py, 36, 17, 47, 24) - 4.0)  # aortic arch
    d = min(d, sd_seg(px, py, 47, 24, 50, 33) - 3.2)  # descending aorta
    d = min(d, sd_seg(px, py, 30, 13, 22, 7) - 3.1)   # left pulmonary artery
    d = min(d, sd_seg(px, py, 33, 13, 42, 6) - 3.1)   # right pulmonary artery
    d = min(d, sd_seg(px, py, 31, 14, 26, 18) - 3.1)  # pulmonary trunk
    return d

def sdf(px, py):
    return min(sdf_heart(px, py), sdf_vessels(px, py))

groove_segs = [
    ((31, 32), (25, 50)),
    ((25, 50), (24, 54)),
    ((20, 31), (44, 31)),
    ((20, 37), (40, 31)),
    ((33, 31), (28, 43)),
]
def groove_dist(px, py):
    m = 1e9
    for (a, b) in groove_segs:
        m = min(m, sd_seg(px, py, a[0], a[1], b[0], b[1]))
    return m

stops = [(0.0, (58, 6, 16)), (0.42, (148, 16, 24)), (0.75, (208, 52, 56)), (1.0, (255, 190, 170))]
def gradient(t):
    t = max(0.0, min(1.0, t))
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]; t1, c1 = stops[i + 1]
        if t <= t1:
            f = 0.0 if t1 == t0 else (t - t0) / (t1 - t0)
            return (round(c0[0] + (c1[0] - c0[0]) * f),
                    round(c0[1] + (c1[1] - c0[1]) * f),
                    round(c0[2] + (c1[2] - c0[2]) * f))
    return stops[-1][1]

L = (-0.42, -0.52, 0.74)
ln = math.sqrt(sum(v * v for v in L))
L = (L[0] / ln, L[1] / ln, L[2] / ln)

EDGE = (34, 3, 9)
NQ = 28.0

canvas = new_canvas(W, H, name="heart")

for y in range(H):
    for x in range(W):
        d = sdf(x, y)
        if d > 0:
            continue
        dx = sdf(x + 1, y) - sdf(x - 1, y)
        dy = sdf(x, y + 1) - sdf(x, y - 1)
        nl = math.sqrt(dx * dx + dy * dy + 1.0)
        nx, ny = dx / nl, dy / nl
        nz = 1.0 / nl
        diff = max(0.0, nx * L[0] + ny * L[1] + nz * L[2])
        t = 0.22 + 0.78 * (diff ** 1.2)
        if sdf_heart(x, y) <= 0 and groove_dist(x, y) < 2.2:
            t = t * 0.60
        tq = round(t * NQ) / NQ
        col = gradient(tq)
        if diff > 0.80:
            f = round(((diff - 0.80) / 0.20) * 10) / 10
            col = (round(col[0] + (255 - col[0]) * f * 0.7),
                   round(col[1] + (225 - col[1]) * f * 0.7),
                   round(col[2] + (215 - col[2]) * f * 0.7))
        if (sdf(x + 1, y) > 0 or sdf(x - 1, y) > 0 or
            sdf(x, y + 1) > 0 or sdf(x, y - 1) > 0):
            col = EDGE
        canvas.set(x, y, col)

print(canvas.stats_text())

pal = {p["index"]: p["rgba"] for p in canvas.palette()}

# fine brightness map (2x2 blocks)
chars = " .:-=+*#%@"
print("brightness map (2x2):")
for by in range(H // 2):
    line = ""
    for bx in range(W // 2):
        tot = 0; n = 0
        for y in range(by * 2, by * 2 + 2):
            for x in range(bx * 2, bx * 2 + 2):
                c = canvas.get(x, y)
                if c == 0:
                    continue
                r, g, b, a = pal[c]
                tot += (r + g + b) / 3
                n += 1
        if n == 0:
            line += " "
        else:
            line += chars[min(9, int(tot / n / 255 * 10))]
    print(line)

counts = {}
for y in range(H):
    for x in range(W):
        c = canvas.get(x, y)
        counts[c] = counts.get(c, 0) + 1
print("colors:", len(counts), "limit 86")

finish(canvas)
