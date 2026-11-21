# Cyberpunk alley — 128x128, compact indexed-style palette
c = new_canvas(128, 128, '#080d1c', name='cyberpunk_alley')

# Palette
ink = '#080d1c'
night = '#10182b'
shadow = '#18243a'
wall = '#20283b'
wall2 = '#303849'
concrete = '#485264'
steel = '#647181'
cyan = '#37e6e8'
blue = '#348cff'
pink = '#ff3e9d'
orange = '#ffae46'
yellow = '#ffe887'
red = '#ff596b'
white = '#d9f8f5'
water = '#142c42'

# Distant rainy sky and alley opening
c.rect(0, 0, 128, 128, ink)
c.rect(42, 0, 45, 76, '#0c1425')
# faint distant towers
for x, w, h in [(45,8,31),(57,7,43),(69,6,27),(78,8,36)]:
    c.rect(x, 43-h, w, h, '#111d31')
    for yy in range(46-h, 41, 8):
        c.rect(x+2, yy, 2, 2, '#263750')
# rain streaks in open sky
for x,y,l in [(47,12,5),(53,27,7),(61,6,4),(72,18,6),(80,8,5),(43,35,6),(67,39,4),(84,30,7),(58,48,4)]:
    c.line(x,y,x-2,y+l, '#26364b')

# Side walls create a strong funnel perspective
c.poly([(0,0),(39,0),(46,68),(40,83),(0,91)], wall)
c.poly([(91,0),(128,0),(128,91),(88,83),(82,68)], '#1b2235')
# left wall panels and edges
c.poly([(0,0),(8,0),(10,87),(0,89)], '#303849')
c.line(39,0,46,68, steel)
c.line(0,65,43,66, '#485267')
c.line(0,69,43,70, '#11192a')
c.rect(3,12,31,2,'#3c4557')
c.rect(8,17,24,2,'#121a2b')
c.rect(5,47,31,2,'#515b69')
c.rect(0,51,40,2,'#11192a')
# right wall structure
c.poly([(119,0),(128,0),(128,90),(119,88)], '#30394b')
c.line(91,0,82,68, '#657080')
c.line(85,64,128,66, '#586477')
c.line(84,69,128,72, '#0c1423')
c.rect(95,14,29,2,'#0c1425')
c.rect(97,18,31,2,'#51596b')

# Windows and lit panels left
c.rect(4,23,12,17, '#0a1323'); c.rect(6,25,8,12, '#253449')
c.rect(8,26,2,10, cyan); c.rect(11,28,2,8, '#1d7d9c')
c.rect(20,22,14,20, '#0a1323'); c.rect(22,24,10,15, '#33233c')
c.rect(24,26,3,4,pink); c.rect(29,31,2,7,'#86334f')
c.rect(4,75,16,5,'#111827'); c.rect(6,72,10,3,wall2)
# right windows
c.rect(101,22,17,22, '#0a1323'); c.rect(103,24,13,17,'#27364a')
c.rect(105,26,4,12, '#f4a15b'); c.rect(111,28,3,10, '#d36660')
c.rect(121,28,5,20,'#101629'); c.rect(122,31,2,13,blue)
c.rect(106,76,17,5,'#101827'); c.rect(109,72,11,4,wall2)

# Neon shop sign on left, projecting into alley
c.rect(12,43,30,19, '#0a1221')
c.rect(13,44,28,16, '#24253c')
c.rect(14,45,26,2,pink); c.rect(14,57,26,2,pink)
c.rect(14,45,2,14,pink); c.rect(38,45,2,14,pink)
c.text(18,49,'RAMEN',yellow,font='5x7')
c.rect(26,61,2,9,steel); c.rect(16,69,22,2,steel)
# smaller blue vertical sign right
c.rect(90,32,12,31, '#111729')
c.rect(91,33,10,29, blue); c.rect(93,35,6,25, '#15243c')
c.text(93,37,'夜',white,font='8px')
c.text(93,48,'BAR',cyan,font='5x7')
c.rect(95,63,2,8,steel)
# red shop marker farther left
c.rect(1,58,10,15, '#111827'); c.rect(2,59,8,13, red)
c.rect(4,61,4,2,white); c.rect(4,65,4,4,'#511f38')

