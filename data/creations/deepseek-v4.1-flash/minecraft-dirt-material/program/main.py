import math
import random

from pixelbench_api import new_canvas, finish, save

W = H = 16

# ------------------------------------------------------------------ palette
# Nine-step warm brown ramp: Minecraft-ish dirt, coarse and granular.
PAL = [
    "#452E1F",  # 0 deepest crevice
    "#523726",  # 1 dark clump
    "#60422C",  # 2 shadow grain
    "#6E4D32",  # 3 base dark
    "#7D5A3B",  # 4 base
    "#8A6543",  # 5 base light
    "#97704A",  # 6 light grain
    "#A47B53",  # 7 brighter grain
    "#B2895F",  # 8 highlight speck
]

c = new_canvas(W, H, background=None, name="dirt")


# ------------------------------------------------------------------ helpers
def smooth(t):
    return t * t * (3.0 - 2.0 * t)


def norm2d(m):
    lo = min(min(r) for r in m)
    hi = max(max(r) for r in m)
    d = (hi - lo) or 1.0
    return [[(v - lo) / d for v in r] for r in m]


def toroidal_noise(seed, cx, cy):
    """Value noise sampled on a 16x16 torus -> the tile wraps seamlessly."""
    rng = random.Random(seed)
    lat = [[rng.random() for _ in range(cx)] for _ in range(cy)]
    out = [[0.0] * W for _ in range(H)]
    sx, sy = cx / float(W), cy / float(H)
    for y in range(H):
        fy = y * sy
        y0 = int(math.floor(fy)) % cy
        y1 = (y0 + 1) % cy
        ty = smooth(fy - math.floor(fy))
        for x in range(W):
            fx = x * sx
            x0 = int(math.floor(fx)) % cx
            x1 = (x0 + 1) % cx
            tx = smooth(fx - math.floor(fx))
            a = lat[y0][x0] * (1 - tx) + lat[y0][x1] * tx
            b = lat[y1][x0] * (1 - tx) + lat[y1][x1] * tx
            out[y][x] = a * (1 - ty) + b * ty
    return norm2d(out)


# --------------------------------------------- clods, mottling and grit
SEED = 88
clod = toroidal_noise(SEED, 4, 4)            # large clods of soil
blotch = toroidal_noise(SEED + 77, 5, 7)     # medium mottling
lump = toroidal_noise(SEED + 131, 6, 6)      # small lumps
grit = toroidal_noise(SEED + 211, 9, 9)      # coarse grain variation
fine = toroidal_noise(SEED + 303, 12, 12)    # per-pixel grit
rng = random.Random(SEED + 5005)

raw = [[0.24 * clod[y][x] + 0.32 * blotch[y][x]
        + 0.28 * lump[y][x] + 0.16 * grit[y][x]
        for x in range(W)] for y in range(H)]
tone = norm2d(raw)

grid = [[4] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        d = 2.0 * tone[y][x] - 1.0
        base = 4.0 + 3.8 * (1.0 if d >= 0 else -1.0) * abs(d) ** 1.4
        speck = 0.55 * fine[y][x] + 0.45 * rng.random()
        off = round((speck - 0.5) * 2.3)
        grid[y][x] = max(0, min(8, int(round(base)) + off))

# ------------------------------------------------- hand-placed dirt details
# a small dark pocket / crevice in the middle of the tile
CREVICE = [(7, 6, 1), (7, 7, 0), (8, 8, 1), (6, 6, 2)]
for x, y, v in CREVICE:
    grid[y][x] = v
    if rng.random() < 0.55:
        grid[(y + 1) % H][x] = min(grid[(y + 1) % H][x], v + 1)

# a few shadowed pits scattered over the open ground
PITS = [(9, 13, 1), (1, 9, 1), (13, 1, 2), (2, 5, 2)]
for x, y, v in PITS:
    grid[y][x] = v

# bright quartz-like glints catching the light (short horizontal dashes)
GLINTS = [(3, 3, 1), (10, 4, 2), (8, 11, 2), (5, 13, 1), (7, 15, 1),
          (12, 8, 1)]
for x, y, n in GLINTS:
    for k in range(n):
        grid[y][(x + k) % W] = 8
    grid[(y + 1) % H][(x + n - 1) % W] = max(
        grid[(y + 1) % H][(x + n - 1) % W], 7)

# ---------------------------------------------------------------- painting
for y in range(H):
    for x in range(W):
        c.set(x, y, PAL[grid[y][x]])

print(c.stats_text())
print(c.matrix_text())
print("levels:")
for row in grid:
    print("  " + "".join(str(v) for v in row))
save("dirt_block", c)
finish(c)
