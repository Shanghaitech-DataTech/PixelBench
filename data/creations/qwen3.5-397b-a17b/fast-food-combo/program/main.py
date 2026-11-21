from pixelbench_api import new_canvas, finish

# Create 64x64 canvas
c = new_canvas(64, 64, name="fast_food_combo")

# Define color palette
# Tray colors
tray_light = c.color("#C0C0C0", "tray_light")
tray_mid = c.color("#909090", "tray_mid")
tray_dark = c.color("#606060", "tray_dark")
tray_shadow = c.color("#404040", "tray_shadow")

# Burger bun colors
bun_top = c.color("#D4A574", "bun_top")
bun_mid = c.color("#C49464", "bun_mid")
bun_bottom = c.color("#B48454", "bun_bottom")
bun_shadow = c.color("#947444", "bun_shadow")
sesame = c.color("#F0E0C0", "sesame")

# Lettuce colors
lettuce_light = c.color("#90D070", "lettuce_light")
lettuce_mid = c.color("#70B050", "lettuce_mid")
lettuce_dark = c.color("#509030", "lettuce_dark")

# Cheese colors
cheese_light = c.color("#FFD040", "cheese_light")
cheese_mid = c.color("#FFC030", "cheese_mid")
cheese_shadow = c.color("#E0A020", "cheese_shadow")

# Patty colors
patty_top = c.color("#6B4423", "patty_top")
patty_mid = c.color("#5B3413", "patty_mid")
patty_shadow = c.color("#4B2403", "patty_shadow")

# Fries colors
fries_light = c.color("#F0D060", "fries_light")
fries_mid = c.color("#E0C050", "fries_mid")
fries_shadow = c.color("#C0A030", "fries_shadow")

# Fries carton colors
carton_red = c.color("#D03030", "carton_red")
carton_dark = c.color("#A02020", "carton_dark")
carton_white = c.color("#FFFFFF", "carton_white")

# Chicken nugget colors
nugget_light = c.color("#D4B060", "nugget_light")
nugget_mid = c.color("#C4A050", "nugget_mid")
nugget_shadow = c.color("#A48030", "nugget_shadow")

# Cola cup colors
cup_clear = c.color("#E0F0FF", "cup_clear")
cup_shadow = c.color("#B0D0E0", "cup_shadow")
cola_dark = c.color("#301000", "cola_dark")
cola_mid = c.color("#502000", "cola_mid")
ice_white = c.color("#FFFFFF", "ice_white")
ice_blue = c.color("#D0E8F0", "ice_blue")
straw_red = c.color("#FF4040", "straw_red")
straw_white = c.color("#FFFFFF", "straw_white")

# Sauce colors
sauce_red = c.color("#CC3333", "sauce_red")
sauce_yellow = c.color("#FFCC33", "sauce_yellow")
sauce_white = c.color("#F0F0F0", "sauce_white")
sauce_cup = c.color("#D0D0D0", "sauce_cup")

# Outline color
outline = c.color("#202020", "outline")

# Draw tray (isometric rectangle at bottom)
# Tray base
c.rect(8, 44, 48, 12, tray_light, fill=True)
c.rect(10, 46, 44, 8, tray_mid, fill=True)
c.rect(12, 48, 40, 4, tray_dark, fill=True)

# Tray rim
c.line(8, 44, 56, 44, tray_shadow)
c.line(8, 44, 8, 56, tray_shadow)
c.line(56, 44, 56, 56, tray_shadow)
c.line(8, 56, 56, 56, tray_shadow)

# === CHEESEBURGER (left side) ===
# Bottom bun
c.ellipse(18, 38, 10, 6, bun_bottom, fill=True)
c.ellipse(18, 36, 10, 6, bun_mid, fill=True)

# Patty
c.ellipse(18, 32, 9, 5, patty_shadow, fill=True)
c.ellipse(18, 30, 9, 5, patty_mid, fill=True)
c.ellipse(18, 28, 9, 5, patty_top, fill=True)

# Melted cheese (dripping)
c.ellipse(18, 26, 10, 4, cheese_shadow, fill=True)
c.ellipse(18, 24, 10, 4, cheese_mid, fill=True)
c.ellipse(18, 22, 10, 4, cheese_light, fill=True)
# Cheese drips
c.set(14, 26, cheese_mid)
c.set(22, 26, cheese_mid)
c.set(16, 27, cheese_light)
c.set(20, 27, cheese_light)

# Lettuce (ruffled edges)
c.ellipse(18, 20, 11, 4, lettuce_dark, fill=True)
c.ellipse(18, 18, 11, 4, lettuce_mid, fill=True)
c.ellipse(18, 16, 11, 4, lettuce_light, fill=True)
# Lettuce ruffles
for x in range(10, 26, 2):
    c.set(x, 15, lettuce_light)

# Top bun with sesame seeds
c.ellipse(18, 12, 10, 5, bun_shadow, fill=True)
c.ellipse(18, 10, 10, 5, bun_bottom, fill=True)
c.ellipse(18, 8, 10, 5, bun_mid, fill=True)
c.ellipse(18, 6, 10, 5, bun_top, fill=True)

# Sesame seeds
c.set(14, 5, sesame)
c.set(16, 4, sesame)
c.set(18, 5, sesame)
c.set(20, 4, sesame)
c.set(22, 5, sesame)
c.set(15, 7, sesame)
c.set(19, 7, sesame)
c.set(21, 6, sesame)

