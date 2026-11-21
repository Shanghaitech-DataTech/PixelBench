result = new_canvas(64,64, '#101522', name='mad_cyborg_scientist')
c=result
# restrained cold shadows and sickly warm spotlight
ink='#101522'; deep='#202537'; steelD='#344052'; steel='#647a88'; light='#a6c5c8'; shine='#e2eee0'
skD='#784549'; skM='#b46b5b'; skin='#e2a77a'; skL='#ffda99'; coatD='#48555c'; coat='#929f93'; coatL='#d2d2ac'
# background halo, framing a silhouette
c.ellipse(31,27,25,25,'#172735')
c.ellipse(30,25,21,23,'#203b44')
c.line(5,49,17,37,'#2b4a50'); c.line(51,12,58,19,'#2b4a50')
# coat silhouette
c.poly([(6,63),(7,48),(11,42),(22,38),(23,34),(40,35),(43,40),(51,43),(56,53),(57,63)],ink)
c.poly([(8,63),(9,49),(13,44),(24,39),(39,39),(49,45),(53,63)],coatD)
c.poly([(9,62),(11,49),(16,44),(24,41),(25,50),(20,63)],coat)
c.poly([(10,59),(12,49),(17,46),(15,55),(15,62),(9,63)],coatL)
c.poly([(39,42),(45,43),(49,47),(47,57),(50,63),(39,63)],coat)
# neck and ribbed robot throat
c.poly([(24,32),(38,32),(40,42),(34,47),(23,40)],skD)
c.poly([(25,33),(30,36),(30,41),(26,40)],skin)
c.poly([(31,34),(39,33),(38,42),(33,44)],steelD)
for y in (36,39,42): c.line(32,y,37,y-1,steel)
# leather apron
c.poly([(25,42),(33,46),(39,42),(42,63),(20,63)],'#51352f')
c.poly([(26,46),(33,49),(38,46),(39,60),(24,60)],'#87533c')
c.line(26,47,24,57,'#bb8252');c.line(38,48,40,58,'#2f2b2c')
c.line(22,40,27,48,'#c08d58'); c.line(41,40,37,48,'#b17c50')
c.set(27,48,shine);c.set(37,48,shine)
# broad lab coat lapels
c.poly([(21,39),(24,41),(28,48),(22,46),(24,50),(18,57),(18,47)],coatL)
c.poly([(40,39),(43,43),(43,49),(39,47),(39,51),(34,48)],'#b9bfa2')
c.line(19,48,18,54,coatD)
# grime and torn stitching
c.rect(11,54,3,2,'#72785f');c.set(12,57,'#72785f');c.line(15,60,18,59,'#686655')
c.rect(41,53,4,1,coatD); c.rect(42,54,3,3,'#778270'); c.set(43,58,'#626856')
# skull and hair black silhouette
c.poly([(17,30),(15,23),(15,16),(12,12),(18,12),(16,7),(22,9),(23,3),(28,7),(33,2),(36,7),(41,5),(42,10),(47,13),(47,27),(43,34),(38,38),(28,39),(22,34)],ink)
# wild white hair spikes
c.poly([(16,23),(15,17),(12,14),(18,14),(16,9),(22,11),(23,5),(27,10),(32,4),(33,9),(38,5),(38,10),(42,8),(42,13),(36,18),(26,16),(21,26)],'#8eaaa9')
c.poly([(15,14),(20,15),(18,11),(24,13),(24,8),(28,12),(31,7),(31,12),(36,9),(34,15),(26,15),(21,19),(18,23),(18,17)],shine)
c.line(22,13,20,17,'#ffffff'); c.line(27,9,28,12,'#ffffff')
# face human left
c.poly([(22,18),(28,15),(33,17),(34,34),(30,38),(25,35),(20,28),(20,23)],skM)
c.poly([(23,18),(28,17),(30,19),(29,24),(32,27),(30,30),(25,31),(22,27)],skin)
c.poly([(23,19),(27,18),(28,20),(24,21)],skL)
c.poly([(22,25),(24,27),(24,29),(22,28)],skL)
# human ear
c.rect(18,24,3,6,skD); c.rect(18,24,2,4,skin);c.set(19,25,skD)
# metal hemisphere, angular plates
c.poly([(33,15),(39,12),(43,14),(46,19),(45,28),(42,33),(37,37),(32,36),(31,29),(32,23)],steelD)
c.poly([(34,16),(39,14),(42,15),(44,20),(37,21),(33,23)],steel)
c.poly([(35,16),(39,14),(42,16),(42,18),(35,19)],light)
c.line(34,17,33,22,shine)
c.poly([(43,23),(44,23),(43,28),(40,29),(40,25)],steel)
c.poly([(33,29),(38,29),(40,33),(36,36),(33,34)],steel)
c.line(34,35,37,35,light)
c.line(32,18,31,24,ink);c.line(31,27,32,31,ink)
# robotic temple vents
for y in (18,20,22):c.line(43,y,45,y+1,ink)
# eye socket human angry raised brow
c.line(22,22,25,21,skD);c.line(25,21,28,22,ink)
c.poly([(22,23),(28,23),(27,26),(24,25)],ink)
c.line(23,23,27,24,shine);c.set(26,24,'#b5e660'); c.set(26,23,ink)
c.line(23,27,26,28,skD)
# nose dividing the face
c.poly([(29,23),(28,28),(26,29),(30,30),(32,28)],skM)
c.set(28,28,skL);c.line(29,30,31,29,ink)
# luminous cybernetic eye
c.poly([(34,22),(37,20),(41,21),(43,24),(40,27),(35,26)],ink)
c.line(35,22,39,21,'#237a80');c.line(35,25,40,25,'#237a80')
c.rect(36,22,5,3,'#26c8b6');c.rect(37,22,3,2,'#a8ffcd'); c.set(38,22,'#ffffff'); c.set(41,23,'#6effd0')
# maniacal wide grin
c.poly([(24,30),(28,32),(32,31),(39,28),(38,32),(34,35),(29,35),(26,33)],ink)
c.poly([(25,30),(29,32),(33,31),(38,29),(36,32),(31,34),(28,33)],'#f6e3af')
for x,y in [(28,32),(31,32),(34,31),(36,30)]:c.set(x,y,'#8d7161')
c.line(28,35,31,36,skL);c.line(35,35,39,32,steelD)
# bolts and stitch pins
for x,y in [(40,16),(43,27),(36,34)]:
 c.set(x,y,ink);c.set(x,y-1,shine)
