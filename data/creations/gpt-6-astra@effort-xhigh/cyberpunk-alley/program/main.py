import random
random.seed(17)

# A compact, shared palette: blue-black masonry, fuchsia, mint and sodium light.
P = {
 'ink':'#080c1b', 'deep':'#101426', 'void':'#121a2d', 'sky':'#19243b',
 'far':'#223149', 'far2':'#2b4055', 'wall':'#202039', 'wallL':'#29253e',
 'wallHi':'#35334d', 'plum':'#432941', 'steel':'#344657', 'slate':'#42556a',
 'blue':'#26405c', 'blueHi':'#355a74', 'tealD':'#153a48', 'teal':'#205767',
 'tealHi':'#347d88', 'cyan':'#56c9cd', 'ice':'#a4f5e4', 'white':'#e7fff0',
 'purp':'#472e60', 'violet':'#67417e', 'lav':'#9b6bba', 'pinkD':'#662b57',
 'pinkM':'#a4376a', 'pink':'#ec4c95', 'pinkHi':'#ff88bc', 'pinkLit':'#ffd0dc',
 'redD':'#663542', 'rust':'#8c494b', 'red':'#dd655d', 'amberD':'#654448',
 'amberM':'#a36353', 'amber':'#edac70', 'cream':'#ffe2a1', 'road':'#161e32',
 'roadHi':'#202b40', 'roadBlue':'#293d50', 'puddle':'#1a3041',
 'glass0':'#1e3449', 'glass1':'#29465a', 'glass2':'#365a6c',
 'glass3':'#4b7786', 'glass4':'#6b9aa5', 'glass5':'#97c6c8',
}
c = new_canvas(128,128,P['ink'],name='Rain on Neon Lane')
def R(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def L(x,y,xx,yy,k): c.line(x,y,xx,yy,P.get(k,k))
def S(x,y,k): c.set(x,y,P.get(k,k))
def Q(pts,k): c.poly(pts,P.get(k,k))
def path(d,k,fill=True): c.path(d,P.get(k,k),fill=fill)

# A narrow piece of sky above the receding canyon.
R(32,0,68,66,'sky')
Q([(43,0),(51,0),(51,16),(58,16),(58,8),(68,8),(68,23),(75,23),(75,0),(90,0),(91,70),(39,70)],'far')
R(52,24,14,39,'void'); R(67,32,16,37,'far2')
R(73,28,5,5,'far2'); L(75,27,75,19,'steel')
R(57,19,3,5,'void')
for x,y,w,k in [(54,29,3,'blueHi'),(60,36,2,'steel'),(54,43,3,'teal'),(69,39,2,'tealHi'),(77,39,2,'teal'),(69,46,2,'teal'),(77,47,2,'blueHi'),(56,52,3,'tealHi')]: R(x,y,w,2,k)
# Back entrance and an amber light deep in the lane.
R(60,54,15,22,'blue'); R(63,58,8,16,'deep')
R(64,59,6,10,'amberM'); R(65,60,4,8,'amber')
R(64,68,6,6,'amberD'); R(62,56,11,2,'amberD'); R(63,56,9,1,'cream')
R(56,65,4,9,'tealD'); L(57,67,57,73,'teal')

# Left building: broad silhouette and stepped perspective edge.
Q([(0,0),(35,0),(35,16),(42,19),(42,59),(47,63),(47,82),(27,107),(0,114)],'wall')
Q([(0,0),(27,0),(27,100),(0,116)],'wallL')
R(0,10,26,2,'wallHi'); R(0,13,26,2,'deep')
R(4,0,2,39,'plum'); R(23,0,2,27,'deep')
R(7,17,15,19,'ink'); R(8,18,13,16,'blue')
R(9,19,5,5,'tealD'); R(16,19,4,5,'teal')
R(9,27,5,5,'teal'); R(16,27,4,5,'blueHi')
L(15,18,15,34,'ink'); L(8,25,20,25,'ink')
R(6,35,17,2,'wallHi')
# Building seam and plumbing.
L(30,4,30,28,'deep'); L(31,4,31,28,'wallHi')
L(25,40,25,63,'rust'); L(26,40,26,63,'plum')
Q([(39,60),(45,63),(45,83),(40,90)],'plum')
L(43,66,43,83,'pinkD'); L(40,63,40,88,'pinkM')
# Small inset shutter down the alley.
Q([(30,69),(39,65),(39,88),(30,96)],'deep')
for y in range(71,93,3): L(31,y,37,y-3,'wallHi')
L(38,66,38,87,'pinkD')

# Right facade with inset windows, industrial ducts and a deep doorway.
Q([(92,0),(128,0),(128,117),(95,98),(84,76),(84,49),(90,45)],'deep')
Q([(103,0),(128,0),(128,120),(111,111),(104,64)],'wall')
Q([(89,24),(101,20),(101,66),(88,62)],'blue')
Q([(92,27),(98,25),(98,43),(91,45)],'ink')
L(92,31,97,29,'tealD'); L(91,39,97,37,'teal')
L(101,0,101,30,'steel'); L(102,0,102,30,'void')
R(108,3,17,16,'ink'); R(110,5,13,12,'wallHi')
for yy in range(6,17,3): R(111,yy,11,1,'deep')
R(108,19,18,2,'steel')
R(119,22,4,40,'void'); L(119,22,119,61,'wallHi')
R(118,25,6,2,'steel'); R(118,54,6,2,'steel')
Q([(85,56),(97,57),(98,88),(87,80)],'tealD')
Q([(87,59),(95,60),(95,83),(87,78)],'ink')
L(86,58,86,79,'tealHi')
R(105,45,13,16,'void')
for y in range(47,60,3): R(106,y,11,1,'wallHi')
R(107,63,18,2,'steel')

# Selective masonry wear: quiet clusters stay within the existing wall planes.
wall_idx = {c.color(P[k]):k for k in ['wall','wallL','deep','blue']}
for x,y,w,k,base in [
 (1,3,8,'plum','wallL'),(10,6,11,'wallHi','wallL'),(0,21,5,'wallHi','wallL'),
 (1,29,4,'plum','wallL'),(3,39,11,'plum','wallL'),(17,39,5,'wallHi','wallL'),
 (27,19,5,'wallHi','wall'),(27,22,2,'plum','wall'),(29,8,4,'wallHi','wall'),
 (28,16,5,'deep','wall'),(29,63,7,'plum','wall'),(30,67,5,'wallHi','wall'),
 (105,25,8,'wallHi','wall'),(108,22,8,'plum','wall'),(125,25,3,'wallHi','wall'),
 (104,46,2,'steel','wall'),(124,48,4,'wallHi','wall'),(121,58,6,'plum','wall'),
 (105,61,11,'plum','wall'),(91,4,6,'wallHi','deep'),(89,18,9,'wall','deep'),
 (90,14,2,'wallHi','deep'),(95,21,3,'steel','deep')]:
    for xx in range(x,min(128,x+w)):
        if c.get(xx,y)==c.color(P[base]): S(xx,y,k)
# Thin mortar edges and patchwork repairs.
L(0,8,7,8,'deep'); L(9,9,9,10,'deep'); L(17,3,25,3,'deep')
L(0,26,5,26,'deep'); L(2,24,2,25,'deep')
R(28,8,3,7,'void'); R(28,9,1,4,'steel')
R(107,56,4,5,'wallHi'); R(108,57,2,3,'steel')
L(125,24,127,24,'deep'); L(126,25,126,28,'deep')
# Two small service placards and bundled conduit on the right.
R(87,64,5,7,'wallHi'); R(88,65,3,4,'amberD'); R(88,66,2,1,'amber')
L(125,46,125,66,'ink'); L(126,46,126,65,'slate')
R(124,61,4,2,'deep')

# Overhead cables: dark weight with small cold highlights on rain-wet edges.
path('M0 5 Q42 28 96 8 Q111 4 127 6','ink',False)
path('M0 7 Q46 33 97 10 Q114 5 127 8','steel',False)
path('M0 8 Q45 34 96 11 Q114 6 127 9','ink',False)
path('M20 0 Q30 41 89 30 Q112 26 127 19','ink',False)
path('M32 0 Q34 42 95 37 Q110 36 127 29','ink',False)
path('M0 39 Q42 49 88 33','ink',False)
L(48,20,48,31,'ink'); R(46,31,5,3,'deep'); R(47,34,3,1,'amber')
L(80,30,80,36,'ink'); R(79,36,3,2,'tealHi')
# Clamped cable loops and junction box.
R(2,37,5,6,'deep'); R(3,38,3,3,'steel')
path('M3 43 Q10 50 5 55 L5 62','ink',False)

# Neon shop signs: dark casings and sharply separated luminous tubes.
# Vertical noodle-shop blade.
R(32,23,14,37,'ink'); R(33,24,12,35,'pinkD')
R(34,25,10,33,'deep'); L(33,25,33,57,'pink')
L(35,24,43,24,'pinkHi'); L(44,25,44,58,'pink')
L(35,59,43,59,'pinkM')
c.text(33,28,'夜',P['pinkLit'],font='12px')
c.text(33,43,'食',P['pinkHi'],font='12px')
R(29,29,3,2,'ink'); R(29,52,3,2,'ink')
# Main front horizontal sign.
R(0,43,31,13,'pinkD'); R(0,44,30,11,'ink')
L(0,44,28,44,'pink'); L(0,54,29,54,'pinkHi')
c.text(1,46,'RAMEN',P['pinkLit'])
R(2,56,27,2,'plum')
# Far motel sign.
R(77,45,16,10,'tealD'); R(78,46,14,8,'ink')
L(78,45,92,45,'cyan'); L(92,46,92,53,'tealHi')
c.text(79,47,'IN',P['ice'])
L(94,46,100,45,'ink')
# Right hand 24-hour sign, with a glowing canopy beneath.
R(99,27,28,14,'tealD'); R(101,28,26,12,'cyan')
R(102,29,24,10,'deep'); c.text(106,31,'24H',P['ice'])
R(103,41,22,1,'tealHi'); R(105,43,19,1,'blue')

# Foreground noodle counter, beneath a striped awning.
R(0,64,27,38,'ink'); R(1,67,24,28,'amberD')
R(2,68,21,23,'amberM'); R(3,70,19,19,'amber')
R(3,70,9,7,'cream'); R(14,70,8,7,'amber')
# Interior shelves, mullions, and small stacked bowls.
L(2,79,22,79,'amberD'); L(12,68,12,91,'plum')
R(4,82,6,2,'cream'); R(5,84,4,1,'amberD')
R(15,82,6,2,'cream'); R(16,84,4,1,'amberD')
R(4,88,17,2,'rust'); R(1,92,25,3,'plum')
R(1,92,23,1,'red'); R(2,96,21,7,'deep')
for x in [5,11,17,23]: L(x,97,x,102,'wall')
R(0,103,26,3,'ink'); L(0,104,25,104,'pinkD')
Q([(0,58),(26,58),(31,65),(0,65)],'plum')
for x in [1,9,17,25]: Q([(x,58),(x+3,58),(min(x+6,31),65),(x+2,65)],'redD')
L(0,65,30,65,'pinkM'); R(0,66,30,2,'ink')
# A paper menu and a tiny exterior lamp.
R(26,73,3,9,'amberD'); R(26,74,2,6,'amber')
R(29,62,2,3,'pinkHi')

# Wet lane; masonry gives way to long, converging curb lines.
Q([(57,74),(76,74),(104,98),(128,118),(128,128),(0,128),(0,112),(34,91)],'road')
Q([(57,75),(61,75),(25,128),(0,128),(0,113)],'roadHi')
Q([(77,76),(80,77),(128,116),(128,128),(113,128)],'roadHi')
L(49,86,15,127,'wallHi'); L(46,90,4,122,'deep')
L(82,84,116,127,'steel'); L(84,84,124,127,'ink')
# Broad calm puddles catch soft fields of reflected neon.
Q([(37,97),(55,89),(51,102),(62,110),(55,116),(66,123),(62,128),(16,128),(22,120),(37,114),(27,111)],'pinkD')
Q([(84,89),(94,95),(92,103),(108,111),(102,119),(120,128),(82,128),(85,118),(76,115),(84,107),(78,102)],'tealD')
Q([(61,78),(68,78),(70,86),(65,94),(74,104),(66,108),(57,102),(62,93),(58,88)],'amberD')
Q([(28,112),(40,107),(55,111),(59,117),(52,122),(32,124),(20,122)],'puddle')
Q([(77,118),(96,114),(111,119),(107,126),(72,126)],'puddle')
# Reflections are horizontal broken strokes that broaden toward the viewer.
for x,y,w,k in [
 (61,79,6,'amberM'),(59,82,9,'amber'),(62,84,4,'cream'),(58,87,9,'amberM'),
 (56,92,8,'amberD'),(58,96,13,'amberM'),(59,99,6,'amber'),(55,104,9,'amberD'),
 (43,90,5,'pinkM'),(41,94,8,'pink'),(38,97,11,'pinkM'),(42,99,5,'pinkHi'),
 (34,102,10,'pinkM'),(38,104,12,'pink'),(29,107,14,'pinkD'),(36,109,13,'pinkM'),
 (32,113,8,'pink'),(42,115,12,'pinkD'),(24,118,13,'pinkM'),(32,120,14,'pink'),
 (18,124,17,'pinkD'),(40,124,13,'pinkM'),(47,126,12,'pinkD'),
 (83,90,5,'teal'),(84,94,9,'tealHi'),(88,96,7,'cyan'),(81,100,8,'teal'),
 (87,103,10,'cyan'),(90,105,6,'ice'),(82,108,17,'tealHi'),(88,110,14,'cyan'),
 (99,113,7,'teal'),(85,116,12,'tealHi'),(94,119,16,'cyan'),(83,121,10,'teal'),
 (88,124,22,'tealHi'),(101,126,14,'cyan'),(78,127,10,'teal'),
 (5,111,10,'amberD'),(3,114,13,'amberM'),(8,117,7,'amber'),(0,121,10,'redD'),
 (1,125,11,'amberM'),(118,120,7,'blueHi'),(119,124,8,'steel')]:
    R(x,y,w,1,k)
# Broken reflection clusters: small patches cut the broad mirrored light fields.
for yy in range(94,128,2):
    for xx in range(3,126,3):
        idx=c.get(xx,yy)
        if idx == c.color(P['pinkD']) and random.random()<0.31:
            R(xx,yy,random.choice([2,3,5,7]),1,random.choice(['road','roadHi','pinkM']))
        elif idx == c.color(P['tealD']) and random.random()<0.27:
            R(xx,yy,random.choice([2,3,4]),1,random.choice(['road','teal','tealHi']))
        elif idx == c.color(P['road']) and random.random()<0.08:
            R(xx,yy,2,1,'roadBlue')
# Small ripples, always horizontal, and submerged paving joints.
for x,y,k in [(35,116,'pinkM'),(99,115,'tealHi'),(73,122,'blueHi'),(16,118,'steel'),(53,94,'slate'),(85,112,'cyan'),(50,123,'pinkM')]:
    L(x-3,y,x+3,y,k); S(x-4,y-1,k); S(x+4,y-1,k); L(x-1,y+2,x+2,y+2,'roadBlue')
L(17,111,28,110,'deep'); L(3,127,15,125,'ink'); L(108,113,119,112,'ink')
R(4,108,18,2,'deep')
for x in range(6,22,3): S(x,108,'steel')

# Pair of vending machines: cyan drinks on the left, violet snacks on the right.
Q([(95,68),(113,68),(116,72),(116,107),(95,106)],'ink')
R(95,69,17,36,'blueHi'); R(96,70,15,34,'teal')
Q([(112,70),(115,72),(115,107),(112,105)],'blue')
L(95,70,95,104,'cyan'); R(97,71,13,4,'ice')
R(99,72,8,1,'cyan')
R(97,77,11,18,'ink'); R(98,78,9,16,'tealD')
for yy in [79,86]:
    for xx,col in [(99,'ice'),(102,'cyan'),(105,'amber')]:
        R(xx,yy+1,2,4,col); S(xx,yy,'steel'); S(xx,yy+4,'tealHi')
    R(98,yy+6,9,1,'blueHi')
R(109,79,2,8,'deep'); S(109,80,'pinkHi'); R(109,84,1,2,'ice')
R(98,97,10,5,'ink'); R(99,98,8,1,'blueHi'); R(99,101,7,1,'tealHi')
R(97,105,3,2,'ink'); R(109,105,4,2,'ink')
# Right machine partly cropped, with chunky reflected panels.
R(116,70,12,39,'ink'); R(117,71,11,36,'purp')
L(117,72,117,105,'lav'); R(119,73,8,4,'pink')
R(120,74,6,1,'pinkLit'); R(119,79,8,16,'deep')
for yy in [81,87]:
    R(120,yy,2,4,'amber'); R(124,yy,2,4,'pinkHi'); R(120,yy+4,6,1,'violet')
R(119,98,8,5,'ink'); R(120,98,6,1,'violet'); R(118,107,10,2,'deep')
L(96,109,108,109,'tealHi'); L(117,111,126,111,'pinkD')
# A low curb-side crate away from the person's silhouette.
Q([(29,94),(35,91),(40,93),(40,101),(31,105),(29,103)],'ink')
Q([(30,95),(35,93),(38,94),(33,97)],'steel')
Q([(31,98),(39,95),(39,100),(31,103)],'wallHi')
L(33,98,33,101,'deep'); L(36,97,36,100,'deep')

# Rain: sparse short groups preserve large readable areas of darkness.
for x,y,length,k in [
 (6,2,3,'slate'),(17,7,4,'steel'),(46,3,4,'blueHi'),(63,2,3,'slate'),(86,8,5,'blueHi'),
 (117,1,3,'steel'),(53,14,4,'blueHi'),(72,16,3,'slate'),(10,36,3,'steel'),(24,26,3,'slate'),
 (49,40,4,'blueHi'),(64,34,3,'slate'),(83,23,4,'blueHi'),(114,23,3,'teal'),(124,46,4,'slate'),
 (5,57,3,'pinkM'),(52,54,3,'tealHi'),(74,56,4,'slate'),(82,62,3,'cyan'),(55,63,3,'blueHi'),
 (91,59,3,'tealHi'),(111,53,3,'steel'),(17,59,2,'pinkM'),(8,95,3,'amberM'),
 (21,109,3,'slate'),(47,89,3,'pinkM'),(88,88,3,'tealHi'),(121,60,3,'steel'),
 (92,117,3,'cyan'),(10,119,2,'slate'),(79,107,3,'blueHi'),(56,113,2,'slate'),(115,116,2,'teal')]:
    L(x,y,x-1,y+length,k)

# Single walker, with black separated legs and a coherent coat silhouette.
c.ellipse(67,117,11,1,P['ink'])
L(58,118,69,118,'roadBlue'); L(68,119,76,119,'roadBlue')
# Legs: one planted, one taking the next step.
Q([(61,101),(67,102),(66,110),(64,115),(59,115),(60,112)],'ink')
Q([(67,101),(72,101),(72,107),(76,112),(75,114),(71,114),(67,108)],'ink')
L(60,111,60,114,'violet'); R(58,115,7,2,'ink'); S(58,115,'pinkM')
R(73,113,5,2,'ink'); L(74,112,76,113,'tealHi')
# Coat and arm lifted to the handle.
Q([(63,89),(68,89),(72,92),(72,97),(75,105),(69,107),(59,105),(60,98),(59,94)],'ink')
Q([(62,91),(65,92),(64,100),(62,104),(59,104),(61,97)],'wall')
L(60,93,59,99,'pinkM'); L(59,100,59,103,'pinkD')
Q([(69,92),(71,95),(74,91),(74,88),(72,88),(71,91)],'void')
L(74,89,74,92,'cyan'); L(70,100,73,104,'blueHi')
# Head, short hair, a small warm facial edge and turned collar.
R(63,83,6,6,'ink'); R(62,84,1,3,'ink')
R(68,85,2,3,'amberD'); S(69,85,'amber'); R(65,89,3,2,'plum')
L(63,90,67,91,'pinkD'); S(63,85,'violet')
# Umbrella shaft and curled grip, behind the hand.
L(72,74,72,94,'steel'); L(73,81,73,89,'cyan')
path('M72 92 L72 95 Q70 97 69 94','tealHi',False)
R(72,89,2,2,'amber')

# Transparent canopy: remap background to six glass tones while retaining details.
canopy = new_canvas(128,128,name='canopy mask')
dome = 'M44 81 Q48 73 56 71 Q63 68 68 69 Q80 70 87 81 Q82 78 77 81 Q71 79 65 82 Q58 79 52 82 Q47 80 44 81 Z'
canopy.path(dome,'#ffffff')
indices = {entry['index']:entry['rgba'] for entry in c.palette()}
for yy in range(68,83):
    for xx in range(43,89):
        if canopy.get(xx,yy) != canopy.get(0,0):
            r,g,b,a=indices[c.get(xx,yy)]
            lum=(r*2+g*4+b)/7
            lev=0 if lum<25 else 1 if lum<48 else 2 if lum<76 else 3 if lum<112 else 4 if lum<160 else 5
            S(xx,yy,'glass'+str(lev))
# Thin wet perimeter and visible ribs explain the clear material.
path('M44 81 Q48 73 56 71 Q63 68 68 69 Q80 70 87 81','cyan',False)
path('M45 81 Q48 79 52 82 Q58 79 65 82 Q71 79 77 81 Q82 78 86 81','glass3',False)
path('M66 70 Q57 72 52 81 M66 70 Q65 75 65 81 M66 70 Q74 73 77 80','glass3',False)
L(65,67,65,69,'ice'); L(54,72,59,70,'ice'); L(70,70,75,72,'ice')
L(45,79,47,77,'pinkHi'); S(44,81,'pinkLit'); S(87,81,'ice')
S(51,74,'white'); S(79,75,'ice'); S(57,77,'glass5'); S(72,76,'glass4')
L(46,83,46,84,'cyan'); S(86,84,'cyan')
# Long foreground rain catches neon only where it passes a light source.
for x,y,length,k in [
 (3,16,5,'wallHi'),(20,2,5,'slate'),(37,6,4,'blueHi'),(57,6,5,'steel'),
 (78,2,5,'blueHi'),(94,2,4,'steel'),(110,7,4,'slate'),(125,11,5,'steel'),
 (15,24,5,'tealHi'),(28,31,4,'pinkM'),(48,26,5,'blueHi'),(61,22,5,'blueHi'),
 (71,30,5,'slate'),(84,40,3,'teal'),(96,35,4,'tealHi'),(115,47,4,'tealHi'),
 (2,74,4,'amber'),(14,91,3,'amber'),(24,82,5,'rust'),(35,77,4,'pinkM'),
 (48,59,5,'blueHi'),(60,46,4,'steel'),(72,62,3,'tealHi'),(80,57,5,'tealHi'),
 (91,72,5,'cyan'),(109,61,5,'tealHi'),(121,91,4,'lav'),
 (7,100,5,'slate'),(17,98,5,'slate'),(27,107,4,'pinkM'),(49,101,5,'pinkM'),
 (54,87,4,'slate'),(82,95,4,'tealHi'),(91,109,4,'cyan'),(116,101,4,'tealHi'),
 (125,114,5,'tealHi'),(56,120,4,'steel'),(79,116,4,'slate'),(5,117,4,'steel')]:
    L(x,y,x-1,y+length,k)
# A few tiny surface highlights keep the umbrella looking like clear vinyl.
S(49,77,'glass5'); S(62,72,'ice'); L(81,77,82,78,'glass5')
L(51,83,51,85,'glass4'); S(77,83,'glass5')
# Last foreground raindrops and ground shine, kept clear of the walker.
for x,y in [(5,126),(25,113),(47,119),(83,124),(110,118),(36,96)]:
    S(x,y,'slate'); L(x-1,y+1,x+1,y+1,'blueHi')

result = c
print(result.stats_text())
view(result,scale=4,margin=0)
save('cyberpunk-alley',result)
finish(result)
