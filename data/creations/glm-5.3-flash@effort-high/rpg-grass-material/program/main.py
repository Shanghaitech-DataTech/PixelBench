from pixelbench_api import new_canvas, finish, view
import random

c = new_canvas(16, 16, background=None, name="grass_tile")

# Palette
BASE   = c.color("#4a8f3c", "grass_base")
DARK   = c.color("#2e6b28", "grass_dark")
LIGHT  = c.color("#7ab648", "grass_light")
YELLOW = c.color("#f2d13c", "flower_yellow")
DIRT   = c.color("#8a6a42", "dirt")
DIRT_D = c.color("#6b4f30", "dirt_dark")

W = H = 16

def put(x, y, col):
    """Wrap-around plot so the tile is seamless on all edges."""
    c.set(x % W, y % H, col)

# 1) Base grass
c.rect(0, 0, 16, 16, BASE)

# 2) Interleaved dark/light speckles (wrapped -> seamless)
random.seed(7)
for _ in range(26):
    x, y = random.randrange(W), random.randrange(H)
    put(x, y, DARK if random.random() < 0.5 else LIGHT)

# 3) Small darker grass tufts (little 3-pixel blades)
tufts = [(2, 3), (10, 6), (5, 11), (13, 13)]
for tx, ty in tufts:
    put(tx, ty, DARK)
    put(tx + 1, ty - 1, DARK)
    put(tx - 1, ty - 1, DARK)
    put(tx, ty - 2, DARK)

# 4) A few tiny yellow flowers (2x2-ish: yellow core + light pixel petal)
flowers = [(6, 2), (12, 9), (3, 8)]
for fx, fy in flowers:
    put(fx, fy, YELLOW)
    put(fx + 1, fy, YELLOW)
    put(fx, fy + 1, YELLOW)
    put(fx + 1, fy + 1, LIGHT)

# 5) Sparse bare-dirt patches (small clusters, wrapped)
patches = [((1, 6), [(0,0),(1,0),(0,1)]),
           ((9, 13), [(0,0),(1,0),(2,0),(1,1)]),
           ((14, 1), [(0,0),(0,1),(1,1)])]
for (px, py), cells in patches:
    for i, (dx, dy) in enumerate(cells):
        put(px + dx, py + dy, DIRT_D if (i == 0) else DIRT)

print(c.stats_text())
print(c.matrix_text())

view(c, scale=24)
finish(c)
