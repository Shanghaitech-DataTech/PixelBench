import random, math
random.seed(17)
c = new_canvas(128, 128, '#211a39', name='Moonwell Cottage')
P = {
'ink':'#151323','deep':'#1b172b','sky':'#211a39','sky2':'#292040','sky3':'#332747','sky4':'#3b2e50',
'far':'#3f3154','far2':'#493959','mist':'#655471','mist2':'#78677e','mist3':'#938495',
'moonshadow':'#b5a5b8','moonmid':'#ded3d4','moon':'#f6ead7','moonglow':'#53425f',
'ground':'#353540','ground2':'#42434b','ground3':'#53515a','grass':'#4c5550','grass2':'#697063',
'barkdeep':'#271d2d','bark':'#3d2938','bark2':'#593949','bark3':'#76505c','barklight':'#946975',
'leafdark':'#2c2033','leaf':'#442838','leaf2':'#623340','leaf3':'#81424a','leaf4':'#9b5660',
'roofdark':'#242e32','roof':'#35413d','moss':'#4c5a47','moss2':'#677451','moss3':'#899263',
'wooddeep':'#34272e','wood':'#5f403d','wood2':'#825646','wood3':'#aa7757',
'stonedark':'#49414e','stone':'#645b64','stone2':'#817779','stone3':'#a19692',
'lightdark':'#914539','lightedge':'#bd6238','light':'#ed963e','light2':'#ffc361','light3':'#ffe09a',
'path':'#6c6570','pathlight':'#92858a','pathdark':'#494551'
}
C = {k:c.color(v, name=k) for k,v in P.items()}
def rect(x,y,w,h,col): c.rect(x,y,w,h,C.get(col,col))
def poly(points,col): c.poly(points,C.get(col,col))
def line(x,y,u,v,col): c.line(x,y,u,v,C.get(col,col))
def dot(x,y,col): c.set(x,y,C.get(col,col))
def ellipse(x,y,rx,ry,col): c.ellipse(x,y,rx,ry,C.get(col,col))
def path(d,col,fill=True): c.path(d,C.get(col,col),fill=fill)

# A quiet, stepped violet sky.
rect(0,30,128,24,'sky2'); rect(0,54,128,26,'sky3'); rect(0,80,128,21,'sky4')
# Lunar halo and a full, softly cratered disc.
ellipse(48,23,15,15,'sky3'); ellipse(48,23,13,13,'moonglow')
ellipse(48,23,11,11,'moonmid'); ellipse(47,22,10,10,'moon')
poly([(52,14),(56,18),(57,25),(54,31),(48,33),(45,31),(51,30),(54,25),(54,19)],'moonmid')
poly([(41,17),(43,16),(45,17),(44,19),(42,20),(40,19)],'moonmid')
rect(39,23,3,2,'moonmid'); dot(42,25,'moonmid'); rect(47,28,3,2,'moonmid')
rect(52,20,2,3,'moonshadow'); dot(51,23,'moonmid'); dot(46,15,'moonmid')
for x,y in [(31,17),(64,15),(69,25),(32,39),(57,6),(78,10),(91,17),(105,40),(25,50),(59,31)]:
    dot(x,y,'moonshadow')
line(72,7,72,11,'moonmid'); line(70,9,74,9,'moonmid'); dot(72,9,'moon')

# Distant trunks and twig silhouettes, deliberately soft in value.
for x,w,top,bend in [(23,3,20,3),(31,3,31,-2),(38,2,36,4),(57,2,28,-2),(95,3,21,6),(104,3,13,-4),(113,3,26,3),(7,3,20,1)]:
    poly([(x-w,91),(x,top+15),(x+bend,top),(x+bend+1,top),(x+2,55),(x+w,92)],'far')
    line(x,top+25,x-8,top+13,'far'); line(x-8,top+13,x-10,top+6,'far')
    line(x,top+34,x+7,top+20,'far'); line(x+7,top+20,x+8,top+11,'far')
