result = new_canvas(64,32,name='swordsman_walk')
O='#172034'; C='#253957'; B='#34567b'; L='#527797'; skin='#edb887'; sh='#bd785c'; hi='#ffdab0'; hair='#be4935'; red='#ef7847'; dark='#7e3034'; steel='#91b9cc'; shine='#d8eef0'; gold='#d6a557'; boot='#65464a'
for f in range(2):
 c=new_canvas(32,32,name='pose'+str(f))
 dy=f
 # cape swept behind the shoulders, with a moving hem
 if f==0:
  c.poly([(12,10),(9,11),(8,17),(4,24),(7,25),(10,24),(13,25),(16,19),(15,12)],O)
  c.poly([(11,12),(10,17),(6,23),(9,22),(11,23),(14,19),(14,12)],C)
  c.poly([(11,13),(10,19),(8,22),(11,21),(13,16),(13,12)],B)
  c.line(10,19,7,23,L)
 else:
  c.poly([(12,11),(9,12),(8,18),(6,25),(10,24),(12,26),(15,22),(16,13)],O)
  c.poly([(11,13),(10,19),(8,23),(10,22),(12,24),(14,21),(14,13)],C)
  c.poly([(12,13),(11,20),(10,22),(12,22),(14,17)],B)
 # legs: alternate leading foot and trailing foot
 if f==0:
  c.poly([(14,20),(18,20),(17,24),(13,27),(12,28),(9,28),(10,25),(13,23)],O)
  c.poly([(14,22),(16,22),(14,25),(11,26),(12,24)],C)
  c.poly([(10,25),(13,26),(12,28),(14,28),(14,30),(8,30),(8,28)],O)
  c.line(10,27,10,29,boot)
  c.poly([(17,20),(20,20),(20,24),(23,27),(23,28),(19,28),(17,25),(16,23)],O)
  c.poly([(18,22),(19,22),(19,25),(21,27),(19,27),(17,24)],L)
  c.poly([(19,27),(22,27),(23,28),(25,28),(25,30),(19,30)],O)
  c.line(20,28,23,29,boot)
 else:
  c.poly([(16,21),(20,21),(20,25),(17,28),(14,28),(16,24)],O)
  c.line(18,23,17,26,C)
  c.rect(14,27,4,3,O);c.rect(15,28,2,1,boot)
  c.poly([(13,21),(17,21),(16,25),(15,27),(17,28),(19,28),(19,30),(13,30),(12,27),(13,24)],O)
  c.line(14,23,14,26,L); c.line(14,28,17,29,boot)
 # tunic and cuirass
 c.poly([(12,11+dy),(16,10+dy),(20,13+dy),(20,18+dy),(21,21+dy),(13,22+dy),(12,18+dy)],O)
 c.poly([(14,12+dy),(17,12+dy),(19,14+dy),(18,18+dy),(14,18+dy)],B)
 c.line(14,13+dy,14,16+dy,steel)
 c.rect(14,19+dy,6,2,boot); c.rect(17,19+dy,2,1,gold)
 c.line(14,21+dy,19,21+dy,C)
 # head and red hair silhouette
 c.poly([(12,3+dy),(15,2+dy),(18,3+dy),(20,5+dy),(20,7+dy),(22,8+dy),(21,10+dy),(18,11+dy),(18,12+dy),(14,12+dy),(13,10+dy),(11,8+dy),(11,5+dy)],O)
 c.poly([(15,5+dy),(19,5+dy),(19,8+dy),(21,8+dy),(20,9+dy),(18,10+dy),(17,11+dy),(15,10+dy)],skin)
 c.rect(15,10+dy,2,2,sh)
 c.set(19,7+dy,O); c.set(20,8+dy,hi)
 c.poly([(11,4+dy),(13,3+dy),(16,3+dy),(19,4+dy),(20,5+dy),(17,5+dy),(16,7+dy),(14,6+dy),(14,9+dy),(12,10+dy),(12,7+dy),(10,7+dy)],dark)
 c.poly([(12,4+dy),(16,3+dy),(18,4+dy),(17,5+dy),(15,5+dy),(13,8+dy),(12,7+dy)],hair)
 c.line(13,4+dy,16,4+dy,red); c.set(12,5+dy,red)
 # shoulder and forward arm
 c.poly([(17,12+dy),(20,12+dy),(21,14+dy),(20,16+dy),(17,15+dy)],O)
 c.line(18,13+dy,20,13+dy,steel);c.line(18,14+dy,20,14+dy,L)
 c.poly([(20,15+dy),(21,16+dy),(24,16+dy),(25,18+dy),(23,19+dy),(20,18+dy),(19,17+dy)],O)
 c.line(21,17+dy,23,17+dy,skin)
 # sword held forward, long diagonal blade
 c.line(23,18+dy,25,15+dy,O)
 c.poly([(24,14+dy),(29,5+dy),(29,10+dy),(26,16+dy)],O)
 c.poly([(25,14+dy),(29,6+dy),(28,11+dy),(26,15+dy)],steel)
 c.line(25,14+dy,29,6+dy,shine)
 c.line(23,14+dy,27,16+dy,O)
 c.line(23,14+dy,26,15+dy,gold)
 c.set(24,17+dy,hi);c.set(23,19+dy,gold)
 result.blit(c,32*f,0)
view(result,scale=8)
save('swordsman_walk',result)
finish(result)
