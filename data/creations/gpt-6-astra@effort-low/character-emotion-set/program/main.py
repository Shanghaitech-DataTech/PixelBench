result = new_canvas(64,64,name='emotions')
ink='#252336'; hair='#543447'; light='#965568'; shine='#bd7880'; skin='#f5bf96'; shade='#d98c78'; hi='#ffdbad'; shirt='#398b94'; shirtlight='#70c2bf'
def portrait(ox,oy,mood):
 def rect(x,y,w,h,c): result.rect(ox+x,oy+y,w,h,c)
 def line(x,y,a,b,c): result.line(ox+x,oy+y,ox+a,oy+b,c)
 def poly(p,c): result.poly([(ox+x,oy+y) for x,y in p],c)
 # shoulders and collar
 poly([(5,30),(6,26),(11,24),(20,24),(25,26),(26,30)],ink)
 poly([(7,30),(8,27),(12,26),(19,26),(23,27),(24,30)],shirt)
 rect(8,27,3,3,shirtlight);rect(21,28,2,2,'#27616f')
 rect(12,22,8,5,ink);rect(13,22,6,4,shade)
 poly([(11,25),(15,28),(18,28),(21,25),(19,25),(16,26),(13,25)],ink)
 # head outline ears
 poly([(6,9),(8,5),(12,3),(20,3),(24,6),(26,10),(25,21),(22,24),(10,24),(7,21)],ink)
 rect(5,14,3,6,ink);rect(25,14,3,6,ink)
 rect(6,15,3,4,shade);rect(24,15,3,4,shade)
 poly([(9,10),(13,7),(21,8),(24,12),(24,20),(21,23),(18,25),(13,24),(9,21)],shade)
 poly([(9,10),(14,8),(21,9),(23,12),(23,20),(20,23),(14,23),(10,20)],skin)
 rect(11,12,4,2,hi)
 # hair cap and distinctive swooping bangs
 poly([(6,14),(6,9),(8,5),(11,4),(12,2),(20,2),(21,3),(24,4),(26,8),(26,14),(23,16),(22,10),(20,9),(18,12),(14,13),(15,10),(12,12),(8,13),(8,17),(7,17)],ink)
 poly([(7,10),(9,6),(13,4),(19,3),(23,5),(25,8),(25,12),(24,13),(22,8),(19,7),(17,10),(15,11),(16,8),(12,10),(8,12)],hair)
 poly([(9,7),(13,5),(19,4),(22,5),(20,6),(15,6),(12,8),(9,9)],light)
 line(13,5,18,5,shine)
 rect(24,10,1,3,light)
 # tiny matching brass hairclip
 line(8,11,10,10,'#edc66f')
 if mood=='calm':
  line(11,14,14,14,hair);line(19,14,22,14,hair)
  rect(12,16,2,3,ink);rect(20,16,2,3,ink)
  line(15,21,18,21,ink)
 elif mood=='smile':
  line(11,14,14,13,hair);line(19,13,22,14,hair)
  line(11,17,12,16,ink);line(12,16,14,17,ink)
  line(19,17,20,16,ink);line(20,16,22,17,ink)
  poly([(13,20),(20,20),(19,23),(15,23)],ink)
  rect(14,20,5,1,'#fff0d6');rect(16,22,3,1,'#d16d7d')
 elif mood=='angry':
  line(10,13,14,15,ink);line(19,15,23,13,ink)
  rect(12,16,2,3,ink);rect(20,16,2,3,ink)
  line(14,22,16,21,ink);line(16,21,19,22,ink)
 else:
  line(11,13,14,12,hair);line(19,12,22,13,hair)
  rect(11,15,4,5,ink);rect(19,15,4,5,ink)
  rect(11,15,2,3,'#fff0d6');rect(19,15,2,3,'#fff0d6')
  rect(15,21,4,3,ink);rect(16,22,2,1,'#a65065')
 # nose and cheek warmth
 result.set(ox+17,oy+19,shade)
 if mood in ('smile','calm'):
  rect(10,19,2,1,'#e89787');rect(22,19,2,1,'#e89787')
for x,y,m in [(0,0,'calm'),(32,0,'smile'),(0,32,'angry'),(32,32,'surprise')]: portrait(x,y,m)
view(result)
finish(result)
