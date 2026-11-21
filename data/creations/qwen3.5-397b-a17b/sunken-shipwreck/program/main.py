from pixelbench_api import *

# Create 64x64 canvas for underwater shipwreck scene
c = new_canvas(64, 64)

# Define color palette
# Water colors (deep to lighter blue)
deep_water = c.color("#0a1628", "deep_water")
mid_water = c.color("#1a3a5c", "mid_water")
light_water = c.color("#2d5a7a", "light_water")
water_highlight = c.color("#4a7a9a", "water_highlight")

# Sand colors
sand_dark = c.color("#8b6f47", "sand_dark")
sand_mid = c.color("#a68b5e", "sand_mid")
sand_light = c.color("#c4a574", "sand_light")

# Wood/shipwreck colors
wood_dark = c.color("#3d2817", "wood_dark")
wood_mid = c.color("#5c3d2a", "wood_mid")
wood_light = c.color("#7a5238", "wood_light")
wood_bright = c.color("#9a6b4a", "wood_bright")
rust = c.color("#8b4513", "rust")
corroded = c.color("#4a3728", "corroded")

# Fish colors
fish_silver = c.color("#c0c8d0", "fish_silver")
fish_dark = c.color("#6a7a8a", "fish_dark")
fish_fin = c.color("#4a5a6a", "fish_fin")

# Coral colors
coral_red = c.color("#d64a5a", "coral_red")
coral_orange = c.color("#e67a4a", "coral_orange")
coral_pink = c.color("#f09a8a", "coral_pink")

# Seaweed colors
seaweed_dark = c.color("#2d5a3a", "seaweed_dark")
seaweed_mid = c.color("#3d7a4a", "seaweed_mid")
seaweed_light = c.color("#5a9a6a", "seaweed_light")

# Bubbles
bubble = c.color("#ffffff", "bubble")

# === BACKGROUND: Water gradient ===
# Fill with deep water base
c.rect(0, 0, 64, 64, deep_water)

# Add water gradient effect (lighter toward top)
for y in range(0, 32):
    alpha = int(128 * (1 - y/32))
    c.rect(0, y, 64, 1, light_water)
for y in range(32, 48):
    c.rect(0, y, 64, 1, mid_water)

# === OCEAN FLOOR: Sand ===
# Sand hill rising from bottom
c.rect(0, 48, 64, 16, sand_dark)
c.rect(0, 46, 64, 4, sand_mid)
c.rect(0, 44, 64, 3, sand_light)

# Sand texture with dithering
for x in range(0, 64, 4):
    for y in range(48, 64, 3):
        if (x + y) % 8 == 0:
            c.set(x, y, sand_light)
        elif (x + y) % 8 == 4:
            c.set(x+1, y+1, sand_mid)

# === SUNKEN SHIPWRECK ===
# Main hull - half buried, angled slightly
# Bottom part buried in sand (y=44 to 58)
# Top part visible (y=28 to 44)

# Hull base shape - curved wooden planks
# Lower hull (buried portion)
c.poly([
    (8, 52), (12, 56), (20, 58), (28, 58), (36, 57), (44, 55),
    (48, 52), (48, 48), (44, 46), (36, 45), (28, 45), (20, 46),
    (12, 48), (8, 50)
], wood_dark, fill=True)

# Upper hull (visible portion) - weathered wood
c.poly([
    (8, 50), (12, 48), (20, 46), (28, 45), (36, 45), (44, 46),
    (48, 48), (50, 46), (48, 42), (44, 38), (38, 35), (32, 33),
    (26, 34), (20, 36), (14, 39), (10, 43), (8, 47)
], wood_mid, fill=True)

# Hull planks (horizontal lines showing wood grain)
for y in [35, 38, 41, 44, 47, 50, 53, 56]:
    c.line(10, y, 46, y, wood_light)

# Vertical hull damage/cracks
c.line(18, 36, 20, 54, corroded)
c.line(32, 34, 34, 52, corroded)
c.line(40, 40, 42, 56, rust)

# Rusted metal fittings
c.rect(14, 34, 4, 8, rust)
c.rect(28, 32, 6, 6, rust)
c.rect(42, 38, 4, 10, rust)

# Broken mast/stump
c.rect(24, 20, 6, 14, wood_dark)
c.rect(25, 21, 4, 12, wood_mid)
c.line(24, 20, 30, 22, corroded)  # crack

# Tattered sail remnant
c.poly([
    (24, 22), (30, 24), (28, 32), (26, 34), (24, 30)
], "#5a4a3a", fill=True)  # tattered fabric

# Ship deck remnants
c.rect(20, 32, 24, 4, wood_bright)
c.rect(22, 33, 20, 2, wood_light)

# Porthole (broken, dark)
c.circle(34, 42, 4, "#1a1a2a", fill=True)
c.circle(34, 42, 3, "#2a2a3a", fill=True)

