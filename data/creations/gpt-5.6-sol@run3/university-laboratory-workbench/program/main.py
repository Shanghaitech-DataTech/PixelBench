# 64x64 university laboratory workbench
result = new_canvas(64, 64, background="#dce8e6", name="university_lab_workbench")

# Palette
ink = "#172b3a"
ink2 = "#294657"
wall = "#dce8e6"
tile = "#b9cecd"
tile_hi = "#eef6f1"
steel = "#7895a0"
steel_hi = "#b8cdd0"
shadow = "#4b6872"
bench = "#a86f45"
bench_hi = "#c58b58"
bench_edge = "#70452f"
cabinet = "#5d7180"
cab_hi = "#718895"
white = "#f7f0d4"
paper = "#fff8df"
blue = "#3b8fa8"
blue_hi = "#72c5ce"
teal = "#3d9b8b"
green = "#77ad68"
acid = "#b9d657"
yellow = "#f2c14e"
orange = "#e27a3f"
red = "#be4b4b"
purple = "#725b91"
glass = "#bce2df"

# Tiled laboratory wall
for y in (0, 9, 18, 27):
    result.rect(0, y, 64, 1, tile)
for row, y0 in enumerate((0, 9, 18, 27)):
    offset = 0 if row % 2 == 0 else 8
    for x in range(offset, 64, 16):
        result.rect(x, y0, 1, 9, tile)
result.rect(0, 1, 64, 1, tile_hi)

# Power outlet and backsplash
result.rect(49, 17, 11, 8, ink2)
result.rect(50, 18, 9, 6, white)
result.rect(52, 20, 2, 2, shadow)
result.rect(56, 20, 2, 2, shadow)
result.rect(0, 31, 64, 3, ink2)
result.rect(0, 31, 64, 1, steel_hi)

# Bench top and front
result.rect(0, 34, 64, 18, bench)
result.rect(0, 34, 64, 2, bench_hi)
result.rect(0, 50, 64, 4, bench_edge)
result.rect(0, 54, 64, 10, cabinet)
result.rect(2, 55, 28, 9, cab_hi)
result.rect(33, 55, 29, 9, cab_hi)
result.rect(30, 54, 3, 10, ink2)
result.rect(14, 57, 6, 2, ink2)
result.rect(44, 57, 7, 2, ink2)
result.rect(3, 55, 26, 1, steel)
result.rect(34, 55, 27, 1, steel)

# Rear reagent bottles, differentiated by neck/cap/body shape
# Amber round-shouldered bottle
result.rect(26, 18, 6, 2, ink)
result.rect(27, 20, 4, 4, orange)
result.rect(25, 24, 8, 10, ink)
result.rect(26, 24, 6, 9, "#a95d38")
result.rect(27, 25, 2, 7, orange)
result.rect(26, 28, 6, 3, white)
result.rect(28, 28, 2, 3, yellow)
# Tall blue bottle
result.rect(36, 16, 5, 2, ink)
result.rect(37, 18, 3, 4, glass)
result.rect(35, 22, 7, 12, ink)
result.rect(36, 22, 5, 11, blue)
result.rect(37, 23, 2, 4, blue_hi)
result.rect(36, 27, 5, 3, white)
result.rect(38, 27, 1, 3, red)
# Squat green squeeze bottle with nozzle
result.rect(46, 22, 5, 2, ink)
result.rect(48, 19, 2, 3, white)
result.rect(49, 17, 5, 2, ink)
result.rect(51, 16, 4, 1, ink)
result.rect(45, 24, 8, 10, ink)
result.rect(46, 24, 6, 9, teal)
result.rect(47, 25, 2, 7, green)
result.rect(46, 28, 6, 3, white)
result.rect(48, 29, 2, 2, acid)
# Small purple vial
result.rect(56, 24, 5, 2, ink)
result.rect(57, 26, 3, 2, glass)
result.rect(55, 28, 7, 6, ink)
result.rect(56, 28, 5, 5, purple)
result.rect(57, 29, 2, 2, white)