# === FRENCH FRIES (center-back) ===
# Fries carton
c.rect(30, 30, 12, 14, carton_red, fill=True)
c.rect(31, 31, 10, 12, carton_dark, fill=True)
# Carton top rim
c.line(30, 30, 42, 30, carton_white)
c.rect(30, 29, 12, 2, carton_red, fill=True)

# Fries sticking out
# Left cluster
c.line(31, 29, 31, 20, fries_shadow)
c.line(32, 29, 32, 18, fries_mid)
c.line(33, 29, 33, 22, fries_light)
c.line(34, 29, 34, 19, fries_mid)
# Right cluster
c.line(37, 29, 37, 21, fries_light)
c.line(38, 29, 38, 17, fries_mid)
c.line(39, 29, 39, 20, fries_shadow)
c.line(40, 29, 40, 18, fries_light)
# Center fries
c.line(35, 29, 35, 16, fries_light)
c.line(36, 29, 36, 19, fries_mid)

# === CHICKEN NUGGETS (front right) ===
# Nugget 1
c.ellipse(44, 42, 5, 3, nugget_shadow, fill=True)
c.ellipse(44, 40, 5, 3, nugget_mid, fill=True)
c.ellipse(44, 38, 5, 3, nugget_light, fill=True)
# Nugget texture
c.set(42, 40, nugget_mid)
c.set(44, 39, nugget_shadow)
c.set(46, 40, nugget_mid)

# Nugget 2
c.ellipse(50, 44, 4, 3, nugget_shadow, fill=True)
c.ellipse(50, 42, 4, 3, nugget_mid, fill=True)
c.ellipse(50, 40, 4, 3, nugget_light, fill=True)
c.set(48, 42, nugget_mid)
c.set(50, 41, nugget_shadow)
c.set(52, 42, nugget_mid)

# Nugget 3
c.ellipse(47, 48, 4, 3, nugget_shadow, fill=True)
c.ellipse(47, 46, 4, 3, nugget_mid, fill=True)
c.ellipse(47, 44, 4, 3, nugget_light, fill=True)
c.set(45, 46, nugget_mid)
c.set(47, 45, nugget_shadow)
c.set(49, 46, nugget_mid)

# === COLA CUP (back right) ===
# Cup body (tapered)
c.rect(48, 18, 12, 18, cup_clear, fill=True)
c.rect(49, 19, 10, 16, cup_shadow, fill=True)
# Cup rim
c.ellipse(54, 18, 6, 2, cup_clear, fill=True)

# Cola inside
c.ellipse(54, 20, 5, 3, cola_dark, fill=True)
c.ellipse(54, 22, 4, 2, cola_mid, fill=True)

# Ice cubes
c.rect(51, 19, 2, 2, ice_white, fill=True)
c.rect(54, 19, 2, 2, ice_blue, fill=True)
c.rect(56, 20, 2, 2, ice_white, fill=True)
c.set(53, 21, ice_blue)
c.set(55, 21, ice_white)

# Straw
c.line(54, 18, 54, 12, straw_white)
c.line(54, 12, 57, 10, straw_red)
c.line(57, 10, 59, 10, straw_red)

# === SAUCE CUPS (front left) ===
# Sauce cup 1 (red sauce)
c.ellipse(14, 50, 4, 2, sauce_cup, fill=True)
c.ellipse(14, 49, 3, 2, sauce_red, fill=True)

# Sauce cup 2 (yellow sauce)
c.ellipse(22, 52, 4, 2, sauce_cup, fill=True)
c.ellipse(22, 51, 3, 2, sauce_yellow, fill=True)

# Sauce cup 3 (white sauce)
c.ellipse(18, 54, 4, 2, sauce_cup, fill=True)
c.ellipse(18, 53, 3, 2, sauce_white, fill=True)

# === OUTLINES ===
# Add dark outlines to key elements for definition

# Tray outline
c.line(8, 44, 56, 44, outline)
c.line(56, 44, 56, 56, outline)
c.line(8, 56, 56, 56, outline)
c.line(8, 44, 8, 56, outline)

# Burger outline
c.poly([(8, 12), (12, 8), (24, 8), (28, 12), (28, 38), (24, 42), (12, 42), (8, 38)], outline, fill=False)

# Fries carton outline
c.line(30, 30, 30, 44, outline)
c.line(42, 30, 42, 44, outline)
c.line(30, 44, 42, 44, outline)

# Cola cup outline
c.line(48, 18, 48, 36, outline)
c.line(60, 18, 60, 36, outline)
c.line(48, 36, 60, 36, outline)

# Nugget outlines
c.poly([(40, 38), (44, 36), (48, 38), (48, 44), (44, 46), (40, 44)], outline, fill=False)
c.poly([(46, 40), (50, 38), (54, 40), (54, 46), (50, 48), (46, 46)], outline, fill=False)
c.poly([(43, 44), (47, 42), (51, 44), (51, 50), (47, 52), (43, 50)], outline, fill=False)

# Sauce cup outlines
c.poly([(11, 48), (14, 47), (17, 48), (17, 52), (14, 53), (11, 52)], outline, fill=False)
c.poly([(19, 50), (22, 49), (25, 50), (25, 54), (22, 55), (19, 54)], outline, fill=False)
c.poly([(15, 52), (18, 51), (21, 52), (21, 56), (18, 57), (15, 56)], outline, fill=False)

# Check stats
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

# Submit
finish(c)
