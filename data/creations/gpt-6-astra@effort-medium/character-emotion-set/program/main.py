result = new_canvas(64,64,name='emotion_set')
ink='#252334'
hair='#704451'; light='#b87569'; shade='#493346'
skin='#efb58b'; bright='#ffd3a1'; shadow='#cd846d'
shirt='#427f89'; shirtlight='#78b4af'
def portrait(ox,oy,emotion):
 c=new_canvas(32,32)
 # shoulders, matching high collar jacket
 c.poly([(5,30),(6,26),(10,24),(12,23),(20,23),(23,24),(26,26),(27,30)],ink)
 c.poly([(7,29),(8,26),(12,25),(20,25),(24,26),(25,29)],shirt)
 c.line(9,26,9,28,shirtlight);c.line(23,26,23,28,'#305663')
 c.rect(13,21,6,5,ink);c.rect(14,22,4,4,shadow)
 c.poly([(11,24),(14,25),(16,28),(12,27)],shirtlight)
 c.poly([(20,24),(18,25),(16,28),(20,27)],shirtlight)
 c.line(16,28,16,29,ink)
 # consistent tousled hair silhouette
 c.poly([(4,12),(3,9),(5,9),(5,6),(8,6),(9,3),(13,4),(16,2),(19,3),(23,3),(23,5),(26,6),(27,10),(27,17),(25,21),(22,23),(9,23),(6,21),(5,17)],ink)
 c.poly([(5,10),(7,7),(10,7),(10,5),(14,6),(16,4),(20,5),(22,5),(22,7),(25,7),(25,19),(22,21),(9,21),(6,18)],hair)
 # ears
 c.rect(5,14,4,5,ink);c.rect(6,15,3,3,skin)
 c.rect(23,14,4,5,ink);c.rect(23,15,3,3,shadow)
 # face
 c.poly([(9,9),(21,9),(24,12),(24,19),(22,23),(19,25),(13,25),(9,23),(7,19),(7,13)],ink)
 c.poly([(10,10),(20,10),(23,12),(23,19),(21,22),(18,24),(13,24),(10,22),(8,19),(8,13)],skin)
 c.poly([(9,12),(12,10),(20,11),(21,13),(21,19),(19,22),(12,22),(9,19)],bright)
 c.line(11,23,13,24,shadow);c.line(20,22,22,20,shadow)
 # fringe shapes across forehead, identical in every tile
 c.poly([(6,11),(8,7),(13,7),(17,5),(23,7),(25,11),(24,15),(21,12),(21,10),(18,12),(18,9),(14,12),(14,10),(10,13),(10,11),(7,15)],ink)
 c.poly([(6,10),(9,8),(13,8),(17,6),(22,7),(24,10),(23,12),(21,9),(18,10),(18,8),(14,10),(14,9),(10,11),(10,9),(7,12)],hair)
 c.line(9,8,12,8,light);c.line(14,7,17,6,light);c.line(18,6,21,7,light)
 c.set(7,10,light)
 # nose and warm cheeks
 c.set(16,18,shadow);c.line(10,19,11,19,'#e59a83');c.line(21,19,22,19,'#e59a83')
 if emotion=='calm':
  c.line(10,14,13,14,hair);c.line(19,14,22,14,hair)
  c.line(10,16,13,16,ink);c.line(19,16,22,16,ink)
  c.set(12,17,ink);c.set(20,17,ink)
  c.line(14,21,18,21,ink)
 elif emotion=='smile':
  c.line(10,13,13,13,hair);c.line(19,13,22,13,hair)
  c.poly([(10,17),(11,15),(12,15),(14,17)],ink,fill=False)
  c.poly([(18,17),(20,15),(21,15),(22,17)],ink,fill=False)
  c.rect(13,20,7,2,ink);c.rect(14,21,5,2,ink);c.rect(14,20,5,1,'#fff0d1');c.line(15,22,17,22,'#c76e78')
 elif emotion=='angry':
  c.line(9,13,14,15,ink);c.line(18,15,23,13,ink)
  c.line(10,16,13,16,ink);c.set(12,17,ink)
  c.line(19,16,22,16,ink);c.set(20,17,ink)
  c.line(14,22,15,21,ink);c.line(15,21,18,21,ink);c.set(19,22,ink)
 else:
  c.line(10,13,13,12,hair);c.line(19,12,22,13,hair)
  c.rect(10,15,4,4,ink);c.rect(19,15,4,4,ink)
  c.rect(11,15,2,3,'#fff0d1');c.rect(20,15,2,3,'#fff0d1');c.line(12,16,12,18,ink);c.line(20,16,20,18,ink)
  c.rect(15,20,3,4,ink);c.set(16,23,'#b96670')
 result.blit(c,ox,oy)
portrait(0,0,'calm')
portrait(32,0,'smile')
portrait(0,32,'angry')
portrait(32,32,'surprised')
view(result)
finish(result)
