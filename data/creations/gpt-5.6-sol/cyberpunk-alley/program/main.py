from pixelbench_api import *

# Cyberpunk alley at rainy night, built in a compact hand-pixelled palette.
c = new_canvas(128, 128, '#070914', name='cyberpunk_alley')

# Palette
sky = '#0b1022'; far = '#11182b'; deep = '#080b18'; ink = '#050712'
blueblack = '#0b1422'; wall_l = '#13192b'; wall_l2 = '#1b2033'
wall_r = '#171326'; wall_r2 = '#241a32'; edge = '#28304a'
cyan = '#1ff5e9'; cyan2 = '#12aeb7'; cyan3 = '#145d70'; pale = '#b9fff7'
mag = '#ff2da8'; mag2 = '#a91678'; mag3 = '#59154e'; pink = '#ff91dc'
yellow = '#ffd45a'; orange = '#ed6a3a'; white = '#e7faff'
road = '#0b1220'; road2 = '#101c2a'; puddle = '#172c3b'; steel = '#34465a'
purple = '#533c83'; rain = '#718ba8'; skin = '#d8a28f'

# Distant sky and alley mouth.
c.rect(22, 0, 84, 72, sky)
c.rect(42, 16, 47, 55, far)
c.poly([(48,18),(84,18),(78,68),(53,68)], '#151e33')
c.rect(58, 25, 18, 38, '#19273a')
c.rect(62, 34, 10, 29, '#102031')
c.rect(65, 40, 4, 23, cyan3)
c.rect(66, 42, 2, 17, cyan2)

# Left architecture, stepped and heavily shadowed.
c.poly([(0,0),(39,0),(39,53),(47,67),(38,80),(0,91)], wall_l)
c.rect(0, 0, 9, 78, '#0a0d19')
c.rect(10, 7, 5, 67, wall_l2)
c.rect(17, 0, 21, 68, '#101524')
c.rect(20, 13, 15, 3, edge)
c.rect(21, 17, 12, 15, '#090d18')
c.rect(23, 19, 3, 9, cyan3)
c.rect(29, 19, 2, 9, mag3)
c.rect(35, 30, 7, 35, '#090d18')
c.line(39, 0, 39, 53, '#35405b')
c.line(40, 52, 48, 67, edge)
# Pipes and utility boxes left.
c.rect(2, 35, 4, 35, '#222b3b')
c.rect(3, 38, 1, 29, steel)
c.rect(8, 57, 10, 13, '#0b111e')
c.rect(9, 58, 8, 11, '#273044', fill=False)
c.rect(11, 61, 4, 2, orange)
c.line(17, 62, 35, 64, '#384158')

# Right architecture and projecting awnings.
c.poly([(94,0),(128,0),(128,94),(88,79),(84,66),(92,50)], wall_r)
c.rect(106, 0, 22, 77, '#100d1b')
c.rect(95, 10, 10, 57, wall_r2)
c.line(94, 0, 94, 49, '#3d2947')
c.poly([(90,48),(128,44),(128,53),(87,57)], '#0a0b16')
c.line(91, 48, 127, 45, mag3)
c.rect(110, 55, 18, 24, '#16101f')
c.rect(113, 58, 13, 17, '#080a13')
c.rect(115, 61, 8, 2, purple)
c.rect(115, 66, 6, 6, '#19273a')
# Right drain pipe.
c.rect(123, 8, 3, 77, '#273044')
c.rect(124, 10, 1, 72, '#566078')

# Perspective ground.
c.poly([(0,77),(38,66),(89,66),(128,83),(128,128),(0,128)], road)
c.poly([(38,68),(88,68),(110,128),(17,128)], road2)
c.line(38, 68, 17, 127, '#263447')
c.line(88, 68, 110, 127, '#263447')
c.line(0, 84, 45, 69, '#222a3c')
c.line(128, 89, 85, 69, '#32243b')
# Pavement seams.
c.line(0, 103, 31, 91, '#141f2d')
c.line(128, 108, 98, 94, '#1c2030')
c.line(29, 124, 50, 72, '#172536')
c.line(100, 126, 80, 71, '#242032')

