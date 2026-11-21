from pixelbench_api import new_canvas, finish

# Create 128x128 canvas for isometric forge house
c = new_canvas(128, 128, name="forge_house")

# Define palette colors - staying under 86 colors
# Wood tones
wood_dark = c.color("#3d2817", "wood_dark")
wood_mid = c.color("#5c3a21", "wood_mid")
wood_light = c.color("#7d5030", "wood_light")
wood_highlight = c.color("#9c6842", "wood_highlight")

# Roof red tiles
roof_dark = c.color("#8b2323", "roof_dark")
roof_mid = c.color("#b33030", "roof_mid")
roof_light = c.color("#d44545", "roof_light")
roof_highlight = c.color("#e86060", "roof_highlight")

# Stone/gray tones
stone_dark = c.color("#4a4a4a", "stone_dark")
stone_mid = c.color("#6b6b6b", "stone_mid")
stone_light = c.color("#8a8a8a", "stone_light")

# Furnace glow
glow_dark = c.color("#8b4513", "glow_dark")
glow_mid = c.color("#cd6600", "glow_mid")
glow_bright = c.color("#ff8c00", "glow_bright")
glow_yellow = c.color("#ffcc00", "glow_yellow")

# Barrel colors
barrel_dark = c.color("#4a3520", "barrel_dark")
barrel_mid = c.color("#6b4d30", "barrel_mid")
barrel_band = c.color("#2a2a2a", "barrel_band")

# Sign colors
sign_wood = c.color("#6b4423", "sign_wood")
sign_text = c.color("#f5deb3", "sign_text")

# Chimney
chimney_dark = c.color("#5a5a5a", "chimney_dark")
chimney_light = c.color("#7a7a7a", "chimney_light")

# Shadows and outlines
shadow = c.color("#2a1a10", "shadow")
outline = c.color("#1a1a1a", "outline")

# Background - transparent (default)

# Isometric building - centered with proper margins
# Building positioned so everything fits in 128x128
base_x = 64
base_y = 85  # Lower base to make room for roof
half_width = 28
height = 38

# Draw left wall (darker, in shadow)
left_wall_pts = [
    (base_x - half_width, base_y),
    (base_x, base_y - half_width),
    (base_x, base_y - half_width - height),
    (base_x - half_width, base_y - height)
]
c.poly(left_wall_pts, stone_dark, fill=True)

# Draw right wall (lighter)
right_wall_pts = [
    (base_x, base_y - half_width),
    (base_x + half_width, base_y),
    (base_x + half_width, base_y - height),
    (base_x, base_y - half_width - height)
]
c.poly(right_wall_pts, stone_light, fill=True)

# Draw front face (main wall with furnace)
front_wall_pts = [
    (base_x - half_width, base_y),
    (base_x + half_width, base_y),
    (base_x + half_width, base_y - height),
    (base_x - half_width, base_y - height)
]
c.poly(front_wall_pts, stone_mid, fill=True)

