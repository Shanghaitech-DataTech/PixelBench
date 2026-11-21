# Offshore service landing — 64 x 64, hard-edged pixel clusters.
result = new_canvas(64, 64, background='#a9c8d0', name='offshore_maintenance')
c = result
P = {
 'sky_top':'#93b9cb', 'sky_mid':'#aacbd3', 'sky_low':'#c4d9d8',
 'cloud':'#dae5df', 'cloud_light':'#e8ece1',
 'horizon':'#719ba9', 'sea_far':'#638f9f', 'sea_mid':'#467c90',
 'sea':'#32677f', 'sea_deep':'#28566f', 'trough':'#234c66',
 'ripple':'#84b4bc', 'foam':'#bfdad5', 'foam_light':'#e0e7d8',
 'steel_dark':'#293f51', 'steel':'#526a77', 'steel_light':'#8fa4a6',
 'tower_shade':'#7995a1', 'tower_mid':'#b0c3c3', 'tower':'#d5dfd6', 'tower_light':'#edf0df',
 'yellow_dark':'#9d7135', 'yellow':'#d4a33e', 'yellow_light':'#f3ce68',
 'rust':'#8b613c', 'orange_dark':'#ad4e30', 'orange':'#ed853c',
 'orange_light':'#ffb659', 'skin':'#e7b48b', 'navy':'#243c50',
}
def rect(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def line(x,y,xx,yy,k): c.line(x,y,xx,yy,P.get(k,k))
def poly(points,k): c.poly(points,P.get(k,k))
def pix(x,y,k): c.set(x,y,P.get(k,k))
# Open, hazy morning sky.
rect(0,0,64,11,'sky_top')
rect(0,11,64,13,'sky_mid')
rect(0,24,64,10,'sky_low')
# Long broken cloud banks.
rect(1,5,15,2,'cloud'); rect(5,4,9,1,'cloud')
rect(0,7,22,1,'cloud'); rect(2,6,17,1,'cloud_light')
rect(20,15,10,1,'cloud'); rect(23,14,7,1,'cloud')
rect(46,5,13,1,'cloud'); rect(50,4,7,1,'cloud')
rect(51,6,13,1,'cloud_light')
rect(0,29,7,1,'cloud'); rect(16,29,14,1,'cloud')
# Sea is separated from the sky by a quiet horizon.
rect(0,34,64,30,'sea_far')
rect(0,34,64,1,'horizon')
rect(0,42,64,10,'sea_mid')
rect(0,52,64,12,'sea')
rect(0,59,64,5,'sea_deep')
# Two complete, distant turbines. Their muted edges recede into the haze.
# Left: larger of the pair.
line(12,20,12,39,'tower_shade')
line(13,21,13,39,'tower')
rect(12,38,2,3,'yellow_dark')
poly([(12,20),(11,17),(12,7),(13,8),(13,18),(14,20)], 'tower')
line(12,8,12,18,'tower_light')
poly([(12,20),(10,22),(2,27),(3,24),(10,19)],'tower')
line(3,25,10,20,'tower_light')
poly([(13,20),(16,21),(23,27),(20,26),(13,22)],'tower')
line(15,22,21,26,'tower_light')
rect(11,19,4,2,'tower_shade'); rect(11,19,3,1,'tower_light'); pix(12,20,'tower')
# Right: further out to sea.
line(55,25,55,38,'tower_shade'); line(56,26,56,38,'tower')
rect(55,38,2,2,'yellow_dark')
poly([(55,25),(54,23),(55,14),(56,15),(56,24)],'tower')
line(55,15,55,23,'tower_light')
poly([(55,25),(53,27),(46,30),(48,27),(54,24)],'tower')
line(48,28,53,25,'tower_light')
poly([(56,25),(58,26),(63,31),(60,30),(55,27)],'tower')
line(57,27,62,30,'tower_light')
rect(54,24,3,2,'tower_shade'); rect(54,24,3,1,'tower_light'); pix(55,25,'tower')
# Distant surface texture, clean horizontal clusters.
for x,y,w in [(0,37,6),(18,36,9),(44,36,7),(59,36,5),(4,40,5),(17,39,4),(45,40,5),(58,41,5),(1,44,10),(15,43,5),(51,44,7)]:
    rect(x,y,w,1,'ripple')
for x,y,w in [(0,41,4),(15,41,8),(48,38,4),(58,39,6),(7,46,8),(19,47,4),(46,46,8),(57,48,7)]:
    rect(x,y,w,1,'sea')
# Broad nearer wave crests with stepped tips and shaded undersides.
poly([(0,50),(5,50),(7,49),(13,49),(15,50),(19,50),(19,51),(8,51),(6,52),(0,52)],'trough')
line(1,49,6,49,'ripple'); line(7,48,12,48,'ripple'); line(10,49,15,49,'foam')
line(0,50,3,50,'foam'); line(15,50,18,50,'ripple')
poly([(44,51),(49,51),(51,50),(58,50),(61,51),(63,51),(63,54),(55,54),(52,53),(45,53)],'sea_deep')
line(46,51,51,51,'ripple'); line(52,50,58,50,'foam'); line(59,51,63,51,'ripple')
poly([(1,58),(6,58),(9,56),(16,56),(19,57),(22,57),(22,59),(16,59),(12,60),(0,60)],'trough')
line(1,57,6,57,'ripple'); line(7,56,9,56,'foam'); line(10,55,15,55,'foam')
line(16,56,19,56,'ripple'); line(4,58,10,58,'sea_mid')
line(0,62,5,62,'sea_mid'); line(9,63,17,63,'ripple')
line(50,59,55,59,'ripple'); line(56,58,63,58,'foam')
line(48,62,53,62,'sea_mid'); line(60,61,63,61,'ripple')
# Shadow and wash around the single large monopile.
poly([(30,57),(40,56),(48,57),(50,59),(46,61),(31,62),(22,60),(24,58)],'trough')
line(28,59,33,59,'foam'); line(42,60,47,60,'ripple'); line(31,61,39,61,'ripple')
# Near turbine: the huge mast extends beyond the upper frame for human scale.
poly([(36,0),(43,0),(46,40),(33,40)],'tower_shade')
poly([(36,0),(41,0),(43,40),(33,40)],'tower')
poly([(36,0),(38,0),(36,40),(33,40)],'tower_light')
poly([(41,0),(43,0),(45,40),(41,40)],'tower_mid')
line(43,0,46,39,'tower_shade')
# Segmented tubular steel, light catches the weld seam.
line(35,22,44,22,'tower_mid'); line(35,23,40,23,'tower_light')
# Yellow transition piece and darker wet pile.
rect(33,39,13,17,'yellow_dark')
rect(34,39,9,18,'yellow'); rect(34,40,2,15,'yellow_light')
rect(43,40,2,17,'yellow_dark'); line(45,43,45,58,'steel_dark')
rect(34,56,11,4,'steel_dark'); rect(35,56,6,4,'steel')
rect(35,54,1,3,'rust'); rect(41,51,1,5,'yellow_dark')
line(33,43,44,43,'yellow_light')
# Rear railings behind the mast, then the grating deck.
line(25,35,33,35,'yellow_light'); line(46,35,51,35,'yellow_light')
line(25,36,33,36,'yellow_dark'); line(46,36,51,36,'yellow_dark')
for x in [25,31,48,51]: line(x,35,x,40,'yellow')
# Deck trapezoid, rim, and steel diagonal braces.
poly([(26,39),(49,39),(53,42),(23,42)],'steel_light')
line(26,40,49,40,'steel')
for x in range(28,50,3): line(x,40,x+1,41,'steel_dark')
rect(23,42,31,2,'steel_dark')
line(24,42,52,42,'yellow_light'); line(24,43,52,43,'yellow_dark')
poly([(30,44),(33,44),(36,50),(34,50)],'steel_dark')
line(31,44,35,49,'steel')
poly([(46,44),(50,44),(45,50),(43,50)],'steel_dark')
line(49,44,45,48,'steel_light')
# Main tower service door, just above the platform.
rect(37,26,5,14,'tower_shade')
rect(38,27,3,13,'tower_mid')
line(38,27,40,27,'tower_light'); line(38,28,38,38,'tower')
rect(39,29,2,2,'steel'); pix(40,36,'steel_dark')
rect(38,39,4,1,'steel')
# Foreground guardrail, waist-high compared with the person.
line(24,35,52,35,'yellow_dark'); line(24,34,51,34,'yellow_light')
line(24,38,52,38,'yellow')
for x in [24,31,45,52]:
    line(x,35,x,41,'yellow_dark'); line(x-1,35,x-1,40,'yellow_light')
# A break in the rail marks the ladder access gate.
rect(25,35,4,4,'sea_far')
line(25,34,29,34,'yellow_light'); line(29,35,29,41,'yellow')
# Ladder and its two grab handles.
line(24,40,24,59,'steel_dark'); line(30,40,30,59,'steel_dark')
line(25,39,25,59,'steel_light'); line(29,39,29,59,'steel_light')
for y in range(42,60,3):
    line(25,y,29,y,'steel_dark'); line(25,y,28,y,'tower_mid')
line(25,36,25,40,'yellow_light'); line(29,36,29,40,'yellow_light')
# Technician climbing: hard hat, gloves, reflective vest and work boots.
# Safety tether goes behind the raised arm and clips onto the fall-arrest rail.
line(25,48,28,46,'yellow_light'); pix(29,46,'steel_dark')
# Reaching right arm, with a gloved hand wrapped over a high rung.
pix(28,45,'yellow_light'); line(27,46,27,48,'orange_dark')
pix(26,48,'orange')
# Head in profile, with a dark chinstrap under the helmet.
rect(23,45,3,2,'skin'); pix(23,46,'navy'); pix(26,46,'skin')
rect(23,43,3,1,'yellow_light'); rect(22,44,5,1,'yellow')
line(23,44,25,44,'yellow_light'); pix(25,45,'navy')
# The bright jacket is a compact shape against the dark ocean.
rect(23,47,3,4,'orange'); line(22,48,22,49,'orange_dark')
pix(23,47,'orange_light'); pix(23,48,'orange_light')
line(23,50,25,50,'tower_light')
# Harness shoulder strap and belt; free hand grips the near rail.
line(24,47,24,49,'navy'); line(23,51,25,51,'navy')
pix(22,50,'orange'); pix(23,49,'yellow_light')
# One straight leg and one bent leg, with boots on separate rungs.
line(23,52,23,55,'navy'); pix(24,52,'orange_dark')
pix(23,54,'steel_light'); line(23,56,25,56,'navy')
line(25,52,27,51,'navy'); line(27,51,27,53,'navy')
pix(27,52,'steel_light'); line(27,53,28,53,'navy')
# Wash curls over the footing; small bright pixels catch the sun.
line(31,58,33,58,'foam'); pix(30,59,'foam_light')
line(35,60,42,60,'foam'); line(42,59,46,59,'foam_light')
pix(47,58,'ripple'); line(25,61,29,61,'sea_mid')
view(result, scale=8, margin=0)
save('offshore_maintenance', result)
finish(result)
