import random, math
rng=random.Random(32)
c=new_canvas(128,128,background='#211c3c',name='Moonwell Cottage')
# Deliberately limited, cool violet and warm ember palette.
p={
'sky':'#211c3c','sky2':'#2b2346','sky3':'#342b50','haze':'#453958','haze2':'#55455e',
'moonhalo':'#443853','moonrim':'#aaa0b1','moon':'#ded8c4','moonhi':'#f4eacb','moonmark':'#bdb9b9',
'far':'#302941','far2':'#393148','far3':'#47394c','mist':'#736074','mist2':'#887384',
'black':'#171b2a','dark':'#211f2e','trunk':'#342633','bark':'#49313b','barkhi':'#67434a','barklight':'#805552',
'leafdark':'#30232e','leaf':'#472a36','leaf2':'#5f323e','leaf3':'#793f47','leafhi':'#955249',
'earth':'#292c38','earth2':'#343641','grass':'#414b49','grasshi':'#64705a','mossdark':'#2b403c','moss':'#405a46','mosshi':'#657550','mosslight':'#92935e',
'roofdark':'#252c34','roof':'#354342','roofhi':'#4d5c51','roofpurple':'#494552',
'wooddark':'#3e2b2e','wood':'#674536','woodhi':'#936344','woodlit':'#be8754','woodshadow':'#513739',
'stonedark':'#383541','stone':'#59515a','stonehi':'#7a6d72','stonelight':'#a39490','stonecold':'#655e71',
'glowdark':'#633b39','glow':'#a55636','orange':'#e68b3f','gold':'#ffc36b','light':'#ffe5a0','bright':'#fff0bd',
'path':'#77707c','pathhi':'#a49a9a','water':'#222d40','waterhi':'#817987'
}
for k,v in p.items(): c.color(v,k)
def rect(x,y,w,h,col):c.rect(x,y,w,h,p.get(col,col))
def line(x,y,a,b,col):c.line(x,y,a,b,p.get(col,col))
def poly(pts,col):c.poly(pts,p.get(col,col))
def ell(x,y,rx,ry,col):c.ellipse(x,y,rx,ry,p.get(col,col))
def dot(x,y,col):c.set(x,y,p.get(col,col))
# Night sky: broad, quiet bands and a restrained lunar aureole.
rect(0,32,128,31,'sky2');rect(0,58,128,32,'sky3')
ell(85,25,22,21,'sky2');ell(85,25,18,18,'moonhalo')
ell(85,25,13,13,'moonrim');ell(85,24,12,12,'moon');ell(84,23,11,11,'moonhi')
# Broken crater shapes stay subdued at sprite scale.
poly([(87,14),(91,16),(92,20),(89,21),(87,19)],'moon')
ell(79,27,3,2,'moon');dot(78,25,'moonmark');line(87,32,91,30,'moon');dot(92,24,'moon');dot(83,16,'moon')
for x,y in [(27,17),(46,10),(62,23),(105,12),(111,39),(35,34),(68,5),(18,38)]:
 dot(x,y,'moonrim')
dot(46,9,'mist');dot(45,10,'mist');dot(47,10,'mist')
# Far wood: spectral trunks and meandering branches.
for x,y,w in [(7,21,3),(22,30,2),(35,18,2),(48,32,2),(106,28,3),(119,17,3),(99,44,2)]:
 poly([(x,88),(x+1,y+23),(x-2,y),(x+w,y+7),(x+w+2,86)],'far')
 line(x+1,y+26,x-10,y+14,'far');line(x+1,y+19,x+10,y+5,'far')
 line(x-7,y+17,x-9,y+8,'far');line(x+5,y+14,x+13,y+12,'far')
for x,y in [(13,51),(30,61),(109,55),(119,70),(7,68)]:
 poly([(x-11,y+20),(x-8,y+4),(x-2,y+9),(x+3,y-5),(x+9,y+4),(x+14,y+23)],'far2')