poly([(0,78),(13,75),(24,78),(35,74),(49,77),(65,73),(84,77),(101,72),(127,77),(127,104),(0,104)],'far')
# Broken ribbons of mist behind the buildings.
poly([(0,75),(14,74),(27,76),(43,75),(51,77),(33,79),(17,78),(0,79)],'mist')
poly([(91,71),(105,69),(120,70),(127,69),(127,73),(114,73),(105,72),(91,73)],'mist')
rect(24,70,12,1,'far2'); rect(28,69,16,1,'far2'); rect(104,77,20,1,'mist2')
poly([(0,85),(18,82),(37,83),(54,82),(70,84),(91,83),(115,80),(127,82),(127,91),(0,96)],'ground')
poly([(0,95),(13,91),(32,93),(45,90),(62,94),(82,90),(101,94),(118,89),(127,92),(127,128),(0,128)],'ground2')
poly([(0,111),(18,107),(31,112),(48,107),(59,112),(78,110),(102,106),(127,111),(127,128),(0,128)],'ground')
poly([(0,121),(21,117),(39,121),(60,117),(82,121),(108,116),(127,119),(127,128),(0,128)],'deep')

# Ancient trees curl inward to enclose the clearing.
poly([(0,8),(9,11),(14,27),(12,40),(17,54),(15,67),(17,78),(13,94),(20,105),(30,111),(19,111),(10,104),(4,112),(0,111)],'ink')
poly([(0,12),(7,15),(11,30),(9,43),(13,56),(11,70),(13,80),(9,95),(15,104),(8,101),(3,105),(5,89),(4,73),(7,57),(3,43)],'bark')
poly([(1,24),(5,31),(4,43),(9,58),(7,74),(8,84),(5,96),(4,83),(5,67),(2,51)],'bark2')
path('M 10 68 Q 21 60 21 52 Q 20 42 26 35 L 32 27 L 35 14 L 39 5 L 42 5 L 38 18 L 36 29 L 29 39 Q 25 44 27 52 Q 27 64 15 76 Z','barkdeep')
path('M 12 67 Q 23 58 23 51 Q 21 44 28 35 L 34 27 L 37 14 L 39 8 L 39 15 L 36 29 L 30 38 Q 25 46 26 52 Q 24 64 13 72 Z','bark2')
path('M 8 43 Q 17 35 15 23 L 21 14 L 24 5 L 27 0 L 31 0 L 26 12 L 20 21 Q 23 37 11 49 Z','bark')
line(22,24,30,22,'bark'); line(30,22,34,17,'bark')
line(26,38,35,40,'bark2'); line(35,40,41,36,'bark2'); line(35,40,36,44,'bark')
path('M 7 74 Q 11 59 8 51 M 11 89 L 10 97 L 19 106 M 12 40 Q 18 32 17 25','bark3',False)
# knot, splitting roots, and a few lit ridges
ellipse(10,59,3,5,'barkdeep'); path('M 10 55 Q 6 60 10 63 L 11 60','bark3',False)
line(11,101,25,108,'bark2'); line(25,108,33,108,'bark'); line(4,103,1,110,'bark2')

poly([(118,0),(127,0),(127,113),(122,108),(111,109),(103,114),(99,112),(111,103),(114,90),(112,77),(116,63),(112,49),(113,35),(109,24)],'ink')
poly([(121,0),(127,0),(127,104),(124,102),(116,105),(119,91),(116,78),(120,64),(117,50),(118,35),(114,22)],'bark')
poly([(121,13),(124,27),(122,42),(122,56),(124,65),(120,79),(122,92),(119,103),(116,104),(118,88),(115,77),(119,63),(116,49),(117,33)],'bark2')
path('M 118 58 Q 109 51 110 42 Q 109 34 99 32 L 93 25 L 83 22 L 80 17 L 84 17 L 88 20 L 97 22 L 103 28 Q 116 29 116 42 Q 114 48 121 51 Z','barkdeep')
path('M 119 54 Q 111 49 113 42 Q 113 32 102 30 L 95 24 L 87 22 L 97 25 L 102 32 Q 110 34 110 42 Q 109 51 118 58 Z','bark2')
path('M 121 32 L 111 22 L 106 12 L 97 7 L 89 9 L 83 7 L 81 3 L 86 5 L 98 3 L 111 10 L 115 18 L 126 23 Z','bark')
line(107,13,110,5,'bark2'); line(110,5,108,0,'bark2')
path('M 121 47 L 123 57 L 121 68 L 118 77 L 120 87 M 121 30 L 118 21 L 116 16','bark3',False)
ellipse(121,72,2,4,'barkdeep'); line(121,69,120,72,'bark3')
line(119,103,109,109,'bark2'); line(109,109,106,112,'bark'); line(124,103,126,108,'bark3')

