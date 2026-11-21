import random
random.seed(18)
result=new_canvas(128,128,background='#080c1b',name='cyberpunk_alley')
c=result
# tightly controlled midnight palette
ink='#070a16'; deep='#101327'; wall='#171a32'; blue='#202940'; edge='#2b3651'; teal='#16778b'; cyan='#54d9e1'; ice='#bbf5ed'; pink='#ee458d'; pale='#ff98c0'; purple='#713665'; gold='#ffd281'
# distant wedge of night and layered towers
c.poly([(40,0),(88,0),(91,83),(43,83)],'#111e32')
c.rect(48,4,17,66,'#19283c'); c.rect(68,0,14,73,'#142236')
c.rect(58,0,3,55,'#24334b'); c.rect(73,6,5,3,edge)
for x,y in [(52,16),(52,25),(62,36),(71,14),(75,31),(67,48),(58,53)]:
 c.rect(x,y,2,3,'#376071')
c.rect(62,55,13,28,'#244656');c.rect(65,60,7,23,'#356573');c.rect(68,64,2,19,'#6ab0b7')
# alley pavement
c.poly([(45,78),(82,78),(128,107),(128,128),(0,128),(0,106)],'#121b2c')
c.poly([(59,80),(72,80),(102,128),(29,128)],'#192b3c')
# left building facade, roof, plumbing
c.poly([(0,0),(37,0),(45,17),(45,82),(0,110)],wall)
c.poly([(0,0),(29,0),(29,91),(0,109)],'#1c1c33')
c.line(31,3,31,90,edge);c.line(34,0,34,88,ink)
c.poly([(36,21),(46,25),(46,79),(36,86)],'#10182a')
for y in [11,32,50,70]:
 c.line(0,y,28,y+5,'#29283f')
# windows high left
c.rect(4,4,19,18,ink);c.rect(6,6,15,13,'#26334a')
c.rect(8,7,4,10,'#435368');c.line(15,6,15,18,ink)
c.line(6,13,20,13,ink)
c.rect(1,36,24,14,ink)
for y in range(38,49,3): c.line(3,y,23,y,'#303349')
# right massive architecture
c.poly([(88,0),(128,0),(128,110),(83,81),(83,21)],'#161526')
c.poly([(100,0),(128,0),(128,109),(100,94)],'#20182d')
c.line(99,0,99,93,'#373049');c.line(86,22,86,81,edge)
c.rect(106,7,17,22,ink);c.rect(109,9,12,16,'#29253c')
c.line(114,9,114,25,'#494054');c.line(109,18,120,18,'#554051')
# drain pipes
c.line(125,0,125,99,'#3b3049');c.line(123,0,123,98,ink)
for y in (21,49,76): c.rect(122,y,5,2,'#584055')
# far doors / lamps
c.rect(39,58,8,24,ink);c.rect(40,60,5,18,'#1d3d4c');c.rect(43,61,1,14,teal)
c.rect(79,49,7,32,ink);c.rect(81,52,3,23,'#323148')
c.rect(79,48,6,2,pink);c.line(80,51,80,61,purple)
# shop left entrance
c.poly([(0,65),(27,62),(27,94),(0,109)],ink)
c.poly([(2,68),(24,65),(24,93),(2,104)],'#203348')
c.poly([(4,69),(12,68),(12,97),(4,101)],'#25495b')
c.poly([(15,68),(23,67),(23,92),(15,96)],'#193347')
c.line(13,67,13,99,ink);c.line(2,84,24,77,'#101b2b')
c.rect(19,81,1,5,cyan)
# overhead slatted awning
c.poly([(0,57),(27,55),(33,63),(0,69)],'#27304a')
for x in range(0,29,6): c.line(x,58,x+3,64,'#45405e')
c.line(0,68,32,62,ink);c.line(1,69,30,64,teal)
# left neon sign frame
c.rect(1,24,30,12,ink);c.rect(2,25,28,10,'#63305e');c.rect(3,26,26,8,'#231d36')
c.text(5,27,'NOOD',pale,spacing=0);c.line(3,34,28,34,pink)
# hanging cyan vertical sign
c.rect(35,20,11,3,ink);c.rect(41,22,10,27,ink)
c.rect(42,23,8,25,teal);c.rect(43,24,6,23,'#123447')
# small graphic ideograms, deliberate neon strokes
for y in (26,35):
 c.line(44,y,48,y,ice);c.line(46,y-1,46,y+6,cyan);c.line(44,y+3,48,y+3,cyan);c.set(44,y+5,ice);c.set(48,y+5,cyan)
