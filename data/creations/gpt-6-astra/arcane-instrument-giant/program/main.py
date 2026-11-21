import math, random
random.seed(19)
W=H=256
result=new_canvas(W,H,name='The Aetheric Grand Orrery')
c=result
ink='#090e18'
bg=['#080d17','#0a111b','#0d1721','#101e28','#132630','#18303a','#1d3c44','#24474c']
brass=['#211c24','#3b2b2b','#574033','#795537','#9c713e','#c0914d','#dfb665','#f4d98a','#fff0b3']
steel=['#15232c','#253741','#3a5058','#526a70','#789291']
teal=['#143d48','#1a5a64','#26828b','#43a9ac','#75d2c9','#b3f3df','#edffe4']
# Quiet pool of illumination behind the machine, in discrete pixel tones.
for y in range(256):
 for x in range(256):
  d=math.sqrt(((x-128)/112)**2+((y-108)/124)**2)
  k=max(0,min(7,int((1.2-d)*6)))
  c.set(x,y,bg[k])
# The vaulted hall: recessed arches, masonry and slender fluted columns.
for side in [0,1]:
 x=8 if side==0 else 219
 c.rect(x,0,29,205,'#0b141e')
 c.rect(x+3,0,3,204,'#1b2932')
 c.rect(x+7,0,2,204,'#111e28')
 c.rect(x+19,0,4,204,'#172630')
 c.rect(x+24,0,2,204,'#22343b')
 for yy in [38,79,120,161,200]:
  c.line(x+3,yy,x+25,yy,'#080f19')
  c.line(x+4,yy+1,x+24,yy+1,'#24333a')
 c.rect(x-2,199,33,5,'#1a2932')
 c.rect(x-4,204,37,5,'#0c1721')
 c.rect(x-4,204,37,1,'#2a3b42')
# Arch behind the silhouette.
for rad in [105,108,114]:
 pts=[]
 for i in range(181):
  t=math.pi+i*math.pi/180
  pts.append((round(128+rad*math.cos(t)),round(111+rad*math.sin(t))))
 for a,b in zip(pts,pts[1:]): c.line(*a,*b,'#26363c' if rad==108 else '#101c26')
for x in [43,212]: c.line(x,61,x,198,'#1c2e37')
for y in [31,58,88,121,155,186]:
 c.line(38,y,50,y,'#1c2b34'); c.line(205,y,217,y,'#1c2b34')
# Perspective floor.
c.poly([(0,212),(81,201),(174,201),(255,212),(255,256),(0,256)],'#111e29')
for yy in [218,232,253]: c.line(0,yy,255,yy,'#293b43'); c.line(0,yy+1,255,yy+1,'#0b1520')
for xx in [-120,-30,50,128,205,285,375]:
 x1=max(0,min(255,xx))
 c.line(128+int((xx-128)*.22),202,x1,255,'#2b3d43')
c.ellipse(128,232,71,15,'#090f19')
c.ellipse(128,229,55,9,'#0b1720')
# Stone pedestal, beveled and worn.
c.poly([(77,231),(179,231),(190,244),(190,251),(65,251),(65,244)],ink)
c.poly([(78,231),(178,231),(187,243),(68,243)],'#435158')
c.rect(68,244,120,5,'#24323d'); c.line(69,244,187,244,'#66716d')
c.poly([(88,211),(167,211),(176,235),(79,235)],'#263640')
c.poly([(88,211),(102,214),(96,234),(80,234)],'#46565b')
c.poly([(155,214),(167,211),(175,234),(160,234)],'#182832')
c.rect(103,216,51,17,'#162933'); c.rect(105,217,47,1,'#59706b')
c.poly([(81,204),(174,204),(184,212),(173,220),(82,220),(71,212)],ink)
c.poly([(82,203),(173,203),(181,211),(172,216),(83,216),(74,211)],'#697974')
c.poly([(83,205),(171,205),(176,210),(169,213),(86,213),(79,210)],'#354d52')
c.line(76,212,83,217,'#9ca58d'); c.line(83,217,171,217,'#7d8e7e')
c.line(83,219,172,219,'#182c36')
for x in [88,95,160,169]: c.line(x,224,x-1,231,'#56666a')
c.line(91,241,96,244,'#1a2933'); c.line(96,244,94,249,'#111e29')
c.line(161,233,158,237,'#0d1d28'); c.line(158,237,165,239,'#0d1d28')
# Inlaid alchemical sigils on the plinth.
c.circle(128,225,6,brass[3],False); c.poly([(128,220),(123,229),(133,229)],teal[3],False)
for x in [111,144]: c.line(x,222,x,228,brass[4]); c.set(x+2,225,teal[4])
# Levitation pool, layered hard-edged glow.
for rx,ry,col in [(36,7,'#183942'),(29,5,'#205661'),(22,3,'#2e7880')]: c.ellipse(128,208,rx,ry,col)
c.ellipse(128,208,30,6,teal[3],False); c.ellipse(128,208,19,3,teal[4],False)
for x,y in [(109,199),(145,200),(119,194),(138,191),(128,201)]:
 c.line(x,y,x,y+3,teal[3]); c.set(x,y,teal[5])
