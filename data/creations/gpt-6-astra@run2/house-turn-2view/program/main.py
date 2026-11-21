import math, random
import numpy as np
# Original palette, retained throughout the turn.
INK='#161c2e'; WOOD='#6c513a'; SHADE='#97763d'; MID='#bda759'; BROWN='#98694e'; GOLD='#dcaa46'; LIGHT='#f9e279'; STRAW='#e1d968'; PLASTER='#e1dca3'; DULL='#bbae93'
# Paint the architectural surfaces in their own editable texture canvases.
front=new_canvas(89,112,PLASTER,name='front-paint')
front.rect(0,53,89,59,MID)
front.poly([(5,112),(5,55),(14,40),(31,22),(44,9),(58,25),(75,43),(84,59),(84,112)],PLASTER)
front.poly([(6,103),(6,60),(15,48),(12,68),(17,83),(15,110)],DULL)
front.poly([(70,47),(83,61),(83,111),(72,111),(76,89),(72,74)],MID)
# Foundation and great corner timbers.
front.rect(0,105,89,7,INK)
for x in [1,77]:
 front.rect(x,55,11,51,WOOD)
 front.poly([(x+2,56),(x+7,57),(x+5,70),(x+9,87),(x+7,105),(x+2,104),(x+4,86),(x+1,71)],SHADE)
 front.line(x+4,59,x+3,71,MID); front.line(x+3,74,x+7,91,MID)
 front.line(x+7,91,x+5,104,MID)
# Gable plaster chips.
for pts,col in [([(13,56),(18,45),(30,32),(25,44),(18,50)],LIGHT), ([(34,29),(44,20),(54,30),(49,29),(44,25)],DULL), ([(60,37),(72,48),(75,58),(69,53)],STRAW)]: front.poly(pts,col)
front.line(23,47,33,47,STRAW);front.line(57,51,66,51,LIGHT)
# Deep arched entry, surround, and inset golden door.
front.path('M 22 108 L 22 76 Q 21 54 44 48 Q 68 54 68 76 L 68 108 Z',INK)
front.path('M 24 106 L 24 76 Q 24 57 44 52 Q 65 57 65 77 L 65 106 L 59 106 L 59 78 Q 59 63 44 60 Q 30 65 30 79 L 30 106 Z',WOOD)
front.path('M 25 104 L 25 76 Q 25 59 44 54 Q 63 59 63 77 L 63 104 L 60 104 L 60 77 Q 59 63 44 59 Q 30 63 29 77 L 29 104 Z',MID)
front.path('M 25 84 L 25 76 Q 25 59 44 54 Q 56 56 62 68',LIGHT,fill=False)
front.path('M 31 105 L 31 80 Q 31 66 44 63 Q 58 67 58 80 L 58 105 Z',BROWN)
front.path('M 34 103 L 34 80 Q 35 71 44 67 Q 53 71 55 80 L 55 103 Z',GOLD)
front.poly([(36,80),(37,76),(42,70),(42,86),(36,86)],MID)
front.rect(31,85,28,4,INK);front.rect(32,88,26,3,LIGHT);front.rect(33,91,24,2,SHADE)
front.line(43,71,43,83,SHADE);front.line(47,94,47,103,SHADE)
front.rect(35,96,2,5,SHADE);front.rect(53,95,2,4,LIGHT)
front.rect(53,83,3,3,INK);front.set(53,83,LIGHT)
front.rect(29,106,31,4,WOOD)
side=new_canvas(93,61,MID,name='right-wall-paint')
side.rect(0,0,93,7,WOOD); side.rect(0,7,93,2,GOLD)
side.rect(0,55,93,6,INK);side.rect(0,53,93,3,WOOD)
# Uneven ochre infill and wood grain.
side.poly([(8,10),(81,10),(83,51),(73,51),(75,30),(66,15),(22,14),(14,27),(12,51),(8,51)],PLASTER)
side.poly([(15,15),(33,13),(26,20),(18,22),(16,34),(12,40)],STRAW)
side.poly([(76,18),(84,10),(84,51),(76,51),(78,40),(73,31)],DULL)
for x in [0,84]:
 side.rect(x,6,9,49,WOOD)
 side.poly([(x+2,8),(x+6,8),(x+4,22),(x+7,37),(x+5,53),(x+2,53),(x+3,37),(x+1,23)],SHADE)
 side.line(x+3,10,x+2,24,MID);side.line(x+3,26,x+5,38,GOLD);side.line(x+5,40,x+3,52,MID)
