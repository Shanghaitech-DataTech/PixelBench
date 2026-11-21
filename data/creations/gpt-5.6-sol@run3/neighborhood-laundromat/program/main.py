from pixelbench_api import *

# Neighborhood laundromat, 64x64 pixel-art scene.
c = new_canvas(64, 64, background="#d9e8e9", name="neighborhood-laundromat")

# Palette
ink = "#182b35"
deep = "#243b46"
edge = "#41616b"
wall = "#b9d0d2"
wall_hi = "#dcebec"
white = "#eef7f5"
light = "#f8ffff"
steel = "#8faeb2"
steel_dark = "#66868d"
blue = "#5aa6bd"
blue_hi = "#90d4df"
glass = "#274854"
glass_hi = "#487482"
shadow = "#6b8990"
floor = "#91adb0"
floor_dark = "#718e94"
tile_hi = "#b7cbcb"
red = "#db6258"
yellow = "#e7c85c"
basket = "#e89b49"
basket_hi = "#ffc266"
cloth1 = "#d65f72"
cloth2 = "#4d91c1"
cloth3 = "#f1d56a"
plant = "#4d806f"

# Back wall and structural bands.
c.rect(0, 0, 64, 18, wall_hi)
c.rect(0, 13, 64, 5, wall)
c.rect(0, 16, 64, 2, steel_dark)
c.rect(0, 17, 64, 1, ink)
# Ceiling strip and cool fluorescent panels.
c.rect(0, 0, 64, 2, steel)
c.rect(5, 3, 18, 1, steel)
c.rect(6, 2, 16, 3, light)
c.rect(39, 3, 17, 1, steel)
c.rect(40, 2, 15, 3, light)
c.set(7, 5, blue_hi); c.set(21, 5, blue_hi); c.set(41, 5, blue_hi); c.set(54, 5, blue_hi)
# Small hanging sign.
c.rect(3, 7, 18, 7, white)
c.rect(3, 7, 18, 1, blue)
c.text(5, 9, "WASH", deep, font="5x7", spacing=0)

# Wall clock.
c.circle(54, 10, 6, ink)
c.circle(54, 10, 5, white)
c.set(54, 6, deep); c.set(58, 10, deep); c.set(54, 14, deep); c.set(50, 10, deep)
c.line(54, 10, 54, 7, deep); c.line(54, 10, 57, 11, deep); c.set(54, 10, red)

# Floor with perspective tile grid.
c.poly([(0, 35), (63, 35), (63, 63), (0, 63)], floor)
c.rect(0, 35, 64, 2, floor_dark)
for y in (45, 55):
    c.line(0, y, 63, y, floor_dark)
c.line(10, 36, 3, 63, floor_dark)
c.line(27, 36, 25, 63, floor_dark)
c.line(44, 36, 48, 63, floor_dark)
c.line(58, 36, 63, 53, floor_dark)
# Cool tile glints.
c.line(29, 47, 39, 47, tile_hi)
c.line(51, 57, 61, 57, tile_hi)
c.line(5, 59, 17, 59, tile_hi)

# Back row: five clearly separated front loaders.
for x in (1, 13, 25, 37, 49):
    c.rect(x, 18, 11, 17, ink)
    c.rect(x+1, 19, 9, 15, steel)
    c.rect(x+1, 19, 9, 4, white)
    c.rect(x+2, 20, 3, 1, blue)
    c.set(x+8, 20, red)
    c.circle(x+5, 28, 4, deep)
    c.circle(x+5, 28, 3, glass)
    c.rect(x+4, 26, 3, 1, glass_hi)
    c.set(x+3, 29, blue_hi)
    c.rect(x+2, 33, 7, 1, shadow)
# Extra vertical separator shine.
for x in (12, 24, 36, 48):
    c.rect(x, 19, 1, 15, deep)

# Near row shadow and four larger individual machines.
c.rect(0, 38, 45, 20, deep)
for x in (1, 12, 23, 34):
    c.rect(x, 38, 10, 20, ink)
    c.rect(x+1, 39, 8, 18, "#a9c0c2")
    c.rect(x+1, 39, 8, 5, white)
    c.rect(x+2, 40, 3, 1, blue)
    c.set(x+7, 40, red)
    c.set(x+7, 42, yellow)
    c.circle(x+5, 50, 4, deep)
    c.circle(x+5, 50, 3, glass)
    c.line(x+3, 48, x+6, 47, glass_hi)
    c.set(x+4, 52, blue_hi)
    c.rect(x+2, 56, 6, 1, shadow)
# Divider posts make every unit distinct.
for x in (11, 22, 33, 44):
    c.rect(x, 38, 1, 20, ink)
# Near row feet and cast shadow.
c.rect(2, 58, 7, 2, deep); c.rect(13, 58, 7, 2, deep)
c.rect(24, 58, 7, 2, deep); c.rect(35, 58, 7, 2, deep)
c.rect(0, 60, 44, 2, floor_dark)

# Folding table at right, angled top with folded laundry.
c.poly([(44, 38), (61, 38), (63, 42), (46, 43)], ink)
c.poly([(45, 37), (60, 37), (62, 40), (46, 41)], white)
c.line(47, 41, 47, 56, deep); c.line(60, 40, 62, 56, deep)
c.rect(46, 55, 3, 2, deep); c.rect(60, 55, 3, 2, deep)
# Folded fabric stack.
c.rect(49, 34, 9, 3, cloth2)
c.rect(48, 32, 11, 3, cloth3)
c.rect(50, 30, 8, 3, cloth1)
c.line(52, 31, 57, 31, "#ef9ba7")

# Orange laundry basket in foreground with dark rim, handle, and open slats.
c.line(49, 47, 50, 43, deep); c.line(50, 43, 58, 43, deep); c.line(58, 43, 60, 47, deep)
c.poly([(47, 46), (61, 46), (59, 61), (49, 61)], ink)
c.poly([(48, 47), (60, 47), (58, 60), (50, 60)], basket)
c.rect(47, 46, 14, 3, basket_hi)
c.rect(49, 47, 10, 1, deep)
for y in (51, 55):
    c.rect(50, y, 9, 2, deep)
    c.rect(51, y, 2, 2, basket_hi)
    c.rect(55, y, 2, 2, basket_hi)
# Clothes peeking out of basket.
c.poly([(49, 46), (51, 42), (55, 45), (57, 42), (60, 46)], cloth2)
c.rect(52, 44, 4, 2, cloth3)
c.set(58, 44, cloth1)

# Foreground edge and tiny reflection accents.
c.rect(0, 62, 64, 2, steel_dark)
c.rect(1, 62, 17, 1, tile_hi)
c.rect(29, 62, 10, 1, tile_hi)
c.set(46, 61, light); c.set(62, 59, light)

result = c
view(result, scale=8, margin=0)
finish(result)
