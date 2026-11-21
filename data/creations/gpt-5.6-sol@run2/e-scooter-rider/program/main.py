from pixelbench_api import *

# 32x32 transparent pixel-art sprite
result = new_canvas(32, 32, background=None, name="e-scooter-rider")

# Compact palette
outline = result.color("#172431", "outline")
tire = result.color("#101820", "tire")
rubber_hi = result.color("#314353", "rubber highlight")
metal = result.color("#5f7480", "metal")
metal_hi = result.color("#a7c2c8", "metal highlight")
teal_dark = result.color("#087f87", "scooter dark")
teal = result.color("#11b6b6", "scooter")
teal_hi = result.color("#7be5d6", "scooter highlight")
yellow_dark = result.color("#d98b1c", "helmet shadow")
yellow = result.color("#ffc83d", "helmet")
yellow_hi = result.color("#fff08a", "helmet highlight")
skin_dark = result.color("#b95f43", "skin shadow")
skin = result.color("#ef9a6c", "skin")
skin_hi = result.color("#ffd0a3", "skin highlight")
coral_dark = result.color("#ad3f4b", "jacket shadow")
coral = result.color("#ed5b5f", "jacket")
coral_hi = result.color("#ff8a72", "jacket highlight")
pants = result.color("#31516f", "pants")
pants_hi = result.color("#4f7590", "pants highlight")
shoe = result.color("#21313d", "shoe")
white = result.color("#eaf7ef", "light")

# Small motion streaks behind the rider
result.rect(2, 13, 4, 1, metal_hi)
result.rect(1, 16, 5, 1, teal_hi)
result.rect(3, 19, 3, 1, metal_hi)

# Wheels, outlined and chunky
for cx in (8, 25):
    result.circle(cx, 27, 4, tire)
    result.circle(cx, 27, 2, rubber_hi)
    result.circle(cx, 27, 1, metal_hi)
    result.set(cx, 27, outline)
# Wheel shine pixels
result.set(7, 24, metal)
result.set(24, 24, metal)

# Scooter deck: dark undercarriage, turquoise top rail
result.poly([(6, 21), (22, 21), (24, 23), (22, 25), (8, 25), (6, 23)], outline)
result.rect(7, 21, 15, 2, teal)
result.rect(9, 21, 10, 1, teal_hi)
result.rect(9, 23, 13, 1, teal_dark)
result.set(23, 23, metal_hi)

# Front fork and angled stem
result.line(25, 25, 25, 22, outline)
result.line(24, 23, 26, 11, outline)
result.line(25, 22, 27, 11, teal_dark)
result.line(26, 21, 28, 11, teal)
result.set(27, 15, teal_hi)
# Handlebar and controls
result.rect(24, 9, 6, 2, outline)
result.rect(25, 9, 4, 1, metal_hi)
result.rect(28, 10, 2, 2, outline)
result.set(28, 10, teal)

# Rider rear leg, bent toward the back of the deck
result.poly([(12, 17), (16, 18), (13, 21), (10, 23), (7, 23), (7, 21), (10, 20)], outline)
result.poly([(12, 18), (14, 19), (12, 20), (10, 22), (8, 22), (10, 19)], pants)
result.set(11, 19, pants_hi)
# Rear shoe resting near deck tail
result.rect(6, 22, 6, 3, outline)
result.rect(7, 22, 4, 1, white)

# Front/standing leg, knee angled forward and foot planted
result.poly([(14, 17), (18, 18), (18, 21), (21, 22), (22, 24), (16, 24), (15, 21), (13, 20)], outline)
result.poly([(15, 18), (17, 19), (17, 21), (20, 22), (17, 23), (15, 20)], pants)
result.set(16, 19, pants_hi)
result.set(17, 20, pants_hi)
# Front shoe
result.rect(18, 22, 6, 3, outline)
result.rect(19, 22, 4, 1, white)
result.set(23, 23, metal_hi)

# Leaning torso and jacket
result.poly([(10, 10), (15, 10), (18, 13), (17, 19), (12, 19), (9, 15)], outline)
result.poly([(11, 11), (14, 11), (16, 13), (16, 18), (12, 18), (10, 15)], coral)
result.poly([(11, 11), (13, 11), (12, 17), (10, 15)], coral_hi)
result.rect(14, 16, 2, 2, coral_dark)
result.set(16, 14, coral_dark)

# Extended arm: sleeve, forearm, and gripping hand
result.poly([(14, 11), (17, 11), (20, 14), (19, 16), (16, 14)], outline)
result.poly([(15, 12), (17, 12), (19, 14), (18, 15), (16, 13)], coral)
result.set(16, 12, coral_hi)
result.line(19, 14, 23, 11, outline)
result.line(20, 14, 24, 10, skin)
result.set(21, 12, skin_hi)
result.rect(23, 9, 3, 3, outline)
result.rect(24, 9, 2, 2, skin)

# Neck
result.rect(12, 8, 4, 4, outline)
result.rect(13, 8, 2, 3, skin_dark)
result.set(14, 9, skin)

# Head in profile, nose pointing right
result.poly([(10, 4), (15, 3), (18, 5), (18, 7), (20, 8), (18, 10), (14, 10), (11, 8)], outline)
result.poly([(12, 5), (16, 5), (17, 6), (17, 8), (19, 8), (17, 9), (14, 9), (12, 8)], skin)
result.set(16, 6, skin_hi)
result.set(18, 8, skin_hi)
result.set(17, 7, outline)

# Bright helmet with visor and lower strap
result.poly([(9, 4), (11, 2), (15, 2), (18, 4), (18, 6), (11, 6), (9, 5)], outline)
result.poly([(10, 4), (12, 3), (15, 3), (17, 4), (17, 5), (10, 5)], yellow)
result.rect(12, 3, 3, 1, yellow_hi)
result.rect(10, 5, 3, 2, yellow_dark)
result.line(12, 6, 13, 9, outline)
result.set(13, 8, yellow_dark)
# Visor brim
result.rect(16, 5, 4, 2, outline)
result.rect(17, 5, 2, 1, yellow)

# Tiny jacket zipper highlight
result.set(13, 13, white)
result.set(13, 14, white)

view(result, scale=16, margin=0)
finish(result)
