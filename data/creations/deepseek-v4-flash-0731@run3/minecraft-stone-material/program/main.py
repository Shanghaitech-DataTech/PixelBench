from pixelbench_api import new_canvas, finish
import random

S = 16
rng = random.Random(20240607)

# ---- Periodic value noise (period 16) for stone grain ----
cells = 4
cell = S // cells
corners = {}
for cy in range(cells):
    for cx in range(cells):
        corners[(cx, cy)] = rng.random()

def smooth(t):
    return t * t * (3 - 2 * t)

def noise(x, y):
    fx = x / cell
    fy = y / cell
    i = int(fx)
    j = int(fy)
    tx = smooth(fx - i)
    ty = smooth(fy - j)
    i0 = i % cells
    i1 = (i + 1) % cells
    j0 = j % cells
    j1 = (j + 1) % cells
    a = corners[(i0, j0)] * (1 - tx) + corners[(i1, j0)] * tx
    b = corners[(i0, j1)] * (1 - tx) + corners[(i1, j1)] * tx
    return a * (1 - ty) + b * ty

base    = (122, 122, 122)
dark1   = (104, 104, 104)
dark2   = ( 88,  88,  88)
light1  = (138, 138, 138)
light2  = (153, 153, 153)
edge    = ( 62,  62,  62)   # crack shadow edge
crack   = ( 36,  36,  36)   # crack fissure

tile = new_canvas(S, S, name="tile")
for y in range(S):
    for x in range(S):
        n = noise(x, y)
        if n < 0.22:
            col = dark2
        elif n < 0.40:
            col = dark1
        elif n < 0.62:
            col = base
        elif n < 0.82:
            col = light1
        else:
            col = light2
        tile.set(x, y, col)

# ---- 3x3 tiled overlay so cracks can wrap across edges ----
ov = new_canvas(S * 3, S * 3, name="ov")
for ty in range(3):
    for tx in range(3):
        ov.blit(tile, tx * S, ty * S)

# Cracks spanning tile boundaries (coordinates relative to one tile, offset by 16)
cracks = [
    [(-3, 4), (1, 2), (4, 5), (8, 2), (12, 5), (16, 3), (19, 5)],
    [(6, -3), (5, 1), (7, 5), (6, 9), (8, 13), (6, 17), (7, 20)],
    [(-2, 13), (2, 11), (5, 14), (9, 12), (13, 15), (17, 13), (19, 14)],
]
branches = [
    [(6, 3), (9, 1), (11, 2)],
    [(7, 13), (10, 11), (12, 12)],
]
for pts in cracks + branches:
    off = [(x + 16, y + 16) for (x, y) in pts]
    for i in range(len(off) - 1):
        ov.line(off[i][0], off[i][1], off[i + 1][0], off[i + 1][1], edge)
    for i in range(len(off) - 1):
        ov.line(off[i][0], off[i][1], off[i + 1][0], off[i + 1][1], crack)

# A couple of fuzzy dark speckle dots for grit
speck = (80, 80, 80)
rng3 = random.Random(99)
for _ in range(14):
    x = 16 + rng3.randrange(16)
    y = 16 + rng3.randrange(16)
    ov.set(x, y, speck)

result = new_canvas(S, S, name="result")
ov.select(16, 16, 16, 16).copy_to(0, 0, result, mode="replace")

print(result.stats_text())
finish(result)
