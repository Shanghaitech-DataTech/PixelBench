import random
random.seed(22)
c=new_canvas(128,128,background='#211b38',name='Moonlit cottage')
# distant violet sky
c.rect(0,35,128,42,'#30213f'); c.rect(0,61,128,40,'#3c294b')
c.circle(87,23,15,'#40334e');c.circle(87,22,12,'#c6b9c6');c.circle(85,20,10,'#e5d7cd')
c.circle(89,18,3,'#cbbfca');c.circle(81,23,2,'#cbbfca');c.set(89,28,'#f3e6d2')
for x,y in [(34,10),(57,8),(69,28),(106,39),(43,29),(17,35),(110,13)]: c.set(x,y,'#a493b2')
# remote trees
for x in [3,19,32,49,65,103,118]:
 c.poly([(x-3,86),(x,27),(x+2,18),(x+3,67),(x+7,87)],'#30263f')
 c.line(x,47,x-10,31,'#30263f');c.line(x,54,x+11,32,'#30263f')
 c.line(x,37,x+6,20,'#30263f')
c.poly([(0,86),(19,80),(39,86),(64,78),(95,81),(127,75),(127,128),(0,128)],'#292b3c')
# low mist ribbons
for x,y,w in [(0,76,35),(15,80,53),(88,72,40),(80,83,44),(1,89,25)]:
 c.rect(x,y,w,2,'#514157');c.rect(x+4,y-1,w-9,1,'#514157')
# cottage silhouette and walls
c.poly([(28,70),(59,29),(74,36),(97,72),(93,99),(31,102)],'#171f2c')
c.rect(34,65,56,31,'#6f5551');c.poly([(70,60),(90,70),(90,95),(70,95)],'#4a4145')
# plaster panels
c.rect(39,70,25,18,'#9a7660');c.rect(42,71,19,14,'#ad886c')
c.rect(73,73,13,17,'#7b5e50')
# stone footing
c.rect(32,91,60,11,'#363c46')
for row in range(3):
 for x in range(33-row%2*4,91,9):
  y=92+row*3
  c.rect(x,y,7,2,random.choice(['#68656a','#787175','#52555e']))
# wooden structural beams
for x in [35,66,88]:
 c.rect(x,68,3,25,'#392f35');c.line(x,73,x,87,'#6c4b40')
c.rect(36,88,53,3,'#423539');c.line(73,89,86,76,'#43353a')
# door
c.rect(55,77,11,23,'#302a32');c.rect(57,79,7,20,'#674838')
for x in [58,61,63]:c.line(x,81,x,98,'#46332e')
c.set(62,90,'#e7aa62')
# window amber surrounds
c.rect(40,73,13,14,'#52382f');c.rect(41,74,11,11,'#c2713e');c.rect(42,74,9,10,'#f4b859');c.rect(43,75,7,6,'#ffe0a0')
c.line(46,74,46,85,'#694231');c.line(41,80,51,80,'#694231');c.rect(39,86,15,2,'#2c2b31')
c.rect(75,75,9,11,'#372e33');c.rect(76,76,7,8,'#e59245');c.rect(77,76,4,5,'#ffd78b');c.line(79,76,79,84,'#795039')
# chimney behind roof
c.rect(76,36,8,19,'#554b50')
for y in [38,43,48]:c.line(76,y,82,y,'#8b7776')
c.rect(75,34,10,3,'#342f3c')
# steep roof
c.poly([(25,73),(32,60),(58,28),(66,31),(77,50),(96,73),(84,70),(64,45),(57,39),(38,70)],'#192b30')
c.poly([(29,68),(58,31),(63,33),(71,48),(86,67),(74,61),(59,39),(39,67)],'#3c5145')
c.poly([(58,32),(62,33),(76,55),(91,69),(83,68),(67,51)],'#293b37')
# broken moss courses
for y in range(39,69,4):
 left=int(58-(y-32)*.78);right=int(61+(y-32)*.48)
 for x in range(left+1,right,4):
  if random.random()<.8:c.rect(x,y,random.choice([2,3,4]),1,random.choice(['#637354','#7b8059','#4e644c','#263e38']))