CX,CY=128,106
# Small helpers for heavy black outlines and faceted metal.
def seg(a,b,col,width=1):
 if width==1: c.line(round(a[0]),round(a[1]),round(b[0]),round(b[1]),col); return
 dx=b[0]-a[0];dy=b[1]-a[1]; ll=math.hypot(dx,dy) or 1
 nx=-dy/ll*width/2;ny=dx/ll*width/2
 c.poly([(round(a[0]+nx),round(a[1]+ny)),(round(b[0]+nx),round(b[1]+ny)),(round(b[0]-nx),round(b[1]-ny)),(round(a[0]-nx),round(a[1]-ny))],col)
def gear(x,y,r,n=14):
 pts=[]
 for i in range(n*4):
  a=i*math.tau/(n*4); rr=r if i%4 in [1,2] else r-3
  pts.append((round(x+rr*math.cos(a)),round(y+rr*math.sin(a))))
 c.poly(pts,ink); c.poly([(x+(px-x)*.88,y+(py-y)*.88) for px,py in pts],brass[4]); c.poly(pts,ink,False)
 c.circle(x,y,r-5,brass[1]); c.circle(x,y,r-6,brass[5],False)
 for i in range(6):
  a=i*math.tau/6
  p=(x+(r-6)*math.cos(a),y+(r-6)*math.sin(a))
  seg((x,y),p,brass[3],3);seg((x-1,y-1),(p[0]-1,p[1]-1),brass[6])
 c.circle(x,y,4,ink);c.circle(x,y,3,brass[6]);c.circle(x,y,1,brass[2])
def dial(x,y,r):
 c.circle(x,y,r+2,ink); c.circle(x,y,r,brass[5]);c.circle(x,y,r-2,brass[1]);c.circle(x,y,r-3,'#172f37')
 for i in range(12):
  a=i*math.tau/12
  seg((x+(r-3)*math.cos(a),y+(r-3)*math.sin(a)),(x+(r-5)*math.cos(a),y+(r-5)*math.sin(a)),brass[6])
 seg((x-3,y+3),(x+4,y-6),teal[5]);c.circle(x,y,1,brass[7])
# Rear mechanical cage and transmission assembly.
for a in [0.25,1.05,1.9,2.8,3.7,4.8,5.5]:
 p=(CX+74*math.cos(a),CY+74*math.sin(a))
 q=(CX+24*math.cos(a+.12),CY+24*math.sin(a+.12))
 seg(p,q,ink,7);seg(p,q,brass[2],4);seg((p[0]-1,p[1]-1),(q[0]-1,q[1]-1),brass[5])
for x,y,r,n in [(71,153,22,17),(93,171,17,14),(160,163,23,18),(184,155,15,12),(181,83,17,14),(72,71,16,13),(153,44,14,12)]: gear(x,y,r,n)
# Main meridian ring, with a toothed rim and illuminated engraved track.
for i in range(72):
 a=i*math.tau/72
 p=(CX+85*math.cos(a),CY+85*math.sin(a));q=(CX+89*math.cos(a),CY+89*math.sin(a))
 seg(p,q,ink,5);seg(p,q,brass[4],2)
for r in range(86,72,-1):
 col={86:ink,85:brass[1],84:brass[3],83:brass[7],82:brass[5],81:brass[3],80:brass[2],79:brass[1],78:brass[1],77:brass[2],76:brass[4],75:brass[6],74:brass[3],73:ink}[r]
 c.circle(CX,CY,r,col,False)
