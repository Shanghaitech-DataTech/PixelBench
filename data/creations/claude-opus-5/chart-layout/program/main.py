# fruit bar chart, 128x64

BG   = "#1b1d30"
GRID = "#2e3150"
AXIS = "#5a6090"
GRN  = "#4fae3e"
GRN2 = "#2f7a28"
STEM = "#7a4f2a"

c = new_canvas(128, 64, background=BG, name="output")

# ---------------------------------------------------------------- data
# (label, value, base, light, dark)
DATA = [
    ("apple",  10, "#d8343c", "#f06a66", "#93202a"),
    ("banana",  5, "#f2c94c", "#ffe389", "#b78a22"),
    ("orange",  7, "#f08a2a", "#ffb45e", "#a85713"),
    ("lemon",  14, "#e8e24a", "#f7f58e", "#a39c22"),
    ("grape",   2, "#8a5ad6", "#b68cf0", "#5a2f96"),
]

X0 = 14          # bar origin
UNIT = 7         # pixels per unit
AX = 12          # vertical axis column
AY = 59          # bottom axis row

# ---------------------------------------------------------------- icons
APPLE = [
    "....B.G...",
    "...R.GG...",
    "..RRRRRR..",
    ".RHRRRRRR.",
    ".RHRRRRRR.",
    ".RRRRRRRR.",
    ".RRRRRRRR.",
    "..RRRRRR..",
    "...RR.RR..",
    "..........",
]
BANANA = [
    "..........",
    ".D........",
    ".YY.......",
    ".LYY......",
    "..LYY.....",
    "..LYYY....",
    "...LYYYY..",
    "....LYYYYD",
    "......LLL.",
    "..........",
]
ORANGE = [
    "....GG....",
    "...OOOO...",
    "..OHOOOO..",
    ".OHOOOODO.",
    ".OOOOOOOO.",
    ".OOOODOOO.",
    ".OOOOOOOO.",
    "..OOOOOO..",
    "...OOOO...",
    "..........",
]
LEMON = [
    "..........",
    ".....GG...",
    "...HHHG...",
    "..HHYYYY..",
    ".DYYYYYYY.",
    ".DYYYYYYYD",
    "..YYYYYYD.",
    "...YYYY...",
    "..........",
    "..........",
]
GRAPE = [
    "......G...",
    "...GGP....",
    "..PHPPP...",
    ".PHPPPPP..",
    "..PPPPPP..",
    "...PPPPP..",
    "....PPP...",
    ".....P....",
    "..........",
    "..........",
]


def draw_icon(canvas, ox, oy, rows, cmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch != ".":
                canvas.set(ox + i, oy + j, cmap[ch])


def icon_for(name, base, light, dark):
    if name == "apple":
        return APPLE, {"R": base, "H": light, "D": dark, "G": GRN, "B": STEM}
    if name == "banana":
        return BANANA, {"Y": base, "L": light, "D": dark}
    if name == "orange":
        return ORANGE, {"O": base, "H": light, "D": dark, "G": GRN}
    if name == "lemon":
        return LEMON, {"Y": base, "H": light, "D": dark, "G": GRN2}
    return GRAPE, {"P": base, "H": light, "D": dark, "G": GRN2}


# ---------------------------------------------------------------- grid
for gx in (X0 + 5 * UNIT - 1, X0 + 10 * UNIT - 1, X0 + 15 * UNIT - 1):
    for gy in range(2, AY, 2):
        c.set(gx, gy, GRID)

# axes
c.line(AX, 2, AX, AY, AXIS)
c.line(AX, AY, 120, AY, AXIS)
for tx in (X0, X0 + 5 * UNIT - 1, X0 + 10 * UNIT - 1, X0 + 15 * UNIT - 1):
    c.set(tx, AY + 1, AXIS)

# ---------------------------------------------------------------- rows
for i, (name, value, base, light, dark) in enumerate(DATA):
    y = 4 + i * 11
    length = value * UNIT
    c.rect(X0, y, length, 8, base)
    c.line(X0, y, X0 + length - 1, y, light)
    c.line(X0, y + 7, X0 + length - 1, y + 7, dark)
    c.line(X0 + length - 1, y + 1, X0 + length - 1, y + 7, dark)
    rows, cmap = icon_for(name, base, light, dark)
    draw_icon(c, 1, y - 1, rows, cmap)

view(c)
save("fruit_chart", c)
finish(c)
