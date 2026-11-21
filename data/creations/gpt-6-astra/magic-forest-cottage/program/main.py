import random, math
random.seed(21)
c = new_canvas(128,128,background='#211b36',name='Moonlit cottage')
# restrained dusk palette
sky='#211b36'; deep='#191c2c'; ink='#171b25'; plum='#30223c'; purple='#3b2c4d'; haze='#51405e'; mist='#75617b'; moon='#f1dfbb'; moonsh='#cebdac'
# sky strata
c.rect(0,31,128,28,'#29213e'); c.rect(0,59,128,31,'#332b47')
# stars
for x,y in [(26,13),(46,8),(61,18),(86,9),(107,23),(34,27),(15,36),(117,7),(57,32),(95,30)]:
 c.set(x,y,'#ab889c')
c.line(59,9,59,13,'#b79aa9'); c.line(57,11,61,11,'#b79aa9')
# full moon
c.circle(91,22,14,'#3c304d'); c.circle(91,22,12,'#68536a'); c.circle(91,22,11,moonsh); c.circle(90,21,10,moon)
c.poly([(83,17),(85,14),(90,13),(87,17),(87,19),(83,20)],'#e1cdb3')
c.rect(94,24,3,3,'#ddc7ac'); c.set(92,29,'#ddc7ac'); c.line(85,27,87,28,'#ddc7ac')
# distant thin trees
for x in [6,19,30,43,64,76,108,119,126]:
 y=random.randint(20,45)
 c.poly([(x-3,91),(x-1,y+12),(x-3,y),(x,y+8),(x+2,89)],purple)
 c.line(x,y+24,x-9,y+13,purple); c.line(x,y+33,x+8,y+16,purple)
 c.line(x-7,y+15,x-9,y+7,purple)
# distant shrub shapes
for i in range(35):
 x=random.randrange(128); y=random.randrange(61,89)
 c.ellipse(x,y,random.randrange(4,11),random.randrange(3,7),'#40334f')
# mist banks behind cottage
c.poly([(0,77),(20,73),(39,75),(58,72),(83,75),(106,69),(127,72),(127,77),(98,75),(75,80),(41,78),(15,80),(0,81)],'#64516c')
c.line(2,76,27,76,'#8b7088'); c.line(98,73,121,73,'#92798f')
c.poly([(0,85),(29,82),(58,84),(83,81),(127,82),(127,87),(100,86),(75,88),(35,86),(0,89)],haze)
# rolling forest floor
c.poly([(0,91),(23,86),(45,89),(64,85),(90,88),(111,85),(127,89),(127,128),(0,128)],'#292b35')
c.poly([(0,105),(24,100),(48,104),(72,97),(94,104),(127,96),(127,128),(0,128)],'#30363b')
# cottage silhouette stone base and timber body
c.poly([(30,70),(55,45),(78,67),(78,91),(69,99),(29,93)],ink)
c.poly([(32,69),(55,48),(75,69),(75,90),(67,95),(32,91)],'#8b7568')
c.poly([(55,49),(75,68),(75,90),(66,94),(66,66)],'#5e5354')
c.rect(32,75,34,17,'#6c6570')
c.poly([(66,76),(75,72),(75,90),(66,94)],'#514e60')
# individually laid stone foundation
for yy in range(77,93,5):
 for xx in range(33,65,8):
  xx += (3 if yy%2 else 0)
  if xx<63: c.rect(xx,yy,random.randint(5,7),3,random.choice(['#8c8180','#776e79','#5c5866']))
for xx,yy in [(68,78),(69,84),(67,89)]: c.rect(xx,yy,5,3,'#6c626d')
# plaster and timber
c.poly([(35,67),(55,49),(65,64),(65,76),(35,76)],'#a98b71')
c.line(36,68,63,68,'#644b45'); c.rect(33,68,3,10,'#4b3a3c'); c.rect(63,64,3,15,'#4b3a3c')
c.line(40,66,55,52,'#59423f'); c.line(55,53,55,67,'#59423f')
# chimney behind roof
c.poly([(65,38),(72,37),(73,56),(66,55)],'#655866')
c.rect(64,36,10,4,ink); c.rect(65,36,8,2,'#a28b88')
c.line(67,43,71,43,'#a28b88'); c.line(65,48,69,48,'#a28b88')
# chimney smoke wisps
c.path('M 69 34 Q 63 29 69 25 Q 75 21 70 16', '#6b566f',fill=False)
c.path('M 72 32 Q 68 29 73 26', '#92768a',fill=False)
# broad steep mossy roof, bent fairy tale ridge
c.poly([(22,74),(31,62),(45,39),(50,32),(55,34),(62,43),(76,60),(84,67),(81,72),(59,64),(52,47),(41,65),(29,77)],ink)
c.poly([(25,72),(34,58),(46,38),(50,35),(53,36),(60,45),(73,62),(80,68),(76,69),(57,62),(51,43),(39,65),(29,73)],'#3e4b42')
c.poly([(51,36),(60,45),(75,65),(80,68),(76,69),(58,62),(52,46)],'#293c3a')
c.line(26,74,40,65,'#7d6c53'); c.line(40,65,51,46,'#7d6c53'); c.line(58,64,80,71,'#655344')
# ragged moss and wooden shingle clusters inside roof
for y in range(40,70,3):
 for x in range(28,77,4):
  col=c.get(x,y)
  if col in [c.color('#3e4b42'),c.color('#293c3a')]:
   color=random.choice(['#65734e','#7c8457','#4f6248','#35483f','#53614a'])
   c.line(x,y,x+random.randint(1,3),y,color)
   if random.random()<.45:c.set(x,y+1,color)
