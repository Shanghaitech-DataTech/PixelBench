# University laboratory workbench, 64x64 pixel art
result = new_canvas(64, 64, background="#d7ded8", name="university-laboratory-workbench")

# Palette
outline = "#202b35"
dark = "#34444d"
shadow = "#52636a"
steel = "#8da0a4"
lightsteel = "#c3d0ce"
white = "#f4f2df"
paper = "#fff9db"
wall = "#d7ded8"
wall_shadow = "#b9c8c3"
tile = "#9fb3ae"
wood = "#8e6043"
wood_light = "#b47b51"
wood_dark = "#5f4033"
glass = "#bde8e5"
glass_hi = "#eafff7"
blue = "#3489a8"
blue_dark = "#23627b"
cyan = "#62c7c4"
red = "#d9534f"
yellow = "#e7b94b"
green = "#5a9b67"
purple = "#7b659c"
ink = "#55759b"

# Tiled laboratory wall
result.rect(0, 0, 64, 39, wall)
for y in (10, 20, 30):
    result.line(0, y, 63, y, wall_shadow)
for x in (15, 31, 47):
    result.line(x, 0, x, 39, wall_shadow)
# offset tile joints
for x in (7, 23, 39, 55):
    result.set(x, 10, tile); result.set(x, 30, tile)
# hanging shelf
result.rect(3, 5, 28, 2, outline)
result.rect(4, 3, 2, 3, dark); result.rect(28, 3, 2, 3, dark)
# small shelf bottles
result.rect(8, 1, 5, 4, blue_dark); result.rect(9, 0, 3, 1, outline); result.rect(9, 3, 3, 2, glass)
result.rect(17, 2, 5, 3, green); result.rect(18, 1, 3, 1, outline); result.rect(18, 3, 3, 1, white)
result.rect(25, 1, 3, 4, purple); result.rect(25, 0, 3, 1, outline)

# Rear bench splash and worktop
result.rect(0, 37, 64, 3, wood_dark)
result.rect(0, 40, 64, 15, wood)
result.rect(0, 40, 64, 2, wood_light)
result.line(0, 53, 63, 53, wood_dark)
# front cabinetry
result.rect(0, 55, 64, 9, wood_dark)
result.rect(2, 56, 26, 8, wood)
result.rect(30, 56, 32, 8, wood)
result.rect(13, 57, 5, 1, outline); result.rect(44, 57, 5, 1, outline)

# Rear labeled reagent bottles, distinct silhouettes
# square amber bottle
result.rect(48, 22, 8, 16, outline)
result.rect(49, 23, 6, 14, "#b86f38")
result.rect(50, 20, 4, 3, outline); result.rect(49, 19, 6, 2, dark)
result.rect(49, 27, 6, 5, white); result.rect(51, 28, 2, 3, red)
result.set(50, 24, "#df9b51")
# round blue wash bottle with nozzle
result.rect(57, 27, 6, 11, outline); result.rect(58, 28, 5, 9, blue)
result.rect(59, 25, 3, 3, outline); result.line(60, 24, 60, 21, outline); result.line(60, 21, 63, 21, outline)
result.rect(58, 31, 5, 3, white); result.line(59, 32, 61, 32, blue_dark)

