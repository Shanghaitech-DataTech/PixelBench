from pixelbench_api import *

c = new_canvas(32, 32, name="slime")

C = {
    "K": "#1d4a2a",   # slime outline
    "M": "#55c26b",   # body green
    "H": "#9cea90",   # highlight
    "S": "#2f9a54",   # shadow
    "D": "#1e6b3d",   # deep shadow
    "m": "#5f8f3c",   # moss
    "t": "#84ab4e",   # moss light
    "a": "#d5a460",   # antler
    "c": "#f0d8a4",   # mushroom stem
    "r": "#e84d3c",   # mushroom cap red
    "d": "#a02d24",   # cap underside
    "s": "#fdf2da",   # mushroom spots
    "G": "#7fefff",   # eye glow
    "W": "#ffffff",
    "P": "#1d403a",   # pupil
    "u": "#ff9db8",   # blush
}

rows = {
    5:  [(14, 17, "r")],
    6:  [(13, 13, "r"), (14, 14, "s"), (15, 16, "r"), (17, 17, "s"), (18, 18, "r")],
    7:  [(13, 18, "r")],
    8:  [(13, 18, "d")],
    9:  [(15, 16, "c")],
    10: [(11, 14, "m"), (15, 16, "c"), (17, 20, "m")],
    11: [(9, 22, "m")],
    12: [(8, 8, "K"), (9, 22, "M"), (23, 23, "K")],
    13: [(7, 7, "K"), (8, 15, "H"), (16, 23, "M"), (24, 24, "K")],
    14: [(6, 6, "K"), (7, 14, "H"), (15, 24, "M"), (25, 25, "K")],
    15: [(6, 6, "K"), (7, 13, "H"), (14, 24, "M"), (25, 25, "K")],
    16: [(6, 6, "K"), (7, 12, "H"), (13, 24, "M"), (25, 25, "K")],
    17: [(6, 6, "K"), (7, 11, "H"), (12, 19, "M"), (20, 24, "S"), (25, 25, "K")],
    18: [(6, 6, "K"), (7, 10, "H"), (11, 18, "M"), (19, 24, "S"), (25, 25, "K")],
    19: [(6, 6, "K"), (7, 9, "H"), (10, 17, "M"), (18, 24, "S"), (25, 25, "K")],
    20: [(6, 6, "K"), (7, 8, "H"), (9, 16, "M"), (17, 24, "S"), (25, 25, "K")],
    21: [(6, 6, "K"), (7, 15, "M"), (16, 24, "S"), (25, 25, "K")],
    22: [(6, 6, "K"), (7, 14, "M"), (15, 24, "S"), (25, 25, "K")],
    23: [(7, 7, "K"), (8, 13, "M"), (14, 23, "S"), (24, 24, "K")],
    24: [(8, 8, "K"), (9, 15, "S"), (16, 22, "D"), (23, 23, "K")],
    25: [(10, 12, "K"), (15, 16, "K"), (19, 21, "K")],
}

for r, segs in rows.items():
    for (x0, x1, ch) in segs:
        for x in range(x0, x1 + 1):
            c.set(x, r, C[ch])

# tiny antlers (left + mirrored right)
for (x, y) in [(9, 5), (10, 6), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10),
              (22, 5), (21, 6), (20, 6), (20, 7), (20, 8), (20, 9), (20, 10)]:
    c.set(x, y, C["a"])

# moss light speckles on the moss band
for (x, y) in [(12, 10), (13, 10), (17, 10), (18, 10)]:
    c.set(x, y, C["t"])

# glowing eyes
for (ex, ey) in [(11, 13), (17, 13)]:
    pat = ["GGGG", "GWWG", "GPPG", "GGGG"]
    for ly, line in enumerate(pat):
        for lx, ch in enumerate(line):
            c.set(ex + lx, ey + ly, C[ch])

# blush cheeks
for (x, y) in [(10, 17), (11, 17), (10, 18), (11, 18),
              (20, 17), (21, 17), (20, 18), (21, 18)]:
    c.set(x, y, C["u"])

# small w-smile
for (x, y) in [(14, 19), (17, 19), (15, 20), (16, 20)]:
    c.set(x, y, C["K"])

print(c.stats_text())
print("bbox:", c.stats()["bbox"])
print(c.matrix_text())

finish(c)
