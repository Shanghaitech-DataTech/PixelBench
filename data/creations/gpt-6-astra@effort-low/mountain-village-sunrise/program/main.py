import random
random.seed(8)
c=new_canvas(128,128,background='#f6bd87',name='Sunrise village')
# sky bands
for y,col in [(0,'#7c7899'),(12,'#a58ba2'),(23,'#cf9a9e'),(33,'#e9ac96'),(43,'#f6bd87'),(53,'#ffd392')]: c.rect(0,y,128,12,col)
c.circle(65,42,13,'#ffe5a6'); c.circle(65,42,10,'#fff0bd')
# slender illuminated clouds
for x,y,w in [(10,28,22),(4,30,14),(85,21,27),(94,23,24),(31,16,18)]:c.rect(x,y,w,1,'#e5b2b0')
# mountain planes
c.poly([(0,58),(0,39),(10,45),(26,23),(45,47),(59,34),(78,53),(98,28),(122,49),(127,44),(127,72)],'#8d829e')
c.poly([(10,45),(26,23),(45,47),(28,36),(22,38),(19,34)],'#c7adbb')
c.poly([(78,53),(98,28),(122,49),(105,42),(99,36),(94,41),(92,39)],'#d8b4bd')
c.poly([(0,61),(17,46),(29,58),(48,42),(72,63),(86,49),(105,60),(118,46),(127,53),(127,80),(0,80)],'#777e95')
c.poly([(0,71),(20,59),(38,67),(60,54),(79,65),(102,56),(127,65),(127,89),(0,89)],'#627d84')
# valley base
c.poly([(0,80),(29,73),(61,78),(92,71),(127,80),(127,128),(0,128)],'#697c66')
c.poly([(0,98),(42,80),(75,83),(127,91),(127,128),(0,128)],'#89916b')
c.poly([(0,116),(32,101),(68,99),(99,103),(127,94),(127,128),(0,128)],'#a19a70')
def pine(x,y,h, dark, light):
 c.rect(x-1,y-h+4,2,h,'#554e4e')
 for k in range(3):
  top=y-h+k*h//5; base=top+h//2; w=3+k*2+h//9
  c.poly([(x,top),(x-w,base),(x+w,base)],dark)
  c.poly([(x,top),(x-w,base),(x-1,base-2)],light)
for x,y,h in [(4,80,20),(14,78,16),(29,77,19),(38,77,13),(88,76,16),(103,79,22),(115,80,17),(124,81,23)]:pine(x,y,h,'#45676a','#608179')
# path with darker border
c.poly([(61,81),(68,81),(72,94),(65,103),(73,111),(91,128),(55,128),(52,116),(51,107),(58,95)],'#686c62')
c.poly([(62,81),(67,81),(69,94),(61,105),(66,114),(83,128),(59,128),(55,115),(54,107),(60,94)],'#b4aa8a')
# individual paving stones
for y in range(87,128,5):
 center=64 if y<97 else (58 if y<113 else 58+(y-113))
 width=3+(y-87)//6
 for x in range(center-width,center+width,6):
  c.poly([(x,y),(x+4,y-1),(x+5,y+1),(x+3,y+3),(x-1,y+2)],random.choice(['#d4c5a0','#c3b795','#968f78']))
# houses, centered largest

def house(x,y,w,h):
 # ground shadow
 c.ellipse(x+w//2+3,y+h+2,w//2+7,4,'#66735f')
 c.rect(x,y,w,h,'#664c46');c.rect(x+2,y+1,w-4,h-2,'#a16b4c')
 c.rect(x+w-7,y,7,h,'#795341')
 for yy in range(y+4,y+h,4):
  c.line(x+1,yy,x+w-2,yy,'#714d3e');c.line(x+3,yy+1,x+w-9,yy+1,'#bb8155')
 for xx in [x+1,x+w-3]:c.rect(xx,y,2,h,'#d09a61')
 # chimney
 c.rect(x+w-10,y-15,5,13,'#756368');c.rect(x+w-11,y-16,7,3,'#b7a18e')
 # roof silhouette and lit slope
 c.poly([(x-4,y+2),(x+w//2,y-18),(x+w+4,y+2)],'#493f4d')
 c.poly([(x-2,y-1),(x+w//2,y-16),(x+w+1,y-1)],'#824f49')
 c.poly([(x-2,y-1),(x+w//2,y-16),(x+w//2-2,y-2)],'#ba7355')
 for yy in range(y-11,y,4):
  delta=(y-yy)* (w//2+3)//19
  c.line(x+delta,yy,x+w-delta,yy,'#d18a61')
 c.line(x-4,y+2,x+w+4,y+2,'#3e4044')
 c.line(x-3,y-1,x+w//2,y-18,'#edb276')
 # door
 c.rect(x+w//2-3,y+h-13,7,13,'#493f3c');c.rect(x+w//2-2,y+h-12,4,11,'#795844');c.set(x+w//2+2,y+h-6,'#efc077')
 # windows
 for xx in [x+4,x+w-10]:
  c.rect(xx-1,y+5,7,8,'#493f3c');c.rect(xx,y+6,5,5,'#ffcf78');c.rect(xx,y+6,2,2,'#ffebaf');c.line(xx+2,y+6,xx+2,y+10,'#996944');c.line(xx,y+8,xx+4,y+8,'#996944');c.rect(xx-1,y+12,7,1,'#d6a46c')
 c.rect(x+w//2-5,y+h,11,2,'#c2b08c')
# smoke airy stepped wisps behind roofs
for x,y in [(29,56),(73,43),(107,57)]:
 c.path(f'M {x} {y+10} Q {x-4} {y+4} {x+1} {y} Q {x+6} {y-5} {x+1} {y-9} L {x-2} {y-9} Q {x+2} {y-4} {x-3} {y} Q {x-6} {y+6} {x-2} {y+10} Z','#d2b7aa')
house(12,76,29,22)
house(89,77,26,21)
house(45,65,37,28)
# center front porch
c.rect(57,94,15,2,'#dfc49b');c.rect(56,96,17,2,'#807965')
# foreground framing trees
pine(5,116,42,'#294f50','#42685b');pine(120,119,45,'#294f50','#42685b')
pine(17,126,30,'#28494c','#3f6355')
# meadow pixel clusters
for i in range(170):
 x=random.randrange(128);y=random.randrange(99,128)
 if abs(x-(59+max(0,y-113)))<13 or x<23 or x>113:continue
 col=random.choice(['#78865c','#c0ae75','#8a8b60'])
 c.line(x,y,x+2,y,col)
 if i%4==0:c.set(x+1,y-1,col)
# rocks and wildflowers
for x,y in [(39,114),(96,116),(46,103),(104,105),(33,124)]:
 c.poly([(x-2,y),(x,y-3),(x+3,y-2),(x+4,y+1),(x-2,y+1)],'#777c70');c.line(x,y-3,x+2,y-3,'#bcb498')
for x,y in [(28,107),(32,111),(93,106),(101,122),(42,121),(88,119)]:
 c.line(x,y,x,y-3,'#637650');c.set(x,y-4,'#f2c77e');c.set(x+1,y-4,'#f8d995')
view(c)
finish(c)
