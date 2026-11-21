# Poolcore liminal pool hall, 128x128 pixel art
result = new_canvas(128, 128, background="#b9e8ed", name="poolcore-water-slide")

# Palette
ceiling = "#d8f2f1"
ceiling_shadow = "#a9d5d8"
beam = "#83b9c1"
light = "#f5ffff"
light_glow = "#e8ffff"
wall = "#c7e9e9"
wall_hi = "#dff7f4"
tile = "#93cbd1"
tile_dark = "#609da8"
deep = "#247d98"
water = "#65c6dd"
water_hi = "#c8fbf5"
water_mid = "#42aecb"
water_dark = "#2087a7"
white = "#f1f8ee"
slide_shadow = "#a8d4d5"
slide_dark = "#68aab5"
yellow = "#f5c62e"
yellow_hi = "#ffe96a"
yellow_dark = "#c78c16"
skin = "#d69b72"
skin_hi = "#efbd92"
hair = "#3d2c32"
hair_hi = "#68434a"
suit = "#245b72"

# Ceiling plane and distant wall
result.poly([(0,0),(127,0),(127,34),(0,45)], ceiling)
result.poly([(0,45),(127,34),(127,66),(0,66)], wall)
# Ceiling perspective beams
result.poly([(0,7),(127,4),(127,7),(0,11)], ceiling_shadow)
result.poly([(0,27),(127,21),(127,24),(0,31)], ceiling_shadow)
result.poly([(18,0),(23,0),(36,40),(31,41)], beam)
result.poly([(70,0),(74,0),(77,37),(72,38)], beam)
result.poly([(108,0),(112,0),(106,36),(101,37)], beam)
# Fluorescent fixtures
for pts in [
    [(3,14),(25,13),(27,16),(4,18)],
    [(45,9),(66,8),(67,12),(46,13)],
    [(82,14),(100,13),(99,17),(82,18)],
    [(112,8),(127,8),(127,12),(111,13)],
    [(28,29),(42,27),(43,30),(29,32)],
    [(82,27),(95,25),(95,28),(82,30)]]:
    result.poly(pts, light_glow)
    # central crisp tube
result.poly([(5,14),(24,14),(25,15),(5,16)], light)
result.poly([(47,9),(65,9),(65,11),(47,11)], light)
result.poly([(84,14),(99,14),(98,16),(84,16)], light)
result.poly([(113,9),(127,9),(127,11),(112,11)], light)
result.poly([(30,29),(41,28),(41,29),(30,30)], light)
result.poly([(83,27),(94,26),(94,27),(83,28)], light)

# Back wall mosaic grid, converging slightly toward distance
for y in [48,54,60,65]:
    result.line(0,y,127,y-5 if y<65 else y, tile)
for x in range(3,128,8):
    topx = 64 + (x-64)*0.82
    result.line(int(topx),40,x,66,tile)
# Back wall highlights and far doorway alcoves
result.rect(7,48,17,16,"#b5dddd")
result.rect(8,49,15,14,"#7ebbc3")
result.rect(10,51,11,12,deep)
result.rect(104,42,17,20,"#b1dada")
result.rect(106,44,13,18,"#5799a7")
result.rect(108,46,9,16,deep)
# Door reflections
result.rect(11,52,2,10,"#8fcbd1")
result.rect(109,47,2,13,"#7dbbc3")

# Tiled columns with depth
for x,w,top in [(0,9,28),(27,8,34),(92,9,31),(121,7,25)]:
    result.rect(x,top,w,42-top,wall_hi)
    result.rect(x+w-2,top,2,42-top,tile_dark)
    result.rect(x,top,2,42-top,white)
    for yy in range(top+5,43,6): result.line(x,yy,x+w-1,yy,tile)
    for xx in range(x+5,x+w,6): result.line(xx,top,xx,42,tile)
# bases
result.rect(0,63,10,4,white); result.rect(26,63,10,4,white)
result.rect(91,62,11,5,white); result.rect(120,62,8,5,white)

# Pool coping and vast water plane
result.rect(0,66,128,5,white)
result.line(0,66,127,66,tile_dark)
result.line(0,70,127,70,tile)
result.rect(0,71,128,57,water)
# underwater perspective tile grid
for y in [79,90,104,121]:
    result.line(0,y,127,y,water_dark)
for x0,x1 in [(0,19),(18,34),(43,51),(65,67),(88,83),(116,101),(127,114)]:
    result.line(x0,71,x1,127,water_mid)
