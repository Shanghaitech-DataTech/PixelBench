result = new_canvas(64,64,background='#253f49',name='university_lab')
c=result
# Restrained cool wall, tile joints, and warm wooden worktop.
c.rect(0,0,64,29,'#42636a')
c.rect(0,0,64,3,'#35555f')
c.line(0,15,63,15,'#395860')
for x in [5,31,57]: c.line(x,3,x,14,'#395860')
for x in [18,44]: c.line(x,16,x,28,'#395860')
c.rect(0,27,64,3,'#263f48')
c.line(0,27,63,27,'#6d8785')
c.poly([(0,30),(63,30),(63,55),(0,55)],'#ad8157')
c.line(0,30,63,30,'#d0a16b')
c.rect(0,55,64,5,'#715346')
c.rect(0,55,64,1,'#e1b57b')
c.rect(0,60,64,4,'#263e47')
c.line(0,59,63,59,'#423e3d')
c.rect(4,60,5,4,'#675448')
c.rect(55,60,5,4,'#675448')
# Quiet wood grain, interrupted by the instruments.
for x,y,w in [(1,35,7),(29,38,8),(1,48,8),(9,52,8),(47,33,10),(47,52,7),(3,32,9)]:
    c.line(x,y,x+w,y,'#986d4d')
c.line(2,57,61,57,'#8f684b')
# Contact shadows.
c.ellipse(17,43,14,3,'#805e49')
c.ellipse(47,36,13,2,'#805e49')
c.ellipse(33,35,6,2,'#805e49')
# Bottles behind the notebook: amber reagent with broad blank label.
c.rect(29,19,7,3,'#203943')
c.line(30,19,34,19,'#819795')
c.rect(30,22,5,3,'#9f663e')
c.poly([(30,24),(34,24),(37,27),(37,34),(28,34),(28,27)],'#4c4540')
c.poly([(30,25),(34,25),(36,27),(36,33),(29,33),(29,27)],'#b2763e')
c.line(30,26,30,32,'#d8a057')
c.rect(29,28,7,4,'#e6d7ac')
c.rect(31,29,3,1,'#73867b')
# Rack tubes: rounded bottoms, open rims, distinct fill heights.
for x,h,liquid in [(40,19,'#70c5bc'),(46,17,'#d88579'),(52,20,'#e9bb66')]:
    c.rect(x-1,h,5,14 if h==17 else 32-h,'#294c58')
    c.rect(x,h+1,3,31-h,'#83aeb2')
    c.rect(x+1,h+2,2,29-h,'#4e7985')
    c.rect(x,26 if h!=20 else 25,3,5 if h!=20 else 6,liquid)
    c.line(x,h+2,x,29,'#c0d9cc')
    c.line(x-1,h,x+3,h,'#d1e4d7')
    c.line(x,31,x+2,31,'#bdd9ce')
# Wooden test tube rack: top rail, open window, lower shelf, feet.
c.rect(37,25,20,3,'#684d40')
c.line(38,25,56,25,'#e5b77b')
c.line(38,27,56,27,'#a77349')
for x in [37,55]:
    c.rect(x,27,2,9,'#754d37')
    c.line(x,28,x,34,'#d49c61')
