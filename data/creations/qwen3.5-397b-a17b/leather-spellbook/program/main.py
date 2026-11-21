from pixelbench_api import new_canvas, finish

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="spellbook")

# Define colors (max 8 visible colors + transparent)
dark_outline = c.color("#1a1a1a", "outline")
leather_dark = c.color("#4a2810", "leather_dark")
leather_base = c.color("#6b3d1f", "leather_base")
leather_light = c.color("#8f5a33", "leather_light")
spine_dark = c.color("#2d1a0f", "spine_dark")
metal_base = c.color("#9a9a9a", "metal_base")
metal_dark = c.color("#5a5a5a", "metal_dark")
metal_bright = c.color("#c0c0c0", "metal_bright")

# Draw the spellbook - closed, showing front cover and spine
# Book is positioned at an angle, spine on left side

# ===== SPINE (left side, shows depth) =====
# Main spine area - dark brown gradient
for y in range(8, 25):
    for x in range(4, 8):
        c.set(x, y, leather_dark)

# Spine highlight (left edge of spine)
for y in range(9, 24):
    c.set(4, y, leather_light)

# Spine shadow (right edge of spine, where it meets cover)
for y in range(9, 24):
    c.set(7, y, spine_dark)

# Spine decorative bands (horizontal)
for x in range(5, 8):
    c.set(x, 10, metal_dark)
    c.set(x, 11, metal_dark)
    c.set(x, 18, metal_dark)
    c.set(x, 19, metal_dark)

# ===== FRONT COVER =====
# Main cover area - trapezoid shape to show perspective
# Cover extends from spine (x=8) to right edge of book

# Cover base color
for y in range(7, 26):
    # Calculate cover width at this row (tapers slightly)
    left_edge = 8
    right_edge = 27 - ((y - 7) // 4)  # Slight perspective taper
    
    for x in range(left_edge, right_edge + 1):
        c.set(x, y, leather_base)

# Cover highlight (top-left area, where light hits)
for y in range(8, 15):
    for x in range(9, 20 - ((y - 8) // 2)):
        c.set(x, y, leather_light)

# Cover shadow (bottom-right area)
for y in range(18, 25):
    for x in range(18 - ((y - 18) // 2), 26 - ((y - 7) // 4)):
        c.set(x, y, leather_dark)

# ===== METAL CORNERS =====
# Top-left corner (near spine)
c.set(8, 7, metal_base)
c.set(9, 7, metal_base)
c.set(8, 8, metal_base)
c.set(9, 8, metal_bright)

# Top-right corner
corner_tr = 26
c.set(corner_tr, 7, metal_base)
c.set(corner_tr - 1, 7, metal_base)
c.set(corner_tr, 8, metal_base)
c.set(corner_tr - 1, 8, metal_bright)

# Bottom-left corner (near spine)
c.set(8, 25, metal_base)
c.set(9, 25, metal_base)
c.set(8, 24, metal_base)
c.set(9, 24, metal_bright)

# Bottom-right corner
corner_br = 25
c.set(corner_br, 25, metal_base)
c.set(corner_br - 1, 25, metal_base)
c.set(corner_br, 24, metal_base)
c.set(corner_br - 1, 24, metal_bright)

# ===== CLASP/BUCKLE (center right edge) =====
# Metal clasp on the front cover
for x in range(23, 26):
    c.set(x, 16, metal_dark)
    c.set(x, 17, metal_base)
    c.set(x, 18, metal_dark)
c.set(24, 17, metal_bright)

# ===== DECORATIVE ELEMENTS ON COVER =====
# Simple embossed pattern in center
# Diamond shape
c.set(15, 12, leather_light)
c.set(14, 13, leather_light)
c.set(16, 13, leather_light)
c.set(13, 14, leather_light)
c.set(17, 14, leather_light)
c.set(14, 15, leather_light)
c.set(16, 15, leather_light)
c.set(15, 16, leather_light)

# ===== DARK OUTLINE =====
# Outline the entire book shape

# Spine left edge
for y in range(8, 25):
    c.set(3, y, dark_outline)

# Top edge (spine to right corner)
for x in range(4, 27):
    c.set(x, 6, dark_outline)

# Right edge (slight diagonal for perspective)
for y in range(7, 26):
    right_x = 27 - ((y - 7) // 4)
    c.set(right_x + 1, y, dark_outline)

# Bottom edge
for x in range(4, 26):
    c.set(x, 26, dark_outline)

# Inner spine edge (where spine meets cover)
for y in range(8, 25):
    c.set(8, y, dark_outline)

# Corner accent pixels
c.set(4, 7, dark_outline)
c.set(4, 25, dark_outline)

print(c.stats_text())
print(c.matrix_text())

finish(c)
