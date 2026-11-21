# 128x128 magic forest cottage
result = new_canvas(128, 128, background="#160f2e", name="magic-forest-cottage")

# Palette
sky0 = "#160f2e"; sky1 = "#21153f"; sky2 = "#302052"; sky3 = "#49306b"
moon0 = "#fff0b0"; moon1 = "#e8d79b"; moon2 = "#c8b783"
mist0 = "#776b91"; mist1 = "#554b73"; mist2 = "#3c355b"
ground0 = "#171426"; ground1 = "#242035"; ground2 = "#343047"; moss0 = "#26372e"; moss1 = "#40523b"; moss2 = "#647055"
wood0 = "#281b25"; wood1 = "#46302c"; wood2 = "#684536"; wood3 = "#8a5c3d"
stone0 = "#393642"; stone1 = "#56505a"; stone2 = "#756d70"; stone3 = "#928783"
roof0 = "#1e2529"; roof1 = "#2f3b35"; roof2 = "#465442"
light0 = "#ffb83e"; light1 = "#ff792d"; light2 = "#ffe17a"; glow = "#c85b31"
leaf0 = "#261527"; leaf1 = "#452039"; leaf2 = "#652b3d"; leaf3 = "#783947"

# Night sky bands and sparse stars
result.rect(0, 0, 128, 45, sky1)
result.rect(0, 0, 128, 18, sky0)
result.dither(0, 17, 128, 18, [sky1, sky2], pattern="bayer4")
for x,y,c in [(13,13,sky3),(25,26,"#a99ac0"),(47,11,sky3),(61,25,"#c9b8ce"),(76,8,sky3),(111,11,"#b6a5c3"),(119,31,sky3),(7,39,sky3),(53,34,sky3)]:
    result.set(x,y,c)
# Moon halo and moon
result.circle(96, 25, 15, sky2)
result.circle(96, 25, 12, moon1)
result.circle(94, 23, 10, moon0)
result.circle(91, 20, 2, "#f6e5a8")
result.circle(101, 29, 2, moon2)
result.set(88,27,moon2); result.set(89,28,moon2); result.set(99,18,moon1)

# Distant tree line
result.poly([(0,45),(6,36),(10,46),(18,32),(22,46),(29,38),(33,47),(41,31),(45,46),(52,37),(58,47),(66,34),(71,46),(79,37),(84,47),(93,34),(99,46),(108,36),(114,47),(121,31),(128,44),(128,67),(0,67)], "#19182a")
result.poly([(0,54),(12,46),(20,55),(34,43),(46,54),(62,46),(77,56),(90,43),(106,55),(119,44),(128,51),(128,72),(0,72)], "#24243a")

# Twisted ancient trees, behind cottage
# left trunk and branches
result.path("M0 82 L0 18 L7 17 L11 38 L16 27 L20 28 L14 45 L23 39 L26 42 L15 54 L18 73 Z", wood0)
result.path("M4 60 L7 20 L10 39 L9 67 Z", wood1)
result.path("M7 25 C16 18 20 12 25 4 L28 5 C25 18 19 26 10 33 Z", wood0)
result.path("M8 34 C19 31 27 24 34 17 L36 20 C29 31 20 38 9 42 Z", wood0)
# right trunk and moon-crossing branch
result.path("M113 75 C116 58 117 43 115 31 C112 21 116 10 123 0 L128 0 L128 86 Z", wood0)
result.path("M119 43 C108 36 103 29 101 20 L104 18 C109 28 116 32 123 34 Z", wood0)
result.path("M120 29 C108 22 97 18 83 18 L82 15 C99 12 114 17 124 23 Z", wood0)
result.path("M121 16 C111 11 106 5 102 0 L109 0 C114 6 120 8 126 10 Z", wood1)
result.path("M120 51 C109 48 102 43 97 37 L100 34 C107 41 116 43 124 44 Z", wood1)
# bark highlights
result.line(4,43,5,71,wood2); result.line(9,47,11,66,wood2)
result.line(120,39,119,69,wood2); result.line(123,20,125,54,wood1)

