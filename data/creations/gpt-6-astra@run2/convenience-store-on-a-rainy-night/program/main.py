result = new_canvas(64,64, '#101b30', name='rainy_corner_store')
c=result
# Limited cool night / warm shop palette
ink='#101b30'; deep='#16253c'; wall='#294258'; edge='#426279'; blue='#66889a'
c.rect(0,18,64,29,deep)
# neighboring silhouettes
c.rect(0,8,9,36,'#192a40'); c.rect(2,12,4,8,'#263c52'); c.rect(58,4,6,41,'#1b2c42')
c.rect(60,10,2,7,'#34475a')
# wet street
c.rect(0,44,64,20,'#23374c')
c.poly([(0,49),(43,44),(63,47),(63,63),(0,63)],'#293f53')
c.line(0,48,63,48,'#455b6a');c.line(0,49,63,49,'#172b40')
# building mass, side wall and cornice
c.rect(10,13,47,33,ink)
c.rect(12,16,43,28,wall)
c.rect(54,18,3,27,'#20374d')
c.rect(9,12,48,3,'#405970'); c.line(11,12,55,12,'#66808e')
# illuminated anonymous sign
c.rect(13,15,40,6,'#d2a55f');c.rect(14,16,38,4,'#ffe6a1')
# small abstract sign decorations; no logos
c.rect(21,17,16,1,'#bc7951');c.rect(24,19,10,1,'#bc7951')
c.rect(16,17,2,2,'#ebbb72'); c.rect(47,17,2,2,'#ebbb72')
# teal awning
c.poly([(11,21),(54,21),(57,25),(9,25)],'#497b82')
for x in range(12,54,6): c.poly([(x,21),(x+2,21),(x+3,25),(x,25)],'#77a09c')
c.rect(9,25,48,2,'#21485a'); c.line(10,25,55,25,'#8cbbb0')
# panes and entrance
c.rect(13,28,27,14,ink);c.rect(14,28,25,12,'#f2c47e')
c.rect(41,27,12,18,ink);c.rect(42,28,10,15,'#db9c5d')
c.rect(43,29,8,13,'#f8d38b')
# interior ceiling light and bands of shelves
c.rect(15,29,23,2,'#fff1b3')
c.rect(15,32,23,1,'#c9965b')
for x,col,h in [(16,'#b96e54',3),(19,'#719381',2),(22,'#cb8256',3),(26,'#828f73',2),(29,'#b55f4e',3),(33,'#698d86',3),(36,'#cc9157',2)]:
 c.rect(x,35-h,2,h,col); c.set(x,35-h,'#ffe3a0')
c.rect(14,35,25,1,'#8e694f');c.line(15,36,38,36,'#ffdf96')
for x,col in [(16,'#728879'),(20,'#b27655'),(24,'#c58d5b'),(28,'#8c9b7f'),(34,'#af7051')]: c.rect(x,37,3,3,col)
# window frame and glass glints
c.rect(25,28,1,13,'#426275');c.rect(13,41,27,2,'#62818a')
c.line(16,30,16,32,'#fff5c9');c.line(17,29,19,29,'#fff5c9')
c.line(31,30,29,32,'#ffe7a8');c.line(37,37,35,39,'#e7d5a0')
c.rect(42,28,1,15,'#708a8a');c.rect(51,28,1,15,'#738383');c.set(50,36,'#fff0b1')
c.rect(41,44,13,2,'#8b8d7b');c.line(42,44,52,44,'#e3c28b')
# curb and reflected shop glow in broken puddles
c.poly([(18,48),(37,47),(42,50),(37,52),(16,53),(11,51)],'#536568')
c.line(15,50,35,50,'#ab926d');c.line(19,51,38,51,'#7d8574')
c.line(22,53,33,53,'#c2a278');c.line(14,55,29,55,'#586f78')
c.line(25,57,39,57,'#7d8b80');c.line(27,58,34,58,'#bd9b6e')
c.line(42,48,52,48,'#aa926c');c.line(43,50,50,50,'#dfb976');c.line(40,52,51,52,'#9d8b70')
c.line(44,54,53,54,'#6a7978');c.line(43,56,49,56,'#b29a73')
c.line(3,59,16,59,'#4c6a7c');c.line(5,60,11,60,'#6a8692');c.line(53,60,62,60,'#526e7f')
# umbrella rack on right of entrance: curved handles and folded canopies
c.line(56,34,56,43,'#a5b3ad');c.line(56,33,58,33,'#a5b3ad');c.set(58,34,'#a5b3ad')
c.poly([(55,36),(57,36),(58,41),(54,41)],'#77909d')
c.line(60,35,60,43,'#bfa993');c.set(61,35,'#bfa993');c.set(61,36,'#bfa993')
c.poly([(59,38),(61,38),(62,42),(58,42)],'#af7066')
c.rect(54,41,8,5,'#162c3e');c.line(54,41,61,41,'#7d98a0');c.line(55,44,60,44,'#446174');c.set(55,46,'#91a3a4');c.set(60,46,'#91a3a4')
# bicycle silhouette, two wheels and angular frame
for x in (7,23):
 c.circle(x,46,5,ink,False);c.circle(x,46,4,'#698798',False)
 c.line(x-2,44,x+2,48,'#3e596e');c.line(x-2,48,x+2,44,'#3e596e');c.set(x,46,'#b0bcb8')
