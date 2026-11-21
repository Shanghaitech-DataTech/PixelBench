from pixelbench_api import *

W, H = 32, 32
c = new_canvas(W, H, name="pear")

# Register the 7-colour palette.
OUT = c.color((30, 64, 34), name="outline")
BASE = c.color((98, 152, 60), name="base")
LIGHT = c.color((142, 192, 82), name="light")
HI = c.color((200, 226, 110), name="highlight")
SHADOW = c.color((54, 102, 44), name="shadow")
STEM = c.color((116, 82, 42), name="stem")
LEAF = c.color((70, 160, 76), name="leaf")

# Pear body silhouette as (y, x0, x1) inclusive.
body_rows = [
    (3, 14, 17),
    (4, 13, 18),
    (5, 12, 19),
    (6, 11, 20),
    (7, 10, 21),
    (8, 9, 22),
    (9, 8, 23),
    (10, 7, 24),
    (11, 7, 24),
    (12, 6, 25),
    (13, 6, 25),
    (14, 6, 25),
    (15, 6, 25),
    (16, 6, 26),
    (17, 5, 26),
    (18, 5, 26),
    (19, 5, 27),
    (20, 5, 27),
    (21, 4, 27),
    (22, 4, 27),
    (23, 4, 27),
    (24, 5, 27),
    (25, 5, 26),
    (26, 6, 26),
    (27, 7, 25),
    (28, 8, 24),
    (29, 9, 23),
]

# Fill the whole body with the base green.
body = set()
for y, x0, x1 in body_rows:
    for x in range(x0, x1 + 1):
        body.add((x, y))
        c.set(x, y, BASE)

# Turn every body pixel that touches transparency into the dark outline.
for (x, y) in body:
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in body:
            c.set(x, y, OUT)
            break

# Stem.
stem = set()
for y in range(0, 4):
    for x in (15, 16):
        stem.add((x, y))
        c.set(x, y, STEM)

# Small dark outline flanking the stem, where it meets transparency.
for y in range(0, 4):
    if (14, y) not in stem and (14, y) not in body:
        c.set(14, y, OUT)
    if (17, y) not in stem and (17, y) not in body:
        c.set(17, y, OUT)

# Leaf on the upper right of the stem.
leaf_rows = [
    (0, 20, 20),
    (1, 17, 20),
    (2, 16, 18),
]
leaf = set()
for y, x0, x1 in leaf_rows:
    for x in range(x0, x1 + 1):
        leaf.add((x, y))
        c.set(x, y, LEAF)

# Soft highlight on the upper-left of the fruit.
light_rows = [
    (6, 12, 15),
    (7, 11, 15),
    (8, 10, 16),
    (9, 10, 16),
    (10, 9, 16),
    (11, 9, 16),
    (12, 8, 16),
    (13, 8, 15),
    (14, 8, 15),
    (15, 8, 14),
    (16, 8, 14),
    (17, 7, 13),
]
for y, x0, x1 in light_rows:
    for x in range(x0, x1 + 1):
        c.set(x, y, LIGHT)

# Brighter highlight spot.
hi_rows = [
    (8, 11, 13),
    (9, 10, 12),
    (10, 10, 12),
    (11, 9, 12),
    (12, 9, 11),
    (13, 8, 11),
]
for y, x0, x1 in hi_rows:
    for x in range(x0, x1 + 1):
        c.set(x, y, HI)

# Shadow on the lower-right of the fruit.
shadow_rows = [
    (17, 20, 25),
    (18, 20, 25),
    (19, 21, 26),
    (20, 21, 26),
    (21, 20, 26),
    (22, 20, 26),
    (23, 20, 26),
    (24, 19, 26),
    (25, 19, 25),
    (26, 18, 25),
    (27, 17, 24),
    (28, 16, 23),
]
for y, x0, x1 in shadow_rows:
    for x in range(x0, x1 + 1):
        c.set(x, y, SHADOW)

# Centre the pear a little better vertically (one row of clear space above
# the leaf and one below the fruit).
c.shift(0, 1)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

finish(c)