# Leaf clusters framing sky
for cx,cy,r,c in [(3,17,8,leaf0),(13,14,7,leaf1),(22,9,8,leaf0),(31,16,6,leaf2),(5,33,7,leaf1),(20,29,6,leaf0),(35,25,5,leaf1),(115,8,8,leaf0),(126,15,9,leaf1),(112,23,6,leaf2),(126,33,8,leaf0),(108,40,5,leaf1)]:
    result.circle(cx,cy,r,c)
# blocky leaf highlights
for x,y,c in [(15,11,leaf2),(20,7,leaf3),(29,15,leaf3),(6,27,leaf2),(31,24,leaf2),(117,7,leaf2),(122,19,leaf3),(111,22,leaf3),(121,35,leaf2)]:
    result.rect(x,y,3,2,c)

# Ground planes
result.poly([(0,70),(23,66),(47,70),(71,65),(96,69),(128,62),(128,128),(0,128)], ground0)
result.poly([(0,87),(23,79),(50,82),(77,75),(102,82),(128,75),(128,128),(0,128)], ground1)
result.dither(0, 94, 128, 34, [ground1, ground0], pattern="bayer4")
# low mist strips behind cottage
result.path("M0 69 C18 64 31 69 43 66 C58 62 69 69 84 65 C101 61 112 65 128 59 L128 70 C109 68 98 72 84 70 C65 74 53 68 38 72 C22 75 11 70 0 74 Z", mist2)
result.path("M0 78 C19 74 32 78 46 75 C61 72 74 77 90 74 C106 70 116 74 128 70 L128 77 C112 76 101 80 88 78 C71 81 57 77 42 80 C26 83 12 79 0 82 Z", mist1)

# Cottage body, irregular stone walls
result.poly([(30,61),(84,58),(91,103),(25,106)], stone0)
result.rect(28,69,60,34,stone1)
# stone blocks
for x,y,w,h,c in [(30,72,10,5,stone2),(42,70,12,6,stone0),(57,70,10,5,stone2),(70,68,14,6,stone0),(27,80,13,7,stone0),(42,79,10,6,stone2),(55,78,14,7,stone0),(72,77,15,7,stone2),(29,90,9,6,stone2),(40,88,14,7,stone0),(57,88,11,6,stone2),(72,87,15,7,stone0),(27,99,12,5,stone0),(42,98,13,5,stone2),(69,97,17,6,stone2)]:
    result.rect(x,y,w,h,c)
# mortar chips
for x,y in [(35,78),(49,86),(63,76),(80,85),(32,97),(61,96),(83,73)]: result.set(x,y,stone3)

# Steep mossy roof outline and roof
result.poly([(19,65),(49,28),(61,27),(96,62),(91,69),(52,42),(28,70)], roof0)
result.poly([(24,62),(50,31),(59,31),(90,62),(86,64),(55,40),(31,66)], roof1)
# roof plank/tile diagonal texture
result.line(35,57,52,36,roof2); result.line(48,57,60,40,roof2); result.line(62,48,76,61,roof2)
result.line(28,65,45,62,moss2); result.line(53,39,66,50,moss1); result.line(40,50,55,44,moss1)
result.rect(31,59,9,4,moss1); result.rect(66,53,8,4,moss0); result.rect(77,60,9,3,moss2)
for x,y in [(34,57),(39,56),(45,47),(53,40),(57,43),(68,52),(73,58),(82,61)]: result.set(x,y,moss2)
# crooked chimney
result.poly([(70,42),(70,25),(79,24),(80,50)], stone0)
result.rect(69,24,11,4,stone2); result.rect(73,29,6,5,stone1); result.rect(71,35,8,5,stone2)
# smoke
result.path("M75 22 C69 17 73 13 80 12 C86 10 84 6 80 3 C88 5 93 10 88 14 C84 18 80 17 75 22 Z", mist2)

