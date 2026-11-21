from pixelbench_api import *

# Palette (bamboo steamer)
inner        = (122, 74, 30)     # dark interior of basket
wall         = (200, 138, 61)    # bamboo body
wall_light   = (226, 170, 96)    # rim highlight
wall_dark    = (140, 88, 36)     # slats / shadow
lid          = (216, 160, 88)    # lid top
lid_dark     = (158, 104, 44)    # lid underside / edge
dumpling     = (246, 236, 216)   # cream dumpling
dumpling_shade = (214, 190, 148) # dumpling shadow/outline
dumpling_hi  = (255, 251, 242)   # dumpling highlight
steam        = (255, 255, 255, 170)  # soft white steam

c = new_canvas(32, 32, background=None, name="steamer")

# --- basket interior (opening we look into) ---
c.ellipse(16, 14, 9, 4, inner, fill=True)

# --- three dumplings inside, in a clear triangle ---
def draw_dumpling(cx, cy):
    c.circle(cx, cy, 2, dumpling, fill=True)
    c.circle(cx, cy, 2, dumpling_shade, fill=False)
    c.set(cx - 1, cy - 1, dumpling_hi)       # small top highlight
    c.set(cx + 1, cy + 1, dumpling_shade)    # small lower shade

draw_dumpling(10, 13)
draw_dumpling(20, 15)
draw_dumpling(14, 16)

# --- bamboo front wall of the basket ---
# Top edge is the front (lower) half of the opening ellipse;
# bottom edge is the front (lower) half of the bottom ellipse.
c.path("M 7 14 A 9 4 0 0 0 25 14 L 25 26 A 9 3 0 0 1 7 26 Z", wall, fill=True)

# --- rim of the opening ---
c.ellipse(16, 14, 9, 4, wall_light, fill=False)

# --- bamboo slats on the front wall ---
for x in (9, 12, 15, 18, 21, 24):
    c.line(x, 18, x, 27, wall_dark)

# --- horizontal binding band ---
c.line(7, 21, 25, 21, wall_dark)

# --- partially open lid (tilted toward the upper right) ---
c.ellipse(20, 10, 7, 3, lid_dark, fill=True)  # underside / edge
c.ellipse(20, 8, 7, 3, lid, fill=True)        # top surface
c.circle(20, 5, 1, lid_dark, fill=True)       # knob

# --- small rising steam wisps ---
for x, y in [(10, 8), (11, 8), (10, 7), (9, 6), (9, 5), (10, 4), (10, 3), (9, 2),
             (13, 7), (14, 6), (14, 5), (13, 4), (13, 3), (12, 2)]:
    c.set(x, y, steam)

finish(c)