# Single substantial four-pane window.
side.rect(29,16,37,32,WOOD);side.rect(31,18,33,27,INK)
side.rect(34,20,27,22,SHADE)
for x in [35,49]:
 for y in [21,33]:
  side.rect(x,y,10,8,INK)
  side.poly([(x,y),(x+9,y),(x+9,y+2),(x+2,y+8),(x,y+8)],DULL)
  side.line(x+1,y+1,x+6,y+1,PLASTER)
side.rect(46,19,3,25,GOLD);side.rect(33,30,29,3,GOLD)
side.rect(29,15,37,3,MID); side.rect(30,15,35,1,LIGHT)
side.rect(27,44,41,4,WOOD);side.rect(28,43,39,2,LIGHT);side.rect(30,48,35,2,SHADE)
# Hand-laid staggered roof shingles, with chunky chips and highlights.
roofs=[]
for sign in [-1,1]:
 r=new_canvas(57,103,BROWN,name='roof-paint-'+str(sign))
 rng=random.Random(16 if sign==1 else 22)
 for row in range(7):
  v=row*16
  for j in range(-1,5):
   u=j*16+(8 if row%2 else 0)
   # clip the painted tiles explicitly at texture borders
   pts=[(u+1,v+1),(u+14,v+1),(u+14,v+12),(u+11,v+15),(u,v+15)]
   pts=[(max(0,min(56,x)),max(0,min(102,y))) for x,y in pts]
   r.poly(pts,GOLD if rng.random()>.28 else SHADE)
   x=max(0,min(54,u+2)); y=min(100,v+3)
   r.rect(x,y,min(3,57-x),min(10,103-y),LIGHT if rng.random()>.35 else MID)
   if 0<=u+13<57:r.line(u+13,min(v+3,102),u+13,min(v+12,102),BROWN)
   if 0<=u+7<57:r.line(u+7,min(v+14,102),min(u+12,56),min(v+14,102),WOOD)
 roofs.append(r)
