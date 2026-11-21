from pixelbench_api import *

c = new_canvas(128, 64, background=None, name="fruit_chart")

RED    = c.color("#d62828", "apple_red")
YELLOW = c.color("#f4c430", "banana_yellow")
ORANGE = c.color("#f77f00", "orange")
LEMON  = c.color("#f7e26b", "lemon")
PURPLE = c.color("#7b2d8b", "grape")
GREEN  = c.color("#2e7d32", "leaf")
BROWN  = c.color("#6d4c1b", "stem")
GRID   = c.color("#cccccc", "grid")
AXIS   = c.color("#444444", "axis")

data = [
    ("apple",  10, RED, """
.G.....
..RRR..
.RRRRR.
.RRRRR.
.RRRRR.
..RRR..
......."""),
    ("banana",  5, YELLOW, """
....YY.
..YYY..
YYY....
YY.....
.YYY...
...YYY.
......."""),
    ("orange",  7, ORANGE, """
...G...
.OOOOO.
OOOOOOO
OOOOOOO
OOOOOOO
.OOOOO.
......."""),
    ("lemon",  14, LEMON, """
.......
..YYY..
.YYYYY.
.YYYYY.
.YYYYY.
..YYY..
......."""),
    ("grape",   2, PURPLE, """
..P.P..
.PPPPP.
.PPPPP.
..PPP..
...S...
.......
......."""),
]

# gridlines every 5 units (35 px), chart area x 14..119
for u in range(5, 16, 5):
    x = 14 + u * 7
    for y in range(3, 55):
        c.set(x, y, GRID)
# axes
for y in range(2, 55):
    c.set(13, y, AXIS)
for x in range(13, 120):
    c.set(x, 54, AXIS)

y0 = 5
for name, val, col, icon in data:
    iy = y0 + 1
    ix = 4
    rows = icon.strip("\n").split("\n")
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch == ".":
                continue
            m = {"R": RED, "Y": YELLOW if name != "lemon" else LEMON,
                 "O": ORANGE, "P": PURPLE, "G": GREEN, "S": BROWN}
            c.set(ix + i, iy + j, m[ch])
    # bar
    w = val * 7
    c.rect(14, y0, w, 5, col)
    # darker bottom edge for depth
    dark = c.color({"apple": "#a31d1d", "banana": "#c99a1a", "orange": "#c25f00",
                    "lemon": "#d4bc42", "grape": "#5a1f66"}[name])
    c.line(14, y0 + 4, 13 + w, y0 + 4, dark)
    # highlight pixel
    c.set(15, y0 + 1, "#ffffff")
    y0 += 10

print(c.stats_text())
result = c
finish(result)
