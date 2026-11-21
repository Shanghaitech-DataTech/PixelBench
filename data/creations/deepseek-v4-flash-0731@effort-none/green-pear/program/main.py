from pixelbench_api import *

# Create a 32x32 canvas
c = new_canvas(32, 32)

# Define colors (7 max including transparent)
# pear body green (light)
L_GREEN = "#a8c839"
# pear body green (mid)
M_GREEN = "#7a9b2e"
# pear shadow/dark
D_GREEN = "#55701f"
# highlight light green
HL_GREEN = "#d2e878"
# stem brown
BROWN = "#6b4226"
# leaf green
LEAF_GREEN = "#4d7c14"

# The pear shape: bottom is broad rounded, top narrows to a stem.
# Fill the main body with mid green using an ellipse-like shape.
# Body center roughly at (16, 19)
# Draw body as a filled shape bottom-heavy.

# Main body: a broad rounded bottom.
c.ellipse(16, 20, 12, 10, M_GREEN)  # main bulb
# Narrow upper part
c.ellipse(16, 13, 7, 5, M_GREEN)
# A bit of shoulder
c.ellipse(16, 16, 9, 6, M_GREEN)

# Darker shadow on right-bottom
c.ellipse(20, 22, 6, 7, D_GREEN)

# Light highlight on top-left
c.ellipse(12, 16, 4, 6, L_GREEN)
# little specular highlight
c.circle(11, 14, 2, HL_GREEN)

# Stem: brown curved line from top
c.line(16, 5, 16, 9, BROWN)
c.line(16, 5, 15, 5, BROWN)

# Leaf attached at top of stem
# small leaf
c.ellipse(21, 6, 4, 2, LEAF_GREEN)

# Trim stems: above body is stem area. Let's draw stem from top area (y=? body top).
# Actually body top around y=8. Draw stem from y=5 to y=8.
# We already did y=5..9 overlapping body - fine.

# Let's do a proper stem: vertical from y=4 to y=8 at x=16
c.clear(15, 3, 3, 2)  # just ensure top area clean? clear may remove. skip

# Redraw cleanly to avoid artifacts - rebuild fresh
c2 = new_canvas(32, 32)
c = c2

# Body silhouette: pear is wider at bottom.
# Bottom bulb
c.ellipse(16, 21, 11, 8, M_GREEN)      # y 13..29
# Middle
c.ellipse(16, 15, 8, 5, M_GREEN)       # y 10..20
# Top neck
c.ellipse(16, 10, 5, 3, M_GREEN)       # y 7..13

# Shadow on right side (inner edge along right of body)
c.ellipse(19, 21, 6, 7, D_GREEN)

# Light on left, mid
c.ellipse(12, 17, 4, 6, L_GREEN)

# Small bright specular
c.circle(11, 14, 2, HL_GREEN)

# Stem - connect from top of neck
c.rect(15, 4, 2, 6, BROWN)   # y 4..9
# small crook on stem
c.rect(14, 4, 2, 2, BROWN)

# Leaf at top right of stem
c.ellipse(20, 5, 4, 2, LEAF_GREEN)
# stem tip reaching under leaf
c.rect(15, 4, 2, 2, BROWN)

# cleanup stray pixels
c.set(16, 4, None)   # stray leaf pixel below leaf
c.set(13, 26, None)  # stray body pixel bottom

# Little dimple spot on pear bottom
c.rect(16, 28, 2, 1, D_GREEN)

print(c.stats_text())

finish(c)
