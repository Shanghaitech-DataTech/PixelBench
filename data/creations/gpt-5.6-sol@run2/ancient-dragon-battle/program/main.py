# Ancient dragon battle, 256x256 pixel art
result = new_canvas(256, 256, background="#1a1420", name="ancient-dragon-battle")

# Palette
sky0 = "#24172d"; sky1 = "#44223a"; sky2 = "#783444"; sky3 = "#b95043"
sky4 = "#e07b49"; sun = "#f6c56a"; ink = "#17131b"; deep = "#251b26"
mount0 = "#352438"; mount1 = "#493044"; stone0 = "#34313a"; stone1 = "#4b4650"
stone2 = "#68606a"; stone3 = "#8b7880"; smoke0 = "#29232c"; smoke1 = "#40323a"
smoke2 = "#5b4143"; flame0 = "#9e302d"; flame1 = "#e55332"; flame2 = "#ff9a3c"
flame3 = "#ffd36a"; metal0 = "#77727b"; metal1 = "#b0a3a0"; red = "#842d35"
red2 = "#bd3e38"; gold = "#d49a45"; wood0 = "#3b2725"; wood1 = "#64402c"
wood2 = "#8a5a32"; dragon0 = "#211923"; dragon1 = "#403044"; dragon2 = "#68454b"
dragon3 = "#a55d4a"; eye = "#ffe36e"; earth0 = "#211a22"; earth1 = "#322329"

# Sunset bands
result.rect(0, 0, 256, 34, sky0)
result.rect(0, 34, 256, 31, sky1)
result.rect(0, 65, 256, 29, sky2)
result.rect(0, 94, 256, 28, sky3)
result.rect(0, 122, 256, 28, sky4)
# Horizontal sky streaks and dithering
result.rect(8, 25, 74, 3, sky1); result.rect(22, 30, 48, 2, sky1)
result.rect(170, 42, 66, 3, sky2); result.rect(192, 49, 44, 2, sky2)
result.rect(2, 70, 54, 2, sky3); result.rect(13, 76, 31, 2, sky3)
result.rect(177, 77, 71, 3, sky3); result.rect(202, 84, 38, 2, sky3)
result.dither(0, 88, 256, 18, [sky2, sky3], pattern="bayer4")
result.dither(0, 106, 256, 20, [sky3, sky4], pattern="checker")
# Sun behind smoke
result.circle(190, 104, 21, sun)
result.rect(171, 105, 39, 4, sky4); result.rect(176, 114, 31, 3, sky4)

# Distant mountains
result.poly([(0,125),(22,103),(34,112),(55,87),(69,105),(83,96),(103,126)], mount0)
result.poly([(64,126),(91,104),(106,112),(127,85),(143,107),(157,97),(181,126)], mount1)
result.poly([(151,126),(175,102),(188,111),(207,88),(224,107),(239,97),(256,119),(256,143),(151,143)], mount0)
# Snow/rim highlights
result.poly([(49,94),(55,87),(61,96),(57,94),(54,101)], stone3)
result.poly([(120,93),(127,85),(133,97),(128,94),(124,100)], stone3)
result.poly([(201,95),(207,88),(214,99),(208,96),(204,101)], stone2)

# Dragon silhouette: broad wings behind body
result.poly([(125,47),(99,35),(75,21),(48,18),(61,31),(77,43),(48,37),(23,43),(43,54),(70,60),(43,67),(28,80),(57,75),(89,64),(110,62)], ink)
result.poly([(141,50),(161,34),(183,22),(216,16),(201,32),(183,43),(213,35),(238,39),(216,51),(188,58),(216,63),(232,76),(204,73),(169,64),(148,64)], ink)
# Wing membranes
result.poly([(106,52),(96,40),(77,28),(57,23),(69,35),(85,49),(57,42),(35,45),(53,53),(79,57),(52,66),(40,73),(65,68),(91,59)], dragon1)
result.poly([(151,53),(163,40),(184,28),(207,22),(194,36),(177,49),(207,40),(226,42),(207,51),(180,56),(207,65),(220,71),(194,67),(166,59)], dragon1)
# Membrane ribs
for a,b,c,d in [(98,48,57,23),(94,53,35,45),(91,58,40,73),(159,50,207,22),(163,54,226,42),(166,59,220,71)]:
    result.line(a,b,c,d,dragon2)