# luminous vertical light reflections
result.poly([(5,71),(15,71),(21,127),(4,127)],"#7ed8e4")
result.poly([(48,71),(59,71),(55,127),(38,127)],"#8ddde5")
result.poly([(93,71),(102,71),(116,127),(98,127)],"#8edee4")
# reflected ceiling streaks and ripples
for x0,y,x1,c in [
    (2,75,22,water_hi),(31,74,52,water_hi),(69,76,87,"#aaf0ed"),(103,74,124,water_hi),
    (9,83,34,"#a2e9e9"),(57,84,76,water_hi),(91,85,113,"#b3f1ed"),
    (1,96,18,"#91e3e6"),(24,94,44,water_hi),(75,96,93,"#9be8e8"),(106,99,126,water_hi),
    (8,111,31,water_hi),(39,116,59,"#a5efec"),(79,110,104,water_hi),(107,121,126,"#94e4e7")]:
    result.line(x0,y,x1,y,c)
# broken dark ripple accents
for x0,y,x1 in [(15,78,28),(77,81,91),(2,88,15),(37,88,50),(98,92,116),(19,102,34),(62,105,77),(4,119,18),(85,124,101)]:
    result.line(x0,y,x1,y,water_dark)
    result.set(x0-2,y,"#49b8cf"); result.set(x1+2,y,"#49b8cf")

# Curving white water slide: rear support and stair glimpses
result.rect(48,43,3,27,slide_dark)
result.rect(52,45,2,22,tile_dark)
for yy in range(47,65,4): result.line(48,yy,54,yy,white)
# upper slide mouth and descending S curve, dark underside first
result.path("M 42 38 C 55 34, 72 35, 76 43 C 80 52, 65 55, 60 60 C 55 65, 64 68, 76 69 L 75 76 C 57 76, 46 70, 49 61 C 52 52, 68 49, 66 43 C 63 39, 53 41, 44 44 Z", slide_dark)
# bright inner chute
result.path("M 41 36 C 56 32, 75 34, 79 42 C 84 53, 67 58, 62 62 C 58 66, 67 69, 79 68 L 80 73 C 63 75, 51 71, 53 62 C 55 54, 72 51, 70 43 C 67 38, 54 39, 43 42 Z", white)
# inner pale channel and rim highlights
result.path("M 47 38 C 58 35, 72 37, 74 43 C 77 49, 63 54, 59 59", slide_shadow, fill=False)
result.line(42,36,43,42,light)
result.path("M 79 42 C 84 53, 68 58, 62 62", light, fill=False)
result.line(79,69,80,73,slide_shadow)
# splash at slide outlet
result.line(76,74,71,78,water_hi); result.line(79,74,84,78,water_hi)
result.set(75,78,water_hi); result.set(82,77,water_hi)

# Girl from behind, floating at centre; subtle water shadow
result.ellipse(64,101,19,4,"#319bb8")
result.line(48,102,80,102,water_hi)
# yellow ring outer pixel ellipse, inner water cutout
result.ellipse(64,95,16,10,yellow_dark)
result.ellipse(64,93,16,9,yellow)
result.ellipse(64,91,13,6,yellow_hi)
result.ellipse(64,91,8,4,water_mid)
# body/shoulders emerging through ring
result.poly([(58,89),(59,82),(62,78),(68,78),(71,83),(71,91),(68,95),(60,94)], skin)
result.rect(60,86,10,8,suit)
result.line(60,87,58,91,skin_hi); result.line(70,87,73,91,skin_hi)
# head and hair viewed from behind
result.rect(61,73,8,9,skin)
result.set(60,75,skin_hi); result.set(69,75,skin)
result.poly([(60,73),(62,70),(68,70),(71,73),(70,81),(68,84),(67,78),(63,78),(62,84),(60,80)], hair)
result.line(62,72,68,71,hair_hi)
result.set(61,74,hair_hi); result.set(69,73,hair_hi)
# ring shine and lower occlusion by water
result.line(51,90,57,87,light)
result.line(73,88,77,91,yellow_hi)
result.line(49,96,55,98,yellow_dark)
result.line(73,99,79,96,yellow_dark)
result.line(55,101,73,101,water_hi)
# concentric quiet ripples around swimmer
result.line(39,105,52,105,"#b8f4ef"); result.line(76,105,91,105,"#b8f4ef")
result.line(31,109,49,109,"#8ce1e5"); result.line(79,109,100,109,"#8ce1e5")
result.line(44,113,57,113,water_hi); result.line(71,113,86,113,water_hi)

# A few crisp mosaic specks and reflected glints
for x,y in [(18,58),(39,51),(83,57),(114,55),(7,86),(120,80),(29,123),(69,119),(110,108)]:
    result.set(x,y,wall_hi if y<66 else water_hi)

view(result, scale=4, margin=0)
finish(result)