# Neon signs, left vertical and small shop sign.
c.rect(14, 33, 17, 5, '#081017')
c.rect(15, 34, 15, 3, cyan)
c.rect(16, 35, 12, 1, pale)
c.rect(4, 8, 12, 38, '#21142d')
c.rect(5, 9, 10, 36, mag2)
c.rect(7, 11, 6, 31, '#351342')
# stylized vertical glyphs
for y in (13,21,30,38):
    c.rect(8, y, 4, 2, pink)
    c.set(8, y+2, mag)
    c.set(11, y-1, mag)
c.rect(4, 8, 12, 38, mag3, fill=False)
c.line(16, 12, 21, 12, '#572047')
c.line(16, 42, 21, 42, '#572047')
# left cyan spill
c.rect(16, 42, 18, 2, cyan3)
c.rect(18, 44, 16, 1, '#113d50')

# Right neon signage.
c.rect(99, 15, 21, 26, '#0a0c19')
c.rect(100, 16, 19, 24, mag3)
c.rect(102, 18, 15, 20, '#24112f')
c.rect(104, 20, 11, 2, mag)
c.rect(102, 25, 12, 2, pink)
c.rect(105, 30, 10, 2, mag)
c.rect(102, 35, 8, 2, pink)
c.rect(99, 15, 21, 26, mag2, fill=False)
c.rect(91, 43, 22, 6, '#071118')
c.rect(92, 44, 20, 4, cyan2)
c.rect(94, 45, 16, 2, pale)
# bracket
c.line(95, 15, 89, 15, steel); c.line(89,15,89,24,steel)

# Vending machine on right foreground.
c.rect(96, 65, 24, 36, '#111b29')
c.rect(98, 67, 20, 31, '#26364a')
c.rect(100, 69, 16, 15, '#0b1522')
c.rect(101, 70, 14, 4, cyan3)
c.rect(102, 71, 5, 2, cyan)
c.rect(109, 71, 5, 2, yellow)
c.rect(101, 76, 14, 7, '#17283a')
for x,col in [(102,cyan2),(106,mag),(110,yellow)]:
    c.rect(x,77,3,4,col)
c.rect(101, 86, 10, 2, '#5b6f81')
c.rect(113, 86, 3, 7, '#0a0d16')
c.set(114,88,mag)
c.rect(99, 96, 4, 3, ink); c.rect(114,96,4,3,ink)
c.line(97, 65, 92, 68, '#3d5269')

# Small vending unit on left.
c.rect(1, 72, 23, 28, '#111927')
c.rect(3, 74, 18, 13, '#263448')
c.rect(5, 76, 14, 4, '#0a101b')
c.rect(5, 81, 4, 4, cyan2); c.rect(10,81,4,4,mag2); c.rect(15,81,4,4,yellow)
c.rect(4, 90, 10, 2, '#607088'); c.rect(17,89,3,7,'#070a12')
c.rect(3, 98, 4, 3, ink); c.rect(18,98,4,3,ink)

# Wet puddles and reflected neon, broken into pixel clusters.
c.poly([(28,88),(50,84),(61,88),(55,93),(34,94),(22,91)], puddle)
c.poly([(74,102),(105,99),(121,108),(111,116),(80,115),(65,109)], '#152939')
c.poly([(35,111),(66,107),(86,114),(77,123),(43,124),(23,119)], '#122536')
# Cyan reflections.
c.rect(42, 87, 14, 2, cyan3); c.rect(35,90,20,1, cyan2)
c.rect(47,93,8,1, cyan)
c.rect(81,104,18,2, cyan3); c.rect(76,108,28,2, cyan2)
c.rect(84,112,13,2, cyan); c.rect(89,116,7,1, pale)
c.rect(31,116,23,2, cyan3); c.rect(39,120,18,2, cyan2)
# Magenta reflections.
c.rect(103,94,10,1, mag2); c.rect(104,97,15,2, mag3)
c.rect(104,103,12,2, mag2); c.rect(109,107,8,2, mag)
c.rect(13,105,12,2, mag3); c.rect(8,111,17,2, mag2); c.rect(5,116,10,2, mag)
c.rect(61,117,13,2, mag3); c.rect(64,122,9,2, mag2)
# puddle glints
for x,y,w in [(2,124,14),(21,102,12),(25,97,5),(76,91,9),(115,121,11),(48,101,8),(96,125,17)]:
    c.rect(x,y,w,1,steel)

