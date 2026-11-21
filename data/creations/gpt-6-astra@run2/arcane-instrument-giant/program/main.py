import math, random
random.seed(27)
c=new_canvas(256,256,'#090c19',name='Astral engine')
# Palette: cold architectural shadows, warm patinated brass, spectral turquoise
ink='#080b14'; deep='#111725'; stone='#20283a'; edge='#30394b'
brass=['#282326','#49362b','#715034','#9c713e','#c39450','#e0b768','#ffe1a0']
cyan=['#163b49','#205e6c','#328b95','#58bdbe','#91e5da','#d7fff0']
# gloomy hall
c.rect(8,0,240,220,'#0d1220')
c.path('M 30 219 V 86 Q 30 14 128 1 Q 226 14 226 86 V 219', '#161d2d')
c.path('M 40 219 V 87 Q 40 27 128 12 Q 216 27 216 87 V 219', '#0b101e')
for x in (10,26,225,241):
 c.rect(x,0,5,219,'#1b2232'); c.line(x,0,x,218,'#2a3040')
for y in (24,55,88,123,158,193):
 for x in (8,24,224,240): c.rect(x,y,9,4,'#101522'); c.line(x,y,x+8,y,'#303449')
for y in (208,222,239,254): c.line(0,y,255,y,'#222737')
for x in (-120,-20,52,128,204,276,376):
 c.line(128+(x-128)//4,205,max(0,min(255,x)),255,'#242a39')
# faint core halo, discrete concentric flat shades
for r,col in [(93,'#101b2a'),(78,'#122332'),(61,'#172c37'),(45,'#203a40')]: c.circle(128,104,r,col)
# masonry behind machine, restrained
for y in (44,76,108,140,172):
 c.line(41,y,57,y,'#1b2330');c.line(203,y,216,y,'#1b2330')
# pedestal and projected shadow
hall=c
c=new_canvas(256,256,name='Pedestal')
c.ellipse(128,236,65,12,'#070a12')
c.poly([(79,221),(128,206),(178,221),(178,237),(128,252),(79,237)],ink)
c.poly([(81,222),(128,210),(175,222),(128,237)],'#48505a')
c.poly([(81,225),(128,239),(128,249),(81,235)],'#252e40')
c.poly([(128,239),(175,225),(175,235),(128,249)],'#182132')
c.line(83,224,128,237,'#697072');c.line(128,237,173,224,'#3f535c')
c.poly([(94,205),(128,197),(162,205),(160,226),(128,235),(96,225)],ink)
c.poly([(98,206),(128,201),(128,230),(99,223)],'#35404c')
c.poly([(128,201),(158,206),(157,223),(128,230)],'#253241')
for x in (103,111,119):
 c.line(x,211+(x-103)//4,x,222+(x-103)//4,'#172434');c.line(x+1,211+(x-103)//4,x+1,222+(x-103)//4,'#515b61')
c.poly([(88,201),(127,190),(169,201),(169,210),(128,222),(88,210)],ink)
c.poly([(90,201),(128,192),(166,201),(128,212)],'#697477')
c.poly([(90,203),(128,214),(128,219),(90,208)],'#3b4b54')
c.poly([(128,214),(166,203),(166,208),(128,219)],'#263b46')
c.line(92,202,128,212,'#a5aea0');c.line(128,212,165,202,'#5f8b8c')
c.ellipse(128,201,26,7,brass[1]);c.ellipse(128,200,26,6,brass[4]);c.ellipse(128,200,21,4,cyan[0]);c.ellipse(128,200,15,2,cyan[3]);c.line(116,199,139,199,cyan[5])
# Lower the plinth to leave a visible levitation gap.
base=new_canvas(256,256,name='Lowered pedestal')
c.select(0,190,256,64).resize(256,54).copy_to(0,200,base,mode='over')
c=flatten([hall,base],name='Astral engine finished')
# primitive multi segment strokes
def stroke(points,color,width=1):
 for a,b in zip(points,points[1:]):
  if width==1: c.line(round(a[0]),round(a[1]),round(b[0]),round(b[1]),color)
  else:
   n=max(1,int(math.dist(a,b)*2))
   for i in range(n+1):
    t=i/n;c.circle(round(a[0]+(b[0]-a[0])*t),round(a[1]+(b[1]-a[1])*t),width//2,color)
def orbit(cx,cy,rx,ry,angle,t):
 a=math.radians(angle);t=math.radians(t)
 return (cx+rx*math.cos(t)*math.cos(a)-ry*math.sin(t)*math.sin(a),cy+rx*math.cos(t)*math.sin(a)+ry*math.sin(t)*math.cos(a))
def ring(cx,cy,rx,ry,angle,start=0,end=360,wide=7):
 p=[orbit(cx,cy,rx,ry,angle,t) for t in range(start,end+1,2)]
 stroke(p,ink,wide+4);stroke(p,brass[1],wide+2);stroke(p,brass[4],wide)
 stroke([(x,y-1) for x,y in p],brass[6],1)
 stroke([(x,y+2) for x,y in p],brass[2],1)
 return p
def gear(x,y,r,teeth=12):
 pts=[]
 for i in range(teeth*4):
  a=i*math.tau/(teeth*4); rr=r if i%4 in (1,2) else r-3
  pts.append((round(x+rr*math.cos(a)),round(y+rr*math.sin(a))))
 c.poly(pts,ink);c.poly([(x+(a-x)*.91,y+(b-y)*.91) for a,b in pts],brass[3]);c.circle(x,y,r-5,brass[5]);c.circle(x,y,r-7,brass[1])
 for i in range(6):
  a=i*math.tau/6
  c.line(x,y,round(x+(r-6)*math.cos(a)),round(y+(r-6)*math.sin(a)),brass[4])
 for j in range(teeth):
  a=(j+.5)*math.tau/teeth
  px=round(x+(r-4)*math.cos(a));py=round(y+(r-4)*math.sin(a))
  c.set(px,py,brass[1])
 for j in range(6):
  a=(j+.5)*math.tau/6
  px=round(x+(r-10)*math.cos(a));py=round(y+(r-10)*math.sin(a))
  c.circle(px,py,1,ink)
 c.circle(x,y,4,ink);c.circle(x,y,2,brass[6]);c.set(x+1,y+1,brass[3])
def rune(x,y,ang,idx,col=cyan[4]):
 # small radial runic glyphs, individual strokes, no font
 designs=[ [(-2,-3),(-2,3),(2,0),(-2,-1)], [(-2,-2),(0,-4),(2,-2),(0,0),(0,3)], [(-2,3),(0,-3),(2,3),(0,1),(-2,3)], [(-2,-3),(2,-3),(0,-1),(0,3)], [(-2,-3),(-2,2),(2,2),(2,-2)] ]
 a=math.radians(ang)
 pts=[(x+u*math.cos(a)-v*math.sin(a),y+u*math.sin(a)+v*math.cos(a)) for u,v in designs[idx%5]]
 stroke([(u+1,v+1) for u,v in pts],cyan[0]);stroke(pts,col)
# floating gimbal foot and spine
c.poly([(121,153),(135,153),(139,174),(133,187),(128,194),(123,187),(117,174)],ink)
c.poly([(125,155),(131,155),(134,176),(128,189),(123,176)],brass[3]);c.line(126,158,126,182,brass[6]);c.circle(128,175,6,ink);c.circle(128,175,4,cyan[2]);c.set(126,173,cyan[5])
# radial supporting struts behind rings
for a in (15,65,115,165,215,265,315):
 p=orbit(128,105,83,83,0,a)
 stroke([(128,105),p],ink,7);stroke([(128,105),p],brass[2],3)
# outer circumferential ring
ring(128,104,88,88,0,wide=7)
# engraved indices and studs around outer circumference
for a in range(0,360,5):
 p=orbit(128,104,85,85,0,a);q=orbit(128,104,89 if a%15 else 91,89 if a%15 else 91,0,a)
 stroke([p,q],brass[1])
 if a%30==0:
  x,y=orbit(128,104,88,88,0,a);c.circle(round(x),round(y),2,ink);c.set(round(x),round(y),brass[6])
# inner engraved turquoise runic band
ring(128,104,75,75,0,wide=5)
for j,a in enumerate(range(8,360,18)):
 x,y=orbit(128,104,75,75,0,a);rune(x,y,a+90,j)
# top finial and alignment spear
stroke([(128,6),(128,34)],ink,5);stroke([(128,7),(128,32)],brass[5],1)
c.poly([(128,2),(133,12),(128,20),(123,12)],ink);c.poly([(128,5),(130,12),(128,16),(126,12)],cyan[3]);c.set(128,8,cyan[5])
# mechanical assemblies nested inside gimbal
for x,y,r,n in [(75,144,20,13),(93,164,14,10),(168,141,22,14),(186,122,13,10),(99,59,15,11),(155,53,13,10)]: gear(x,y,r,n)
# small alchemical dials
def dial(x,y,r):
 c.circle(x,y,r+2,ink);c.circle(x,y,r,brass[5]);c.circle(x,y,r-2,brass[1]);c.circle(x,y,r-3,'#162c35')
 for a in range(0,360,30):
  p=orbit(x,y,r-3,r-3,0,a);q=orbit(x,y,r-5,r-5,0,a);stroke([p,q],brass[5])
 stroke([(x-4,y+4),(x+3,y-6)],cyan[4]);c.circle(x,y,1,brass[6])
dial(63,99,12);dial(190,85,10);dial(113,158,9)
# crossing elliptical orbit bands behind central core
ring(128,104,107,37,-35,wide=5)
ring(128,104,101,39,44,wide=5)
ring(128,104,35,90,10,wide=4)
# ornamented central core housing
c.circle(128,104,32,ink);c.circle(128,104,30,brass[3]);c.circle(128,104,28,brass[6]);c.circle(128,104,26,brass[1]);c.circle(128,104,23,cyan[0])
for a in range(0,360,30):
 p=orbit(128,104,28,28,0,a);q=orbit(128,104,32,32,0,a);stroke([p,q],ink,3);stroke([p,q],brass[5])
# radiant light in stepped color shells
for r,col in [(21,cyan[1]),(18,cyan[2]),(15,cyan[3]),(12,cyan[4]),(8,cyan[5])]:c.circle(128,104,r,col)
c.poly([(128,83),(133,98),(147,104),(133,109),(128,124),(123,109),(109,104),(123,99)],'#baffea')
c.poly([(128,89),(131,101),(141,104),(131,107),(128,118),(125,107),(116,104),(125,101)],'#ffffd5')
c.line(118,93,122,89,cyan[5]);c.line(113,99,113,105,cyan[4])
# foreground orbital arcs, strategically mask central core only around the edge
ring(128,104,107,37,-35,0,145,wide=5)
ring(128,104,101,39,44,8,153,wide=5)
# engraving diagonal bands
for j,t in enumerate(range(12,151,13)):
 x,y=orbit(128,104,101,39,44,t);rune(x,y,44,j,brass[6])
for t in range(188,348,9):
 p=orbit(128,104,107,36,-35,t);q=orbit(128,104,107,39,-35,t);stroke([p,q],brass[1])
# crystal satellites held in ornate brass cages
def crystal(x,y,r,colors):
 c.ellipse(x,y+r+3,r+4,3,ink)
 c.circle(x,y,r+3,ink);c.circle(x,y,r+1,brass[3]);c.circle(x,y,r,colors[0])
 c.poly([(x,y-r+1),(x+r-2,y-3),(x+r-1,y+4),(x,y+r-1),(x-r+2,y+3),(x-r+2,y-4)],colors[1])
 c.poly([(x,y-r+1),(x+3,y-2),(x,y+5),(x-r+2,y+3),(x-r+2,y-4)],colors[2])
 c.poly([(x,y-r+1),(x+3,y-2),(x+r-2,y-3)],colors[3])
 c.poly([(x+3,y-2),(x+r-1,y+4),(x,y+r-1),(x,y+5)],colors[0])
 c.line(x-r+4,y-3,x-2,y-r+4,colors[4]);c.set(x-3,y-r+3,colors[4])
 c.line(x-r-3,y+3,x-r-1,y+7,brass[5]);c.line(x-r-1,y+7,x+r-1,y+7,brass[3]);c.line(x+r-1,y+7,x+r+3,y+2,brass[5]);c.set(x,y+r+2,brass[6])
crystal(51,147,12,cyan[0:5])
crystal(207,54,13,['#312749','#514478','#7965a4','#b096d0','#e8d9ff'])
crystal(83,39,10,['#1b4654','#226b7b','#399eab','#77d7d6','#d5fff0'])
crystal(187,169,14,['#423240','#74415b','#b86276','#ee9d9a','#ffe3bd'])
crystal(153,20,7,['#24504c','#397866','#6daf82','#a4e2ad','#e0ffcf'])
# reflective accents and bolts
for x,y in [(42,105),(214,105),(128,191),(128,17),(65,58),(191,151)]:
 c.circle(x,y,4,ink);c.circle(x,y,3,brass[3]);c.line(x-1,y-2,x+1,y-2,brass[6]);c.set(x,y,brass[1])
# suspended energy from engine to dais
for y,w in [(194,1),(198,2),(202,1),(206,2)]: c.line(128-w,y,128+w,y,cyan[3])
c.set(123,200,cyan[1]);c.set(134,204,cyan[2]);c.set(122,207,cyan[2])
# sparse dust illuminated by machine
for i in range(47):
 x=random.randrange(35,222);y=random.randrange(12,206)
 if c.get(x,y) in [c.color('#0b101e'),c.color('#101b2a'),c.color('#122332')]:
  c.set(x,y,random.choice(['#36505a','#4d676a','#6f8179']))
# sharp crystalline glints
for x,y in [(202,47),(78,34),(46,140),(182,161),(128,103)]:
 c.line(x-3,y,x+3,y,cyan[5]);c.line(x,y-4,x,y+4,'#ffffdf');c.set(x-1,y-1,'#ffffdf')
view(c)
result=c
save('arcane-instrument',result)
finish(result)
