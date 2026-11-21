import math, random
ink='#161c2e'; wood='#6c513a'; brown='#97763d'; straw='#bda759'; rust='#98694e'; gold='#dcaa46'; light='#f9e279'; pale='#e1dca3'; plaster='#bbae93'
frames=[]
for angle in (45,90):
 c=new_canvas(176,176,name='turn_'+str(angle))
 a=math.radians(angle); co=math.cos(a); si=math.sin(a)
 def p(v):
  x,y,z=v
  return (round(88+1.16*(x*co+y*si)),round(127-1.16*.7071*(y*co-x*si+z)))
 def line(v,w,col,width=1):
  x,y=p(v); X,Y=p(w)
  for dx in range(-(width//2),width-width//2):
   for dy in range(-(width//2),width-width//2): c.line(x+dx,y+dy,X+dx,Y+dy,col)
 def poly(v,col,edge=None,width=1):
  c.poly([p(t) for t in v],col)
  if edge:
   for j in range(len(v)):line(v[j],v[(j+1)%len(v)],edge,width)
 def front(points,col,edge=None,w=1):poly([(x,-30,z) for x,z in points],col,edge,w)
 def side(points,col,edge=None,w=1):poly([(30,y,z) for y,z in points],col,edge,w)
 # Ground silhouette, compact and transparent outside
 poly([(-32,-33,0),(34,-33,0),(34,33,0),(-32,33,0)],ink)
 # Right plaster wall
 side([(-30,0),(30,0),(30,56),(-30,56)],straw,ink,4)
 side([(-25,7),(25,7),(25,51),(-25,51)],plaster)
 side([(-23,10),(22,10),(22,48),(-23,48)],pale)
 # rough plaster shadows
 side([(-24,9),(-19,15),(-21,26),(-18,33),(-23,45),(-25,47)],straw)
 side([(19,7),(24,7),(24,47),(20,43),(22,30),(18,23)],straw)
 # structural side timbers
 for yy in (-28,28):
  line((31,yy,2),(31,yy,55),wood,6)
  line((32,yy-1,4),(32,yy-1,51),brown,3)
  line((33,yy-2,9),(33,yy-2,47),straw,1)
 line((31,-28,5),(31,28,5),wood,5)
 line((32,-27,7),(32,27,7),brown,2)
 # Side window, deep inset with golden timber surround
 side([(-15,18),(15,18),(15,43),(-15,43)],wood,ink,3)
 side([(-12,21),(12,21),(12,40),(-12,40)],gold)
 side([(-9,23),(9,23),(9,38),(-9,38)],ink)
 side([(-8,25),(-2,25),(-2,36),(-8,36)],brown)
 side([(2,25),(8,25),(8,36),(2,36)],'#98694e')
 line((32,0,22),(32,0,39),straw,3)
 line((32,-11,30),(32,11,30),straw,2)
 line((33,-16,18),(33,16,18),wood,4)
 line((34,-16,20),(34,16,20),light,2)
 if angle==45:
  front([(-30,0),(30,0),(30,56),(0,91),(-30,56)],plaster,ink,4)
  front([(-25,7),(25,7),(25,54),(0,83),(-25,54)],pale)
  front([(-25,11),(-20,16),(-22,29),(-19,40),(-24,50)],straw)
  front([(21,9),(25,10),(25,49),(19,44),(22,34),(19,25)],straw)
  for xx in (-28,28):
   line((xx,-31,1),(xx,-31,55),wood,6)
   line((xx,-32,5),(xx,-32,52),brown,3)
   line((xx-1,-33,12),(xx-1,-33,45),straw,1)
  # rounded arch surround with layered timber bands
  arch=[(-17,0),(17,0),(17,29),(15,37),(10,44),(4,47),(-4,47),(-10,44),(-15,37),(-17,29)]
  front(arch,wood,ink,3)
  front([(-14,1),(14,1),(14,29),(12,36),(8,41),(2,44),(-3,44),(-10,39),(-14,30)],straw)
  front([(-11,0),(11,0),(11,28),(9,34),(4,39),(-3,39),(-9,33),(-11,27)],ink)
  front([(-8,3),(8,3),(8,27),(5,33),(0,36),(-5,32),(-8,26)],rust)
  front([(-7,5),(7,5),(7,26),(3,31),(-3,31),(-7,25)],gold)
  for xx in (-4,3):line((xx,-31,5),(xx,-31,29),brown,1)
  line((-9,-32,18),(9,-32,18),wood,3)
  line((-9,-33,20),(9,-33,20),light,2)
  c.circle(*p((6,-34,12)),1,ink)
 # roof surface: right slope, eaves overhang
 def roof(x,y):return (x,y,96-1.17*abs(x))
 # left roof surface visible from elevated camera at 45
 if angle==45:
  poly([roof(-36,-36),roof(-36,36),roof(0,36),roof(0,-36)],brown,ink,4)
 poly([roof(0,-36),roof(0,36),roof(36,36),roof(36,-36)],rust,ink,4)
 # irregular thick golden thatch courses
 rng=random.Random(8)
 for sign in ((-1,1) if angle==45 else (1,)):
  for row in range(5):
   x0=row*7+1; x1=min(35,x0+7)
   for k in range(9):
    yy=-35+k*8+(3 if row%2 else 0)
    y1=min(35,yy+7)
    if yy>=35:continue
    col=rng.choice([gold,gold,gold,straw,rust])
    poly([roof(sign*x0,yy),roof(sign*x0,y1),roof(sign*x1,y1-1),roof(sign*(x1-1),yy)],col)
    if rng.random()<.6:line(roof(sign*(x0+1),yy+1),roof(sign*(x1-2),yy+1),light,1)
 # eave beams
 for sign in ((-1,1) if angle==45 else (1,)):
  line(roof(sign*36,-37),roof(sign*36,37),ink,7)
  line(roof(sign*36,-37),roof(sign*36,37),wood,5)
  line(roof(sign*35,-37),roof(sign*35,37),straw,2)
 # back gable verge
 line(roof(0,36),roof(36,36),wood,5)
 line(roof(0,36),roof(36,36),straw,2)
 # prominent ornamental front gable fascia
 if angle==45:
  for sign in (-1,1):
   line(roof(0,-37),roof(sign*37,-37),ink,8)
   line(roof(0,-38),roof(sign*37,-38),wood,6)
   line(roof(0,-39),roof(sign*37,-39),straw,3)
   line(roof(sign*4,-40),roof(sign*35,-40),brown,1)
 # ridge cap worn wooden spine
 line(roof(0,-39),roof(0,39),ink,8)
 line(roof(0,-39),roof(0,39),brown,6)
 line(roof(-1,-38),roof(-1,38),straw,3)
 for y in range(-32,36,12):
  line(roof(1,y),roof(-1,y+6),wood,2)
 if angle==45:
  poly([(-4,-40,96),(4,-40,96),(4,-40,88),(-4,-40,88)],straw,wood,1)
  line((-4,-41,89),(4,-41,89),light,2)
 frames.append(c)
view(frames[0]);view(frames[1])
finish(frames)
