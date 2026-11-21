import random
random.seed(8)
c=new_canvas(128,128,'#080d20',name='rain alley')
# restrained nocturnal palette
ink='#070b19'; wall='#15172c'; edge='#292440'; blue='#17344b'; cyan='#59e8eb'; pink='#fa479e'; gold='#ffbe78'
c.rect(39,0,53,80,'#111c32')
c.rect(51,19,24,58,'#172b40')
c.rect(56,30,14,48,'#20384b')
# remote windows
for x,y in [(44,8),(44,19),(78,11),(78,28),(53,23),(63,15)]:
 c.rect(x,y,3,5,'#32516a')
c.rect(59,54,7,24,'#367181');c.rect(61,57,2,18,'#75b7bc')
# buildings left and right converge
c.poly([(0,0),(36,0),(43,82),(0,106)],wall)
c.poly([(91,0),(127,0),(127,109),(82,81)],'#111223')
c.poly([(0,0),(10,0),(10,96),(0,103)],'#202038')
c.line(35,0,43,81,'#36304b');c.line(91,0,82,81,'#284457')
# architectural seams and brick hints
for y in range(12,90,10):
 c.line(11,y,35,y+3,'#232039')
for y in range(9,92,9):
 c.line(95,y,127,y-2,'#20243a')
for i in range(45):
 x=random.randrange(0,35);y=random.randrange(8,90)
 c.line(x,y,min(x+random.randrange(2,6),35),y,'#29223c')
# left shutter and door
c.poly([(12,46),(31,48),(33,87),(12,98)],ink)
for y in range(51,91,4): c.line(14,y,30,y-1,'#343049')
c.line(12,46,12,97,'#66324e');c.line(14,49,30,50,'#ba477a')
c.rect(36,49,5,29,'#0b1222');c.line(37,53,38,73,'#2c6070')
# pipes
c.line(6,8,6,88,'#414154');c.line(7,8,7,86,'#202b3c')
for y in [28,59,80]:c.rect(5,y,4,2,'#565166')
c.line(119,17,119,49,'#334454');c.line(119,49,126,49,'#334454')
# ground
c.poly([(43,79),(82,79),(127,107),(127,127),(0,127),(0,105)],'#111c30')
c.poly([(53,80),(69,80),(90,127),(24,127)],'#192b40')
c.line(43,81,0,111,'#384055');c.line(83,82,127,113,'#29445a')
# perspective pavement seams
for yy in [88,98,113,125]: c.line(0,yy,127,yy+3,'#101628')
c.line(57,83,39,127,'#101729');c.line(76,84,107,127,'#101729')
# reflection pools, broken horizontal pixel clusters
for i in range(190):
 y=random.randrange(84,128);x=random.randrange(5,124)
 col=random.choice(['#243d53','#234d62','#20566b','#30334e'])
 if x<47: col=random.choice(['#412840','#6d305c','#a43975','#da498b','#343049'])
 if 77<x<113: col=random.choice(['#18506a','#257c8b','#3babb4','#66d7d2','#263952'])
 c.line(x,y,min(127,x+random.randrange(1,8)),y,col)
# shop canopy left
c.poly([(0,37),(30,40),(37,49),(0,47)],'#592943')
c.line(0,46,36,49,pink)
c.line(0,48,32,51,'#882f64')
# neon sign front left
c.rect(1,23,31,16,'#441d3c');c.rect(2,24,29,14,pink);c.rect(3,25,27,12,'#1b142d')
c.text(4,28,'NOODL', '#ff94ca',spacing=0)
c.line(5,37,27,37,'#932a66')
# vertical neon blade
c.rect(34,17,12,30,'#091426');c.rect(35,18,10,28,'#1b5c6a');c.rect(36,19,8,26,'#123445')
for y in [22,30,38]:
 c.line(38,y,42,y,cyan);c.line(40,y-1,40,y+5,cyan);c.line(38,y+3,42,y+3,cyan)
c.line(45,20,45,45,'#56b5c3')
# right shop awning
c.poly([(89,33),(127,26),(127,39),(87,43)],'#203e4c');c.line(88,43,127,39,cyan)
c.rect(99,14,27,13,'#153642');c.rect(100,15,25,11,'#32737d');c.rect(101,16,23,9,'#102432')
c.text(101,17,'24H',cyan)
# shop glazing
c.poly([(94,47),(127,43),(127,85),(91,77)],'#09212e')
for x in [95,109,124]:c.line(x,46,x,81,'#285163')
c.line(97,49,120,46,'#367b88')
# vending machines distinct compact boxes
for x,y,w,h in [(99,58,17,35),(117,56,11,39)]:
 c.rect(x-1,y-1,w+2,h+2,ink);c.rect(x,y,w,h,'#28515d');c.rect(x+1,y+1,w-2,h-2,'#183749')
 c.rect(x+2,y+3,w-5,17,'#64d9d5');c.rect(x+3,y+4,w-7,15,'#173d50')
 for yy in range(y+6,y+18,5):
  for xx in range(x+3,x+w-5,4):
   c.rect(xx,yy,2,3,random.choice(['#ffbe78','#fa479e','#59e8eb']))
  c.line(x+3,yy+3,x+w-5,yy+3,'#498fa0')
 c.rect(x+w-3,y+8,1,6,pink);c.rect(x+3,y+24,w-7,5,ink);c.line(x+3,y+24,x+w-5,y+24,'#387984')
 c.line(x+1,y+1,x+1,y+h-2,'#58a7af')
