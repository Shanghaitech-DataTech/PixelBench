from pixelbench_api import *

c = new_canvas(16, 16, background="#B0854E", name="wood_planks")

# palette
LIGHT   = c.color("#CFA268", "light")
MID     = c.color("#B0854E", "mid")
SHADOW  = c.color("#9A6F3E", "shadow")
GRAIN   = c.color("#8A6236", "grain")
SEAM    = c.color("#5A3D22", "seam")
DARKEND = c.color("#7A5630", "dark_end")
KNOT    = c.color("#6B4A28", "knot")

# ---- vertical seams (1px) every 4 px, tile seamlessly ----
for x in (0, 4, 8, 12):
    for y in range(16):
        c.set(x, y, SEAM)

# ---- boards: 3 px wide each, highlight / mid / shadow shading ----
boards = [(1, 3), (5, 7), (9, 11), (13, 15)]
for bx0, bx1 in boards:
    for y in range(16):
        c.set(bx0, y, LIGHT)
        c.set(bx0 + 1, y, MID)
        c.set(bx1, y, SHADOW)

# ---- horizontal butt joints, one per board at staggered heights ----
# light end above, dark end below (alternating look)
joints = {0: 5, 1: 11, 2: 3, 3: 9}
for i, (bx0, bx1) in enumerate(boards):
    jy = joints[i]
    for x in range(bx0, bx1 + 1):
        c.set(x, jy, SEAM)          # joint groove
        c.set(x, jy - 1, LIGHT)     # light board end
        c.set(x, jy + 1, DARKEND)   # dark board end

# ---- wood grain: short horizontal dashes ----
grain = [
    (1, 2, 2), (5, 1, 2), (9, 6, 2), (13, 4, 2),
    (2, 8, 2), (6, 7, 2), (10, 13, 2), (14, 12, 2),
    (1, 12, 1), (5, 14, 2), (9, 1, 1), (13, 6, 1),
    (2, 14, 1), (6, 3, 1), (10, 9, 1), (14, 1, 1),
]
for gx, gy, glen in grain:
    for k in range(glen):
        c.set(gx + k, gy, GRAIN)

# ---- knots ----
def knot(cx, cy):
    c.set(cx, cy, KNOT)
    c.set(cx + 1, cy, KNOT)
    c.set(cx, cy + 1, KNOT)
    c.set(cx + 1, cy + 1, GRAIN)
    c.set(cx - 1, cy, GRAIN)
    c.set(cx + 2, cy + 1, GRAIN)
    c.set(cx, cy - 1, GRAIN)
    c.set(cx + 1, cy + 2, GRAIN)

knot(2, 9)
knot(10, 6)

print(c.stats_text())
print(c.matrix_text())

result = c
finish(result)
