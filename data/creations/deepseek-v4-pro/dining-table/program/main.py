from pixelbench_api import *

# 64x64 dining table sprite, top-down view, transparent background.
c = new_canvas(64, 64, background=None, name="dining_table")

# ---------- palette ----------
OUTLINE       = c.color("#1e1412", "outline")
TABLE         = c.color("#a4692f", "table")
TABLE_LIGHT   = c.color("#c8904c", "table_light")
TABLE_DARK    = c.color("#7a481f", "table_dark")
EDGE          = c.color("#5d3716", "edge")
CHAIR_WOOD    = c.color("#9a5e2a", "chair_wood")
CHAIR_DARK    = c.color("#6d421d", "chair_dark")
CUSHION       = c.color("#c9705a", "cushion")
CUSHION_DARK  = c.color("#9d4a37", "cushion_dark")
BOWL          = c.color("#e8d4b2", "bowl")
BOWL_DARK     = c.color("#b39466", "bowl_dark")
BOWL_INSIDE   = c.color("#7c4f2d", "bowl_inside")
HIGHLIGHT     = c.color("#fff1d0", "highlight")
APPLE         = c.color("#d43c32", "apple")
ORANGE        = c.color("#f2a43c", "orange")
LEMON         = c.color("#f0d23c", "lemon")
GREEN_APPLE   = c.color("#93c04a", "green_apple")
GRAPE         = c.color("#8f5fb0", "grape")


def outlined_rect(x, y, w, h, fill, outline=OUTLINE):
    """Draw a 1px-outlined filled rectangle. x,y,w,h describe the inner fill."""
    c.rect(x - 1, y - 1, w + 2, h + 2, outline, fill=True)
    c.rect(x, y, w, h, fill, fill=True)


def fruit(cx, cy, r, colour):
    c.circle(cx, cy, r, colour, fill=True)
    if r >= 2:
        c.set(cx - 1, cy - 1, HIGHLIGHT)
    else:
        c.set(cx, cy - 1, HIGHLIGHT)


# ---------- chairs (drawn first, they sit around the table) ----------
# top chair
outlined_rect(24, 5, 16, 3, CHAIR_WOOD)     # backrest
outlined_rect(24, 11, 16, 5, CUSHION)       # seat
c.set(27, 13, CUSHION_DARK); c.set(31, 13, CUSHION_DARK); c.set(35, 13, CUSHION_DARK)

# bottom chair
outlined_rect(24, 56, 16, 3, CHAIR_WOOD)    # backrest
outlined_rect(24, 48, 16, 5, CUSHION)       # seat
c.set(27, 50, CUSHION_DARK); c.set(31, 50, CUSHION_DARK); c.set(35, 50, CUSHION_DARK)

# left chair
outlined_rect(5, 24, 3, 16, CHAIR_WOOD)     # backrest
outlined_rect(11, 24, 5, 16, CUSHION)       # seat
c.set(13, 27, CUSHION_DARK); c.set(13, 31, CUSHION_DARK); c.set(13, 35, CUSHION_DARK)

# right chair
outlined_rect(56, 24, 3, 16, CHAIR_WOOD)    # backrest
outlined_rect(48, 24, 5, 16, CUSHION)       # seat
c.set(50, 27, CUSHION_DARK); c.set(50, 31, CUSHION_DARK); c.set(50, 35, CUSHION_DARK)

# ---------- table ----------
c.rect(16, 16, 32, 32, OUTLINE, fill=True)          # outer dark outline
c.rect(17, 17, 30, 30, TABLE, fill=True)            # wooden table edge/surface
c.rect(19, 19, 26, 26, TABLE_LIGHT, fill=True)      # lighter central panel

# wood grain: plank separation lines
c.line(19, 27, 44, 27, TABLE_DARK)
c.line(19, 37, 44, 37, TABLE_DARK)

# subtle vertical grain, broken by the plank lines
for x in (22, 28, 34, 40):
    c.line(x, 20, x, 26, TABLE_DARK)
    c.line(x, 28, x, 36, TABLE_DARK)
    c.line(x, 38, x, 43, TABLE_DARK)

# a few pale streaks for warmth
for y in (21, 31, 41):
    c.line(24, y, 26, y, HIGHLIGHT)

# ---------- bowl of fruit ----------
c.ellipse(31, 31, 10, 9, OUTLINE, fill=True)        # bowl outline
c.ellipse(31, 31, 9, 8, BOWL, fill=True)            # ceramic rim
c.ellipse(31, 31, 6, 5, BOWL_INSIDE, fill=True)     # dark interior

fruit(27, 29, 2, APPLE)
fruit(34, 28, 2, ORANGE)
fruit(28, 34, 2, LEMON)
fruit(35, 34, 2, GREEN_APPLE)

# small grape cluster tucked between the larger fruits
c.circle(30, 30, 1, GRAPE, fill=True)
c.circle(31, 31, 1, GRAPE, fill=True)
c.circle(30, 32, 1, GRAPE, fill=True)
c.set(30, 30, HIGHLIGHT)

# rim highlight to make the ceramic read as round and glossy
c.set(26, 24, HIGHLIGHT)
c.set(27, 23, HIGHLIGHT)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

finish(c)