# Power and data cables across the open sky.
c.line(0, 18, 45, 27, '#03050c'); c.line(45,27,83,21,'#03050c'); c.line(83,21,127,29,'#03050c')
c.line(0, 25, 50, 34, '#24263a'); c.line(50,34,93,29,'#24263a'); c.line(93,29,127,35,'#24263a')
c.line(32,0,48,33,'#050711'); c.line(115,0,88,34,'#050711')
c.rect(47,25,3,5,'#33364a'); c.rect(86,27,3,5,'#33364a')

# Person: transparent umbrella effect via sparse tinted canopy and visible ribs.
# Canopy dark underfill preserves a readable silhouette against bright alley.
c.poly([(48,76),(51,71),(57,67),(66,65),(75,67),(82,72),(85,77)], '#132536')
# Dithered translucent-looking panels.
c.dither(52,69,12,7,[cyan3,'#18334a'],pattern='checker')
c.dither(65,67,16,9,['#20314b',mag3],pattern='checker')
# crisp canopy rim and ribs
c.line(48,76,85,77,pale)
c.line(50,75,57,69,cyan2); c.line(57,69,66,66,cyan2)
c.line(66,66,75,69,purple); c.line(75,69,84,76,mag2)
c.line(66,66,66,78,steel)
c.set(48,75,cyan); c.set(85,76,mag)
# Head, coat and legs.
c.rect(62,77,8,8,ink)
c.rect(64,78,4,5,skin)
c.rect(61,83,11,24,'#080b13')
c.poly([(61,86),(56,101),(60,103),(64,93)], '#070910')
c.poly([(71,87),(77,101),(73,103),(68,94)], '#070910')
c.rect(62,104,4,15,ink); c.rect(68,104,4,15,ink)
c.rect(59,118,7,3,'#02040a'); c.rect(68,118,8,3,'#02040a')
# Coat rim lighting.
c.line(61,84,58,101,cyan); c.line(58,101,62,104,cyan2)
c.line(71,84,75,101,mag); c.line(75,101,71,104,mag2)
c.line(62,105,62,116,cyan3); c.line(71,105,71,116,mag3)
# Umbrella shaft and curved handle.
c.line(66,76,66,101,steel)
c.line(66,100,68,103,white); c.line(68,103,70,101,white)

# Rain streaks: varied length and spacing, kept off the face.
for x,y,l in [(3,4,6),(20,2,4),(27,47,5),(43,5,7),(52,38,4),(59,8,6),(72,4,5),(82,35,6),(90,3,7),(121,43,5),(35,76,5),(89,74,4),(27,103,6),(118,104,5),(16,53,4),(78,84,4),(46,79,3),(93,54,5),(10,101,4),(123,88,4)]:
    c.line(x,y,x-1,y+l,rain)
# bright near-field rain
for x,y in [(31,7),(55,53),(87,8),(23,68),(93,91),(119,16),(42,107),(80,118)]:
    c.line(x,y,x-1,y+3,white)

# Foreground scattered highlights and curb shine.
c.rect(0,102,18,1,'#40546b'); c.rect(111,91,17,1,'#59405c')
c.set(29,89,pale); c.set(101,107,pink); c.set(58,124,cyan)
c.set(18,117,pink); c.set(116,113,cyan)

result = c
view(result, scale=4, margin=0)
finish(result)
