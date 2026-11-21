from pixelbench_api import new_canvas, finish

# Create 64x64 canvas for tavern interior
c = new_canvas(64, 64)

# Define color palette - warm tavern colors (aiming for ~86 colors max)
# Wood tones
dark_wood = c.color((62, 40, 25), "dark_wood")
medium_wood = c.color((101, 67, 33), "medium_wood")
light_wood = c.color((139, 90, 43), "light_wood")
pale_wood = c.color((181, 137, 84), "pale_wood")

# Lighting - warm yellows and oranges
lamp_core = c.color((255, 255, 220), "lamp_core")
lamp_yellow = c.color((255, 220, 100), "lamp_yellow")
lamp_glow = c.color((255, 180, 50), "lamp_glow")
warm_light = c.color((255, 150, 80), "warm_light")
warm_orange = c.color((255, 120, 40), "warm_orange")

# Background and walls
wall_dark = c.color((45, 35, 30), "wall_dark")
wall_mid = c.color((70, 55, 45), "wall_mid")
wall_light = c.color((95, 75, 60), "wall_light")
wall_highlight = c.color((120, 95, 75), "wall_highlight")

# Floor
floor_dark = c.color((55, 40, 28), "floor_dark")
floor_mid = c.color((80, 58, 38), "floor_mid")
floor_light = c.color((100, 75, 50), "floor_light")

# Bottles - various colors
bottle_green = c.color((60, 100, 60), "bottle_green")
bottle_green_dark = c.color((40, 70, 40), "bottle_green_dark")
bottle_brown = c.color((100, 60, 40), "bottle_brown")
bottle_brown_dark = c.color((70, 40, 25), "bottle_brown_dark")
bottle_blue = c.color((50, 70, 100), "bottle_blue")
bottle_blue_dark = c.color((30, 50, 80), "bottle_blue_dark")
bottle_amber = c.color((180, 120, 40), "bottle_amber")
bottle_amber_dark = c.color((140, 90, 25), "bottle_amber_dark")
bottle_clear = c.color((180, 200, 220), "bottle_clear")
bottle_clear_tint = c.color((200, 220, 240), "bottle_clear_tint")

# Barrel colors
barrel_dark = c.color((85, 55, 30), "barrel_dark")
barrel_mid = c.color((120, 80, 45), "barrel_mid")
barrel_light = c.color((150, 100, 55), "barrel_light")
barrel_band = c.color((140, 120, 80), "barrel_band")
barrel_band_dark = c.color((100, 85, 50), "barrel_band_dark")

# Stool colors
stool_seat = c.color((100, 70, 45), "stool_seat")
stool_seat_dark = c.color((75, 50, 30), "stool_seat_dark")
stool_leg = c.color((60, 45, 30), "stool_leg")
stool_leg_dark = c.color((40, 30, 20), "stool_leg_dark")

# Glass colors
glass_body = c.color((160, 180, 200, 160), "glass_body")
glass_highlight = c.color((220, 240, 255, 200), "glass_highlight")
glass_rim = c.color((140, 160, 180), "glass_rim")

# Smoke/atmosphere
smoke_light = c.color((180, 170, 150, 70), "smoke_light")
smoke_mid = c.color((140, 130, 110, 50), "smoke_mid")
smoke_dark = c.color((100, 90, 80, 40), "smoke_dark")

# Outline
outline = c.color((25, 20, 15), "outline")
outline_light = c.color((50, 40, 30), "outline_light")

# Shadow colors
shadow = c.color((30, 25, 20, 180), "shadow")

# =====================
# BACKGROUND - walls with gradient
# =====================
# Back wall - dark to light gradient
c.rect(0, 0, 64, 38, wall_dark, fill=True)
c.rect(0, 8, 64, 25, wall_mid, fill=True)
c.rect(8, 12, 48, 18, wall_light, fill=True)
c.rect(12, 16, 40, 10, wall_highlight, fill=True)

# Wall planks/boards effect
for y in range(5, 35, 6):
    c.line(0, y, 64, y, outline_light)

# Floor - wooden planks with perspective
c.rect(0, 38, 64, 26, floor_dark, fill=True)
c.rect(0, 42, 64, 22, floor_mid, fill=True)
c.rect(5, 46, 54, 18, floor_light, fill=True)

# Floor plank lines
for y in range(40, 62, 4):
    c.line(0, y, 64, y, floor_dark)

# =====================
# BAR COUNTER
# =====================
# Main bar structure - extends from left to right
c.rect(4, 30, 52, 22, medium_wood, fill=True)
c.rect(4, 30, 52, 4, light_wood, fill=True)  # bar top surface
c.rect(6, 34, 48, 16, dark_wood, fill=True)  # front panel

# Bar top detail - wood grain
c.line(5, 31, 55, 31, pale_wood)
c.line(8, 32, 52, 32, light_wood)

