from pixelbench_api import new_canvas, finish

# Create a 32x32 canvas for the forest slime monster
c = new_canvas(32, 32, name="forest_slime")

# Define colors (keeping under 86 visible colors)
slime_base = c.color("#5a9f7f", "slime_base")      # Main slime body - brighter green
slime_dark = c.color("#3a6f5f", "slime_dark")      # Shadow areas
slime_light = c.color("#7fcfbf", "slime_light")    # Highlights
slime_glow = c.color("#9fffdF", "slime_glow")      # Inner glow
moss_green = c.color("#4a7b4a", "moss_green")      # Moss patches
moss_dark = c.color("#2a4a2a", "moss_dark")        # Dark moss
antler_brown = c.color("#9a7b5a", "antler_brown")  # Tiny antlers
antler_light = c.color("#ba9b7a", "antler_light")  # Antler highlight
eye_white = c.color("#ffffff", "eye_white")        # Eye white
eye_glow = c.color("#ffffaa", "eye_glow")          # Glowing yellow eyes
eye_pupil = c.color("#1a1a3a", "eye_pupil")        # Dark pupil with blue tint
blush = c.color("#ffaaaa", "blush")                # Cute blush
mushroom_red = c.color("#e04a4a", "mushroom_red")  # Mushroom cap
mushroom_white = c.color("#ffffff", "mushroom_white")  # Mushroom spots
mushroom_stem = c.color("#f0e0d0", "mushroom_stem")  # Mushroom stem

# Draw the main slime body (compact blob shape, front-facing)
# More rounded and cute
c.poly([
    (7, 26), (5, 24), (4, 21), (4, 17), (5, 13),
    (7, 9), (10, 6), (14, 4), (18, 6), (22, 9),
    (25, 13), (27, 17), (28, 21), (27, 24), (25, 26),
    (16, 27)
], slime_base, fill=True)

# Add shadow/darker areas on the slime (bottom and sides)
c.poly([
    (9, 24), (7, 22), (6, 19), (7, 16), (9, 14),
    (12, 12), (16, 11), (20, 12), (23, 14), (25, 16),
    (26, 19), (25, 22), (23, 24), (16, 25)
], slime_dark, fill=True)

# Add highlights on the slime (top-left areas)
c.poly([
    (11, 7), (13, 5), (15, 5), (17, 7), (16, 9),
    (14, 10), (12, 9)
], slime_light, fill=True)

# Inner glow effect (center)
c.poly([
    (13, 11), (15, 10), (17, 11), (17, 13), (15, 14), (13, 13)
], slime_glow, fill=True)

# Draw moss patches on the slime body
# Left side moss
c.poly([(5, 17), (7, 16), (8, 18), (7, 20), (5, 19)], moss_green, fill=True)
c.set(6, 18, moss_dark)

# Right side moss  
c.poly([(24, 17), (26, 16), (27, 18), (26, 20), (24, 19)], moss_green, fill=True)
c.set(25, 18, moss_dark)

# Top moss near head area
c.poly([(11, 6), (13, 5), (15, 6), (14, 8), (12, 8)], moss_green, fill=True)

# Bottom moss patches
c.poly([(8, 23), (10, 22), (11, 24), (10, 25), (8, 24)], moss_green, fill=True)
c.poly([(21, 23), (23, 22), (24, 24), (23, 25), (21, 24)], moss_green, fill=True)

# Draw tiny antlers (small delicate branches from top of head)
# Left antler - small branch
c.set(12, 4, antler_brown)
c.set(11, 3, antler_brown)
c.set(10, 2, antler_brown)
c.set(11, 2, antler_light)

# Right antler - small branch
c.set(20, 4, antler_brown)
c.set(21, 3, antler_brown)
c.set(22, 2, antler_brown)
c.set(21, 2, antler_light)

# Draw large cute glowing eyes (front-facing, expressive)
# Left eye - white base (larger for cuteness)
c.circle(11, 15, 3, eye_white, fill=True)
# Left eye - glow
c.circle(11, 15, 2, eye_glow, fill=True)
# Left eye - pupil (looking slightly inward for cute expression)
c.set(11, 15, eye_pupil)
c.set(12, 15, eye_pupil)
c.set(11, 16, eye_pupil)
c.set(12, 16, eye_pupil)

# Right eye - white base
c.circle(21, 15, 3, eye_white, fill=True)
# Right eye - glow
c.circle(21, 15, 2, eye_glow, fill=True)
# Right eye - pupil (looking slightly inward)
c.set(20, 15, eye_pupil)
c.set(21, 15, eye_pupil)
c.set(20, 16, eye_pupil)
c.set(21, 16, eye_pupil)

# Add sparkle highlights in eyes (makes them look alive)
c.set(10, 14, eye_white)
c.set(22, 14, eye_white)

# Draw cute smiling mouth
c.set(14, 21, slime_dark)
c.set(15, 22, slime_dark)
c.set(16, 22, slime_dark)
c.set(17, 22, slime_dark)
c.set(18, 21, slime_dark)

# Add blush marks (cute expression, below eyes)
c.set(9, 19, blush)
c.set(10, 19, blush)
c.set(22, 19, blush)
c.set(23, 19, blush)

# Draw small red mushroom on the BACK (top-center of slime)
# Mushroom stem
c.set(15, 3, mushroom_stem)
c.set(16, 3, mushroom_stem)
c.set(15, 4, mushroom_stem)
c.set(16, 4, mushroom_stem)

# Mushroom cap (red dome with white spots)
c.poly([
    (13, 3), (14, 1), (16, 0), (18, 1), (19, 3),
    (19, 4), (18, 5), (14, 5), (13, 4)
], mushroom_red, fill=True)

# White spots on mushroom cap
c.set(14, 2, mushroom_white)
c.set(18, 2, mushroom_white)
c.set(16, 1, mushroom_white)

# Add some texture/detail to the slime body
# Small highlights scattered
c.set(8, 15, slime_light)
c.set(24, 15, slime_light)
c.set(10, 22, slime_light)

# Edge definition for better readability
c.set(5, 13, slime_dark)
c.set(27, 13, slime_dark)
c.set(7, 9, slime_dark)
c.set(25, 9, slime_dark)

print(c.stats_text())
print(c.matrix_text())

finish(c)