# Dragon body, neck and head
result.path("M100 55 C107 45 119 42 130 49 C143 43 154 48 159 60 C165 73 157 89 145 98 L138 89 C146 78 143 66 135 63 C130 75 127 91 133 108 L119 108 C113 90 113 73 100 67 Z", ink)
result.path("M104 57 C113 49 122 49 130 55 C142 48 151 55 152 63 C154 75 146 85 140 91 L134 84 C141 73 139 61 130 60 C124 73 122 89 127 103 L120 103 C116 85 115 68 104 64 Z", dragon2)
# Head snout, horns, eye
result.poly([(98,54),(87,50),(78,53),(88,58),(101,61)], ink)
result.poly([(97,56),(87,53),(82,55),(90,57),(101,60)], dragon3)
result.poly([(89,52),(84,44),(94,51)], ink); result.poly([(98,53),(96,44),(103,53)], ink)
result.set(91,54,eye); result.set(92,54,eye)
# Tail curling right
result.path("M129 101 C147 103 165 97 169 86 C173 76 167 70 161 68 C176 68 185 76 180 88 C175 101 156 111 132 111 Z", ink)
result.path("M132 104 C150 105 165 97 168 89 C171 82 168 77 164 74 C175 77 177 83 174 90 C169 101 153 107 132 108 Z", dragon2)
# Legs and claws
result.poly([(116,91),(107,104),(102,113),(108,112),(113,105),(119,102)], ink)
result.poly([(135,91),(145,102),(151,110),(145,109),(140,105),(132,101)], ink)
for x,y in [(102,113),(108,112),(145,109),(151,110)]: result.line(x,y,x-2,y+3,metal1)

# Arrows across sky
for x,y,dx,dy in [(13,62,13,4),(28,89,14,-3),(52,99,14,-5),(184,92,-15,-5),(217,84,-14,2),(231,108,-14,-5),(9,116,14,-4),(205,58,-13,4)]:
    result.line(x,y,x+dx,y+dy,ink); result.line(x,y,x+3,y-3,metal1)

# Smoke columns behind castle
for pts,col in [([(73,137),(67,119),(73,106),(69,94),(81,85),(88,94),(86,107),(94,116),(90,137)],smoke1),
                ([(145,139),(139,122),(147,110),(142,99),(151,90),(160,97),(157,109),(166,118),(161,139)],smoke0),
                ([(196,142),(187,126),(191,113),(187,102),(197,94),(207,100),(204,111),(212,123),(207,142)],smoke2)]:
    result.poly(pts, ink); inner=[(x, y+2) for x,y in pts[1:-1]]; result.poly([(pts[0][0]+3,pts[0][1])]+inner+[(pts[-1][0]-3,pts[-1][1])],col)
# Pixel smoke caps
result.circle(79,91,8,smoke1); result.circle(72,98,6,smoke1); result.circle(153,95,8,smoke0)
result.circle(199,98,8,smoke2); result.rect(68,91,8,5,smoke1); result.rect(146,89,9,5,smoke0)

# Castle mass and walls
result.rect(55,128,151,70,ink)
result.rect(60,133,141,61,stone0)
# Keep blocks
result.rect(91,108,48,88,ink); result.rect(96,114,38,80,stone1)
# Battlements
for x in range(90,140,12): result.rect(x,104,8,13,ink); result.rect(x+2,106,5,9,stone1)
for x in range(53,208,16): result.rect(x,122,10,14,ink); result.rect(x+2,125,6,9,stone1)
# Towers
result.rect(43,119,27,83,ink); result.rect(48,125,17,72,stone1)
result.rect(192,116,28,86,ink); result.rect(197,122,18,75,stone1)
for x in [42,52,62,191,201,211]: result.rect(x,112,9,14,ink); result.rect(x+2,115,5,9,stone2)
# Masonry blocks
for x,y,w in [(62,143,20),(69,158,17),(59,177,23),(145,140,18),(166,151,25),(143,174,22),(101,126,13),(119,137,12),(101,155,28),(198,142,13),(199,170,15)]:
    result.rect(x,y,w,3,stone2)
# Gate
result.path("M103 195 L103 174 C103 157 128 157 128 174 L128 195 Z", ink)
result.path("M109 195 L109 176 C109 165 122 165 122 176 L122 195 Z", wood0)
for x in [112,117]: result.rect(x,168,2,27,wood2)
# Windows
for x,y in [(54,139),(54,164),(202,136),(202,161),(105,125),(122,125),(105,146),(122,146)]:
    result.rect(x,y,6,10,ink); result.rect(x+2,y+3,2,5,flame2)