# Bar edge highlights
c.line(4, 30, 56, 30, pale_wood)
c.line(4, 33, 56, 33, light_wood)

# Bar support legs
c.rect(8, 48, 6, 6, dark_wood, fill=True)
c.rect(46, 48, 6, 6, dark_wood, fill=True)

# =====================
# BAR STOOLS (3 stools)
# =====================
# Stool 1 (left)
c.rect(14, 52, 8, 4, stool_seat, fill=True)
c.rect(15, 52, 6, 2, stool_seat_dark, fill=True)  # seat top
c.line(16, 56, 16, 62, stool_leg)
c.line(20, 56, 20, 62, stool_leg)
c.line(16, 59, 20, 59, stool_leg_dark)  # foot rest

# Stool 2 (middle)
c.rect(28, 52, 8, 4, stool_seat, fill=True)
c.rect(29, 52, 6, 2, stool_seat_dark, fill=True)
c.line(30, 56, 30, 62, stool_leg)
c.line(34, 56, 34, 62, stool_leg)
c.line(30, 59, 34, 59, stool_leg_dark)

# Stool 3 (right)
c.rect(42, 52, 8, 4, stool_seat, fill=True)
c.rect(43, 52, 6, 2, stool_seat_dark, fill=True)
c.line(44, 56, 44, 62, stool_leg)
c.line(48, 56, 48, 62, stool_leg)
c.line(44, 59, 48, 59, stool_leg_dark)

# =====================
# SHELVES WITH BOTTLES
# =====================
# Shelf 1 (upper shelf)
c.rect(6, 6, 52, 3, dark_wood, fill=True)
c.rect(6, 6, 52, 1, barrel_band, fill=True)  # shelf edge

# Bottles on shelf 1
c.rect(10, 3, 4, 3, bottle_green, fill=True)
c.rect(11, 2, 2, 1, bottle_green_dark, fill=True)
c.rect(18, 3, 4, 3, bottle_brown, fill=True)
c.rect(19, 2, 2, 1, bottle_brown_dark, fill=True)
c.rect(26, 3, 4, 3, bottle_amber, fill=True)
c.rect(27, 2, 2, 1, bottle_amber_dark, fill=True)
c.rect(34, 3, 4, 3, bottle_blue, fill=True)
c.rect(35, 2, 2, 1, bottle_blue_dark, fill=True)
c.rect(42, 3, 4, 3, bottle_clear, fill=True)
c.rect(43, 2, 2, 1, bottle_clear_tint, fill=True)
c.rect(50, 3, 4, 3, bottle_green, fill=True)
c.rect(51, 2, 2, 1, bottle_green_dark, fill=True)

# Shelf 2 (lower shelf)
c.rect(6, 14, 52, 3, dark_wood, fill=True)
c.rect(6, 14, 52, 1, barrel_band, fill=True)

# Bottles on shelf 2
c.rect(8, 11, 4, 3, bottle_brown, fill=True)
c.rect(9, 10, 2, 1, bottle_brown_dark, fill=True)
c.rect(16, 11, 4, 3, bottle_green, fill=True)
c.rect(17, 10, 2, 1, bottle_green_dark, fill=True)
c.rect(24, 11, 4, 3, bottle_amber, fill=True)
c.rect(25, 10, 2, 1, bottle_amber_dark, fill=True)
c.rect(32, 11, 4, 3, bottle_blue, fill=True)
c.rect(33, 10, 2, 1, bottle_blue_dark, fill=True)
c.rect(40, 11, 4, 3, bottle_clear, fill=True)
c.rect(41, 10, 2, 1, bottle_clear_tint, fill=True)
c.rect(48, 11, 4, 3, bottle_brown, fill=True)
c.rect(49, 10, 2, 1, bottle_brown_dark, fill=True)
c.rect(54, 11, 3, 3, bottle_amber, fill=True)
c.rect(55, 10, 1, 1, bottle_amber_dark, fill=True)

# =====================
# HANGING LAMPS (3 lamps with glow)
# =====================
# Lamp 1 (left)
c.line(16, 0, 16, 2, outline)  # chain
c.rect(14, 2, 4, 3, lamp_glow, fill=True)
c.rect(15, 3, 2, 1, lamp_yellow, fill=True)
c.set(15, 3, lamp_core)
c.rect(13, 5, 6, 2, warm_light, fill=True)
c.rect(12, 7, 8, 2, warm_orange, fill=True)

# Lamp 2 (center)
c.line(32, 0, 32, 2, outline)
c.rect(30, 2, 4, 3, lamp_glow, fill=True)
c.rect(31, 3, 2, 1, lamp_yellow, fill=True)
c.set(31, 3, lamp_core)
c.rect(29, 5, 6, 2, warm_light, fill=True)
c.rect(28, 7, 8, 2, warm_orange, fill=True)

