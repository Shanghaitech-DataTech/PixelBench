from pixelbench_api import new_canvas, finish
import random

W = H = 16

BASE = (58, 138, 58)      # mid green base
DARK = (40, 104, 40)     # dark green speckle
LIGHT = (128, 196, 96)   # light green speckle
DIRT = (124, 84, 46)     # bare dirt
DIRT_D = (100, 66, 34)   # darker dirt
TUFT = (28, 82, 32)      # darker grass tuft
FLOWER = (242, 208, 66)  # yellow petal
FLOWER_C = (252, 238, 150)  # pale flower centre

rng = random.Random(2024)

c = new_canvas(W, H)
c.rect(0, 0, W, H, BASE)

def pset(x, y, col):
    # wrap modulo so the tile is seamless in every direction
    c.set(x % W, y % H, col)

# interleaved dark / light grass speckles across the whole tile
for y in range(H):
    for x in range(W):
        r = rng.random()
        if r < 0.085:
            pset(x, y, DARK)
        elif r < 0.21:
            pset(x, y, LIGHT)

# sparse bare-dirt patches (small wrapped blobs)
for _ in range(3):
    cx = rng.randrange(W)
    cy = rng.randrange(H)
    pset(cx, cy, DIRT_D)
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if rng.random() < 0.45:
                pset(cx + dx, cy + dy, DIRT)

# small darker grass tufts
for _ in range(4):
    tx = rng.randrange(W)
    ty = rng.randrange(H)
    pset(tx, ty, TUFT)
    if rng.random() < 0.8:
        pset(tx + 1, ty + 1, TUFT)
    if rng.random() < 0.7:
        pset(tx, ty + 2, TUFT)

# a few tiny yellow flowers (pale centre + 3-4 yellow petals around it)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(3):
    fx = rng.randrange(W)
    fy = rng.randrange(H)
    pset(fx, fy, FLOWER_C)
    rng.shuffle(dirs)
    for dx, dy in dirs[: rng.choice([3, 4])]:
        pset(fx + dx, fy + dy, FLOWER)

print(c.stats_text())
print(c.matrix_text())
finish(c)
