import random, math
random.seed(17)
result=new_canvas(256,256,background='#241e35',name='ancient_dragon_battle')
c=result
# Closed, deliberately compact palette
ink='#171b25'; deep='#252632'; violet='#3c3044'; plum='#54384a'; rust='#82454d'; rose='#ad5351'; orange='#d97550'; amber='#efa35e'; gold='#ffd180'; cream='#ffe7a0'
rock0='#30323b'; rock1='#45414a'; rock2='#615153'; rock3='#84645c'; rock4='#ae8270'
scale0='#202d31'; scale1='#354441'; scale2='#52604f'; scale3='#798064'; scale4='#a3a37a'
# Sunset, discrete horizontal colour bands
for y0,y1,col in [(0,26,'#343047'),(26,51,'#56374c'),(51,76,'#85434e'),(76,102,'#b25852'),(102,129,'#db7958'),(129,157,'#efa363'),(157,184,'#bf785c'),(184,256,'#493b40')]: c.rect(0,y0,256,y1-y0,col)
c.circle(192,83,37,amber); c.circle(192,83,30,'#ffc677')
# Long broken, block-edged cloud ribbons
for pts,col in [([(0,12),(43,12),(43,16),(76,16),(76,20),(105,20),(105,24),(66,24),(66,22),(21,22),(21,19),(0,19)],plum), ([(143,18),(191,18),(191,14),(226,14),(226,18),(255,18),(255,29),(210,29),(210,26),(169,26),(169,23),(143,23)],plum), ([(0,49),(28,49),(28,46),(53,46),(53,51),(88,51),(88,56),(47,56),(47,59),(0,59)],rust), ([(167,56),(216,56),(216,53),(255,53),(255,60),(234,60),(234,63),(187,63),(187,60),(167,60)],rose), ([(0,88),(29,88),(29,85),(58,85),(58,89),(83,89),(83,93),(38,93),(38,96),(0,96)],rose)]: c.poly(pts,col)
# Thin illuminated cloud undersides
for x,y,w in [(0,98,40),(212,104,44),(157,121,59),(13,113,46),(221,37,35)]:c.rect(x,y,w,2,orange)
# Distant mountain silhouettes
c.poly([(0,147),(18,132),(26,137),(48,111),(68,137),(84,123),(106,151),(136,135),(152,142),(170,126),(184,140),(208,116),(221,131),(238,119),(255,138),(255,190),(0,190)],'#886066')
c.poly([(25,138),(48,111),(61,130),(49,124),(43,129),(40,126)],'#b78071')
c.poly([(188,138),(208,116),(221,131),(210,126),(205,129),(201,127)],'#b78071')
c.poly([(0,163),(23,149),(37,156),(63,141),(94,169),(118,153),(148,166),(172,149),(189,155),(219,143),(255,161),(255,195),(0,195)],'#624c58')
# Smoke piles ascending behind the burning walls
for x,y,r in [(74,133,13),(69,119,14),(59,104,13),(53,90,13),(37,81,15),(25,73,13),(175,129,15),(181,111,17),(194,99,13),(212,91,15),(226,80,16),(241,73,19),(253,59,16),(128,142,12),(121,127,11)]:
 c.circle(x,y,r,plum)
 c.circle(x-3,y-3,max(3,r-4),'#68434c')
 c.rect(x-r+3,y+r-3,r+3,3,plum)