for x,y in [(31,19),(31,22),(32,30)]:c.line(x,y,x+1,y,light)
# brain electrode jacks and cables, over hair
c.line(36,12,36,7,ink);c.line(37,12,37,7,steel)
c.rect(35,7,4,3,ink);c.rect(35,7,3,2,'#af784f');c.set(36,7,'#f4c884')
c.line(40,12,43,8,ink);c.line(43,8,47,8,ink);c.line(47,8,49,11,ink)
c.line(42,11,44,9,'#bd6653');c.line(44,9,47,9,'#bd6653');c.line(47,9,49,12,'#bd6653')
c.rect(39,10,4,4,steelD);c.rect(40,10,2,2,light)
# tool belt at bottom
c.rect(19,58,23,4,'#302b2d');c.line(20,58,40,58,'#bc8754')
c.rect(29,58,6,4,'#d1b272');c.rect(30,59,4,2,'#3e3431');c.set(33,59,'#ead6a2')
# tools in apron loop
c.line(23,53,23,62,ink);c.line(24,53,24,62,steel)
c.rect(22,51,4,4,steelD);c.line(22,51,22,53,light);c.line(25,51,25,53,light)
c.line(37,54,37,62,steelD);c.rect(36,52,3,5,'#ac5a42');c.set(37,52,'#df9261')
# exposed raised robotic arm, disconnected from coat sleeve at right
c.poly([(46,47),(49,44),(52,45),(57,54),(56,59),(51,61),(46,57),(45,52)],ink)
c.circle(49,48,4,steelD);c.circle(49,48,2,steel);c.set(48,47,shine);c.set(49,48,ink)
c.poly([(49,51),(52,49),(56,54),(54,57),(51,56)],steel)
c.line(50,51,53,54,light);c.line(48,52,51,56,steelD)
c.circle(54,56,3,steelD);c.circle(54,56,1,light)
# upright forearm and cabling
c.poly([(52,53),(51,43),(53,40),(58,40),(59,44),(58,53),(55,56)],ink)
c.poly([(53,52),(53,44),(55,42),(57,44),(56,53)],steel)
c.line(54,45,54,51,shine);c.line(57,44,57,51,steelD)
c.path('M 52 43 L 50 46 L 51 52 L 53 54', '#c36b4d',fill=False)
c.path('M 58 43 L 60 46 L 59 52 L 57 54', '#4fa5a2',fill=False)
# articulated prosthetic hand with visible individual fingers
c.poly([(51,41),(50,37),(51,33),(53,34),(53,37),(54,37),(54,30),(56,29),(57,31),(57,36),(58,33),(60,33),(61,36),(59,42),(56,44),(53,43)],ink)
c.line(51,37,52,40,steel);c.set(51,35,light)
c.rect(55,31,1,7,light);c.set(56,30,steel);c.set(55,34,ink)
c.line(59,34,59,38,steel);c.set(59,35,light);c.set(59,37,ink)
c.poly([(53,38),(57,37),(58,39),(57,42),(54,42)],steel)
c.line(54,38,56,38,shine);c.rect(54,40,2,2,steelD);c.set(55,40,'#56dac1')
# loose signal cable from wrist to elbow
c.path('M 52 41 L 49 40 L 48 42 L 48 45', '#c7ac69',fill=False)
view(result)
save('mad-cyborg-scientist',result)
finish(result)
