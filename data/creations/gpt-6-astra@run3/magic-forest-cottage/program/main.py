import random, math
random.seed(23)
c = new_canvas(128,128,background='#20162f',name='Moonwood cottage')
# A deliberately limited, cool-to-warm palette
sky='#20162f'; deep='#161625'; plum='#2f1d38'; haze='#44314d'; fog='#63516d'
ink='#211c29'; bark='#35232f'; wood='#593740'; woodlit='#80504b'; gold='#e68a4c'; light='#ffd891'
# layered night sky
c.rect(0,29,128,37,'#2b203d'); c.rect(0,53,128,30,'#352941')
# moon halo and cratered disk
c.circle(94,24,17,'#30253f'); c.circle(94,24,14,'#4a3b54'); c.circle(94,24,11,'#d5c8b7'); c.circle(93,23,10,'#eee0bd')
c.poly([(97,15),(102,20),(103,27),(98,32),(93,33),(97,28),(99,23)],'#c3b7ad')
c.rect(88,19,3,2,'#d5c8b7'); c.rect(90,17,2,1,'#d5c8b7'); c.rect(86,25,2,3,'#d5c8b7'); c.set(94,29,'#d5c8b7')
for x,y in [(30,17),(51,9),(72,20),(80,7),(108,43),(40,30),(63,25),(23,36),(114,13)]:
 c.set(x,y,'#b8a3a7')
c.line(72,9,72,13,'#a18a9a');c.line(70,11,74,11,'#a18a9a');c.set(72,11,'#eee0bd')
# distant skeletal trees
for x,y,w in [(4,27,4),(25,23,3),(42,18,3),(76,35,3),(110,24,4),(121,17,4)]:
 col='#3f304a'
 c.poly([(x-w,89),(x-1,y+17),(x-4,y),(x,y+3),(x+3,y+31),(x+w,91)],col)
 c.line(x,y+37,x-12,y+17,col);c.line(x-11,y+18,x-12,y+9,col)
 c.line(x,y+46,x+12,y+22,col);c.line(x+9,y+28,x+8,y+15,col)
# low fog ribbons, behind buildings
c.poly([(0,65),(15,63),(37,66),(60,64),(87,64),(106,59),(127,60),(127,76),(93,79),(62,74),(26,78),(0,76)],'#4b3d58')
c.poly([(0,71),(24,69),(41,72),(82,70),(108,66),(127,67),(127,70),(98,70),(75,74),(35,74),(0,76)],'#5a4964')
c.line(2,68,21,68,'#6b5671');c.line(102,64,124,64,'#6b5671')
# uneven woodland floor
c.poly([(0,84),(19,80),(39,85),(61,86),(87,81),(109,79),(127,83),(127,128),(0,128)],'#282b36')
c.poly([(0,100),(29,91),(57,95),(80,91),(108,94),(127,90),(127,128),(0,128)],'#30353b')
c.poly([(0,116),(27,102),(63,107),(96,101),(127,112),(127,128),(0,128)],'#34343e')
# stone slab path, widening toward viewer
for pts in [[(59,95),(67,95),(68,98),(58,99)],[(56,101),(66,100),(69,104),(56,105)],[(53,107),(67,106),(71,111),(51,113)],[(46,117),(61,113),(68,116),(65,121),(45,123)],[(67,123),(78,120),(86,124),(85,128),(66,128)]]:
 c.poly([(x,y+2) for x,y in pts],deep);c.poly(pts,'#737078');c.line(pts[0][0],pts[0][1],pts[1][0],pts[1][1],'#a19496')