# Canopy: jagged, overlapping leaf masses in wine red and plum.
leftmass=[(0,0),(37,0),(35,5),(29,8),(30,13),(23,15),(24,20),(18,23),(21,28),(14,31),(13,36),(6,34),(4,40),(0,39)]
rightmass=[(76,0),(127,0),(127,44),(121,42),(119,36),(112,38),(109,32),(106,29),(108,24),(99,21),(99,16),(90,17),(88,12),(80,13),(82,8),(75,6)]
poly(leftmass,'leafdark'); poly(rightmass,'leafdark')
def leaf_patch(x,y,s,col):
    poly([(x-s,y),(x-s+2,y-2),(x-1,y-2),(x,y-4),(x+3,y-3),(x+3,y-1),(x+s,y),(x+s-1,y+2),(x+2,y+2),(x,y+4),(x-3,y+3),(x-3,y+1),(x-s,y+1)],col)
for x,y,s in [(5,4,7),(17,4,9),(28,3,7),(8,16,8),(19,12,8),(5,27,6),(14,24,5),(82,3,6),(94,7,8),(108,3,9),(120,10,9),(111,18,8),(124,25,7),(117,31,5)]:
    leaf_patch(x,y,s,'leaf')
for x,y,s in [(7,6,5),(20,3,6),(5,17,5),(17,13,5),(6,27,4),(89,4,5),(101,8,6),(113,4,7),(120,16,5),(109,20,4),(123,29,4)]:
    leaf_patch(x,y,s,'leaf2')
for x,y in [(4,5),(17,1),(23,4),(8,14),(15,13),(3,26),(88,2),(98,6),(104,9),(113,2),(122,14),(109,18),(122,28)]:
    rect(x,y,3,1,'leaf3'); dot(x-1,y+1,'leaf3'); dot(x+1,y+2,'leaf2')
for x,y in [(20,24),(29,16),(29,44),(36,35),(93,32),(104,36),(115,43),(17,40)]:
    line(x,y,x+2,y-1,'leaf2'); dot(x+2,y,'leaf3')

# Low fog travels behind the cottage and well.
poly([(1,88),(12,86),(26,87),(38,85),(49,87),(49,90),(26,90),(15,89),(1,90)],'mist')
rect(20,91,18,1,'mist'); rect(26,92,12,1,'far2')
poly([(105,86),(116,84),(126,85),(127,87),(115,87),(106,89)],'mist')
rect(111,89,13,1,'mist2')

# Cottage silhouette, chimney, and old stone walls.
poly([(37,70),(62,34),(82,33),(112,74),(106,78),(106,100),(61,103),(39,95),(39,75),(35,75)],'ink')
# tall chimney, with worn cap and mortar
poly([(56,50),(56,30),(60,27),(68,29),(69,47)],'stonedark')
rect(57,30,9,19,'stone'); rect(63,30,4,19,'stonedark')
rect(55,28,13,3,'wooddeep'); rect(56,27,11,2,'stone2'); rect(58,27,7,1,'stone3')
line(57,35,65,35,'stonedark'); line(60,30,60,34,'stonedark'); line(58,40,67,40,'stonedark'); line(63,36,63,39,'wooddeep')
rect(58,36,3,2,'stone2'); rect(58,43,4,2,'stone2')
# A curl of lavender smoke, cut into small wisps.
path('M 60 25 Q 56 21 60 18 Q 64 16 62 12 L 64 14 Q 66 18 62 20 Q 59 22 62 25 Z','far2')
line(60,10,62,11,'far'); line(59,9,59,7,'far')
poly([(40,72),(62,76),(62,100),(40,93)],'stonedark')
poly([(62,73),(83,41),(105,74),(105,99),(62,101)],'stone')
# Side wall courses with deliberately irregular stones.
for x,y,w,h,col in [(41,75,8,4,'stone'),(50,77,10,3,'stone2'),(41,81,6,4,'stone'),(49,82,10,4,'stone'),(42,88,8,4,'stone2'),(52,89,8,4,'stone'),(47,94,12,3,'stone')]:
    rect(x,y,w,h,col)
