from pixelbench_api import *

# Create a 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None)

# Define colors - keeping palette minimal and consistent
outline = c.color("#2d2d44", name="outline")      # Dark outline
blade = c.color("#b8b8d0", name="blade")          # Silver/steel blade
blade_shine = c.color("#e0e0f0", name="blade_shine")  # Blade highlight
wood = c.color("#8b5a3c", name="wood")            # Brown wood
wood_dark = c.color("#5c3a28", name="wood_dark")  # Dark brown wood
leather = c.color("#6b4423", name="leather")      # Leather grip
gold = c.color("#c9a94a", name="gold")            # Gold trim
shield_blue = c.color("#4a5f7f", name="shield_blue")  # Shield main
shield_red = c.color("#8b2332", name="shield_red")    # Shield center
axe_metal = c.color("#9898a8", name="axe_metal")  # Axe head metal

# Each icon fits in 28x28 area with padding
# Top-left: sword, Top-right: bow, Bottom-left: shield, Bottom-right: axe

# === SWORD (top-left: 4,4 to 30,30) ===
sx, sy = 5, 5

# Blade - pointing diagonally up-right (northeast)
# Main blade - filled triangle
c.poly([(sx+6, sy+16), (sx+16, sy+6), (sx+20, sy+10), (sx+10, sy+20)], blade, fill=True)
# Blade highlight
c.poly([(sx+8, sy+16), (sx+15, sy+9), (sx+18, sy+12)], blade_shine, fill=True)

# Crossguard (horizontal bar at base of blade)
c.rect(sx+4, sy+18, 8, 4, gold, fill=True)

# Handle (grip)
c.rect(sx+12, sy+21, 4, 8, leather, fill=True)
# Handle details
c.line(sx+13, sy+22, sx+15, sy+22, wood_dark)
c.line(sx+13, sy+25, sx+15, sy+25, wood_dark)
c.line(sx+13, sy+28, sx+15, sy+28, wood_dark)

# Pommel (round end cap)
c.circle(sx+14, sy+31, 3, gold, fill=True)

# Outline edges
c.line(sx+16, sy+6, sx+17, sy+6, outline)
c.line(sx+17, sy+7, sx+18, sy+7, outline)

# === BOW (top-right: 34,4 to 60,30) ===
bx, by = 36, 5

# Bow body - curved C shape opening to right
# Top curve
c.line(bx+2, by+4, bx+5, by+2, wood)
c.line(bx+5, by+2, bx+9, by+1, wood)
c.line(bx+9, by+1, bx+13, by+2, wood)
c.line(bx+13, by+2, bx+16, by+4, wood)
c.line(bx+16, by+4, bx+18, by+7, wood)
# Right side (straight part)
c.line(bx+18, by+7, bx+19, by+11, wood)
c.line(bx+19, by+11, bx+19, by+15, wood)
c.line(bx+19, by+15, bx+19, by+19, wood)
# Bottom curve
c.line(bx+19, by+19, bx+18, by+22, wood)
c.line(bx+18, by+22, bx+16, by+25, wood)
c.line(bx+16, by+25, bx+13, by+27, wood)
c.line(bx+13, by+27, bx+9, by+28, wood)
c.line(bx+9, by+28, bx+5, by+27, wood)
c.line(bx+5, by+27, bx+2, by+25, wood)
# Left side going up
c.line(bx+2, by+25, bx+1, by+22, wood)
c.line(bx+1, by+22, bx+1, by+19, wood)
c.line(bx+1, by+19, bx+1, by+15, wood)
c.line(bx+1, by+15, bx+1, by+11, wood)
c.line(bx+1, by+11, bx+1, by+7, wood)
c.line(bx+1, by+7, bx+2, by+4, wood)

# Bow string (straight vertical line)
c.line(bx+3, by+6, bx+3, by+23, wood_dark)

# Bow grip
c.rect(bx+0, by+13, 4, 5, leather, fill=True)

# Outline bow curve
c.line(bx+8, by+1, bx+9, by+0, outline)
c.line(bx+19, by+14, bx+20, by+14, outline)

# === SHIELD (bottom-left: 4,34 to 30,60) ===
shx, shy = 5, 36

# Shield - heater shield shape (pointed bottom)
# Main body
c.poly([
    (shx+10, shy+2),   # top center
    (shx+20, shy+2),   # top right corner
    (shx+24, shy+7),   # right shoulder
    (shx+24, shy+16),  # right side
    (shx+20, shy+22),  # bottom right
    (shx+15, shy+26),  # bottom point
    (shx+10, shy+22),  # bottom left
    (shx+6, shy+16),   # left side
    (shx+6, shy+7),    # left shoulder
    (shx+10, shy+2)    # back to top
], shield_blue, fill=True)

# Shield border/rim
c.poly([
    (shx+10, shy+2), (shx+20, shy+2), (shx+23, shy+6), (shx+23, shy+16),
    (shx+19, shy+21), (shx+15, shy+25), (shx+11, shy+21), (shx+7, shy+16),
    (shx+7, shy+6), (shx+10, shy+2)
], gold, fill=False)

# Center boss (round decoration)
c.circle(shx+15, shy+14, 4, shield_red, fill=True)
c.circle(shx+15, shy+14, 5, gold, fill=False)
c.circle(shx+15, shy+14, 2, gold, fill=True)

# === BATTLE AXE (bottom-right: 34,34 to 60,60) ===
ax, ay = 36, 38

# Axe handle - diagonal from lower-left to upper-right
c.line(ax+4, ay+22, ax+18, ay+6, wood)
c.line(ax+6, ay+24, ax+20, ay+8, wood_dark)

# Left axe blade (crescent shape)
c.poly([
    (ax+2, ay+4),
    (ax+7, ay+8),
    (ax+9, ay+12),
    (ax+7, ay+16),
    (ax+2, ay+20)
], axe_metal, fill=True)
# Blade detail
c.line(ax+4, ay+6, ax+6, ay+8, blade_shine)
c.line(ax+4, ay+18, ax+6, ay+16, blade_shine)

# Right axe blade (crescent shape, mirrored)
c.poly([
    (ax+24, ay+4),
    (ax+19, ay+8),
    (ax+17, ay+12),
    (ax+19, ay+16),
    (ax+24, ay+20)
], axe_metal, fill=True)
# Blade detail
c.line(ax+22, ay+6, ax+20, ay+8, blade_shine)
c.line(ax+22, ay+18, ax+20, ay+16, blade_shine)

# Center collar/connection
c.rect(ax+9, ay+8, 8, 8, gold, fill=True)

# Handle butt (end cap)
c.rect(ax+2, ay+22, 5, 5, wood_dark, fill=True)

# Outline blade tips
c.line(ax+2, ay+4, ax+3, ay+4, outline)
c.line(ax+2, ay+20, ax+3, ay+20, outline)
c.line(ax+23, ay+4, ax+24, ay+4, outline)
c.line(ax+23, ay+20, ax+24, ay+20, outline)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

# Submit
finish(c)