# Distant mist, with interrupted stepped edges.
poly([(0,74),(12,72),(26,74),(42,72),(58,75),(77,72),(98,69),(114,71),(128,68),(128,91),(0,91)],'haze')
poly([(0,81),(19,78),(33,80),(45,79),(54,82),(79,80),(98,76),(119,78),(128,76),(128,94),(0,94)],'haze2')
line(1,80,19,80,'mist');line(11,78,27,78,'mist');line(101,75,119,75,'mist');line(111,77,127,77,'mist')
# Rolling forest ground.
poly([(0,91),(18,88),(36,92),(52,91),(72,94),(99,88),(117,89),(128,86),(128,128),(0,128)],'earth')
poly([(0,106),(23,99),(45,104),(69,98),(92,99),(115,96),(128,99),(128,128),(0,128)],'earth2')
# Shadow and amber spill beneath the house.
ell(71,101,34,6,'dark');ell(64,104,19,6,'glowdark')
poly([(66,96),(76,98),(91,121),(65,120),(59,111)],'woodshadow')
# Path slabs lead the eye from lower foreground to the cottage door.
slabs=[([(68,101),(77,100),(79,103),(68,105),(65,103)],'stone'), ([(66,107),(79,105),(83,109),(72,112),(62,111)],'stonehi'), ([(72,115),(86,111),(92,115),(88,119),(72,120),(68,118)],'path'), ([(79,124),(94,119),(104,123),(105,127),(77,127),(74,126)],'path')]
for pts,col in slabs:
 poly([(x+1,y+2) for x,y in pts],'dark');poly(pts,col)
 for a,b in zip(pts,pts[1:]):
  if b[1]<=a[1]:line(a[0],a[1],b[0],b[1],'pathhi')
line(73,116,80,115,'stonelight');line(85,124,93,122,'stonehi');dot(76,108,'woodlit')
# Cottage masonry body, front and receding side.
poly([(78,75),(98,73),(98,96),(78,103)],'stonedark')
poly([(38,75),(79,75),(79,103),(38,100)],'stone')
# Stone courses are uneven and individually lit.
for yy in [78,85,92,98]:
 line(39,yy,78,yy+1,'stonedark')
for x,y,w,h,col in [(40,80,9,4,'stonehi'),(51,80,9,4,'stone'),(63,79,12,5,'stonehi'),(39,87,6,4,'stonecold'),(60,87,9,4,'stonelight'),(71,87,7,5,'stonehi'),(40,94,10,4,'stonehi'),(52,95,9,5,'stonecold'),(62,96,8,5,'stone'),(72,96,6,6,'stonehi')]:rect(x,y,w,h,col)
for x,y in [(49,79),(61,81),(44,86),(69,86),(51,94),(62,95),(72,97)]:line(x,y,x,y+3,'stonedark')
for y in [80,87,94]:line(80,y,97,y-4,'wooddark')
line(88,76,88,79,'stone');line(94,87,94,92,'stone');line(85,94,85,99,'stone')
# Timber gable and structural beams.
poly([(38,77),(59,48),(80,78)],'wood')
poly([(59,51),(78,77),(59,77)],'woodshadow')
for yy in [64,69,74]:line(43,yy,74,yy,'wooddark')
line(59,51,59,78,'wooddark');line(42,76,77,76,'wooddark')
line(39,79,39,97,'wooddark');line(78,78,78,100,'wooddark');line(40,98,77,101,'wooddark')
line(40,79,40,96,'woodhi');line(44,72,55,57,'woodhi')
# Chimney at the back of the steep roof, cool stone, warm smoke.
poly([(81,48),(89,48),(89,65),(81,61)],'stonedark')
rect(82,47,6,14,'stone');rect(80,45,10,3,'stonedark');rect(81,44,9,2,'stonehi')
line(83,50,87,50,'stonehi');line(82,55,86,55,'stonedark');dot(85,52,'stonedark');line(87,56,87,59,'stonehi')
# Little winding vapor, behind chimney and below moon.
line(85,42,83,39,'mist');line(83,39,83,36,'mist');line(83,36,80,34,'haze2');line(80,34,79,31,'haze2')
# Broad right-hand roof plane, its shingles stepped down the pitch.
poly([(60,44),(80,49),(104,77),(81,83)],'roofdark')
poly([(62,47),(79,51),(100,75),(81,79)],'roof')
for i in range(7):
 y=51+i*4; xl=64+i*2; xr=79+i*3
 line(xl,y,xr,y+2,'roofdark')
 for j in range(3):
  xx=xl+2+j*5
  if xx<xr:line(xx,y+1,xx+2,y+3,'roofhi' if (i+j)%3 else 'roofpurple')
