# Ancient dragon battle, 256x256 pixel art
c = new_canvas(256, 256, background="#160f19", name="ancient-dragon-battle")

# Compact fantasy palette
INK="#17131b"; DEEP="#251827"; PLUM="#43223a"; PURPLE="#653047"
RED="#8f3c3d"; EMBER="#c85835"; ORANGE="#ed7b35"; GOLD="#f5b94b"; PALE="#ffd777"
SKY="#b84945"; MAUVE="#773b58"; ASH="#574351"; SMOKE="#73545a"
MOUNTAIN="#30263a"; DISTANT="#49334b"; STONE="#4b4650"; STONE2="#666069"; LIGHTSTONE="#8a7770"
STEEL="#9aa0a1"; HI="#d4c8ad"; BROWN="#553328"; WOOD="#7a4931"; WOODHI="#a5673b"
DRAGON="#211820"; DRAGMID="#3a2529"; DRAGHI="#713b32"; FIRE="#fff0a0"

# Sunset sky bands
c.rect(0,0,256,24,"#3b2039")
c.rect(0,24,256,25,"#563047")
c.rect(0,49,256,24,MAUVE)
c.rect(0,73,256,25,SKY)
c.rect(0,98,256,27,"#d45b3f")
c.rect(0,125,256,31,ORANGE)
c.rect(0,156,256,22,GOLD)
# sun and hazy glow
c.circle(204,105,24,"#f39b45")
c.circle(204,105,16,PALE)
# sky dithering and thin cloud streaks
c.dither(0,19,256,18,["#3b2039","#563047"],"checker")
c.dither(0,66,256,14,[MAUVE,SKY],"bayer4")
c.dither(0,116,256,13,["#d45b3f",ORANGE],"checker")
for x,y,w,col in [(8,39,50,"#6b3650"),(26,52,77,"#7f3e55"),(151,35,64,"#5c3148"),(178,57,67,"#8b4050"),(3,91,45,"#aa4347")]:
    c.rect(x,y,w,3,col); c.rect(x+9,y-2,max(8,w-24),2,col)

# Distant mountains
c.poly([(0,139),(22,118),(34,132),(55,106),(76,133),(98,116),(119,143),(143,117),(163,137),(186,111),(211,140),(233,121),(256,143),(256,180),(0,180)],DISTANT)
c.poly([(0,151),(31,129),(49,145),(70,121),(97,154),(124,127),(153,151),(178,128),(209,154),(234,132),(256,148),(256,184),(0,184)],MOUNTAIN)
# mountain highlights
c.poly([(31,129),(37,140),(45,137),(49,145)],ASH)
c.poly([(70,121),(78,138),(87,143),(80,145)],ASH)
c.poly([(124,127),(131,143),(139,141),(153,151)],ASH)
c.poly([(178,128),(184,142),(192,143),(209,154)],ASH)

# Smoke columns behind castle, chunky clusters
for cx,cy,r,col in [(88,119,12,SMOKE),(82,104,10,ASH),(91,89,13,SMOKE),(84,74,9,PURPLE),(164,119,14,SMOKE),(171,101,12,ASH),(163,84,10,SMOKE),(176,69,8,PURPLE),(128,126,9,ASH)]:
    c.circle(cx,cy,r,col)
    c.rect(cx-r,cy,r*2+1,4,col)
# soot cores
c.circle(90,96,6,"#493541"); c.circle(166,94,6,"#493541")

# Castle mass and towers with dark outline
c.rect(59,135,139,64,INK)
c.rect(63,139,131,60,STONE)
# central keep
c.rect(98,112,61,88,INK); c.rect(102,116,53,84,"#57515a")
# side towers
c.rect(47,126,37,75,INK); c.rect(51,130,29,71,"#514a53")
c.rect(176,123,36,78,INK); c.rect(180,127,28,74,"#514a53")
# battlements
for x in range(47,84,12): c.rect(x,119,9,12,INK); c.rect(x+4,123,5,8,"#5d555d")
for x in range(98,159,13): c.rect(x,104,9,13,INK); c.rect(x+4,108,5,9,"#655b61")
for x in range(176,212,12): c.rect(x,116,9,12,INK); c.rect(x+4,120,5,8,"#5d555d")
# stonework
for y in [145,158,172,187]:
    off=0 if y%2 else 8
    for x in range(64+off,194,18): c.rect(x,y,11,2,"#70666a")
