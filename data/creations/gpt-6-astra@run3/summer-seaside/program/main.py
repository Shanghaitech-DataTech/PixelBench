import random
random.seed(12)
result = new_canvas(128,128,background='#75d5ed',name='summer-seaside')
c=result
# Clear high sky, in broad pixel bands.
c.rect(0,0,128,17,'#69c9ec')
c.rect(0,17,128,19,'#79d7ef')
c.rect(0,36,128,15,'#91e1ef')
# Sun with a warm stepped corona.
c.circle(103,18,12,'#a5e4e8')
c.circle(103,18,10,'#fff1a1')
c.circle(103,18,8,'#fff8ce')
c.rect(99,11,7,2,'#fffce7')
# Clouds are clustered, with cool undersides.
def cloud(x,y,s=1):
    c.rect(x,y+5,26,5,'#d5f2f5')
    c.rect(x+3,y+2,19,7,'#f7fcf5')
    c.rect(x+7,y,9,4,'#f7fcf5')
    c.rect(x-3,y+6,33,3,'#f7fcf5')
    c.rect(x+4,y+9,21,2,'#c1e8f1')
    c.rect(x,y+8,28,2,'#e8f8f7')
cloud(13,13)
cloud(56,29)
c.rect(0,36,16,3,'#d5f2f5'); c.rect(2,33,9,4,'#f7fcf5')
# Two distant gull silhouettes.
for x,y in [(46,20),(84,12)]:
    c.line(x-4,y-2,x-2,y-2,'#33768f')
    c.line(x-2,y-2,x,y,'#33768f')
    c.line(x,y,x+2,y-2,'#33768f')
    c.line(x+2,y-2,x+4,y-2,'#33768f')
# Ocean horizon and its long colour shelves.
c.rect(0,49,128,4,'#227cb8')
c.rect(0,53,128,8,'#258dc4')
c.rect(0,61,128,8,'#249fd0')
c.rect(0,69,128,10,'#24b5d0')
c.rect(0,79,128,13,'#35c6cc')
c.rect(0,92,128,10,'#69d9cb')
# The beach sweeps diagonally across the composition.
sand=[(0,83),(15,86),(29,90),(45,93),(61,94),(76,93),(94,89),(111,84),(127,81),(127,128),(0,128)]
c.poly(sand,'#f2cf82')
# damp darker sand under wash
c.path('M0 80 L16 83 L30 87 L45 90 L61 91 L77 90 L94 86 L111 81 L127 78 L127 84 L111 87 L94 92 L77 97 L61 98 L45 97 L30 94 L16 89 L0 86 Z','#dcbf79')
c.path('M0 78 L16 81 L30 85 L45 88 L61 89 L77 88 L94 84 L111 79 L127 76 L127 81 L111 84 L94 89 L77 93 L61 95 L45 93 L30 90 L16 86 L0 83 Z','#8de3d2')
# Lacy shore edge.
for pts,col in [([(0,82),(15,85),(29,89),(45,92),(61,94),(77,92),(94,88),(111,83),(127,80)],'#f7fff0'), ([(0,80),(15,83),(29,87),(45,90),(61,91),(77,90),(94,86),(111,81),(127,78)],'#c8f6e7')]:
    for a,b in zip(pts,pts[1:]): c.line(*a,*b,col)
for x,y,w in [(3,83,5),(20,87,5),(35,91,7),(52,94,6),(68,94,4),(83,91,7),(99,87,5),(119,82,8)]: c.rect(x,y,w,1,'#fffcec')
# Broken ocean glints, kept horizontal.
for y,xs,col in [(54,[3,23,61,111],'#64c4dc'),(58,[12,40,74,117],'#63c8e3'),(64,[0,27,59,98],'#79dce5'),(70,[15,47,84,115],'#85e8e7'),(76,[4,34,68,105],'#a6f1e7')]:
    for x in xs: c.rect(x,y,random.randint(3,10),1,col)
# rolling whitecaps
for points in [[(0,70),(12,71),(24,74),(38,76),(51,76)],[(65,80),(79,79),(93,75),(109,72),(127,71)]]:
    for a,b in zip(points,points[1:]): c.line(*a,*b,'#dcfff0')
