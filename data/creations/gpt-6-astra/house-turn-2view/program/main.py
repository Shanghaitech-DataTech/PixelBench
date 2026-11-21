import math, random
INK='#161c2e'; WOOD='#6c513a'; MID='#97763d'; OLIVE='#bda759'; RUST='#98694e'; GOLD='#dcaa46'; LIGHT='#f9e279'; YELLOW='#e1d968'; PLASTER='#e1dca3'; SHADE='#bbae93'; CREAM='#e7dc8f'

def make(angle,name):
 c=new_canvas(172,180,name=name)
 a=math.radians(angle); co=math.cos(a); si=math.sin(a)
 def p(x,y,z): return (round(86+x*co+y*si),round(128+(x*si-y*co-z)*0.70710678))
 def line(points,col,width=1):
  pts=[p(*v) for v in points]
  for (x,y),(u,v) in zip(pts,pts[1:]):
   if width==1: c.line(x,y,u,v,col)
   else:
    for dx in range(-(width//2),width-width//2):
     for dy in range(-(width//2),width-width//2): c.line(x+dx,y+dy,u+dx,v+dy,col)
 def poly(points,col,edge=None,width=1):
  c.poly([p(*v) for v in points],col)
  if edge: line(points+[points[0]],edge,width)
 def front(coords,col,edge=None,width=1,y=-43): poly([(x,y,z) for x,z in coords],col,edge,width)
 def side(coords,col,edge=None,width=1,x=36): poly([(x,y,z) for y,z in coords],col,edge,width)
 # two wall faces, elevated perspective
 side([(-43,0),(43,0),(43,73),(-43,73)],OLIVE,INK,3)
 side([(-39,6),(39,6),(39,68),(-39,68)],SHADE)
 side([(-32,12),(32,12),(32,65),(-32,65)],PLASTER)
 # aged plaster facets
 side([(-30,12),(-23,17),(-26,35),(-30,48),(-32,62),(-36,56),(-34,27)],CREAM)
 side([(25,10),(34,10),(34,59),(28,52),(31,34)],OLIVE)
 # timber posts along right wall
 for y in [-40,39]:
  side([(y-4,0),(y+4,0),(y+4,73),(y-4,73)],MID,WOOD,1)
  line([(37,y-1,6),(37,y+1,24),(37,y-2,39),(37,y+1,57),(37,y,68)],OLIVE,2)
  line([(37,y+3,8),(37,y+2,31),(37,y+3,49)],WOOD)
 side([(-43,0),(43,0),(43,7),(-43,7)],WOOD,INK,2)
 line([(37,-39,7),(37,39,7)],MID,2)
 # right-hand window: heavy wood frame, warm glass, cross mullions
 side([(-20,21),(21,21),(21,55),(-20,55)],WOOD,INK,3,x=37)
 side([(-17,24),(18,24),(18,52),(-17,52)],GOLD,OLIVE,2,x=38)
 side([(-14,27),(15,27),(15,49),(-14,49)],INK,x=39)
 side([(-12,29),(-2,29),(-2,47),(-12,47)],GOLD,x=39)
 side([(2,29),(13,29),(13,47),(2,47)],GOLD,x=39)
 side([(-11,41),(-3,46),(-3,48),(-11,48)],LIGHT,x=39)
 side([(3,32),(12,39),(12,44),(3,37)],LIGHT,x=39)
 line([(40,0,27),(40,0,49)],MID,3)
 line([(40,-14,38),(40,15,38)],MID,3)
 line([(40,-14,40),(40,15,40)],LIGHT)
 side([(-24,19),(24,19),(24,24),(-24,24)],MID,INK,2,x=40)
 line([(41,-23,24),(41,23,24)],LIGHT,2)
 if angle<89:
  front([(-36,0),(36,0),(36,73),(25,87),(10,107),(0,126),(-10,107),(-25,87),(-36,73)],WOOD,INK,3)
  front([(-29,5),(29,5),(29,69),(22,82),(0,108),(-22,82),(-29,69)],SHADE)
  front([(-26,9),(26,9),(26,68),(18,80),(0,102),(-21,78),(-27,65)],PLASTER)
  front([(-26,47),(-21,48),(-23,68),(-14,81),(0,94),(13,81),(20,80),(0,103),(-25,78)],CREAM)
  front([(21,7),(28,7),(28,66),(22,57)],OLIVE)
  for x in [-32,32]:
   front([(x-4,0),(x+4,0),(x+4,72),(x-4,72)],MID,WOOD)
   line([(x,-44,4),(x-2,-44,22),(x+1,-44,39),(x-2,-44,53),(x,-44,68)],OLIVE,2)
   line([(x+3,-44,9),(x+1,-44,30),(x+3,-44,51)],WOOD)
  # arched doorway, concentric carved surround
  arch=[(-24,0),(24,0),(24,40),(20,54),(12,65),(0,69),(-12,65),(-20,54),(-24,40)]
  front(arch,OLIVE,INK,3,y=-44)
  front([(-19,1),(19,1),(19,39),(16,51),(9,59),(0,62),(-9,59),(-16,51),(-19,39)],MID,WOOD,2,y=-45)
  front([(-15,2),(15,2),(15,39),(11,49),(5,55),(-5,55),(-11,49),(-15,39)],RUST,INK,3,y=-46)
  front([(-11,5),(12,5),(12,39),(8,47),(3,51),(-4,51),(-11,42)],GOLD,y=-47)
  front([(-12,4),(-5,4),(-6,29),(-11,37)],MID,y=-47)
  for x in [-7,4,10]: line([(x,-48,7),(x,-48,29)],RUST)
  front([(-14,27),(14,27),(14,32),(-14,32)],MID,INK,1,y=-48)
  line([(-13,-49,32),(13,-49,32)],LIGHT,2)
  front([(5,17),(9,17),(9,21),(5,21)],LIGHT,WOOD,1,y=-49)
  line([(-23,-46,39),(-19,-46,54),(-10,-46,64),(0,-46,67),(11,-46,63)],YELLOW,2)
  front([(-25,0),(25,0),(25,4),(-25,4)],WOOD,INK,2,y=-49)
 # Swooping shingled roof, near/right slope
 profile=[(0,132),(6,113),(15,99),(28,85),(45,74)]
 def rz(x):
  for (x0,z0),(x1,z1) in zip(profile,profile[1:]):
   if x<=x1:return z0+(z1-z0)*(x-x0)/(x1-x0)
  return 74
 poly([(x,y,z) for x,y,z in [(0,-50,132),(0,50,132),(6,50,113),(15,50,99),(28,50,85),(45,50,74),(45,-50,74),(28,-50,85),(15,-50,99),(6,-50,113)]],RUST,INK,3)
 rng=random.Random(40)
 courses=[0,6,13,21,30,38,45]
 for row,(xa,xb) in enumerate(zip(courses,courses[1:])):
  cuts=[-50]+[v for v in range(-50+(9 if row%2 else 17),50,17)]+[50]
  for j,(ya,yb) in enumerate(zip(cuts,cuts[1:])):
   col=[GOLD,GOLD,GOLD,OLIVE,RUST][rng.randrange(5)]
   poly([(xa,ya,rz(xa)),(xa,yb,rz(xa)),(xb,yb,rz(xb)),(xb,ya,rz(xb))],col)
   line([(xa,ya,rz(xa)),(xb,ya,rz(xb))],RUST,2)
   line([(xb,ya,rz(xb)),(xb,yb,rz(xb))],MID,2)
   if yb-ya>5:
    line([(xa+1,ya+3,rz(xa+1)+.5),(xb-1,ya+3,rz(xb-1)+.5)],LIGHT,2)
    line([(xb-1,ya+4,rz(xb-1)+.5),(xb-1,min(ya+10,yb-1),rz(xb-1)+.5)],LIGHT)
 # long side eave beam
 poly([(45,-52,75),(45,52,75),(45,52,68),(45,-52,68)],MID,INK,3)
 line([(46,-50,74),(46,50,74)],OLIVE,2)
 line([(46,-50,69),(46,50,69)],WOOD,2)
 # raised ridge cap along the roof top
 poly([(-3,-53,132),(-3,52,132),(1,53,136),(5,52,130),(5,-53,130)],MID,INK,2)
 line([(0,-52,135),(0,51,135)],OLIVE,3)
 line([(2,-50,133),(2,49,133)],LIGHT)
 # front verge: carved curved rafters echo the input's broad scrollwork
 if angle<89:
  for s in [-1,1]:
   coords=[(s*0,134),(s*7,113),(s*16,99),(s*29,86),(s*47,76),(s*47,68),(s*29,79),(s*14,94),(s*5,108),(s*0,126)]
   front(coords,MID,INK,3,y=-53)
   line([(s*3,-54,125),(s*10,-54,108),(s*23,-54,92),(s*43,-54,78)],OLIVE,3)
   line([(s*12,-55,104),(s*26,-55,89),(s*44,-55,77)],LIGHT)
   line([(s*17,-55,93),(s*30,-55,81),(s*45,-55,73)],WOOD,2)
  # central tall finial and drooping carved pendant
  front([(-4,141),(4,141),(5,129),(3,118),(5,107),(3,96),(4,91),(-4,91),(-5,97),(-3,108),(-5,119),(-4,131)],OLIVE,INK,2,y=-56)
  line([(-1,-57,138),(1,-57,130),(-2,-57,119),(1,-57,108),(-1,-57,97)],MID,2)
  line([(-3,-57,137),(-3,-57,129)],LIGHT)
  front([(-6,96),(6,96),(6,92),(3,91),(3,88),(-3,88),(-3,91),(-6,92)],YELLOW,INK,1,y=-57)
 else:
  # end-on verge bands remain narrow; wall itself stays entirely side-on
  for yy in [-51,51]:
   line([(x,yy,z) for x,z in profile],WOOD,3)
   line([(x,yy,z+2) for x,z in profile],OLIVE,2)
  # The carved front tip is edge-on at this yaw.
  line([(0,-54,140),(0,-54,128),(2,-54,117),(0,-54,105),(0,-54,92)],INK,5)
  line([(0,-54,139),(0,-54,129),(2,-54,117),(0,-54,105),(0,-54,93)],OLIVE,3)
  line([(0,-55,138),(0,-55,130)],LIGHT)
 view(c)
 return c
f1=make(45,'house_45')
f2=make(90,'house_90')
finish([f1,f2])