# chimney behind roof
c.poly([(69,40),(69,23),(80,23),(80,51)],ink);c.rect(71,25,7,20,'#65565e')
for x,y in [(71,27),(75,31),(71,35),(76,39)]:c.rect(x,y,3,2,'#938083')
c.rect(68,22,13,3,'#302a38');c.line(69,22,79,22,'#a29291')
# wisps of chimney smoke
c.poly([(72,20),(74,16),(70,12),(71,8),(75,6),(73,11),(78,16),(77,20)],'#514054')
# house shadow and stone foundation
c.ellipse(61,95,29,6,'#20252e')
c.poly([(36,64),(60,41),(85,65),(85,94),(76,99),(37,96)],ink)
c.rect(39,65,43,26,'#685048');c.poly([(73,61),(84,66),(84,92),(74,96)],'#48383d')
c.rect(38,87,44,9,'#514d54')
# stone courses
for y in [87,91]:
 for x in range(39,81,7):
  xx=x+(3 if y==91 else 0)
  if xx<81:c.rect(xx,y,min(6,82-xx),3,random.choice(['#6f6669','#817477','#625d65']))
# wall plaster and heavy old timbers
c.rect(42,66,29,21,'#9a7155');c.rect(44,68,26,2,'#b18b63')
c.line(40,66,40,87,'#3e2b30');c.rect(72,64,3,28,'#3e2b30');c.line(74,66,82,73,'#382b31')
c.line(41,85,71,85,'#533b35');c.line(42,83,51,73,'#654332')
# roof silhouette, steep fairy tale pitch
roof=[(27,68),(34,57),(43,43),(52,33),(59,26),(65,33),(74,47),(82,57),(91,68),(84,72),(58,40),(35,71)]
c.poly(roof,ink)
c.poly([(29,65),(40,47),(52,33),(59,28),(64,35),(74,51),(87,66),(81,67),(59,36),(35,66)],'#3c4c49')
# broad near roof slope, the gable at right catches warm reflected light
c.poly([(30,65),(41,47),(53,33),(59,29),(62,36),(58,42),(51,53),(41,66)],'#465a4b')
# shingles laid in staggered rows on the left slope
for y in range(37,65,4):
 left=int(54-(y-37)*.68);right=int(61-(y-37)*.65)
 for x in range(left,right+1,4):
  c.line(x,y,x+3,y,random.choice(['#283e3d','#334740','#627151']))
  c.set(x,y-1,'#79815b')
# right slope wooden scallops and moss
for i in range(8):
 x=62+i*3;y=36+i*4
 c.line(x,y,x+4,y+3,'#657355');c.line(x+1,y+3,x+4,y+5,'#2d3a37')
# moss clusters on roof
for i in range(65):
 y=random.randint(37,63);x=int(56-(y-37)*.67)+random.randint(-3,3)
 c.rect(x,y,random.choice([1,2,3]),1,random.choice(['#7b8659','#647950','#4d6547']))
