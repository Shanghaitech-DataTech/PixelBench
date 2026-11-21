from pixelbench_api import new_canvas, finish

# Create 32x32 canvas for the ancient golden compass icon
c = new_canvas(32, 32, background=None, name="compass")

# Color palette - staying well under 86 colors
# Ancient gold tones (5 colors)
gold1 = c.color((160, 100, 30), "gold1")      # Dark gold shadow
gold2 = c.color((200, 140, 40), "gold2")      # Medium gold
gold3 = c.color((230, 180, 60), "gold3")      # Main gold
gold4 = c.color((250, 210, 100), "gold4")     # Light gold highlight
gold5 = c.color((255, 235, 150), "gold5")     # Bright highlight

# Blue crystal (4 colors)
blue1 = c.color((30, 80, 150), "blue1")       # Dark blue shadow
blue2 = c.color((60, 130, 200), "blue2")      # Medium blue
blue3 = c.color((120, 180, 240), "blue3")     # Light blue
blue4 = c.color((200, 230, 255), "blue4")     # Crystal highlight

# Outline
outline = c.color((25, 20, 15), "outline")    # Dark brown-black

cx, cy = 16, 16

# === OUTER GOLD RING ===
# Draw the main ring body (outer radius 12, inner radius 8)
c.circle(cx, cy, 12, gold3, fill=True)
c.circle(cx, cy, 8, None, fill=True)  # Cut out center

# Ring shading - outer edge lighter, inner edge darker
c.circle(cx, cy, 12, gold4, fill=False)  # Outer highlight
c.circle(cx, cy, 8, gold1, fill=False)   # Inner shadow

# === CARDINAL POINT MARKERS ===
# North marker (top) - prominent triangle pointing up
c.poly([(16, 2), (13, 8), (19, 8)], gold4, fill=True)
c.poly([(16, 3), (14, 7), (18, 7)], gold5, fill=True)

# South marker (bottom) - smaller triangle pointing down
c.poly([(16, 30), (14, 24), (18, 24)], gold2, fill=True)
c.poly([(16, 29), (15, 25), (17, 25)], gold1, fill=True)

# East marker (right) - triangle pointing right
c.poly([(30, 16), (24, 13), (24, 19)], gold3, fill=True)
c.poly([(29, 16), (25, 14), (25, 18)], gold4, fill=True)

# West marker (left) - triangle pointing left
c.poly([(2, 16), (8, 13), (8, 19)], gold2, fill=True)
c.poly([(3, 16), (7, 14), (7, 18)], gold1, fill=True)

# === DECORATIVE DOTS ON RING ===
# 8 small dots around the ring at radius 10
dots_positions = [
    (16, 6),   # N
    (22, 9),   # NE
    (26, 16),  # E
    (22, 23),  # SE
    (16, 26),  # S
    (10, 23),  # SW
    (6, 16),   # W
    (10, 9),   # NW
]
for dx, dy in dots_positions:
    c.set(dx, dy, gold5)

# === INNER DECORATIVE RING ===
# Small tick marks at 8 positions inside the ring
ticks = [
    (16, 9), (19, 11), (21, 16), (19, 21),
    (16, 23), (13, 21), (11, 16), (13, 11)
]
for tx, ty in ticks:
    c.set(tx, ty, gold1)

# === BLUE CRYSTAL CENTER ===
# Main crystal circle (radius 6)
c.circle(cx, cy, 6, blue2, fill=True)

# Crystal facets for gem effect
# Top-left highlight
c.poly([(13, 13), (16, 10), (16, 14)], blue3, fill=True)

# Bottom-right shadow
c.poly([(19, 19), (16, 16), (19, 16)], blue1, fill=True)

# Center bright highlight
c.set(15, 12, blue4)
c.set(16, 11, blue4)
c.set(15, 11, blue3)

# Crystal edge definition
c.circle(cx, cy, 6, blue1, fill=False)

# Inner crystal detail - smaller circle
c.circle(cx, cy, 3, blue3, fill=True)
c.set(16, 10, blue4)

# === COMPASS NEEDLE ===
# North-pointing arrow (prominent, on top of crystal)
c.poly([(16, 6), (14, 11), (16, 10), (18, 11)], gold5, fill=True)

# South pointer (subtle)
c.poly([(16, 22), (15, 18), (17, 18)], gold1, fill=True)

# === THICK OUTLINE ===
# Draw outline around the entire compass at radius 13
import math
for angle in range(0, 360, 3):
    rad = math.radians(angle)
    ox = int(round(cx + 13 * math.cos(rad)))
    oy = int(round(cy + 13 * math.sin(rad)))
    if 0 <= ox < 32 and 0 <= oy < 32:
        c.set(ox, oy, outline)

# Thicken outline at cardinal and diagonal points
outline_thick = [
    (16, 3), (16, 29), (3, 16), (29, 16),  # Cardinals
    (6, 6), (26, 6), (6, 26), (26, 26),    # Diagonals
]
for ox, oy in outline_thick:
    c.set(ox, oy, outline)

# Connect outline for continuous octagonal border
c.line(16, 3, 26, 6, outline)
c.line(26, 6, 29, 16, outline)
c.line(29, 16, 26, 26, outline)
c.line(26, 26, 16, 29, outline)
c.line(16, 29, 6, 26, outline)
c.line(6, 26, 3, 16, outline)
c.line(3, 16, 6, 6, outline)
c.line(6, 6, 16, 3, outline)

# Clean up - ensure ring edge is clean
c.circle(cx, cy, 12, gold3, fill=False)

print(c.stats_text())
print(c.matrix_text())

finish(c)
