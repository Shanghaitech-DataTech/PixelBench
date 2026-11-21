from pixelbench_api import *

# Summer seaside, rendered directly at native pixel resolution.
c = new_canvas(128, 128, background="#79d8f2", name="summer-seaside")

# Compact daylight palette.
sky = "#79d8f2"
sky_hi = "#9ce8f6"
white = "#fffdf0"
cloud_shade = "#d9f3f3"
sun = "#ffd84a"
sun_hi = "#fff27a"
horizon = "#176fb5"
deep = "#187fc1"
midsea = "#159fbd"
teal = "#20b8ba"
sea_light = "#61d6ce"
foam = "#fffbea"
foam_shadow = "#ccebdc"
sand = "#f2c76f"
sand_hi = "#ffdb83"
sand_shadow = "#dba956"
sand_dark = "#be873d"
red_dark = "#b82936"
red = "#e54645"
red_hi = "#ff7060"
navy = "#16435d"
wood = "#8b5d38"
towel_blue = "#2f83c5"
towel_light = "#64c9d2"
sole = "#f05a50"
strap = "#9d2f3d"

# Subtle sky bands.
c.rect(0, 31, 128, 23, sky_hi)

# Sun with crisp halo rays and a warm pixel disc.
c.rect(103, 5, 2, 6, sun_hi)
c.rect(103, 31, 2, 6, sun_hi)
c.rect(87, 20, 7, 2, sun_hi)
c.rect(114, 20, 7, 2, sun_hi)
c.line(92, 9, 96, 13, sun_hi)
c.line(113, 10, 110, 13, sun_hi)
c.line(92, 32, 96, 28, sun_hi)
c.line(113, 32, 110, 28, sun_hi)
c.circle(104, 21, 10, sun)
c.circle(101, 18, 5, sun_hi)

# Soft stepped clouds.
c.rect(8, 18, 37, 7, white)
c.rect(13, 14, 12, 13, white)
c.rect(25, 11, 11, 16, white)
c.rect(36, 17, 15, 10, white)
c.rect(9, 25, 38, 3, cloud_shade)
c.rect(16, 25, 9, 2, white)
c.rect(58, 35, 26, 5, white)
c.rect(63, 31, 10, 10, white)
c.rect(72, 33, 8, 8, white)
c.rect(59, 40, 22, 2, cloud_shade)

# Two distant gulls, simple dark-blue wing marks.
c.line(60, 18, 63, 16, navy)
c.line(63, 16, 67, 19, navy)
c.set(63, 17, sky)
c.line(76, 26, 79, 24, navy)
c.line(79, 24, 83, 27, navy)
c.set(79, 25, sky)

# Calm sea bands and bright glints.
c.rect(0, 54, 128, 7, horizon)
c.rect(0, 61, 128, 9, deep)
c.rect(0, 70, 128, 9, midsea)
c.rect(0, 79, 128, 10, teal)
c.rect(0, 87, 128, 8, sea_light)
c.rect(7, 64, 18, 2, "#5fc8d6")
c.rect(35, 57, 15, 1, "#a0e5eb")
c.rect(78, 66, 19, 2, "#57cad2")
c.rect(103, 73, 17, 2, "#70ded7")
c.rect(19, 76, 20, 2, "#7be1d7")
c.rect(51, 82, 22, 2, "#94e7dc")

# Tiny sailboat at the horizon.
c.rect(89, 52, 14, 1, navy)
c.poly([(94, 52), (94, 42), (86, 51)], white)
c.poly([(95, 43), (96, 52), (103, 52)], "#f6d965")
c.rect(94, 41, 1, 12, navy)
c.poly([(87, 53), (104, 53), (101, 57), (91, 57)], red_dark)
c.rect(91, 57, 10, 1, "#8fe3e2")

# Golden beach base.
c.rect(0, 92, 128, 36, sand)
c.poly([(0, 91), (20, 89), (39, 92), (61, 88), (84, 92), (105, 87), (127, 90), (127, 99), (0, 99)], foam_shadow)
c.poly([(0, 88), (19, 86), (38, 89), (58, 85), (82, 89), (103, 84), (127, 87), (127, 94), (108, 92), (91, 96), (68, 92), (49, 96), (24, 92), (0, 96)], foam)
# Broken foamy wavelets.
c.rect(3, 83, 15, 2, foam)
c.rect(9, 85, 19, 2, foam)
c.rect(32, 85, 13, 2, foam)
c.rect(65, 82, 18, 2, foam)
c.rect(90, 81, 15, 2, foam)
c.rect(111, 80, 12, 2, foam)

