import random
from pixelbench_api import new_canvas, finish

W = H = 16

# Minecraft-style earthy dirt palette (9 colours, under the 10 limit)
COL = [
    (0x2E, 0x1E, 0x12),  # 0 very dark speck
    (0x3F, 0x2B, 0x1B),  # 1 dark clump
    (0x4E, 0x37, 0x23),  # 2
    (0x5C, 0x42, 0x2A),  # 3 base dark
    (0x6B, 0x4F, 0x33),  # 4 base
    (0x7A, 0x5C, 0x3C),  # 5
    (0x8A, 0x6A, 0x46),  # 6
    (0x9B, 0x7A, 0x53),  # 7 light patch
    (0xAC, 0x8B, 0x62),  # 8 light speck
]

rng = random.Random(20260418)


def smooth(t):
    return t * t * (3 - 2 * t)


def make_grid(grid, seed):
    r = random.Random(seed)
    return [[r.random() for _ in range(grid)] for _ in range(grid)]


def sample(vals, grid, x, y):
    """Periodic value noise sample (period == grid, so 16px canvas tiles seamlessly)."""
    lat0 = (x // grid) * grid
    lat1 = lat0 + grid
    fx = (x - lat0) / grid
    i0 = lat0 % grid
    i1 = lat1 % grid
    row0 = (y // grid) * grid
    row1 = row0 + grid
    fy = (y - row0) / grid
    j0 = row0 % grid
    j1 = row1 % grid
    sx = smooth(fx)
    sy = smooth(fy)
    a = vals[j0][i0] * (1 - sx) + vals[j0][i1] * sx
    b = vals[j1][i0] * (1 - sx) + vals[j1][i1] * sx
    return a * (1 - sy) + b * sy


g4 = make_grid(4, 11)
g8 = make_grid(8, 22)
g2 = make_grid(2, 33)

c = new_canvas(W, H, name="dirt")

TABLE = [0, 1, 1, 2, 3, 4, 4, 5, 6, 7]


def hash01(x, y, seed):
    h = (x * 374761393 + y * 668265263 + seed * 2246822519) & 0xFFFFFFFF
    h = (h ^ (h >> 13)) * 1274126177 & 0xFFFFFFFF
    h = h ^ (h >> 16)
    return (h & 0xFFFF) / 65535.0


for y in range(H):
    for x in range(W):
        v = 0.5 * sample(g4, 4, x, y) + 0.35 * sample(g8, 8, x, y) + 0.15 * sample(g2, 2, x, y)
        v = (v - 0.5) * 1.6 + 0.5
        j = (hash01(x, y, 77) - 0.5) * 0.6
        v = v + j
        if v < 0:
            v = 0
        elif v > 1:
            v = 1
        ci = TABLE[min(int(v * 10), 9)]
        if ci > 7:
            ci = 7
        r = rng.random()
        if r < 0.03:
            ci = 0
        elif r < 0.06:
            ci = 1
        elif r < 0.115:
            ci = 8
        elif r < 0.15:
            ci = 7
        c.set(x, y, COL[ci])

print(c.stats_text())
print(c.matrix_text())
finish(c)
