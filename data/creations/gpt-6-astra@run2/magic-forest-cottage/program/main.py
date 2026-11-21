import random
random.seed(18)
c = new_canvas(128,128, '#201a38', name='Moonwood cottage')
# compact twilight palette
sky='#201a38'; deep='#19192c'; ink='#201e2d'; bark='#302333'; wood='#583941'; woodlit='#805247'; mauve='#51405b'; mist='#625570'
# sky bands
c.rect(0,29,128,35,'#2b2344'); c.rect(0,64,128,35,'#352b4b')
# moon halo and luminous full disc
c.circle(91,23,18,'#302947'); c.circle(91,23,15,'#423750'); c.circle(91,23,12,'#c3b5be'); c.circle(91,22,11,'#f0dfc8')
c.poly([(84,14),(82,20),(83,25),(88,30),(94,31),(88,32),(81,27),(79,21),(81,16)],'#d5c3c2')
c.rect(95,17,3,2,'#e0ccc5');c.rect(97,22,2,3,'#e0ccc5');c.set(87,16,'#fff0d2')
for x,y in [(34,11),(51,18),(66,7),(112,34),(72,31),(44,32),(20,29),(104,9)]:
 c.set(x,y,'#a58aab')
c.line(57,28,57,32,'#b6a0b5');c.line(55,30,59,30,'#b6a0b5')
# distant forest spires
for x,y,w in [(3,24,6),(15,31,5),(27,16,4),(40,22,4),(56,8,4),(69,21,4),(108,22,5),(119,13,6)]:
 c.poly([(x-w,92),(x-2,y+21),(x,y),(x+2,y+24),(x+w,91)],'#30283f')
 c.line(x,y+32,x-7,y+20,'#30283f');c.line(x,y+24,x+8,y+12,'#30283f')
# layered mist across forest floor
c.poly([(0,70),(15,66),(34,70),(52,66),(71,70),(89,65),(109,67),(127,63),(127,87),(0,87)],'#443950')
c.poly([(0,78),(20,73),(43,76),(65,72),(85,75),(107,70),(127,73),(127,86),(0,88)],'#51465c')
for x,y,w in [(2,73,25),(76,70,29),(105,77,23),(8,82,29),(91,83,30)]: c.rect(x,y,w,1,'#70617b')
# earth
c.poly([(0,88),(19,85),(40,89),(59,84),(81,87),(101,84),(127,88),(127,128),(0,128)],'#282a38')
c.poly([(0,105),(27,94),(48,99),(67,94),(84,99),(106,89),(127,98),(127,128),(0,128)],'#34343f')
# distant bushes
for x,y,r in [(8,86,8),(20,85,6),(105,85,8),(120,87,10)]:
 c.circle(x,y,r,'#343741'); c.rect(x-3,y-5,5,2,'#49504b')
# cottage chimney behind roof
c.poly([(64,27),(73,29),(72,51),(64,47)],'#49414a')
c.rect(63,26,12,4,'#282734');c.rect(65,26,7,2,'#8a6c66')
c.rect(65,32,4,3,'#766069'); c.rect(69,38,3,3,'#756068');c.line(65,36,69,36,'#272735')
# drifting chimney smoke
c.path('M 68 24 Q 58 20 65 15 Q 71 11 66 7', '#68536c',False)
c.path('M 71 23 Q 63 20 69 15', '#483b53',False)
# cottage broad base shadow
c.ellipse(60,97,39,9,'#242532')
# walls: front gable left and side right
c.poly([(29,64),(49,42),(69,65),(69,96),(29,96)],'#6d5450')
c.poly([(69,63),(88,58),(88,91),(69,96)],'#463b40')
# stone lower foundation
c.rect(29,83,40,13,'#716665');c.poly([(69,84),(88,80),(88,92),(69,97)],'#514c54')
for x,y,w in [(30,84,7),(39,85,9),(50,84,8),(60,85,8),(31,90,9),(42,91,7),(58,91,10)]:
 c.rect(x,y,w,4,'#958079');c.line(x,y+4,x+w,y+4,'#48424b');c.set(x,y,'#b29a83')
for x,y in [(72,87),(80,85),(72,93),(82,91)]:c.rect(x,y,5,3,'#72636a')
# siding horizontal planks
for y in range(67,84,4):
 c.line(31,y,67,y,'#49363b');c.line(33,y+1,66,y+1,'#896052')
for y in range(65,81,4):c.line(71,y,86,y-3,'#312d36')
# roof silhouette, long sloped side plane
c.poly([(23,68),(47,32),(65,34),(93,61),(69,70),(48,44),(29,71)],'#191f2b')
c.poly([(48,34),(64,35),(90,59),(69,65)],'#344342')
c.poly([(26,65),(47,35),(49,41),(31,67)],'#54644c')
# roof rows, staggered mossy shingles following plane
for row in range(7):
 y=37+row*4
 left=51+row*3; right=65+row*3
 c.line(left,y,right,y,'#637058')
 c.line(left+2,y+2,right+2,y+2,'#26383b')
 for x in range(left+2,right+1,5):
  c.line(x,y,x+2,y+2,'#465648')
