from pixelbench_api import *
import math

W = H = 64
c = new_canvas(W, H, background=(46, 66, 38))  # deep forest/mountain base

# ---- palette ----
BG_RIDGE   = (96, 70, 30)   # soil dike
GOLD      = [(246, 210, 96), (233, 187, 68), (216, 159, 47),
             (193, 133, 32), (170, 109, 24), (150, 92, 22),
             (128, 78, 20)]
FARM     = (42, 33, 28)
HAT      = (184, 150, 72)
WALL     = (216, 198, 168)
ROOF     = (168, 92, 46)
DOOR     = (90, 60, 30)
FTREE    = (58, 86, 46)
FTREE2   = (70, 100, 52)
LEAF     = (120, 118, 46)

# ---- contour generator: concentric irregular closed paths ----
def contour(cx, cy, base_r, seed, n=80):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        r = base_r * (1.0
                     + 0.22 * math.sin(a * 2 + seed)
                     + 0.10 * math.sin(a * 3 + seed * 1.31)
                     + 0.05 * math.sin(a * 5 + seed * 2.17)
                     + 0.03 * math.sin(a * 7 + seed * 0.71))
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts

# center of the terrace hill
CX, CY = 33, 36
radii = [25.5, 22.5, 19.6, 16.8, 14.0, 11.3, 8.8, 6.4, 4.2]

# build all polygons (outermost first)
polys = [contour(CX, CY, r, seed) for r, seed in
         zip(radii, [1.3, 2.2, 1.0, 2.9, 0.4, 1.8, 2.5, 0.9, 1.6])]

# layered values for depth: outer rings deeper/darker, inner brighter,
# with alternating warm variation so adjacent bands differ
ring_colors = [GOLD[5], GOLD[2], GOLD[6], GOLD[3], GOLD[0],
               GOLD[4], GOLD[1], GOLD[5], GOLD[2]]

# fill outermost first so successive inner fills create bands
for i, (p, col) in enumerate(zip(polys, ring_colors)):
    c.poly(p, col, fill=True)

# narrow soil dikes between terraces (draw each contour outline except maybe outmost)
for i in range(len(polys) - 1):
    c.poly(polys[i], BG_RIDGE, fill=False)

# water sheen / wet lower paddies: few thin highlight lines near center-less (skipped)
# subtle darker inner shadows along edges of a couple rings already via tones

# ---- distant forest fringe along top band and edges ----
for x in range(0, W):
    for y in range(0, 9):
        pass  # base forest remains; sprinkle trees below
import random
rnd = random.Random(7)
for _ in range(26):
    x = rnd.randint(0, W - 1)
    y = rnd.randint(0, 10)
    if c.get(x, y) is None:
        c.set(x, y, FTREE if (x + y) % 2 else FTREE2)
# ensure band solid textured
for y in range(0, 6):
    for x in range(0, W):
        if (x * 7 + y * 13) % 3 == 0:
            c.set(x, y, FTREE2)
        else:
            c.set(x, y, FTREE)

# ---- simple village houses in the distance (top band) ----
def house(x, y, wcol=WALL, rcol=ROOF):
    # walls
    c.rect(x, y + 2, 5, 3, wcol)
    # roof (gable, 2 px)
    c.rect(x, y, 5, 2, rcol)
    c.set(x + 1, y - 1, rcol)
    c.set(x + 3, y - 1, rcol)
    c.set(x + 2, y - 2, rcol)
    c.set(x + 2, y + 3, DOOR)
    c.set(x + 2, y + 4, DOOR)

house(8, 3)
house(17, 5)
house(26, 2)
house(35, 4)
house(44, 3)
house(52, 5)
# tiny trees between houses
for (tx, ty) in [(5, 6), (14, 8), (22, 7), (32, 7), (41, 6), (49, 8)]:
    c.set(tx, ty, FTREE2)

# ---- two farmers on narrow ridges ----
def farmer(x, y):
    # feet/legs on dike
    c.set(x, y, FARM)
    c.set(x + 1, y, FARM)
    # body
    c.set(x, y + 1, FARM)
    c.set(x + 1, y + 1, FARM)
    c.set(x, y + 2, FARM)
    c.set(x + 1, y + 2, FARM)
    # hat / shoulders
    c.set(x - 1, y, HAT)
    c.set(x + 2, y, HAT)
    c.set(x, y - 1, HAT)
    c.set(x + 1, y - 1, HAT)
    # shadow
    c.set(x + 3, y + 1, FARM)
    c.set(x, y + 3, FARM)

farmer(18, 48)   # on a mid-lower ridge
farmer(42, 27)   # on an upper ridge
# a couple of stacked rice sheaves near a farmer
for (sx, sy) in [(23, 50), (40, 31), (26, 49)]:
    c.set(sx, sy, GOLD[2])
    c.set(sx, sy + 1, GOLD[4])

# small leaf/dry-rice tufts scattered for texture
rnd2 = random.Random(3)
guard = {c.color((42, 33, 28)), c.color((184, 150, 72)), c.color((90, 60, 30)), c.color((46, 66, 38)), c.color((58, 86, 46)), c.color((70, 100, 52))}
for _ in range(140):
    x = rnd2.randint(4, W - 4)
    y = rnd2.randint(10, H - 1)
    idx = c.get(x, y)
    if idx is not None and idx not in guard:
        c.set(x, y, GOLD[rnd2.randint(1, 6)])

# shadow beneath the whole hill where it meets forest
for i in [0]:
    c.poly(contour(CX, CY, radii[0] + 1.5, 1.3), (40, 58, 34), fill=False)

print(c.stats_text())
finish(c)
