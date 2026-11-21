# Poolcore liminal indoor pool hall, 128x128 pixel art
result = new_canvas(128, 128, background="#b9edf0", name="poolcore-water-slide")

# Compact cool palette
ceiling = "#d9f3f1"
ceiling_shadow = "#a8d8dc"
line_light = "#edfdf8"
grid = "#7fc5cf"
grid_dark = "#5aa9b8"
far_blue = "#9bdddf"
wall = "#bde8e6"
wall_hi = "#d8f5ef"
wall_sh = "#8fcbd0"
deep = "#58b6ca"
water = "#72cedb"
water_light = "#bff4ed"
water_mid = "#8de1e5"
water_dark = "#3c9fb9"
water_deep = "#358da8"
white = "#f4fff8"
slide_sh = "#b7d7d8"
slide_dark = "#7eb7c0"
outline = "#397f91"
yellow = "#ffd449"
yellow_hi = "#fff08a"
yellow_sh = "#e6a92e"
skin = "#dca07e"
skin_hi = "#f0bd98"
hair = "#543e46"
hair_hi = "#76515a"
suit = "#487f95"

# Ceiling and rear wall
result.rect(0, 0, 128, 43, ceiling)
result.rect(0, 43, 128, 26, wall)
# Long ceiling seams converging toward center
for x in [-30, 0, 25, 47, 81, 103, 128, 158]:
    result.line(x, 0, 64, 43, ceiling_shadow)
result.line(0, 20, 127, 20, ceiling_shadow)
result.line(0, 41, 127, 41, grid_dark)
# fluorescent fixtures, crisp luminous strips
fixtures = [(7,7,24,4),(43,8,20,4),(79,8,20,4),(106,7,18,4),
            (18,26,18,3),(50,27,14,3),(77,27,14,3),(103,26,16,3)]
for x,y,w,h in fixtures:
    result.rect(x-1,y-1,w+2,h+2,ceiling_shadow)
    result.rect(x,y,w,h,line_light)
    result.line(x+2,y,x+w-3,y,white)

# Rear wall tile grid
for y in range(47, 69, 6):
    result.line(0, y, 127, y, grid)
for x in range(3, 128, 7):
    result.line(x, 43, x, 68, grid)
# distant openings / alcoves
result.rect(8, 48, 24, 17, grid_dark)
result.rect(10, 50, 20, 15, "#68b8c3")
result.rect(13, 53, 14, 12, far_blue)
result.rect(43, 49, 19, 16, grid_dark)
result.rect(45, 51, 15, 14, "#8dd3d5")
result.rect(94, 47, 25, 18, grid_dark)
result.rect(96, 49, 21, 16, "#73bec8")
result.rect(99, 52, 15, 13, far_blue)
# waterline rim at horizon
result.rect(0, 66, 128, 3, white)
result.line(0, 69, 127, 69, grid_dark)

# Pool water base
result.rect(0, 70, 128, 58, water)
# perspective tiled floor visible beneath water: rays and horizontal bands
for x in range(-48, 177, 14):
    result.line(64, 69, x, 127, grid_dark)
for y in [74, 80, 88, 98, 110, 123]:
    result.line(0, y, 127, y, "#60becb")
# submerged pale tile patches
result.poly([(0,76),(15,76),(29,88),(0,88)], water_mid)
result.poly([(90,72),(128,73),(128,82),(103,81)], water_mid)
result.poly([(0,105),(21,101),(32,112),(0,120)], "#62c1d0")
result.poly([(101,103),(128,99),(128,113),(111,116)], "#69c7d4")

# Left foreground tiled column
result.poly([(0,25),(13,27),(15,99),(0,111)], wall_hi)
result.poly([(13,27),(20,31),(21,94),(15,99)], wall_sh)
result.line(13,27,15,99,grid_dark)
for y in range(35,101,9):
    result.line(0,y,15,y-1,grid)
for x in [5,10]:
    result.line(x,26,x+2,106,grid)
# right rear column, adding depth
result.poly([(112,29),(126,27),(127,78),(113,75)], wall_hi)
result.poly([(108,32),(112,29),(113,75),(108,77)], wall_sh)
for y in range(37,76,8):
    result.line(109,y,127,y-1,grid)
for x in [116,122]:
    result.line(x,29,x,76,grid)