# Microscope base and foot, left side
result.poly([(4,49),(8,46),(25,46),(30,51),(29,54),(6,54),(3,52)], outline)
result.poly([(7,49),(11,48),(24,48),(27,51),(26,52),(7,52)], steel)
result.rect(12, 46, 11, 2, lightsteel)
# microscope curved arm
result.poly([(7,43),(7,31),(10,24),(14,20),(19,19),(22,21),(20,24),(16,23),(13,26),(11,32),(11,42),(16,46),(12,48)], outline)
result.poly([(9,41),(9,32),(12,26),(15,22),(19,21),(20,22),(18,24),(15,24),(13,27),(11,34),(11,41),(15,45),(13,46)], steel)
result.set(10,29, lightsteel); result.set(11,27, lightsteel)
# head tube angled downward
result.poly([(16,18),(20,15),(27,22),(24,26),(22,25),(24,22),(19,18),(18,21)], outline)
result.poly([(19,18),(20,17),(25,22),(24,23)], lightsteel)
# eyepiece
result.poly([(18,13),(21,11),(25,15),(22,18)], outline)
result.poly([(20,13),(21,13),(23,15),(22,16)], blue_dark)
# objective turret and lenses
result.rect(21,25,8,3, outline); result.rect(23,28,2,5, dark); result.rect(27,27,2,5, dark)
result.set(23,32, cyan); result.set(28,31, cyan)
# stage
result.rect(12,34,19,3, outline); result.rect(14,34,15,1, lightsteel)
result.rect(18,33,8,1, glass_hi); result.set(22,35, blue)
# focus knobs
result.circle(12,29,3, outline); result.circle(12,29,1, yellow)
# stage support / illuminator
result.poly([(17,37),(27,37),(25,45),(18,45)], dark)
result.circle(22,42,3, outline); result.circle(22,42,2, "#e6dfaa"); result.set(22,41, glass_hi)

# Test-tube rack on right middle
result.rect(33,33,14,2, outline); result.rect(34,35,2,10, outline); result.rect(44,35,2,10, outline)
result.rect(32,44,16,3, outline); result.rect(34,44,12,1, wood_light)
# tube 1 cyan
result.rect(35,27,3,7, outline); result.rect(36,28,1,5, glass_hi); result.rect(36,31,1,3, cyan)
result.set(35,26, outline); result.set(37,26, outline)
# tube 2 red
result.rect(39,26,3,8, outline); result.rect(40,27,1,6, glass_hi); result.rect(40,30,1,4, red)
result.set(39,25, outline); result.set(41,25, outline)
# tube 3 yellow
result.rect(43,28,3,6, outline); result.rect(44,29,1,5, glass_hi); result.rect(44,31,1,3, yellow)
result.set(43,27, outline); result.set(45,27, outline)

# Dropper laid on a clear strip of benchtop: bulb, glass shaft, liquid tip
result.poly([(48,42),(50,41),(53,43),(52,46),(49,46),(47,44)], outline)
result.poly([(49,42),(51,42),(52,43),(51,45),(49,44)], red)
result.line(52,44,61,44, outline); result.line(53,43,61,43, glass_hi)
result.set(61,43, blue); result.set(62,44, blue_dark)

# Open laboratory notebook in foreground, perspective shape
result.poly([(27,49),(39,47),(51,49),(61,47),(62,59),(51,62),(39,59),(27,61)], outline)
# left and right pages
result.poly([(28,50),(39,48),(50,50),(50,60),(40,58),(28,60)], paper)
result.poly([(51,50),(60,48),(61,58),(52,60)], white)
# center binding
result.line(50,50,51,59, wood_dark)
result.set(50,52, yellow); result.set(50,55, yellow); result.set(51,58, yellow)
# believable notebook marks: diagram, data lines, check boxes
result.line(31,52,41,51, ink); result.line(31,54,38,53, ink); result.line(31,57,39,56, ink)
result.rect(42,52,5,4, blue, fill=False); result.line(43,55,46,52, red)
result.line(54,52,58,51, ink); result.line(53,54,59,53, ink); result.line(53,57,58,56, ink)
result.set(59,50, red); result.set(58,55, green)

# Crisp scattered lab details: cap and small spatula
result.circle(5,45,2, outline); result.circle(5,45,1, purple)
result.line(2,42,8,42, lightsteel); result.set(1,42, outline); result.set(9,42, outline)

# Selective highlights and grounded contact shadows
result.line(34,48,46,48, wood_dark)
result.set(50,24, "#e6a05c"); result.set(58,29, cyan)

view(result, scale=8, margin=0)
finish(result)