c.line(43,46,48,46,cyan)
# right hot pink projecting sign
c.line(87,15,101,15,ink);c.line(91,18,101,18,edge)
c.rect(89,18,12,29,'#582544');c.rect(90,19,10,27,pink);c.rect(91,20,8,25,'#291c35')
c.text(93,22,'B',pale);c.text(93,30,'A',pale);c.text(93,38,'R',pale)
c.line(89,21,89,44,'#8d315e')
# right storefront and vending machines
c.poly([(103,44),(128,42),(128,101),(103,90)],ink)
c.rect(104,43,24,6,'#702c58');c.rect(106,44,22,2,pink)
c.rect(105,51,16,41,'#374157');c.rect(106,52,13,37,'#245368')
c.rect(108,54,10,5,cyan);c.rect(109,55,8,3,ice)
c.rect(108,61,10,19,ink)
for y in (63,69,75):
 c.rect(109,y,3,4,'#e77a99');c.set(109,y, gold)
 c.rect(114,y,3,4,'#4bb9c6');c.set(114,y,ice)
 c.line(108,y+4,117,y+4,'#427387')
c.rect(109,83,7,4,ink);c.line(109,83,115,83,teal)
c.rect(119,61,1,15,cyan);c.rect(119,79,1,3,pink)
c.line(106,90,120,94,'#102037')
c.rect(123,52,5,44,'#55304c');c.rect(124,54,4,6,pink);c.rect(124,63,4,20,'#19253b')
for y in (65,71,77):c.rect(125,y,2,3,gold)
c.rect(124,87,4,4,ink)
# bundled overhead power cables, with highlights
for d in [0,3,8]:
 c.path(f'M 0 {8+d} Q 53 {38+d} 127 {9+d}',ink,fill=False)
c.path('M 0 9 Q 52 38 127 10','#303047',fill=False)
c.path('M 28 0 Q 50 31 89 14',ink,fill=False)
c.path('M 0 46 Q 40 61 88 37',ink,fill=False)
c.line(57,27,57,40,ink);c.rect(55,39,5,3,ink);c.rect(56,41,3,1,gold)
c.line(107,21,107,37,ink);c.rect(106,36,3,3,ink)
# pavement seams
for a,b in [((47,85),(10,127)),((79,85),(121,126)),((60,84),(48,127))]:c.line(*a,*b,'#243446')
c.line(0,116,127,102,ink);c.line(27,96,94,92,'#0c1526')
# broken puddle reflections: horizontal pixel clusters
for i in range(120):
 y=random.randrange(84,128)
 if i%3==0:
  center=111+(y-97)//5; col=random.choice(['#492a49','#723452','#aa3b6a','#ee458d'])
 elif i%3==1:
  center=39-(y-85)//3;col=random.choice(['#205063','#277c8d','#369eac','#54d9e1'])
 else:
  center=67;col=random.choice(['#214252','#2e5d6b','#3b8490'])
 x=center+random.randrange(-9,10); w=random.randrange(2,10)
 if 0<=x and x+w<=128:c.rect(x,y,w,1,col)
# nearby long ripples
for x,y,w,col in [(2,118,20,teal),(11,120,11,cyan),(4,123,28,'#254c61'),(86,120,28,purple),(96,121,20,pink),(71,108,15,'#347786'),(46,91,10,'#4a8994')]:c.rect(x,y,w,1,col)
# curb edges and rubbish
c.line(0,111,41,85,'#34475a');c.line(0,113,41,87,ink)
c.line(88,85,127,110,'#50334c')
c.poly([(15,99),(19,91),(26,91),(31,98),(29,103),(20,107)],'#0b1323');c.line(19,93,23,92,'#334153')
c.rect(2,91,8,15,'#172a38');c.line(2,91,9,91,'#456373')
c.poly([(88,111),(94,110),(98,112),(92,114)],'#697278');c.line(90,111,94,111,'#9b9290')
# rain behind figure: dark and brightly caught short streaks
for i in range(100):
 x=random.randrange(1,127);y=random.randrange(0,123)
 col=random.choice(['#2b3a51','#2b3a51','#38536a','#407989'])
 c.line(x,y,x-1,y+random.randrange(2,5),col)