# Radial engraved tick marks and tiny angular rune glyphs.
for i in range(96):
 a=i*math.tau/96
 if i%4:
  seg((CX+83*math.cos(a),CY+83*math.sin(a)),(CX+81*math.cos(a),CY+81*math.sin(a)),brass[7] if i%2 else brass[1])
def rune(x,y,a,col,kind):
 ux,uy=math.cos(a),math.sin(a);vx,vy=-uy,ux
 def p(u,v): return (x+ux*u+vx*v,y+uy*u+vy*v)
 seg(p(-2,-2),p(2,-2),col);seg(p(0,-2),p(0,2),col)
 if kind%3==0: seg(p(0,0),p(2,2),col);seg(p(-2,0),p(-2,2),col)
 elif kind%3==1: seg(p(-2,2),p(2,2),col);seg(p(2,-2),p(2,0),col)
 else: seg(p(-2,0),p(0,2),col);seg(p(0,2),p(2,0),col)
for i in range(32):
 a=i*math.tau/32
 rune(CX+79*math.cos(a),CY+79*math.sin(a),a,teal[4] if i%3 else brass[7],i)
# Compass crowns and screws around the massive outer bezel.
for i in range(8):
 a=i*math.tau/8
 x=round(CX+85*math.cos(a));y=round(CY+85*math.sin(a))
 c.circle(x,y,5,ink);c.circle(x,y,4,brass[4]);c.circle(x-1,y-1,2,brass[7]);c.line(x-1,y+1,x+2,y-2,brass[1])
# Two inner circular tracks.
for r,col in [(63,ink),(62,brass[5]),(61,brass[2]),(60,brass[3]),(59,brass[7]),(58,ink),(49,ink),(48,brass[3]),(47,brass[6]),(46,brass[1])]: c.circle(CX,CY,r,col,False)
for i in range(40):
 a=i*math.tau/40
 seg((CX+59*math.cos(a),CY+59*math.sin(a)),(CX+62*math.cos(a),CY+62*math.sin(a)),brass[1])
for i in range(16):
 a=i*math.tau/16
 rune(CX+53*math.cos(a),CY+53*math.sin(a),a,brass[4],i)
# Orbital ellipses: points of a tilted ring, layered front/back around the core.
def orbitpoint(t,rx,ry,angle):
 a=math.radians(angle);x=rx*math.cos(t);y=ry*math.sin(t)
 return (CX+x*math.cos(a)-y*math.sin(a),CY+x*math.sin(a)+y*math.cos(a))
def orbit(rx,ry,angle,start,end):
 pts=[orbitpoint(start+(end-start)*i/240,rx,ry,angle) for i in range(241)]
 for width,col,off in [(8,ink,0),(5,brass[3],0),(2,brass[7],-2),(1,brass[1],2)]:
  for p,q in zip(pts,pts[1:]):seg((p[0],p[1]+off),(q[0],q[1]+off),col,width)
 for i in range(61):
  t=start+(end-start)*i/60;p=orbitpoint(t,rx,ry,angle)
  if i%3==0: c.set(round(p[0]),round(p[1]),teal[5])
orbit(106,37,-27,math.pi,math.tau)
orbit(94,32,58,math.pi,math.tau)
# Instrument dials nested into the brass cage.
dial(88,128,13);dial(170,124,12);dial(113,164,10)
# Suspension spindle, cap and little alchemical gauge.
c.poly([(122,25),(122,16),(127,10),(132,16),(134,25)],ink)
c.poly([(125,23),(125,16),(128,13),(130,17),(131,23)],brass[5]);c.line(127,15,127,22,brass[8])
c.rect(119,24,18,5,ink);c.rect(120,24,16,2,brass[6])
c.poly([(121,185),(134,185),(137,192),(128,199),(119,192)],ink)
c.poly([(123,186),(132,186),(134,191),(128,196),(122,191)],brass[4]);c.line(124,188,128,194,brass[7])
# The core's concentric containment lattice.
for r,col in [(35,ink),(33,brass[3]),(32,brass[7]),(30,brass[1]),(28,teal[1]),(26,teal[2]),(23,teal[3]),(20,teal[4]),(16,teal[5]),(12,teal[6])]: c.circle(CX,CY,r,col)
for i in range(12):
 a=i*math.tau/12
 p=(CX+30*math.cos(a),CY+30*math.sin(a));q=(CX+24*math.cos(a+.12),CY+24*math.sin(a+.12))
 seg(p,q,ink,4);seg(p,q,brass[5],2)
 c.set(round(p[0]),round(p[1]),brass[8])