c.line(34,59,46,40,'#8b9060'); c.line(46,40,50,36,'#a1a16b')
for x,y in [(28,73),(32,70),(41,65),(59,64),(72,69),(77,71)]:
 c.line(x,y,x,y+random.randint(2,5),'#65734e')
# warm attic jewel
c.rect(49,57,9,10,'#4b3539'); c.rect(50,58,7,8,'#d47943'); c.rect(51,59,5,6,'#ffce78'); c.line(53,59,53,65,'#8a4b38'); c.line(50,62,57,62,'#8a4b38')
# front door, arched top
c.path('M 48 94 L 48 79 Q 53 72 58 79 L 58 94 Z',ink)
c.path('M 50 92 L 50 80 Q 53 76 56 80 L 56 92 Z','#765344')
c.line(52,81,52,92,'#523e3b'); c.line(55,80,55,91,'#a1714b'); c.set(55,86,'#efba65')
c.rect(48,93,13,3,'#aca08b'); c.rect(46,96,16,2,'#5f5d61')
# glowing front window
c.rect(35,76,11,12,'#332d37'); c.rect(36,77,9,9,'#bc643c'); c.rect(37,78,7,7,'#ffb75b'); c.rect(38,78,5,4,'#ffdb8a')
c.line(40,77,40,85,'#704138'); c.line(36,82,44,82,'#704138'); c.rect(34,87,13,2,'#a38164')
# side window
c.poly([(68,71),(73,69),(73,80),(68,82)],'#2c2933'); c.poly([(69,72),(72,71),(72,79),(69,80)],'#f5a24f'); c.line(70,72,70,79,'#945035')
# lantern on front beam
c.line(61,75,61,79,ink); c.rect(59,79,4,6,'#473634'); c.rect(60,80,2,3,'#ffda8b'); c.set(61,84,'#b36c41')
# path winds out to lower edge
c.poly([(49,98),(60,98),(64,104),(59,111),(63,117),(79,128),(48,128),(44,119),(46,111),(54,104)],'#41413f')
slabs=[([(49,99),(59,99),(61,102),(51,103),(48,102)],'#a49784'), ([(52,105),(61,104),(59,108),(48,109),(48,107)],'#827d7d'), ([(47,112),(57,111),(58,115),(45,116),(44,114)],'#a0968b'), ([(46,119),(59,118),(64,122),(49,124),(45,122)],'#7e7c7d'), ([(52,126),(66,124),(73,128),(51,128)],'#9b9290')]
for pts,col in slabs:
 c.poly([(x,y+1) for x,y in pts],ink); c.poly(pts,col); c.line(pts[0][0],pts[0][1],pts[1][0],pts[1][1],'#b4a595')
# well behind right foreground
c.ellipse(92,105,16,5,'#202730')
c.rect(80,91,23,13,'#565365'); c.ellipse(91,103,11,5,'#565365')
for yy in [94,99,104]:
 for xx in range(81,102,6):
  c.rect(xx+(2 if yy==99 else 0),yy,4,3,random.choice(['#8c8190','#6d687c','#a1979c']))
