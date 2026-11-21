# 64x64 pixel art: family dining table, four chairs, bowl of fruit (front view)

LINE = "#3a2620"        # dark outline
WALL = "#f7e9cd"        # warm wall
TRIM = "#eed9b2"        # baseboard
FLOOR = "#e3c79b"       # wooden floor
FLOOR_LINE = "#cfae7e"  # plank lines
SHADOW = "#d6b78a"      # soft floor shadow

WOOD_LIGHT = "#dca76a"  # table top
WOOD_MID = "#b57a44"    # table front / legs
WOOD_DARK = "#8a5530"   # shading, slat gaps
GRAIN = "#c8935a"       # top grain

CHAIR = "#c98f55"
CHAIR_LIGHT = "#e0b078"

BOWL = "#f2ede2"
BOWL_SHADE = "#cfc7b8"
RED = "#d84a3a"; RED_L = "#f08a6a"
ORANGE = "#f2913c"; ORANGE_L = "#ffc07a"
GREEN = "#7fae4a"
PURPLE = "#8a4a9a"

c = new_canvas(64, 64, name="dining-table")


def orect(x, y, w, h, fill, line=LINE):
    """Filled rect with a 1px dark outline."""
    c.rect(x, y, w, h, line)
    if w > 2 and h > 2:
        c.rect(x + 1, y + 1, w - 2, h - 2, fill)


def chair_back(x, y, w, h):
    """Chair backrest seen from the front."""
    orect(x, y, w, h, CHAIR)
    c.rect(x + 1, y + 1, w - 2, 3, CHAIR_LIGHT)   # top rail
    c.rect(x + 2, y + 6, w - 4, 1, WOOD_DARK)     # slat gap
    c.rect(x + 2, y + 11, w - 4, 1, WOOD_DARK)    # slat gap


# ---------- room ----------
c.rect(0, 0, 64, 46, WALL)
c.rect(0, 42, 64, 4, TRIM)
c.rect(0, 46, 64, 18, FLOOR)
c.rect(0, 52, 64, 1, FLOOR_LINE)
c.rect(0, 59, 64, 1, FLOOR_LINE)
for x, y, h in [(18, 47, 5), (46, 47, 5), (10, 53, 6), (30, 53, 6), (54, 53, 6)]:
    c.rect(x, y, 1, h, FLOOR_LINE)

# soft shadow on the floor
c.ellipse(32, 55, 22, 3, SHADOW)

# ---------- framed pictures on the wall (cozy touch) ----------
for fx in (5, 50):
    orect(fx, 4, 9, 8, WOOD_MID)
    c.rect(fx + 1, 5, 7, 6, "#bcd9e8")          # sky
    c.rect(fx + 1, 8, 7, 3, "#8fae5e")          # hill
    c.set(fx + 2, 6, "#f7d154")                 # sun
    c.rect(fx + 1, 10, 7, 1, LINE)              # frame lip

# ---------- back chairs (behind the table) ----------
chair_back(14, 14, 10, 17)
chair_back(40, 14, 10, 17)

# ---------- table ----------
c.rect(9, 27, 46, 11, LINE)            # outline block
c.rect(10, 28, 44, 4, WOOD_LIGHT)      # top face
c.rect(10, 32, 44, 5, WOOD_MID)        # front edge
c.rect(13, 29, 12, 1, GRAIN)           # grain on top
c.rect(38, 30, 13, 1, GRAIN)
c.rect(12, 34, 17, 1, WOOD_DARK)       # grain on front
c.rect(36, 33, 14, 1, WOOD_DARK)
# legs
orect(12, 37, 4, 18, WOOD_MID)
c.rect(14, 38, 1, 16, WOOD_DARK)
orect(48, 37, 4, 18, WOOD_MID)
c.rect(50, 38, 1, 16, WOOD_DARK)

# ---------- front chairs (backs to the viewer) ----------
chair_back(17, 36, 12, 17)
chair_back(35, 36, 12, 17)
orect(18, 52, 3, 8, WOOD_MID)
orect(25, 52, 3, 8, WOOD_MID)
orect(36, 52, 3, 8, WOOD_MID)
orect(43, 52, 3, 8, WOOD_MID)

# ---------- bowl of fruit ----------
c.ellipse(31, 27, 9, 4, LINE)
c.ellipse(31, 27, 8, 3, BOWL)
c.rect(26, 29, 11, 1, BOWL_SHADE)

# green apple (back centre)
c.circle(31, 22, 2, LINE)
c.circle(31, 22, 1, GREEN)
c.set(31, 19, WOOD_DARK)
# red apple (left)
c.circle(27, 25, 3, LINE)
c.circle(27, 25, 2, RED)
c.set(26, 24, RED_L)
c.set(27, 21, WOOD_DARK)
# orange (right)
c.circle(35, 25, 3, LINE)
c.circle(35, 25, 2, ORANGE)
c.set(34, 24, ORANGE_L)
c.set(36, 21, GREEN)
# grapes in front
c.circle(24, 28, 1, LINE); c.set(24, 28, PURPLE)
c.circle(38, 28, 1, LINE); c.set(38, 28, PURPLE)

print(c.stats_text())
print(c.matrix_text(region=(8, 12, 56, 40)))
print(c.matrix_text(region=(8, 36, 56, 62)))
finish(c)