for x,y in [(49,36),(55,40),(62,42),(61,47),(69,49),(75,52),(73,57),(82,57),(67,53)]:
 c.rect(x,y,4,2,'#74805a');c.set(x,y-1,'#91956b')
c.line(48,33,64,34,'#8a9068');c.line(64,34,90,59,'#5b6853')
# layered roof edges, moss draping
c.line(23,68,47,32,'#a19b6e');c.line(24,69,48,35,'#58694d')
c.line(69,66,92,60,'#68734e');c.line(70,69,92,63,'#1e2830')
for x,y,h in [(73,66,4),(79,64,3),(85,63,5),(31,62,5),(37,53,4)]:
 c.line(x,y,x,y+h,'#67724e');c.set(x+1,y+1,'#89915c')
# front gable timber framing
c.line(30,67,48,42,'#352c32');c.line(48,42,68,68,'#302a31')
c.line(32,67,48,45,'#aa7557');c.line(48,45,66,67,'#986446')
c.rect(30,68,3,16,'#392e34'); c.rect(65,69,3,16,'#392e34');c.rect(47,47,3,15,'#493239')
# attic amber round window
c.circle(49,59,6,'#302a32');c.circle(49,59,4,'#d67a3f');c.circle(48,58,3,'#ffd28a')
c.line(49,55,49,63,'#6a4138');c.line(45,59,53,59,'#6a4138');c.line(44,65,54,65,'#b3835e')
# front lit square window
c.rect(35,70,16,14,'#342c32');c.rect(36,71,14,11,'#bc6037');c.rect(37,71,11,9,'#ffb65d');c.rect(38,72,9,4,'#ffe0a0')
c.rect(41,71,2,11,'#78503b');c.line(36,77,49,77,'#87543b');c.rect(34,83,18,2,'#b48864')
c.rect(33,72,2,9,'#765046');c.rect(51,72,2,10,'#3c3036')
# door
c.rect(55,73,9,22,'#2c2931');c.rect(56,74,6,19,'#65453f');c.line(58,76,58,92,'#88604b');c.line(61,75,61,93,'#402e35');c.set(61,85,'#ffca74')
c.rect(53,94,13,3,'#aa8d77');c.rect(51,98,17,2,'#69616a')
# side window
c.poly([(74,69),(83,67),(83,78),(74,80)],'#262630');c.poly([(75,70),(82,69),(82,77),(75,78)],'#f2a354')
c.line(78,70,78,78,'#80523d');c.line(75,74,82,73,'#80523d');c.line(73,81,84,78,'#89735a')
# amber light puddle
c.poly([(36,91),(48,91),(60,106),(26,109)],'#49403f')
# winding stone slabs toward foreground
stones=[(53,101,10,3),(50,105,12,4),(46,110,14,4),(39,116,18,5),(32,123,22,5)]
for x,y,w,h in stones:
 c.poly([(x+3,y),(x+w-2,y-1),(x+w,y+h-1),(x+1,y+h),(x-1,y+2)],'#222632')
 c.poly([(x+3,y),(x+w-3,y),(x+w-1,y+h-2),(x+1,y+h-1)],'#827577')
 c.line(x+3,y,x+w-3,y,'#b19a8a');c.set(x+4,y+2,'#a89180')
# well at right with rear rim and winch uprights
c.ellipse(95,108,18,5,'#242631')
c.rect(82,85,3,19,'#302b31');c.rect(84,85,1,19,'#a27a59')
c.rect(105,82,3,20,'#332c35');c.rect(105,83,1,18,'#986c51')
# well body
c.rect(81,99,28,10,'#5f5962');c.ellipse(95,108,14,5,'#5f5962')
for x,y,w in [(82,100,7),(91,101,7),(100,99,7),(85,106,8),(95,107,8),(104,104,4)]:
 c.rect(x,y,w,4,'#8b7a7a');c.line(x,y+4,x+w-1,y+4,'#3f3d4b');c.line(x,y,x+w-1,y,'#a49387')
