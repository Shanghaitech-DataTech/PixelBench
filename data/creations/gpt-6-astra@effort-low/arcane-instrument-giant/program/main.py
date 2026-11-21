import math, random
random.seed(18)
c=new_canvas(256,256,background='#080c18',name='Arcane orrery')
# restrained ramp colors
ink='#080b14'; shadow='#302326'; bronze='#65452e'; brass='#a7783c'; gold='#d5a853'; light='#ffe29a'; teal='#48cabc'; ice='#baffec'
# hall masonry
for y in range(0,219,18):
 for x in range(-20,256,32):
  xx=x+(16 if y%36 else 0)
  c.rect(max(0,xx),y,31,17,random.choice(['#0c1220','#0e1422','#101624']))
# distant gothic recesses
for x in [30,226]:
 c.path(f'M {x-17} 197 L {x-17} 58 Q {x-17} 29 {x} 16 Q {x+17} 29 {x+17} 58 L {x+17} 197 Z','#18202c')
 c.path(f'M {x-12} 194 L {x-12} 59 Q {x-12} 37 {x} 24 Q {x+12} 37 {x+12} 59 L {x+12} 194 Z','#080e1b')
 c.line(x,38,x,192,'#1b2531')
for x in [6,56,195,245]:
 c.rect(x,0,5,212,'#1c2330'); c.line(x,0,x,209,'#29303a'); c.rect(x-3,203,11,9,'#242b36')
c.poly([(0,213),(256,213),(256,256),(0,256)],'#111725')
for x in range(-128,385,42): c.line(128,207,x,255,'#252c37')
for y in [220,231,248]: c.line(0,y,255,y,'#252c37')
c.ellipse(128,232,66,12,'#080d18')
# pedestal
c.poly([(84,226),(172,226),(183,240),(172,247),(84,247),(73,240)],ink)
c.poly([(84,225),(172,225),(180,237),(76,237)],'#45505b')
c.rect(80,237,96,7,'#252e3c'); c.line(81,237,175,237,'#677079')
c.poly([(93,210),(163,210),(168,234),(88,234)],'#343e4b')
for x in [93,105,149,161]: c.line(x,216,x-2 if x<128 else x+2,232,'#626875')
c.ellipse(128,210,48,10,ink); c.ellipse(128,208,47,9,'#67717a'); c.ellipse(128,207,40,6,'#313c49'); c.ellipse(128,207,29,4,'#23535a')
for x in range(106,151,11):
 c.line(x,220,x,228,teal); c.line(x-2,221,x+2,221,teal); c.set(x+2,225,ice)
# floating light
for y,w in [(195,18),(199,25),(202,31)]: c.ellipse(128,y,w,2,'#21444c',False)
# ring helpers
cx,cy=128,105
def point(rx,ry,t,rot=0):
 a=math.radians(t); r=math.radians(rot)
 x=rx*math.cos(a); y=ry*math.sin(a)
 return round(cx+x*math.cos(r)-y*math.sin(r)),round(cy+x*math.sin(r)+y*math.cos(r))
def curve(rx,ry,rot,col,start=0,end=360):
 prev=point(rx,ry,start,rot)
 for i in range(start+1,end+1):
  p=point(rx,ry,i,rot);c.line(*prev,*p,col);prev=p
def ring(rx,ry,rot,width=6):
 for d in range(2,-width-2,-1):
  col=ink if d in [2,1,-width-1] else light if d==0 else gold if d==-1 else bronze if d<-width+1 else brass
  curve(rx+d,ry+d,rot,col)
def gear(x,y,r,n):
 for i in range(n):
  a=i*2*math.pi/n
  px=round(x+math.cos(a)*r);py=round(y+math.sin(a)*r)
  c.rect(px-2,py-2,5,5,ink);c.rect(px-1,py-1,3,3,brass)
 c.circle(x,y,r,ink);c.circle(x,y,r-2,gold);c.circle(x,y,r-4,bronze);c.circle(x,y,r-6,ink)
 for i in range(6):
  a=i*math.pi/3;c.line(x,y,round(x+math.cos(a)*(r-4)),round(y+math.sin(a)*(r-4)),brass)
 c.circle(x,y,3,gold);c.set(x-1,y-1,light)
# suspension tips
c.line(128,8,128,191,bronze)
c.poly([(128,3),(133,12),(128,20),(123,12)],gold)
c.circle(128,12,2,ice)
# far orbital ellipse
ring(99,43,-37,5)
# giant outer casing
ring(87,87,0,9)
for a in range(0,360,5):
 p=point(85,85,a);q=point(80 if a%15==0 else 82,80 if a%15==0 else 82,a)
 c.line(*p,*q,shadow)
