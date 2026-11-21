from pixelbench_api import *

# Create a 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="monarch")

# Define colors for monarch butterfly
black = c.color("#000000", "black")
orange = c.color("#FF8C00", "orange")
orange_dark = c.color("#CC6600", "orange_dark")
white = c.color("#FFFFFF", "white")

# === BODY (center vertical) ===
# Head
c.set(15, 6, black)
c.set(16, 6, black)
# Thorax (wider section)
c.set(14, 7, black)
c.set(15, 7, black)
c.set(16, 7, black)
c.set(17, 7, black)
c.set(14, 8, black)
c.set(15, 8, black)
c.set(16, 8, black)
c.set(17, 8, black)
# Abdomen (tapering down)
c.set(15, 9, black)
c.set(16, 9, black)
c.set(15, 10, black)
c.set(16, 10, black)
c.set(15, 11, black)
c.set(16, 11, black)
c.set(15, 12, black)
c.set(16, 12, black)
c.set(15, 13, black)
c.set(16, 13, black)
c.set(15, 14, black)
c.set(16, 14, black)
c.set(15, 15, black)
c.set(16, 15, black)
c.set(15, 16, black)
c.set(16, 16, black)

# White spots on body (segment markings)
c.set(14, 7, white)
c.set(17, 7, white)
c.set(15, 10, white)
c.set(16, 10, white)
c.set(15, 13, white)
c.set(16, 13, white)

# Antennae (curved with clubbed tips)
c.set(14, 6, black)
c.set(13, 5, black)
c.set(12, 4, black)
c.set(12, 3, black)
c.set(17, 6, black)
c.set(18, 5, black)
c.set(19, 4, black)
c.set(19, 3, black)

# === LEFT WINGS ===
# Upper left wing - fill with orange first
c.poly([
    (14, 5), (11, 3), (7, 2), (3, 3), (1, 6),
    (1, 10), (3, 13), (7, 14), (11, 12), (14, 8)
], orange, fill=True)

# Lower left wing - larger and rounder
c.poly([
    (14, 11), (11, 13), (7, 15), (4, 15), (2, 13),
    (2, 9), (4, 7), (8, 8), (11, 9), (14, 10)
], orange, fill=True)

# === RIGHT WINGS ===
# Upper right wing
c.poly([
    (17, 5), (20, 3), (24, 2), (28, 3), (30, 6),
    (30, 10), (28, 13), (24, 14), (20, 12), (17, 8)
], orange, fill=True)

# Lower right wing - larger and rounder
c.poly([
    (17, 11), (20, 13), (24, 15), (27, 15), (29, 13),
    (29, 9), (27, 7), (23, 8), (20, 9), (17, 10)
], orange, fill=True)

# === BLACK BORDERS ===
# Left upper wing border
c.poly([
    (14, 5), (12, 4), (8, 3), (4, 4), (2, 7), (2, 10),
    (4, 12), (8, 13), (12, 11), (14, 7)
], black, fill=False)

# Left lower wing border
c.poly([
    (14, 11), (11, 13), (7, 14), (4, 14), (3, 12),
    (3, 9), (5, 8), (9, 8), (12, 9), (14, 10)
], black, fill=False)

# Right upper wing border
c.poly([
    (17, 5), (19, 4), (23, 3), (27, 4), (29, 7), (29, 10),
    (27, 12), (23, 13), (19, 11), (17, 7)
], black, fill=False)

# Right lower wing border
c.poly([
    (17, 11), (20, 13), (24, 14), (27, 14), (28, 12),
    (28, 9), (26, 8), (22, 8), (19, 9), (17, 10)
], black, fill=False)

# === BLACK VEINS ===
# Left upper wing veins
c.line(14, 6, 8, 4, black)
c.line(14, 7, 4, 6, black)
c.line(14, 8, 3, 9, black)

# Left lower wing veins
c.line(14, 11, 9, 11, black)
c.line(14, 11, 7, 13, black)
c.line(14, 11, 4, 10, black)

# Right upper wing veins
c.line(17, 6, 23, 4, black)
c.line(17, 7, 27, 6, black)
c.line(17, 8, 28, 9, black)

# Right lower wing veins
c.line(17, 11, 22, 11, black)
c.line(17, 11, 24, 13, black)
c.line(17, 11, 27, 10, black)

# === WHITE SPOTS on black borders ===
# Left upper wing spots (along the edge)
c.set(3, 8, white)
c.set(5, 5, white)
c.set(8, 4, white)
c.set(11, 5, white)

# Left lower wing spots
c.set(4, 12, white)
c.set(6, 14, white)
c.set(9, 13, white)

# Right upper wing spots
c.set(28, 8, white)
c.set(26, 5, white)
c.set(23, 4, white)
c.set(20, 5, white)

# Right lower wing spots
c.set(27, 12, white)
c.set(25, 14, white)
c.set(22, 13, white)

# === DARKER ORANGE shading (near body) ===
# Left wing
c.set(10, 7, orange_dark)
c.set(9, 9, orange_dark)
c.set(8, 11, orange_dark)
c.set(7, 12, orange_dark)

# Right wing
c.set(21, 7, orange_dark)
c.set(22, 9, orange_dark)
c.set(23, 11, orange_dark)
c.set(24, 12, orange_dark)

print(c.stats_text())
print(c.matrix_text())

finish(c)