# Slide support poles behind chute
result.rect(89,32,3,42,slide_dark)
result.rect(112,26,3,48,slide_dark)
result.rect(90,34,1,39,white)
result.rect(113,28,1,44,white)
# curving slide, dark outer silhouette then white body
result.path("M126 24 C109 25 103 35 105 44 C107 54 103 60 92 64 C81 68 78 76 82 84 L94 87 C92 79 96 75 106 71 C120 65 123 54 119 44 C116 37 120 34 127 34 Z", slide_dark)
result.path("M126 27 C113 28 108 35 110 44 C113 55 108 63 96 67 C86 70 82 76 86 82 L92 83 C90 78 95 73 103 71 C117 66 120 55 116 44 C113 36 118 31 127 31 Z", white)
# slide interior and edge highlights
result.path("M124 31 C115 33 114 37 116 44 C119 55 115 63 103 68 C94 71 89 76 90 82", slide_sh, fill=False)
result.path("M126 27 C113 28 108 35 110 44", line_light, fill=False)
result.line(82,84,94,87,outline)
# splash where slide enters
result.line(79,86,86,82,water_light)
result.line(88,88,96,84,water_light)
result.line(83,89,91,87,white)

# Water reflections and ripples, mostly broken horizontal pixels
ripples = [
(4,73,15,water_light),(23,72,9,wall_hi),(38,76,16,water_light),(67,73,13,wall_hi),(96,76,21,water_light),
(1,83,22,water_dark),(27,85,13,water_light),(47,82,18,water_mid),(70,86,12,water_light),(101,85,19,water_dark),
(7,93,14,water_light),(25,96,21,water_dark),(52,92,12,water_light),(76,95,19,water_dark),(104,92,20,water_light),
(0,106,18,water_deep),(24,103,11,water_light),(40,109,21,water_dark),(71,104,17,water_light),(97,109,27,water_deep),
(6,119,27,water_light),(39,121,14,water_deep),(62,116,22,water_dark),(90,123,31,water_light)]
for x,y,w,c in ripples:
    result.rect(x,y,w,2 if y%3==0 else 1,c)
# Thin light reflections from ceiling
for x,y,w in [(12,79,8),(34,78,6),(56,75,7),(72,80,9),(111,79,8),(17,100,12),(83,112,15),(44,126,18)]:
    result.rect(x,y,w,1,white)

# Girl floating from behind: arms, ring, torso, hair
# far ripple shadow under subject
result.ellipse(63,108,22,5,water_dark)
result.rect(45,105,38,2,water_mid)
# arms draped around ring
result.line(49,91,45,99,skin)
result.line(78,91,82,99,skin)
result.rect(44,98,6,3,skin_hi)
result.rect(79,98,6,3,skin_hi)
# yellow ring outer stepped ellipse with dark outline
result.ellipse(64,101,22,11,outline)
result.ellipse(64,100,21,10,yellow_sh)
result.ellipse(64,98,20,8,yellow)
# ring hole
result.ellipse(64,98,11,5,water_dark)
result.ellipse(64,97,10,4,"#4eacc0")
# torso and swimsuit above ring
result.poly([(57,88),(70,88),(74,99),(54,99)],skin)
result.poly([(58,91),(69,91),(72,99),(55,99)],suit)
result.line(56,96,71,96,"#386c81")
# neck and head from behind
result.rect(60,82,8,8,skin)
result.rect(61,80,6,5,skin_hi)
result.ellipse(64,76,9,10,hair)
# hair silhouette and highlights
result.rect(56,75,17,9,hair)
result.poly([(56,78),(58,87),(62,89),(64,82),(67,89),(72,86),(73,77)],hair)
result.rect(59,68,11,3,hair)
result.rect(57,71,15,6,hair)
result.line(59,72,65,69,hair_hi)
result.line(68,72,71,78,hair_hi)
# small crown reflection / hair sheen
result.rect(61,70,5,1,"#8c6470")
# ring highlights
result.rect(48,94,8,2,yellow_hi)
result.rect(46,97,5,2,yellow_hi)
result.rect(71,107,8,1,"#c88926")
# foreground ripples crossing ring reflection
result.rect(35,113,22,2,water_light)
result.rect(57,116,29,2,water_deep)
result.rect(74,112,18,1,water_light)
result.rect(48,121,16,1,water_light)

# Sparse sparkle pixels
for x,y in [(3,91),(31,75),(38,101),(91,91),(119,96),(24,116),(100,118),(69,72)]:
    result.set(x,y,white)

finish(result)
