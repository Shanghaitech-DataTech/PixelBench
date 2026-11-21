from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="tavern")

OUTLINE = "#150d08"
CEIL = "#1d1108"
BEAM = "#2a1a0d"
WALL = "#3a2513"
WALL_D = "#2c1b0d"
SHELF = "#5d3a1d"
SHELF_L = "#6e4420"
WOOD = "#70411f"
WOOD_L = "#8a552a"
WOOD_D = "#4f2d13"
FLOOR = "#221309"
FLOOR_D = "#190d05"
LAMP_D = "#332414"
LAMP_G = "#ffd863"
HALO = "#7d5c1e"
CAP = "#3b2715"
CORK = "#a8783f"
GLASS = "#c2cfca"
GLASS_L = "#e8f0ea"
SMOKE = "#7d6a58"
SMOKE_L = "#94806c"
BARREL = "#7c4821"
BARREL_L = "#9a5c2a"
BARREL_D = "#5c3315"
BAND = "#26201a"
TOP = "#7a4520"
TOP_L = "#9a6129"
LEG = "#221109"


def bottle(cx, base, h, col, colL, neck=2, cap=CAP):
    # body
    c.rect(cx - 2, base - h, 5, h, OUTLINE)
    c.rect(cx - 1, base - h, 3, h, col)
    c.rect(cx - 1, base - h, 1, h, colL)
    # neck
    c.rect(cx - 1, base - h - neck, 3, neck, OUTLINE)
    c.rect(cx, base - h - neck + 1, 1, neck - 1, col)
    # cap
    c.rect(cx - 2, base - h - neck - 2, 5, 1, OUTLINE)
    c.rect(cx - 1, base - h - neck - 1, 3, 1, cap)


def lamp(cx):
    c.circle(cx, 13, 4, HALO)
    c.circle(cx, 13, 2, LAMP_G)
    c.rect(cx, 2, 1, 6, OUTLINE)
    c.poly([(cx - 3, 10), (cx + 3, 10), (cx + 2, 16), (cx - 2, 16)], OUTLINE)
    c.poly([(cx - 2, 11), (cx + 2, 11), (cx + 1, 15), (cx - 1, 15)], LAMP_D)


def barrel(x, y):
    c.rect(x, y, 10, 12, OUTLINE)
    c.rect(x + 1, y + 1, 8, 10, BARREL)
    c.rect(x + 1, y + 1, 1, 10, BARREL_L)
    c.rect(x + 2, y + 2, 6, 1, BARREL_D)
    c.rect(x + 1, y + 4, 8, 1, BAND)
    c.rect(x + 1, y + 8, 8, 1, BAND)
    c.rect(x + 7, y + 5, 1, 5, BARREL_D)


def stool(cx):
    c.rect(cx - 4, 48, 8, 3, OUTLINE)
    c.rect(cx - 3, 49, 6, 2, TOP)
    c.rect(cx - 3, 49, 6, 1, TOP_L)
    c.rect(cx - 2, 51, 1, 7, OUTLINE)
    c.rect(cx + 1, 51, 1, 7, OUTLINE)
    c.rect(cx - 2, 52, 1, 6, LEG)
    c.rect(cx + 1, 52, 1, 6, LEG)
    c.rect(cx - 2, 57, 5, 1, OUTLINE)
    c.rect(cx - 1, 58, 4, 1, LEG)


# --- background wall + ceiling
c.rect(0, 0, W, H, WALL)
c.rect(0, 0, W, 8, CEIL)
c.rect(0, 5, W, 1, BEAM)
for x in range(6, W, 9):
    c.rect(x, 8, 1, 28, WALL_D)

# --- smoky atmosphere wisps (upper area)
c.circle(6, 15, 2, SMOKE)
c.circle(13, 20, 3, SMOKE)
c.circle(24, 14, 2, SMOKE_L)
c.circle(38, 19, 2, SMOKE)
c.circle(44, 13, 2, SMOKE_L)
c.circle(56, 17, 3, SMOKE)
c.circle(60, 12, 2, SMOKE)

# --- hanging lamps
lamp(17)
lamp(47)

# --- shelf of bottles
c.rect(4, 25, 56, 3, OUTLINE)
c.rect(5, 26, 54, 1, SHELF_L)
c.rect(5, 27, 54, 1, SHELF)

bottle(7,  26, 5, "#4a3018", "#6a4a30", cap=CORK)
bottle(13, 26, 7, "#41722f", "#5f9b4a")
bottle(19, 26, 6, "#8e2f22", "#b34a38")
bottle(25, 26, 5, "#b8c8c8", "#e6ece8")
bottle(31, 26, 7, "#45658a", "#5f86b0")
bottle(37, 26, 6, "#b57128", "#d89a3e")
bottle(43, 26, 5, "#9a4654", "#c06a78")
bottle(49, 26, 7, "#2e5226", "#3f6b33")
bottle(55, 26, 6, "#b8c8c8", "#e6ece8", cap=CORK)

# --- wooden bar counter
c.rect(4, 36, 56, 5, OUTLINE)
c.rect(5, 37, 54, 3, WOOD)
c.rect(5, 37, 54, 1, WOOD_L)
for x in range(11, 59, 9):
    c.rect(x, 37, 1, 3, WOOD_D)
c.rect(14, 37, 6, 3, HALO)
c.rect(44, 37, 6, 3, HALO)
c.rect(4, 41, 56, 7, OUTLINE)
for i in range(6):
    c.rect(5 + i * 9, 42, 9, 5, WOOD if i % 2 == 0 else WOOD_D)
for x in range(14, 56, 9):
    c.rect(x, 42, 1, 5, OUTLINE)

# --- glasses and a mug on the counter
c.rect(22, 35, 4, 5, OUTLINE)
c.rect(23, 36, 2, 3, GLASS)
c.set(23, 36, GLASS_L)
c.rect(29, 35, 4, 5, OUTLINE)
c.rect(30, 36, 2, 3, GLASS)
c.set(30, 36, GLASS_L)
c.rect(34, 36, 5, 4, OUTLINE)
c.rect(35, 37, 3, 3, WOOD)
c.set(35, 37, WOOD_L)

# --- floor, warm pools, barrels, stools
c.rect(0, 48, 64, 16, FLOOR)
for y in (51, 55, 59):
    c.rect(0, y, 64, 1, FLOOR_D)
for x in (10, 30, 50):
    c.rect(x, 52, 1, 11, FLOOR_D)
c.ellipse(17, 52, 5, 2, HALO)
c.ellipse(32, 52, 5, 2, HALO)
c.ellipse(46, 52, 5, 2, HALO)

barrel(5, 49)
barrel(51, 49)

stool(17)
stool(32)
stool(46)

# --- vignette (cozy darkness at edges)
c.rect(0, 8, 2, 27, WALL_D)
c.rect(62, 8, 2, 27, WALL_D)
c.rect(0, 28, 4, 8, WALL_D)
c.rect(60, 28, 4, 8, WALL_D)

print(c.stats_text())
print("--- LOWER ---")
print(c.matrix_text(region=(2, 46, 61, 63)))

finish(c)