# Microscope: heavy base and coherent curved arm
result.poly([(3,47),(4,43),(8,41),(17,41),(22,44),(24,47)], ink)
result.poly([(5,46),(7,43),(18,43),(21,46)], steel)
result.rect(8, 40, 11, 3, ink)
result.rect(9, 40, 9, 1, steel_hi)
# upright curved arm
result.poly([(7,39),(6,35),(7,28),(10,22),(14,19),(18,20),(20,24),(19,29),(16,29),(16,25),(14,23),(12,24),(10,29),(10,36),(13,39)], ink)
result.poly([(9,36),(9,29),(12,23),(15,21),(18,23),(18,26),(16,27),(15,24),(13,24),(11,29),(11,36)], steel)
result.rect(9, 29, 2, 6, steel_hi)
# eyepiece and angled body tube
result.poly([(13,18),(16,15),(22,19),(20,22)], ink)
result.poly([(16,16),(21,19),(19,21),(14,18)], steel)
result.rect(14, 13, 7, 3, ink)
result.rect(15, 13, 6, 1, steel_hi)
# focus knobs
result.circle(18, 28, 3, ink)
result.circle(18, 28, 2, blue)
result.set(17,27,blue_hi)
# nosepiece and objectives
result.rect(17, 31, 7, 3, ink)
result.rect(19, 34, 2, 5, ink)
result.rect(22, 34, 2, 4, ink)
result.rect(19, 34, 2, 2, yellow)
result.rect(22, 34, 2, 2, red)
# slide on stage
result.rect(6, 37, 18, 3, ink)
result.rect(8, 37, 14, 1, steel_hi)
result.rect(12, 36, 7, 1, glass)
result.rect(15, 36, 2, 1, acid)
# lamp glow/window
result.rect(12, 44, 5, 2, yellow)
result.rect(13, 44, 3, 1, white)

# Test-tube rack in center foreground
result.rect(27, 36, 21, 3, ink)
result.rect(28, 36, 19, 1, steel_hi)
result.rect(28, 46, 20, 3, ink)
result.rect(30, 39, 2, 7, ink2)
result.rect(44, 39, 2, 7, ink2)
# tubes with distinct liquid levels
for x in (30, 35, 40, 45):
    result.rect(x, 30, 4, 2, ink)
    result.rect(x+1, 32, 2, 14, glass)
    result.set(x+2,33,white)
result.rect(31, 40, 2, 6, blue)
result.set(32,40,blue_hi)
result.rect(36, 37, 2, 9, acid)
result.set(37,37,white)
result.rect(41, 41, 2, 5, red)
result.set(42,41,orange)
result.rect(46, 35, 2, 11, purple)
result.set(47,35,white)

# Open laboratory notebook, foreground perspective
result.poly([(18,49),(33,47),(34,60),(18,62)], ink)
result.poly([(34,47),(53,50),(51,63),(34,60)], ink)
result.poly([(20,49),(33,48),(33,59),(20,61)], paper)
result.poly([(35,48),(51,51),(49,61),(35,59)], paper)
result.line(34,48,34,59,bench_edge)
# ruled pages and diagram
result.line(22,52,31,51,tile)
result.line(22,55,31,54,tile)
result.line(22,58,31,57,tile)
result.line(38,52,48,54,tile)
result.line(37,55,47,57,tile)
result.rect(25,50,5,1,blue)
result.circle(42,54,2,teal,fill=False)
result.line(42,52,46,50,teal)
result.set(46,50,red)

# Glass dropper laid diagonally across the right notebook page
result.poly([(37,48),(40,49),(42,52),(39,54),(37,52),(36,50)], ink)
result.poly([(38,49),(40,50),(41,52),(39,53),(37,51)], red)
result.line(41,52,49,59,ink)
result.line(40,53,48,60,ink)
result.line(42,53,48,59,glass)
result.set(47,58,blue)
result.set(48,60,blue)
result.set(49,61,blue_hi)

# Tiny cast shadows to ground objects
result.rect(25,33,8,1,bench_edge)
result.rect(54,33,8,1,bench_edge)

view(result, scale=8, margin=0)
finish(result)
