import random
random.seed(11)
result=new_canvas(128,128,'#080d20',name='cyberpunk-alley')
c=result
# palette
ink='#080d20'; dark='#10172b'; wall='#182238'; edge='#28354b'; teal='#167183'; cyan='#55e5df'; pale='#b0fff1'; pink='#fa459d'; rose='#862d70'; gold='#ffce79'
# far sky and tower blocks
c.rect(42,0,46,83,'#111b35')
c.rect(49,5,13,67,'#1b2943'); c.rect(68,0,19,79,'#15243c')
for x,y in [(53,12),(57,24),(72,8),(77,8),(72,30),(80,45),(52,47),(58,59)]:
 c.rect(x,y,2,4,'#346176')
c.rect(61,38,9,46,'#233850');c.rect(64,43,2,23,'#498197')
# distant bright alley
c.poly([(61,67),(75,62),(81,90),(53,90)],'#205666')
c.rect(66,70,6,16,'#469b9a');c.rect(68,73,2,12,'#89d8c6')
# road
c.poly([(51,80),(81,80),(128,128),(0,128)],'#101c30')
c.poly([(66,83),(76,83),(104,128),(35,128)],'#173342')
# side buildings
c.poly([(0,0),(36,0),(47,18),(47,84),(0,113)],'#182139')
c.poly([(0,0),(21,0),(25,99),(0,113)],'#20283d')
c.poly([(36,0),(48,14),(48,85),(38,91)],'#111a2c')
c.poly([(89,0),(128,0),(128,114),(81,85),(81,19)],'#14192b')
c.poly([(103,0),(128,0),(128,111),(103,97)],'#1d2134')
# facades and pipes
c.line(34,0,34,91,'#30405a');c.line(36,2,36,91,'#090e21')
c.line(4,4,4,106,'#3c4153');c.line(6,4,6,105,ink)
c.line(95,0,95,89,'#343449');c.line(97,0,97,91,ink)
for y in [20,40,60,81]:
 c.line(0,y,24,y+4,'#2c3549')
for y in [10,30,50]:
 c.rect(8,y,16,12,ink);c.rect(10,y+2,12,2,'#343b52');c.line(15,y+2,15,y+10,'#293248')
c.rect(104,8,18,17,ink)
for y in range(10,24,3): c.line(106,y,120,y,'#32364b')
c.rect(109,35,19,11,'#0b1123');c.line(109,36,127,36,rose)
# rear door
c.rect(38,55,8,31,ink);c.rect(40,59,5,23,'#20384a');c.line(44,61,44,77,'#3a6470')
# left glowing storefront
c.rect(6,54,25,42,'#101224')
c.rect(8,57,20,24,'#155667');c.rect(10,59,16,20,'#298e92')
c.rect(12,61,6,17,'#286376');c.rect(20,61,4,17,'#163e54')
c.line(18,58,18,81,ink);c.line(7,82,29,82,cyan)
c.rect(8,85,21,9,'#172b3e');c.line(9,86,28,86,'#327482')
# awning
c.poly([(4,51),(30,51),(34,56),(2,56)],'#263d51');c.line(4,51,30,51,cyan)
for x in range(5,31,5): c.line(x,52,x-2,55,'#416272')
# main neon sign
c.rect(5,38,27,12,ink);c.rect(6,39,25,10,rose);c.rect(7,40,23,8,'#301e3a')
c.text(8,41,'NOOD',pink,spacing=0)
c.line(7,49,30,49,'#ff8fca')
# vertical right sign
c.rect(84,17,12,37,'#090e20');c.rect(85,18,10,35,teal);c.rect(86,19,8,33,'#14283e')
for yy in [21,31,41]:
 c.line(88,yy,92,yy,cyan);c.line(90,yy-1,90,yy+6,cyan);c.line(88,yy+3,92,yy+3,pale);c.line(88,yy+6,92,yy+6,cyan)
c.line(85,19,85,51,pale)
c.line(94,54,94,65,'#32747b')
# far sign
c.rect(50,46,9,13,'#572744');c.rect(51,47,7,11,'#ce4975');c.line(53,49,56,49,gold);c.line(54,49,54,55,gold)
# two vending machines
for x,y,w,h,col in [(100,62,16,35,cyan),(117,67,11,36,pink)]:
 c.rect(x-1,y-1,w+2,h+2,ink);c.rect(x,y,w,h,'#314255' if x==100 else '#422a45')
 c.line(x,y,x+w-1,y,col);c.line(x,y+1,x,y+h-1,'#4d7782')
 c.rect(x+2,y+3,w-4,7,col);c.rect(x+3,y+4,w-6,5,'#d7ffe9' if x==100 else '#ff9ac6')
 c.rect(x+2,y+12,w-6,13,'#0c1d31')
 for yy in [y+14,y+20]:
  for xx in range(x+3,x+w-5,4):
   c.rect(xx,yy,2,3,'#58b8b9' if yy==y+14 else '#e8aa87')
  c.line(x+2,yy+4,x+w-5,yy+4,'#536078')
 c.rect(x+w-3,y+14,2,3,gold);c.rect(x+3,y+h-7,w-6,4,ink)
 c.line(x+3,y+h-7,x+w-4,y+h-7,'#567b86')
# cables sag across overhead
for d in ['M 0 9 Q 49 34 104 5','M 18 0 Q 61 40 127 22','M 0 23 Q 60 44 128 29','M 39 0 Q 56 17 89 9']:
 c.path(d,ink,fill=False)