# Awning and storefront beneath left sign
c.poly([(0,72),(43,68),(47,77),(0,83)], '#131b2b')
c.line(0,72,43,68, cyan)
for x in range(3,43,8):
    c.poly([(x,72-(x//8)),(x+4,72-(x//8)),(x+6,79),(x+2,80)], '#303448')
c.rect(1,81,37,5,'#0b1423')
# storefront windows glow
c.poly([(3,84),(19,82),(19,99),(3,103)], '#11182a')
c.poly([(5,86),(17,84),(17,96),(5,99)], '#1c4655')
c.line(11,85,11,98,cyan); c.line(5,92,17,90,'#4da9ab')
c.poly([(22,82),(38,80),(39,94),(22,97)], '#121a2a')
c.rect(25,84,10,9,'#594255'); c.rect(27,86,2,5,orange); c.rect(31,85,2,6,pink)

# Right storefront + vending machines
c.poly([(88,69),(128,72),(128,83),(84,79)], '#101827')
c.line(88,70,128,73, pink)
c.rect(102,80,22,22,'#080f1d')
c.rect(104,82,9,18,'#17283c'); c.rect(115,82,7,18,'#222a3c')
# vending machine face and bright display
c.rect(105,83,8,13,'#286179'); c.rect(106,84,6,8,'#9be8de')
c.rect(106,84,6,2,cyan); c.rect(106,87,2,2,pink); c.rect(110,87,2,2,orange)
c.rect(106,93,6,2,blue); c.rect(116,84,5,9,'#35384b')
for x,y,col in [(116,85,red),(119,85,yellow),(116,88,cyan),(119,88,pink),(116,91,orange),(119,91,blue)]: c.rect(x,y,2,2,col)
c.rect(105,97,17,2,steel); c.rect(109,99,9,2,wall2)
# secondary vending machine at right edge
c.rect(124,82,4,17,'#101827'); c.rect(125,84,2,8,cyan)

# Ground plane, perspective converges around (64,70)
c.poly([(0,88),(40,80),(87,80),(128,89),(128,128),(0,128)], '#101a2b')
c.poly([(0,99),(43,84),(86,84),(128,100),(128,128),(0,128)], '#142437')
# curb / pavement perspective lines
c.line(0,92,43,82, '#647181'); c.line(128,93,85,82, '#657080')
c.line(0,106,54,87, '#28384c'); c.line(128,106,74,87, '#29394d')
c.line(0,119,59,91, '#25374b'); c.line(128,119,69,91, '#26374a')
# paving joints
c.line(21,128,57,87,'#1e3044'); c.line(101,128,71,87,'#1e3044')
c.line(0,113,128,112,'#192b3e')
c.line(0,124,128,123,'#1d3045')
# distant street lights and haze
c.rect(61,66,2,13, '#586477'); c.rect(58,64,8,2,cyan)
c.rect(43,72,2,9, '#46536a'); c.rect(41,70,7,2,pink)
c.rect(80,71,2,10, '#49566a'); c.rect(78,69,7,2,orange)

# Power cables overhead, sagging in the alley
c.path('M 0 18 Q 34 39 62 22', '#050914', fill=False)
c.path('M 0 19 Q 34 40 62 23', '#465063', fill=False)
c.path('M 128 13 Q 103 36 63 25', '#050914', fill=False)
c.path('M 128 14 Q 103 37 63 26', '#465063', fill=False)
c.line(28,31,30,37,'#111827'); c.line(95,29,93,36,'#111827')
c.rect(28,37,3,2,steel); c.rect(92,36,3,2,steel)

# Rain streaks across the street, sparse and directional
for x,y,l in [(8,92,7),(19,101,5),(31,89,6),(47,96,8),(56,86,5),(72,94,7),(86,88,5),(98,102,7),(112,91,6),(121,107,7),(38,116,5),(77,121,6),(15,74,5),(52,70,4),(109,63,6)]:
    c.line(x,y,x-2,y+l, '#485264')

# Puddles: dark pools with neon broken reflections
c.ellipse(30,111,17,4,water); c.ellipse(93,114,22,5,water); c.ellipse(63,101,9,3,'#183349')
# reflected neon strokes
for x,y,w,col in [(16,108,11,pink),(23,112,19,'#a43f76'),(37,115,8,cyan),(49,99,10,blue),(55,103,6,'#4eb5c8'),(77,112,17,cyan),(83,118,10,'#217c9c'),(97,107,17,orange),(103,113,12,'#bd5d67'),(111,120,9,pink),(57,108,4,yellow),(68,116,5,blue)]:
    c.rect(x,y,w,1,col)
for x,y in [(20,119),(43,107),(71,107),(89,105),(118,111),(5,116),(33,123),(77,125),(108,99)]:
    c.line(x,y,x+5,y, '#738493')

# Lone figure with transparent umbrella silhouette, placed in foreground
# umbrella canopy, translucent read via alternating dark panels and bright rim
c.path('M 48 82 Q 50 68 64 66 Q 79 68 81 82 Q 76 78 72 82 Q 68 78 64 82 Q 60 78 56 82 Q 52 78 48 82 Z', '#183247')
c.path('M 48 82 Q 50 68 64 66 Q 79 68 81 82', cyan, fill=False)
c.line(48,82,56,82,cyan); c.line(56,82,64,82,cyan); c.line(64,82,72,82,cyan); c.line(72,82,81,82,cyan)
c.line(64,67,64,84,'#80f3ef'); c.line(55,72,58,82,'#4a8594'); c.line(73,72,70,82,'#4a8594')
# head and coat
c.circle(64,86,3,'#d9a17d')
c.rect(61,85,6,2,'#131a2a') # hood/hair cap
c.poly([(60,90),(68,90),(71,105),(69,117),(59,117),(57,105)], '#080d18')
c.poly([(61,91),(67,91),(69,105),(67,114),(61,114),(59,104)], '#202c40')
# coat seams and collar
c.poly([(61,90),(64,93),(68,90),(67,96),(61,96)], '#ff3e9d')
c.line(64,96,64,112,cyan); c.line(60,104,57,111,'#7b8790'); c.line(68,103,72,109,'#7b8790')
# legs and boots
c.line(61,115,59,123,'#101523'); c.line(67,115,69,123,'#101523')
c.rect(56,122,5,2,steel); c.rect(68,122,5,2,steel)
# handle from canopy to hand
c.line(64,82,65,89,white); c.line(65,89,68,91,white)
# tiny puddle shadow beneath person
c.ellipse(64,126,12,2,'#0a1421'); c.line(54,126,60,126,cyan); c.line(68,126,75,126,pink)

# Accent glows as crisp pixels around signage and wet surfaces
c.rect(40,49,1,7,pink); c.rect(89,41,1,9,blue)
c.rect(100,74,2,1,pink); c.rect(39,79,2,1,cyan)
c.rect(11,104,5,1,'#a84c7e'); c.rect(115,105,6,1,'#d78565')

view(c)
print(c.palette())
finish(c)
