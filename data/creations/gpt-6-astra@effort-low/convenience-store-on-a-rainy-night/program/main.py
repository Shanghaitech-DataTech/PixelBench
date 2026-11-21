c = new_canvas(64,64, '#131d32', name='Rainy corner store')
# Night and distant structures
c.rect(0,13,10,31,'#1b2a40'); c.rect(3,10,6,32,'#1b2a40')
c.rect(55,8,9,38,'#19283d')
c.rect(58,15,3,5,'#2c4051'); c.rect(0,29,7,3,'#344251')
# wet pavement
c.rect(0,44,64,20,'#24354a')
c.poly([(0,53),(63,46),(63,64),(0,64)],'#293d51')
c.line(0,48,63,48,'#526075')
c.line(0,50,63,50,'#18283d')
# store shadow, side wall and main facade
c.rect(8,18,49,29,'#101c2d')
c.poly([(6,20),(12,17),(12,44),(6,47)],'#344356')
c.rect(11,18,44,27,'#657379')
c.rect(13,22,40,21,'#213846')
# warm glass bays
c.rect(14,24,22,17,'#f4cb79')
c.rect(15,25,20,3,'#ffe6a1')
c.rect(15,28,20,12,'#c79158')
# shelves and merchandise
for x,col in [(16,'#edc987'),(20,'#7e9b83'),(24,'#e4b365'),(28,'#a77664'),(32,'#86a9a1')]:
 c.rect(x,29,2,3,col); c.rect(x,35,2,3,col)
c.rect(15,32,20,1,'#755746'); c.rect(15,38,20,2,'#795b4a')
c.line(15,33,35,33,'#ffe1a0')
# entrance with visible lit floor
c.rect(38,24,14,19,'#ffe2a0')
c.rect(40,27,10,13,'#d4a46b')
c.poly([(39,39),(50,38),(52,43),(38,43)],'#f6ce83')
# glass reflection diagonals
c.line(15,30,20,25,'#ffe9b1'); c.line(15,34,24,25,'#e7d79a')
c.line(29,35,34,30,'#e6c98b')
c.rect(25,24,1,17,'#46616a'); c.rect(36,23,2,20,'#344c56')
c.rect(13,41,24,2,'#77888a')
# door frame and open door
c.poly([(39,25),(44,27),(44,43),(39,42)],'#6d8d8b')
c.poly([(40,27),(43,28),(43,40),(40,40)],'#a3b9a1')
c.line(42,33,42,35,'#fbe3a0')
c.line(51,24,51,43,'#47616a')
# canopy and sign, fictional generic lettering
c.rect(8,12,48,10,'#132a39')
c.rect(9,12,46,8,'#5b9294')
c.rect(11,13,42,6,'#b7d2b8')
c.text(17,13,'OPEN', '#294f5c',spacing=2)
c.rect(8,20,48,3,'#326a73')
for x in range(10,55,6): c.rect(x,20,3,2,'#548e91')
c.line(9,23,54,23,'#fff0ba')
c.line(12,11,53,11,'#364b60')
# threshold and cast light
c.rect(37,44,17,2,'#9b9d84')
c.poly([(38,46),(51,46),(59,54),(32,54)],'#4b5654')
for x,y,w,col in [(34,49,17,'#8b8261'),(37,51,18,'#b09b69'),(31,54,26,'#7a7860'),(35,57,16,'#a18e66'),(39,60,11,'#6d7669'),(12,52,13,'#6c7464'),(15,55,13,'#968a65'),(9,58,18,'#50656b')]:
 c.rect(x,y,w,1,col)
c.line(33,55,47,55,'#c4aa73'); c.line(42,58,54,58,'#465e69')
# umbrella rack left of entry
c.rect(28,40,7,6,'#233c4b'); c.rect(28,41,7,1,'#8babad')
c.rect(29,43,1,3,'#5f7d85'); c.rect(33,43,1,3,'#5f7d85')
for x,y,col in [(29,34,'#b86c70'),(32,35,'#699fa7'),(34,33,'#d2ad73')]:
 c.line(x,y,x,43,col); c.set(x-1,y,col); c.set(x-1,y+1,col)
# bicycle wheels and frame
for x in [9,23]:
 c.circle(x,47,5,'#111e2f'); c.circle(x,47,4,'#8198a4',False)
 c.line(x-3,47,x+3,47,'#3d566b'); c.line(x,44,x,50,'#3d566b')
c.line(9,47,13,40,'#75b4b7'); c.line(13,40,18,47,'#75b4b7'); c.line(18,47,9,47,'#75b4b7')
c.line(13,40,21,40,'#75b4b7'); c.line(21,40,18,47,'#75b4b7'); c.line(21,39,23,47,'#a0c9c5')
c.line(20,37,21,40,'#bacbc5'); c.line(20,37,23,37,'#bacbc5')
c.line(13,40,12,38,'#bcc8bd'); c.line(10,38,14,38,'#101c2b')
c.set(18,47,'#e4c58c'); c.line(18,47,20,49,'#b8c2b4')
# raincoated customer, stepping into door
c.line(47,42,46,47,'#172a39'); c.line(50,42,51,45,'#172a39')
c.line(45,47,47,47,'#0e1c2d'); c.line(51,45,53,45,'#0e1c2d')
c.poly([(46,32),(50,32),(51,37),(52,42),(44,42),(45,37)],'#d99b42')
c.poly([(46,33),(48,33),(48,39),(46,41),(45,41)],'#f4c963')
c.circle(48,30,3,'#e7b651'); c.rect(48,29,3,4,'#9b6b45'); c.rect(49,29,2,3,'#edc58b')
c.line(46,28,49,28,'#ffe08b')
c.line(46,35,43,37,'#f0bf59'); c.set(43,36,'#edc58b')
c.line(50,35,51,39,'#ae733c')
# sparse rain and puddle rings, kept clear of focal details
for x,y in [(3,3),(16,2),(27,5),(41,1),(53,3),(60,5),(6,15),(1,36),(58,29),(61,38),(4,54),(29,47),(58,56),(24,59),(2,23),(59,18),(36,7)]:
 c.line(x,y,x-1,y+3,'#52738a')
for x,y in [(7,59),(29,56),(58,50),(19,62)]:
 c.line(x-2,y,x+2,y,'#638294'); c.set(x-3,y-1,'#405b72'); c.set(x+3,y-1,'#405b72')
c.set(8,24,'#a0c9c5'); c.line(55,24,55,27,'#7799a6')
view(c)
finish(c)