c.line(26,73,39,70,'#778061');c.line(39,70,58,42,'#697553');c.line(60,40,83,69,'#566b4d');c.line(83,69,96,73,'#53644b')
# attic window
c.poly([(51,62),(58,50),(65,61)],'#362f35');c.rect(53,60,10,9,'#362f35');c.rect(55,60,6,7,'#e59849');c.rect(56,59,4,6,'#ffcf79');c.line(58,59,58,67,'#624537')
# doorstep and wandering slabs
c.rect(54,100,15,3,'#8b7c76');c.rect(53,103,16,2,'#50515a')
for pts in [[(55,106),(66,105),(71,108),(60,110),(53,109)],[(61,112),(74,110),(79,114),(68,117),(59,115)],[(69,119),(85,116),(91,121),(83,125),(66,124)],[(80,127),(94,124),(102,127)]]:
 c.poly(pts,'#77717a');c.line(pts[0][0],pts[0][1],pts[1][0],pts[1][1],'#a09594')
# grass and stones
for i in range(180):
 x=random.randrange(128);y=random.randrange(92,128)
 if (30<x<94 and y<105) or (53<x<103 and y>104):continue
 c.line(x,y,x+random.choice([-1,0,1]),y-random.choice([0,1,2]),random.choice(['#414847','#535447','#333b3e']))
# well shadow and stone ring
c.ellipse(23,113,17,5,'#202733');c.rect(10,102,25,11,'#41464f');c.ellipse(22,111,13,5,'#41464f')
for row in range(3):
 for x in range(11+(row%2)*3,34,7):c.rect(x,103+row*3,5,2,random.choice(['#77777b','#65666e','#8a8386']))
c.ellipse(22,101,14,5,'#939099');c.ellipse(22,101,10,3,'#242935');c.line(13,104,30,104,'#b0a1a0')
# well posts and winch
for x in [9,34]:
 c.rect(x,84,3,22,'#342a30');c.line(x,85,x,102,'#936449')
c.rect(9,87,28,3,'#684837');c.line(10,87,36,87,'#bc8659')
c.rect(19,86,7,5,'#9b704d')
for x in [20,22,24]:c.line(x,86,x,90,'#d1a77a')
c.line(23,91,23,101,'#b29a78');c.line(37,88,39,88,'#a57a55');c.line(39,88,39,93,'#a57a55');c.rect(37,93,4,2,'#503c35')
# ancient framing tree trunks
for pts in [[(0,121),(7,95),(8,69),(5,46),(0,38),(0,24),(11,42),(16,67),(14,96),(22,121),(12,115),(8,127)],[(113,119),(119,94),(116,71),(121,47),(118,26),(125,13),(128,14),(126,49),(123,72),(127,99),(127,125),(121,118)]]:c.poly(pts,'#211f2d')
for pts in [[(10,65),(16,43),(29,30),(32,18),(36,15),(33,33),(22,46),(15,76)],[(6,48),(20,25),(19,13),(24,3),(25,5),(23,17),(25,27),(12,53)],[(119,68),(109,50),(98,43),(95,32),(99,37),(115,46),(124,60)],[(122,40),(109,28),(104,13),(109,18),(113,26),(125,31)]]:c.poly(pts,'#282332')
c.path('M 9 110 L 11 93 L 11 69 L 8 47 M 12 65 L 19 44 L 29 33 M 121 110 L 120 88 L 120 68 L 124 47', '#51404a',fill=False)
# canopy pixel clusters
for i in range(155):
 x=random.randrange(128);y=random.randrange(36)
 if (x<40 and y<24-x//5) or (x>99 and y<26) or y<7:
  col=random.choice(['#302333','#41283b','#502e40','#603541','#713e45'])
  c.rect(x,y,random.randint(2,7),random.randint(2,4),col)
# sparse fallen crimson leaves, mushrooms, fireflies
for x,y in [(17,120),(39,115),(99,115),(108,105),(46,124),(31,119)]:c.rect(x,y,3,1,'#80494e')
for x,y in [(42,107),(102,117),(6,111)]:
 c.line(x,y,x,y+3,'#a99689');c.rect(x-2,y-1,5,2,'#a85853');c.set(x-1,y-1,'#d79879')
for x,y in [(30,82),(101,83),(44,96),(100,104),(18,66)]:
 c.set(x,y,'#e3c183');c.set(x,y+1,'#7f7758')
# Merge the closest shades to keep a compact pixel-art palette.
from collections import Counter
while True:
 counts=Counter(c.get(x,y) for y in range(128) for x in range(128))
 if len(counts)<=86:break
 pal={p['index']:p['rgba'] for p in c.palette()}
 ids=list(counts)
 a,b=min(((a,b) for i,a in enumerate(ids) for b in ids[i+1:]),key=lambda ab:sum((pal[ab[0]][k]-pal[ab[1]][k])**2 for k in range(3)))
 if counts[a]>counts[b]:a,b=b,a
 for y in range(128):
  for x in range(128):
   if c.get(x,y)==a:c.set(x,y,b)
view(c)
finish(c)