for x,y in [(55,145),(70,136),(185,139),(199,154),(108,126),(139,135),(119,179),(151,164),(76,181)]: c.rect(x,y,8,3,"#827273")
# gate arch
c.rect(118,166,23,34,INK); c.circle(129,166,11,INK); c.rect(122,167,15,33,BROWN)
for x in [125,130,135]: c.rect(x,169,2,31,"#2c2020")
# fiery windows
for x,y in [(69,148),(187,143),(110,132),(143,146),(91,165),(162,168)]:
    c.rect(x-2,y-2,9,15,INK); c.rect(x,y,5,10,EMBER); c.rect(x+1,y+2,3,6,GOLD); c.set(x+2,y+3,FIRE)
# flames on parapets
for x,h in [(72,15),(91,10),(126,18),(151,13),(187,17)]:
    c.poly([(x-5,137),(x-3,129),(x,133),(x+2,137-h),(x+5,129),(x+6,137)],EMBER)
    c.poly([(x-2,137),(x,130),(x+2,134),(x+3,127),(x+4,137)],GOLD)

# Rampart knights: helmet, body, spear, shield
def knight(x,y,face=1):
    c.line(x+2,y-18,x+2+face*3,y+7,INK)
    c.line(x+3,y-19,x+3+face*3,y+6,WOODHI)
    c.circle(x,y-7,4,INK); c.rect(x-4,y-6,8,3,STEEL); c.set(x+face*4,y-6,HI)
    c.rect(x-3,y-2,6,11,INK); c.rect(x-1,y-1,4,8,"#777b7d")
    c.poly([(x+face*2,y),(x+face*8,y+2),(x+face*7,y+10),(x+face*2,y+12)],INK)
    c.poly([(x+face*3,y+2),(x+face*6,y+3),(x+face*5,y+8),(x+face*3,y+10)],RED)
for args in [(55,126,1),(77,126,-1),(105,112,1),(122,112,-1),(145,112,1),(184,123,-1),(204,123,1)]: knight(*args)

# Dragon wings, huge dark silhouette
# far wing left and right
c.poly([(129,68),(106,49),(83,42),(59,45),(35,35),(52,55),(76,64),(101,70),(118,82)],INK)
c.poly([(141,70),(161,45),(184,32),(209,30),(231,18),(218,42),(199,57),(176,68),(154,83)],INK)
# wing membranes
c.poly([(116,70),(103,54),(84,48),(62,49),(82,59),(102,65)],DRAGMID)
c.poly([(153,70),(165,52),(184,39),(212,34),(193,52),(174,62)],DRAGMID)
# membrane struts
for a,b,d,e in [(128,68,84,48),(126,72,62,49),(143,70,184,39),(147,74,212,34)]: c.line(a,b,d,e,DRAGHI)
# body and neck
c.poly([(113,70),(123,60),(139,58),(151,65),(158,78),(157,93),(146,105),(130,108),(115,100),(106,87)],INK)
c.poly([(122,69),(136,64),(146,69),(151,82),(146,94),(132,101),(119,95),(113,84)],DRAGMID)
# long neck and head facing left
c.poly([(122,74),(108,66),(95,62),(80,65),(68,61),(57,66),(70,72),(90,73),(105,83),(118,88)],INK)
c.poly([(72,64),(60,57),(62,67),(52,70),(66,74),(79,70)],INK)
# horns and eye
c.poly([(62,59),(53,51),(57,63)],PALE); c.poly([(70,62),(68,52),(75,63)],HI)
c.set(61,66,GOLD); c.set(60,66,FIRE)
# jaw and fire breath
c.poly([(59,70),(43,72),(54,76),(68,74)],DRAGMID)
c.poly([(51,72),(37,68),(23,72),(39,76),(16,83),(39,81),(55,75)],EMBER)
c.poly([(46,72),(33,72),(21,77),(42,76)],GOLD); c.set(26,76,FIRE)
# tail curls right
c.path("M148 96 C169 99 180 91 180 82 C180 74 174 72 169 77 C175 78 174 85 168 87 C161 90 153 87 147 84 Z",INK)
# legs and claws
c.poly([(123,98),(115,114),(107,121),(115,121),(125,109),(132,101)],INK)
c.poly([(145,99),(153,112),(164,116),(157,119),(147,111),(138,103)],INK)
for x,y in [(108,121),(114,121),(158,119),(164,116)]: c.line(x,y,x-3,y+3,HI)
# scales and belly
for x,y in [(126,73),(137,70),(143,78),(124,84),(136,89),(129,97)]: c.rect(x,y,4,2,DRAGHI)
c.line(116,87,143,96,"#855042")

