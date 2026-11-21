# Mountain village at sunrise, 128x128 pixel art
result = new_canvas(128, 128, background="#251f35", name="mountain-village-sunrise")

# Compact dawn palette
sky0 = "#332744"; sky1 = "#4b304b"; sky2 = "#77414f"; sky3 = "#ad5b55"
sky4 = "#dc805e"; sky5 = "#f2ad72"; sun = "#ffd58a"; sun_hi = "#ffe6a6"
far0 = "#5a4960"; far1 = "#66536a"; far2 = "#79606d"; mist = "#b77a72"
mid0 = "#3c4652"; mid1 = "#485563"; mid2 = "#596573"; snow = "#d6b6a2"
ground0 = "#263b3b"; ground1 = "#304943"; ground2 = "#3d594b"; ground3 = "#526550"
pine0 = "#172d31"; pine1 = "#203b38"; pine2 = "#2d4c40"; pine3 = "#3f5d49"
wood0 = "#4b302d"; wood1 = "#674034"; wood2 = "#85543c"; wood3 = "#a96d48"
plaster = "#c79067"; plaster_hi = "#e2b27c"; roof0 = "#382b31"; roof1 = "#56353a"; roof2 = "#74433e"
stone0 = "#4a4a49"; stone1 = "#65605a"; stone2 = "#85766a"; stone3 = "#a58d78"
window = "#ffbd58"; window_hi = "#ffe08a"; smoke0 = "#8b7480"; smoke1 = "#b08d8a"

# Sunrise sky in clean horizontal bands
result.rect(0, 0, 128, 15, sky0)
result.rect(0, 15, 128, 12, sky1)
result.rect(0, 27, 128, 13, sky2)
result.rect(0, 40, 128, 13, sky3)
result.rect(0, 53, 128, 17, sky4)
result.rect(0, 70, 128, 12, sky5)
# subtle pixel clouds
result.rect(8, 20, 22, 2, "#5e3b54").rect(14, 18, 12, 2, "#5e3b54")
result.rect(91, 31, 27, 2, "#92525b").rect(98, 29, 13, 2, "#92525b")
result.rect(4, 46, 25, 2, "#c16a60").rect(11, 44, 12, 2, "#c16a60")
# Blocky sun behind the central valley
result.circle(66, 53, 11, sun)
result.rect(59, 43, 15, 3, sun_hi).rect(56, 47, 21, 6, sun_hi)

# Distant mountain silhouettes
result.poly([(0,53),(10,45),(18,49),(30,36),(41,47),(52,39),(65,52),(75,43),(88,51),(101,35),(111,46),(121,40),(127,46),(127,78),(0,78)], far0)
result.poly([(0,61),(15,51),(25,57),(38,44),(49,57),(62,48),(76,61),(90,48),(101,55),(113,45),(127,57),(127,81),(0,81)], far1)
# far snow ridges
result.poly([(25,48),(30,36),(35,45),(32,43),(29,48)], snow)
result.poly([(96,43),(101,35),(107,44),(103,42),(100,47)], snow)
result.poly([(109,49),(113,45),(118,51),(113,49)], mist)
# nearer blue-gray ridge
result.poly([(0,72),(14,61),(25,68),(39,55),(52,66),(66,58),(80,70),(95,59),(108,70),(119,60),(127,65),(127,88),(0,88)], mid0)
result.poly([(0,78),(18,68),(31,73),(43,63),(56,73),(69,66),(83,76),(98,67),(111,76),(127,70),(127,91),(0,91)], mid1)
result.poly([(39,66),(43,63),(48,68),(44,67)], mid2)
result.poly([(92,70),(98,67),(103,72),(98,70)], mid2)
# mist line separates village basin
result.rect(0, 78, 128, 3, "#8b6f70")
result.rect(20, 76, 32, 2, "#9d7774").rect(80, 77, 39, 2, "#9d7774")

# Rolling village ground
result.poly([(0,82),(18,78),(37,84),(57,78),(76,84),(96,79),(112,83),(127,79),(127,128),(0,128)], ground1)
result.poly([(0,94),(18,88),(36,92),(56,86),(77,91),(96,87),(113,91),(127,86),(127,128),(0,128)], ground2)
result.poly([(0,108),(25,99),(48,105),(70,97),(93,103),(112,97),(127,101),(127,128),(0,128)], ground0)
# fields/terraces
result.line(2,98,36,91,ground3).line(88,94,125,88,ground3)
result.line(1,101,38,94,pine2).line(91,97,127,91,pine2)
result.rect(8,105,22,2,ground1).rect(97,105,25,2,ground1)

# Winding stone path, broad in foreground, narrow at focal house
result.poly([(66,91),(72,91),(75,101),(70,108),(83,128),(45,128),(59,108),(64,101)], stone1)
result.poly([(67,92),(70,92),(72,101),(67,108),(73,128),(52,128),(62,107),(66,100)], stone2)
# path stones
for pts, col in [
    ([(61,122),(67,118),(74,120),(78,125),(72,127),(59,127)],stone3),
    ([(49,124),(55,118),(61,120),(59,127),(49,127)],stone0),
    ([(62,111),(67,108),(72,111),(69,116),(63,116)],stone0),
    ([(69,102),(73,101),(72,106),(68,107)],stone3),
    ([(64,117),(69,116),(68,119),(63,121)],stone1),
    ([(65,97),(70,96),(71,100),(66,101)],stone0)]:
    result.poly(pts,col)

