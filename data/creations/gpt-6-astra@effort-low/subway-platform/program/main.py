result = new_canvas(64,64, '#142337', name='subway')
c=result
# station shell
c.rect(0,0,64,9,'#23364b')
c.poly([(0,0),(64,0),(64,4),(0,12)],'#31465a')
c.line(0,12,63,5,'#506579')
c.rect(0,13,64,30,'#192c40')
c.rect(0,11,64,2,'#93a8b1')
c.rect(2,12,17,1,'#e9eacb'); c.rect(35,12,24,1,'#e9eacb')
# arriving train, nose at right, light trails
c.rect(0,17,48,22,'#b6c5c5')
c.poly([(48,17),(54,19),(58,25),(58,37),(53,40),(0,40),(0,35),(49,35)],'#7e989f')
c.rect(0,20,48,10,'#294b62')
for x in [1,14,27,40]:
 c.rect(x,20,10,9,'#395e75'); c.rect(x+1,21,8,2,'#7fabb6'); c.line(x+2,27,x+8,24,'#527e95')
 c.rect(x+10,19,2,13,'#c7d2cc')
c.poly([(49,20),(53,21),(56,26),(56,30),(49,30)],'#20384c')
c.line(50,21,54,26,'#8aafb9')
c.rect(0,32,53,2,'#e69c58');c.rect(0,34,54,2,'#a75746')
c.rect(52,33,4,2,'#fff0b5')
c.rect(0,38,53,3,'#273c4c')
for x,y,w in [(0,18,9),(3,24,9),(0,28,6),(15,31,12),(0,36,18)]: c.rect(x,y,w,1,'#d1d8cb')
# platform screen doors, transparently suggested glass with blue edges
c.rect(0,40,64,3,'#0e1f30')
c.rect(0,16,64,2,'#5d7c8a')
for x in [0,16,32,48,63]:
 c.rect(x,17,2,25,'#233e50');c.line(x,18,x,39,'#96b3b8')
for x in [8,24,40,56]:
 c.line(x,19,x,39,'#547d8b'); c.rect(x-2,29,5,2,'#c0cabc'); c.set(x,29,'#e6ba60')
for x in [3,19,35,51]:
 c.line(x,36,x+4,32,'#638d99')
c.rect(0,39,64,2,'#557482')
# ground perspective and tactile strip
c.rect(0,43,64,21,'#526471')
c.rect(0,43,64,3,'#d3af63')
for x in range(0,64,3): c.set(x,44,'#856c46')
c.line(0,47,63,47,'#75858b')
c.line(0,55,63,55,'#647780')
c.line(10,63,26,47,'#394e60');c.line(44,63,40,47,'#394e60')
c.line(0,62,63,62,'#394e60')
# hanging wayfinding
c.line(7,4,7,6,'#0c1b2b');c.line(29,2,29,6,'#0c1b2b')
c.rect(4,6,33,9,'#0c1c2e');c.rect(5,7,5,5,'#d6ad59');c.text(12,7,'EAST', '#e1e6d8',font='5x7')
c.rect(47,6,13,5,'#123449');c.line(49,8,56,8,'#e2e7d9');c.line(54,6,56,8,'#e2e7d9');c.line(54,10,56,8,'#e2e7d9')
# bench
c.rect(23,47,16,2,'#283747');c.rect(24,41,14,5,'#a47e60');c.line(25,42,36,42,'#d2aa7b');c.line(25,44,36,44,'#715c50')
c.rect(23,46,16,2,'#c49769');c.rect(25,48,2,5,'#1d2d3e');c.rect(36,48,2,5,'#1d2d3e')
# shadows
c.ellipse(12,58,6,2,'#3a5060');c.ellipse(32,53,5,1,'#3a5060');c.ellipse(51,59,8,2,'#3a5060')
# standing passenger left, phone raised
c.rect(9,36,5,6,'#d6a075');c.rect(9,35,5,2,'#172332');c.set(8,37,'#172332')
c.rect(9,41,6,10,'#e0b95f');c.rect(8,43,2,7,'#aa7849');c.rect(14,43,2,4,'#e0b95f');c.line(15,46,18,42,'#d6a075');c.rect(18,40,2,3,'#172332');c.set(18,40,'#89c9cf')
c.rect(10,51,2,7,'#172332');c.rect(13,51,2,7,'#26344a');c.rect(9,58,3,1,'#0d1927');c.rect(13,58,4,1,'#0d1927')
# seated passenger bent knees
c.rect(29,35,4,5,'#bc896e');c.rect(28,34,5,2,'#242333');c.rect(29,39,5,7,'#81aba2');c.rect(28,41,2,4,'#57877e');c.line(30,44,34,45,'#dfb094')
c.rect(30,46,7,3,'#243149');c.rect(35,48,2,5,'#243149');c.rect(31,48,2,4,'#34435a');c.rect(35,53,4,1,'#111e2e');c.rect(31,52,3,1,'#111e2e')
# walking passenger right, wide stride and bag
c.rect(48,34,5,6,'#d4a185');c.rect(48,33,5,2,'#392d39');c.rect(52,35,2,3,'#392d39')
c.poly([(48,40),(52,40),(54,49),(48,51),(46,46)],'#cf7466')
c.line(47,42,44,48,'#cf7466');c.rect(43,47,2,3,'#d4a185');c.line(52,42,56,46,'#e09479');c.rect(56,46,2,2,'#d4a185')
c.poly([(48,50),(51,50),(48,55),(46,59),(43,59)],'#182638')
c.poly([(51,49),(53,49),(54,54),(58,57),(57,59),(51,55)],'#24344b')
c.rect(42,59,5,1,'#0d1927');c.rect(56,59,4,1,'#0d1927')
c.rect(42,50,5,5,'#876c55');c.rect(43,49,3,2,'#dbb984',fill=False);c.line(43,51,43,54,'#b99b70')
view(result)
finish(result)
