result = new_canvas(64,64, '#101623', name='mad_cyborg_scientist')
c=result
# Controlled cool shadows and warm flesh, with a toxic mint eye.
ink='#10131e'; deep='#202737'; mid='#394959'; metal='#657d88'; light='#a6c2c7'; shine='#e0efdc'
skinshadow='#743d48'; skin='#ba705b'; sklight='#e7aa7a'; warm='#ffe0a0'
coatshadow='#4c555b'; coat='#91978a'; coatlight='#d1d0ab'; hairshadow='#7c969e'; hair='#c6d4c8'; white='#f6f1cf'
# angular vignette
c.poly([(4,18),(17,5),(46,4),(60,20),(60,48),(49,59),(10,56),(3,41)], '#192737')
c.poly([(7,24),(18,10),(44,8),(55,20),(55,42),(45,53),(13,50)], '#223848')
c.line(6,18,6,25,'#36515b'); c.line(7,17,12,12,'#36515b')
c.line(55,8,59,8, '#37616b'); c.line(57,6,57,10,'#37616b')
# back silhouette: wild hair
c.poly([(13,31),(10,25),(12,19),(7,18),(14,14),(12,8),(20,10),(22,3),(27,7),(32,2),(35,7),(43,4),(42,9),(49,9),(46,15),(49,22),(44,32)], ink)
c.poly([(14,25),(12,21),(16,18),(11,17),(18,14),(15,10),(22,12),(24,6),(28,10),(32,5),(34,11),(40,7),(39,12),(46,11),(42,17),(46,21),(42,27),(25,30)],hairshadow)
c.poly([(13,17),(20,13),(18,11),(23,13),(25,8),(28,13),(32,7),(33,13),(39,9),(37,16),(42,13),(41,20),(31,24),(19,22)],hair)
c.line(16,16,23,14,white); c.line(24,12,25,9,white); c.line(29,13,32,9,white)
c.line(34,15,38,12,white); c.line(14,21,17,22,hair)
# torso and coat silhouette
c.poly([(22,36),(40,35),(44,39),(50,40),(54,46),(53,63),(7,63),(8,48),(12,42),(20,40)],ink)
c.poly([(21,39),(26,42),(36,41),(40,38),(48,42),(51,49),(48,63),(9,63),(10,49),(14,43)],coatshadow)
c.poly([(18,41),(22,40),(26,45),(23,52),(19,63),(10,63),(12,47)],coat)
c.poly([(18,42),(21,41),(23,45),(19,50),(20,54),(16,60),(13,61),(13,48)],coatlight)
c.poly([(39,40),(44,42),(47,47),(44,57),(45,63),(37,63),(35,47)],coat)
c.poly([(40,42),(43,43),(44,48),(40,51),(40,56),(37,51)],coatlight)
# neck
c.poly([(25,33),(37,32),(38,41),(33,46),(26,42)],ink)
c.poly([(26,34),(32,35),(33,40),(30,42),(26,39)],skinshadow)
c.poly([(26,35),(29,37),(30,40),(27,39)],skin)
c.poly([(33,34),(37,34),(36,41),(33,43)],metal)
c.line(33,37,36,37,deep); c.line(33,40,35,40,deep)
# leather apron and shoulder straps
c.line(24,42,27,48,'#382a2b');c.line(37,42,35,48,'#382a2b')
c.line(25,42,28,48,'#a06d43'); c.line(36,43,34,48,'#a06d43')
c.poly([(26,47),(35,47),(39,63),(21,63)],'#382a2b')
c.poly([(27,48),(34,48),(37,63),(23,63)],'#6b4433')
c.poly([(27,49),(30,49),(28,59),(25,60)],'#93603d')
c.line(25,59,35,59,'#b5804d'); c.line(27,52,33,52,'#382a2b'); c.line(27,53,27,56,'#382a2b')
c.set(27,48,'#d0ab6c'); c.set(34,48,'#d0ab6c')
# head outline and ear
c.poly([(20,17),(27,14),(35,14),(41,17),(44,24),(42,33),(37,39),(28,39),(22,35),(19,29),(17,28),(16,23),(18,21)],ink)
c.poly([(18,23),(21,22),(23,28),(20,29),(18,27)],skin)
c.set(19,25,skinshadow)
# human half
c.poly([(22,18),(27,16),(32,17),(33,22),(32,29),(34,34),(32,38),(28,37),(23,33),(21,28),(21,23)],skin)
c.poly([(23,19),(28,17),(30,19),(29,23),(26,24),(24,28),(22,25)],sklight)
c.poly([(24,27),(26,28),(28,26),(29,30),(25,31),(23,30)],sklight)
c.poly([(24,32),(28,34),(32,34),(30,37),(27,35)],sklight)
# robot plates split at irregular center seam
c.poly([(32,16),(37,16),(41,19),(42,24),(41,31),(38,36),(33,38),(31,33),(32,29),(30,26),(32,23)],mid)
c.poly([(33,17),(37,17),(40,20),(40,23),(34,22),(32,24)],metal)
c.line(33,17,37,17,light); c.line(38,18,40,20,light)
c.poly([(40,26),(41,27),(39,32),(36,34),(32,32),(33,29),(36,30)],metal)
c.poly([(39,27),(40,27),(38,31),(36,32),(37,29)],light)
c.poly([(34,34),(38,33),(36,36),(33,37)],metal)
c.line(33,35,35,35,light)
c.line(31,18,31,22,ink); c.set(30,24,ink); c.line(31,27,32,29,ink)
# robotic temple bolts and brow
c.rect(40,21,3,6,deep);c.set(41,22,light);c.set(41,26,metal)
c.line(34,19,36,19,deep);c.set(37,20,deep)
# the human eye and expression
c.poly([(22,22),(25,21),(29,23),(28,25),(24,25)],skinshadow)
c.line(23,22,26,22,ink);c.line(26,22,29,24,ink)
c.line(24,24,27,24,white);c.set(26,24,ink);c.set(24,25,skinshadow)
c.line(22,20,24,19,skinshadow)
# projecting nose
c.poly([(29,24),(28,28),(30,29),(32,28),(30,27)],skinshadow)
c.line(29,25,29,27,warm);c.set(30,28,sklight)
# eye housing, one brilliant cybernetic eye
c.poly([(33,23),(36,22),(39,23),(40,25),(38,28),(34,28),(32,26)],ink)
c.line(34,23,37,23,'#258e91'); c.line(33,25,34,27,'#258e91')
c.rect(34,24,4,3,'#44eeb5'); c.rect(35,24,2,2,'#ecffcf');c.set(38,25,'#99ffd0');c.set(35,27,'#20aa97')
# huge asymmetric maniacal grin
c.poly([(24,29),(27,31),(31,31),(35,29),(36,32),(33,35),(28,35),(25,33)],ink)
c.line(25,30,28,32,white);c.line(28,32,32,32,white);c.line(32,32,34,30,white)
c.set(28,32,skinshadow);c.set(31,32,skinshadow)
c.line(29,34,32,34,'#cf7868');c.set(25,29,skinshadow);c.set(35,29,light)
# white hair forelock over the forehead
c.poly([(19,20),(19,17),(24,14),(30,14),(32,16),(28,17),(25,16),(23,18),(22,21)],hair)
c.line(21,17,25,15,white);c.line(25,15,28,15,white)
# electrode sockets emerging above skull with small wires
c.line(35,15,35,11,ink);c.rect(33,10,5,4,ink);c.rect(34,10,3,3,metal);c.set(34,10,shine)
c.line(36,10,38,7,'#c78553');c.line(38,7,44,7,'#c78553');c.line(44,7,46,10,'#c78553')
c.rect(40,14,5,4,ink);c.rect(41,14,3,2,light);c.line(44,14,48,12,'#3da7a3');c.line(48,12,49,15,'#3da7a3');c.line(49,15,48,20,'#3da7a3')
# stains, worn cuff and pocket
c.rect(13,53,5,1,coatshadow);c.line(13,54,14,57,coatshadow);c.line(14,57,17,57,coatshadow)
c.set(15,59,'#766944');c.rect(11,60,2,2,'#766944');c.set(19,47,'#766944');c.set(17,49,'#9c9163')
c.line(16,50,16,53,ink);c.set(16,50,'#bd6b55')
# tool belt, metal buckle and tools
c.rect(20,60,22,4,ink);c.rect(21,61,20,2,'#493431');c.rect(28,60,6,4,metal);c.rect(29,61,4,2,ink);c.set(30,61,light)
c.rect(23,58,2,6,deep);c.rect(23,57,2,3,metal);c.set(23,57,light)
c.rect(36,58,2,6,'#b48048');c.rect(36,56,2,3,deep);c.set(36,56,light)
# exposed upper arm, shoulder ball
c.poly([(45,42),(50,41),(54,44),(54,50),(51,54),(46,52),(44,47)],ink)
c.circle(49,46,4,mid);c.circle(49,46,3,metal);c.circle(49,46,1,deep);c.set(48,44,shine)
c.poly([(49,49),(53,48),(55,55),(51,59),(47,56)],ink)
c.poly([(50,50),(52,50),(53,55),(51,56),(49,54)],metal)
c.line(50,50,51,54,shine);c.line(53,51,54,54,mid)
# bent forearm reaching up along right side
c.poly([(50,55),(53,56),(57,49),(58,41),(54,39),(51,43)],ink)
c.poly([(52,53),(54,52),(56,46),(56,42),(54,42)],mid)
c.line(53,51,55,44,light);c.line(52,51,53,45,metal)
c.rect(52,42,5,3,metal);c.line(53,42,56,42,shine)
# prosthetic hand and individually articulated crooked fingers
c.poly([(53,42),(51,39),(51,35),(49,32),(50,30),(53,32),(54,35),(54,29),(56,27),(58,28),(58,32),(60,30),(62,32),(62,37),(59,41),(58,44)],ink)
c.poly([(54,41),(52,38),(52,35),(50,32),(51,32),(54,36),(55,35),(55,30),(56,29),(57,29),(57,35),(59,33),(60,32),(61,33),(60,37),(57,41)],metal)
c.line(55,30,55,34,light);c.set(56,29,shine);c.line(60,33,60,35,light)
c.line(52,35,53,37,light);c.rect(54,37,4,3,mid);c.line(54,37,57,37,light)
c.set(56,39,ink);c.line(58,35,59,35,ink);c.set(55,33,ink)
# external cable loops from wrist to elbow
c.path('M 57 41 Q 62 44 59 50 Q 57 55 54 56',ink,fill=False)
c.path('M 58 42 Q 61 45 58 50 L 55 54','#b56a40',fill=False)
c.path('M 51 44 Q 48 49 49 52 L 51 55','#299a99',fill=False)
c.set(58,43,'#e1ac60')
view(result)
save('mad-cyborg-scientist',result)
finish(result)
