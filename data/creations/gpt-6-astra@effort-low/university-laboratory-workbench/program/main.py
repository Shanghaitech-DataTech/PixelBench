result = new_canvas(64,64,background='#c5d7d4',name='lab_workbench')
c=result
ink='#263d49'; shadow='#587778'; light='#e9f1df'; steel='#a3bfbd'; blue='#527e8b'
# tiled laboratory wall
c.rect(0,0,64,33,'#c6d8d4')
for y in (8,20,32): c.line(0,y,63,y,'#b1c8c6')
for x in (12,36,60): c.line(x,0,x,7,'#b1c8c6'); c.line(x,21,x,31,'#b1c8c6')
for x in (0,24,48): c.line(x,9,x,19,'#b1c8c6')
# back ledge and bench
c.rect(0,32,64,3,ink); c.rect(0,33,64,2,blue)
c.rect(0,35,64,23,'#a99377')
c.line(0,36,63,36,'#ccb797')
c.rect(0,58,64,3,'#655e54'); c.line(0,58,63,58,'#e0c59d')
c.rect(0,61,64,3,'#344c55')
# cast shadows
c.ellipse(17,43,14,3,'#7c7c69')
c.ellipse(47,40,14,2,'#7c7c69')
c.ellipse(41,54,18,2,'#7c7c69')
# microscope foot
c.poly([(5,40),(9,38),(24,38),(29,42),(29,44),(5,44)],ink)
c.poly([(7,40),(12,39),(23,39),(26,42),(7,42)],steel)
c.line(8,40,20,40,light)
# curved support upright
c.path('M 21 18 Q 29 18 28 27 L 25 38 L 19 38 L 22 28 Q 24 23 19 23 Z',ink)
c.path('M 23 20 Q 27 22 25 29 L 23 36 L 21 36 L 24 26 L 22 22 Z',blue)
c.line(24,22,25,25,steel)
# illuminator
c.rect(13,36,6,3,ink); c.rect(14,36,4,2,'#e8d49b')
# stage
c.rect(8,30,16,3,ink);c.line(9,30,22,30,steel)
c.line(12,29,19,29,'#e4f3ed');c.set(16,29,'#7fc3bf')
# angled optical body
c.poly([(10,11),(15,9),(22,21),(17,24)],ink)
c.poly([(12,12),(15,11),(20,20),(17,21)],steel)
c.line(12,13,17,21,light)
# eyepiece
c.poly([(8,10),(12,8),(15,12),(11,14)],ink)
c.line(9,10,12,9,blue)
# objectives
c.rect(16,23,6,2,ink);c.rect(15,25,3,4,ink);c.rect(16,25,1,3,steel)
c.line(20,25,22,27,ink); c.set(21,25,steel)
# focus knob
c.circle(25,26,3,ink);c.circle(25,26,2,steel);c.set(25,26,blue)
# bottles rear right
for x,y,w,h,col in [(33,23,9,13,'#a2653d'),(46,20,10,16,'#4c9296')]:
 c.rect(x+2,y-4,w-4,4,ink); c.line(x+2,y-3,x+w-3,y-3,blue)
 c.poly([(x+2,y),(x+w-3,y),(x+w-1,y+3),(x+w-1,y+h),(x,y+h),(x,y+3)],ink)
 c.rect(x+1,y+3,w-2,h-4,col)
 c.line(x+1,y+3,x+1,y+h-3,'#c3b985' if x==33 else '#8dc9c1')
 c.rect(x+2,y+6,w-4,5,'#eee4bf');c.line(x+3,y+8,x+w-4,y+8,'#76857b')
# test tube rack, right foreground
for x,col,level in [(40,'#ba6b72',36),(47,'#72ada1',34),(54,'#d6b865',35)]:
 c.rect(x,29,5,13,ink);c.rect(x+1,30,3,11,'#c4e1d6')
 c.rect(x+1,level,3,41-level,col);c.set(x+1,40,'#e0d9ba');c.line(x+1,31,x+1,34,'#f3f4df')
 c.line(x,29,x+4,29,light)
c.rect(37,35,23,3,'#694c3e');c.line(38,35,59,35,'#d6ab70')
c.rect(37,38,2,6,'#694c3e');c.rect(58,38,2,6,'#694c3e')
c.rect(36,43,25,2,'#694c3e');c.line(37,43,59,43,'#cb9d62')
# open notebook
c.poly([(25,46),(35,45),(41,47),(53,46),(58,54),(43,56),(39,55),(28,56)],ink)
c.poly([(26,46),(35,46),(40,48),(40,54),(29,54)],'#eadbb1')
c.poly([(41,48),(52,47),(56,53),(43,55),(41,54)],'#faf0d0')
c.line(40,48,42,54,'#ab9879')
for y in [48,50,52]: c.line(29,y,35,y,'#a4a99b')
c.line(44,49,51,48,'#a4a99b');c.line(45,51,53,50,'#a4a99b');c.line(46,53,54,52,'#a4a99b')
# dropper diagonal left foreground, rubber bulb and glass pipette
c.line(9,49,20,54,ink);c.line(10,49,20,53,'#d5e9dc');c.line(11,50,19,53,'#86b5b3');c.set(21,54,'#d5e9dc')
c.line(6,47,10,49,ink);c.line(6,48,9,49,ink);c.line(7,47,9,48,blue)
view(c)
finish(result)
