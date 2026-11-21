from pixelbench_api import *
import random

random.seed(13)
out = input_canvas.copy(name='output')

# Palette
sky0='#09070f'; sky1='#160b18'; sky2='#28101d'; sky3='#461522'; sky4='#6b1d27'
cloud0='#120b17'; cloud1='#25101e'; cloud2='#3b1522'; cloud3='#571b25'
red0='#4d0912'; red1='#7d1019'; red2='#b51d22'; red3='#e44432'; red4='#ff7450'; red5='#ffb060'
ink='#07070b'; black='#0c0b10'; stone0='#15131a'; stone1='#211923'; stone2='#30202a'; stone3='#45262e'; edge='#62303a'
ash='#725057'; bone='#b58a7d'; lava='#ff3b1f'; glow='#ff8a32'

# Repaint full atmosphere in horizontal night bands.
out.rect(0,0,256,128,sky0)
out.rect(0,18,256,26,sky1)
out.rect(0,44,256,24,sky2)
out.rect(0,68,256,25,'#31121c')
# Blood haze near horizon.
out.dither(0,54,256,28,[sky2,sky3],'bayer4')
out.dither(0,75,256,18,[sky3,'#35131d'],'checker')

# Jagged clouds, arranged as curved streaks around the moon.
clouds = [
 [(0,9),(22,7),(31,12),(57,10),(69,15),(54,19),(18,17),(0,20)],
 [(0,28),(35,25),(52,29),(78,25),(91,30),(76,34),(42,32),(19,36),(0,34)],
 [(153,9),(183,6),(198,11),(224,8),(256,12),(256,21),(226,18),(205,21),(178,17),(157,20)],
 [(164,29),(194,25),(213,30),(244,26),(256,29),(256,38),(229,35),(207,39),(184,34),(160,37)],
 [(0,48),(26,45),(55,50),(83,47),(99,52),(72,57),(37,53),(17,58),(0,56)],
 [(149,50),(176,45),(202,49),(226,44),(256,47),(256,58),(230,55),(202,59),(177,54),(151,58)]
]
for i,p in enumerate(clouds): out.poly(p, cloud1 if i%2==0 else cloud2)
# Lit undersides of clouds.
out.line(0,57,35,55,cloud3); out.line(35,55,62,58,cloud3); out.line(195,58,225,55,cloud3); out.line(225,55,255,58,cloud3)
out.line(5,36,31,33,'#32131f'); out.line(218,38,250,35,'#32131f')