c.line(30,66,40,66,'#929069');c.line(58,30,85,66,'#768160');c.line(35,69,59,40,'#493c37')
c.line(60,40,83,69,'#b18b63');c.line(61,43,81,68,'#6f4b3c')
# hanging strands of roof moss
for x,y,l in [(32,66,4),(37,66,3),(43,61,3),(80,64,4),(85,67,4)]:c.line(x,y,x,y+l,'#526c4b');c.set(x,y+l,'#7b8659')
# triangular gable face
c.poly([(46,64),(59,45),(73,64)],'#896448');c.line(59,45,59,64,'#49312e')
# small round attic window
c.circle(59,57,5,'#3a2a30');c.circle(59,57,3,'#ee9b50');c.circle(58,56,2,'#ffd891');c.line(59,54,59,60,'#70422e');c.line(56,57,62,57,'#70422e')
# glowing main window
c.rect(43,71,14,12,'#392b30');c.rect(44,72,12,9,'#d3773f');c.rect(45,72,10,7,'#ffb55d');c.rect(46,72,8,3,'#ffe5a3')
c.line(49,72,49,81,'#815033');c.line(44,77,55,77,'#815033');c.rect(42,82,16,2,'#3c3032');c.line(43,82,56,82,'#b78051')
c.rect(41,72,2,9,'#5f3f35');c.rect(57,72,2,10,'#5f3f35')
# arched door
c.poly([(61,93),(61,74),(63,71),(68,71),(71,75),(71,93)],'#342931')
c.poly([(63,92),(63,75),(65,73),(67,73),(69,76),(69,92)],'#6f493a')
c.line(65,78,65,91,'#4d3331');c.line(68,78,68,91,'#4d3331');c.rect(64,75,4,4,'#ffc377');c.line(66,75,66,79,'#7c4b36');c.set(68,85,'#ebba6d')
c.rect(60,94,13,2,'#9a8680');c.rect(58,96,17,2,'#625a60')
# side window
c.poly([(77,74),(82,76),(82,83),(77,82)],'#d77944');c.line(79,75,79,82,'#553930');c.line(77,78,82,79,'#553930')
# tiny lantern at entrance
c.line(74,72,76,70,'#25222b');c.rect(74,73,3,5,'#e68a4c');c.set(75,74,'#ffe5a3');c.line(73,72,77,72,'#25222b');c.line(74,78,76,78,'#25222b')
# well casting shadow to the right
c.ellipse(100,108,16,4,'#20252e')
# well posts and cross bar, distinctly open wooden winch
c.rect(88,79,3,24,'#30282f');c.rect(89,80,1,22,'#9a6c50');c.rect(108,78,3,25,'#30282f');c.rect(108,79,1,22,'#936148')
c.rect(87,78,25,3,'#593e37');c.line(88,78,110,78,'#b38964')
c.line(90,87,109,87,'#b28357');c.rect(96,85,6,4,'#734833');c.line(97,85,97,88,'#c39766');c.line(100,85,100,88,'#c39766')
c.line(112,87,112,92,'#b28357');c.line(109,87,112,87,'#b28357');c.rect(111,91,4,2,'#593e37')
c.line(99,89,99,100,'#b6a081')
# circular stone well rim and body
c.ellipse(99,102,12,5,'#37333e');c.rect(87,101,25,7,'#55545f');c.ellipse(99,108,12,4,'#55545f')
for y in [102,106]:
 for x in range(88,111,6):
  c.rect(x+(2 if y==106 else 0),y,5,3,random.choice(['#77747e','#686975','#8b8185']))
c.ellipse(99,100,12,5,'#999097');c.ellipse(99,100,8,2,'#272734');c.line(94,99,104,99,'#141d2b');c.line(94,101,102,101,'#4e5964')
c.line(88,100,88,103,'#b4a2a0');c.line(92,103,104,103,'#b4a2a0');c.line(93,96,93,98,'#5a5360');c.line(103,96,103,98,'#5a5360')
# bucket beside well
c.poly([(80,104),(86,104),(85,110),(81,110)],'#73513d');c.line(81,105,85,105,'#b09676');c.line(81,108,85,108,'#b09676');c.path('M81 104 Q80 99 84 100 L86 104','#9b8b7e',fill=False)
# foreground trees: gnarled silhouettes and forked reaching branches
c.poly([(0,127),(0,15),(8,12),(13,39),(12,57),(18,74),(17,91),(24,111),(34,120),(21,118),(13,108),(10,116)],'#241e2a')
c.poly([(4,111),(7,86),(6,63),(3,37),(8,44),(11,61),(14,76),(13,92),(19,110),(27,117),(17,111),(12,99),(11,111)],'#4f3440')
c.poly([(9,61),(16,44),(18,28),(28,17),(25,17),(15,25),(12,43),(7,49)],'#2b202d')
c.poly([(15,37),(26,32),(35,21),(33,20),(24,28),(16,30)],'#352330')
c.line(14,44,18,30,'#6a414b');c.line(19,28,25,21,'#6a414b')
c.poly([(6,45),(1,36),(0,24),(4,32),(10,38)],'#4f3440')
c.line(9,70,10,83,'#79505a');c.line(9,89,8,102,'#79505a')
c.poly([(115,128),(120,108),(116,92),(120,71),(118,52),(110,39),(108,25),(112,29),(114,39),(123,48),(126,61),(125,89),(127,103),(127,128)],'#241e2a')
c.poly([(122,115),(120,93),(124,70),(122,54),(125,58),(127,74),(124,93),(127,112)],'#50333f')
c.poly([(121,65),(111,53),(104,49),(102,42),(106,46),(113,49),(124,59)],'#352330')
c.line(120,56,112,46,'#69424c');c.line(121,91,123,80,'#79505a')
# clusters of dark wine, aubergine and rust leaves framing the sky
clusters=[(1,7,15,10),(17,7,16,8),(34,3,16,7),(7,23,10,10),(25,17,10,7),(39,11,8,6),(56,1,13,5),(119,5,15,12),(125,22,12,11),(115,34,10,7),(125,42,7,8)]
for cx,cy,rx,ry in clusters:
 for i in range(30):
  x=cx+random.randint(-rx,rx);y=cy+random.randint(-ry,ry)
  if 0<=x<126 and 0<=y<126:
   col=random.choice(['#2b1e30','#392332','#482735','#592d3c','#693543'])
   c.rect(x,y,random.randint(2,5),random.randint(1,3),col)