c.line(6,72,16,73,'#8fe7dd');c.line(28,76,40,78,'#8fe7dd')
c.line(86,79,100,75,'#8fe7dd');c.line(112,73,124,73,'#8fe7dd')
# Tiny far-off sailboat, white triangular sail and shaded jib.
c.line(90,44,90,61,'#476d7b')
c.poly([(88,45),(88,58),(78,58)],'#fffdf0')
c.poly([(92,49),(98,58),(92,58)],'#d6edf0')
c.line(87,48,87,56,'#ffffff')
c.poly([(78,60),(100,60),(96,64),(83,64)],'#f9f8df')
c.line(83,64,96,64,'#286e9c')
c.line(83,67,94,67,'#6bcddc')
# Sand warmth and little grains.
c.poly([(0,109),(17,104),(31,107),(48,105),(62,110),(87,106),(108,101),(127,102),(127,128),(0,128)],'#f8d991')
for i in range(80):
    x=random.randrange(128);y=random.randrange(94,128)
    if c.get(x,y) in [c.color('#f2cf82'),c.color('#f8d991')]:
        c.rect(x,y,random.choice([1,2,3]),1,random.choice(['#e6bc73','#ffe6aa']))
# Broad umbrella shadow cast to lower right.
c.ellipse(40,108,23,6,'#dfb574')
c.ellipse(38,107,18,4,'#d5a96b')
# Pole.
c.line(31,77,35,108,'#986647')
c.line(32,77,36,107,'#ffe3a6')
c.set(36,108,'#a9794b')
# Umbrella silhouette and alternating radial panels.
c.poly([(7,78),(10,70),(15,64),(23,59),(31,57),(40,59),(49,64),(55,71),(59,79),(49,82),(39,81),(29,83),(18,80)],'#ab3c47')
c.poly([(8,76),(12,69),(20,62),(31,58),(23,66),(18,77)],'#f25553')
c.poly([(18,77),(23,66),(31,58),(30,68),(29,80)],'#fff6dc')
c.poly([(29,80),(30,68),(31,58),(38,66),(40,79)],'#ee514f')
c.poly([(40,79),(38,66),(31,58),(45,64),(50,78)],'#fff6dc')
c.poly([(50,78),(45,64),(40,61),(49,65),(55,72),(58,78)],'#e34149')
# fine canopy lighting and scalloped hem
c.line(13,69,21,63,'#ff8070');c.line(21,63,30,59,'#ff8070')
c.line(25,65,29,61,'#ffffff');c.line(33,61,37,66,'#ff8070')
c.poly([(8,76),(18,77),(18,80),(12,80),(8,78)],'#cf454b')
c.poly([(18,77),(29,80),(29,82),(23,82),(18,80)],'#e7e6d1')
c.poly([(29,80),(40,79),(40,82),(34,84),(29,82)],'#ce3e47')
c.poly([(40,79),(50,78),(50,81),(45,83),(40,82)],'#e7e6d1')
c.poly([(50,78),(58,78),(58,80),(54,82),(50,81)],'#bf3543')
c.rect(30,55,2,3,'#a66d49');c.set(30,55,'#ffe5aa')
# Towel in perspective, with turquoise stripes and fringe.
c.poly([(69,100),(89,96),(104,115),(80,121)],'#d8ae70')
c.poly([(67,98),(87,94),(102,113),(79,119)],'#fff4d7')
for p in [[(69,101),(90,97),(92,100),(72,104)],[(74,107),(94,102),(96,105),(76,110)],[(78,113),(99,108),(101,111),(80,116)]]: c.poly(p,'#39aeb6')
c.line(68,98,87,94,'#fffbe6')
for x,y in [(79,119),(83,118),(87,117),(91,116),(95,115),(99,114)]: c.line(x,y,x+1,y+2,'#fff2cf')
# Flip-flops beside the towel, each with a readable Y strap.
c.poly([(108,101),(111,98),(115,99),(117,103),(116,110),(113,113),(110,111)],'#d3a56b')
c.poly([(106,100),(108,97),(112,97),(114,100),(114,106),(111,110),(108,109)],'#275c78')
c.poly([(107,100),(109,98),(111,98),(113,101),(112,106),(110,108),(108,107)],'#3d94a5')
c.line(108,104,110,101,'#fff0c6');c.line(110,101,113,103,'#fff0c6');c.set(110,100,'#fff0c6')
c.poly([(118,105),(121,103),(124,105),(125,111),(123,117),(120,117),(117,114)],'#d3a56b')
c.poly([(117,104),(120,102),(123,104),(123,110),(121,115),(118,115),(116,112)],'#275c78')
c.poly([(118,105),(120,103),(122,105),(122,110),(120,113),(118,113),(117,111)],'#3d94a5')
c.line(117,109,120,107,'#fff0c6');c.line(120,107,122,110,'#fff0c6');c.set(120,106,'#fff0c6')
# A little pink shell on the open sand.
c.poly([(53,113),(54,110),(57,109),(60,111),(60,113),(57,115)],'#d99679')
c.line(54,111,57,114,'#fff1cf');c.line(57,110,58,113,'#f7c4a1')
view(result)
finish(result)
