# Isometric forge-house, 128x128
c = new_canvas(128, 128, background="#25313a", name="red-roofed-forge-house")

# Palette
stone = "#59646a"
stone_l = "#758184"
stone_d = "#39464d"
wood = "#70432e"
wood_l = "#a76a3c"
wood_d = "#4b3028"
roof = "#b83232"
roof_l = "#e0523e"
roof_d = "#852a31"
roof_hi = "#f0784c"
cream = "#e7cf9b"
metal = "#3a4144"
glow = "#ffb347"
glow_l = "#ffe080"
coal = "#d94c24"
shadow = "#18242a"

# Ground shadow and stone foundation
c.poly([(64,91),(112,65),(123,72),(64,108),(7,76),(17,70)], shadow)
c.poly([(64,84),(108,60),(116,65),(64,96),(12,67),(20,62)], stone_d)
c.poly([(12,67),(64,96),(64,103),(12,74)], stone)
c.poly([(64,96),(116,65),(116,72),(64,103)], stone_d)
c.line(12,70,64,99,stone_l)
c.line(64,99,116,68,stone)

# Lower wall planes
c.poly([(20,52),(64,76),(64,102),(20,78)], "#a88e69")
c.poly([(64,76),(108,52),(108,78),(64,102)], "#80694f")
# timber framing on walls
c.line(23,59,23,78,wood_d)
c.line(61,80,61,101,wood_d)
c.line(67,80,67,101,wood_d)
c.line(104,56,104,78,wood_d)
c.line(20,75,64,99,wood_l)
c.line(64,99,108,75,wood_d)

# Roof two steep, clean isometric planes
c.poly([(64,18),(17,44),(64,75)], roof_l)
c.poly([(64,18),(111,44),(64,75)], roof_d)
# eaves and ridge highlights
c.line(17,44,64,72,roof_hi)
c.line(64,72,111,44,roof)
c.line(64,18,64,73,"#f26447")
c.line(18,46,64,73,roof_d)
c.line(64,73,110,46,"#641f2a")
# tile courses, snapped to 45-degree roof geometry
for y in (32,40,48,56,64):
    # left slope tile seams
    x0 = 64 - (y-18)*47//26
    c.line(max(18,x0), y+1, 64, y + (y-18)*31//57, roof_d)
for x in (29,40,51,61):
    c.line(x, 44-(x-17)*26//47, x+12, 51-(x-17)*26//47, roof_hi)
for x in (68,79,90,101):
    c.line(x-4, 21+(x-64)*26//47, x+7, 27+(x-64)*26//47, "#a83235")
# segmented tile rows across each plane
for y in (39,48,57,66):
    c.line(max(18, 64-(y-18)*47//26), y, 64, 18+(y-18)*57//31, "#d04739")
    c.line(64, 18+(y-18)*57//31, 64+(y-18)*47//26, y, "#76252e")

# Chimney rising from rear-right roof plane
c.poly([(79,25),(88,20),(99,26),(90,31)], "#9b4037")
c.poly([(79,25),(90,31),(90,45),(79,39)], "#71342f")
c.poly([(90,31),(99,26),(99,40),(90,45)], "#512d2d")
c.poly([(77,23),(88,17),(101,24),(90,30)], "#c45b45")
c.line(80,25,90,30,"#ef8260")
c.line(90,30,100,24,roof_d)
c.rect(85,31,3,4,metal)
c.rect(94,29,3,4,metal)

# Furnace mouth on right wall, framed in stone
c.poly([(78,77),(94,68),(103,73),(86,83)], stone_l)
c.poly([(78,77),(86,83),(86,95),(78,90)], stone_d)
c.poly([(86,83),(103,73),(103,86),(86,96)], metal)
c.poly([(88,84),(100,77),(100,86),(88,93)], glow)
c.poly([(90,85),(98,80),(98,86),(90,91)], glow_l)
c.poly([(91,89),(97,85),(97,89),(91,92)], coal)
c.line(78,77,86,83,cream)
c.line(86,83,103,73,stone)
# Furnace tools and warm light pixels
c.set(105,84,"#ffca62")
c.set(108,82,"#ffca62")
c.line(102,93,109,89,wood_d)
c.line(108,86,111,84,metal)

# Small dark window on left-facing wall
c.poly([(31,59),(42,65),(42,76),(31,70)], wood_d)
c.poly([(33,61),(40,65),(40,72),(33,68)], "#283a41")
c.line(36,63,36,70,cream)
c.line(33,66,40,70,cream)

# Wooden hanging sign on left side
c.line(49,69,49,79,wood_d)
c.poly([(43,73),(54,79),(54,89),(43,83)], wood_d)
c.poly([(44,74),(53,79),(53,86),(44,81)], wood_l)
c.line(45,76,52,80,cream)
c.set(49,81,cream)
c.line(45,83,50,85,wood_d)

# Stacked barrels beside the building, with pixel highlights and hoops
# front lower barrel
c.poly([(20,78),(27,74),(35,79),(35,91),(27,96),(20,92)], wood_d)
c.poly([(21,79),(27,76),(34,80),(34,90),(27,94),(21,91)], wood_l)
c.ellipse(27,80,5,2,"#bd8050")
c.line(22,84,33,88,metal)
c.line(22,89,33,93,metal)
c.line(23,80,23,90,wood_hi if False else cream)
c.set(31,83,wood_d)
# upper rear barrel
c.poly([(31,68),(37,65),(44,69),(44,79),(37,83),(31,79)], wood_d)
c.poly([(32,69),(37,67),(43,70),(43,78),(37,81),(32,78)], "#98613f")
c.ellipse(37,70,5,2,"#c18a56")
c.line(32,74,43,77,metal)
c.line(33,69,33,78,cream)

# Forge-side stacked split logs and small anvil
c.rect(95,97,11,3,wood_d)
c.line(96,96,105,92,wood_l)
c.line(99,99,108,95,wood_l)
c.rect(109,91,7,3,metal)
c.poly([(109,90),(112,87),(118,88),(116,91)], "#788184")
c.rect(111,91,3,5,metal)
c.line(109,96,116,96,stone_l)

# Final pixel accents and edge definition
c.line(20,52,64,76,cream)
c.line(64,76,108,52,stone_l)
c.line(20,52,20,76,wood_d)
c.line(108,52,108,76,wood_d)
c.line(64,102,64,108,stone_d)

print(c.stats_text())
print(c.matrix_text(region=(58,16,70,32)))
finish(c)
