# 64px character portrait: THE GALVANIST
result = new_canvas(64, 64, '#101724', name='mad_cyborg_scientist')
c = result
P = {
'bg':'#101724','bg2':'#192637','halo':'#263849','halo2':'#304858',
'ink':'#11121d','deep':'#202332','shadow':'#343747',
'skin0':'#653d42','skin1':'#a65b50','skin2':'#d68a67','skin3':'#f2ba83','skin4':'#ffe0a3',
'metal0':'#243644','metal1':'#3e5663','metal2':'#65818a','metal3':'#9db6b7','metal4':'#deebe0',
'white0':'#626e78','white1':'#a3b0ad','white2':'#dae0cc','white3':'#fff0cf',
'coat0':'#414a4d','coat1':'#7c8580','coat2':'#b7b9a1','coat3':'#e0d9b5',
'leather0':'#372a2c','leather1':'#664035','leather2':'#955d40','leather3':'#c18a54',
'cyan0':'#17677a','cyan1':'#1bb7bb','cyan2':'#6bf8d5','cyan3':'#dcffdf',
'red0':'#633541','red1':'#c95750','gold':'#e9b96c','tooth':'#fff1c7'
}
for k,v in P.items(): c.color(v,k)
def poly(points,col): c.poly(points,P.get(col,col))
def line(x0,y0,x1,y1,col): c.line(x0,y0,x1,y1,P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def px(x,y,col): c.set(x,y,P.get(col,col))
# Quiet laboratory halo; the offset ring separates the white hair and coat.
c.ellipse(33,29,27,27,P['bg2'])
c.ellipse(34,27,23,24,P['halo'])
c.ellipse(34,27,20,22,P['bg2'])
line(49,8,55,14,'halo2'); line(56,17,58,23,'halo2')
line(9,29,9,37,'halo2'); line(10,40,13,45,'halo2')
# Fine exposed leads behind the silhouette.
c.path('M 42 8 C 52 4 56 13 50 20 L 48 24',P['cyan0'],False)
c.path('M 18 19 C 7 18 10 30 16 31 L 19 34',P['red0'],False)
line(7,51,14,44,'metal1'); line(7,52,7,56,'metal1')
# Torso silhouette, broad sloped shoulders and a high collar.
poly([(21,36),(29,35),(38,36),(43,39),(49,40),(54,46),(56,63),(6,63),(8,49),(12,43)],'ink')
poly([(20,38),(27,39),(29,47),(23,62),(8,63),(10,50),(14,44)],'coat1')
poly([(20,39),(23,43),(19,47),(21,50),(15,59),(14,63),(8,63),(11,50),(15,44)],'coat2')
poly([(16,44),(19,42),(18,47),(14,51),(12,60),(9,62),(11,51)],'coat3')
poly([(38,38),(45,41),(49,46),(48,63),(39,63),(34,46)],'coat0')
poly([(39,40),(44,42),(46,46),(42,45),(40,51),(36,46)],'coat2')
line(41,41,44,43,'coat3')
# Neck, dark under the jaw; leather bib and shoulder straps.
poly([(25,32),(38,33),(38,42),(34,47),(27,44),(24,39)],'ink')
poly([(26,35),(31,37),(33,41),(29,43),(26,40)],'skin1')
poly([(33,36),(38,35),(37,41),(34,43)],'metal1')
line(35,38,36,41,'metal3')
poly([(26,42),(31,45),(36,42),(40,48),(43,63),(20,63),(23,49)],'leather0')
poly([(27,44),(31,47),(36,44),(38,49),(40,62),(23,62),(25,49)],'leather1')
poly([(27,47),(30,49),(35,47),(36,55),(26,55)],'leather2')
line(26,49,25,55,'leather3'); line(35,48,36,54,'leather3')
line(23,41,27,48,'leather0'); line(24,41,28,47,'leather3')
line(39,42,36,48,'leather0'); line(38,42,35,47,'leather3')
rect(25,46,3,3,'gold'); px(26,47,'leather0')
rect(35,46,3,3,'metal3'); px(36,47,'leather0')
# Coat pocket, wear marks and stains.
line(12,53,18,54,'coat0'); line(12,54,12,58,'coat0'); line(12,58,16,59,'coat0')
line(14,51,15,54,'metal1'); px(14,50,'red1')
px(10,60,'leather1'); px(11,61,'leather2'); px(19,49,'leather2')
rect(17,55,2,2,'coat1'); px(16,57,'leather2'); px(19,61,'coat0')
# Belt with buckle, pouches, and hanging tools.
poly([(9,59),(22,57),(39,57),(47,60),(47,63),(9,63)],'leather0')
line(12,59,23,58,'leather2'); line(35,58,44,60,'leather2')
rect(27,57,8,6,'ink'); rect(28,58,6,4,'gold'); rect(30,59,3,2,'leather0'); px(29,59,'white3')
rect(19,58,5,6,'leather1'); line(20,59,22,59,'leather3')
rect(39,59,5,5,'leather1'); line(40,60,42,60,'leather3')
line(14,58,13,63,'metal3'); px(13,57,'metal3'); px(15,57,'metal3'); px(14,59,'metal0')
# Robotic arm emerging from the rolled sleeve, bent upward.
poly([(45,43),(49,43),(53,48),(54,55),(50,59),(45,57),(42,51)],'ink')
poly([(45,44),(48,44),(51,48),(49,52),(44,51),(43,48)],'coat1')
line(44,45,47,45,'coat3'); line(44,48,48,49,'coat2')
poly([(47,50),(51,49),(54,53),(53,57),(49,58),(46,55)],'metal1')
c.circle(50,54,3,P['metal0']); c.circle(50,54,2,P['metal2']); px(50,54,'ink'); px(49,53,'metal4')
poly([(51,50),(51,43),(54,40),(59,42),(59,48),(55,54),(52,55)],'ink')
poly([(53,44),(56,42),(58,43),(57,48),(53,52)],'metal1')
poly([(53,44),(55,43),(55,48),(52,52)],'metal3')
line(53,45,53,48,'metal4'); line(56,46,56,48,'cyan1')
# Flexible external cables route around the elbow.
c.path('M 58 39 C 63 47 58 57 54 58 L 51 58',P['ink'],False)
c.path('M 59 42 C 62 48 57 56 54 56',P['cyan1'],False)
c.path('M 57 43 C 59 48 54 53 53 54',P['red1'],False)
# Head silhouette and left human ear.
poly([(21,11),(29,8),(38,10),(44,14),(46,22),(44,31),(39,37),(32,39),(25,35),(21,30),(18,23),(19,16)],'ink')
poly([(19,21),(16,21),(16,26),(19,29),(22,27),(22,23)],'skin0')
poly([(18,22),(17,23),(18,26),(20,27),(20,23)],'skin2')
line(18,24,19,25,'skin0')
# Warm human half: forehead, temple and high cheekbone.
poly([(23,12),(30,11),(34,14),(33,23),(32,28),(34,36),(30,36),(25,32),(22,27),(21,20)],'skin1')
poly([(24,13),(30,12),(32,15),(30,21),(32,25),(29,27),(26,25),(22,25),(22,19)],'skin2')
poly([(24,14),(29,13),(30,16),(28,18),(24,18),(23,21),(22,20)],'skin3')
line(24,14,28,13,'skin4')
poly([(23,25),(25,24),(29,26),(28,28),(24,29)],'skin3')
px(23,26,'skin4')
poly([(26,33),(30,34),(33,33),(32,36),(29,35)],'skin2')
# Right cranium: shadow planes and beveled steel plates.
poly([(33,11),(38,12),(42,15),(44,19),(44,27),(42,32),(37,36),(33,36),(32,29),(34,24),(32,20)],'metal0')
poly([(34,12),(39,14),(42,17),(42,21),(36,22),(33,19)],'metal2')
poly([(34,12),(38,14),(40,16),(35,16),(34,19),(33,17)],'metal3')
line(34,12,38,14,'metal4')
poly([(41,16),(44,20),(44,27),(41,30),(40,25),(42,23)],'metal1')
poly([(35,25),(39,24),(40,28),(42,29),(40,32),(36,34),(33,32)],'metal2')
poly([(33,28),(35,29),(35,33),(38,34),(36,36),(33,35)],'metal3')
line(42,18,43,20,'metal3'); line(43,25,42,27,'metal3')
# Skull segmentation, rivets and a little vent at the temple.
line(37,14,37,17,'metal0'); line(38,17,41,18,'metal0')
px(39,15,'metal4'); px(39,16,'metal0')
rect(43,21,3,7,'ink'); line(44,22,44,26,'metal2')
px(45,23,'metal3'); px(45,25,'metal3')
line(38,26,39,27,'metal0'); px(40,29,'metal4')
# Human eye: pinched brow, small bright eyeball, tiny dark pupil.
poly([(22,20),(24,19),(29,21),(29,23),(26,23),(23,22)],'skin0')
line(23,20,28,22,'ink')
line(24,22,27,23,'tooth'); px(26,22,'ink'); px(26,23,'ink')
line(23,24,25,25,'skin0')
# The cybernetic eye in a deep, asymmetric socket.
poly([(34,20),(38,19),(42,20),(42,23),(39,25),(35,24),(33,22)],'ink')
line(35,20,39,20,'cyan0'); line(34,22,36,24,'cyan0')
poly([(36,21),(40,20),(41,21),(40,23),(36,23),(35,22)],'cyan1')
line(36,21,40,21,'cyan2'); line(37,22,39,22,'cyan3'); px(40,22,'cyan2')
px(41,24,'cyan0'); px(35,25,'cyan0')
line(35,18,39,18,'metal4')
# Split nose: strong warm lit bridge against steel.
poly([(30,20),(31,21),(31,24),(33,26),(32,28),(28,28),(28,26)],'skin0')
poly([(30,22),(30,25),(32,26),(30,27),(28,26)],'skin3')
px(30,25,'skin4'); px(31,28,'ink'); px(28,27,'skin1')
# Broad, crooked maniacal grin, individual broken tooth shapes.
poly([(24,28),(27,29),(31,30),(35,29),(40,27),(40,31),(37,34),(31,35),(27,33)],'ink')
line(25,28,28,29,'skin0'); line(24,28,24,30,'skin0')
poly([(26,30),(31,31),(35,30),(39,28),(38,31),(34,33),(30,33),(27,32)],'tooth')
line(28,30,28,31,'skin0'); line(31,31,31,32,'skin0'); line(35,30,35,31,'metal0'); px(38,29,'metal0')
line(29,34,32,35,'skin0'); line(36,34,39,32,'metal0')
px(27,34,'skin3')
# Hair silhouette with deliberate large jagged clumps.
poly([(17,22),(15,18),(17,13),(13,14),(18,9),(17,6),(23,7),(24,3),(28,6),(33,2),(33,6),(38,4),(38,8),(43,7),(46,12),(42,15),(39,12),(34,12),(31,15),(27,12),(23,14),(22,18),(19,17),(19,23)],'ink')
poly([(17,19),(18,14),(16,14),(21,10),(19,8),(24,9),(25,5),(29,8),(32,4),(32,8),(36,6),(36,10),(41,9),(44,12),(40,13),(36,11),(32,13),(28,10),(24,12),(21,16),(19,15),(19,19)],'white1')
poly([(18,14),(23,10),(22,9),(26,10),(26,7),(29,10),(31,7),(31,11),(34,9),(36,10),(32,12),(28,10),(24,12),(20,15)],'white3')
poly([(34,9),(36,8),(36,10),(41,10),(42,12),(39,11),(36,11)],'white2')
line(24,12,22,14,'white2'); line(19,17,18,20,'white0')
line(28,7,29,8,'white2')
# Short tufts at the organic jaw.
poly([(20,23),(21,25),(22,28),(24,31),(21,30),(20,27)],'white0')
line(21,26,22,29,'white2')
# Electrode sockets and upright plugs break the hair silhouette.
poly([(40,10),(39,8),(41,5),(44,5),(45,8),(44,11),(42,12)],'ink')
poly([(41,9),(41,7),(43,6),(44,8),(43,10)],'metal2')
line(42,5,44,5,'metal4'); line(41,8,43,9,'metal4')
line(43,4,45,2,'ink'); line(44,4,46,2,'cyan1'); px(46,2,'cyan2')
rect(35,4,3,4,'ink'); rect(36,4,1,3,'metal3'); px(36,3,'red1')
# Raised prosthetic hand: pinching a live electrode with segmented fingers.
# Small dark electrode and tiny energy spark.
line(53,23,55,34,'ink'); line(54,25,55,32,'metal3')
px(53,24,'cyan3'); px(52,23,'cyan2'); px(54,22,'cyan1')
px(50,23,'cyan0'); px(53,20,'cyan1'); px(56,23,'cyan0')
# Bent articulated fingers and knuckle silhouettes.
poly([(51,40),(49,36),(49,32),(51,30),(54,30),(55,32),(58,31),(60,33),(61,37),(59,42),(55,45),(52,43)],'ink')
poly([(52,39),(50,36),(50,33),(52,32),(54,32),(54,34),(52,35),(54,37)],'metal2')
line(51,33,53,33,'metal4'); line(51,35,52,36,'metal0')
poly([(55,33),(58,32),(59,34),(58,37),(56,38),(54,37),(54,35)],'metal3')
line(56,33,58,33,'metal4'); line(55,35,58,35,'metal0')
poly([(54,38),(57,37),(59,35),(60,37),(58,41),(55,43),(52,41)],'metal1')
poly([(53,38),(55,39),(56,41),(54,43),(52,41)],'metal3')
line(53,39,54,41,'metal4'); line(57,39,58,38,'metal3')
px(56,40,'ink'); px(55,41,'cyan1'); px(59,37,'metal4')
# Wrist cuff and crosswise machining lines.
line(53,43,56,44,'ink'); line(53,44,55,45,'metal4')
px(47,51,'metal4'); px(48,56,'metal3')
# A few grime flecks and sharp rim highlights, kept sparse.
px(24,54,'leather0'); line(28,53,30,53,'leather1'); px(34,51,'leather0')
px(11,55,'leather2'); px(18,46,'coat1'); line(8,62,9,57,'coat2')
# Carry the cropped torso cleanly through the bottom edge.
c.select(6,62,50,1).copy_to(6,63,c)
print(c.stats_text())
print(c.matrix_text(region=(18,18,45,36)))
save('mad_cyborg_scientist',result)
finish(result)
