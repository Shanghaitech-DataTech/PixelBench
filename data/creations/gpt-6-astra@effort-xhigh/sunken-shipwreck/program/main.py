# A small wreck resting in the blue-green shallows.
result = new_canvas(64, 64, background='#123f50', name='sunken_shipwreck')
c = result
P = {
 'water0':'#287b87','water1':'#236e7d','water2':'#1c606f','water3':'#185362','water4':'#144958','water5':'#123f50',
 'ray0':'#308490','ray1':'#2a7885','ray2':'#246a79','ray3':'#205d6c',
 'deep':'#102f3c','ink':'#102d34','shadow':'#173c41','silt':'#265b60',
 'sand0':'#638c80','sand1':'#7c9c87','sand2':'#a6b294','sand3':'#c4c3a0','sandshade':'#416e6a',
 'wood0':'#3b4940','wood1':'#595b47','wood2':'#7d7350','wood3':'#a18c5f','wood4':'#c0a373','split':'#293c37',
 'algae0':'#245b52','algae1':'#3a7b65','algae2':'#6b9673','algae3':'#8aaf87',
 'coral0':'#864d59','coral1':'#ba6b68','coral2':'#e69b83',
 'fish0':'#c28e62','fish1':'#efc483','fish2':'#ffe1a0','bluefish':'#7eb9ad','bubble':'#6ca3a7'
}
def r(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def l(x,y,X,Y,col): c.line(x,y,X,Y,P.get(col,col))
def p(points,col): c.poly(points,P.get(col,col))
def s(x,y,col): c.set(x,y,P.get(col,col))
# Deepening water, with deliberately stepped shafts of light.
r(0,0,64,8,'water0'); r(0,8,64,9,'water1'); r(0,17,64,10,'water2'); r(0,27,64,12,'water3'); r(0,39,64,10,'water4')
for pts,col in [([(4,0),(12,0),(17,8),(8,8)],'ray0'), ([(8,8),(17,8),(23,17),(13,17)],'ray1'), ([(13,17),(23,17),(29,27),(19,27)],'ray2'), ([(19,27),(29,27),(34,38),(27,38)],'ray3'), ([(21,0),(24,0),(29,8),(25,8)],'ray0'), ([(25,8),(29,8),(34,17),(30,17)],'ray1'), ([(30,17),(34,17),(40,27),(36,27)],'ray2')]: p(pts,col)
# Soft far-away bottom contours and rocks.
p([(0,46),(8,44),(17,46),(25,45),(36,47),(47,44),(55,44),(63,46),(63,63),(0,63)],'silt')
p([(0,50),(9,47),(20,49),(32,48),(46,47),(56,46),(63,48),(63,63),(0,63)],'sandshade')
p([(0,53),(9,50),(22,52),(37,50),(47,49),(55,48),(63,51),(63,63),(0,63)],'sand0')
# Distant weed silhouettes.
for pts in [[(1,47),(2,36),(5,32),(4,39),(4,47)],[(5,48),(7,40),(6,35),(8,39),(8,45)],[(56,46),(55,35),(57,29),(57,38),(58,46)],[(59,48),(60,39),(63,35),(61,42),(61,48)]]: p(pts,'silt')
# Shadow beneath the timbers.
c.ellipse(32,49,24,5,P['sandshade'])
c.ellipse(32,48,20,3,P['shadow'])
# Broken mast, its light edge and a hanging old line.
l(28,35,23,15,'ink'); l(29,35,24,16,'wood1'); l(30,34,25,17,'wood2')
l(29,31,25,20,'wood3'); s(24,15,'wood3'); s(25,16,'wood0')
l(19,23,36,20,'ink'); l(20,22,34,20,'wood2'); l(22,22,29,21,'wood3')
s(35,21,'wood1'); s(19,22,'wood0')
# A scrap of sail, torn away at the bottom.
p([(28,23),(32,23),(33,26),(36,30),(32,29),(32,31),(29,27)],'silt')
l(28,23,30,27,'sandshade'); s(31,25,'sand0')
l(34,22,38,32,'silt'); l(38,32,41,35,'silt')
# Complete broken silhouette: raised stern, curved belly, upswept bow.
p([(9,28),(13,28),(14,30),(18,31),(20,33),(24,33),(25,31),(27,32),(27,34),(34,34),(35,32),(38,34),(42,34),(44,32),(47,33),(52,29),(56,29),(55,35),(53,42),(49,47),(41,51),(24,52),(16,49),(12,44),(10,37)],'ink')
# Back edge of the open deck.
p([(12,30),(17,32),(22,35),(29,35),(36,36),(43,35),(49,33),(53,31),(52,37),(44,40),(23,40),(15,36)],'wood1')
l(14,31,22,34,'wood3'); l(22,34,26,34,'wood2'); l(37,35,43,34,'wood2')
# Empty hold and broken cross-beams visible from above.
p([(15,33),(22,36),(34,37),(45,36),(51,33),(48,39),(39,42),(22,40),(17,37)],'deep')
l(20,34,23,40,'wood0'); l(21,35,24,40,'wood2')
l(32,36,31,41,'wood1'); s(32,36,'wood3')
l(44,35,41,41,'wood1'); l(45,35,42,40,'wood3')
# Broad near side of the hull.
p([(11,34),(15,37),(22,39),(32,40),(42,39),(50,36),(54,32),(52,41),(48,46),(40,49),(25,50),(17,47),(13,42)],'wood1')
p([(14,40),(23,43),(35,44),(47,41),(52,37),(50,43),(44,48),(36,50),(25,50),(18,47)],'wood0')
# Courses of weathered wood; each follows the hull curvature.
l(12,35,18,39,'wood3'); l(18,39,28,41,'wood2'); l(28,41,39,41,'wood2'); l(39,41,49,38,'wood3'); l(49,38,53,34,'wood3')
l(14,40,22,43,'split'); l(22,43,36,44,'split'); l(36,44,47,41,'split'); l(47,41,51,38,'split')
l(15,41,23,44,'wood2'); l(24,45,35,45,'wood1'); l(36,45,46,42,'wood2'); l(47,42,50,39,'wood2')
l(19,46,27,48,'wood1'); l(28,48,37,48,'split'); l(38,48,45,45,'wood1')
# Heavy ribs and the two splintered ends.
l(11,30,12,37,'wood3'); l(12,38,15,44,'wood2'); l(15,44,18,47,'wood1')
l(17,38,19,44,'split'); l(18,38,20,44,'wood3'); l(20,45,23,48,'wood2')
l(26,41,27,47,'split'); l(27,41,28,47,'wood2'); s(28,48,'wood1')
l(38,41,37,46,'split'); l(39,41,38,46,'wood3'); s(38,47,'wood2')
l(48,38,46,44,'split'); l(49,38,47,44,'wood3')
l(53,31,51,38,'wood4'); s(54,30,'wood3'); s(10,29,'wood4'); s(12,30,'wood4')
# Breached, jagged planking on the side.
p([(30,42),(33,41),(35,42),(35,45),(34,45),(34,47),(30,47),(29,45)],'ink')
s(30,42,'wood3'); s(33,41,'wood2'); l(30,47,33,47,'wood2'); s(34,46,'wood0')
r(21,40,3,2,'ink'); s(22,42,'ink'); s(21,39,'wood4'); s(24,41,'wood3')
# A few pale splinters and dark checks break up the old planking.
l(14,38,16,39,'wood4'); l(28,41,31,41,'wood3'); l(40,42,43,41,'wood3')
l(20,44,23,45,'split'); s(24,45,'wood3'); l(41,46,43,45,'split')
s(19,32,'wood3'); l(18,31,18,33,'wood0'); l(35,33,36,35,'wood3')
# Marine corrosion, barnacles and algae clinging to the wood.
for x,y in [(13,36),(14,37),(15,37),(16,38),(16,39),(24,43),(25,44),(40,39),(41,39),(42,38),(43,38),(44,38),(50,35),(50,36),(45,44),(44,45),(42,46),(21,47),(23,48),(24,48),(35,48)]: s(x,y,'algae1')
for x,y in [(13,35),(15,36),(24,42),(41,38),(43,37),(49,35),(44,44),(23,47)]: s(x,y,'algae2')
for x,y in [(16,41),(25,46),(40,44),(45,40),(50,37)]: s(x,y,'sand2')
s(16,42,'wood0'); s(40,45,'wood0'); s(45,41,'wood0')
# Sand banks overlap and bury the keel.
p([(0,54),(7,52),(14,52),(18,51),(22,50),(28,51),(36,51),(44,49),(50,49),(56,51),(63,53),(63,64),(0,64)],'sand1')
p([(0,58),(11,56),(20,56),(28,54),(37,54),(47,52),(53,53),(61,56),(63,56),(63,64),(0,64)],'sand2')
l(19,51,25,51,'sand2'); l(26,52,34,52,'sand2'); l(37,51,43,50,'sand2'); l(45,50,49,50,'sand2')
p([(0,61),(11,59),(20,60),(31,58),(41,58),(49,57),(57,60),(63,60),(63,64),(0,64)],'sand1')
l(5,56,11,55,'sand3'); l(12,55,17,55,'sand3'); l(34,56,41,55,'sand3'); l(43,54,49,54,'sand3'); l(52,55,56,55,'sand3')
# Fallen timber half hidden in the foreground.
p([(23,56),(25,55),(36,59),(34,60)],'wood0')
l(25,56,34,59,'wood3'); l(29,58,33,59,'wood2'); s(25,57,'sand2'); s(35,59,'sand1')
# Seagrass with bent, ribbonlike leaves.
for pts in [[(6,54),(4,49),(4,43),(3,39),(5,42),(6,49),(7,53)],[(7,54),(7,45),(10,40),(10,44),(9,47),(9,53)],[(8,53),(10,48),(13,46),(11,49),(10,54)],[(55,53),(53,48),(53,42),(51,38),(54,40),(55,46),(56,51)],[(56,53),(57,47),(56,42),(58,38),(58,44),(59,48),(58,53)],[(57,54),(60,48),(62,46),(61,50),(59,54)]]: p(pts,'algae0')
l(5,44,5,49,'algae1'); l(6,50,7,53,'algae2'); l(8,48,9,44,'algae2'); l(10,42,10,43,'algae3'); l(54,42,54,47,'algae1'); l(55,48,56,52,'algae2'); l(58,45,58,48,'algae1'); l(58,52,60,49,'algae2')
# Branching coral at both edges.
def branch(points, col):
 for (x,y),(X,Y) in zip(points,points[1:]): l(x,y,X,Y,col)
for pts in [[(3,57),(3,48),(1,46),(1,43)],[(3,52),(6,49),(6,46)],[(3,49),(4,46),(4,43)],[(3,55),(1,53),(0,51)],[(61,56),(60,52),(61,48),(60,45)],[(61,52),(63,50),(63,47)],[(61,55),(58,52),(58,49)]]: branch(pts,'coral0')
for pts in [[(2,56),(2,49),(0,47),(0,44)],[(2,52),(5,49),(5,46)],[(2,49),(3,46),(3,43)],[(60,56),(59,52),(60,48),(59,45)],[(60,52),(62,50),(62,47)],[(60,55),(57,52),(57,49)]]: branch(pts,'coral1')
for x,y in [(0,44),(3,43),(5,46),(2,50),(59,45),(62,47),(57,49),(59,53)]: s(x,y,'coral2')
# Little pebbles, shells and sparse grains of sand.
for x,y in [(10,58),(18,60),(41,60),(47,57),(53,62),(60,58),(4,61),(39,53),(15,53),(30,62)]:
 s(x,y,'sandshade'); s(x+1,y,'sand0')
for x,y in [(8,60),(17,57),(21,59),(37,62),(45,58),(51,59),(56,57),(12,62),(28,54),(4,58)]: s(x,y,'sand3')
r(44,59,3,1,'sand3'); s(45,58,'sand3'); s(45,60,'sand0')
# The school swims to the left, lit warm against cool open water.
def fish(x,y,scale=1, pale=False):
 mid='bluefish' if pale else 'fish1'
 shade='sand0' if pale else 'fish0'
 if scale==1:
  s(x+4,y,shade); r(x+5,y,1,2,shade); r(x+6,y-1,1,4,mid)
  r(x,y,4,2,mid); r(x+1,y-1,2,1,'fish2' if not pale else 'bubble'); r(x+1,y+2,2,1,shade)
  s(x+1,y,'ink'); s(x,y+1,'fish2' if not pale else 'bubble')
 else:
  s(x,y,mid); s(x+1,y,mid); s(x+3,y-1,shade); s(x+3,y,shade); s(x+2,y,shade)
fish(42,12); fish(52,16); fish(39,19); fish(48,23); fish(57,26,0); fish(51,8,0,True); fish(58,11,0,True)
fish(6,24,0,True); fish(1,28,0,True)
# Tiny suspended motes and bubbles rising from the hold.
for x,y in [(4,7),(18,5),(37,7),(59,4),(9,16),(15,26),(4,34),(46,28),(59,33),(35,15),(20,11)]: s(x,y,'ray1')
for x,y in [(32,16),(35,10),(31,28)]:
 s(x,y,'bubble'); s(x+1,y-1,'bubble'); s(x+2,y,'silt'); s(x+1,y+1,'silt')
s(33,23,'bubble'); s(30,12,'ray0')
view(result, scale=8, margin=0)
save('sunken_shipwreck', result)
finish(result)
