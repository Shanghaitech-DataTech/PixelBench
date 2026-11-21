c = new_canvas(64,64, '#111c32', name='Rainy corner store')
# restricted night / amber palette
ink='#0b1427'; dark='#18243b'; wall='#34485a'; edge='#547082'; teal='#315b6c'; rain='#52798d'; light='#ffe8a0'; gold='#edb865'; orange='#b77449'
# distant buildings
c.rect(0,8,11,34,'#1b2a40'); c.rect(3,5,7,37,'#1b2a40')
c.rect(54,3,10,40,'#19273e'); c.rect(58,0,6,6,'#19273e')
for x,y in [(3,13),(7,24),(57,10),(61,23),(1,33)]:
 c.rect(x,y,2,3,'#34495a')
c.rect(0,42,64,22,'#203449')
c.line(0,46,63,46,'#385467')
# store side wall and roof silhouette
c.poly([(6,18),(13,13),(56,13),(60,19),(60,44),(55,47),(6,45)],ink)
c.rect(7,19,49,25,wall)
c.poly([(56,18),(60,20),(60,43),(56,46)],'#26394d')
c.line(59,23,59,42,'#3b5262')
# raised roof and light sign, no logos
c.rect(8,13,49,7,ink)
c.rect(9,14,47,5,'#456575')
c.rect(10,14,45,1,'#769092')
c.rect(11,15,43,3,'#f0d187')
# little generic sign lettering
c.text(16,15,'OPEN', '#795349',spacing=1) if False else None
# minimal shop sign: horizontal luminous panel and tile accents
c.rect(12,15,3,3,'#cc8255'); c.rect(50,15,3,3,'#cc8255')
c.line(20,16,44,16,'#fff0b5')
# awning
c.poly([(8,19),(56,19),(59,23),(5,23)],'#527c82')
for x in range(9,56,8):
 c.poly([(x,19),(x+3,19),(x+5,23),(x+1,23)],'#8ba49a')
c.rect(5,23,54,2,'#203b4d'); c.line(6,23,58,23,'#699799')
# window frames / glowing panes
c.rect(9,25,46,17,ink)
c.rect(10,26,28,14,gold)
c.rect(11,26,26,3,light)
c.rect(10,29,28,11,'#e8bf76')
# interior ceiling lamps
c.rect(13,26,8,1,'#fff4cb'); c.rect(27,26,8,1,'#fff4cb')
# shelves and products
for yy in [32,37]:
 c.rect(11,yy,26,1,'#956649')
 c.rect(12,yy+1,24,1,'#f5d88b')
for x,col,h in [(12,'#74978a',3),(15,'#bd6e48',2),(18,'#7e8568',3),(22,'#a86b52',2),(26,'#709786',3),(30,'#cb8154',2),(34,'#8d785b',3)]:
 c.rect(x,32-h,2,h,col)
for x,col in [(12,'#b6754c'),(16,'#628b82'),(20,'#bd794e'),(25,'#719080'),(29,'#a27356'),(33,'#5d867f')]:
 c.rect(x,35,2,2,col); c.set(x,35,'#fff0b1')
# mullions and glass reflection
c.rect(23,26,2,14,'#3b535b')
c.line(10,26,10,39,'#fff0b3')
c.line(12,38,19,31,'#f5d996'); c.line(29,34,35,28,'#f5d996')
c.rect(9,40,30,3,'#4a6167'); c.line(9,40,38,40,'#93a7a0')
# doorway, open door angled outward
c.rect(40,25,14,18,'#192c39')
c.rect(41,26,11,15,'#ffe6a0')
c.rect(42,28,7,12,'#c58f5b'); c.rect(43,29,5,10,'#dfb370')
c.poly([(51,25),(56,28),(56,44),(51,41)],'#71908b')
c.poly([(52,27),(55,29),(55,41),(52,39)],'#b2ba94')
c.line(53,30,54,31,'#eddda4'); c.rect(52,35,1,3,'#4d676c')
c.rect(39,42,17,2,'#94a095'); c.rect(38,44,19,2,'#4b6169')
# sidewalk slabs
c.line(0,48,63,48,'#11263a'); c.line(27,45,25,48,'#263e50'); c.line(61,45,63,47,'#263e50')
# pavement reflected light, broken horizontal clusters
c.poly([(11,49),(31,49),(38,60),(6,60)],'#304f59')
c.poly([(40,47),(54,47),(59,58),(35,58)],'#3e5c60')
for x,y,w,col in [(10,50,19,'#8c8c68'),(14,51,12,'#b2a779'),(8,53,11,'#6d8271'),(21,53,9,'#c3a472'),(13,55,19,'#82947e'),(9,57,10,'#b0a37b'),(22,58,13,'#576e69'),(39,49,15,'#b3a77d'),(42,50,10,'#ddbd7f'),(38,52,18,'#7d8c72'),(42,54,10,'#c5ab74'),(36,56,9,'#687e73'),(48,57,11,'#9e9971'),(3,61,18,'#426577'),(34,62,19,'#3d6174'),(54,60,8,'#4e7280')]:
 c.rect(x,y,w,1,col)