c.path('M 0 8 Q 49 32 104 4','#3a455b',fill=False)
c.line(64,29,64,35,ink);c.rect(62,35,5,2,'#677b81');c.rect(63,37,3,1,gold)
# pavement seams
c.line(0,114,52,84,'#314655');c.line(85,86,127,119,'#394152')
c.line(10,125,54,92,'#0a1426');c.line(85,97,107,126,'#0b182a')
# broken wet reflections
for i in range(150):
 y=random.randint(87,127)
 # reflected colored bands
 center=random.choice([19,27,62,91,107,121])
 x=center+random.randint(-8,8)
 if 0<=x<128:
  col=random.choice([teal,'#236378','#29435a','#2c4d61'])
  if center in [19,121]: col=random.choice([rose,'#b63a84','#503052'])
  if center==62: col=random.choice(['#386f79','#4a9895','#285664'])
  c.rect(x,y,min(random.randint(2,10),128-x),1,col)
for x,y,w,col in [(8,107,15,cyan),(15,112,12,'#3eb8bf'),(5,119,17,pink),(14,122,7,'#f47ab6'),(98,106,13,cyan),(103,112,16,'#36a6b1'),(114,116,12,pink),(53,96,9,'#6abbb3'),(42,121,12,'#69a9a7')]: c.rect(x,y,w,1,col)
# crates
c.poly([(0,92),(10,89),(18,94),(8,99)],'#364454');c.poly([(0,93),(8,99),(8,109),(0,106)],'#182338');c.poly([(9,99),(18,95),(18,104),(9,109)],'#10192b');c.line(10,100,16,97,'#436373')
# rain, fine sparse streaks
for i in range(100):
 x=random.randrange(128);y=random.randrange(126)
 col=random.choice(['#2c4057','#35455d','#386475'])
 c.line(x,y,max(0,x-1),min(127,y+random.choice([1,2,3])),col)
# umbrella bearer's reflection
c.poly([(67,109),(76,109),(80,126),(63,126)],'#0b1929')
c.line(64,120,76,120,'#284655');c.line(64,125,80,125,'#1b3b4a')
# figure feet and coat silhouette
c.line(67,100,66,111,ink);c.line(68,101,68,110,ink);c.line(74,100,76,110,ink)
c.rect(64,110,5,2,ink);c.rect(75,109,5,2,ink)
c.poly([(66,84),(73,84),(77,91),(76,103),(63,103),(64,92)],'#090f21')
c.line(64,91,63,101,'#327081');c.line(65,102,72,102,'#234455')
c.poly([(74,87),(78,91),(81,87),(82,89),(78,95),(73,92)],'#10162a')
c.line(76,90,78,92,'#476a7b')
c.rect(67,78,6,7,'#111528');c.rect(72,79,2,4,'#bb8b90');c.line(67,78,71,77,'#385b6d')
c.rect(68,84,5,2,'#693655')
# umbrella pole and hooked handle
c.line(79,72,79,91,'#92acb6');c.line(79,91,81,92,'#92acb6');c.set(82,91,'#92acb6');c.rect(79,87,3,2,'#c29b9c')
# translucent canopy: restrained cool glass with background hints
c.poly([(53,76),(57,70),(64,66),(74,64),(84,66),(92,71),(96,77),(86,75),(77,77),(66,75)],'#294859')
c.poly([(58,72),(65,67),(74,65),(67,73)],'#3c6675')
c.poly([(75,65),(84,68),(90,73),(79,74)],'#355768')
# seen-through facade streaks
c.line(61,71,61,73,'#437783');c.line(86,70,86,73,'#40929c')
c.path('M 53 76 Q 60 64 74 64 Q 88 64 96 77','#89c8cf',fill=False)
c.path('M 53 76 Q 59 73 66 75 Q 71 74 77 77 Q 82 74 86 75 Q 92 74 96 77','#63a9b6',fill=False)
c.path('M 74 64 Q 67 68 66 75 M 74 64 Q 77 68 77 77 M 74 64 Q 84 68 86 75','#587f91',fill=False)
c.line(74,62,74,64,'#c5eeee');c.line(59,70,64,67,'#c0f3ec');c.set(93,75,'#e0fff3')
# rain beads on canopy and small road splashes
for x,y in [(60,71),(69,66),(80,67),(89,72)]: c.set(x,y,'#a3dadb')
for x,y in [(29,117),(87,121),(47,107),(94,99),(34,96)]:
 c.line(x,y,x+3,y,'#517b8a');c.set(x+1,y-1,'#517b8a')
# Consolidate the closest shades while retaining high-contrast accent colours.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(128) for x in range(128))
pal={p['index']:p['rgba'] for p in c.palette()}
remap={i:i for i in counts}
while len(counts)>86:
 ids=list(counts)
 a,b=min(((a,b) for j,a in enumerate(ids) for b in ids[j+1:]),key=lambda ab: sum((pal[ab[0]][k]-pal[ab[1]][k])**2 for k in range(3)))
 if counts[a]>counts[b]: a,b=b,a
 for i in remap:
  if remap[i]==a: remap[i]=b
 counts[b]+=counts.pop(a)
for y in range(128):
 for x in range(128):
  i=c.get(x,y)
  if remap[i]!=i: c.set(x,y,remap[i])
view(c)
finish(result)