# Pale smoky backlit wisps
for x,y,w in [(8,64,17),(17,83,12),(207,80,17),(233,59,20),(185,108,10)]:c.rect(x,y,w,2,rust)
# Fire utility with forked tongues
def flame(x,y,w,h):
 c.poly([(x-w,y),(x-w+1,y-h//3),(x-w//2,y-h//2),(x-w//2,y-h),(x,y-h*2//3),(x+2,y-h-4),(x+w//2,y-h//2),(x+w,y-h//3),(x+w,y)],'#a7473c')
 c.poly([(x-w+2,y),(x-w//2,y-h//3),(x-1,y-h+4),(x+2,y-h//2),(x+w//2,y-h*2//3),(x+w-2,y)],'#ec7941')
 c.poly([(x-w//2,y),(x,y-h*2//3),(x+2,y-h//3),(x+w//2,y)],'#ffc360')
 c.poly([(x-2,y),(x,y-h//3),(x+3,y)],cream)
for x,y,w,h in [(65,153,10,32),(88,151,9,24),(114,166,11,34),(143,162,10,29),(166,149,12,27),(193,151,10,38)]:flame(x,y,w,h)
# Castle cliff base
c.poly([(48,185),(75,176),(177,177),(204,185),(218,228),(38,232)],ink)
c.poly([(55,191),(83,182),(178,185),(203,199),(212,223),(46,227)],rock0)
for pts in [[(54,205),(77,190),(71,211),(56,224)],[(84,189),(110,192),(95,220),(77,228)],[(155,192),(177,193),(191,225),(161,219)],[(183,192),(202,205),(207,222),(193,213)]]:c.poly(pts,rock1)
# Masonry with staggered block joints
def masonry(x,y,w,h,base=rock2):
 c.rect(x,y,w,h,ink); c.rect(x+2,y+1,w-4,h-1,base)
 c.rect(x+w-7,y+1,5,h-1,rock1)
 for yy in range(y+4,y+h,7):
  c.line(x+2,yy,x+w-3,yy,rock1)
  for xx in range(x+3+(4 if ((yy-y)//7)%2 else 0),x+w-3,10):
   c.line(xx,yy,xx, min(yy+6,y+h-1),rock1)
   if random.random()<.6:c.line(xx+1,yy+1,min(xx+6,x+w-8),yy+1,rock3)
 c.line(x+2,y+1,x+2,y+h-2,rock4)
def crenels(x,y,w):
 c.rect(x,y+5,w,6,ink);c.rect(x+1,y+6,w-2,3,rock3)
 for xx in range(x,x+w-3,8):
  c.rect(xx,y,5,8,ink);c.rect(xx+1,y+1,3,5,rock3);c.set(xx+1,y+1,rock4)
def window(x,y):
 c.rect(x,y,4,10,ink);c.rect(x+1,y+2,1,7,'#bd694d');c.set(x+1,y+3,amber)
# Rear keep
masonry(108,143,43,52);crenels(105,136,49)
masonry(119,126,21,32);crenels(117,120,25)
window(128,132)
c.line(129,120,129,104,ink);c.poly([(130,105),(145,108),(140,112),(130,111)],'#a94945');c.line(131,106,140,108,orange)
# Side towers
masonry(61,146,30,59);crenels(58,137,36)
masonry(169,140,30,67);crenels(166,131,36)
for xx,yy in [(69,155),(80,155),(69,179),(177,149),(188,149),(177,174),(188,174)]:window(xx,yy)
c.rect(60,174,32,4,ink);c.rect(61,174,30,2,rock3)
c.rect(168,168,32,4,ink);c.rect(169,168,30,2,rock3)
# Foreground curtain wall and arch
masonry(85,175,91,39);crenels(85,166,91)
c.poly([(117,214),(117,193),(120,186),(126,182),(132,182),(138,186),(141,193),(141,214)],ink)
c.poly([(121,214),(121,194),(123,190),(128,186),(133,187),(137,193),(137,214)],'#3b3035')
for xx in range(123,138,3):c.line(xx,191 if xx>124 and xx<135 else 194,xx,213,ink)
for yy in [197,205]:c.line(121,yy,137,yy,ink)
for xx,yy in [(115,193),(118,186),(123,181),(132,181),(139,186),(142,194)]:c.rect(xx,yy,3,5,rock4)
# Wall buttresses
for x in [90,106,148,166]:
 c.poly([(x,180),(x+5,180),(x+5,205),(x+8,215),(x-2,215)],ink)
 c.poly([(x+1,182),(x+3,182),(x+3,205),(x+5,213),(x,213)],rock3)
# Ancient dragon: tail, wings, body, head. Dark contour is part of every form.
def shape(points,col,outline=ink):
 c.poly(points,col);c.poly(points,outline,fill=False)
# Long whiplash tail
shape([(117,93),(106,107),(91,115),(72,116),(57,110),(46,110),(43,115),(49,120),(61,122),(78,127),(95,125),(113,116),(126,103)],scale1)
c.line(49,114,61,117,scale3);c.line(61,117,77,121,scale3);c.line(78,121,93,120,scale2)
# Far wing stretched against sun
shape([(124,79),(139,51),(161,32),(192,21),(188,36),(190,51),(200,67),(182,60),(173,62),(168,74),(153,68),(145,79),(136,91)],'#573b42')
shape([(135,74),(144,52),(163,35),(185,25),(172,43),(159,48),(147,65)],'#78504b')
for a,b in [((140,76),(161,35)),((161,35),(188,50)),((161,35),(170,70)),((161,35),(150,70))]:c.line(*a,*b,ink)
c.line(145,51,183,26,scale2)
# Vast near wing with fingers and scalloped trailing edge
shape([(122,91),(102,69),(83,52),(60,23),(52,19),(48,33),(37,49),(24,67),(39,65),(48,68),(54,77),(68,74),(78,79),(84,91),(95,88),(109,99)],'#703f45')
shape([(52,25),(47,44),(31,62),(46,60),(53,67),(57,52),(66,46)],'#a05a50')
shape([(59,31),(65,53),(58,71),(70,67),(79,72),(76,57)],'#8b4a49')
shape([(79,57),(82,75),(87,84),(96,81),(107,88)],'#8b4a49')
# Wing bone ridges
for pts in [[(121,91),(99,67),(78,47),(57,23),(52,19)],[(53,24),(48,44),(25,67)],[(56,28),(60,50),(54,76)],[(62,35),(75,56),(83,90)],[(80,53),(94,70),(108,95)]]:
 for a,b in zip(pts,pts[1:]):
  c.line(*a,*b,ink);c.line(a[0],a[1]-1,b[0],b[1]-1,scale2)
# Thorn on the wing elbow
shape([(49,24),(48,14),(54,20),(60,23)],scale4)
# Weathered membrane folds catch the sunset
for a,b in [((47,48),(37,59)),((63,52),(60,64)),((77,62),(80,73)),((88,67),(99,80)),((171,38),(182,47)),((161,46),(166,60)),((150,55),(145,67))]:
 c.line(*a,*b,'#b16b57')
# Main body and raised neck
shape([(104,85),(115,78),(129,78),(141,85),(148,88),(154,84),(157,73),(164,65),(175,65),(182,72),(178,81),(167,85),(163,98),(151,108),(133,111),(115,103)],scale1)
shape([(112,85),(124,82),(138,88),(146,94),(157,90),(161,77),(168,71),(176,71),(169,78),(164,93),(154,102),(136,106),(121,98)],scale2)
# Belly armour follows the neck
shape([(177,77),(172,83),(168,96),(160,105),(150,110),(132,111),(122,105),(142,105),(154,98),(161,86),(165,77)],'#8b8967')
for a,b in [((165,82),(171,86)),((162,88),(168,92)),((159,94),(165,98)),((155,99),(161,103)),((148,103),(152,109)),((139,105),(141,110)),((130,105),(131,109))]:c.line(*a,*b,scale0)
# Dorsal spines
for pts in [[(109,84),(109,76),(116,80)],[(119,80),(123,71),(128,79)],[(131,80),(138,74),(139,86)],[(147,88),(150,79),(154,83)],[(157,74),(157,64),(163,68)],[(165,66),(168,57),(172,66)]]:shape(pts,scale3)
# Hind legs and hooked talons
shape([(118,98),(116,107),(123,115),(130,116),(129,122),(135,122),(140,115),(134,107),(132,101)],scale1)
c.line(121,105,128,111,scale3)
shape([(145,101),(149,109),(159,111),(161,116),(169,115),(166,108),(156,105),(156,99)],scale1)
for x,y in [(130,120),(135,118),(161,114),(165,113)]:c.line(x,y,x+2,y+4,cream)
# Head pointed right, brows and jagged open jaws
shape([(165,68),(177,66),(184,71),(194,74),(197,80),(188,84),(179,82),(173,86),(166,80)],scale1)
shape([(172,69),(179,69),(184,73),(192,75),(190,78),(177,76),(171,78)],scale3)
shape([(179,80),(189,81),(197,80),(194,86),(183,88),(175,84)],ink)
shape([(176,85),(185,88),(193,86),(190,91),(179,91),(172,85)],scale2)
# Horns sweep back, two different sizes
shape([(173,69),(164,60),(164,54),(170,61),(179,67)],'#c0b18a')
shape([(180,70),(178,59),(184,66),(186,72)],scale4)
c.line(176,75,182,76,ink);c.rect(178,75,3,2,'#f8c76a');c.set(180,75,cream);c.set(181,76,ink)
c.set(191,77,ink)
for x,y in [(183,82),(189,83),(185,87)]:c.line(x,y,x,y+2,cream)
# Scales in tidy irregular clusters
for x,y in [(114,87),(119,90),(124,86),(127,92),(132,89),(137,93),(141,97),(122,97),(114,93),(153,93),(161,78),(164,73),(158,85)]:
 c.line(x,y,x+2,y,scale3);c.set(x+2,y+1,scale0)
# Dragon's descending fire breath
shape([(194,85),(200,92),(202,102),(211,112),(210,120),(220,133),(214,131),(219,145),(208,138),(204,143),(201,127),(197,118),(199,111),(194,98)],'#b54d3d',outline='#b54d3d')
c.poly([(195,87),(201,99),(200,107),(207,117),(206,126),(213,137),(204,131),(202,119),(198,113),(198,102)],'#f28b42')
c.poly([(195,87),(199,99),(199,109),(204,119),(205,129),(201,122),(197,111),(197,100)],'#ffd77b')
c.line(195,87,198,103,cream)
for x,y in [(207,100),(214,110),(219,125),(198,128),(218,139),(203,95)]:c.rect(x,y,1,3,amber)
# Ground rolling toward viewer
c.poly([(0,210),(31,205),(58,214),(88,222),(117,218),(140,216),(173,221),(203,210),(232,205),(255,210),(255,255),(0,255)],ink)
c.poly([(0,220),(31,212),(62,221),(95,229),(124,220),(139,220),(163,230),(203,216),(233,212),(255,220),(255,255),(0,255)],'#393339')
c.poly([(106,255),(117,231),(126,214),(136,214),(145,231),(166,255)],'#66504a')
c.poly([(118,255),(127,232),(130,217),(134,219),(138,236),(150,255)],'#80604f')
for i in range(165):
 x=random.randrange(256);y=random.randrange(216,256)
 if not (113<x<151):c.line(x,y,min(255,x+random.randrange(1,4)),y,random.choice([ink,'#4b3e40','#594648']))
# Siege tower timber silhouettes with red banners
def siege(x,y,w,h):
 # Wheels and heavy frame
 for xx in [x+5,x+w-5]:
  c.circle(xx,y+h,5,ink);c.circle(xx,y+h,2,'#775444');c.set(xx,y+h,ink)
 shape([(x+3,y+h-3),(x+8,y),(x+w-8,y),(x+w-2,y+h-3)],'#392f31')
 for yy in range(y+6,y+h-3,9):c.rect(x+6,yy,w-11,2,'#69483c')
 for xx in [x+4,x+w-7]:
  c.rect(xx,y,3,h,ink);c.line(xx+1,y+2,xx+1,y+h-2,'#9b6c4c')
 for yy in [y+13,y+31]:
  c.line(x+6,yy,x+w-7,yy+15,ink);c.line(x+7,yy,x+w-7,yy+14,'#9b6c4c')
 c.rect(x,y-2,w,9,ink);c.rect(x+1,y,w-2,4,'#755044')
 for xx in range(x,x+w,6):c.rect(xx,y-7,4,7,ink);c.rect(xx+1,y-6,2,4,'#8b6250')
 c.line(x+w//2,y-7,x+w//2,y-26,ink)
 c.poly([(x+w//2+1,y-25),(x+w//2+15,y-22),(x+w//2+11,y-18),(x+w//2+1,y-19)],'#993e3e')
 c.line(x+w//2+2,y-24,x+w//2+11,y-22,'#d77b51')
 c.line(x+w-1,y+5,x+w+14,y-2,ink);c.line(x+w-1,y+6,x+w+14,y-1,'#9b6c4c')
siege(12,167,28,58);siege(220,172,27,56)
# Soldiers: helmets, distinct shields and long spearpoints
def knight(x,y,side=False,small=False):
 # y is boot line
 h=10 if small else 13
 c.line(x+5,y+1,x+5,y-h-9,'#a58a6a')
 c.poly([(x+3,y-h-7),(x+5,y-h-12),(x+7,y-h-7)],'#b6b7a4')
 c.line(x+5,y-h-12,x+5,y-h-7,ink)
 c.line(x-2,y-3,x-3,y,ink);c.line(x+1,y-3,x+2,y,ink)
 c.rect(x-3,y-h+4,7,h-5,ink);c.rect(x-1,y-h+4,3,h-5,'#58636a')
 c.rect(x-2,y-h,5,5,ink);c.rect(x-1,y-h,3,3,'#a0a6a0');c.set(x-1,y-h,'#ded4b3');c.line(x,y-h+2,x+2,y-h+2,ink)
 c.line(x+3,y-h+5,x+5,y-h+6,'#929c95')
 shape([(x-5,y-h+5),(x,y-h+4),(x,y-3),(x-3,y),(x-6,y-3)],'#803e41' if side else '#3d535c')
 c.line(x-4,y-h+6,x-3,y-3,'#d4b075');c.line(x-5,y-h+7,x-1,y-h+7,'#d4b075')
# Rampart guards silhouetted against fire
for x,y in [(65,139),(80,139),(98,168),(112,168),(148,168),(166,168),(176,133),(191,133),(124,122)]:knight(x,y,small=True)
# Massed ranks fan toward the gate, with disciplined spear rhythms
for row in range(3):
 yy=224+row*12
 for x in range(52-row*8,105-row*2,11):knight(x,yy,side=False)
 for x in range(163+row*2,211+row*8,11):knight(x,yy,side=True)
# Foreground standard bearer
c.line(28,251,28,212,ink);c.line(29,251,29,213,'#b0956e')
shape([(30,214),(46,216),(44,229),(37,226),(30,227)],'#94443e')
c.line(32,215,32,224,orange);c.line(36,219,41,219,gold);c.line(38,217,38,223,gold)
knight(27,254,True)
# Arrows, flying along diagonal paths, clear barbed heads
for x,y,dx,dy in [(6,111,10,-6),(27,130,11,-8),(89,132,9,-8),(102,119,10,-7),(145,131,-10,-7),(223,152,-11,-8),(233,127,-12,-5),(9,149,10,-7),(228,45,-10,5),(208,33,-10,4)]:
 c.line(x,y,x+dx,y+dy,ink)
 ex=x+dx;ey=y+dy
 c.line(ex,ey,ex-(3 if dx>0 else -3),ey,ink)
 c.line(x,y,x,y-2,'#c7a17c')
# Ember flecks around the inferno; a few drifting into foreground
for i in range(85):
 x=random.randint(44,218);y=random.randint(107,222)
 if (y<164 and random.random()<.6) or (y>185 and random.random()<.24):
  c.set(x,y,random.choice([orange,amber,'#d55e3e']))
  if random.random()<.25:c.set(x,y-1,gold)
# Scattered foreground debris and grasses
for x,y in [(5,244),(13,253),(91,254),(184,252),(244,246),(248,237),(73,252)]:
 c.line(x-3,y,x+4,y,ink);c.line(x,y,x-2,y-5,ink);c.line(x,y,x+3,y-3,ink)
# Damage and warm reflected fire on the castle stone
for pts in [[(84,158),(81,162),(83,165),(79,170)],[(194,183),(190,186),(193,190)],[(99,191),(97,194),(100,197)],[(145,150),(141,154),(143,158)]]:
 for a,b in zip(pts,pts[1:]):c.line(*a,*b,ink)
for x,y,w in [(65,148,6),(82,150,4),(171,142,6),(191,143,5),(109,146,4),(145,162,4),(150,177,8),(89,177,6)]:c.line(x,y,x+w,y,'#c98b64')
# Abandoned shield and broken shaft beside the approach
shape([(105,239),(111,237),(115,240),(113,245),(108,247),(105,244)],'#803e41')
c.line(108,240,111,244,'#c0a274');c.line(103,249,115,244,'#a58a6a')
c.line(149,237,158,243,ink);c.line(150,237,159,243,'#a58a6a')
# Small stones on the lit path
for x,y in [(126,226),(137,235),(121,246),(143,250),(136,225),(129,240),(150,253)]:
 c.line(x,y,x+2,y,'#393339');c.set(x,y-1,'#a17a5d')
view(c)
print(c.stats_text())
save('ancient-dragon-battle',c)
finish(result)
