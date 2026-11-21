import math, random
from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H, name="minecraft_stone")

# ---- palette (8 visible colors, all grays, Minecraft-stone family) ----
CRACK = c.color((30, 30, 30))
levels = [
    c.color((88, 88, 88)),
    c.color((101, 101, 101)),
    c.color((114, 114, 114)),
    c.color((127, 127, 127)),
    c.color((141, 141, 141)),
    c.color((155, 155, 155)),
    c.color((169, 169, 169)),
]

def smooth(t):
    return t * t * (3 - 2 * t)

def lattice(cell, seed):
    rng = random.Random(seed)
    g = W // cell
    return [[rng.random() for _ in range(g)] for _ in range(g)]

def vnoise(x, y, cell, lat):
    g = W // cell
    gx = (x // cell) % g
    gy = (y // cell) % g
    fx = (x % cell) / cell
    fy = (y % cell) / cell
    sx = smooth(fx)
    sy = smooth(fy)
    a = lat[gy][gx] + (lat[gy][(gx + 1) % g] - lat[gy][gx]) * sx
    b = lat[(gy + 1) % g][gx] + (lat[(gy + 1) % g][(gx + 1) % g] - lat[(gy + 1) % g][gx]) * sx
    return a + (b - a) * sy

lat_c = lattice(8, 3)
lat_f = lattice(4, 11)
rng = random.Random(42)

for y in range(H):
    for x in range(W):
        v = 0.60 * vnoise(x, y, 8, lat_c) + 0.40 * vnoise(x, y, 4, lat_f)
        t = max(0.0, min(1.0, (v - 0.14) / 0.72))
        idx = min(6, int(t * 7))
        r = rng.random()
        if r < 0.05:
            idx = min(6, idx + 1)
        elif r > 0.965:
            idx = max(0, idx - 1)
        c.set(x, y, levels[idx])

# ---- seamless crack drawing (wrapped Bresenham on the 16x16 torus) ----
def bres(x0, y0, x1, y1):
    pts = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        pts.append((x, y))
        if x == x1 and y == y1:
            return pts
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

def crack_seg(x0, y0, x1, y1):
    ox = round((x0 - x1) / 16.0) * 16
    oy = round((y0 - y1) / 16.0) * 16
    for (x, y) in bres(x0, y0, x1 + ox, y1 + oy):
        c.set(x % 16, y % 16, CRACK)

# crack A: vertical, wraps the top/bottom seam
crackA = [(11, 0), (12, 3), (9, 6), (10, 9), (13, 12), (11, 15)]
for i in range(len(crackA)):
    x0, y0 = crackA[i]
    x1, y1 = crackA[(i + 1) % len(crackA)]
    crack_seg(x0, y0, x1, y1)

# crack B: horizontal, wraps the left/right seam
crackB = [(0, 4), (3, 5), (6, 3), (9, 6), (12, 4), (15, 5)]
for i in range(len(crackB)):
    x0, y0 = crackB[i]
    x1, y1 = crackB[(i + 1) % len(crackB)]
    crack_seg(x0, y0, x1, y1)

# short interior branches / chips
crack_seg(6, 11, 8, 10)
crack_seg(3, 12, 4, 10)
crack_seg(9, 9, 9, 9)
# chipped edges along the cracks
for (x, y) in [(9, 6), (10, 8), (11, 9), (8, 10), (5, 4), (6, 2), (1, 4), (14, 5), (12, 3), (11, 1)]:
    c.set(x % 16, y % 16, levels[0])
for (x, y) in [(10, 5), (9, 7), (10, 10), (4, 4), (6, 3), (13, 4), (8, 11)]:
    c.set(x % 16, y % 16, levels[1])

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15), indices=True))

finish(c)