# Lamp 3 (right)
c.line(48, 0, 48, 2, outline)
c.rect(46, 2, 4, 3, lamp_glow, fill=True)
c.rect(47, 3, 2, 1, lamp_yellow, fill=True)
c.set(47, 3, lamp_core)
c.rect(45, 5, 6, 2, warm_light, fill=True)
c.rect(44, 7, 8, 2, warm_orange, fill=True)

# =====================
# BARRELS (2 barrels on floor right side)
# =====================
# Barrel 1 (larger, left)
c.ellipse(52, 54, 6, 7, barrel_mid, fill=True)
c.rect(48, 50, 8, 2, barrel_band, fill=True)
c.rect(48, 55, 8, 2, barrel_band_dark, fill=True)
c.rect(48, 59, 8, 2, barrel_band, fill=True)
c.rect(48, 52, 2, 6, barrel_dark, fill=True)

# Barrel 2 (smaller, right)
c.ellipse(60, 56, 4, 5, barrel_light, fill=True)
c.rect(58, 53, 6, 2, barrel_band, fill=True)
c.rect(58, 57, 6, 2, barrel_band_dark, fill=True)

# =====================
# GLASSES ON BAR (4 glasses with liquid)
# =====================
# Glass 1 - with amber liquid
c.rect(12, 27, 4, 5, glass_body, fill=True)
c.rect(12, 29, 4, 3, bottle_amber, fill=True)
c.rect(13, 27, 1, 2, glass_highlight, fill=True)
c.line(12, 27, 15, 27, glass_rim)

# Glass 2 - empty
c.rect(22, 27, 4, 5, glass_body, fill=True)
c.rect(23, 27, 1, 2, glass_highlight, fill=True)
c.line(22, 27, 25, 27, glass_rim)

# Glass 3 - with green liquid
c.rect(32, 27, 4, 5, glass_body, fill=True)
c.rect(32, 29, 4, 3, bottle_green, fill=True)
c.rect(33, 27, 1, 2, glass_highlight, fill=True)
c.line(32, 27, 35, 27, glass_rim)

# Glass 4 - tall glass
c.rect(44, 26, 4, 6, glass_body, fill=True)
c.rect(44, 29, 4, 3, bottle_brown, fill=True)
c.rect(45, 26, 1, 2, glass_highlight, fill=True)
c.line(44, 26, 47, 26, glass_rim)

# =====================
# SMOKE/ATMOSPHERE
# =====================
c.rect(10, 8, 5, 2, smoke_light, fill=True)
c.rect(26, 9, 5, 2, smoke_light, fill=True)
c.rect(42, 8, 5, 2, smoke_light, fill=True)
c.rect(18, 16, 6, 2, smoke_mid, fill=True)
c.rect(35, 18, 5, 2, smoke_mid, fill=True)
c.rect(8, 22, 4, 2, smoke_dark, fill=True)
c.rect(50, 20, 4, 2, smoke_dark, fill=True)

# =====================
# DARK OUTLINES
# =====================
# Bar counter outline
c.line(4, 30, 56, 30, outline)
c.line(4, 30, 4, 52, outline)
c.line(56, 30, 56, 52, outline)
c.line(4, 52, 56, 52, outline)

# Shelf outlines
c.line(6, 6, 58, 6, outline)
c.line(6, 9, 58, 9, outline)
c.line(6, 14, 58, 14, outline)
c.line(6, 17, 58, 17, outline)

# Floor/wall division
c.line(0, 38, 64, 38, outline)

# Wall edges
c.line(0, 0, 0, 38, outline)
c.line(63, 0, 63, 38, outline)

# =====================
# Additional atmosphere and details
# =====================
# Light spill on bar surface
c.rect(13, 30, 5, 2, warm_light, fill=True)
c.rect(29, 30, 5, 2, warm_light, fill=True)
c.rect(45, 30, 5, 2, warm_light, fill=True)

# Shadows under bar stools
c.rect(14, 61, 8, 2, shadow, fill=True)
c.rect(28, 61, 8, 2, shadow, fill=True)
c.rect(42, 61, 8, 2, shadow, fill=True)

# More smoke near ceiling corners
c.rect(2, 2, 6, 3, smoke_light, fill=True)
c.rect(56, 2, 6, 3, smoke_light, fill=True)

# Candle on bar
c.rect(38, 28, 3, 3, c.color((255, 240, 200), "candle"), fill=True)
c.set(39, 27, lamp_core)  # flame

# Mug on bar
c.rect(20, 28, 4, 4, c.color((120, 80, 50), "mug"), fill=True)
c.rect(21, 29, 2, 3, bottle_amber, fill=True)  # beer

print(c.stats_text())
print(f"Color count: {len(c.palette())}")

finish(c)
