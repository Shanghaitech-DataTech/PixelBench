result = new_canvas(64,64,background='#092c43',name='sunken_shipwreck')
c=result
# Restrained marine palette and broad depth bands.
c.rect(0,0,64,12,'#164c61')
c.rect(0,12,64,14,'#114457')
c.rect(0,26,64,16,'#0d394e')
c.poly([(5,0),(13,0),(30,45),(21,48)],'#195365')
c.poly([(26,0),(30,0),(43,40),(38,43)],'#174c5e')
c.poly([(48,0),(51,0),(60,32),(56,34)],'#174c5e')
# Far-off seabed silhouettes.
c.poly([(0,42),(10,40),(23,44),(36,40),(49,43),(63,39),(63,57),(0,57)],'#174653')
c.path('M 3 46 Q 0 38 4 31 Q 2 41 7 44 L 7 48 Z','#205560')
c.path('M 57 45 Q 53 35 58 29 Q 56 38 60 42 L 60 47 Z','#205560')
# Sand banks and shadow under the wreck.
c.poly([(0,50),(9,47),(20,49),(35,48),(49,45),(63,47),(63,64),(0,64)],'#7f9580')
c.poly([(0,54),(13,51),(26,54),(42,50),(56,50),(63,52),(63,64),(0,64)],'#a9b28c')
c.poly([(0,59),(15,56),(29,59),(45,54),(63,56),(63,64),(0,64)],'#c2c397')
c.ellipse(32,51,24,5,'#596f64')
# Broken leaning mast, rigging, and spar behind hull.
c.line(29,18,45,36,'#315b60')
c.line(29,18,15,38,'#315b60')
c.poly([(29,17),(32,18),(36,43),(32,44)],'#302f32')
c.line(30,19,34,39,'#927853')
c.line(30,20,32,30,'#b29a69')
c.line(22,27,40,23,'#343637')
c.line(22,26,40,22,'#927853')
c.set(40,22,'#c3a575')
# Small remnants of tattered sail.
c.poly([(31,25),(39,24),(39,29),(36,28),(36,32),(33,31)],'#536c67')
c.line(33,26,37,25,'#829181')
# Hull silhouette: an open jagged gunwale, upturned bow on right.
hull=[(8,35),(13,37),(18,38),(22,37),(24,39),(28,38),(30,40),(36,38),(39,39),(43,36),(48,35),(54,30),(56,31),(54,43),(50,49),(42,53),(25,54),(16,50),(11,44)]
c.poly(hull,'#222f32')
c.poly([(11,38),(23,41),(37,41),(48,37),(53,33),(51,43),(47,48),(39,51),(25,51),(17,47),(13,43)],'#6a5b45')
# Open deck interior and broken rim.
c.poly([(12,38),(24,40),(37,40),(49,36),(45,42),(34,45),(22,44),(16,42)],'#283b3b')
c.line(10,36,23,40,'#b19462')
c.line(25,40,29,41,'#92764e')
c.line(36,40,47,36,'#b19462')
c.line(48,36,54,31,'#c0a16c')
# Board courses follow the belly of the vessel.
c.path('M 14 43 L 24 47 L 37 47 L 49 42 L 52 37','#ad8757',False)
c.path('M 16 46 L 25 50 L 38 50 L 47 47 L 50 44','#9b784e',False)
c.path('M 20 49 L 27 52 L 39 52 L 45 50','#73583e',False)
c.line(21,45,22,47,'#343b34')
c.line(33,47,34,49,'#343b34')
c.line(42,45,43,47,'#343b34')
c.line(46,39,47,41,'#343b34')
# Worn iron ribs and the exposed snapped stern.
c.line(15,39,19,47,'#42534a')
c.line(16,40,20,47,'#82907a')
c.line(40,40,38,51,'#3c4c43')
c.line(41,40,39,49,'#7a8668')
c.line(49,37,46,46,'#3c4c43')
c.line(50,36,48,43,'#899077')
c.line(10,36,9,32,'#776d50')
c.line(12,37,13,34,'#ad9466')
# Hull breach with splintered edges.
c.poly([(27,43),(31,43),(34,46),(32,49),(28,48),(26,46)],'#192f34')
c.set(27,43,'#b18b58');c.line(28,49,31,50,'#b18b58')
c.set(33,45,'#98784c')
# Verdigris, barnacles, and salt-weathered timber.
for x,y in [(14,42),(20,44),(23,45),(35,46),(43,43),(46,41),(43,48),(24,49),(35,51)]:
 c.set(x,y,'#69877a')