# figure reflection and shadow
c.ellipse(68,112,12,3,'#0a1120')
c.poly([(63,113),(71,113),(75,126),(62,126)],'#111725')
for y in (116,121,125):c.line(60,y,75,y,'#294451')
# person silhouette: boots, separate legs, coat
c.poly([(62,96),(68,97),(66,110),(62,110)],ink)
c.poly([(69,97),(73,96),(75,109),(71,110)],ink)
c.rect(60,109,7,3,ink);c.rect(71,109,7,3,ink)
c.line(61,109,61,110,'#45556c');c.line(73,109,77,110,'#593c5b')
c.poly([(62,79),(69,78),(73,83),(74,99),(60,99),(61,89),(57,92),(55,89)],ink)
c.poly([(62,81),(65,80),(64,91),(62,97),(60,97)],'#26394e')
c.line(70,82,72,97,'#513149');c.line(63,98,70,98,'#293048')
# neck and head
c.rect(64,76,5,5,'#1b1826');c.ellipse(66,73,4,5,ink)
c.line(63,72,63,75,'#4f6271');c.set(69,76,'#9b6580')
# umbrella handle and raised arm
c.line(75,67,75,88,'#6e9ca7');c.path('M 75 87 Q 75 92 71 90',edge,fill=False)
c.line(69,85,73,87,ink);c.rect(73,84,3,3,'#8a7a87');c.set(75,84,'#c4b6b4')
# clear umbrella canopy: background remains readable through blue-tinted glass
# take underlying pixels and tint manually to limited glass colors
can=new_canvas(128,128,name='canopy_mask')
can.path('M 48 71 Q 51 57 65 54 Q 81 51 93 69 L 85 67 L 78 69 L 69 67 L 60 70 L 54 69 Z','#ffffff')
glass=['#24384e','#30495e','#3b596c','#496c7c']
for y in range(53,72):
 for x in range(48,94):
  if can.get(x,y)!=can.get(0,0):
   # preserve luminous elements through canopy in quantized tones
   idx=c.get(x,y);rgba=c.palette()[idx]['rgba'];brightness=sum(rgba[:3])//3
   c.set(x,y,glass[min(3,brightness//45)])
c.path('M 48 71 Q 51 57 65 54 Q 81 51 93 69','#75bdcc',fill=False)
c.path('M 48 71 L 54 69 L 60 70 L 69 67 L 78 69 L 85 67 L 93 69','#73a2b4',fill=False)
c.path('M 69 54 Q 60 59 60 69', '#548296',fill=False)
c.path('M 69 54 Q 72 58 78 68','#548296',fill=False)
c.path('M 69 54 Q 83 57 85 67','#548296',fill=False)
c.line(69,52,69,54,ice);c.line(54,61,59,57,ice);c.line(61,56,66,54,ice)
c.line(88,62,91,66,pale)
# foreground rain beads / splashes
for x,y in [(50,64),(83,58),(57,65),(73,59),(90,70),(47,74),(99,114),(31,113),(85,101),(42,121)]:
 c.line(x,y,x,y+1,'#80b0bd')
for x,y in [(22,110),(86,116),(48,101),(111,105)]:
 c.line(x-2,y,x+2,y,'#578b9c');c.set(x-3,y-1,'#578b9c');c.set(x+3,y-1,'#578b9c')
# Consolidate near-identical shades while retaining the neon accents.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(128) for x in range(128))
pal={p['index']:p['rgba'][:3] for p in c.palette()}
remap={i:i for i in counts}
while len(counts)>84:
 ids=list(counts)
 best=None
 for a in ids:
  for b in ids:
   if a>=b:continue
   distance=sum((pal[a][k]-pal[b][k])**2 for k in range(3))
   score=distance*min(counts[a],counts[b])**0.35
   if best is None or score<best[0]:best=(score,a,b)
 _,a,b=best
 if counts[a]>counts[b]:a,b=b,a
 for key in remap:
  if remap[key]==a:remap[key]=b
 counts[b]+=counts.pop(a)
for y in range(128):
 for x in range(128):c.set(x,y,remap[c.get(x,y)])
view(c)
print(c.stats())
save('cyberpunk-alley',c)
finish(result)
