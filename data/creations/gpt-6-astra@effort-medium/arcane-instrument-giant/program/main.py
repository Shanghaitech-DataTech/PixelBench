import math, random
random.seed(14)
result=new_canvas(256,256,'#090e1b',name='Arcane astrolabe')
c=result
ink='#080c16'; deep='#171b28'; stone='#252b3b'; edge='#3a4251'
brass=['#392b29','#62432e','#926038','#bd8c48','#e1b963','#ffe39a']
cyan=['#123746','#1e6877','#36acb5','#79e3db','#d6fff0']
# distant hall masonry
c.rect(0,0,256,202,'#101522')
for y in range(12,202,19):
 c.line(0,y,255,y,'#171d2c')
 for x in range((y//19%2)*24,256,48):c.line(x,y,x,y+17,'#171d2c')
c.path('M 44 201 L 44 72 Q 44 4 128 -12 Q 212 4 212 72 L 212 201', '#080f1b')
for x in [14,30,219,235]:
 c.rect(x,0,7,203,'#1e2535');c.rect(x,0,2,203,'#303447');c.rect(x-3,189,13,8,stone)
c.path('M 34 183 L 34 72 Q 34 1 128 -7 Q 222 1 222 72 L 222 183','#2b3040',False)
c.path('M 40 180 L 40 73 Q 40 9 128 0 Q 216 9 216 73 L 216 180','#191f30',False)
# floor
c.rect(0,202,256,54,'#141b28')
for y in [206,217,235,254]:c.line(0,y,255,y,'#2a3040')
for x in [-80,-10,54,104,152,202,266,336]:
 c.line(128+(x-128)//4,202,max(0,min(255,x)),255,'#292f3e')
c.ellipse(128,229,72,12,'#0a101c')
# pedestal layered polygonal steps
c.poly([(65,230),(88,216),(168,216),(191,230),(191,239),(166,250),(87,250),(65,239)],ink)
c.poly([(67,230),(89,218),(167,218),(189,230),(167,241),(89,241)],'#424352')
c.poly([(68,232),(89,242),(166,242),(188,232),(188,238),(165,248),(90,248),(68,238)],'#252c3b')
c.line(91,242,164,242,'#67606a')
c.poly([(88,211),(103,201),(154,201),(170,211),(170,229),(155,237),(103,237),(88,228)],ink)
c.poly([(90,212),(104,205),(153,205),(168,212),(154,220),(104,220)],'#4b4a56')
c.poly([(92,214),(105,221),(153,221),(166,214),(166,228),(153,234),(105,234),(92,228)],'#303746')
c.rect(107,222,43,11,'#202a38')
for x in range(112,149,9):
 c.line(x,224,x,229,cyan[1]);c.line(x,224,x+3,226,cyan[2]);c.set(x+2,230,cyan[3])
c.ellipse(128,206,35,11,ink);c.ellipse(128,204,35,10,'#69606a');c.ellipse(128,203,30,7,'#343745');c.ellipse(128,202,22,5,cyan[0]);c.ellipse(128,202,16,3,cyan[1]);c.line(108,200,147,200,cyan[2])
# levitation particles
for i in range(40):
 x=random.randrange(103,153);y=random.randrange(173,201)
 c.set(x,y,random.choice([cyan[0],cyan[1],cyan[2],brass[2]]))
# mathematical ellipses in rotated planes
cx,cy=128,104
def point(a,rx,ry,rot=0):
 t=math.radians(a);r=math.radians(rot)
 return (round(cx+rx*math.cos(t)*math.cos(r)-ry*math.sin(t)*math.sin(r)),round(cy+rx*math.cos(t)*math.sin(r)+ry*math.sin(t)*math.cos(r)))
def arc(rx,ry,rot,col,start=0,end=360):
 prev=point(start,rx,ry,rot)
 for a in range(start+1,end+1):
  p=point(a,rx,ry,rot);c.line(*prev,*p,col);prev=p
def band(rx,ry,rot,width=7):
 for k in range(width+2,-2,-1):
  col=ink if k in [width+2,width+1,-1] else brass[min(5,max(0,int((width-k)*5/width)))]
  arc(rx+k,ry+k,rot,col)
def ticks(rx,ry,rot):
 for a in range(0,360,5):
  p=point(a,rx,ry,rot);q=point(a,rx+(4 if a%15==0 else 2),ry+(4 if a%15==0 else 2),rot)
  c.line(*p,*q,brass[0])
def rune(x,y,i):
 col=cyan[3] if i%3 else '#fbe4a3'
 c.line(x-2,y-3,x-2,y+3,cyan[0]);c.line(x-1,y-3,x-1,y+3,col)
 c.line(x-1,y-3,x+2,y-1,col);c.line(x-1,y+1,x+2,y-1,col)
 if i%2:c.line(x,y+1,x+2,y+3,col)
 else:c.set(x+2,y+3,col)
# toothed mechanism
from parts import gear
for x,y,r,t in [(72,148,20,14),(179,142,25,16),(91,166,13,10),(155,167,17,12),(173,61,18,12),(82,58,14,10)]:
 gear(c,x,y,r,t,brass,ink)
# supporting spokes and small screw heads
for a in range(0,360,30):
 p=point(a,23,23);q=point(a,82,82)
 c.line(*p,*q,brass[0]);c.line(p[0]+1,p[1],q[0]+1,q[1],brass[2])
# great outside zodiac ring
band(88,88,0,8);ticks(89,89,0)
for a in range(0,360,15):
 x,y=point(a,94,94);c.circle(x,y,2,ink);c.set(x,y,brass[5])
for i,a in enumerate(range(8,360,15)):
 x,y=point(a,92,92);rune(x,y,i)
# perpendicular orbit hoops
band(80,37,-38,5);ticks(82,39,-38)
band(78,36,58,6);ticks(80,38,58)
# round inner assembly
band(52,52,0,6);ticks(53,53,0)
for i,a in enumerate(range(0,360,30)):
 x,y=point(a,56,56);c.circle(x,y,2,ink);c.set(x,y,cyan[3])
# dial embedded left lower
for x,y,r in [(65,137,12),(179,123,11),(154,160,9)]:
 c.circle(x,y,r+2,ink);c.circle(x,y,r+1,brass[4]);c.circle(x,y,r,brass[1]);c.circle(x,y,r-2,'#172b33')
 for a in range(0,360,30):
  t=math.radians(a);c.set(round(x+(r-3)*math.cos(t)),round(y+(r-3)*math.sin(t)),brass[4])
 c.line(x-3,y+4,x+4,y-5,brass[5]);c.circle(x,y,1,cyan[3])
# radiant core, rays with crisp stepped aureole
for a in range(0,360,15):
 p=point(a,21,21);q=point(a,random.randrange(31,42),random.randrange(31,42));c.line(*p,*q,cyan[1])
c.circle(cx,cy,29,ink);c.circle(cx,cy,27,brass[3]);c.circle(cx,cy,25,brass[0]);c.circle(cx,cy,23,cyan[0])
for a in range(0,360,45):
 x,y=point(a,26,26);c.circle(x,y,2,brass[5])
c.circle(cx,cy,20,cyan[1]);c.circle(cx-1,cy-1,17,cyan[2]);c.circle(cx-2,cy-2,13,cyan[3]);c.circle(cx-2,cy-3,9,cyan[4]);c.circle(cx-3,cy-4,5,'#ffffdb')
c.line(105,100,150,100,cyan[3]);c.line(125,80,125,127,cyan[3])
c.poly([(128,84),(140,103),(128,120),(115,103)],'#ecffda',False)
# forward sweep across lower face
for k in range(7,-2,-1):arc(79+k,36+k,-15,ink if k in (7,-1) else brass[min(5,6-k)],0,180)
for a in range(12,175,9):
 p=point(a,81,38,-15);q=point(a,84,41,-15);c.line(*p,*q,brass[0])
# crystal globes with angular facets and brass cages
def crystal(x,y,r,cols):
 c.circle(x+1,y+2,r+3,ink);c.circle(x,y,r+1,brass[3]);c.circle(x,y,r,cols[0])
 c.poly([(x-r+2,y-3),(x-3,y-r+1),(x+r-3,y-r+4),(x+r-1,y+3),(x+2,y+r-1),(x-r+3,y+5)],cols[1])
 c.poly([(x-r+2,y-3),(x-3,y-r+1),(x+2,y-2),(x-2,y+5)],cols[2])
 c.poly([(x-3,y-r+1),(x+r-3,y-r+4),(x+2,y-2)],cols[3])
 c.poly([(x+2,y-2),(x+r-1,y+3),(x+2,y+r-1)],cols[0])
 c.line(x-3,y-r+2,x+2,y-2,cols[4]);c.line(x-r+3,y-3,x+2,y-2,cols[3])
 c.rect(x-4,y-r-3,9,3,ink);c.rect(x-3,y-r-3,7,2,brass[4])
 c.rect(x-3,y+r+1,7,3,brass[2]);c.set(x-4,y-5,cols[4]);c.line(x-6,y-6,x-2,y-6,cols[4])
crystal(59,69,13,cyan)
crystal(194,89,15,['#242044','#494075','#7968ae','#b6a1e0','#efe1ff'])
crystal(109,176,12,['#452432','#894447','#d37a60','#ffc38a','#fff4ca'])
crystal(149,40,9,cyan)
# celestial finial and axis
for x,y in [(128,10),(128,198),(29,104),(227,104)]:
 c.circle(x,y,4,ink);c.circle(x,y,3,brass[2]);c.set(x-1,y-1,brass[5])
c.poly([(124,12),(128,2),(132,12),(128,17)],brass[3]);c.line(128,3,128,13,brass[5])
# luminous dust and metallic glints
for x,y in [(42,47),(208,130),(78,29),(162,20),(36,145),(196,174),(90,192),(153,188)]:
 c.set(x,y,cyan[2]);c.set(x+3,y-4,brass[2])
for x,y in [(61,60),(194,78),(87,24),(44,117),(158,171),(149,33),(128,90)]:
 c.line(x-3,y,x+3,y,'#fff4cf');c.line(x,y-3,x,y+3,'#fff4cf');c.set(x-1,y-1,cyan[3])
view(c)
save('arcane-instrument',c)
finish(result)