for x,y,w,h,col in [(64,73,8,4,'stone2'),(74,73,9,4,'stone2'),(85,72,10,4,'stone'),(97,75,6,3,'stone2'),(63,79,7,5,'stone'),(82,79,6,5,'stone2'),(101,80,3,5,'stone3'),(64,87,8,4,'stone2'),(80,87,8,4,'stone'),(99,88,5,4,'stone2'),(63,94,9,5,'stone2'),(74,94,10,4,'stone2'),(99,95,5,3,'stone2')]:
    rect(x,y,w,h,col)
# Stone nicks and dark bed joints.
for x,y in [(63,77),(82,75),(102,78),(63,92),(77,98),(85,92),(45,87),(54,94),(101,93)]:
    line(x,y,x+2,y,'stonedark')
poly([(62,73),(83,42),(104,73)],'wood')
# Vertical gable boards.
for x in range(65,103,5):
    top=round(43+abs(x-83)*1.45)
    line(x,top,x,72,'wooddeep')
    if top<70: line(x+1,top+2,x+1,71,'wood2')
line(63,73,103,73,'wooddeep'); line(65,71,101,71,'wood3')
line(63,75,63,99,'wooddeep'); line(104,75,104,98,'wooddeep')
# The broad, steeply pitched roof plane.
poly([(35,72),(61,36),(83,33),(60,77)],'roofdark')
poly([(38,70),(62,38),(79,36),(58,72)],'roof')
# Slanting courses and moss patches constrained to the roof.
roofmask = {C['roof'],C['roofdark']}
for y in range(40,74):
    for x in range(36,81):
        if c.get(x,y)==C['roof']:
            if (y+int(x*.35))%7==0:
                dot(x,y,'roofdark')
# Hand-shaped moss, spilling down in tiers.
for pts,col in [([(60,39),(71,36),(79,35),(74,42),(67,43),(66,47),(59,48),(55,53),(51,53)],'moss'), ([(60,40),(69,38),(70,40),(64,42),(62,46),(58,46)],'moss2'), ([(50,54),(58,51),(64,49),(61,55),(56,57),(54,61),(47,63),(45,63)],'moss'), ([(48,57),(54,55),(58,54),(56,57),(51,58),(50,61),(47,61)],'moss2'), ([(39,69),(46,64),(52,64),(49,69),(47,74),(40,72)],'moss'), ([(63,48),(69,44),(72,43),(69,48),(65,52),(63,53)],'moss2'), ([(55,65),(61,58),(64,57),(62,62),(58,67),(56,72),(52,74)],'moss')]:
    poly(pts,col)
for x,y in [(63,39),(67,38),(60,44),(53,55),(49,59),(43,69),(46,66),(66,47),(57,64),(54,70)]:
    line(x,y,x+2,y-1,'moss3')
# Shingle edges, little splits, and roof timbers.
for x,y in [(58,48),(55,51),(62,54),(52,61),(45,65),(58,69),(65,44),(71,40),(46,71)]:
    line(x,y,x+3,y-1,'roofdark')
line(36,72,60,77,'wooddeep'); line(37,71,59,75,'moss2')
line(60,77,83,34,'ink'); line(62,76,83,38,'wood3'); line(63,72,82,38,'moss2')
line(83,34,111,74,'ink'); line(83,37,108,73,'wood2'); line(84,37,109,72,'moss')
line(84,39,105,70,'moss2'); line(62,77,62,80,'wooddeep')
line(108,74,104,74,'wood3'); line(107,73,109,74,'moss3')
for x,y in [(41,73),(48,74),(54,75)]:
    line(x,y,x-1,y+3,'moss'); dot(x-1,y+4,'moss2')