c.ellipse(95,98,15,6,'#b0a090');c.ellipse(95,98,11,3,'#292b38');c.line(88,97,100,96,'#4c4a5b')
c.line(81,99,85,102,'#776c75');c.line(88,103,102,103,'#d0b799')
# wood crank crossbar
c.rect(81,85,28,4,'#362d34');c.line(82,85,108,85,'#b1875f');c.line(83,86,107,86,'#8d624c')
c.rect(91,84,7,6,'#6e4e43')
for x in [92,94,96]:c.line(x,84,x,89,'#c1a071')
c.line(94,90,94,98,'#b29770');c.line(110,86,113,86,'#aa8662');c.line(113,86,113,92,'#aa8662');c.rect(111,91,5,2,'#523b3c')
# giant framing tree trunks
c.poly([(0,18),(6,16),(10,46),(9,65),(15,87),(13,104),(23,113),(12,110),(6,103),(0,110)],'#211e2c')
c.poly([(2,25),(6,24),(7,51),(5,68),(11,90),(9,103),(16,109),(8,106),(3,91)],'#49303d')
c.path('M 6 64 Q 19 44 17 24 L 22 13 L 18 29 Q 22 46 10 69 Z','#302331')
c.path('M 4 43 Q 25 37 33 19 L 31 31 Q 22 43 6 49 Z','#352635')
c.line(5,67,8,86,'#714650');c.line(6,53,6,63,'#694151')
c.poly([(128,33),(121,33),(119,58),(121,77),(117,98),(109,116),(120,111),(127,118)],'#211f2c')
c.poly([(123,44),(125,46),(124,72),(125,89),(121,105),(115,112),(122,109),(127,105),(127,61)],'#4a303d')
c.path('M 123 65 Q 105 54 108 35 L 102 21 L 110 30 Q 111 49 123 54 Z','#2b2231')
c.path('M 121 46 Q 115 24 99 12 L 104 13 Q 120 23 127 40 Z','#322431')
c.line(121,79,119,97,'#754b51');c.line(124,51,124,69,'#68414c')
# clusters of wine-colored leaves, dark canopy silhouette
for x,y,r in [(0,9,19),(15,8,17),(29,4,15),(43,2,11),(4,29,11),(22,19,10),(117,6,21),(100,3,11),(126,25,12),(113,18,10)]:
 c.circle(x,y,r,'#2b2133')
 for i in range(18):
  dx=random.randint(-r,r);dy=random.randint(-r,r)
  if dx*dx+dy*dy<r*r and 0<=x+dx<125 and 0<=y+dy<126:
   col=random.choice(['#432737','#4f2c3e','#623544','#77404b','#3e2b40'])
   c.rect(x+dx,y+dy,random.randint(2,4),2,col)
# roots and forest ground foliage
for x,y in [(4,118),(18,101),(26,117),(69,111),(78,119),(110,120),(119,100),(4,96)]:
 c.line(x,y,x-3,y-5,'#53604f');c.line(x,y,x+3,y-7,'#667052');c.line(x,y,x,y-5,'#83805c')
for i in range(90):
 x=random.randrange(128); y=random.randrange(93,128)
 if (29<x<69 and y<101) or (78<x<111 and y<114) or (30<x<60 and y>103):continue
 c.rect(x,y,2,1,random.choice(['#55504e','#6d5056','#4c5149','#393c42']))
# foreground plants and tiny red mushrooms
for x,y in [(18,116),(22,119),(72,106),(115,115)]:
 c.rect(x,y-2,1,4,'#c2ac91');c.rect(x-2,y-4,5,2,'#9e5559');c.rect(x-1,y-5,3,1,'#c57c70');c.set(x-1,y-4,'#ecc49c')
# floating fireflies
for x,y in [(22,77),(75,84),(98,66),(16,94),(67,107)]:
 c.set(x-1,y,'#746b56');c.set(x,y,'#eace84');c.set(x,y-1,'#a5a36e')
# low wisps in the distance, broken soft lines
c.line(1,90,7,90,'#726579');c.line(16,89,24,89,'#726579');c.line(96,81,114,81,'#77667e')
# Hanging clusters give the ancient canopy a scalloped silhouette.
for x,y in [(9,30),(24,21),(35,12),(4,42),(111,26),(119,32),(97,9)]:
 for dx,dy,w in [(-3,-2,5),(0,0,6),(-2,2,4),(2,4,3)]:
  c.rect(x+dx,y+dy,w,2,'#4f2c3e')
 c.rect(x-2,y-2,3,1,'#77404b');c.rect(x+2,y,3,1,'#623544')
# Consolidate near-identical shades into a controlled pixel-art palette.
from collections import Counter
w,h,raw=c.to_rgba()
px=[tuple(raw[i:i+4]) for i in range(0,len(raw),4)]
counts=Counter(px)
groups=[{'rgb':p[:3], 'n':n, 'members':[p]} for p,n in counts.items()]
while len(groups)>82:
 best=None
 for i in range(len(groups)):
  a=groups[i]
  for j in range(i+1,len(groups)):
   b=groups[j]
   d=sum((a['rgb'][k]-b['rgb'][k])**2 for k in range(3))
   score=d*(a['n']*b['n'])/(a['n']+b['n'])
   if best is None or score<best[0]:best=(score,i,j)
 _,i,j=best
 a,b=groups[i],groups[j];n=a['n']+b['n']
 groups[i]={'rgb':tuple((a['rgb'][k]*a['n']+b['rgb'][k]*b['n'])/n for k in range(3)), 'n':n, 'members':a['members']+b['members']}
 groups.pop(j)
lookup={p:tuple(round(v) for v in g['rgb']) for g in groups for p in g['members']}
for y in range(h):
 for x in range(w):c.set(x,y,lookup[px[y*w+x]])
view(c)
save('moonwood_cottage',c)
finish(c)