# === CORAL ===
# Coral cluster on left side
c.poly([(4, 52), (8, 48), (10, 54), (6, 58), (2, 56)], coral_red, fill=True)
c.poly([(6, 54), (10, 50), (12, 56), (8, 60), (4, 58)], coral_orange, fill=True)
c.set(7, 52, coral_pink)
c.set(9, 55, coral_pink)

# Coral on right side
c.poly([(54, 50), (58, 46), (60, 52), (56, 58), (52, 56)], coral_orange, fill=True)
c.poly([(56, 54), (60, 50), (61, 56), (58, 60), (54, 58)], coral_red, fill=True)
c.set(57, 52, coral_pink)
c.set(59, 55, coral_pink)

# Small coral bits near ship
c.set(50, 54, coral_red)
c.set(52, 56, coral_orange)
c.set(12, 58, coral_pink)

# === SEAWEED ===
# Seaweed strands on left
for i in range(5):
    x = 6 + i * 3
    base_y = 58
    c.line(x, base_y, x-2, base_y-8-i*3, seaweed_dark)
    c.line(x+1, base_y, x-1, base_y-10-i*2, seaweed_mid)
    c.line(x+2, base_y, x, base_y-6-i*2, seaweed_light)

# Seaweed on right
for i in range(4):
    x = 52 + i * 3
    base_y = 56
    c.line(x, base_y, min(x+2, 63), base_y-10-i*2, seaweed_dark)
    c.line(x+1, base_y, min(x+3, 63), base_y-8-i*3, seaweed_mid)
    c.line(x-1, base_y, min(x+1, 63), base_y-6-i*2, seaweed_light)

# Seaweed near ship base
c.line(16, 56, 14, 48, seaweed_mid)
c.line(17, 57, 15, 50, seaweed_light)
c.line(46, 54, 48, 46, seaweed_dark)
c.line(47, 55, 49, 48, seaweed_mid)

# === SCHOOL OF FISH ===
# Fish swimming from left to right, varying sizes
def draw_fish(x, y, size, direction=1):
    # Fish body (oval-ish)
    if size == 3:
        c.set(x, y, fish_silver)
        c.set(x+1*direction, y, fish_silver)
        c.set(x+2*direction, y, fish_silver)
        c.set(x+1*direction, y-1, fish_silver)
        c.set(x+1*direction, y+1, fish_silver)
        c.set(x+3*direction, y, fish_dark)  # tail
        c.set(x-1*direction, y, fish_fin)   # head
    elif size == 4:
        c.rect(x, y-1, 4*direction, 3, fish_silver)
        c.set(x+1*direction, y-2, fish_silver)
        c.set(x+1*direction, y+2, fish_silver)
        c.set(x+4*direction, y, fish_dark)
        c.set(x+4*direction, y-1, fish_dark)
        c.set(x+4*direction, y+1, fish_dark)
        c.set(x-1*direction, y, fish_fin)
    else:  # size 5
        c.rect(x, y-2, 5*direction, 5, fish_silver)
        c.set(x+1*direction, y-3, fish_silver)
        c.set(x+1*direction, y+3, fish_silver)
        c.set(x+2*direction, y-3, fish_silver)
        c.set(x+2*direction, y+3, fish_silver)
        c.set(x+5*direction, y-1, fish_dark)
        c.set(x+5*direction, y, fish_dark)
        c.set(x+5*direction, y+1, fish_dark)
        c.set(x+5*direction, y-2, fish_dark)
        c.set(x+5*direction, y+2, fish_dark)
        if x > 0:
            c.set(x-1*direction, y, fish_fin)
            c.set(x-1*direction, y-1, fish_fin)

# School of fish - various positions
draw_fish(8, 20, 3)
draw_fish(12, 18, 4)
draw_fish(16, 22, 3)
draw_fish(20, 16, 5)
draw_fish(24, 20, 4)
draw_fish(28, 18, 3)
draw_fish(32, 22, 4)
draw_fish(36, 16, 3)
draw_fish(40, 20, 5)
draw_fish(44, 18, 4)
draw_fish(48, 22, 3)

# Some fish lower down
draw_fish(10, 28, 3)
draw_fish(18, 26, 4)
draw_fish(26, 30, 3)
draw_fish(34, 28, 4)
draw_fish(42, 26, 3)

# === BUBBLES ===
# Rising bubbles from shipwreck
bubble_positions = [
    (26, 18), (28, 14), (27, 10), (29, 6),
    (30, 20), (32, 16), (31, 12), (33, 8),
    (24, 22), (25, 18), (23, 14)
]
for bx, by in bubble_positions:
    c.set(bx, by, bubble)
    if by > 10:
        c.set(bx+1, by-1, bubble)

# === WATER PARTICLES/LIGHT RAYS ===
# Subtle light rays from top
for x in range(0, 64, 8):
    for y in range(0, 30, 4):
        if (x + y) % 16 == 0:
            c.set(x + y//4, y, water_highlight)

# Check stats
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

# Submit the result
finish(c)
