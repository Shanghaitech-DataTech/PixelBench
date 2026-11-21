# Neighborhood laundromat interior, 64x64 pixel art
result = new_canvas(64, 64, "#101923", name="neighborhood-laundromat")

# Palette
ink = "#111923"
deep = "#182532"
shadow = "#243544"
wall = "#b9ccd2"
wall2 = "#a7bbc2"
wall_hi = "#d9e9ec"
trim = "#708995"
white = "#eef9f8"
cool = "#c8f5f4"
cyan = "#79d5d5"
teal = "#318f98"
blue = "#39779a"
glass = "#173b51"
glass2 = "#245d70"
steel = "#849aa2"
steel_hi = "#c8d5d7"
floor = "#526975"
floor2 = "#455b68"
gap = "#293b47"
yellow = "#f5cc69"
red = "#d65c5c"
basket = "#e8a94c"
basket_hi = "#ffd174"
cloth = "#ca5f78"
cloth2 = "#6eb6c4"
green = "#6fa477"

# Back wall and cool-lit ceiling
result.rect(1, 1, 62, 43, wall)
result.rect(1, 1, 62, 7, deep)
result.rect(2, 8, 60, 2, trim)
result.rect(4, 3, 17, 2, cool)
result.rect(5, 5, 15, 1, "#729ea5")
result.rect(26, 3, 14, 2, cool)
result.rect(27, 5, 12, 1, "#729ea5")
result.rect(45, 3, 15, 2, cool)
result.rect(46, 5, 13, 1, "#729ea5")
# Light pools / wall paneling
result.rect(3, 11, 58, 1, wall_hi)
result.rect(3, 13, 58, 1, "#91aab2")
for x in range(4, 61, 8):
    result.rect(x, 15, 1, 27, "#a0b6bd")
result.rect(1, 42, 62, 2, ink)

# Clock with square pixel rim
result.circle(51, 19, 6, ink)
result.circle(51, 19, 5, white)
result.set(51, 14, teal).set(56, 19, teal).set(51, 24, teal).set(46, 19, teal)
result.line(51, 19, 51, 15, ink)
result.line(51, 19, 54, 21, ink)
result.rect(50, 18, 2, 2, red)
# small wall sign
result.rect(5, 16, 15, 7, trim)
result.rect(6, 17, 13, 5, white)
result.rect(8, 18, 9, 1, teal)
result.rect(9, 20, 7, 1, cyan)

# Back row plinth and five individually separated washers
result.rect(22, 23, 39, 19, ink)
result.rect(23, 24, 37, 2, steel_hi)
for x in [23, 31, 39, 47, 55]:
    # case
    result.rect(x, 26, 7, 15, steel)
    result.rect(x+1, 27, 5, 2, wall_hi)
    result.set(x+1, 27, teal)
    result.set(x+5, 27, red)
    # dark circular front door with rim
    result.circle(x+3, 34, 3, ink)
    result.circle(x+3, 34, 2, glass2)
    result.set(x+2, 33, cyan)
    result.set(x+4, 35, glass)
    result.rect(x+1, 39, 5, 1, shadow)
# hard separators between machines
for x in [30, 38, 46, 54]:
    result.rect(x, 24, 1, 18, gap)

# Folding table at left, with folded laundry
result.rect(3, 27, 18, 2, white)
result.rect(2, 29, 20, 2, steel_hi)
result.rect(4, 31, 2, 13, shadow)
result.rect(18, 31, 2, 13, shadow)
result.line(5, 37, 19, 43, trim)
result.line(19, 37, 5, 43, trim)
result.rect(6, 24, 8, 3, cloth2)
result.rect(8, 22, 8, 2, cloth)
result.rect(10, 20, 7, 2, yellow)
result.set(15, 21, basket_hi)

# Floor and perspective tile lines
result.rect(1, 44, 62, 19, floor)
result.rect(1, 44, 62, 2, "#6f8791")
for y in [51, 58]:
    result.line(1, y, 62, y, floor2)
for x0 in [5, 17, 29, 41, 53]:
    result.line(32, 44, x0, 63, floor2)
# aisle highlights
result.rect(24, 46, 16, 1, "#78909a")
result.rect(27, 50, 10, 1, "#607985")

# Foreground row: four larger front-loading machines
result.rect(13, 46, 50, 17, ink)
result.rect(14, 47, 48, 2, steel_hi)
for x in [14, 26, 38, 50]:
    result.rect(x, 49, 11, 14, steel)
    result.rect(x+1, 50, 9, 2, wall_hi)
    result.rect(x+1, 50, 2, 1, teal)
    result.set(x+8, 50, red)
    result.circle(x+5, 57, 4, ink)
    result.circle(x+5, 57, 3, glass2)
    result.set(x+3, 55, cyan)
    result.set(x+4, 55, "#9be5e2")
    result.set(x+6, 58, glass)
    result.set(x+7, 59, glass)
    result.rect(x+1, 62, 9, 1, shadow)
for x in [25, 37, 49]:
    result.rect(x, 47, 1, 16, gap)

# Laundry basket in left foreground, outlined and woven
result.rect(2, 48, 10, 2, ink)
result.poly([(1,49),(12,49),(10,62),(3,62)], ink)
result.poly([(3,50),(10,50),(9,61),(4,61)], basket)
result.rect(4, 50, 2, 2, cloth)
result.rect(6, 50, 3, 2, cloth2)
result.rect(4, 53, 5, 1, basket_hi)
result.rect(4, 56, 5, 1, basket_hi)
result.set(4,54,ink).set(8,54,ink).set(4,58,ink).set(8,58,ink)
result.rect(5, 59, 3, 1, yellow)

# Crisp outer frame and tiny room details
result.rect(0, 0, 64, 1, ink)
result.rect(0, 63, 64, 1, ink)
result.rect(0, 0, 1, 64, ink)
result.rect(63, 0, 1, 64, ink)
result.rect(58, 16, 3, 5, green)
result.rect(59, 15, 1, 1, white)

view(result, scale=8, margin=0)
finish(result)