c.ellipse(91,91,13,6,'#aaa0a1'); c.ellipse(91,91,10,3,'#302e42'); c.line(84,93,96,93,'#55556e')
c.line(80,90,84,87,'#d0b9a8'); c.line(81,96,100,96,'#747084')
# well posts, wooden winch and crank
c.rect(80,76,3,19,'#3b3035'); c.rect(80,76,1,16,'#a47c5c')
c.rect(101,75,3,20,'#3b3035'); c.rect(101,76,1,17,'#926b54')
c.rect(79,76,25,4,'#47373b'); c.line(80,76,103,76,'#c29868'); c.line(83,78,100,78,'#92634b')
c.rect(88,75,6,6,'#b9976c')
for x in [89,91,93]:c.line(x,75,x,80,'#6e4f44')
c.line(91,81,91,90,'#c3a47b'); c.line(104,78,108,78,'#b98b60'); c.line(108,78,108,84,'#a47b5b'); c.rect(106,83,4,2,'#49383b')
# ancient framing trees
c.poly([(0,13),(7,15),(14,39),(16,64),(14,88),(18,108),(28,120),(17,116),(12,108),(8,114),(0,117),(0,105),(5,96),(7,75),(6,51),(1,35)],'#211f2c')
c.poly([(4,31),(9,43),(11,66),(9,90),(7,101),(11,109),(3,113),(6,99),(7,79),(7,56)],'#49303c')
c.poly([(10,56),(18,43),(20,29),(23,17),(26,14),(25,29),(22,45),(13,66)],'#282232')
c.poly([(17,44),(34,32),(38,20),(37,33),(29,41),(17,51)],'#282232')
c.line(10,78,12,52,'#67414a'); c.line(19,43,22,30,'#67414a')
c.poly([(127,16),(121,25),(117,42),(118,62),(115,79),(119,103),(111,118),(120,114),(124,108),(127,117)],'#201f2c')
c.poly([(122,34),(121,58),(119,77),(122,96),(124,104),(127,108),(126,93),(123,76),(124,56),(126,40)],'#4c3342')
c.poly([(119,61),(110,48),(108,32),(101,19),(107,22),(112,34),(114,46),(122,55)],'#292232')
c.poly([(111,41),(97,38),(88,32),(98,35),(110,36)],'#292232')
c.line(120,76,122,53,'#76505a'); c.line(122,97,120,82,'#76505a')
# angular leaf clusters dark wine and russet
clusters=[(3,9,19,10),(20,7,21,8),(39,5,13,7),(9,25,13,9),(26,21,12,7),(35,27,10,5),(0,43,10,7),(116,9,20,10),(126,26,15,12),(106,17,13,6),(115,36,10,6),(124,48,10,7)]
for cx,cy,rx,ry in clusters:
 for j in range(20):
  x=int(random.gauss(cx,rx/2)); y=int(random.gauss(cy,ry/2))
  if 0<=x<128 and 0<=y<128 and (x-91)**2+(y-22)**2>22**2:
   w=random.randrange(3,8); h=random.randrange(2,5)
   pts=[(max(0,x-w),y),(max(0,x-w+2),max(0,y-h)),(min(127,x+w-2),max(0,y-h)),(min(127,x+w),y),(min(127,x+w-2),min(127,y+h)),(x,min(127,y+h))]
   c.poly(pts,random.choice(['#312335','#3e283b','#502c3e','#623443','#713c48']))
# foreground foliage and fern silhouettes
for x,y in [(6,122),(19,124),(29,111),(36,121),(84,123),(102,118),(116,125),(121,112)]:
 c.line(x,y,x-1,y-9,'#182a30')
 for k in range(3):
  yy=y-3-k*3
  c.line(x,yy,x-5+k,yy-4,'#3e5049'); c.line(x,yy,x+5-k,yy-4,'#46574e')
# scattered grass and fallen leaves
for i in range(80):
 x=random.randrange(128); y=random.randrange(97,128)
 if c.get(x,y) in [c.color('#292b35'),c.color('#30363b'),c.color('#41413f')]:
  col=random.choice(['#58604e','#6e4a51','#8a5a54','#414a46'])
  c.line(x,y,min(127,x+2),y,col)
# mushrooms warm pinpoints
for x,y in [(24,105),(28,107),(106,111),(109,114)]:
 c.line(x,y,x,y+3,'#b9a192'); c.rect(x-2,y-1,5,2,'#a35859');c.rect(x-1,y-2,3,1,'#d78673');c.set(x-1,y-1,'#f0c2a1')
# small drifting mist ribbons in foreground
c.line(2,96,18,96,'#65576e'); c.line(16,97,25,97,'#65576e'); c.line(105,99,116,99,'#65576e')
c.line(1,98,10,98,'#483e56'); c.line(100,119,114,119,'#625468'); c.line(96,120,106,120,'#625468')
# fireflies
for x,y in [(22,82),(29,90),(77,81),(108,67),(18,61),(71,109)]:
 c.set(x,y,'#e4bb7c'); c.set(x,y+1,'#87775b')
# Consolidate nearby shades to a compact pixel-art palette.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(128) for x in range(128))
colors={p['index']:tuple(p['rgba'][:3]) for p in c.palette()}
replacement={i:i for i in counts}
while len(counts)>86:
 ids=list(counts)
 best=None
 for ia,a in enumerate(ids):
  for b in ids[ia+1:]:
   d=sum((colors[a][k]-colors[b][k])**2 for k in range(3))
   score=d*(min(counts[a],counts[b])**0.35)
   if best is None or score<best[0]:best=(score,a,b)
 _,a,b=best
 if counts[a]>counts[b]:a,b=b,a
 for k in replacement:
  if replacement[k]==a:replacement[k]=b
 counts[b]+=counts[a];del counts[a]
for y in range(128):
 for x in range(128):
  old=c.get(x,y)
  if replacement[old]!=old:c.set(x,y,replacement[old])
result=c
view(result)
finish(result)