for x,y in [(29,28),(33,30),(22,42),(112,57),(108,64),(20,76),(116,74)]:
 c.rect(x,y,2,1,'#89505a');c.set(x+1,y+1,'#592d3c')
# ground vegetation, fern tufts, mushrooms and scattered fallen leaves
for i in range(160):
 x=random.randrange(128);y=random.randrange(93,128)
 if 42<x<77 or 80<x<115 and y<113:continue
 col=random.choice(['#4a4d46','#545345','#493940','#68504c','#393d40'])
 c.line(x,y,min(127,x+random.randrange(1,4)),y,col)
for x,y in [(28,98),(35,107),(18,122),(92,119),(116,116),(75,105),(29,87)]:
 c.line(x,y,x-2,y-5,'#687153');c.line(x,y,x+3,y-6,'#52654e');c.line(x-1,y-2,x-4,y-3,'#52654e');c.line(x+1,y-3,x+4,y-3,'#687153')
for x,y in [(25,110),(31,113),(114,103)]:
 c.line(x,y-3,x,y,'#b8a491');c.rect(x-2,y-4,5,2,'#9a5659');c.rect(x-1,y-5,3,1,'#c78273');c.set(x-1,y-4,'#e0b999')
# delicate horizontal mist pooled among the trees
c.line(0,92,8,92,'#665770');c.line(18,86,31,86,'#665770');c.line(22,87,34,87,'#51485e');c.line(109,90,118,90,'#665770')
c.line(3,119,14,119,'#51485e');c.line(0,120,20,120,'#464051');c.line(102,119,120,119,'#51485e');c.line(110,120,127,120,'#464051')
# a handful of fairy lights
for x,y in [(23,65),(31,81),(89,73),(112,84),(37,102),(80,116)]:
 c.set(x,y,'#c5b482');c.set(x,y+1,'#777757')
# Consolidate near-identical shades while preserving the pixel clusters.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(128) for x in range(128))
palette={p['index']:p['rgba'] for p in c.palette()}
remap={i:i for i in counts}
while len(counts)>86:
 keys=list(counts)
 best=None
 for aidx,a in enumerate(keys):
  for b in keys[aidx+1:]:
   ca,cb=palette[a],palette[b]
   dist=sum(w*(ca[k]-cb[k])**2 for k,w in enumerate([0.9,1.2,1.0]))
   score=dist*(min(counts[a],counts[b])**0.35)
   if best is None or score<best[0]:best=(score,a,b)
 _,a,b=best
 if counts[a]>counts[b]:a,b=b,a
 for key in remap:
  if remap[key]==a:remap[key]=b
 counts[b]+=counts.pop(a)
for y in range(128):
 for x in range(128):
  old=c.get(x,y)
  if remap[old]!=old:c.set(x,y,remap[old])
result=c
view(result)
finish(result)
