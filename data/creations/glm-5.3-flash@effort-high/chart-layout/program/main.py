from pixelbench_api import *

c = new_canvas(128, 64, background=None, name="fruit_chart")

# ---- palette ----
RED    = c.color("#d9302f", "apple_red")
RED_D  = c.color("#a01f1f", "apple_dark")
YEL    = c.color("#f2c14e", "banana")
YEL_D  = c.color("#c9962f", "banana_dark")
ORG    = c.color("#f2760a", "orange")
ORG_D  = c.color("#bf5606", "orange_dark")
LEM    = c.color("#efe95c", "lemon")
LEM_D  = c.color("#c2bb33", "lemon_dark")
GRP    = c.color("#8e44ad", "grape")
GRP_D  = c.color("#6a2f85", "grape_dark")
LEAF   = c.color("#3f9b3f", "leaf")
STEM   = c.color("#7a4a21", "stem")
WHITE  = c.color("#ffffff", "shine")
GRID   = c.color("#3a3a44", "grid")
AXIS   = c.color("#8a8a95", "axis")

# ---- data (order as given) ----
fruits = [
    ("apple",  10, RED,   RED_D),
    ("banana",  5, YEL,   YEL_D),
    ("orange",  7, ORG,   ORG_D),
    ("lemon",  14, LEM,   LEM_D),
    ("grape",   2, GRP,   GRP_D),
]

X0 = 15          # bars start here (axis at x=13)
SCALE = 7        # pixels per unit

# ---- gridlines every 2 units, axis ----
for k in range(1, 8):
    gx = X0 + 14 * k
    for y in range(4, 59):
        c.set(gx, y, GRID)
for y in range(3, 60):
    c.set(13, y, AXIS)
    c.set(14, y, AXIS)
# axis ticks
for k in range(1, 8):
    gx = X0 + 14 * k
    c.set(gx, 59, AXIS)
    c.set(gx, 60, AXIS)

# ---- mini pixel icons (9x9), '.' = transparent ----
ICONS = {
"apple": [
"....t....",
"...t.l...",
"..RRRRR..",
".RWRRRRR.",
".RWRRRRR.",
".RRRRRRR.",
".RRRRRRR.",
"..RRRRR..",
".........",
],
"banana": [
".........",
".....YYY.",
"....YYY..",
"...YYY...",
"..YYY....",
".YYY.....",
"YYY......",
"YY.......",
".........",
],
"orange": [
"....l....",
"..OOOOO..",
".OOOOOOO.",
".OOWOOOO.",
".OOWOOOO.",
".OOOOOOO.",
".OOOOOOO.",
"..OOOOO..",
".........",
],
"lemon": [
".........",
".........",
"..LLLLL..",
".LLLLLLLL",
"LWLLLLLLL",
".LLLLLLLL",
"..LLLLL..",
".........",
".........",
],
"grape": [
"....t....",
"..G.G.G..",
".GGGGGGG.",
".GGGGGGG.",
"..GGGGG..",
"...GGG...",
"....G....",
".........",
".........",
],
}

CHARMAP = {
    "R": RED, "O": ORG, "Y": YEL, "L": LEM, "G": GRP,
    "l": LEAF, "t": STEM, "W": WHITE,
}

def draw_icon(name, ox, oy):
    grid = ICONS[name]
    for j, row in enumerate(grid):
        for i, ch in enumerate(row):
            if ch != ".":
                c.set(ox + i, oy + j, CHARMAP[ch])

# ---- bars + icons ----
for idx, (name, val, col, dark) in enumerate(fruits):
    ytop = 6 + idx * 11
    w = val * SCALE
    # bar body with darker bottom edge for depth
    c.rect(X0, ytop, w, 6, col)
    c.rect(X0, ytop + 5, w, 1, dark)
    c.rect(X0, ytop, 1, 6, dark)
    # small cap pixel at the end
    c.set(X0 + w, ytop, col)
    c.set(X0 + w, ytop + 1, col)
    # icon beside the bar
    draw_icon(name, 2, ytop - 1)

print(c.stats_text())
save("fruit_chart", c)
finish(c)