# Sand highlights, dimples and tiny shell marks.
c.rect(2, 105, 18, 2, sand_hi)
c.rect(90, 103, 20, 2, sand_hi)
c.rect(25, 119, 13, 2, sand_shadow)
c.rect(103, 121, 17, 2, sand_shadow)
c.set(15, 112, sand_dark); c.set(16, 112, sand_dark); c.set(14, 113, sand_dark)
c.set(85, 116, sand_dark); c.set(86, 115, sand_dark)
c.line(114, 109, 118, 107, white); c.line(118, 107, 121, 109, white)
c.rect(117, 109, 2, 1, sand_dark)

# Umbrella shadow on the sand.
c.ellipse(48, 112, 34, 6, "#d29d52")
c.rect(23, 110, 50, 4, "#d29d52")

# Umbrella pole, outlined for contrast.
c.rect(47, 68, 4, 45, navy)
c.rect(48, 69, 2, 44, white)
c.rect(47, 111, 11, 3, navy)

# Large red-and-white striped canopy with a stepped dark outline.
canopy = [(13, 68), (16, 62), (22, 57), (31, 53), (42, 51), (53, 52), (64, 56), (72, 62), (76, 69), (68, 67), (60, 70), (51, 67), (42, 70), (32, 67), (22, 70)]
c.poly(canopy, navy)
# Colored interior stripes fan toward the pole.
c.poly([(15, 67), (18, 62), (23, 58), (31, 54), (39, 53), (34, 66), (22, 68)], red)
c.poly([(31, 54), (40, 52), (48, 53), (48, 66), (42, 68), (34, 66)], white)
c.poly([(48, 53), (56, 54), (64, 58), (70, 63), (73, 67), (61, 68), (53, 66), (48, 66)], red)
c.poly([(64, 58), (70, 62), (74, 67), (69, 66), (61, 68), (56, 66)], white)
# Scalloped valance and sunlit stripe.
c.rect(22, 67, 11, 3, red_dark)
c.rect(42, 67, 10, 3, white)
c.rect(60, 67, 9, 3, red_dark)
c.line(21, 61, 31, 56, red_hi)

# Striped towel in lower-right foreground, lying flat in perspective.
c.poly([(74, 97), (105, 100), (112, 119), (79, 116)], "#24729f")
c.poly([(75, 98), (104, 101), (106, 106), (76, 103)], towel_light)
c.poly([(76, 104), (106, 107), (108, 112), (77, 109)], white)
c.poly([(78, 110), (108, 113), (110, 118), (79, 115)], towel_blue)
c.line(81, 116, 81, 119, towel_blue); c.line(85, 116, 85, 120, white)
c.line(104, 118, 104, 121, white); c.line(108, 118, 108, 121, towel_blue)

# Flip-flops near the towel, with clear inset soles and Y straps.
c.poly([(55, 105), (60, 102), (65, 105), (65, 113), (61, 120), (56, 117), (54, 109)], strap)
c.poly([(57, 105), (60, 104), (63, 106), (63, 113), (60, 118), (57, 116), (56, 109)], sole)
c.poly([(65, 112), (69, 108), (74, 110), (76, 118), (72, 124), (67, 122), (64, 117)], strap)
c.poly([(67, 112), (69, 110), (72, 111), (74, 118), (71, 122), (68, 121), (66, 117)], "#f67f58")
c.line(57, 107, 60, 111, strap); c.line(63, 107, 60, 111, strap); c.line(60, 111, 60, 115, strap)
c.line(67, 113, 70, 116, strap); c.line(73, 113, 70, 116, strap); c.line(70, 116, 71, 120, strap)

# A few foreground grains over the shadow for texture.
c.set(8, 123, sand_dark); c.set(9, 122, sand_dark)
c.set(44, 119, sand_hi); c.set(46, 120, sand_hi)

result = c
view(result, scale=4, margin=0)
finish(result)
