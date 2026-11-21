import math, random
C={'ink':'#161c2e','wood':'#6c513a','brown':'#98694e','ochre':'#97763d','tan':'#bda759','gold':'#dcaa46','light':'#f9e279','cream':'#e1dca3','plaster':'#bbae93','yellow':'#e1d968'}
def make(a,name):
 c=new_canvas(168,180,name=name); t=math.radians(a)
 def p(x,y,z):return (round(84+math.cos(t)*x+math.sin(t)*y),round(133+.707*(math.sin(t)*x-math.cos(t)*y)-.707*z))
 def poly(v,col,edge=None):
  pts=[p(*q) for q in v]; c.poly(pts,C.get(col,col))
  if edge:c.poly(pts,C.get(edge,edge),fill=False)
 def line(v,col,w=1):
  pts=[p(*q) for q in v]
  for q,r in zip(pts,pts[1:]):
   c.line(*q,*r,C.get(col,col))
   if w>1:
    for dx,dy in [(1,0),(0,1)]:c.line(q[0]+dx,q[1]+dy,r[0]+dx,r[1]+dy,C.get(col,col))
 def front(points,col,edge=None):poly([(x,-33,z) for x,z in points],col,edge)
 poly([(-42,-38,0),(42,-38,0),(46,42,0),(-38,44,0)],'#161c2e45')
 # side plaster and posts
 poly([(35,-32,0),(35,32,0),(35,32,76),(35,-32,76)],'ochre','ink')
 poly([(35,-27,8),(35,27,8),(35,27,70),(35,-27,70)],'plaster')
 for y in [-30,28]:
  poly([(36,y-3,0),(36,y+3,0),(36,y+3,76),(36,y-3,76)],'wood','ink')
  line([(36,y-1,4),(36,y,27),(36,y-1,50),(36,y+1,73)],'tan',2)
 for z in [5,70]:poly([(36,-32,z-3),(36,32,z-3),(36,32,z+3),(36,-32,z+3)],'wood','ink')
 # side diagonal timber braces
 line([(36,-27,11),(36,-18,31)],'ochre',2);line([(36,27,12),(36,18,31)],'ochre',2)
 # right window substantial framed square
 poly([(37,-17,25),(37,17,25),(37,17,59),(37,-17,59)],'wood','ink')
 poly([(37,-13,29),(37,13,29),(37,13,55),(37,-13,55)],'ink')
 for yl,yr in [(-11,-2),(2,11)]:
  for zl,zr in [(31,40),(44,53)]:
   poly([(38,yl,zl),(38,yr,zl),(38,yr,zr),(38,yl,zr)],'gold')
   line([(38,yl,zr-1),(38,yr-1,zr-1)],'light')
 line([(39,0,29),(39,0,55)],'tan',2);line([(39,-13,42),(39,13,42)],'tan',2)
 poly([(39,-19,24),(39,19,24),(39,19,28),(39,-19,28)],'tan','wood')
 if a<90:
  front([(-35,0),(35,0),(35,76),(0,133),(-35,76)],'plaster','ink')
  front([(-29,8),(29,8),(29,75),(0,120),(-29,75)],'cream')
  for x in [-31,31]:
   front([(x-4,0),(x+4,0),(x+4,75),(x-4,75)],'wood','ink')
   line([(x,-34,5),(x-1,-34,30),(x+1,-34,53),(x,-34,74)],'tan',2)
  def arch(rad,base,spring,col):
   pts=[(-rad,base),(rad,base),(rad,spring)]
   pts += [(rad*math.cos(i*math.pi/24),spring+rad*math.sin(i*math.pi/24)) for i in range(25)]
   front(pts,col)
  arch(25,0,43,'wood');arch(22,1,43,'tan');arch(18,1,42,'ink');arch(14,2,41,'brown');arch(12,4,40,'gold')
  # carved arched bands and door boards
  line([(22*math.cos(i*math.pi/24),-34,43+22*math.sin(i*math.pi/24)) for i in range(25)],'light',2)
  for x in [-8,0,8]:line([(x,-34,5),(x,-34,36)],'ochre')
  front([(-14,24),(14,24),(14,28),(-14,28)],'wood');line([(-13,-34,28),(13,-34,28)],'light',2)
  c.circle(*p(8,-35,19),1,C['light'])
  front([(-18,0),(18,0),(18,4),(-18,4)],'ink')
 # roof surfaces
 def rz(x):return 141-1.62*abs(x)+.004*x*x
 for side in [-1,1]:
  if side==-1 and a>=90:continue
  xs=[side*i for i in [0,12,24,36,46]]
  for x1,x2 in zip(xs,xs[1:]):
   poly([(x1,-42,rz(x1)),(x2,-42,rz(x2)),(x2,41,rz(x2)),(x1,41,rz(x1))],'ochre','ink')
 # staggered gold roof shingles
 random.seed(4)
 for side in [-1,1]:
  if side==-1 and a>=90:continue
  for row in range(5):
   lo=2+row*8.4; hi=lo+8.0
   for j in range(7):
    y1=-40+j*14-(7 if row%2 else 0);y2=min(39,y1+12)
    y1=max(-40,y1)
    if y2<=y1:continue
    x1=side*lo;x2=side*hi
    poly([(x1,y1,rz(x1)+1),(x2,y1,rz(x2)+1),(x2,y2,rz(x2)+1),(x1,y2,rz(x1)+1)],random.choice(['gold','gold','tan','brown']),'wood')
    line([(x1,y1+1,rz(x1)+2),(x2,y1+1,rz(x2)+2)],'light')
 # sweeping fascia on both roof ends
 for y in [41,-43]:
  if y==-43 and a==90:continue
  for side in [-1,1]:
   pts=[(side*x,y,rz(x)+3) for x in [0,12,24,36,48]]+[(side*x,y,rz(x)-6) for x in [48,36,24,12,0]]
   poly(pts,'wood','ink')
   line([(side*x,y-0.2,rz(x)) for x in [2,12,24,36,47]],'tan',2)
   line([(side*x,y-0.3,rz(x)-3) for x in [3,12,24,36,47]],'ochre')
 # ridge cap with winding grain
 poly([(-3,-46,146),(3,-46,146),(3,44,146),(-3,44,146)],'tan','wood')
 line([(0,-44,147),(1,-29,147),(-1,-15,147),(1,0,147),(0,17,147),(1,41,147)],'ochre',2)
 if a<90:
  poly([(-4,-45,139),(4,-45,139),(5,-45,150),(-3,-45,150)],'tan','wood')
  line([(-1,-46,141),(1,-46,148)],'light')
 return c
f1=make(45,'house_45')
f2=make(90,'house_90')
view(f1)
view(f2)
finish([f1,f2])