# Pine helper: trunk plus stepped needle tiers
def pine(x, y, h, dark=pine0, light=pine2):
    trunk_w = max(2, h // 12)
    result.rect(x-trunk_w//2, y-h//5, trunk_w, h//5+1, wood0)
    top = y-h
    # broad overlapping pixel triangles
    for frac, half in [(0.18, h//8),(0.34,h//6),(0.52,h//5),(0.70,h//4),(0.87,h//3)]:
        cy = top + int(h*frac)
        result.poly([(x, cy-int(h*.18)),(x-half,cy+int(h*.14)),(x-2,cy+int(h*.11)),(x,cy+int(h*.17)),(x+2,cy+int(h*.11)),(x+half,cy+int(h*.14))], dark)
    result.line(x-2,top+6,x-4,y-5,light)
    result.line(x+1,top+9,x+3,y-10,pine1)

# Back pines establish scale
pine(8,94,29,pine1,pine3); pine(119,94,27,pine1,pine3)
pine(26,91,20,pine1,pine3); pine(101,90,18,pine1,pine3)

# Houses, with roofs drawn after bodies
def house(x, y, w, h, focal=False, door_side="right"):
    wall = plaster_hi if focal else plaster
    # wall and timber frame
    result.rect(x,y,w,h,wall)
    result.rect(x,y,w,3,wood1).rect(x,y,3,h,wood1).rect(x+w-3,y,3,h,wood1)
    result.rect(x+w//2-1,y,3,h,wood2)
    result.line(x+2,y+3,x+w//2,y+h-2,wood2)
    result.line(x+w-3,y+3,x+w//2,y+h-2,wood1)
    # roof overhang, warm sunrise edge
    result.poly([(x-4,y+1),(x+w//2,y-10),(x+w+4,y+1),(x+w+2,y+5),(x-3,y+5)], roof0)
    result.poly([(x-3,y),(x+w//2,y-9),(x+w+3,y),(x+w+1,y+2),(x-2,y+2)], roof2)
    result.line(x-2,y+3,x+w+2,y+3,roof1)
    # door and window
    dx = x+w-9 if door_side == "right" else x+3
    result.rect(dx,y+h-10,6,10,wood0).rect(dx+1,y+h-9,4,9,wood1)
    wx = x+5 if door_side == "right" else x+w-11
    result.rect(wx-1,y+7,9,8,wood0).rect(wx,y+8,7,6,window)
    result.rect(wx+3,y+8,1,6,window_hi).rect(wx,y+11,7,1,window_hi)
    result.set(dx+4,y+h-5,window)

# Side houses first, lower contrast
house(18,81,25,19,False,"left")
house(88,80,24,19,False,"right")
# side chimneys
result.rect(21,69,5,10,wood0).rect(20,68,7,2,roof0)
result.rect(105,69,5,9,wood0).rect(104,68,7,2,roof0)

# Center focal house larger and brightest
house(48,75,39,27,True,"right")
result.rect(55,59,6,12,wood0).rect(54,58,8,2,roof0)
# central door detail and front step
result.rect(74,92,7,10,wood0).rect(75,93,5,9,wood2).set(79,97,window)
result.rect(71,102,13,2,stone0).rect(73,104,10,2,stone2)
# central roof snow/light trim
result.line(47,76,67,64,"#dca16d").line(67,64,89,76,"#b56f52")

# Chimney smoke as staggered pixel clusters drifting left
result.rect(56,54,5,4,smoke0).rect(53,50,8,4,smoke1)
result.rect(48,46,10,4,smoke0).rect(43,43,10,3,"#9c7c84")
result.rect(40,40,8,3,"#7c6474").rect(37,38,6,2,"#6a586b")
# smaller smoke plumes
result.rect(22,63,4,5,smoke0).rect(19,59,7,4,"#816b79").rect(16,56,6,3,"#725e70")
result.rect(106,63,4,5,smoke0).rect(108,59,6,4,"#816b79").rect(111,56,7,3,"#725e70")

# Foreground framing pines overlap scene for depth
pine(5,127,47,pine0,pine2); pine(123,127,50,pine0,pine2)
pine(19,128,35,pine1,pine3); pine(108,128,31,pine1,pine3)
# shadow grasses and rocks in foreground
for x,y in [(28,116),(33,121),(91,115),(97,123),(38,112),(87,110)]:
    result.line(x,y,x-2,y-5,pine2).line(x,y,x+2,y-4,pine3)
result.poly([(25,124),(30,119),(36,121),(38,127),(23,127)],stone0)
result.poly([(91,126),(96,120),(103,121),(106,127)],stone0)
result.rect(28,122,7,2,stone2).rect(96,121,6,2,stone2)
# a few warm window reflections on path
result.set(69,105,"#c78a56").set(65,114,"#9c7158").set(72,123,"#8e6855")

view(result, scale=4, margin=0)
finish(result)
