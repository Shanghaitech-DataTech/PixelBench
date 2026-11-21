result = new_canvas(64,64, '#20333e', name='laboratory_workbench')
c=result
# quiet tiled laboratory wall
c.rect(0,0,64,34,'#304b55')
c.rect(0,0,64,3,'#233c47')
for y in [14,28]: c.line(0,y,63,y,'#395963')
for x in [15,36,57]: c.line(x,3,x,27,'#395963')
# wall shelf and mounted light
c.rect(39,7,21,2,'#162c38'); c.rect(40,6,19,1,'#65808a')
c.rect(43,9,2,3,'#20333e'); c.rect(56,9,2,3,'#20333e')
c.rect(4,5,24,3,'#162c38'); c.rect(5,6,22,1,'#d1e6cf')
# bench surface, front lip and cabinetry
c.poly([(0,34),(63,34),(63,53),(0,53)],'#7d938c')
c.line(0,34,63,34,'#b4c1a7')
c.rect(0,53,64,4,'#283c43'); c.line(0,53,63,53,'#d0c9a1')
c.rect(0,57,64,7,'#42555b'); c.line(0,57,63,57,'#172b37')
for x in [2,23,44]:
 c.rect(x,59,18,5,'#53666a'); c.rect(x+6,60,7,1,'#192e39'); c.rect(x+7,61,5,1,'#83928c')
# equipment shadows
c.ellipse(17,45,13,3,'#566f70'); c.ellipse(45,36,15,2,'#566f70')
c.ellipse(47,47,14,3,'#607976')
# bottles on back right, varied shapes with broad blank labels
c.rect(54,19,6,3,'#132d38'); c.rect(55,22,4,2,'#d5c8a0')
c.poly([(54,24),(59,24),(61,27),(61,35),(52,35),(52,27)],'#233b44')
c.poly([(55,24),(58,24),(60,27),(60,34),(53,34),(53,27)],'#b17c44')
c.rect(54,28,6,4,'#e4dfba'); c.line(54,33,59,33,'#805038'); c.line(54,26,54,27,'#e9ba6b')
c.rect(43,22,5,3,'#142c39'); c.rect(44,25,3,2,'#82b2b2')
c.poly([(43,27),(47,27),(49,29),(49,35),(41,35),(41,29)],'#193741')
c.poly([(44,27),(46,27),(48,29),(48,34),(42,34),(42,29)],'#4f9296')
c.rect(42,30,6,3,'#e3dfbb'); c.set(43,28,'#b4d9cd')
# rack: five tubes with visible rounded bottoms and colored contents
c.rect(30,37,20,2,'#253c43')
for x,fluid in [(31,'#e6ac67'),(35,'#6ec3bf'),(39,'#a9bc77'),(43,'#d2887e'),(47,'#72b6c1')]:
 c.rect(x,28,3,9,'#234650'); c.rect(x+1,29,1,7,'#b5d6ce')
 c.rect(x+1,33,1,3,fluid); c.line(x,28,x+2,28,'#d9e7d8')
# warm wooden rack two rails and feet
c.rect(29,31,22,2,'#b98b57'); c.line(29,31,50,31,'#e1bb7d')
c.rect(29,33,2,6,'#795d43'); c.rect(49,33,2,6,'#795d43')
c.rect(29,38,22,2,'#ac7d4e'); c.line(30,38,49,38,'#dbaf70')
# microscope curved arm behind optical assembly
c.path('M 18 21 L 23 22 Q 29 27 26 36 L 23 42 L 18 42 L 21 35 Q 24 28 18 27 Z','#172c39')
c.path('M 19 23 L 22 23 Q 27 28 24 35 L 21 40 L 19 40 L 23 32 Q 24 27 19 26 Z','#8da7a6')
c.path('M 22 24 Q 26 28 24 33','#d0d9c4',fill=False)
# foot
c.poly([(10,40),(22,40),(27,44),(26,46),(7,46),(6,44)],'#172c39')
c.poly([(11,40),(21,40),(25,43),(25,44),(8,44)],'#9eafaa')
c.line(9,42,20,42,'#d3decb'); c.line(8,45,25,45,'#526c76')
# stage, slide and condenser
c.rect(12,34,5,5,'#253e49'); c.rect(13,35,3,2,'#708e94')
c.rect(7,31,17,3,'#152b37'); c.line(8,31,23,31,'#718d93')
c.rect(10,30,9,1,'#c2dcd0'); c.rect(14,30,2,1,'#719c9e')
# diagonal eyepiece and barrel
c.poly([(9,15),(13,13),(20,23),(16,27)],'#162c39')
c.poly([(11,16),(13,15),(18,23),(16,25)],'#b4c7be')
c.line(11,17,15,23,'#e1e6cf')
c.poly([(8,14),(11,12),(14,15),(10,18)],'#142834')
c.line(9,14,11,13,'#698b95')
# turret and two objectives
c.rect(14,24,7,3,'#36515a'); c.line(14,24,19,24,'#dae0c5')
c.rect(14,27,3,3,'#afc1b7'); c.rect(14,29,3,1,'#152f3c')
c.line(19,27,20,29,'#d1d9bf'); c.set(20,30,'#162e39')
# focusing wheel
c.circle(24,29,3,'#162c39'); c.circle(24,29,2,'#557883'); c.set(23,28,'#b0c7bf'); c.set(24,30,'#304b58')
# open notebook, page block and bent leaves
c.poly([(34,42),(43,43),(47,41),(57,43),(60,50),(48,51),(44,52),(32,49)],'#344e53')
c.poly([(34,41),(44,43),(47,41),(56,42),(59,49),(48,50),(44,51),(32,48)],'#bba97f')
c.poly([(34,40),(40,40),(44,42),(44,49),(39,47),(32,47)],'#e3d9af')
c.poly([(44,42),(48,40),(55,41),(58,48),(49,48),(44,49)],'#f1e6bf')
c.line(44,43,44,49,'#a39373')
# diagram and orderly writing marks, no tiny text
c.line(35,42,40,43,'#879588'); c.line(35,44,40,45,'#879588')
c.line(35,46,38,46,'#879588')
c.rect(49,42,3,3,'#8faaa0',fill=False); c.line(48,46,54,46,'#a0ab93')
# foreground glass dropper, distinct bulb and slim pipette
c.line(19,50,30,46,'#3e5a60'); c.line(18,49,28,46,'#daead7'); c.line(19,50,29,47,'#7fa6a7')
c.poly([(27,45),(30,44),(32,45),(32,47),(29,48),(27,47)],'#19333e')
c.line(29,45,31,45,'#4f7180'); c.set(17,50,'#d7e5d0')
assert c.stats()['colors_used'] <= 86
save('laboratory_workbench', result)
view(c)
finish(result)
