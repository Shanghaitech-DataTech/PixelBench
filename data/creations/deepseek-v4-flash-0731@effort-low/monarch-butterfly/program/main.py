from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

ink = c.color((12, 8, 12))        # black
org = c.color((235, 120, 20))     # monarch orange
wht = c.color((250, 240, 225))    # cream white spots

def run(x0, x1, colour, row):
    for x in range(x0, x1 + 1):
        c.set(x, row, colour)
        c.set(31 - x, row, colour)

# Left-wing + left-body cells, given as (start, end, colour). Body spans
# cols 14..15 (mirrored to 16..17). Wing drawn on the left of body.
left = {
    # antenna + head
    0:  [(13, 13, ink)],
    1:  [(12, 12, ink)],
    2:  [(12, 12, ink), (14, 15, ink)],
    3:  [(4, 5, ink), (14, 15, ink)],
    4:  [(4, 6, ink), (7, 7, wht), (14, 15, ink)],
    # upper wing
    5:  [(4, 5, ink), (6, 9, org), (10, 11, ink), (14, 15, ink)],
    6:  [(4, 6, ink), (7, 9, org), (10, 10, ink), (14, 15, ink)],
    7:  [(5, 5, ink), (6, 9, org), (10, 11, ink), (14, 15, ink)],
    8:  [(6, 6, ink), (7, 9, org), (10, 11, ink), (14, 15, ink)],
    9:  [(6, 7, ink), (8, 10, org), (11, 12, ink), (14, 15, ink)],
    10: [(7, 7, ink), (8, 10, org), (11, 12, ink), (14, 15, ink)],
    11: [(8, 8, ink), (9, 11, org), (12, 13, ink), (14, 15, ink)],
    12: [(9, 9, ink), (10, 11, org), (12, 13, ink), (14, 15, ink)],
    13: [(10, 11, ink), (12, 13, org), (14, 15, ink)],
    14: [(11, 11, ink), (12, 13, org), (14, 15, ink)],
    15: [(12, 13, ink), (14, 15, ink)],
    16: [(12, 13, ink), (14, 15, ink)],
    # lower wing
    17: [(13, 13, ink), (14, 15, ink)],
    18: [(11, 12, ink), (13, 14, org), (15, 15, ink)],
    19: [(10, 10, ink), (11, 13, org), (14, 15, ink)],
    20: [(8, 9, ink), (10, 13, org), (14, 15, ink)],
    21: [(7, 7, ink), (8, 12, org), (13, 14, ink), (15, 15, ink)],
    22: [(8, 9, ink), (10, 12, org), (13, 15, ink)],
    23: [(9, 10, ink), (11, 12, org), (13, 14, ink), (15, 15, ink)],
    24: [(10, 10, ink), (11, 12, org), (13, 15, ink)],
    25: [(11, 11, ink), (12, 13, org), (14, 15, ink)],
    26: [(12, 12, ink), (13, 14, org), (15, 15, ink)],
    27: [(13, 13, ink), (14, 15, ink)],
    28: [(14, 15, ink)],
}

for row, runs in left.items():
    for (a, b, ch) in runs:
        run(a, b, ch, row)

# White spots along black margins of both wings.
spots = {
    4:  [(7, 7)],
    5:  [(11, 11)],
    8:  [(11, 11)],
    12: [(12, 12)],
    14: [(12, 12)],
    20: [(14, 14)],
    22: [(13, 13)],
    23: [(10, 10)],
    25: [(13, 13)],
    27: [(13, 13)],
}
for row, cs in spots.items():
    for (a, b) in cs:
        for x in range(a, b + 1):
            c.set(x, row, wht)
            c.set(31 - x, row, wht)

# Black veins running outward through upper wing orange.
veins = {
    5:  (7, 7), 8: (8, 8),
    6:  (8, 8), 9: (8, 8),
    7:  (9, 9), 10:(9, 9),
    11: (10, 10), 12:(10,10),
    13: (12,12), 21:(10,10),
    24: (11,11),
}
for row in (5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26):
    if row in veins:
        a, b = veins[row]
        for x in range(a, b + 1):
            c.set(x, row, ink)
            c.set(31 - x, row, ink)

print(c.matrix_text())
finish(c)
