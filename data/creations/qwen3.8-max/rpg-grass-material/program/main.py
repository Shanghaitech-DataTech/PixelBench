"""16x16 seamless RPG grass material tile."""

try:
    new_canvas  # preloaded?
except NameError:
    from pixelbench_api import *

import random

W = H = 16

# ---- palette (8 colours) ----
BASE = "#57a53c"   # mid grass
DARK = "#3d7d2b"   # dark grass speckle
LIGHT = "#7ec854"  # light grass speckle
TUFT = "#2b6321"   # darker grass tuft
DIRT = "#9c7544"   # bare dirt
DIRTD = "#7a5832"  # dirt shadow / rim
FLOWER = "#f7e25c"  # yellow petals
FCEN = "#e0912f"    # flower centre

c = new_canvas(W, H, background=BASE, name="grass")


def put(x, y, col):
    """Set one pixel, wrapping toroidally so the tile stays seamless."""
    c.set(x % W, y % H, col)


def shape(ox, oy, offsets, col):
    for dx, dy in offsets:
        put(ox + dx, oy + dy, col)


# ---- 1. interleaved dark / light speckles ----
rng = random.Random(20240617)
cells = [(x, y) for y in range(H) for x in range(W)]
rng.shuffle(cells)

singles = cells[:32]
blades = cells[32:39]

for i, (x, y) in enumerate(singles):
    put(x, y, DARK if i % 2 == 0 else LIGHT)
for i, (x, y) in enumerate(blades):
    col = LIGHT if i % 2 == 0 else DARK
    put(x, y, col)
    put(x, y + 1, col)

# ---- 2. sparse bare-dirt patches ----
dirt_a = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2), (2, 2)]
shape(2, 11, dirt_a, DIRT)
shape(2, 11, [(0, 0), (3, 1), (1, 2)], DIRTD)
put(3, 12, DARK)  # tiny sprout inside the bare patch

dirt_b = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1)]
shape(12, 4, dirt_b, DIRT)
shape(12, 4, [(0, 1), (2, 1)], DIRTD)

# single stray dirt grains
put(8, 1, DIRTD)
put(9, 2, DIRT)

# ---- 3. small darker grass tufts ----
tuft = [(-1, 0), (0, 0), (1, 0), (-1, -1), (1, -1), (0, -2)]
for tx, ty in [(5, 3), (10, 14), (14, 8), (1, 6), (7, 9)]:
    shape(tx, ty, tuft, TUFT)

# ---- 4. a few tiny yellow flowers ----
flower = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for fx, fy in [(4, 7), (11, 10), (7, 15)]:
    shape(fx, fy, flower, FLOWER)
    put(fx, fy, FCEN)

view(c)
print(c.stats_text())
print(c.matrix_text())

# ---- seamless check: 2x2 tiling preview (not submitted) ----
t = new_canvas(W * 2, H * 2, name="tiled")
for j in range(2):
    for i in range(2):
        t.blit(c, i * W, j * H)
view(t)

save("grass_tile", c)
finish(c)