# umbrella stand on left of entrance
c.rect(31,41,7,6,ink); c.rect(32,42,5,4,'#657b7e'); c.line(32,46,37,46,'#a5b2a1')
c.line(33,36,33,44,'#263a50'); c.line(36,35,36,44,'#263a50')
c.path('M 33 37 V 35 Q 33 33 31 34', '#b8c6b3',fill=False)
c.path('M 36 36 V 33 Q 36 32 38 33', '#e2c18c',fill=False)
c.poly([(32,37),(34,38),(34,43),(32,43)],'#b46f67')
c.poly([(35,36),(37,37),(37,43),(35,43)],'#517e89')
# parked bicycle silhouette wheels
for x in [10,24]:
 c.circle(x,46,5,ink); c.circle(x,46,4,'#688998',fill=False)
 c.line(x-2,48,x+2,44,'#3e5b70'); c.set(x,46,'#b0c6c1')
# frame triangular turquoise tubes
c.line(10,46,15,40,'#80b2ae'); c.line(15,40,18,46,'#71a6a6')
c.line(10,46,18,46,'#71a6a6'); c.line(18,46,22,40,'#71a6a6'); c.line(15,40,22,40,'#71a6a6')
c.line(21,38,24,46,'#b2c6bc'); c.line(21,38,24,37,'#b2c6bc')
c.line(15,40,14,38,ink); c.line(12,38,16,38,ink)
c.circle(18,46,1,'#c0c8ac'); c.line(18,46,20,48,'#87a4a8'); c.line(20,48,22,48,ink)
c.rect(23,38,5,3,'#4e6873'); c.line(23,38,27,38,'#8fa9aa')
# raincoated person entering, dark outline and boots
c.rect(44,39,3,7,ink); c.rect(48,39,3,5,ink)
c.rect(44,44,4,2,'#162535'); c.rect(48,42,4,2,'#162535')
c.poly([(43,33),(49,32),(51,36),(50,41),(42,41),(42,36)],'#80543d')
c.poly([(44,33),(48,33),(50,36),(49,40),(43,40),(43,36)],'#e7ae50')
c.line(44,35,43,39,'#ffcf69'); c.line(47,36,47,39,'#c48c3f')
# arm reaching into door
c.line(49,35,51,36,'#f4c367'); c.set(52,35,'#f8d3a0')
# hood profile
c.poly([(44,28),(47,27),(50,29),(50,32),(48,34),(43,33),(42,31)],'#8e603d')
c.poly([(44,29),(47,28),(49,29),(49,32),(47,33),(43,32),(43,30)],'#f6c565')
c.rect(48,30,2,2,'#c78d68'); c.set(49,30,'#3c3b3b'); c.line(44,29,46,29,'#ffe298')
# rain streaks in open sky and at edges, short and sparse
for x,y,n in [(2,1,3),(15,2,3),(28,0,3),(40,5,3),(52,1,3),(61,5,3),(7,8,3),(22,7,2),(34,8,2),(48,8,3),(1,19,3),(3,29,3),(62,28,3),(61,37,3),(2,40,2),(5,53,2),(30,49,2),(60,51,3),(27,59,2),(17,61,2)]:
 c.line(x,y,x-1,y+n,rain)
# small puddle ripples
for x,y in [(4,57),(30,54),(59,46),(35,60)]:
 c.line(x-2,y,x+2,y,'#648698'); c.set(x-3,y-1,'#385a71'); c.set(x+3,y-1,'#385a71')
c.set(7,24,'#b8d5c4'); c.line(57,25,57,27,'#8baaaa')
# Consolidate near-identical shades into a compact final palette.
from collections import Counter
pixels = [[c.get(x,y) for x in range(64)] for y in range(64)]
counts = Counter(v for row in pixels for v in row)
rgb = {p['index']: p['rgba'][:3] for p in c.palette()}
remap = {v:v for v in counts}
while len(counts) > 80:
 best = None
 for a in counts:
  for b in counts:
   if a == b: continue
   distance = sum((rgb[a][i]-rgb[b][i])**2 for i in range(3))
   cost = distance * counts[a]
   if best is None or cost < best[0]: best = (cost,a,b)
 _,a,b = best
 for k in remap:
  if remap[k] == a: remap[k] = b
 counts[b] += counts.pop(a)
for y in range(64):
 for x in range(64): c.set(x,y,remap[pixels[y][x]])
view(c)
finish(c)
