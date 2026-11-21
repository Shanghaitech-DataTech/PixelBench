from pixelbench_api import *

c = new_canvas(32, 32)

# Color Palette:
# Outlines:
OUTLINE = "#12151c"
OUTLINE_SOFT = "#1e232e"

# Steel / Chainmail shades:
C_SPEC = "#ffffff"       # Specular gleam
C_LIGHT = "#e2e8f0"      # Bright metal highlight
C_L_MID = "#cbd5e1"      # Light steel
C_MID = "#94a3b8"        # Midtone steel
C_D_MID = "#64748b"      # Dark midtone
C_SHAD = "#475569"       # Shadow steel
C_D_SHAD = "#334155"     # Deep shadow
C_HOLE = "#18202c"       # Inside ring hole / under-armor
C_DEEP = "#0f131a"       # Deep crevices / armhole interior

# Leather trim / straps / collar / belt:
L_HI = "#b45309"         # Leather highlight
L_MID = "#78350f"        # Leather mid
L_SHAD = "#451a03"       # Leather shadow
L_DARK = "#270f02"       # Leather dark outline
GOLD_HI = "#fde047"      # Buckle/rivet highlight
GOLD_MID = "#ca8a04"     # Buckle mid
GOLD_SHAD = "#713f12"    # Buckle shadow

# Let's define the armor silhouette mask
armor_mask = set()

# Shoulders & upper chest (y=5..15)
# Neck opening is at x=13..18, y=4..7
# Left shoulder slopes from (12, 5) to (3, 10)
# Right shoulder slopes from (19, 5) to (28, 10)

# Let's define the full solid shape first:
shape_rows = {
    4: range(12, 20),
    5: range(9, 23),
    6: range(6, 26),
    7: range(4, 28),
    8: range(3, 29),
    9: range(2, 30),
    10: range(2, 30),
    11: range(2, 30),
    12: range(2, 30),
    13: range(2, 30),
    14: range(2, 30),
    15: range(3, 29),
    16: range(8, 24),
    17: range(8, 24),
    18: range(8, 24),
    19: range(8, 24),
    20: range(8, 24),
    21: range(8, 24),
    22: range(7, 25),
    23: range(7, 25),
    24: range(7, 25),
    25: range(7, 25),
    26: range(7, 25),
    27: range(7, 25),
    28: list(range(7, 15)) + list(range(17, 25)),  # Split at center (15, 16)
}

for y, xs in shape_rows.items():
    for x in xs:
        armor_mask.add((x, y))

# Sleeve separation gaps (underarm cutout at y=14..16):
# The sleeves end at y=15, width x=2..7 on left, 24..29 on right
# Gaps between sleeves and torso at y=15, 16:
# Left gap: x=7, 8; Right gap: x=23, 24
for y in [14, 15]:
    armor_mask.discard((7, y))
    armor_mask.discard((8, y))
    armor_mask.discard((23, y))
    armor_mask.discard((24, y))

# Let's fill the base shape with dark undergarment / hole color
for (x, y) in armor_mask:
    c.set(x, y, C_HOLE)

# Add outline around the mask:
for (x, y) in list(armor_mask):
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in armor_mask:
            # Check bounds
            if 0 <= nx < 32 and 0 <= ny < 32:
                c.set(nx, ny, OUTLINE)

# Now, neck hole interior:
# Cut out neck hole:
neck_interior = set()
for x in range(13, 19):
    c.set(x, 4, OUTLINE)
for x in range(13, 19):
    c.set(x, 5, "#1e1b24") # Gambeson interior collar
    neck_interior.add((x, 5))
for x in range(14, 18):
    c.set(x, 6, "#15131a")
    neck_interior.add((x, 6))
c.set(15, 7, "#15131a")
c.set(16, 7, "#15131a")
neck_interior.add((15, 7))
neck_interior.add((16, 7))

# Neck rim / leather collar:
collar_pixels = [
    (12, 5), (19, 5),
    (12, 6), (13, 6), (18, 6), (19, 6),
    (13, 7), (14, 7), (17, 7), (18, 7),
    (14, 8), (15, 8), (16, 8), (17, 8)
]
for x, y in collar_pixels:
    c.set(x, y, L_MID)

view(c)