# Arrows in the sky
for x,y,dx,dy in [(18,104,15,-5),(36,91,14,2),(206,82,-16,5),(226,65,-13,7),(14,129,14,-8),(221,103,-15,-4),(94,35,11,8)]:
    c.line(x,y,x+dx,y+dy,INK); c.line(x,y,x+3,y-3 if dy>0 else y+3,INK)

# Foreground ground
c.poly([(0,192),(37,187),(70,195),(104,188),(139,196),(173,186),(214,193),(256,184),(256,256),(0,256)],INK)
c.poly([(0,205),(42,199),(80,207),(121,201),(158,209),(201,198),(256,202),(256,256),(0,256)],DEEP)

# Siege towers at sides
def tower(x,y,flip=1):
    c.rect(x,y,30,54,INK)
    c.rect(x+4,y+5,22,49,WOOD)
    c.line(x+4,y+8,x+26,y+49,INK); c.line(x+26,y+8,x+4,y+49,INK)
    for yy in [y+10,y+27,y+44]: c.rect(x+2,yy,26,4,WOODHI)
    c.circle(x+6,y+54,7,INK); c.circle(x+24,y+54,7,INK); c.circle(x+6,y+54,3,STONE2); c.circle(x+24,y+54,3,STONE2)
    c.poly([(x,y),(x+4,y-13),(x+26,y-13),(x+30,y)],INK)
    c.poly([(x+4,y-2),(x+7,y-9),(x+23,y-9),(x+26,y-2)],RED)
tower(8,185); tower(218,181)

# Soldier formations in foreground
def soldier(x,y,accent=RED):
    c.circle(x,y-9,3,INK); c.rect(x-2,y-8,5,3,STEEL)
    c.rect(x-3,y-4,6,12,INK); c.rect(x-1,y-3,3,8,ASH)
    c.poly([(x+1,y-3),(x+7,y-1),(x+6,y+7),(x+1,y+9)],INK)
    c.poly([(x+2,y-1),(x+5,y),(x+4,y+5),(x+2,y+7)],accent)
    c.line(x-2,y-5,x-5,y-20,WOODHI); c.set(x-5,y-21,HI)
for row,(yy,start,count) in enumerate([(218,48,11),(236,39,13),(252,31,15)]):
    for i in range(count): soldier(start+i*13+(row%2)*4,yy,RED if i%3 else GOLD)

# Foreground embers and sparks
for x,y in [(15,161),(28,143),(42,173),(92,151),(116,155),(133,143),(158,151),(201,158),(231,139),(244,169),(73,112),(169,132)]:
    c.set(x,y,GOLD); c.set(x,y-1,EMBER)
for x,y in [(22,120),(48,99),(101,92),(193,91),(216,118),(235,95),(12,177),(151,125)]: c.rect(x,y,2,3,ORANGE)

# Pixel clusters and stronger silhouette accents
c.line(0,201,255,192,INK)
c.rect(0,246,256,10,"#100d13")
# banner on central keep
c.line(128,103,128,82,INK); c.poly([(129,84),(146,88),(129,94)],RED); c.rect(130,86,8,2,GOLD)

view(c)
finish(c)