c.poly([(128,80),(144,103),(128,132),(111,105)],teal[1],False)
c.poly([(128,82),(141,104),(128,129),(115,105)],teal[6],False)
c.poly([(128,88),(137,104),(128,123),(119,105)],'#fcffe3')
c.poly([(128,88),(128,123),(119,105)],'#c7f8d9')
c.line(128,92,128,115,'#ffffff')
# Front arcs pass across the containment cage.
orbit(106,37,-27,0,math.pi)
orbit(94,32,58,0,math.pi)
# Radial mounting claws.
for x,y,a in [(56,145,-27),(193,66,-27),(94,51,58),(165,161,58)]:
 p=(x-5*math.cos(math.radians(a)),y-5*math.sin(math.radians(a)))
 q=(x+5*math.cos(math.radians(a)),y+5*math.sin(math.radians(a)))
 seg(p,q,ink,9);seg(p,q,brass[5],5);c.circle(x,y,2,brass[1]);c.set(x-1,y-1,brass[8])
# Faceted orbiting crystal spheres, cupped in miniature armillary frames.
def crystal(x,y,r,pal):
 c.circle(x+1,y+2,r+3,ink)
 c.circle(x,y,r,pal[0])
 c.poly([(x-r+2,y-3),(x-3,y-r+1),(x+3,y-r+2),(x+r-1,y-1),(x+3,y+r-2),(x-3,y+r-1),(x-r+1,y+2)],pal[2])
 c.poly([(x-3,y-r+1),(x-3,y),(x+3,y+3),(x+3,y-r+2)],pal[4])
 c.poly([(x-r+2,y-3),(x-3,y),(x-3,y+r-1),(x-r+1,y+2)],pal[1])
 c.poly([(x-3,y),(x+3,y+3),(x-3,y+r-1)],pal[3])
 c.poly([(x+3,y-r+2),(x+r-1,y-1),(x+3,y+3)],pal[3])
 c.line(x-4,y-r+3,x-1,y-r+2,pal[6]);c.set(x-5,y-r+4,pal[5]);c.set(x+3,y+3,pal[5])
 c.path(f'M {x-r-3} {y-2} Q {x-r-2} {y+r+5} {x+r+3} {y+3}',ink,False)
 c.path(f'M {x-r-3} {y-3} Q {x-r-2} {y+r+3} {x+r+3} {y+2}',brass[6],False)
 c.rect(x-2,y+r+1,5,3,brass[3]);c.line(x-2,y+r+1,x+2,y+r+1,brass[7])
crystal(43,132,12,teal)
crystal(211,67,13,['#252743','#3d3d6a','#665c9a','#9184bf','#b9b3e3','#e0ddf5','#fcf7ff'])
crystal(92,35,9,['#442a2d','#71433b','#a56848','#d49862','#f4cc86','#ffe5ae','#fff6dd'])
crystal(171,181,11,teal)
crystal(182,41,6,teal)
# Constellation etchings and sparks in the empty spaces.
for x,y in [(60,35),(201,111),(47,88),(155,13),(189,188),(73,190),(108,66),(149,148),(217,154)]:
 c.set(x-1,y,teal[2]);c.set(x+1,y,teal[2]);c.line(x,y-2,x,y+2,teal[3]);c.set(x,y,teal[6])
for i in range(45):
 x=random.randint(40,218);y=random.randint(17,201)
 if c.get(x,y) in [c.color(col) for col in bg]: c.set(x,y,random.choice([brass[2],brass[3],teal[2]]))
# Small polished glints on the rim.
for x,y in [(78,38),(151,26),(47,101),(199,146),(95,182)]:
 c.line(x-3,y,x+3,y,brass[8]);c.line(x,y-3,x,y+3,brass[8]);c.set(x,y,'#ffffff')
view(result)
save('arcane-instrument-giant',result)
finish(result)
