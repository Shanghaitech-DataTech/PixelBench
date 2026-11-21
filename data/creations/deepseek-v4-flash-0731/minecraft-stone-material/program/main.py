import random
from pixelbench_api import new_canvas, finish

W = H = 16

# ---- palette (7 visible colours) ----
COLS = {
    "crack":  "#333333",
    "edge":   "#444444",
    "dark":   "#5a5a5a",
    "base":   "#757575",
    "mid":    "#858585",
    "light":  "#969696",
    "white":  "#a8a8a8",
}

c = new_canvas(W, H)
c.rect(0, 0, W, H, COLS["base"])

# ---- seamless value noise (lattice wraps) ----
L = 8
rng = random.Random(20240607)
lat = [[rng.random() for _ in range(L)] for _ in range(L)]

def at(ix, iy):
    return lat[iy % L][ix % L]

def sample(x, y):
    fx = x / W * L
    fy = y / H * L
    ix = int(fx) % L
    iy = int(fy) % L
    dx = fx - int(fx)
    dy = fy - int(fy)
    sx = dx * dx * (3 - 2 * dx)
    sy = dy * dy * (3 - 2 * dy)
    return ((at(ix, iy) * (1 - sx) + at(ix + 1, iy) * sx) * (1 - sy)
            + (at(ix, iy + 1) * (1 - sx) + at(ix + 1, iy + 1) * sx) * sy)

def spackle(x, y):
    r = random.Random((x * 73856093) ^ (y * 19349663) ^ 0x9E3779B9)
    return r.random()

for y in range(H):
    for x in range(W):
        v = 0.62 * sample(x, y) + 0.38 * spackle(x, y)
        if v < 0.30:
            k = "dark"
        elif v < 0.50:
            k = "base"
        elif v < 0.68:
            k = "mid"
        elif v < 0.86:
            k = "light"
        else:
            k = "white"
        c.set(x, y, COLS[k])

# ---- cracks: wrapped random walks ----
crack_idx = c.color(COLS["crack"], "crack")
edge_idx = c.color(COLS["edge"], "edge")
pixels = [[c.get(x, y) for x in range(W)] for y in range(H)]

rc = random.Random(7755)
for _ in range(3):
    x = rc.randrange(W)
    y = rc.randrange(H)
    steps = rc.randrange(10, 15)
    for s in range(steps):
        pixels[y % H][x % W] = crack_idx
        if rc.random() < 0.22:
            pixels[y % H][(x + 1) % W] = crack_idx
        if rc.random() < 0.12:
            pixels[(y + 1) % H][(x + 1) % W] = crack_idx
        d = rc.choice([(1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (-1, 1), (1, -1), (-1, -1)])
        x += d[0]
        y += d[1]

# soft dark shadow pixels hugging cracks for depth
rd = random.Random(31)
for y in range(H):
    for x in range(W):
        if pixels[y][x] != crack_idx:
            n = 0
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if pixels[(y + dy) % H][(x + dx) % W] == crack_idx:
                    n += 1
            if n >= 1 and rd.random() < 0.18:
                pixels[y][x] = edge_idx

for y in range(H):
    for x in range(W):
        c.set(x, y, pixels[y][x])

print(c.stats_text())
print([[e["index"], e["name"], e["rgba"]] for e in c.palette()])
print(c.matrix_text(region=(0, 0, 15, 15), indices=True))

finish(c)