for x,y in [(13,39),(18,42),(37,42),(44,40),(49,38)]:
 c.set(x,y,'#a7b6a0')
c.line(20,42,24,43,'#52766a');c.line(43,39,45,38,'#52766a')
# Drifting sand conceals the bottom planks.
c.poly([(8,51),(14,49),(20,51),(29,53),(37,53),(45,50),(50,49),(55,51),(48,53),(40,55),(23,56),(12,54)],'#a9b28c')
c.line(15,51,22,53,'#d5cea0');c.line(24,54,33,54,'#d5cea0')
c.line(43,52,48,51,'#d5cea0')
# Foreground kelp with bent blades.
for d,col in [
 ('M 6 56 Q 1 47 4 40 Q 7 45 5 49 L 8 56 Z','#265e51'),
 ('M 7 56 Q 10 47 8 36 Q 13 41 11 48 L 9 56 Z','#397d60'),
 ('M 8 55 Q 4 47 1 46 Q 6 46 9 51 Z','#519777'),
 ('M 55 54 Q 51 45 55 39 Q 54 47 58 53 Z','#286754'),
 ('M 57 55 Q 62 43 59 35 Q 64 41 61 49 L 59 55 Z','#3b8567'),
 ('M 57 53 Q 56 45 59 42 L 58 51 Z','#67a17b')]: c.path(d,col)
# Coral branches at front right.
c.ellipse(49,58,7,2,'#7e8e77')
for x0,y0,x1,y1 in [(49,58,49,49),(49,55,45,52),(45,52,45,48),(49,53,53,49),(53,49,53,46),(49,51,47,49),(47,49,47,46),(49,56,54,53),(54,53,55,50)]:
 c.line(x0,y0,x1,y1,'#b76460');c.line(x0+1,y0,x1+1,y1,'#dd8a73')
c.set(48,46,'#f2b28b');c.set(54,46,'#f2b28b');c.set(46,48,'#f2b28b')
# Low purple tube coral on left.
for x,y,h in [(14,58,5),(17,59,7),(20,59,4)]:
 c.rect(x,y-h,3,h,'#6f627f');c.line(x,y-h,x,y-1,'#a18a9d');c.set(x+1,y-h,'#3c435b')
# Little sand pebbles and shell fragments in intentional clusters.
for x,y in [(2,57),(10,60),(24,59),(30,57),(35,61),(41,58),(58,60),(61,54),(4,62),(26,62),(54,62)]:
 c.line(x,y,x+1,y,'#879a7e')
for x,y in [(10,57),(23,58),(33,60),(43,61),(58,57)]:
 c.line(x,y,x+2,y,'#ded5aa')
c.rect(34,56,3,2,'#7d8871');c.line(34,56,36,56,'#c9c59d')
# School of fish, bright silhouettes sweeping past above the ship.
def fish(x,y,col):
 c.poly([(x-3,y),(x-5,y-2),(x-5,y+2)],col)
 c.line(x-2,y-1,x+1,y-1,col)
 c.line(x-3,y,x+3,y,col)
 c.line(x-1,y+1,x+1,y+1,'#5495a0')
 c.set(x+1,y-1,'#d6dec0');c.set(x+2,y,'#183e50')
for x,y,col in [(42,10,'#9dbcb0'),(53,15,'#c6cba0'),(43,19,'#c6cba0'),(57,24,'#91b7ac'),(34,12,'#80aba5'),(24,9,'#80aba5')]: fish(x,y,col)
# Small near-surface fish and suspended specks.
c.line(10,18,13,18,'#83ac9e');c.set(9,17,'#83ac9e');c.set(9,19,'#83ac9e')
c.line(18,22,20,22,'#83ac9e');c.set(17,21,'#83ac9e')
for x,y in [(5,8),(17,13),(22,30),(4,26),(47,27),(60,7),(37,5),(58,31),(18,32)]: c.set(x,y,'#387185')
# A few bubbles above the broken deck.
c.circle(16,29,1,'#61949a',False);c.set(16,30,'#164c61')
c.set(18,25,'#8ab0ad');c.set(15,23,'#4f8491')
view(c)
finish(result)