# Moss clings to the ridge and flows in irregular clumps.
poly([(60,44),(80,49),(86,55),(82,56),(76,53),(73,55),(67,51),(64,54),(62,50)],'moss')
line(62,44,79,49,'mosshi');line(65,46,74,48,'mosslight')
for x,y,rx,ry in [(75,57,4,2),(85,61,4,2),(91,69,5,2),(79,70,3,3),(92,74,6,2),(83,77,4,2)]:
 ell(x,y,rx,ry,'moss');line(x-2,y-1,x+1,y-1,'mosshi')
# Front verge is a crooked, thick, moss-covered silhouette.
poly([(31,81),(36,72),(57,43),(62,43),(85,82),(78,84),(59,53),(40,81)],'roofdark')
poly([(33,78),(57,44),(61,44),(81,79),(78,79),(59,50),(38,79)],'moss')
line(35,76,57,45,'mosshi');line(58,45,61,46,'mosslight')
line(60,48,79,79,'roofhi');line(34,81,40,81,'wooddark');line(80,82,103,77,'wooddark')
for x,y in [(39,71),(44,63),(48,58),(52,53),(67,56),(72,65),(77,74)]:
 line(x,y,x+2,y,'mosshi');dot(x,y-1,'mosslight')
for x,y in [(36,80),(41,78),(80,81),(84,80),(96,78)]:
 line(x,y,x,y+3,'moss');dot(x,y+4,'mosshi')