# Timber framing
result.rect(47,65,4,39,wood0); result.rect(71,64,4,39,wood0)
result.line(29,70,88,66,wood1); result.line(29,87,88,84,wood1)
result.line(31,70,48,85,wood1); result.line(72,84,87,68,wood1)
# Door with warm spill
result.poly([(51,76),(66,75),(67,103),(50,104)], wood0)
result.rect(54,79,10,24,wood2)
result.rect(56,81,7,17,light1)
result.rect(57,81,5,16,light0)
result.set(60,86,light2); result.set(63,94,wood3)
# windows, dark frames and glow
result.rect(31,75,14,14,wood0); result.rect(34,77,9,9,light1); result.rect(35,77,7,8,light0)
result.line(39,77,39,86,wood1); result.line(34,82,43,82,wood1)
result.rect(75,72,12,13,wood0); result.rect(77,74,8,8,light0)
result.line(81,74,81,82,wood1); result.line(77,78,85,78,wood1)
# warm reflected pixels
result.rect(46,104,26,3,glow); result.dither(49,107,20,5,[glow,ground1],pattern="checker")

# foreground stone path, widening toward viewer
result.poly([(55,105),(67,105),(91,128),(31,128)], ground2)
for pts,c in [([(52,108),(67,107),(71,112),(48,113)],stone2), ([(43,115),(72,114),(78,120),(38,121)],stone1), ([(34,123),(81,122),(91,128),(29,128)],stone2)]:
    result.poly(pts,c)
result.line(57,109,59,112,stone3); result.line(55,116,57,120,stone0); result.line(67,123,70,127,stone3)
# grass/moss tufts
for x,y in [(18,103),(24,112),(92,107),(101,117),(15,122),(112,97),(7,109)]:
    result.line(x,y,x-2,y-5,moss1); result.line(x,y,x+1,y-6,moss2); result.line(x,y,x+3,y-3,moss0)

# Stone well on right foreground
result.ellipse(101,91,15,6,stone0)
result.rect(87,90,29,19,stone0)
result.ellipse(101,107,15,6,stone0)
result.rect(88,91,27,15,stone1)
result.ellipse(101,91,13,5,stone2)
result.ellipse(101,91,9,3,ground0)
# well masonry
result.line(88,98,114,98,stone0); result.line(93,92,93,106,stone0); result.line(106,92,106,106,stone0)
result.rect(89,100,4,3,stone2); result.rect(99,100,6,3,stone2); result.rect(108,101,6,3,stone2)
# winch posts and roofless crossbeam
result.rect(87,71,4,22,wood1); result.rect(112,70,4,23,wood0)
result.rect(85,69,33,4,wood2); result.rect(90,70,24,2,wood3)
result.circle(102,80,4,wood0); result.circle(102,80,2,wood3)
result.rect(101,73,2,17,wood1); result.line(104,80,111,84,wood2); result.set(112,85,wood3)
# bucket rope disappears into well
result.line(102,82,102,91,"#9a7652")

# Foreground mist wisps crossing feet, kept pixel-solid
result.path("M0 106 C15 101 24 105 36 103 C46 101 51 103 58 106 C46 105 37 108 25 107 C15 109 8 109 0 111 Z", mist2)
result.path("M75 113 C88 109 99 112 109 109 C116 107 122 108 128 107 L128 113 C118 112 113 114 104 114 C92 116 83 115 75 113 Z", mist1)
# foreground leaf litter
for x,y,c in [(7,116,leaf2),(20,110,leaf3),(82,118,leaf1),(116,121,leaf2),(94,112,leaf3),(14,126,leaf1),(121,104,leaf3)]:
    result.rect(x,y,3,1,c); result.set(x+1,y-1,c)

# Crisp selective outlines/details and a few distant fairy lights
result.line(25,105,48,104,wood0)
result.set(42,74,light2); result.set(84,75,light2)
for x,y in [(20,58),(24,55),(106,57),(111,61),(17,93)]:
    result.set(x,y,light0)
for x,y in [(20,57),(106,56)]:
    result.set(x,y,light2)
result.set(22,59,glow); result.set(109,60,glow)

view(result, scale=4, margin=0)
finish(result)