c.rect(36,33,23,3,'#9a6945')
c.line(37,33,57,33,'#ebbc7d')
c.rect(37,36,3,1,'#654b3d')
c.rect(55,36,3,1,'#654b3d')
# Microscope's swept supporting arm.
c.path('M 20 17 L 25 17 Q 31 19 30 28 L 28 37 L 24 40 L 19 39 L 23 33 L 25 25 Q 25 22 21 22 Z','#253d49')
c.path('M 22 18 L 25 19 Q 29 21 28 28 L 26 36 L 23 38 L 20 38 L 24 32 L 26 25 Q 26 21 22 21 Z','#a4bcb7')
c.path('M 23 19 Q 28 20 27 26 L 25 34 L 23 36 L 22 36 L 24 31 L 25 24 L 22 21 Z','#d4ded0')
# Foot and base.
c.poly([(9,38),(23,38),(28,41),(28,44),(5,44),(5,41)],'#263f49')
c.poly([(10,38),(22,38),(26,41),(26,42),(7,42),(7,41)],'#a0b8b4')
c.line(9,39,22,39,'#e2e5cf')
c.line(7,43,26,43,'#637f88')
# Illuminator below stage.
c.rect(13,33,7,5,'#304b57')
c.ellipse(16,34,4,2,'#92aaa8')
c.line(14,33,18,33,'#e6d496')
c.rect(15,36,3,2,'#65858b')
# Stage and slide.
c.poly([(10,27),(24,27),(23,30),(8,30),(8,28)],'#233b48')
c.line(10,27,23,27,'#658491')
c.line(9,30,22,30,'#142e3b')
c.line(12,26,20,26,'#c8e2d6')
c.line(14,27,19,27,'#69b9b8')
c.set(16,26,'#de9b7b')
# Angled optical body and black eyepiece.
c.poly([(12,12),(16,10),(23,19),(20,23),(16,20)],'#243e4b')
c.poly([(13,12),(16,12),(22,19),(19,21)],'#b2c6bd')
c.line(13,13,19,20,'#e1e5cf')
c.line(17,13,22,19,'#78999f')
c.poly([(10,9),(14,7),(17,11),(12,14)],'#1c3542')
c.line(10,9,14,7,'#8da8ac')
c.line(12,11,15,9,'#496875')
# Nosepiece and objectives.
c.poly([(18,21),(21,20),(24,23),(21,25),(17,24)],'#435f6a')
c.line(18,23,22,22,'#c7d5c8')
c.rect(18,24,2,2,'#d5c58b')
c.rect(22,24,2,3,'#a1b8b3')
c.set(22,27,'#263f49')
# Oversize coarse focus and smaller fine-focus cap.
c.circle(26,26,3,'#263f49')
c.circle(26,26,2,'#738e95')
c.set(25,25,'#d7dfca')
c.rect(26,26,2,2,'#3f606e')
# Open notebook with two trapezoid pages and a visible central fold.
c.poly([(24,44),(34,43),(39,44),(46,42),(50,52),(39,55),(26,55),(22,46)],'#6b5145')
c.poly([(23,43),(34,42),(38,44),(46,42),(50,52),(39,55),(26,54)],'#334d55')
c.poly([(24,43),(34,43),(38,45),(39,53),(27,52)],'#e1d8b4')
c.poly([(38,45),(45,43),(48,51),(40,53)],'#f3e8c8')
c.line(38,45,40,53,'#acac95')
c.line(27,53,38,54,'#bdb798')
c.line(40,54,49,52,'#c7c9ad')
# Sparse notebook rules and a tiny experimental sketch, no illegible text.
for x,y,w in [(27,45,6),(28,47,6),(29,49,4),(41,46,3),(42,48,3)]:
    c.line(x,y,x+w,y,'#9cae9f')
c.line(42,50,46,50,'#b4bdab')
c.set(35,50,'#69938e')
c.set(35,49,'#69938e')
# Small blue solution bottle at right, white label and ribbed cap.
c.ellipse(57,43,5,2,'#805e49')
c.rect(54,33,5,3,'#263f49')
c.line(54,33,58,33,'#91aaa8')
c.set(56,34,'#587782')
c.rect(55,36,3,2,'#a2c9c4')
c.poly([(55,37),(57,37),(60,39),(60,43),(52,43),(52,39)],'#305d6a')
c.poly([(55,38),(57,38),(59,39),(59,42),(53,42),(53,39)],'#4f9b9f')
c.rect(53,40,6,2,'#e1dfbd')
c.set(54,39,'#b5dbce')
# Glass dropper lying diagonally in the foreground, black rubber bulb.
c.line(52,53,60,45,'#805e49')
c.line(51,52,58,45,'#315361')
c.line(52,52,58,46,'#a5d1c6')
c.line(52,51,57,46,'#d6e8d5')
c.set(51,53,'#dde7cb')
c.poly([(56,45),(59,42),(62,44),(59,48)],'#263b49')
c.line(58,44,60,44,'#68838c')
c.line(57,46,58,47,'#162d3a')
# Consolidate near-identical shades while preserving crisp pixel clusters.
from collections import Counter
counts = Counter(c.get(x,y) for y in range(64) for x in range(64))
rgba = {p['index']:p['rgba'] for p in c.palette()}
remap = {i:i for i in counts}
while len(counts)>76:
    ids=list(counts)
    a,b=min(((a,b) for j,a in enumerate(ids) for b in ids[j+1:]), key=lambda ab: sum((rgba[ab[0]][k]-rgba[ab[1]][k])**2 for k in range(3)))
    if counts[a]>counts[b]: a,b=b,a
    for i in remap:
        if remap[i]==a: remap[i]=b
    counts[b]+=counts.pop(a)
for y in range(64):
    for x in range(64):
        c.set(x,y,remap[c.get(x,y)])
view(c)
save('university_lab_workbench',c)
finish(result)