# Fires on castle
for x,y in [(76,142),(151,147),(181,133),(87,181),(171,181)]:
    result.poly([(x-6,y+13),(x-4,y+3),(x,y+7),(x+2,y-4),(x+7,y+6),(x+5,y+13)],flame0)
    result.poly([(x-3,y+12),(x-2,y+4),(x+1,y+7),(x+2,y),(x+4,y+7),(x+3,y+12)],flame2)
    result.set(x+1,y+7,flame3)
# Glowing breach
result.rect(137,184,44,11,flame0); result.dither(141,185,35,8,[flame1,flame2],"checker")

# Rampart knights with spears and shields
for x in [67,82,146,163,181]:
    result.circle(x,119,3,metal1); result.rect(x-2,122,5,10,deep)
    result.line(x+2,126,x+8,120,metal1)
    result.circle(x-3,127,4,red); result.line(x+5,127,x+8,108,ink); result.set(x+8,107,metal1)
# Banners
result.line(112,124,112,90,ink); result.poly([(113,92),(132,97),(113,104)],red2); result.rect(116,96,8,2,gold)
result.line(211,124,211,94,ink); result.poly([(212,96),(228,100),(212,108)],red)

# Ground
result.poly([(0,185),(39,179),(73,189),(114,191),(154,187),(194,190),(223,178),(256,184),(256,256),(0,256)],earth0)
result.dither(0,203,256,53,[earth0,earth1],"bayer4")
result.rect(0,241,256,15,deep)

# Siege towers in foreground
# left tower
result.poly([(7,169),(38,169),(44,230),(2,230)],ink); result.poly([(11,174),(34,174),(38,225),(7,225)],wood0)
for y in [179,194,210]: result.rect(8,y,29,4,wood2)
result.line(9,174,37,225,wood1); result.line(35,174,7,225,wood1)
result.circle(9,229,7,ink); result.circle(36,229,7,ink); result.circle(9,229,3,wood2); result.circle(36,229,3,wood2)
result.rect(5,161,35,10,ink); result.rect(9,164,27,6,wood1)
# right tower
result.poly([(222,165),(249,165),(254,224),(216,224)],ink); result.poly([(226,170),(245,170),(249,219),(221,219)],wood0)
for y in [176,191,206]: result.rect(222,y,27,4,wood2)
result.line(225,170,249,219,wood1); result.line(245,170,221,219,wood1)
result.circle(222,224,7,ink); result.circle(248,224,7,ink)
result.rect(219,157,32,10,ink); result.rect(223,160,24,6,wood1)

# Soldiers in formation, rows of helmets, spears and shields
def soldier(x,y,accent):
    result.line(x+2,y+5,x+5,y-18,ink); result.set(x+5,y-19,metal1)
    result.circle(x,y,3,ink); result.rect(x-2,y+3,5,10,ink)
    result.circle(x-3,y+8,5,accent); result.circle(x-3,y+8,3,stone1)
    result.set(x,y-1,metal1)

for y, xs in [(207,range(54,211,13)),(224,range(44,218,14)),(242,range(25,236,15))]:
    for i,x in enumerate(xs): soldier(x,y, red if i%2==0 else stone0)
# Foreground larger knights
for x in [18,74,126,178,232]:
    result.line(x+5,250,x+11,211,ink); result.poly([(x+11,209),(x+9,215),(x+13,214)],metal1)
    result.circle(x,230,6,ink); result.rect(x-5,235,10,20,ink)
    result.circle(x-7,244,9,red); result.circle(x-7,244,6,stone1)
    result.line(x-11,244,x-3,244,metal1); result.line(x-7,240,x-7,248,metal1)
    result.rect(x-3,228,6,3,metal1)
# Spear forest in silhouette
for x in range(3,256,17):
    h = 18 + (x*7)%23
    result.line(x,256,x+4,256-h,ink); result.set(x+4,255-h,metal1)

# Embers and sparks
for x,y in [(72,116),(83,104),(91,129),(155,118),(168,104),(183,119),(199,132),(62,154),(92,169),(145,161),(188,151),(215,145),(132,116),(42,139)]:
    result.set(x,y,flame3); result.set(x+1,y-2,flame1)

# A few foreground highlights
result.rect(93,251,48,3,stone0); result.rect(150,247,28,2,stone1)

view(result, size=768, margin=0)
finish(result)
