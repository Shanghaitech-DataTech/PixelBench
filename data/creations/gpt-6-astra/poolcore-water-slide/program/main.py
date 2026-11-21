import random, math
random.seed(19)
result = new_canvas(128,128,background='#d1e6e8',name='Stillwater')
c=result
# Restrained cool tile palette
wall=['#c8dfe2','#cfe4e6','#d6e9e9','#bfd8de','#dcebec']
def quadgrid(a,b,d,e,nx,ny,colors,grout):
    # clockwise corners: upper left, upper right, lower right, lower left
    def p(u,v):
        return (round(a[0]*(1-u)*(1-v)+b[0]*u*(1-v)+d[0]*u*v+e[0]*(1-u)*v),round(a[1]*(1-u)*(1-v)+b[1]*u*(1-v)+d[1]*u*v+e[1]*(1-u)*v))
    c.poly([a,b,d,e],colors[0])
    for j in range(ny):
        for i in range(nx):
            c.poly([p(i/nx,j/ny),p((i+1)/nx,j/ny),p((i+1)/nx,(j+1)/ny),p(i/nx,(j+1)/ny)],random.choice(colors))
    for i in range(nx+1):
        x,y=p(i/nx,0); xx,yy=p(i/nx,1); c.line(x,y,xx,yy,grout)
    for j in range(ny+1):
        x,y=p(0,j/ny);xx,yy=p(1,j/ny);c.line(x,y,xx,yy,grout)
# Ceiling, expanding toward the viewer
c.poly([(0,0),(127,0),(127,16),(104,29),(30,29),(0,13)],'#a8c4ce')
c.poly([(0,0),(127,0),(104,27),(30,27)],'#bdd3d9')
for x in [-80,-20,37,90,150,210]:
    c.line(65,38,x,0,'#a9c4cf')
for y in [5,15,23]: c.line(0,y,127,y,'#acc7d0')
# Recessed fluorescent strips
for poly in [[(16,3),(22,3),(42,18),(38,18)],[(75,2),(82,2),(76,18),(72,18)],[(109,10),(116,10),(99,22),(95,22)],[(48,23),(57,23),(60,26),(53,26)]]:
    c.poly(poly,'#e0f1ee')
    c.poly([(x,y-1) for x,y in poly],'#f4fff4')
c.line(30,28,104,28,'#f1f7ee')
# Mosaic room envelope
quadgrid((30,29),(104,29),(104,66),(30,66),19,10,wall,'#aac8d1')
quadgrid((0,13),(30,29),(30,66),(0,89),7,12,['#b8d2db','#c5dce1','#cbdfe3'],'#9fbdca')
quadgrid((104,29),(127,16),(127,89),(104,66),6,13,['#bdd8de','#cbe2e4','#d5e8e7'],'#a5c5ce')
# A vacant opening in the far hall
c.rect(38,40,15,24,'#a2c1ca')
c.rect(40,41,11,22,'#6f96a9')
c.rect(42,43,9,20,'#88adba')
c.rect(44,44,7,19,'#97bac5')
c.line(40,63,53,63,'#e5efea')
c.line(40,41,40,62,'#d8e8e7')
c.rect(65,35,17,2,'#ecf5ed')
# floor surround
quadgrid((30,65),(104,65),(127,127),(0,127),22,15,['#d7e7e6','#cce1e2','#e0edeb','#c0d8dd'],'#a9c8ce')
# far pool curb, dark waterline and broad pale coping
c.poly([(31,64),(98,64),(124,127),(0,127)],'#edf4ed')
c.poly([(34,68),(96,68),(118,127),(4,127)],'#699eaf')
c.poly([(35,70),(95,70),(115,127),(7,127)],'#90d5df')
# Water plane: tiled floor visible through pale clear water
water=['#9edee4','#a5e1e6','#a9e2e7','#99d9e2','#a2dce3']
quadgrid((35,70),(95,70),(115,127),(7,127),15,11,water,'#8fcbd7')
# Broad diffuse cool reflections on the surface
c.poly([(46,72),(51,72),(48,82),(47,89),(43,98),(38,110),(33,121),(23,127),(31,109),(38,93)],'#b6e8e9')
c.poly([(71,72),(74,72),(78,88),(78,97),(83,111),(85,127),(77,127),(77,111),(73,95)],'#b4e7e9')
c.poly([(91,79),(95,79),(100,93),(104,103),(102,106),(98,98)],'#b6e8e9')
# Broken surface glints, following perspective
for x,y,w in [(39,76,7),(53,73,6),(68,76,5),(81,72,7),(28,92,9),(33,96,8),(23,109,12),(17,121,9),(41,116,11),(46,107,7),(80,104,9),(86,118,12),(97,113,10),(73,123,10),(51,125,8),(85,89,7),(39,86,7),(68,83,5),(48,100,5),(93,100,5)]:
    c.line(x,y,x+w,y,'#c9f0ed')
    c.line(x+2,y+1,x+w+2,y+1,'#afe3e7')
for x,y,w in [(42,80,5),(50,88,6),(23,103,10),(32,113,8),(51,120,9),(67,114,9),(89,108,8),(97,123,10),(77,96,5),(85,81,5),(44,103,6)]:
    c.line(x,y,x+w,y,'#88cbd8')