# Orthographic 3D rasteriser: camera elevation is 45 degrees in BOTH frames.
# Texture coordinates remain attached to the building as it turns.
def render(angle,name):
 c=new_canvas(176,180,name=name)
 depth=np.full((180,176),-1e9); pixels=np.zeros((180,176),dtype=int)
 a=math.radians(angle); ca=math.cos(a);sa=math.sin(a); k=math.sqrt(.5)
 def project(p):
  x,y,z=p; d=x*sa+y*ca
  return (88+x*ca-y*sa,121+d*k-z*k,d*k+z*k)
 def tri(points,uvs,tex=None,color=None):
  ps=[project(p) for p in points]; (x0,y0,d0),(x1,y1,d1),(x2,y2,d2)=ps
  den=(y1-y2)*(x0-x2)+(x2-x1)*(y0-y2)
  if abs(den)<.001:return
  col=c.color(color) if color else None
  for y in range(max(0,int(min(y0,y1,y2))),min(179,math.ceil(max(y0,y1,y2)))+1):
   for x in range(max(0,int(min(x0,x1,x2))),min(175,math.ceil(max(x0,x1,x2)))+1):
    aa=((y1-y2)*(x-x2)+(x2-x1)*(y-y2))/den
    bb=((y2-y0)*(x-x2)+(x0-x2)*(y-y2))/den;cc=1-aa-bb
    if min(aa,bb,cc)<-.001:continue
    dd=aa*d0+bb*d1+cc*d2
    if dd<depth[y,x]-.01:continue
    if tex:
     u=int(round(aa*uvs[0][0]+bb*uvs[1][0]+cc*uvs[2][0]));v=int(round(aa*uvs[0][1]+bb*uvs[1][1]+cc*uvs[2][1]))
     tw,th=tex_sizes[tex.name]; col=tex.get(max(0,min(tw-1,u)),max(0,min(th-1,v)))
    pixels[y,x]=col;depth[y,x]=dd
 def quad(p,uv=None,tex=None,color=None):
  if uv is None:uv=[(0,0)]*4
  tri([p[i] for i in [0,1,2]],[uv[i] for i in [0,1,2]],tex,color)
  tri([p[i] for i in [0,2,3]],[uv[i] for i in [0,2,3]],tex,color)
 # Right wall; x is constant, length goes from the back to the front.
 quad([(44,-46,60),(44,46,60),(44,46,0),(44,-46,0)],[(0,0),(92,0),(92,60),(0,60)],side)
 # Front gabled wall.
 if angle<89:
  quad([(-44,46,60),(44,46,60),(44,46,0),(-44,46,0)],[(0,51),(88,51),(88,111),(0,111)],front)
  tri([(-44,46,60),(0,46,108),(44,46,60)],[(0,51),(44,3),(88,51)],front)
 profile=[(0,114),(7,101),(17,88),(30,77),(43,69),(53,65)]
 for si,sgn in enumerate([-1,1]):
  for i in range(len(profile)-1):
   x,z=profile[i];xx,zz=profile[i+1]
   quad([(sgn*x,-51,z),(sgn*xx,-51,zz),(sgn*xx,51,zz),(sgn*x,51,z)],[(x,0),(xx,0),(xx,102),(x,102)],roofs[si])
  # Deep carved boards at each gable: broad dark edge, ochre inset strips.
  for yy in [-52,52]:
   for i in range(len(profile)-1):
    x,z=profile[i];xx,zz=profile[i+1]
    quad([(sgn*x,yy,z+1),(sgn*xx,yy,zz+1),(sgn*xx,yy,zz-8),(sgn*x,yy,z-8)],color=INK)
    quad([(sgn*x,yy+(.12 if yy>0 else -.12),z),(sgn*xx,yy+(.12 if yy>0 else -.12),zz),(sgn*xx,yy+(.12 if yy>0 else -.12),zz-5),(sgn*x,yy+(.12 if yy>0 else -.12),z-5)],color=SHADE)
    quad([(sgn*x,yy+.2,z-1),(sgn*xx,yy+.2,zz-1),(sgn*xx,yy+.2,zz-2),(sgn*x,yy+.2,z-2)],color=MID)
  # Eave fascia, including a narrow golden top lip.
  quad([(sgn*53,-52,65),(sgn*53,52,65),(sgn*53,52,57),(sgn*53,-52,57)],color=INK)
  quad([(sgn*53.2,-52,64),(sgn*53.2,52,64),(sgn*53.2,52,60),(sgn*53.2,-52,60)],color=SHADE)
  quad([(sgn*53.3,-52,64),(sgn*53.3,52,64),(sgn*53.3,52,63),(sgn*53.3,-52,63)],color=MID)
 # Raised curved wooden ridge cap with upswept tips.
 sections=[(-57,124),(-52,122),(-44,116),(-28,115),(12,115),(38,116),(50,120),(56,123)]
 for i in range(len(sections)-1):
  y,z=sections[i];yy,zz=sections[i+1]
  quad([(-4,y,z),(4,y,z),(4,yy,zz),(-4,yy,zz)],color=MID)
  quad([(4,y,z),(4,yy,zz),(4,yy,zz-9),(4,y,z-9)],color=WOOD)
  quad([(4.1,y,z-1),(4.1,yy,zz-1),(4.1,yy,zz-5),(4.1,y,z-5)],color=SHADE)
  quad([(-4,y,z),(-4,yy,zz),(-4,yy,zz-9),(-4,y,z-9)],color=SHADE)
  quad([(-2,y,z+.1),(0,y,z+.1),(1,yy,zz+.1),(-1,yy,zz+.1)],color=LIGHT)
 y,z=sections[-1]
 quad([(-4,y,z),(4,y,z),(4,y,z-10),(-4,y,z-10)],color=MID)
 quad([(-3,y+.1,z-7),(4,y+.1,z-7),(4,y+.1,z-10),(-3,y+.1,z-10)],color=LIGHT)
 # A two-pixel ink silhouette matches the heavy outline of the input.
 mask=pixels!=0
 ink=c.color(INK)
 for y in range(1,179):
  for x in range(1,175):
   if not mask[y,x] and mask[max(0,y-1):y+2,max(0,x-1):x+2].any():c.set(x,y,ink)
 for y,x in zip(*np.where(mask)):c.set(int(x),int(y),int(pixels[y,x]))
 return c
tex_sizes={front.name:(89,112),side.name:(93,61),roofs[0].name:(57,103),roofs[1].name:(57,103)}
f1=render(45,'house-45-degrees')
f2=render(90,'house-90-degrees')
view(f1)
view(f2)
finish([f1,f2])
