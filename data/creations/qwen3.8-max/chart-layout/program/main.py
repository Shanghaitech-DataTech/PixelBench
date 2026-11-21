# Fruit bar chart, 128x64, mini pixel-art fruit icons instead of text labels.

W, H = 128, 64

# --- palette -------------------------------------------------------------
BG     = "#1b1e2b"
PANEL  = "#232839"
GRID   = "#313752"
AXIS   = "#616a90"

# fruit: (light, main, dark)
APPLE  = ("#f2837a", "#d33b32", "#87202a")
BANANA = ("#fbe79a", "#eec93c", "#b0821c")
ORANGE = ("#f9b76a", "#ef8a2b", "#ab5215")
LEMON  = ("#f7f2a6", "#e0d13c", "#9d9021")
GRAPE  = ("#bd93e8", "#8b52c9", "#552c86")

STEM   = "#7c4a26"
LEAF   = "#54ab3f"
LEAFD  = "#2f7227"
TIP    = "#8a6a2a"

# --- geometry ------------------------------------------------------------
BASE    = 46      # baseline row (bars sit on top of it)
SCALE   = 3       # pixels per unit
AXIS_X  = 15
PLOT_X0 = 16
PLOT_X1 = 124
BW      = 13      # bar width
XS      = [20, 42, 64, 86, 108]
ICON_Y  = 50

DATA = [
    ("apple",  10, APPLE),
    ("banana",  5, BANANA),
    ("orange",  7, ORANGE),
    ("lemon",  14, LEMON),
    ("grape",   2, GRAPE),
]

# --- icon bitmaps (11x11, '.' = transparent) -----------------------------
APPLE_ROWS = [
    ".....s.....",
    ".lll.s.....",
    ".lLl.s.....",
    "...aaaaa...",
    "..aaaaaaa..",
    ".aawaaaaaA.",
    ".awaaaaaaA.",
    ".aaaaaaaAA.",
    "..aaaaaaA..",
    "...aaaaA...",
    "...AAAAA...",
]

BANANA_ROWS = [
    "...........",
    "...........",
    "t.........t",
    "b.........b",
    "wb.......bB",
    ".wb.....bB.",
    "..wbbbbbB..",
    "..bbbbbbb..",
    "...bbbbb...",
    "....BBB....",
    "...........",
    "...........",
]

ORANGE_ROWS = [
    ".....s.....",
    "..lLls.....",
    "...ooooo...",
    "..ooooooo..",
    ".owwoooooO.",
    ".owoooooOO.",
    ".ooooooOOO.",
    "..ooooOOO..",
    "...ooOOO...",
    "....OOO....",
    "...........",
]

LEMON_ROWS = [
    "...........",
    "...........",
    ".....g.....",
    "...yyyyy...",
    "..ywyyyyY..",
    "TyyyyyyyyyT",
    "..yyyyyYY..",
    "...YYYYY...",
    "...........",
    "...........",
    "...........",
]

GRAPE_ROWS = [
    ".....s.....",
    "..llls.....",
    "..lLls.....",
    ".ppppppppp.",
    ".ppppppppp.",
    ".ppppppppp.",
    "...pppppp..",
    "...pppppp..",
    "...pppppp..",
    "....ppp....",
    "....ppp....",
]


def icon(c, ox, oy, rows, keymap, dy=0, dots=()):
    for j, row in enumerate(rows):
        assert len(row) == 11, (j, row, len(row))
        for i, ch in enumerate(row):
            if ch == ".":
                continue
            c.set(ox + i, oy + dy + j, keymap[ch])
    for (dx, dy2, col) in dots:
        c.set(ox + dx, oy + dy + dy2, col)


c = new_canvas(W, H, background=BG, name="fruit_chart")

# plot panel
c.rect(PLOT_X0, 3, PLOT_X1 - PLOT_X0 + 1, BASE - 3, PANEL)

# gridlines + axis ticks (every 2 units)
for u in range(2, 15, 2):
    y = BASE - SCALE * u
    c.line(PLOT_X0, y, PLOT_X1, y, GRID)
    c.line(AXIS_X - 2, y, AXIS_X - 1, y, AXIS)

# axes
c.line(AXIS_X, 2, AXIS_X, BASE, AXIS)
c.line(AXIS_X, BASE, PLOT_X1 + 1, BASE, AXIS)
c.line(AXIS_X - 2, BASE, AXIS_X - 1, BASE, AXIS)

# bars
for (name, v, pal), x0 in zip(DATA, XS):
    light, main, dark = pal
    h = SCALE * v
    ytop = BASE - h
    c.rect(x0, ytop, BW, h, main)
    c.line(x0, ytop, x0 + BW - 1, ytop, light)
    c.line(x0, ytop, x0, BASE - 1, light)
    c.line(x0 + BW - 1, ytop + 1, x0 + BW - 1, BASE - 1, dark)
    c.line(x0 + 1, BASE - 1, x0 + BW - 1, BASE - 1, dark)
    if h >= 12:
        c.line(x0 + 3, ytop + 3, x0 + 3, BASE - 3, light)

# fruit icons in place of text labels
for (name, v, pal), x0 in zip(DATA, XS):
    light, main, dark = pal
    ox = x0 + 1
    if name == "apple":
        icon(c, ox, ICON_Y, APPLE_ROWS,
             {"s": STEM, "l": LEAF, "L": LEAFD, "a": main, "w": light, "A": dark})
    elif name == "banana":
        icon(c, ox, ICON_Y, BANANA_ROWS,
             {"t": TIP, "b": main, "w": light, "B": dark}, dy=1)
    elif name == "orange":
        icon(c, ox, ICON_Y, ORANGE_ROWS,
             {"s": STEM, "l": LEAF, "L": LEAFD, "o": main, "w": light, "O": dark},
             dots=[(6, 3, dark), (3, 6, dark), (6, 7, main)])
    elif name == "lemon":
        icon(c, ox, ICON_Y, LEMON_ROWS,
             {"g": LEAF, "y": main, "w": light, "Y": dark, "T": TIP}, dy=1)
    elif name == "grape":
        icon(c, ox, ICON_Y, GRAPE_ROWS,
             {"s": STEM, "l": LEAF, "L": LEAFD, "p": main},
             dots=[(1, 3, light), (4, 3, light), (7, 3, light),
                   (3, 4, dark), (6, 4, dark), (9, 4, dark),
                   (3, 5, dark), (6, 5, dark), (9, 5, dark),
                   (3, 6, light), (6, 6, light),
                   (5, 8, dark), (8, 8, dark),
                   (4, 9, light), (6, 10, dark)])

print(c.stats_text())
view(c, scale=6, margin=0)
save("fruit_chart", c, indexed=True)
finish(c)
