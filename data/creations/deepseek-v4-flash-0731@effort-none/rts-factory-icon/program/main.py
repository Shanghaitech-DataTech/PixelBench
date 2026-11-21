from pixelbench_api import *

# Create 32x32 canvas
c = new_canvas(32, 32, name="factory")

# ---- Color palette ----
# Brick walls
BRICK = "#8B4513"          # main brick
BRICK_DARK = "#6B3410"     # shadow brick
BRICK_LIGHT = "#A85B2E"    # highlight brick
MORTAR = "#5A2D0C"         # mortar line
MORTAR_DARK = "#4A2509"    # dark mortar

# Roof
ROOF = "#565656"           # flat concrete roof
ROOF_DARK = "#3D3D3D"      # roof shade
ROOF_LIGHT = "#777777"     # roof highlight

# Chimney
CHIM_SIDE = "#777777"      # chimney light face
CHIM_FRONT = "#5F5F5F"     # chimney front
CHIM_DARK = "#444444"      # chimney shadow
CHIM_TOP = "#A0A0A0"       # chimney rim

# Outline / silhouette
DARK = "#141414"           # dark outline

# Details
METAL = "#8C8C8C"          # door metal
METAL_DARK = "#6A6A6A"
WINDOW_GLOW = "#FFD984"    # window warm light
WINDOW_FRAME = "#C8A54E"   # window frame
VENT = "#2E2E2E"           # vent dark
VENT_HI = "#464646"        # vent louver highlight

# Smoke
SMOKE = "#E8E8E8"
SMOKE_LT = "#FFFFFF"

# Ground shadow
GROUND = "#3A2A1A"

# ---------------------------------------------------------------
# BUILDING: main body x=3..28, y=13..26  (26 px wide, 14 tall)
# Centered at x=15.5, building spans 3-28.
# ---------------------------------------------------------------

# Ground shadow - soft irregular base
for x in range(1, 31):
    c.set(x, 26, GROUND)
for x in range(2, 30):
    c.set(x, 27, GROUND)
for x in range(4, 28):
    c.set(x, 28, GROUND)
for x in range(6, 26):
    c.set(x, 29, GROUND)
for x in range(9, 23):
    c.set(x, 30, GROUND)
c.set(15, 31, GROUND)

# ---------- Fill brick body ----------
for y in range(13, 26):
    for x in range(3, 29):
        c.set(x, y, BRICK)

# Brick pattern: horizontal courses every 3 rows
for y in range(16, 25, 3):
    for x in range(3, 29):
        c.set(x, y, MORTAR)

# Vertical brick joints staggered
# course 0: y=13,14  course 1: y=15(dark mortar row)... let me define distinct courses
# Courses (3 rows each): y 13-14, 15-16, 18-19, 21-22, 24 - wait need consistent.
# Let's make mortar horizontal lines at y=15, y=18, y=21, y=24
for y in (15, 18, 21, 24):
    for x in range(3, 29):
        c.set(x, y, MORTAR)

# Vertical joints in the two rows above each mortar line
# Course between y13-14: joints at even x (offset 0): x=7,11,15,19,23,27
for y in (13, 14):
    for x in range(3, 29):
        if (x - 3) % 4 == 0:
            c.set(x, y, MORTAR)
# Course y16-17: joints staggered (offset 2)
for y in (16, 17):
    for x in range(3, 29):
        if (x - 3 + 2) % 4 == 0:
            c.set(x, y, MORTAR)
# Course y19-20: joints at offset 0
for y in (19, 20):
    for x in range(3, 29):
        if (x - 3) % 4 == 0:
            c.set(x, y, MORTAR)
# Course y22-23: joints offset 2
for y in (22, 23):
    for x in range(3, 29):
        if (x - 3 + 2) % 4 == 0:
            c.set(x, y, MORTAR)
# Course y25: joints offset 0
for x in range(3, 29):
    if (x - 3) % 4 == 0:
        c.set(x, 25, MORTAR)

# Light on left face and dark on right face of wall
# Highlight top-left corner
for x in range(3, 8):
    c.set(x, 13, BRICK_LIGHT)
for y in range(13, 17):
    c.set(3, y, BRICK_LIGHT)
# Shadow bottom-right
for y in range(22, 26):
    c.set(28, y, BRICK_DARK)
for x in range(24, 29):
    c.set(x, 25, BRICK_DARK)

# ---------- Building outline ----------
# Left edge
for y in range(12, 26):
    c.set(2, y, DARK)
# Right edge
for y in range(12, 26):
    c.set(28, y, DARK)
# Bottom corners to ground
c.set(2, 26, DARK)
c.set(28, 26, DARK)

# ---------- Flat roof with parapet ----------
# Roof deck y=9..12
for y in range(9, 13):
    for x in range(4, 28):
        c.set(x, y, ROOF)
# Parapet top rim (silhouette) - y=8
for x in range(4, 28):
    c.set(x, 8, DARK)
# Parapet inner highlight
for x in range(5, 27):
    c.set(x, 9, ROOF_LIGHT)
