c = new_canvas(64,64, '#101623', name='mad_scientist')
# restrained palette
ink='#11121c'; dark='#252936'; steel='#506774'; mid='#85999b'; light='#c1d0c5'; white='#edf0ce'; skin='#c28b68'; warm='#edbc82'; shade='#80534b'; coat='#a5a991'; dirty='#686f65'; brown='#664538'; leather='#a17145'; cyan='#62fff1'
# background halo
c.ellipse(31,29,27,28,'#1b3040')
c.ellipse(31,24,22,23,'#244554')
c.line(4,46,14,46,'#365563'); c.line(51,12,58,12,'#365563')
c.rect(54,15,2,7,'#365563')
# body silhouette
c.poly([(21,37),(39,36),(48,41),(55,50),(58,63),(6,63),(8,49),(14,42)],ink)
c.poly([(19,40),(29,43),(29,63),(8,63),(10,49)],coat)
c.poly([(39,39),(48,43),(50,61),(36,63),(31,45)],dirty)
c.poly([(16,43),(21,41),(25,49),(19,54),(12,58),(12,49)],light)
c.poly([(39,41),(43,44),(39,52),(34,48)],coat)
# neck
c.poly([(24,32),(39,32),(38,43),(32,47),(23,40)],shade)
c.poly([(26,35),(33,37),(34,43),(29,44),(26,41)],skin)
c.rect(35,36,5,6,steel)
for y in [37,40]: c.line(35,y,39,y,light)
# apron straps and apron
c.line(23,42,27,51,brown); c.line(24,42,28,51,leather)
c.line(38,43,35,51,brown)
c.poly([(27,48),(35,48),(41,63),(22,63)],brown)
c.poly([(28,50),(34,50),(38,60),(25,60)],leather)
c.line(28,51,34,51,'#c49458'); c.rect(28,54,7,5,brown); c.line(29,54,33,54,'#bf8d53')
# hair silhouette and wild spikes
c.poly([(15,28),(10,25),(13,19),(7,18),(13,14),(10,9),(18,11),(18,4),(24,8),(28,2),(31,8),(37,4),(38,10),(45,7),(44,15),(48,18),(44,29)],ink)
c.poly([(16,25),(12,24),(16,18),(10,17),(17,15),(13,11),(21,13),(20,7),(25,11),(28,5),(31,12),(36,7),(35,14),(42,10),(40,17),(44,18),(41,25)],light)
c.poly([(13,16),(22,16),(20,10),(25,13),(28,8),(30,15),(36,11),(34,17),(19,22)],white)
c.line(14,23,20,19,mid)
# head with human/robot division
c.poly([(22,16),(33,14),(40,17),(44,23),(43,33),(39,39),(31,42),(23,39),(18,32),(17,24)],ink)
c.poly([(22,18),(31,16),(34,20),(32,35),(30,39),(24,37),(20,31),(19,24)],skin)
c.poly([(22,19),(29,18),(30,23),(25,25),(22,29),(20,26)],warm)
c.poly([(20,28),(23,29),(24,32),(21,32)],shade)
c.poly([(32,17),(39,19),(42,23),(41,33),(37,38),(31,39),(33,30),(30,26)],steel)
c.poly([(34,18),(39,20),(40,23),(34,23),(32,21)],mid)
c.line(34,18,38,19,light)
c.poly([(40,27),(42,25),(41,33),(37,37),(35,35)],dark)
c.poly([(34,29),(38,29),(38,33),(35,35),(33,33)],mid)
c.line(40,28,40,32,light)
c.line(31,18,31,23,ink)
# ear and port
c.rect(16,25,4,7,shade); c.line(17,26,17,29,warm)
c.rect(42,24,3,7,ink); c.rect(42,25,2,4,mid)
# raised human brow and eye
c.line(21,22,26,21,ink); c.line(26,21,28,23,ink)
c.line(22,24,27,24,white); c.rect(25,23,2,3,ink); c.set(25,23,'#eece70')
# robotic eye black socket and radiance
c.poly([(33,23),(39,23),(41,25),(38,28),(33,27)],ink)
c.line(33,24,38,24,'#168f9a'); c.line(33,25,39,25,cyan); c.line(34,26,37,26,cyan); c.line(35,25,37,25,'#f4ffe7')
# nose
c.poly([(28,24),(27,29),(25,30),(29,31),(31,29)],shade)
c.line(28,26,28,29,warm); c.set(26,30,warm)
# grin
c.poly([(23,32),(28,33),(32,32),(37,30),(36,35),(31,38),(26,36)],ink)
c.poly([(24,33),(29,34),(35,32),(34,35),(29,36),(26,35)],white)
c.set(28,34,shade); c.set(32,34,steel)
c.line(27,38,30,39,warm)
c.line(36,35,38,34,light)
# forehead bolts / brain electrodes
for x,y in [(34,20),(39,30),(37,36)]:
 c.set(x,y,ink); c.set(x+1,y,light)
c.line(38,17,40,12,ink); c.line(39,16,41,12,steel)
c.rect(39,10,5,3,ink); c.rect(40,10,3,2,mid); c.set(41,9,cyan)
c.line(20,17,17,13,ink); c.rect(15,11,4,3,steel); c.line(15,11,17,11,light)
c.path('M 43 11 L 48 11 L 50 15 L 50 23 L 45 27', '#2ca8ae',False)
# dirty coat patches
c.rect(13,53,6,1,dirty); c.rect(14,55,4,4,dirty); c.set(11,59,shade); c.rect(19,58,2,3,shade)
c.line(19,45,22,48,white)
# exposed right arm, raised prosthetic hand
c.poly([(46,42),(50,41),(54,45),(54,52),(49,56),(44,52),(43,46)],ink)
c.poly([(46,43),(49,43),(52,46),(50,49),(45,48)],steel)
c.line(46,43,49,44,light)
c.circle(48,51,4,dark); c.circle(48,51,2,mid); c.set(48,51,ink)
c.poly([(49,51),(54,47),(57,48),(58,52),(52,57),(48,56)],steel)
c.line(51,53,56,49,light); c.line(52,56,57,52,mid)
# cable loops outside arm
c.path('M 44 45 L 42 49 L 43 55 L 48 59 L 54 57 L 58 53',ink,False)
c.path('M 44 46 L 43 50 L 44 54 L 49 58 L 54 56', '#bd7549',False)
# hand palm with raised fingers
c.poly([(53,47),(51,42),(52,38),(55,37),(60,40),(61,46),(57,50)],ink)
c.poly([(54,46),(53,42),(54,39),(58,41),(59,45),(56,48)],mid)
c.line(54,41,57,43,light); c.line(55,45,58,45,steel)
for x,y in [(51,34),(54,32),(57,34)]:
 c.rect(x,y,3,8,ink); c.rect(x,y,2,6,steel); c.set(x,y,light); c.line(x,y+3,x+1,y+3,dark)
c.line(52,44,49,40,ink); c.line(51,43,49,41,mid)
# belt and tools
c.rect(20,60,23,4,ink); c.rect(21,60,21,2,brown); c.rect(28,59,5,4,mid); c.rect(29,60,3,2,ink)
c.rect(36,58,3,6,ink); c.rect(37,56,1,6,light); c.rect(36,55,3,2,steel)
c.rect(23,57,2,5,dark); c.set(23,57,'#d4a75c')
view(c)
finish(c)