c.line(7,46,12,39,'#a1b1ad');c.line(12,39,16,46,'#bd8a72');c.line(7,46,16,46,'#bd8a72')
c.line(12,40,21,40,'#caa088');c.line(16,46,21,40,'#bd8a72');c.line(21,38,23,46,'#9bb0ae')
c.line(20,37,21,39,'#acbdb8');c.line(20,37,23,37,'#acbdb8');c.set(24,38,ink)
c.line(12,39,11,37,'#8b9e9e');c.rect(9,37,5,1,ink);c.line(16,46,18,48,'#b2b4a5');c.line(17,48,19,48,ink)
# raincoated customer stepping into the light
c.poly([(42,30),(46,29),(49,32),(48,35),(50,38),(50,43),(40,44),(41,35),(40,33)],'#765f4b')
c.line(44,42,43,47,ink);c.line(47,42,48,45,ink);c.line(42,47,44,47,'#99a9a4');c.line(48,45,50,45,'#99a9a4')
c.poly([(43,33),(47,33),(49,42),(41,43),(42,37)],'#c38a3c')
c.poly([(43,34),(46,34),(47,41),(42,41)],'#efbd56');c.line(43,35,42,39,'#ffe086')
c.poly([(47,35),(48,36),(50,35),(50,37),(47,39)],'#e7ad47');c.set(50,35,'#f9d396')
c.poly([(43,30),(46,30),(48,32),(48,34),(43,35),(41,33)],'#eec05a')
c.rect(45,31,2,3,'#765f4b');c.set(47,32,'#f3cf91');c.line(43,30,45,30,'#ffe59b');c.line(42,31,42,33,'#ffe086')
# selective rain streaks foreground and sky
for x,y,l in [(3,2,3),(16,2,4),(28,6,3),(40,1,4),(52,6,3),(61,1,2),(7,17,3),(2,28,3),(60,23,3),(5,35,2),(31,0,2),(46,9,2),(19,8,2),(1,51,3),(33,44,3),(59,52,3),(19,59,3),(38,59,3)]:
 c.line(x,y,x-1,y+l,'#557387')
# short ripple arcs
c.line(31,60,36,60,'#526e7d');c.set(30,59,'#526e7d');c.set(37,59,'#526e7d')
c.line(54,55,58,55,'#7d9298');c.set(53,54,'#526e7d')
c.set(12,54,'#b4b8a3');c.set(40,49,'#d4ba86')
# Consolidate near-identical shades into a compact final palette.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(64) for x in range(64))
rgba={p['index']:p['rgba'] for p in c.palette()}
remap={i:i for i in counts}
while len(counts)>82:
 ids=list(counts)
 a,b=min(((a,b) for j,a in enumerate(ids) for b in ids[j+1:]), key=lambda ab: sum((rgba[ab[0]][k]-rgba[ab[1]][k])**2 for k in range(3)))
 if counts[a]>counts[b]: a,b=b,a
 for i in remap:
  if remap[i]==a: remap[i]=b
 counts[b]+=counts.pop(a)
for y in range(64):
 for x in range(64):
  old=c.get(x,y)
  if remap[old]!=old: c.set(x,y,remap[old])
view(c)
finish(result)