# Soft window halos are built from quiet, solid pixel clusters.
ell(51,86,12,13,'glowdark');rect(42,77,19,19,'wooddark');rect(43,78,17,17,'woodhi')
rect(45,80,13,13,'orange');rect(46,81,11,11,'gold');rect(47,81,8,9,'light');rect(48,82,3,4,'bright')
line(51,80,51,93,'wooddark');line(45,86,58,86,'wooddark');line(52,81,52,85,'woodlit')
rect(42,94,19,2,'wooddark');line(43,94,60,94,'woodlit')
# Open shutters, with visible slats and iron hinges.
poly([(39,79),(43,80),(43,93),(39,91)],'wood');line(40,81,40,90,'woodhi');line(39,83,42,84,'wooddark');line(39,88,42,89,'wooddark')
poly([(59,80),(63,78),(63,92),(59,93)],'wood');line(61,80,61,90,'woodhi');line(60,84,63,83,'wooddark');line(60,89,63,88,'wooddark')
# Tiny attic light, inset under the rafters.
poly([(54,71),(54,65),(58,61),(62,65),(62,71)],'wooddark')
poly([(56,70),(56,66),(58,64),(60,66),(60,70)],'gold');line(58,65,58,70,'woodhi');line(54,72,62,72,'woodlit')
# Low arched front door and a tiny iron latch.
poly([(65,101),(65,85),(67,81),(73,81),(76,85),(76,101)],'wooddark')
poly([(67,100),(67,86),(69,83),(72,83),(74,86),(74,100)],'wood')
line(69,87,69,99,'woodshadow');line(72,87,72,99,'woodshadow');line(67,86,74,86,'woodhi')
rect(69,84,3,4,'orange');dot(70,85,'gold');dot(73,94,'gold');rect(65,101,14,2,'stonelight');line(66,103,78,103,'stone')
# Warm side window and its perspective sill.
poly([(84,80),(94,78),(94,89),(84,92)],'wooddark')
poly([(86,81),(92,80),(92,88),(86,90)],'orange');line(87,82,91,81,'light');line(87,83,87,88,'gold');line(89,81,89,89,'wooddark');line(86,85,92,84,'wooddark');line(83,93,95,89,'woodhi')
# Lantern at the door.
line(79,81,82,81,'black');line(81,81,81,84,'black');rect(79,84,5,7,'wooddark');rect(80,85,3,4,'orange');dot(81,86,'light');line(79,91,83,91,'black')
# Well shadow and stone cylinder, in the near left clearing.
ell(25,109,19,5,'dark')
poly([(11,96),(13,105),(18,110),(30,111),(38,106),(40,96)],'stonedark')
poly([(12,97),(14,104),(20,108),(30,109),(37,104),(38,97)],'stone')
poly([(12,97),(15,103),(21,105),(21,109),(15,107),(12,102)],'stonehi')
line(14,102,22,105,'stonedark');line(22,105,36,102,'stonedark');line(23,106,23,109,'stonedark');line(31,104,31,107,'stonedark');line(17,99,17,102,'stonedark')
ell(25,96,15,6,'stonedark');ell(25,95,14,5,'stonehi');ell(25,95,10,3,'water');line(19,94,29,93,'black');line(20,97,29,97,'waterhi')
line(12,96,17,98,'stonelight');line(17,99,24,100,'stonelight');line(28,100,36,97,'stone');line(15,92,19,91,'stonelight');line(32,92,37,94,'stonelight');line(17,91,19,94,'stonedark');line(32,91,31,94,'stonedark')
# Tall wooden uprights with hand-cranked winch and rope.
rect(12,78,4,20,'wooddark');rect(13,79,2,17,'woodhi');rect(35,78,4,21,'wooddark');line(36,79,36,96,'woodhi')
rect(11,77,29,4,'wooddark');line(12,77,39,77,'woodhi');line(15,80,18,83,'wood');line(35,80,32,83,'wood')
rect(15,85,22,3,'wooddark');line(16,85,35,85,'woodlit');rect(23,83,6,5,'wood')
for xx in [24,26,28]:line(xx,84,xx,87,'woodlit')
line(26,88,26,95,'woodlit');dot(26,96,'stonehi');line(39,86,42,86,'stonecold');line(42,86,42,90,'stonecold');line(40,90,43,90,'woodhi')
# A small bucket beside the base.
poly([(38,103),(44,103),(43,110),(39,110)],'wooddark');rect(39,104,4,5,'wood');line(39,105,43,105,'stone');line(39,109,42,109,'stone');c.path('M39 103 Q41 97 44 103',p['stonehi'],fill=False)
# Textured ground: clusters, little moss shelves and cool grasses.
for i in range(170):
 x=rng.randrange(2,126);y=rng.randrange(94,128)
 if (x<44 and 76<y<112) or (37<x<100 and y<105) or (62<x<106 and y>103):continue
 col=rng.choice(['grass','grass','mossdark','stone','earth','grasshi'])
 line(x,y,min(127,x+rng.choice([1,2,3])),y,col)
for x,y in [(7,109),(17,119),(42,116),(53,109),(109,109),(116,119),(60,123),(5,97),(98,102)]:
 line(x,y,x-2,y-3,'grass');line(x,y,x,y-4,'grasshi');line(x,y,x+2,y-2,'grass')