# cables suspended above alley
for d in ['M 0 6 Q 56 37 127 8','M 0 12 Q 57 39 127 17','M 25 0 Q 42 25 93 29','M 71 0 Q 68 31 127 35']:
 c.path(d,ink,fill=False)
c.path('M 0 5 Q 56 36 127 7','#3a3d51',fill=False)
c.line(73,23,73,33,ink);c.rect(70,32,7,3,'#3c374c');c.rect(71,35,5,2,gold)
# bins and clutter
c.poly([(3,92),(13,89),(22,94),(21,107),(5,111)],'#101524');c.line(4,93,19,96,'#4a344d');c.line(9,96,10,106,'#2e2a40')
c.rect(26,91,6,8,'#332538');c.line(26,91,31,91,'#83516a')
# rain behind umbrella
for i in range(100):
 x=random.randrange(128);y=random.randrange(128)
 c.line(x,y,max(0,x-1),min(127,y+3),random.choice(['#315367','#294056','#38536b']))
# person's reflection
for y,w in [(112,8),(115,7),(118,9),(121,5),(124,7)]:
 c.line(65-w//2,y,65+w//2,y,ink)
# person coat and legs: lone silhouette
c.poly([(61,86),(68,85),(72,93),(71,104),(59,104),(59,94)],'#070c1a')
c.poly([(61,89),(64,90),(62,102),(59,103)],'#263148')
c.line(60,92,58,98,'#536072')
c.poly([(60,102),(64,102),(63,112),(59,113)],'#080b19')
c.poly([(66,102),(70,102),(71,112),(67,112)],'#080b19')
c.line(59,113,63,113,'#66848b');c.line(68,112,72,112,'#426372')
c.ellipse(65,83,3,4,'#080b19');c.line(63,80,66,79,'#6d7686')
# gripping arm and umbrella shaft
c.line(70,78,70,96,'#a1bdc6');c.line(70,96,68,97,'#a1bdc6')
c.line(68,90,71,93,'#29374a');c.set(71,92,'#dda6ad')
# transparent umbrella: muted view of structures beneath glass, outlined ribs
c.path('M 47 80 Q 50 67 65 65 Q 80 65 85 80 Q 79 77 75 81 Q 70 77 65 81 Q 59 77 55 81 Q 51 78 47 80 Z','#29485f')
c.path('M 49 77 Q 54 68 65 67 Q 76 67 82 77 L 76 76 L 71 73 L 60 73 L 54 77 Z','#35556c')
# fragments visible through canopy
c.line(56,73,56,77,'#416577');c.line(78,75,79,77,'#3e7181')
c.path('M 47 80 Q 50 67 65 65 Q 80 65 85 80','#9bcbd7',fill=False)
c.path('M 55 80 Q 56 70 65 65 Q 74 70 75 80','#6e9ead',fill=False)
c.line(65,66,65,79,'#87adbd')
c.path('M 47 80 Q 51 77 55 81 Q 59 77 65 81 Q 70 77 75 81 Q 79 77 85 80','#73a2b5',fill=False)
c.line(65,63,65,65,'#c2e8e7');c.line(49,76,53,71,'#f59cc6');c.line(79,72,82,76,cyan)
# bright rain and surface ripples
for x,y in [(8,17),(23,60),(48,50),(73,44),(90,91),(113,104),(33,113),(51,99),(86,11),(14,116),(93,55)]: c.line(x,y,x-1,y+3,'#7b9aa9')
for x,y in [(48,117),(84,111),(28,105),(106,119),(78,94)]:
 c.line(x-3,y,x-1,y,'#5b889a');c.line(x+2,y,x+4,y,'#5b889a');c.line(x-1,y+1,x+2,y+1,'#294b65')
# Consolidate near-identical shades to a compact palette.
from collections import Counter
w,h,data=c.to_rgba()
pixels=[tuple(data[i:i+4]) for i in range(0,len(data),4)]
counts=Counter(pixels)
remap={p:p for p in counts}
while len(counts)>86:
 a,b=min(((a,b) for a in counts for b in counts if a<b),key=lambda ab:sum((ab[0][k]-ab[1][k])**2 for k in range(3)))
 if counts[a]>counts[b]: a,b=b,a
 for p in remap:
  if remap[p]==a: remap[p]=b
 counts[b]+=counts.pop(a)
for i,p in enumerate(pixels):
 if remap[p]!=p:c.set(i%w,i//w,remap[p])
view(c)
finish(c)