# Attic window, amber against the weathered wooden gable.
poly([(77,65),(77,58),(82,53),(87,58),(87,65)],'wooddeep')
poly([(79,64),(79,58),(82,55),(85,58),(85,64)],'light')
line(82,56,82,64,'wooddeep'); line(79,60,85,60,'wooddeep')
line(80,57,81,56,'light3'); rect(79,61,2,2,'light2'); rect(83,61,2,2,'light2')
line(76,66,88,66,'wood3')
# Deep-set glowing front window and blue-violet stone reveal.
rect(65,76,17,17,'wooddeep'); rect(66,77,15,14,'lightdark')
rect(68,78,11,12,'light'); rect(69,79,9,10,'light2')
rect(69,79,3,4,'light3'); rect(75,79,3,4,'light3')
line(73,77,73,90,'wooddeep'); line(67,84,79,84,'wooddeep')
line(66,77,66,90,'wood3'); line(80,77,80,91,'wood2')
rect(64,92,19,2,'wooddeep'); rect(65,91,17,1,'wood3'); rect(66,94,15,1,'lightdark')
# Shutters and their diagonal braces.
rect(61,79,4,11,'wood'); line(61,79,64,89,'wood2'); line(62,79,62,89,'wooddeep')
rect(82,78,4,12,'wood'); line(82,88,85,80,'wood3'); line(84,79,84,88,'wooddeep')
# Side window with perspective-distorted muntin.
poly([(44,77),(53,79),(53,88),(44,86)],'wooddeep')
poly([(46,79),(51,80),(51,86),(46,85)],'light')
line(48,79,48,86,'wooddeep'); line(45,82,52,84,'wooddeep'); dot(46,80,'light3')
line(44,88,54,90,'wood3')
# Arched wooden door.
path('M 89 99 L 89 82 Q 94 75 100 82 L 100 99 Z','wooddeep')
path('M 91 97 L 91 83 Q 94 79 98 83 L 98 97 Z','wood')
line(93,83,93,96,'wood2'); line(96,83,96,96,'wooddeep'); line(91,91,98,91,'wooddeep')
rect(92,83,5,5,'lightdark'); rect(93,83,3,4,'light2'); line(94,83,94,87,'wooddeep')
dot(97,92,'light2'); dot(97,93,'wooddeep')
rect(88,99,14,2,'stone3'); rect(86,101,17,2,'stonedark'); rect(87,101,14,1,'stone2')
# A tiny lantern hung from the eave, with square pixel falloff.
line(104,78,108,78,'wooddeep'); line(108,78,108,81,'wooddeep')
rect(105,81,5,7,'wooddeep'); rect(106,82,3,4,'light'); rect(107,82,1,3,'light3'); rect(105,87,5,1,'wood2')

# Foreground ground-cover, with clustered blades and sparse moonlit stones.
for i in range(160):
    x=random.randint(1,126); y=random.randint(95,125)
    if c.get(x,y) in [C['ground'],C['ground2'],C['deep']]:
        col=random.choice(['grass','ground3','ground','ground2'])
        if random.random()<.6: line(x,y,x+random.choice([-2,-1,1,2]),y-2,col)
        else: line(x,y,x+2,y,col)
# A meandering path of individually laid slabs.
slabs=[([(89,104),(98,103),(100,105),(91,107),(87,106)],'path'), ([(79,107),(87,105),(91,108),(86,111),(78,110)],'path'), ([(72,113),(79,111),(86,113),(83,116),(73,117),(69,115)],'path'), ([(66,120),(72,117),(82,119),(84,122),(77,125),(64,124),(62,122)],'path'), ([(56,127),(62,125),(72,126),(76,128),(55,128)],'path')]
for pts,col in slabs:
    poly([(x,y+1) for x,y in pts],'ink'); poly(pts,col)
    a,b=pts[0],pts[1]; line(a[0],a[1],b[0],b[1],'pathlight')
line(88,105,94,104,'stone3'); line(80,107,86,106,'pathlight'); line(72,113,77,112,'stone3')
line(66,120,72,118,'pathlight'); line(65,121,70,120,'pathlight'); line(78,120,79,122,'pathdark')
line(76,113,78,115,'pathdark'); line(90,104,91,105,'pathdark')
# Warm reflected flecks near the threshold.
line(91,104,96,104,'wood3'); line(83,108,87,107,'wood2')