# Left/right parapet walls
for y in range(8, 13):
    c.set(3, y, DARK)
    c.set(27, y, DARK)
# Parapet corners
c.set(3, 8, DARK)
c.set(27, 8, DARK)

# Roof panel seams - horizontal lines
for x in range(6, 27, 5):
    for y in range(10, 13):
        c.set(x, y, ROOF_DARK)

# ---------- Chimney (right side of roof) ----------
# Chimney body x=21..25, y=3..8
for y in range(3, 9):
    for x in range(20, 26):
        c.set(x, y, CHIM_FRONT)
    # left highlight face
    c.set(20, y, CHIM_SIDE)
    # right shadow
    c.set(25, y, CHIM_DARK)
# Chimney top rim
for x in range(20, 26):
    c.set(x, 3, CHIM_TOP)
    c.set(x, 2, DARK)
c.set(19, 2, DARK)
c.set(26, 2, DARK)
c.set(19, 3, DARK)
c.set(26, 3, DARK)

# ---------- Secondary structure: small vent stack (left side) ----------
# Small exhaust vent on roof left x=7..11
for y in range(6, 9):
    for x in range(7, 12):
        c.set(x, y, CHIM_FRONT)
    c.set(7, y, CHIM_SIDE)
    c.set(11, y, CHIM_DARK)
for x in range(7, 12):
    c.set(x, 6, CHIM_TOP)
    c.set(x, 5, DARK)
c.set(6, 5, DARK)
c.set(12, 5, DARK)
# Vent grille opening on top of small stack
for x in range(8, 11):
    c.set(x, 5, DARK)
    c.set(x, 4, DARK)

# ---------- Windows (second story) ----------
# Left window x=8..12, y=15..18
for y in range(15, 19):
    for x in range(8, 13):
        c.set(x, y, WINDOW_GLOW)
# Window frames
for y in range(15, 19):
    c.set(7, y, DARK)
    c.set(13, y, DARK)
for x in range(8, 13):
    c.set(x, 14, DARK)
    c.set(x, 19, DARK)
# Cross bars
for x in range(8, 13):
    c.set(x, 16, WINDOW_FRAME)
c.set(10, 15, WINDOW_FRAME)
c.set(10, 17, WINDOW_FRAME)

# Right window x=19..23, y=15..18
for y in range(15, 19):
    for x in range(19, 24):
        c.set(x, y, WINDOW_GLOW)
for y in range(15, 19):
    c.set(18, y, DARK)
    c.set(24, y, DARK)
for x in range(19, 24):
    c.set(x, 14, DARK)
    c.set(x, 19, DARK)
for x in range(19, 24):
    c.set(x, 16, WINDOW_FRAME)
c.set(21, 15, WINDOW_FRAME)
c.set(21, 17, WINDOW_FRAME)

# ---------- Vent (first story, left) ----------
# Louver vent x=6..12, y=21..24
for y in range(21, 25):
    for x in range(6, 13):
        c.set(x, y, VENT)
for y in range(21, 25):
    c.set(5, y, DARK)
    c.set(13, y, DARK)
for x in range(6, 13):
    c.set(x, 20, DARK)
    c.set(x, 25, DARK)
# Louver slats
for x in range(6, 13):
    c.set(x, 22, VENT_HI)
    c.set(x, 24, VENT_HI)

# ---------- Door (center, x=15..20, y=21..25) ----------
for y in range(21, 26):
    for x in range(15, 21):
        c.set(x, y, METAL)
# Door outline
for y in range(21, 26):
    c.set(14, y, DARK)
    c.set(21, y, DARK)
for x in range(15, 21):
    c.set(x, 20, DARK)
    c.set(x, 25, DARK)
# Door highlight on left
for x in range(15, 18):
    c.set(x, 22, METAL)
    c.set(x, 23, METAL)
# Door handle
c.set(19, 23, DARK)
# Door panel seam
c.set(17, 21, "#5F5F5F")
c.set(17, 24, "#5F5F5F")

# ---------- Right small vent x=24..28, y=23..25 ----------
for y in range(23, 26):
    for x in range(24, 29):
        c.set(x, y, VENT)
for y in range(23, 26):
    c.set(23, y, DARK)
for x in range(24, 29):
    c.set(x, 22, DARK)
for x in range(24, 29):
    c.set(x, 24, VENT_HI)

# ---------- Smoke puffs from chimney ----------
# Puffs floating above the chimney opening (x=21..24), rows 0-1
c.set(22, 1, SMOKE)
c.set(23, 1, SMOKE)
c.set(21, 1, SMOKE)
c.set(22, 0, SMOKE_LT)
c.set(21, 0, SMOKE)
c.set(23, 0, SMOKE)

# Under-door ground shadow
for x in range(13, 19):
    c.set(x, 26, DARK)
c.set(12, 26, DARK)
c.set(19, 26, DARK)

# Print stats
print(c.stats_text())

# Submit
result = c
finish(result)
