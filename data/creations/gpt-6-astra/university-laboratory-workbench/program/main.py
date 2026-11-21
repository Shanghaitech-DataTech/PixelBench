c = new_canvas(64,64,background='#263e49',name='University laboratory')
# restrained palette
ink='#172b38'; wall='#385864'; grout='#304d59'; light='#a8d2cf'
wood='#b59068'; edge='#785f4d'; ivory='#d5dfcf'; white='#edf0da'; steel='#83a8aa'; shade='#537c87'
# tiled backsplash, and the rear bench lip
c.rect(0,0,64,29,wall)
for y in [9,22]: c.line(0,y,63,y,grout)
for x in [5,25,45]: c.line(x,0,x,8,grout)
for x in [15,35,55]: c.line(x,10,x,21,grout)
for x in [5,25,45]: c.line(x,23,x,28,grout)
c.rect(0,28,64,3,ink).line(0,28,63,28,'#6a8a8a')
# wooden work surface and solid front fascia
c.rect(0,31,64,27,wood)
c.line(0,31,63,31,'#d6b587')
c.rect(0,58,64,6,edge).line(0,58,63,58,'#dfba85').line(0,60,63,60,'#4c4540')
for x,y,n in [(1,39,5),(29,34,5),(3,53,6),(29,55,4),(58,53,5),(4,56,9),(30,39,5)]: c.line(x,y,x+n,y,'#a48160')
# shadows anchor objects
c.ellipse(18,48,14,3,'#8c7258')
c.ellipse(48,43,13,3,'#8c7258')
c.ellipse(38,31,5,2,'#8c7258')
c.ellipse(53,30,6,2,'#8c7258')
# amber reagent bottle with stopper and a broad blank paper label
c.rect(33,19,4,3,ink).rect(32,18,6,3,ink).rect(33,18,4,1,steel)
c.poly([(33,21),(37,21),(37,23),(40,25),(40,31),(31,31),(31,25),(33,23)],ink)
c.poly([(34,22),(36,22),(36,24),(39,26),(39,30),(32,30),(32,26),(34,24)],'#a7653d')
c.line(32,26,32,29,'#dcaa63').rect(33,26,6,3,ivory).rect(35,27,3,1,'#79928b')
# taller clear blue wash/reagent bottle
c.rect(50,15,6,3,ink).rect(51,15,4,1,light)
c.poly([(51,18),(55,18),(55,21),(58,23),(58,30),(48,30),(48,23),(51,21)],ink)
c.poly([(52,18),(54,18),(54,22),(57,24),(57,29),(49,29),(49,24),(52,22)],'#65969c')
c.rect(49,26,8,3,'#397781').line(50,23,50,27,'#b2ddd3')
c.rect(52,24,4,4,white).rect(53,25,2,1,'#779c9c')
# microscope: curved supporting arm behind the optical train
c.path('M 20 23 L 25 23 Q 30 25 29 33 L 26 43 L 21 43 L 24 33 Q 25 29 21 29 Z',ink)
c.path('M 22 24 L 25 24 Q 28 26 27 32 L 24 42 L 22 42 L 25 32 Q 26 28 22 27 Z',ivory)
c.line(26,26,27,29,white)
# foot with sloped shoulders
c.poly([(11,43),(22,42),(28,45),(29,48),(7,48),(7,46)],ink)
c.poly([(12,43),(22,43),(26,45),(27,46),(9,46)],ivory)
c.line(10,45,17,45,white).line(8,47,28,47,shade)
# pillar and mirror / illumination source
c.rect(19,37,4,6,ink).rect(20,38,2,5,steel)
c.ellipse(15,42,4,2,ink).line(12,41,17,41,light).line(14,40,17,40,white)
# stage with a slide
c.rect(8,34,16,4,ink).rect(9,34,14,1,steel)
c.line(11,33,19,33,'#deeee0').set(16,33,'#d47c64')
c.line(10,35,22,35,'#496c77')
# angled eyepiece, optical body, objective turret
c.poly([(11,19),(15,16),(23,26),(18,30)],ink)
c.poly([(13,19),(15,18),(21,26),(18,28)],ivory)
c.line(14,19,19,25,white)
c.poly([(9,17),(13,14),(16,17),(12,20)],ink)
c.line(10,16,12,15,steel).line(12,18,14,17,'#496c77')
c.poly([(18,28),(22,26),(24,28),(20,31)],ink)
c.line(18,29,18,32,steel).line(21,29,22,31,ivory).set(22,32,ink)
# focusing wheel
c.circle(26,32,3,ink).circle(26,32,2,shade).set(25,31,light).set(26,32,steel)
# test tubes on right, colored fluids with glass edge highlights
for x,top,fluid in [(40,30,'#6cb9a6'),(46,29,'#ce796b'),(52,31,'#d9bf68')]:
    c.rect(x,top,4,11,ink)
    c.rect(x+1,top+1,2,9,'#94c5c3')
    c.rect(x+1,top+6,2,4,fluid)
    c.line(x+1,top+1,x+1,top+4,'#d4eee0')
    c.line(x,top,x+3,top,'#d4eee0')
    c.line(x+1,41,x+2,41,ink)
# wooden rack: upper rail, legs, bottom shelf
c.rect(37,35,22,3,ink).rect(38,35,20,2,'#d5a15f')
for x in [40,46,52]: c.rect(x,35,4,1,'#745345')
c.rect(37,38,3,6,ink).rect(38,38,1,5,'#d4a66b')
c.rect(56,38,3,6,ink).rect(57,38,1,5,'#d4a66b')
c.rect(37,43,22,2,ink).rect(38,43,20,1,'#d5a15f')
# open notebook, two separate pages and folded spine
c.poly([(34,47),(44,48),(47,47),(57,47),(60,57),(48,59),(44,58),(32,57)],'#8c7258')
c.poly([(33,46),(44,47),(47,46),(57,46),(60,56),(48,58),(44,57),(31,56)],ink)
c.poly([(34,46),(43,48),(45,55),(33,54)],'#e2d6b3')
c.poly([(45,48),(48,47),(56,47),(58,55),(48,56)],white)
c.line(44,48,46,55,'#9a9e8a')
c.line(33,55,44,56,'#b6b69a').line(48,57,59,56,'#a8ae99')
# notebook contains an intelligible little plotted curve, and ruled notes
c.line(48,49,48,53,'#7b9a9a').line(48,53,55,53,'#7b9a9a')
c.line(49,52,51,52,'#4b7d83').line(51,52,53,49,'#4b7d83').line(53,49,54,50,'#4b7d83')
c.line(35,49,41,50,'#9a9e8a').line(35,51,41,52,'#9a9e8a').line(36,53,39,53,'#9a9e8a')
# glass dropper laid diagonally in foreground: rubber bulb then long narrow pipette
c.line(11,54,25,51,'#8c7258')
c.line(15,53,27,50,ink).line(15,52,25,50,'#d4eee0')
c.line(16,53,24,51,'#79b4b4').set(27,50,light)
c.poly([(8,53),(9,51),(13,50),(16,51),(16,53),(11,55),(9,55)],ink)
c.line(10,52,13,51,shade).line(14,51,15,53,steel)
view(c)
save('laboratory_workbench',c)
finish(c)