# The well: low elliptical stone curb, visible hollow and a timber winch.
ellipse(30,110,15,4,'deep')
poly([(17,98),(19,95),(39,95),(43,99),(42,109),(37,112),(23,112),(17,108)],'ink')
poly([(18,98),(41,98),(41,107),(36,111),(24,111),(18,107)],'stone')
poly([(18,99),(23,101),(23,109),(19,107)],'stonedark')
poly([(37,100),(41,99),(41,107),(37,109)],'stonedark')
# Curved courses and individual block faces.
line(19,104,25,106,'stonedark'); line(25,106,36,106,'stonedark'); line(36,106,41,103,'wooddeep')
line(25,101,25,105,'stonedark'); line(34,101,34,105,'stonedark'); line(29,107,29,110,'stonedark')
line(21,104,21,107,'wooddeep'); line(38,106,38,108,'wooddeep')
rect(27,102,6,3,'stone2'); rect(23,107,5,3,'stone2'); rect(30,107,5,3,'stone2')
line(26,102,32,102,'stone3'); line(30,107,34,107,'stone3'); line(19,100,22,101,'stone2')
ellipse(30,98,13,5,'stone2'); ellipse(30,98,9,3,'ink'); ellipse(30,99,8,2,'deep')
line(23,100,28,101,'mist'); line(29,102,35,101,'stone3')
line(19,97,23,95,'stone3'); line(25,94,32,94,'stone3'); line(36,95,40,97,'stone3')
line(22,95,23,97,'stonedark'); line(32,94,32,95,'stonedark'); line(38,96,36,98,'stonedark')
line(18,99,20,99,'stonedark'); line(26,101,26,103,'stonedark'); line(36,101,36,103,'stonedark')
# Uneven heavy posts, squared beam, windlass, rope and crank.
rect(18,77,4,26,'wooddeep'); rect(19,78,2,22,'wood2'); line(19,78,19,97,'wood3')
rect(39,77,4,25,'wooddeep'); rect(40,78,2,22,'wood'); line(40,79,40,98,'wood2')
poly([(16,76),(43,76),(44,79),(17,80)],'wooddeep'); line(17,76,42,76,'wood3'); line(18,77,41,77,'wood2')
line(21,83,39,83,'ink'); line(21,84,39,84,'wood3'); line(21,85,39,85,'wooddeep')
rect(27,81,7,6,'wood'); rect(28,81,5,1,'wood3')
for x in [28,30,32]: line(x,82,x,86,'stone2')
line(31,87,31,98,'wood3'); dot(31,92,'stone3')
rect(42,83,3,2,'stone2'); line(45,84,45,89,'wooddeep'); line(44,85,44,88,'stone'); rect(44,89,4,2,'wood3'); dot(47,90,'wooddeep')
line(20,80,24,83,'wooddeep'); line(38,83,41,80,'wooddeep')
# A bucket sitting beside the well.
path('M 44 104 Q 44 98 48 99 Q 52 99 51 104','stone2',False)
poly([(43,103),(52,103),(51,110),(45,110)],'wooddeep'); poly([(45,104),(51,104),(50,109),(46,109)],'wood2')
line(47,104,47,109,'wooddeep'); line(44,104,51,104,'stone2'); line(45,108,50,108,'stone')
# Ferns, roots and mushrooms anchor the foreground.
def fern(x,y,flip=1):
    line(x,y,x+flip*2,y-9,'grass')
    for n in range(3):
        yy=y-2-n*2; xx=x+flip*n//2
        line(xx,yy,xx-4+n,yy-3,'grass'); line(xx,yy,xx+4-n,yy-2,'grass2')
fern(13,119); fern(100,118,-1); fern(57,103)
for x,y in [(12,109),(17,116),(103,102),(110,113),(36,119),(91,122)]:
    line(x,y,x-2,y-4,'grass'); line(x,y,x+1,y-5,'grass'); line(x,y,x+4,y-2,'grass')