for a in range(0,360,30):
 x,y=point(83,83,a);c.circle(x,y,2,ink);c.set(x,y,light)
# internal framework spokes
for a in range(0,360,45):
 p=point(76,76,a);q=point(23,23,a+18)
 c.line(*p,*q,ink);c.line(p[0]+1,p[1],q[0]+1,q[1],brass)
# machinery interior
for x,y,r,n in [(84,65,15,12),(165,64,18,14),(78,126,17,12),(157,148,20,16),(111,164,12,10),(181,107,11,10),(111,52,10,10)]: gear(x,y,r,n)
# alchemical dial
for x,y,r in [(100,88,13),(158,118,12),(127,145,9)]:
 c.circle(x,y,r+2,ink);c.circle(x,y,r+1,light);c.circle(x,y,r,bronze);c.circle(x,y,r-2,'#172e36')
 for a in range(0,360,30):
  t=math.radians(a);c.set(round(x+(r-3)*math.cos(t)),round(y+(r-3)*math.sin(t)),gold)
 c.line(x-4,y+4,x+5,y-6,light);c.circle(x,y,2,brass)
ring(66,66,0,5)
# rune glyphs tangent to ring, little angular inscriptions
for a in range(0,360,18):
 t=math.radians(a)
 def rp(u,v): return (round(cx+(60+v)*math.cos(t)-u*math.sin(t)),round(cy+(60+v)*math.sin(t)+u*math.cos(t)))
 for p,q in [((-2,-2),(-2,2)),((-2,2),(2,0)),((2,0),(0,-2))]: c.line(*rp(*p),*rp(*q),teal)
 c.set(*rp(3,2),ice)
# core nested glow rings
for r,col in [(31,'#142b35'),(28,'#1e4548'),(25,'#28615c'),(22,'#31887a')]: c.circle(128,105,r,col)
ring(28,28,0,3)
c.poly([(128,77),(145,91),(149,112),(128,132),(108,113),(111,92)],ink)
c.poly([(128,80),(143,93),(146,112),(128,128),(111,112),(114,93)],teal)
c.poly([(128,80),(128,107),(114,93)],'#83f1ce')
c.poly([(128,80),(143,93),(128,107)],ice)
c.poly([(128,107),(146,112),(128,128)],'#50b6a2')
c.poly([(128,107),(111,112),(128,128)],'#288275')
c.poly([(128,90),(136,104),(128,117),(120,104)],'#eaffce');c.line(128,85,128,120,'#fff6ce')
# crossing orbital hoops
ring(101,34,36,5)
ring(88,31,-64,5)
# polished front segments
curve(101,34,36,light,20,130)
# satellites
for rx,ry,angle,rot,r,col in [(99,43,190,-37,12,'blue'),(101,34,12,36,13,'blue'),(88,31,207,-64,10,'purple'),(99,43,62,-37,8,'purple')]:
 x,y=point(rx,ry,angle,rot)
 c.circle(x,y,r+3,ink);c.circle(x,y,r+2,brass);c.circle(x,y,r+1,light);c.circle(x,y,r,ink)
 shades=['#143945','#226374','#3b9eac','#79dfdc','#d1fff0'] if col=='blue' else ['#302842','#57416c','#9068a4','#c496c9','#ffe0ef']
 c.circle(x,y,r-1,shades[0]);c.circle(x-1,y-1,r-3,shades[1]);c.circle(x-3,y-3,r-5,shades[2]);c.line(x-r+4,y-3,x-2,y-r+4,shades[4]);c.rect(x-4,y-5,3,2,shades[4]);c.line(x+2,y+r-4,x+r-4,y+2,shades[2])
 c.line(x-r-4,y,x-r,y,gold);c.line(x+r,y,x+r+4,y,gold)
# small jewel mount at bottom
c.poly([(128,181),(134,188),(128,197),(122,188)],ink);c.poly([(128,183),(131,188),(128,193),(125,188)],teal)
# glints and suspended motes
for x,y in [(52,52),(183,39),(209,137),(107,20),(43,153),(155,184)]:
 c.line(x-3,y,x+3,y,light);c.line(x,y-3,x,y+3,light);c.set(x,y,ice)
for i in range(36):
 x=random.randrange(40,216);y=random.randrange(20,202)
 if ((x-128)**2+(y-105)**2)>90**2: c.set(x,y,random.choice(['#3b6466','#7a936f','#ae965b']))
view(c)
finish(c)