# Hanging chains behind the moon.
for x,lean in [(102,-1),(154,1)]:
    pts=[]
    for y in range(0,37,4):
        xx=x + (y//4%2)*lean
        out.rect(xx,y,2,2,'#57434a')
        out.set(xx+(-1 if lean<0 else 2),y+2,'#2c242c')
    out.line(x,0,x+lean*8,34,'#211b23')
# Cross chain between suspension lines.
out.line(103,19,117,28,'#3d3037'); out.line(153,19,139,28,'#3d3037')

# Blood moon: black rim, deep red disc, stepped pixel highlights.
out.circle(128,34,27,ink)
out.circle(128,34,24,red1)
out.circle(128,34,21,red2)
out.dither(109,17,38,34,[red2,red3],'bayer4')
out.circle(128,34,17,red3)
out.rect(114,22,5,3,red4); out.rect(119,18,11,2,red4); out.rect(110,29,3,9,red4)
out.rect(139,25,4,8,red1); out.rect(134,38,8,5,'#8f1119'); out.rect(118,44,7,3,'#8f1119')
# Moon craters.
for x,y,w,h in [(121,25,5,4),(136,30,5,3),(126,39,4,5),(114,34,3,3),(132,19,3,3)]: out.rect(x,y,w,h,'#9d161d')
# Hooks biting into the moon.
out.line(103,31,109,35,ash); out.line(109,35,111,32,ash); out.line(153,31,147,35,ash); out.line(147,35,145,32,ash)

# Distant black mountain ranges.
out.poly([(0,82),(13,71),(20,76),(31,65),(43,74),(55,62),(71,77),(83,69),(98,86),(112,76),(128,88),(145,73),(157,81),(169,67),(184,78),(197,62),(211,76),(225,65),(239,75),(256,58),(256,110),(0,110)], '#100c13')
out.poly([(0,92),(18,79),(27,87),(42,76),(54,91),(72,74),(86,92),(105,78),(119,94),(137,80),(153,91),(171,76),(188,90),(207,77),(222,90),(241,72),(256,82),(256,113),(0,113)], stone1)
# Red haze along ridges.
for pts in [[(0,90),(27,86),(54,92),(81,87)],[(174,89),(202,84),(229,87),(255,81)]]:
    for a,b in zip(pts,pts[1:]): out.line(a[0],a[1],b[0],b[1],edge)

# Castle foundation cliff.
out.poly([(66,112),(75,101),(85,98),(91,88),(99,89),(103,80),(111,82),(117,74),(125,79),(131,72),(139,79),(146,77),(151,86),(163,87),(169,96),(181,100),(191,113)], ink)
out.poly([(77,110),(89,96),(101,98),(110,84),(123,91),(133,80),(144,91),(158,93),(176,111)], stone1)
out.poly([(83,107),(97,100),(109,103),(119,93),(133,98),(145,91),(159,101),(174,108)], stone2)

# Main citadel mass with stepped battlements.
out.rect(92,63,72,42,stone0)
out.rect(96,57,12,48,stone1); out.rect(148,56,12,49,stone1)
# Battlements.
for x in range(92,165,9):
    out.rect(x,59 if x in (92,101,155) else 62,5,7,stone0)
# Central keep and ascending tiers.
out.rect(111,51,35,50,stone1)
out.rect(116,44,25,57,stone0)
out.rect(121,35,15,66,stone1)
# Central roof / horns.
out.poly([(116,46),(121,35),(128,41),(136,35),(141,46)],ink)
out.poly([(121,36),(118,25),(124,32),(128,40)],stone0)
out.poly([(135,36),(138,25),(132,32),(128,40)],stone0)
out.line(118,25,115,20,edge); out.line(138,25,141,20,edge)
# Side towers with conical, hooked roofs.
out.rect(80,70,14,34,stone1); out.rect(164,69,14,36,stone1)
out.poly([(77,71),(87,54),(97,71)],ink); out.poly([(161,70),(171,52),(181,70)],ink)
out.line(87,54,82,49,edge); out.line(171,52,176,47,edge)
# Outer turrets.
out.rect(67,83,11,24,stone0); out.rect(181,82,11,25,stone0)
out.poly([(64,83),(72,68),(81,83)],ink); out.poly([(178,82),(187,67),(195,82)],ink)

# Masonry highlights and cracks.
for x,y,w in [(95,70,12),(112,59,10),(132,55,10),(100,84,9),(139,76,14),(84,88,8),(151,91,10),(117,87,8),(168,76,7)]:
    out.rect(x,y,w,2,stone3)
    out.set(x+w-2,y+2,edge)
for x0,y0,x1,y1 in [(105,65,101,76),(151,65,155,79),(126,50,130,58),(119,75,114,83),(143,83,138,91),(88,77,85,87),(171,74,174,86)]:
    out.line(x0,y0,x1,y1,'#5a2c36')

# Windows, all infernal warm light with dark cap.
windows=[(85,78),(70,89),(187,88),(101,68),(154,67),(105,86),(151,84),(124,57),(132,57),(124,72),(133,72),(124,87),(133,87)]
for x,y in windows:
    out.rect(x,y,3,7,ink); out.set(x+1,y+2,red4); out.set(x+1,y+3,glow); out.set(x+1,y+4,red3)
# Throne gate, face-like focal point.
out.poly([(119,104),(119,94),(122,89),(128,86),(134,89),(137,94),(137,104)],ink)
out.rect(123,94,3,3,red4); out.rect(131,94,3,3,red4)
out.poly([(124,100),(128,97),(133,100),(131,104),(126,104)],red1)

# Spikes and hanging banners.
for x in [63,77,96,108,146,162,180,194]: out.poly([(x,104),(x+2,91),(x+4,104)],ink)
out.rect(102,72,4,15,red1); out.poly([(102,87),(106,84),(106,91),(102,89)],red2)
out.rect(150,72,4,14,red1); out.poly([(150,86),(154,83),(154,90),(150,88)],red2)

# Foreground dead valley and angular black silhouettes.
out.poly([(0,103),(15,99),(28,106),(42,101),(56,109),(74,105),(91,112),(110,109),(128,116),(148,108),(166,113),(184,106),(204,111),(221,101),(238,106),(256,96),(256,128),(0,128)], '#0a090d')
out.poly([(0,116),(25,109),(48,118),(70,111),(91,121),(116,113),(139,120),(160,114),(183,121),(205,110),(228,117),(256,107),(256,128),(0,128)], stone0)
# Lava river from gate to foreground.
out.poly([(127,103),(133,103),(138,109),(146,112),(143,116),(157,120),(164,128),(132,128),(137,121),(126,117),(130,112),(124,108)],red1)
out.poly([(129,104),(132,105),(134,110),(141,113),(138,116),(149,121),(153,128),(141,128),(143,123),(132,119),(135,115),(128,111)],lava)
out.set(132,109,red5); out.line(138,115,144,117,glow); out.line(145,123,150,127,red5)
# Lava cracks in the ground.
for segs in [[(0,121),(13,118),(22,121),(35,119)],[(52,126),(63,121),(74,123),(85,118)],[(181,126),(192,119),(203,120),(215,115)],[(224,126),(236,120),(255,118)]]:
    for a,b in zip(segs,segs[1:]): out.line(a[0],a[1],b[0],b[1],red2)
# Dead trees and stakes.
for x,y,h,side in [(18,112,18,-1),(43,117,15,1),(225,112,22,-1),(244,111,26,1)]:
    out.line(x,y,x,y-h,ink); out.line(x,y-h+5,x+side*7,y-h-2,ink); out.line(x,y-h+9,x-side*6,y-h+3,ink)
# Ash flecks and red sparks.
for _ in range(90):
    x=random.randrange(5,251); y=random.randrange(8,101)
    if (x-128)**2+(y-34)**2 > 30**2:
        out.set(x,y, random.choice(['#5b3038','#71333a','#39232b']))
for _ in range(24):
    x=random.randrange(92,166); y=random.randrange(38,105)
    out.set(x,y, random.choice([red2,red3,glow]))

# A final crisp silhouette pass on roof points.
out.set(128,31,ink); out.line(128,31,128,39,ink)

print(out.stats_text())
save('demon_kings_castle',out,indexed=True)
view(out,scale=3,margin=0)
finish(out)
