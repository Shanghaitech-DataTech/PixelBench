import random
random.seed(11)
c=new_canvas(128,128,background='#d7e9e9',name='pool_hall')
# ceiling and distant walls
c.poly([(0,0),(128,0),(128,26),(28,27),(0,43)],'#b9d0d4')
c.poly([(0,0),(128,0),(128,7),(25,12),(0,27)],'#cbdcde')
for x in [5,38,75,112]: c.line(x,0,28+(x-28)//2,27,'#a7c0c6')
c.line(0,17,128,9,'#a9c2c7')
# inset fluorescent fixtures
for pts in [[(18,8),(41,7),(35,10),(12,12)],[(64,5),(88,4),(86,7),(61,8)],[(104,2),(123,2),(124,4),(104,5)]]:
 c.poly(pts,'#8faeb8'); c.poly([(x,y-1) for x,y in pts],'#f5ffff')
c.rect(29,27,99,42,'#d4e8e9')
# back wall grid
for y in range(28,69,5): c.line(29,y,127,y,'#b5d1d6')
for x in range(29,129,5): c.line(x,27,x,68,'#b5d1d6')
for y in range(29,67,5):
 for x in range(30,127,5):
  if random.random()<.21:c.rect(x,y,4,4,'#c5dfe3')
# dark corridor beyond
c.rect(72,35,15,29,'#7dabb7'); c.rect(75,37,12,26,'#6695a4')
for y in range(40,64,5):c.line(75,y,86,y,'#77a3b0')
c.line(81,37,81,63,'#77a3b0')
# left wall perspective
c.poly([(0,42),(29,27),(29,69),(0,97)],'#c3dde1')
for y in range(32,72,5):c.line(0,y+15,29,y,'#9fbfc9')
for x in [2,8,15,22,28]:c.line(x,42-x//2,x,96-x,'#a5c6ce')
# floor terrace and pool rim
c.poly([(29,63),(128,63),(128,128),(0,128),(0,93)],'#dceced')
for y in [67,72,79,89,103,122]:c.line(0,y,127,y,'#a7c9d0')
for x in range(-90,240,15):
 c.line(60+(x-60)//5,63,x,127,'#a9cbd1')
# pool dark edge and interior
c.poly([(33,72),(114,72),(127,83),(127,127),(0,127),(0,105)],'#76b3c2')
c.poly([(35,76),(112,76),(127,87),(127,127),(0,127),(0,108)],'#a1d8df')
# underwater grid perspective
for y in [80,86,94,105,119]:c.line(max(0,34-(y-76)),y,127,y,'#8bc9d4')
for x in range(-100,240,16):c.line(38+(x-38)//4,77,x,127,'#8ccbd5')
c.line(33,72,114,72,'#f1faf6'); c.line(0,104,33,72,'#f3faf5')
c.line(114,72,127,83,'#effaf6')
c.line(33,73,114,73,'#bddce1')
# repeated tiled columns
for x,y,w,h in [(92,24,7,44),(119,16,9,59),(29,26,7,43)]:
 c.rect(x,y,w,h,'#e7f2ee'); c.rect(x+w-2,y,2,h,'#a9c9cf')
 c.line(x+2,y,x+2,y+h-1,'#c3dadd')
 for yy in range(y+3,y+h,5):c.line(x,yy,x+w-1,yy,'#b6d1d5')
 c.rect(x-1,y+h-1,w+2,2,'#b1cfd4')
# broad near left column
c.poly([(4,34),(12,30),(12,85),(4,93)],'#eff7f2')
c.poly([(12,30),(17,32),(17,84),(12,85)],'#a4c5ce')
for yy in range(38,91,6):
 c.line(4,yy,11,yy-3,'#b4d0d6')
 if yy<85:c.line(12,yy-3,16,yy-2,'#8eB4c0')
c.line(8,33,8,88,'#d1e3e4')
# water: clustered flat ripples and light reflections
for i in range(180):
 y=random.randrange(79,128); x=random.randrange(128)
 if x<max(0,38-(y-76)):continue
 col=random.choice(['#bce8e9','#c9eeee','#91ced9','#aedef0','#d4f3ef'])
 length=random.choice([2,3,4,6,8])
 c.line(x,y,min(127,x+length),y,col)
 if i%4==0 and y<126:c.line(x+1,y+1,min(127,x+length-2),y+1,'#b0e0e5')
# reflected column light streaks
for x in [33,94,120]:
 for y in range(80,123,4):
  xx=x+random.randrange(-3,4)
  c.line(xx,y,min(127,xx+random.randrange(2,7)),y,'#d5f2ed')
# slide support and ladder at far right
c.rect(109,39,2,32,'#7fa6b3');c.rect(119,37,2,38,'#789daa')
for y in range(43,72,5):c.line(111,y,118,y-1,'#c4dce0')
# winding slide silhouette and underside
c.path('M 104 29 C 123 29 127 39 118 48 C 111 55 94 52 91 59 C 87 65 103 65 99 74 C 96 81 84 85 77 85 L 75 77 C 86 75 90 73 89 71 C 87 68 78 65 80 58 C 82 47 105 48 109 42 C 113 38 108 37 103 37 Z','#8dafba')
c.path('M 103 27 C 120 27 126 36 118 44 C 111 52 93 50 88 57 C 83 64 100 63 97 72 C 95 78 84 81 76 82 L 73 75 C 83 74 89 71 86 69 C 79 65 76 61 80 55 C 85 46 103 46 109 40 C 113 36 107 34 102 34 Z','#f0f7ef')
# slide recessed blue-gray trough
c.path('M 105 30 C 120 31 120 38 113 43 C 104 49 88 47 84 56 C 80 62 91 64 92 69 C 94 74 83 78 76 78 L 75 75 C 84 74 89 71 86 69 C 79 65 76 61 80 55 C 85 46 103 46 109 40 C 113 36 107 34 104 34 Z','#c4dce0')
c.path('M 103 27 C 120 27 126 36 118 44 C 111 52 93 50 88 57 C 83 64 100 63 97 72 C 95 78 84 81 76 82','#ffffff',fill=False)
c.line(74,75,76,81,'#e9f6ef')
for x,y in [(73,83),(80,84),(76,87),(85,82)]:c.line(x,y,x+4,y,'#e2f8f3')
# girl and ring reflections
c.ellipse(58,105,13,3,'#8bc6ce')
c.line(50,111,61,111,'#d0e8bb');c.line(53,113,64,113,'#b5dccd')
c.ellipse(58,101,12,5,'#c49b45')
c.ellipse(58,99,12,5,'#f8d65e')
c.ellipse(58,98,11,4,'#ffe985')
c.ellipse(58,98,6,2,'#8bbfc7')
c.line(49,97,52,96,'#fff4b0');c.line(47,99,48,101,'#ffeaa0')
c.line(64,101,68,99,'#edbb43')
# torso viewed from behind
c.poly([(54,92),(61,92),(63,99),(53,99)],'#c58f78')
c.rect(55,92,6,5,'#e0ad90')
c.poly([(54,97),(61,97),(62,100),(54,100)],'#577c8d')
c.line(54,94,50,98,'#edbc9b');c.line(61,94,65,98,'#e3ad8b')
c.set(50,99,'#f1c7a1');c.set(65,99,'#f1c7a1')
# dark hair, back of head
c.ellipse(58,89,4,5,'#514b48')
c.rect(55,88,7,6,'#5e5149');c.rect(55,86,3,5,'#766050')
c.line(55,87,55,91,'#92745b');c.rect(57,93,5,2,'#514b48')
c.set(62,91,'#d9a386')
# soft wakes
for x,y,l in [(42,103,6),(68,104,6),(49,108,5),(67,108,3),(43,97,3)]:c.line(x,y,x+l,y,'#ddf5ef')
view(c)
finish(c)