# Furnace opening (glowing)
furnace_x = base_x
furnace_y = base_y - 12
furnace_w = 16
furnace_h = 12
c.rect(furnace_x - furnace_w//2, furnace_y - furnace_h//2, furnace_w, furnace_h, glow_dark, fill=True)
c.rect(furnace_x - furnace_w//2 + 2, furnace_y - furnace_h//2 + 2, furnace_w - 4, furnace_h - 4, glow_mid, fill=True)
c.rect(furnace_x - furnace_w//2 + 4, furnace_y - furnace_h//2 + 4, furnace_w - 8, furnace_h - 8, glow_bright, fill=True)
c.set(furnace_x, furnace_y, glow_yellow)

# Furnace frame
c.rect(furnace_x - furnace_w//2 - 2, furnace_y - furnace_h//2 - 2, furnace_w + 4, 2, stone_dark, fill=True)
c.rect(furnace_x - furnace_w//2 - 2, furnace_y + furnace_h//2, furnace_w + 4, 2, stone_dark, fill=True)

# Roof base (flat top of building)
roof_base_y = base_y - height

# Pyramid roof with red tiles - smaller roof to fit
roof_peak_x = base_x
roof_peak_y = base_y - half_width - height - 18  # Peak height

# Left roof face
left_roof_pts = [
    (base_x - half_width, roof_base_y),
    (base_x, roof_base_y - half_width),
    (roof_peak_x, roof_peak_y)
]
c.poly(left_roof_pts, roof_dark, fill=True)

# Right roof face  
right_roof_pts = [
    (base_x + half_width, roof_base_y),
    (base_x, roof_base_y - half_width),
    (roof_peak_x, roof_peak_y)
]
c.poly(right_roof_pts, roof_mid, fill=True)

# Front roof face
front_roof_pts = [
    (base_x - half_width, roof_base_y),
    (base_x + half_width, roof_base_y),
    (roof_peak_x, roof_peak_y)
]
c.poly(front_roof_pts, roof_light, fill=True)

# Roof tile lines (horizontal bands)
for i in range(4):
    tile_y = roof_peak_y + 3 + i * 3
    # Left roof tiles
    c.line(base_x - half_width + i * 2, roof_base_y - i, 
           base_x - 4 + i, tile_y, roof_highlight)
    # Right roof tiles
    c.line(base_x + 4 - i, tile_y,
           base_x + half_width - i * 2, roof_base_y - i, roof_highlight)

# Chimney on right side of roof
chimney_x = base_x + 10
chimney_base_y = roof_base_y - half_width // 2
chimney_w = 6
chimney_h = 10
c.rect(chimney_x - chimney_w//2, chimney_base_y - chimney_h, chimney_w, chimney_h, chimney_dark, fill=True)
c.rect(chimney_x - chimney_w//2 + 1, chimney_base_y - chimney_h, 2, chimney_h, chimney_light, fill=True)
# Chimney top
c.rect(chimney_x - chimney_w//2 - 1, chimney_base_y - chimney_h - 2, chimney_w + 2, 3, chimney_dark, fill=True)
# Smoke particles (subtle gray)
for i in range(3):
    c.set(chimney_x - 1 + i, chimney_base_y - chimney_h - 3 - i * 2, stone_light)

# Wooden sign hanging on front
sign_x = base_x - 18
sign_y = roof_base_y + 8
sign_w = 16
sign_h = 10
# Sign board
c.rect(sign_x, sign_y, sign_w, sign_h, sign_wood, fill=True)
c.rect(sign_x + 1, sign_y + 1, sign_w - 2, sign_h - 2, wood_light, fill=True)
# Sign posts
c.line(sign_x + 2, sign_y + sign_h, sign_x + 2, sign_y + sign_h + 6, wood_dark)
c.line(sign_x + sign_w - 2, sign_y + sign_h, sign_x + sign_w - 2, sign_y + sign_h + 6, wood_dark)
# Sign text (simple anvil symbol)
c.set(sign_x + 6, sign_y + 3, sign_text)
c.set(sign_x + 7, sign_y + 3, sign_text)
c.set(sign_x + 8, sign_y + 3, sign_text)
c.set(sign_x + 7, sign_y + 4, sign_text)
c.set(sign_x + 5, sign_y + 5, sign_text)
c.set(sign_x + 6, sign_y + 5, sign_text)
c.set(sign_x + 7, sign_y + 5, sign_text)
c.set(sign_x + 8, sign_y + 5, sign_text)
c.set(sign_x + 9, sign_y + 5, sign_text)

# Sign chains
c.line(sign_x + 2, sign_y, sign_x + 2, sign_y - 6, stone_dark)
c.line(sign_x + sign_w - 2, sign_y, sign_x + sign_w - 2, sign_y - 6, stone_dark)

# Stacked barrels (left side of building)
barrel_x = base_x - half_width - 15
barrel_y = base_y - 3
barrel_r = 6

# Bottom row - 2 barrels
for bx in [barrel_x - 8, barrel_x + 8]:
    # Barrel body
    c.ellipse(bx, barrel_y, barrel_r, barrel_r, barrel_mid, fill=True)
    c.ellipse(bx, barrel_y, barrel_r - 1, barrel_r - 1, barrel_dark, fill=True)
    # Barrel bands
    c.line(bx - barrel_r + 2, barrel_y - 3, bx + barrel_r - 2, barrel_y - 3, barrel_band)
    c.line(bx - barrel_r + 2, barrel_y + 3, bx + barrel_r - 2, barrel_y + 3, barrel_band)
    # Highlights
    c.set(bx - 2, barrel_y - 4, wood_highlight)
    c.set(bx + 2, barrel_y - 2, wood_highlight)

# Top barrel (centered on bottom two)
top_barrel_x = barrel_x
top_barrel_y = barrel_y - 11
c.ellipse(top_barrel_x, top_barrel_y, barrel_r, barrel_r, barrel_mid, fill=True)
c.ellipse(top_barrel_x, top_barrel_y, barrel_r - 1, barrel_r - 1, barrel_dark, fill=True)
c.line(top_barrel_x - barrel_r + 2, top_barrel_y - 3, top_barrel_x + barrel_r - 2, top_barrel_y - 3, barrel_band)
c.line(top_barrel_x - barrel_r + 2, top_barrel_y + 3, top_barrel_x + barrel_r - 2, top_barrel_y + 3, barrel_band)
c.set(top_barrel_x - 2, top_barrel_y - 4, wood_highlight)
c.set(top_barrel_x + 2, top_barrel_y - 2, wood_highlight)

# Ground shadow under building
shadow_pts = [
    (base_x - half_width - 2, base_y + 1),
    (base_x, base_y - half_width + 1),
    (base_x + half_width + 2, base_y + 1),
    (base_x, base_y + 2)
]
c.poly(shadow_pts, shadow, fill=True)

# Add outline to building edges
c.poly(left_wall_pts, outline, fill=False)
c.poly(right_wall_pts, outline, fill=False)
c.poly(front_wall_pts, outline, fill=False)

# Door on front wall
door_x = base_x - 6
door_y = base_y - 3
door_w = 12
door_h = 16
c.rect(door_x, door_y - door_h, door_w, door_h, wood_dark, fill=True)
c.rect(door_x + 2, door_y - door_h + 2, door_w - 4, door_h - 4, wood_mid, fill=True)
# Door frame
c.line(door_x, door_y - door_h, door_x, door_y, wood_dark)
c.line(door_x + door_w, door_y - door_h, door_x + door_w, door_y, wood_dark)
c.line(door_x, door_y - door_h, door_x + door_w, door_y - door_h, wood_dark)
# Door handle
c.set(door_x + door_w - 3, door_y - door_h // 2, stone_light)

# Window on right wall with furnace glow spill
window_x = base_x + 15
window_y = roof_base_y - 10
window_w = 8
window_h = 10
c.rect(window_x, window_y - window_h, window_w, window_h, glow_dark, fill=True)
c.rect(window_x + 2, window_y - window_h + 2, window_w - 4, window_h - 4, glow_mid, fill=True)
# Window frame
c.line(window_x, window_y - window_h, window_x, window_y, wood_dark)
c.line(window_x + window_w, window_y - window_h, window_x + window_w, window_y, wood_dark)
c.line(window_x, window_y - window_h, window_x + window_w, window_y - window_h, wood_dark)
c.line(window_x, window_y, window_x + window_w, window_y, wood_dark)
c.line(window_x + window_w // 2, window_y - window_h, window_x + window_w // 2, window_y, wood_dark)
c.line(window_x, window_y - window_h // 2, window_x + window_w, window_y - window_h // 2, wood_dark)

# Small anvil near entrance
anvil_x = base_x - 20
anvil_y = base_y - 1
c.rect(anvil_x, anvil_y - 5, 10, 5, stone_dark, fill=True)
c.rect(anvil_x - 2, anvil_y - 7, 14, 3, stone_mid, fill=True)
c.set(anvil_x + 3, anvil_y - 8, stone_light)
c.set(anvil_x + 6, anvil_y - 8, stone_light)

# Hammer leaning against wall
hammer_x = base_x - half_width - 5
hammer_y = roof_base_y + 5
c.line(hammer_x, hammer_y, hammer_x + 6, hammer_y + 16, wood_dark)
c.rect(hammer_x - 2, hammer_y - 3, 6, 5, stone_dark, fill=True)

# Roof ridge lines
c.line(base_x - half_width, roof_base_y, roof_peak_x, roof_peak_y, roof_highlight)
c.line(base_x + half_width, roof_base_y, roof_peak_x, roof_peak_y, roof_highlight)

# Additional building details - brick pattern hints on walls
for row in range(4):
    by = base_y - height + 5 + row * 8
    for col in range(6):
        bx = base_x - half_width + 3 + col * 9
        if row % 2 == 0:
            c.set(bx, by, stone_light)
        else:
            c.set(bx + 4, by, stone_light)

print(c.stats_text())
print(c.matrix_text(region=(25, 35, 105, 110)))

finish(c)
