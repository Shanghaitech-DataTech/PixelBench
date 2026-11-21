f1=new_canvas(49,49,name='original')
f1.blit(input_canvas,6,1)
f2=new_canvas(49,49,name='full_draw')
# Preserve the original clothing, head and equipment; reposition the legs.
for y in range(47):
 for x in range(35):
  col=input_canvas.get(x,y)
  if col==0: continue
  if y>=42 and col==42:
   f2.set(x+6,y+1,col)
   continue
  # isolate body from bow and old projecting hands
  limit=22 if y<19 else (20 if y<26 else (22 if y<35 else 21))
  if y>=40: limit=26
  if x>limit: continue
  if 19<=y<=24 and x>=10: continue
  dx=5
  if y>=30 and x>=14: dx=8
  elif y>=36 and x<12: dx=4
  f2.set(x+dx,y+1,col)
# Palette from original: dark outline, leather, skin and green-grey armour.
O='c24'; D='c27'; M='c30'; S='c31'; H='c32'; L='c11'; K='c2'
# continuous turned torso under both arms
f2.poly([(16,20),(24,18),(29,23),(26,29),(17,28)],O)
f2.poly([(17,21),(23,19),(27,23),(24,27),(18,26)],S)
f2.line(18,21,23,20,H)
f2.poly([(18,24),(24,23),(25,26),(19,27)],M)
f2.line(18,27,25,28,'c26')
# Drawing arm, elbow carried behind the shoulder, forearm angled to cheek
f2.poly([(20,19),(23,22),(15,25),(10,23),(10,20),(20,16),(24,16),(25,19),(17,22)],O)
f2.poly([(19,20),(21,22),(15,24),(11,22),(12,20),(17,18),(19,20)],M)
f2.line(11,21,15,19,H)
f2.line(12,22,15,23,S)
f2.poly([(15,19),(21,16),(24,16),(24,19),(17,22)],K)
f2.line(16,19,22,17,L)
f2.line(16,20,19,19,'c13')
f2.line(16,19,18,21,'c36')
# Fully extended bow arm, held at shoulder height
f2.poly([(25,19),(30,18),(34,19),(41,18),(44,19),(44,23),(33,23),(29,24),(25,23)],O)
f2.poly([(26,20),(30,19),(33,20),(33,22),(29,23),(26,22)],S)
f2.line(27,20,30,20,H)
f2.line(28,21,31,21,'c34')
f2.rect(33,20,7,3,K)
f2.line(34,20,40,20,L)
# Metal bracer on straight forearm
f2.poly([(35,19),(40,19),(40,23),(35,23)],M)
f2.line(35,19,39,19,H)
f2.rect(36,20,3,2,S)
f2.line(39,20,39,22,H)
# Bent golden bow limbs, tips swept back toward the archer
outer=[(34,3),(37,5),(39,8),(42,11),(44,15),(45,19),(45,23),(43,28),(40,32),(37,35),(34,38),(33,37),(36,33),(38,30),(40,26),(42,22),(42,18),(41,14),(39,11),(37,8),(34,6)]
f2.poly(outer,'c0')
f2.path('M 34 4 L 37 6 L 38 9 L 41 12 L 43 16 L 44 20 L 43 24 L 41 28 L 39 31 L 36 35 L 34 37','c8',fill=False)
f2.path('M 35 4 L 38 7 L 40 10 L 42 13 L 44 17 L 44 22 L 42 27 L 40 30 L 37 34 L 34 37','c6',fill=False)
# Rose bindings echo the original bow
for x,y in [(41,12),(40,29)]:
 f2.line(x,y,x+1,y+2,'c20')
 f2.set(x+1,y,'c22')
# Taut string to the drawing fingers at the face
f2.line(34,4,25,17,'c11')
f2.line(25,17,34,37,'c11')
# Anchor hand at jaw, visibly curling around the string
f2.poly([(22,16),(25,15),(26,16),(26,19),(23,20),(22,18)],'c1')
f2.line(23,16,25,16,'c13')
f2.line(23,17,25,17,L)
f2.line(24,19,25,19,K)
# Bow grip and wrapped fingers, no arrow
f2.line(43,19,43,23,'c9')
f2.rect(41,19,3,3,K)
f2.line(41,19,43,19,'c13')
f2.line(42,20,44,20,L)
f2.line(42,22,44,22,'c1')
view(f1,scale=8)
view(f2,scale=8)
finish([f1,f2])