for x,y,s in [(54,114,3),(59,115,2),(106,111,3),(111,114,2)]:
    line(x,y,x,y+3,'stone3'); ellipse(x,y,s,1,'leaf3'); line(x-s+1,y-1,x+s-1,y-1,'leaf4'); dot(x-1,y-1,'moonmid')
# Fallen wine-colored leaves and tiny luminous woodland motes.
for x,y in [(5,114),(26,116),(44,120),(93,110),(100,121),(114,118),(33,125),(19,122)]:
    line(x,y,x+2,y-1,'leaf2'); dot(x+1,y,'leaf3')
for x,y in [(30,65),(35,87),(112,67),(50,98),(56,109),(91,115),(23,72)]:
    dot(x,y,'moss3')
for x,y in [(35,86),(111,66),(55,109)]: dot(x,y,'light3')
# Weathered surfaces: short chips stay inside the existing stone faces.
random.seed(38)
for i in range(65):
    x=random.randint(40,104); y=random.randint(74,99)
    base=c.get(x,y)
    if base==C['stone'] and random.random()<.7: dot(x,y,'stone2')
    elif base==C['stone2'] and random.random()<.45: dot(x,y,'stone3')
# A warm rim on the masonry directly below the windows.
line(67,95,71,95,'wood2'); line(75,95,79,95,'wood2'); dot(64,90,'wood2')
line(87,88,87,92,'wood2'); line(101,88,101,91,'wood2')
line(42,87,43,88,'wood2'); line(46,91,49,92,'wood2')
# Window reflections and a little potted silhouette in the lower pane.
rect(75,88,3,2,'lightdark'); line(76,87,76,85,'wood2'); dot(75,86,'wood2'); dot(77,85,'wood2')
# Slipped shingles and cool, moon-facing flecks in the moss.
for x,y in [(62,42),(58,46),(52,55),(49,60),(44,68),(67,45),(56,67)]:
    dot(x,y,'moss3'); dot(x+1,y,'moss2')
line(54,61,57,60,'roofdark'); line(54,62,56,61,'moss')
line(62,50,65,49,'roofdark'); line(63,51,65,50,'moss')
# Ivy climbs the cool side wall, and strands hang from the eaves.
path('M 57 97 L 55 91 L 56 86 L 54 82 L 56 77','roofdark',False)
for x,y in [(55,94),(57,92),(54,89),(56,86),(54,83),(56,79),(57,76)]:
    line(x,y,x-2,y-1,'moss'); dot(x-1,y-1,'moss2')
line(101,95,102,91,'roofdark'); line(102,91,100,88,'roofdark')
for x,y in [(101,96),(103,93),(101,90)]:
    line(x,y,x+2,y-1,'moss'); dot(x,y-1,'moss2')
# A few soft, broken ground-mist wisps; the darker gaps remain visible.
line(2,94,9,94,'far2'); line(4,95,13,95,'far2'); line(6,95,10,95,'mist')
line(47,102,52,102,'ground3'); line(49,103,55,103,'ground3')
line(106,97,115,97,'far2'); line(109,96,119,96,'far2'); line(113,96,117,96,'mist')
# Ivy and lichen patches catch the moon on the ancient trunks.
for x,y in [(9,78),(11,74),(8,83),(117,91),(119,84),(120,60)]:
    line(x,y,x+1,y-2,'moss'); dot(x,y,'moss2')
# Quiet bracken at the foot of the far wall.
for x,y in [(58,98),(61,102),(106,101)]:
    line(x,y,x-2,y-3,'moss'); line(x,y,x+2,y-2,'moss'); dot(x+1,y-3,'moss2')
# Foreground silhouetted shoots.
poly([(0,128),(0,119),(4,123),(5,117),(8,123),(12,121),(10,127),(22,128)],'ink')
poly([(108,128),(113,124),(113,119),(117,123),(120,116),(121,123),(126,119),(127,116),(127,128)],'ink')

result = c
assert tuple(result.stats()['size']) == (128,128)
assert result.stats()['colors_used'] <= 86
print(result.stats_text())
view(result)
save('magic-forest-cottage',result)
finish(result)