# Ancient trunks frame the whole scene with forked, angular roots.
poly([(0,0),(12,0),(16,18),(13,37),(17,58),(14,80),(17,102),(27,116),(18,113),(11,105),(8,116),(0,121)],'dark')
poly([(3,0),(9,0),(12,20),(9,38),(13,60),(10,79),(13,99),(19,110),(11,105),(6,96),(6,70),(8,55),(6,37),(8,19)],'trunk')
poly([(9,4),(12,19),(10,34),(12,49),(10,60),(11,74),(8,88),(10,99),(7,96),(6,78),(8,59),(6,39)],'bark')
line(10,42,12,58,'barkhi');line(9,65,8,79,'barkhi');line(9,94,14,105,'barkhi');line(5,28,6,36,'barkhi')
# Limbs reach inward over the sky.
poly([(10,41),(20,30),(24,15),(30,6),(29,17),(25,28),(25,34),(17,46)],'dark')
poly([(11,25),(22,20),(35,20),(47,12),(41,19),(33,24),(22,24),(13,32)],'trunk')
line(20,31,23,20,'bark');line(23,22,35,22,'bark');line(35,21,42,17,'barkhi')
poly([(0,58),(4,51),(5,42),(0,35)],'black')
# Right elder, bent toward the moon.
poly([(115,0),(128,0),(128,128),(119,124),(114,116),(103,119),(111,111),(115,94),(112,76),(117,58),(113,38),(115,23),(109,10)],'dark')
poly([(120,0),(124,0),(120,23),(119,39),(122,59),(117,79),(121,100),(117,113),(123,124),(117,120),(114,111),(118,96),(114,77),(119,58),(115,38),(118,22)],'trunk')
line(119,44,122,59,'bark');line(122,59,117,77,'barkhi');line(116,80,119,96,'bark');line(119,99,115,112,'barkhi')
poly([(117,52),(110,44),(102,41),(98,31),(94,27),(101,29),(107,38),(115,40),(121,49)],'dark')
line(119,48,110,42,'bark');line(110,42,105,42,'barkhi');line(105,39,101,32,'bark')
poly([(119,26),(108,19),(103,8),(94,0),(101,0),(108,8),(111,15),(122,21)],'trunk')
line(111,17,105,10,'bark');line(116,22,110,18,'barkhi')
line(103,9,95,11,'trunk');line(108,38,111,32,'trunk');line(98,31,92,32,'trunk');line(26,25,34,30,'trunk')
# Angular leaf masses, dark wine and russet. Small stepped clusters, never noise.
clusters=[(1,6,18,9),(18,4,18,8),(35,3,18,6),(48,3,12,5),(2,22,10,9),(24,15,10,5),(37,18,10,5),(4,45,7,6),(125,8,14,12),(109,1,16,8),(119,29,11,8),(109,39,8,5),(126,49,8,9),(4,74,6,7),(125,82,6,10)]
for cx,cy,rx,ry in clusters:
 pts=[(cx-rx,cy-2),(cx-rx+3,cy-ry+2),(cx-4,cy-ry),(cx+1,cy-ry-2),(cx+5,cy-ry+1),(cx+rx-2,cy-3),(cx+rx,cy+2),(cx+rx-4,cy+ry-1),(cx+1,cy+ry),(cx-4,cy+ry+2),(cx-rx+2,cy+ry-1)]
 # clip manually for frame foliage
 pts=[(max(0,min(127,x)),max(0,min(127,y))) for x,y in pts]
 poly(pts,'leafdark')
 for j in range(19):
  x=cx+rng.randrange(-rx,rx+1);y=cy+rng.randrange(-ry,ry+1)
  if 0<=x<126 and 0<=y<126 and ((x-cx)/max(1,rx))**2+((y-cy)/max(1,ry))**2<0.9:
   col=rng.choice(['leaf','leaf','leaf2','leaf3'])
   rect(x,y,rng.choice([2,3,4]),2,col)
   if col=='leaf3' and j%3==0:dot(x+1,y,'leafhi')
# Foreground roots and stray fallen leaves.
line(0,123,9,116,'black');line(8,117,14,116,'trunk');line(115,117,107,124,'black');line(119,121,125,127,'black')
for x,y in [(27,117),(36,122),(47,112),(56,119),(110,102),(103,114),(20,123),(31,113),(63,125)]:
 line(x,y,x+2,y-1,'leaf3');dot(x+1,y-1,'leafhi')
# Low ribbons of mist drift through the clearing, keeping their edges broken.
line(19,87,29,87,'mist');line(23,86,32,86,'haze2');line(28,88,35,88,'haze2')
line(100,86,111,86,'mist');line(98,87,106,87,'haze2');line(104,84,113,84,'haze2')
line(1,91,8,91,'haze2');line(94,97,105,97,'haze2');line(99,98,108,98,'haze')
# Moonlit mushrooms and a few amber fireflies add a fairy-tale scale.
for x,y in [(47,105),(51,107),(103,108),(107,110)]:
 line(x,y,x,y+3,'stonehi');line(x-2,y,x+2,y,'leaf3');line(x-1,y-1,x+1,y-1,'leafhi');dot(x,y-1,'woodlit')
for x,y in [(31,66),(101,68),(54,112),(20,59),(109,92)]:
 dot(x,y,'gold');dot(x-1,y,'glowdark');dot(x,y+1,'glowdark')
print(c.stats_text())
print(c.matrix_text(region=(10,77,62,110)))
save('magic-forest-cottage',c)
finish(c)
