from pixelbench_api import *

c = new_canvas(16, 16, name="wood-planks")

# palette
LIGHT   = c.color("#C79A62", "wood_light")
MID     = c.color("#B0824A", "wood_mid")
DARK    = c.color("#8F6234", "wood_dark")
SEAM    = c.color("#4E3218", "seam")
KNOT    = c.color("#5F3E1F", "knot")
END_L   = c.color("#DDB377", "end_light")
END_D   = c.color("#6E4722", "end_dark")

# board face columns: 0-2, 4-6, 8-10, 12-14 ; seams at 3,7,11,15
boards = [(0,1,2), (4,5,6), (8,9,10), (12,13,14)]

# base fill: alternate boards light/mid tone
for bi, cols in enumerate(boards):
    base = MID if bi % 2 == 0 else LIGHT
    for x in cols:
        for y in range(16):
            c.set(x, y, base)

# seam grooves
for x in (3, 7, 11, 15):
    for y in range(16):
        c.set(x, y, SEAM)

# alternating board ends: top 2 rows + bottom row shaded
for bi, cols in enumerate(boards):
    endc = END_L if bi % 2 == 0 else END_D
    for x in cols:
        for y in (0, 1, 15):
            c.set(x, y, endc)

# wood grain lines (horizontal-ish wavy streaks)
grain = [
    (LIGHT, [(0,4),(1,4),(2,5)]),
    (DARK,  [(0,9),(1,9),(2,8)]),
    (DARK,  [(0,13),(1,12),(2,13)]),
    (LIGHT, [(4,6),(5,6),(6,7)]),
    (DARK,  [(4,11),(5,10),(6,11)]),
    (LIGHT, [(4,14),(5,14),(6,13)]),
    (DARK,  [(8,3),(9,4),(10,3)]),
    (LIGHT, [(8,8),(9,8),(10,9)]),
    (DARK,  [(8,12),(9,13),(10,12)]),
    (LIGHT, [(12,5),(13,5),(14,4)]),
    (DARK,  [(12,10),(13,9),(14,10)]),
    (LIGHT, [(12,14),(13,13),(14,14)]),
]
for col, pts in grain:
    for x, y in pts:
        c.set(x, y, col)

# wood knots: two small knots
# knot 1 in board 1 at (5,3)
k1 = [(5,3),(6,3),(4,4),(5,4),(6,4),(5,5)]
for x, y in k1:
    c.set(x, y, KNOT)
c.set(5, 4, END_D)
# knot 2 in board 3 at (13,7)
k2 = [(13,7),(12,8),(13,8),(14,8),(13,9)]
for x, y in k2:
    c.set(x, y, KNOT)
c.set(13, 8, END_D)

print(c.stats_text())
print(c.matrix_text())
save("wood-planks", c)
finish(c)
