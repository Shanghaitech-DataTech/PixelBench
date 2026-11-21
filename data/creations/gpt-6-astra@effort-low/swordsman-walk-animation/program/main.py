result = new_canvas(64,32)
ink='#192033'; navy='#233451'; blue='#344e72'; lightblue='#4b6a8b'; red='#a73537'; hair='#d95337'; gold='#ef8b48'; skin='#e5ac80'; shade='#b97561'; steel='#92b5c6'; shine='#deedf0'; armor='#55798d'; dark='#303b50'; boot='#57434b'
for i in range(2):
 c=new_canvas(32,32)
 bob=i
 # cape flowing behind the shoulders
 c.poly([(12,10+bob),(9,11+bob),(7,16),(3+i,22),(4,25),(9,24),(13,21),(15,13+bob)],ink)
 c.poly([(11,12+bob),(9,14),(8,18),(5+i,23),(8,23),(12,20),(13,13+bob)],navy)
 c.line(10,14+bob,7+i,21,blue)
 c.line(9,22,11,18,lightblue)
 # legs, swapping the leading foot
 if i==0:
  c.poly([(12,20),(15,20),(13,25),(10,28),(6,28),(6,26),(9,25)],ink)
  c.line(12,23,10,26,armor); c.line(7,27,10,27,boot)
  c.poly([(14,20),(17,20),(18,24),(21,27),(21,29),(16,29),(16,27),(14,25)],ink)
  c.line(16,22,16,25,steel); c.line(17,26,19,28,boot); c.set(17,28,'#8b6260')
 else:
  c.poly([(14,21),(17,21),(16,25),(12,28),(8,28),(8,26),(12,25)],ink)
  c.line(15,23,13,26,armor); c.line(9,27,12,27,boot)
  c.poly([(11,21),(14,21),(16,25),(19,27),(19,29),(15,29),(13,26)],ink)
  c.line(13,23,15,26,steel); c.line(15,27,17,28,boot)
 # torso and tunic
 c.poly([(12,10+bob),(16,10+bob),(18,14+bob),(17,21+bob),(11,21+bob),(10,17+bob)],ink)
 c.poly([(12,12+bob),(15,12+bob),(16,15+bob),(15,19+bob),(12,19+bob)],armor)
 c.line(12,13+bob,12,17+bob,steel)
 c.rect(11,19+bob,6,2,'#75504d'); c.set(15,19+bob,'#edbd70')
 # head profile
 c.poly([(11,3+bob),(16,3+bob),(18,5+bob),(18,7+bob),(20,8+bob),(18,9+bob),(18,11+bob),(14,12+bob),(11,9+bob)],ink)
 c.poly([(14,5+bob),(17,5+bob),(17,7+bob),(19,8+bob),(17,9+bob),(17,10+bob),(14,10+bob),(13,8+bob)],skin)
 c.set(17,7+bob,ink); c.set(16,10+bob,shade)
 # swept red hair
 c.poly([(10,3+bob),(12,2+bob),(16,2+bob),(18,4+bob),(17,6+bob),(14,5+bob),(13,8+bob),(11,9+bob),(10,7+bob),(9,7+bob)],red)
 c.poly([(10,4+bob),(13,3+bob),(16,3+bob),(17,4+bob),(13,4+bob),(12,7+bob),(11,6+bob)],hair)
 c.line(12,3+bob,15,3+bob,gold)
 # shoulder and reaching arm
 c.rect(14,12+bob,4,4,ink); c.rect(14,12+bob,3,2,steel); c.set(14,14+bob,armor)
 c.poly([(16,15+bob),(18,15+bob),(19,17+bob),(22,16+bob),(23,18+bob),(19,19+bob),(17,18+bob)],ink)
 c.line(17,15+bob,18,17+bob,armor); c.line(19,17+bob,21,17+bob,skin)
 # long forward-pointing sword, diagonal above hand
 c.line(22,16+bob,29,8+bob,ink); c.line(23,16+bob,30,8+bob,ink)
 c.line(23,15+bob,29,9+bob,steel); c.line(23,14+bob,29,8+bob,shine)
 c.line(21,14+bob,25,18+bob,ink); c.line(21,14+bob,24,17+bob,'#d6a359')
 c.line(22,17+bob,20,19+bob,'#855342'); c.set(22,17+bob,skin)
 result.blit(c,i*32,0)
view(result)
finish(result)