# Pool rim highlights
c.line(31,65,98,65,'#f3f8ef')
c.line(31,66,0,126,'#e7f2ed')
c.line(98,66,123,127,'#f7faf0')
c.line(33,69,5,127,'#78afbf')
c.line(97,69,119,127,'#84b6c3')
# Column repeated into distance
# Back pilaster
quadgrid((59,29),(64,29),(64,64),(59,64),2,9,['#e3efeb','#d8e9e7'],'#b4d0d4')
c.poly([(64,29),(67,29),(67,64),(64,64)],'#9fbfc9')
c.line(59,29,59,63,'#f4f7ec')
# left mid column
quadgrid((18,24),(24,27),(24,77),(18,82),2,12,['#d4e6e6','#e4efeb','#dcebe7'],'#aac9d0')
c.poly([(24,27),(28,29),(28,72),(24,77)],'#96b6c4')
for y in range(33,73,5): c.line(24,y,28,y-1,'#84a9ba')
c.poly([(16,80),(24,75),(28,74),(26,79),(17,85)],'#e4eeea')
c.line(18,25,18,80,'#f0f5eb')
# right foreground column
quadgrid((114,20),(123,15),(123,101),(114,92),3,16,['#dbece7','#e3f0e9','#d4e7e6'],'#afcdd0')
c.poly([(123,15),(127,13),(127,101),(123,101)],'#92b3c0')
for y in range(22,100,5): c.line(123,y,127,y,'#7ea4b6')
c.line(114,21,114,92,'#f4f8ed')
c.poly([(112,92),(123,99),(127,99),(127,104),(122,104),(111,96)],'#e7f0e8')
# Slide access ladder behind the chute
c.line(99,40,105,65,'#6e96a6'); c.line(104,39,110,65,'#6e96a6')
c.line(100,40,106,65,'#c6dcdf');c.line(105,40,111,65,'#d9e8e6')
for y in [46,51,56,61]:
    x=100+(y-40)//4
    c.line(x,y,x+5,y,'#7d9faf')
# Slide support posts
c.rect(88,58,3,15,'#86afbc');c.line(88,59,88,71,'#e1eeea')
c.line(85,73,93,73,'#81bdcb')
# Sculpted white S-shaped flume, open end over water
c.path('M 101 37 C 90 36 78 40 78 47 C 78 53 94 54 93 60 C 92 67 79 67 78 76 L 85 80 C 86 72 101 71 103 61 C 105 49 88 48 88 45 C 88 43 97 43 103 44 Z','#7eabbc')
c.path('M 101 35 C 88 34 76 39 76 46 C 75 54 92 54 92 59 C 91 65 77 65 76 75 L 82 78 C 82 70 98 69 100 60 C 102 51 86 49 85 45 C 84 42 95 41 103 42 Z','#eef5ee')
# inner trough and highlighted upper lip
c.path('M 101 38 C 90 37 79 40 79 46 C 79 52 96 52 96 59 C 96 66 81 67 79 75', '#bfd7dd',fill=False)
c.path('M 101 39 C 90 38 81 41 81 46 C 82 51 97 52 97 59 C 97 67 82 68 81 75', '#cbdfe1',fill=False)
c.path('M 99 35 C 88 35 76 40 76 46 C 76 53 92 54 92 59 C 92 64 78 67 76 74','#ffffff',fill=False)
c.line(76,75,82,78,'#f8faf2')
# small flowing ripples at the exit
c.line(77,79,84,81,'#d8f6ed');c.line(74,83,81,83,'#caf1eb');c.line(85,80,89,80,'#d0f4ed')
# Isolated swimmer and ring reflection
c.ellipse(59,98,11,3,'#8bcbd3')
c.line(52,101,63,101,'#d0e9cb')
c.line(55,104,61,104,'#b9dfcf')
c.ellipse(59,95,10,4,'#6aadb9')
c.ellipse(59,93,10,5,'#ba953d')
c.ellipse(59,92,10,4,'#f2ce57')
c.ellipse(59,91,9,3,'#ffe885')
c.ellipse(59,91,5,2,'#6ba8b4')
c.line(51,93,54,94,'#ffe78a');c.line(63,94,67,92,'#e8b947')
# Back, shoulders and arms seen from behind
c.poly([(56,85),(61,85),(64,89),(63,92),(55,92),(54,89)],'#d5a48b')
c.line(55,87,52,90,'#f1c7a5');c.line(52,90,50,90,'#edc1a0')
c.line(62,87,65,90,'#edc1a0');c.line(65,90,67,90,'#edc1a0')
c.rect(57,83,4,5,'#e8bb9b')
c.line(57,89,61,89,'#885e58');c.rect(56,90,6,2,'#7c6971')
# Dark wet hair, rounded silhouette and subtle warm highlight
c.poly([(57,78),(60,78),(62,80),(62,85),(60,87),(56,86),(55,83),(55,80)],'#4c4c53')
c.rect(56,80,5,5,'#665a5b');c.line(56,80,59,79,'#87706a')
c.line(60,81,61,85,'#534e56');c.set(57,85,'#77605e')
# Ring's nearer edge and surrounding concentric ripples
c.line(55,95,62,95,'#f5d361')
c.line(47,97,51,98,'#d4f3ea');c.line(66,98,72,96,'#d1f1e8')
c.line(49,100,53,101,'#a7dde0');c.line(65,101,71,100,'#c0e9e6')
# Consolidate near-identical shades into a compact pixel-art palette.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(128) for x in range(128))
pal={p['index']:p['rgba'] for p in c.palette()}
remap={i:i for i in counts}
while len(counts)>84:
    ids=list(counts)
    pair=min(((a,b) for k,a in enumerate(ids) for b in ids[k+1:]),key=lambda ab:sum((pal[ab[0]][j]-pal[ab[1]][j])**2 for j in range(3)))
    a,b=pair
    if counts[a]>counts[b]: a,b=b,a
    counts[b]+=counts.pop(a)
    for i in remap:
        if remap[i]==a: remap[i]=b
for y in range(128):
    for x in range(128):
        idx=c.get(x,y)
        if remap[idx]!=idx: c.set(x,y,remap[idx])
view(result)
finish(result)
