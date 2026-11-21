import math, random
random.seed(13)
result = new_canvas(256,256,background='#090e1c',name='Arcane Orrery')
c=result
P={'ink':'#080b14','edge':'#161827','deep':'#302531','bronze':'#604034','shade':'#885338','brass':'#b47c43','gold':'#dda75c','light':'#f6d58a','white':'#fff4cb','teal':'#236373','cyan':'#51c9ce','ice':'#b4fff0'}
def line(x,y,X,Y,col):c.line(round(x),round(y),round(X),round(Y),col)
def poly(pts,col):c.poly([(round(x),round(y)) for x,y in pts],col)
def circ(x,y,r,col):c.circle(round(x),round(y),r,col)
def pos(cx,cy,rx,ry,a,rot=0):
 t=math.radians(a);r=math.radians(rot);x=rx*math.cos(t);y=ry*math.sin(t)
 return cx+x*math.cos(r)-y*math.sin(r),cy+x*math.sin(r)+y*math.cos(r)
def arc(cx,cy,rx,ry,col,rot=0,start=0,end=360):
 last=pos(cx,cy,rx,ry,start,rot)
 for a in range(start+2,end+2,2):
  p=pos(cx,cy,rx,ry,min(a,end),rot);line(*last,*p,col);last=p
# Hall: layered vaulted recess and masonry
c.rect(20,0,216,215,'#101827')
c.path('M 39 214 L 39 78 Q 39 13 128 1 Q 217 13 217 78 L 217 214 Z','#182233')
c.path('M 47 213 L 47 79 Q 47 24 128 11 Q 209 24 209 79 L 209 213 Z','#0c1322')
c.path('M 58 213 L 58 80 Q 58 36 128 23 Q 198 36 198 80 L 198 213','#233045',False)
c.path('M 61 212 L 61 81 Q 61 40 128 27 Q 195 40 195 81 L 195 212','#141e30',False)
for x in [12,27,225,240]:
 c.rect(x,0,5,217,'#1a2332');c.rect(x,0,1,217,'#293043');c.rect(x+4,0,2,217,'#070d19')
 for y in [29,77,127,177,211]:c.rect(x-3,y,11,3,'#263044');c.line(x-2,y+3,x+7,y+3,'#080d1a')
for y in [54,86,118,150,182,213]:
 for x in [0,33,202,247]:c.line(x,y,min(x+10,255),y,'#222a3a')
# Floor tiles
c.rect(0,218,256,38,'#121b2a');c.line(0,218,255,218,'#30374a')
for y in [225,236,252]:c.line(0,y,255,y,'#283144');c.line(0,y+1,255,y+1,'#0b1220')
for x in [-60,-10,40,90,166,216,266,316]:line(128+(x-128)*.39,218,x,255,'#30364a')
c.ellipse(129,235,75,12,'#080d19');c.ellipse(129,231,53,7,'#0c1421')
# Quiet blue ambient motes
for i in range(65):
 x=random.randrange(35,222);y=random.randrange(10,216)
 if random.random()<.6:c.set(x,y,random.choice(['#1e3446','#294859','#365467']))
# Pedestal cut stone, assembled on an independent layer
c=new_canvas(256,256,name='Pedestal working layer')
poly([(87,220),(169,220),(182,231),(174,241),(81,241),(74,232)],P['ink'])
poly([(87,220),(167,220),(178,230),(77,230)],'#536071')
poly([(78,231),(178,231),(173,239),(83,239)],'#2b3549')
c.line(82,232,175,232,'#7b8090');c.line(85,240,171,240,'#141b2d')
poly([(98,198),(159,198),(165,225),(92,225)],'#111929')
poly([(99,200),(157,200),(162,224),(95,224)],'#354256')
poly([(99,200),(113,203),(110,223),(95,224)],'#4e5b6c')
poly([(145,203),(157,200),(162,224),(149,222)],'#222d40')
c.rect(115,205,28,17,'#152336');c.rect(117,206,24,1,'#687381')
c.poly([(122,212),(128,207),(134,212),(128,219)],'#39717a',False)
c.line(124,212,132,212,P['cyan']);c.set(128,210,P['ice']);c.set(128,216,P['cyan'])
for x in [102,152]:c.line(x,205,x,218,'#77818a');c.line(x+2,206,x+2,221,'#1d293c')
c.ellipse(128,198,46,10,P['ink']);c.rect(82,195,93,6,P['ink'])
c.ellipse(128,198,44,8,'#334155');c.ellipse(128,194,46,9,'#75808a');c.ellipse(128,193,40,6,'#354353');arc(128,194,44,8,'#a1a5a0',start=0,end=180)
c.ellipse(128,193,27,4,'#122638');arc(128,193,27,4,'#4a9ba2')
# Lower the altar cap to leave an open levitation gap
result.blit(c,0,12)
c=result
# Floating field lines
for y,rx in [(201,17),(206,23)]:
 arc(128,y,rx,3,'#24505e');arc(128,y,rx,3,'#5ba8ae',start=10,end=120)
for x in [116,128,140]:
 c.line(x,198,x,209,'#244f60');c.set(x,205,'#70cdd1')
# mechanical helpers
def gear(cx,cy,r,teeth=16):
 pts=[]
 for i in range(teeth*4):
  a=360*i/(teeth*4);rr=r if i%4 in [1,2] else r-3
  pts.append(pos(cx,cy,rr,rr,a))
 poly(pts,P['ink']);
 pts2=[]
 for i in range(teeth*4):
  a=360*i/(teeth*4);rr=r-1 if i%4 in [1,2] else r-4
  pts2.append(pos(cx,cy,rr,rr,a))
 poly(pts2,P['brass']);circ(cx,cy,r-5,P['deep']);arc(cx,cy,r-5,r-5,P['light'],start=190,end=310)
 for a in range(0,360,60):line(*pos(cx,cy,3,3,a),*pos(cx,cy,r-6,r-6,a),P['bronze'])
 circ(cx,cy,4,P['ink']);circ(cx,cy,2,P['gold']);c.set(round(cx),round(cy-1),P['white'])
def band(cx,cy,rx,ry,width,rot=0,start=0,end=360):
 # dark borders and a lit chamfer, rendered in discrete metal tones
 for a in range(start,end,2):
  b=min(a+2,end)
  v=math.cos(math.radians(a+125))
  col=P['gold'] if v>.6 else P['brass'] if v>-.1 else P['shade'] if v>-.75 else P['bronze']
  poly([pos(cx,cy,rx,ry,a,rot),pos(cx,cy,rx,ry,b,rot),pos(cx,cy,rx-width,ry-width,b,rot),pos(cx,cy,rx-width,ry-width,a,rot)],col)
 arc(cx,cy,rx+1,ry+1,P['ink'],rot,start,end);arc(cx,cy,rx-width-1,ry-width-1,P['ink'],rot,start,end)
 arc(cx,cy,rx-1,ry-1,P['light'],rot,start,end)
 arc(cx,cy,rx-width+1,ry-width+1,P['deep'],rot,start,end)
def rune(cx,cy,a,r,col,index):
 # tiny radial inscriptions with five distinct letterforms
 ux,uy=math.cos(math.radians(a)),math.sin(math.radians(a));vx,vy=-uy,ux
 x,y=cx+r*ux,cy+r*uy
 shapes=[ [(-2,-2),(2,-2),(0,0),(2,2),(-2,2)], [(-2,2),(-2,-2),(2,0),(-2,1)], [(-2,-2),(0,2),(2,-2),(0,0),(-2,-2)], [(-2,1),(2,1),(0,-2),(0,3)], [(-2,-2),(-2,2),(2,2),(2,-2)] ]
 sh=shapes[index%5]
 for (u,v),(s,t) in zip(sh,sh[1:]):line(x+u*vx+v*ux,y+u*vy+v*uy,x+s*vx+t*ux,y+s*vy+t*uy,col)
# rear celestial ring and spines
band(128,105,98,83,3,-24)
for a in range(0,360,30):
 p=pos(128,105,98,83,a,-24);circ(*p,3,P['ink']);circ(*p,1,P['gold'])
# radial braces behind the great limb
for a in [25,65,115,155,205,245,295,335]:
 p=pos(128,104,37,37,a);q=pos(128,104,84,84,a)
 line(*p,*q,P['ink']);line(p[0]+1,p[1],q[0]+1,q[1],P['shade'])
# major limb
band(128,104,87,87,11)
arc(128,104,82,82,P['deep']);arc(128,104,79,79,P['gold'])
for a in range(0,360,3):
 r=85 if a%15 else 83
 line(*pos(128,104,r,r,a),*pos(128,104,86,86,a),P['deep'])
for i,a in enumerate(range(0,360,15)):
 rune(128,104,a,81,P['ice'] if i%3==0 else P['cyan'],i)
# inner degree circle
band(128,104,71,71,4)
for a in range(0,360,6):line(*pos(128,104,68,68,a),*pos(128,104,65 if a%30==0 else 67,65 if a%30==0 else 67,a),P['gold'])
# external gear trains
for x,y,r,t in [(57,158,17,14),(77,174,12,12),(188,150,18,15),(201,129,11,11),(172,177,12,12),(43,105,12,12),(199,74,12,12)]:gear(x,y,r,t)
# hanging lower ornamental keystone
poly([(117,177),(139,177),(137,189),(128,197),(119,189)],P['ink'])
poly([(120,178),(136,178),(134,188),(128,194),(122,188)],P['brass'])
poly([(124,179),(132,179),(131,187),(128,191),(125,187)],P['deep']);c.line(122,180,124,187,P['light']);c.line(128,181,128,186,P['cyan'])
# Exposed inner escapements and meshing planetary gears
for gx,gy,gr,gt in [(104,73,10,12),(150,68,8,10),(153,139,10,12),(100,126,8,10),(170,129,7,9)]:
 gear(gx,gy,gr,gt)
# orbit tilted around the heart; back halves
band(128,104,78,34,5,39,180,360)
band(128,104,77,32,5,-43,180,360)
# fine equatorial hoops
arc(128,104,74,22,'#192b38',12);arc(128,104,74,22,P['shade'],12,start=180,end=360)
# central cage and dials
gear(128,104,35,24)
band(128,104,28,28,5)
for a in range(0,360,30):
 line(*pos(128,104,20,20,a),*pos(128,104,27,27,a),P['gold'])
 circ(*pos(128,104,31,31,a),1,P['light'])
circ(128,104,21,'#15303b');arc(128,104,20,20,P['cyan']);arc(128,104,17,17,'#367581')
# radiant energy lancets
for a in range(0,360,45):
 poly([pos(128,104,11,11,a-14),pos(128,104,30 if a%90==0 else 23,30 if a%90==0 else 23,a),pos(128,104,11,11,a+14)],'#65c9c5')
# core sun faceted
circ(128,104,15,P['ink']);circ(128,104,14,'#ae7040');circ(127,103,12,'#edb95d')
poly([(116,100),(123,92),(133,93),(140,103),(134,113),(123,114)],'#ffe4a0')
poly([(116,100),(123,102),(126,112),(123,114),(117,108)],'#e5ac60')
poly([(123,92),(133,93),(135,99),(124,104),(119,100)],'#fff8d6');circ(128,103,5,'#fff8d6')
# front crossing bands
band(128,104,78,34,5,39,0,180)
band(128,104,77,32,5,-43,0,180)
for rot in [39,-43]:
 for i,a in enumerate(range(10,180,17)):
  x,y=pos(128,104,75,31 if rot==39 else 29,a,rot);circ(x,y,1,P['ice'] if i%2==0 else P['deep'])
# axis finials
for x,y in [(128,17),(128,191),(41,104),(215,104)]:
 circ(x,y,6,P['ink']);circ(x,y,4,P['shade']);circ(x-1,y-1,2,P['gold']);c.set(x-2,y-2,P['white'])
# top crown / astronomical sight
poly([(116,20),(120,11),(125,11),(128,4),(131,11),(136,11),(140,20)],P['ink'])
poly([(120,18),(123,13),(126,14),(128,8),(130,14),(133,13),(136,18)],P['gold'])
circ(128,20,6,P['ink']);circ(128,20,4,P['brass']);circ(128,20,2,P['cyan']);c.set(127,19,P['ice'])
# Alchemical inset dials, hands and marks
def dial(x,y,r):
 circ(x,y,r+2,P['ink']);circ(x,y,r,P['gold']);circ(x,y,r-2,P['deep']);circ(x,y,r-3,'#192733')
 for a in range(0,360,45):line(*pos(x,y,r-3,r-3,a),*pos(x,y,r-5,r-5,a),P['gold'])
 line(x,y,x-2,y-r+4,P['ice']);line(x,y,x+4,y+2,P['light']);circ(x,y,1,P['brass']);arc(x,y,r,r,P['light'],start=195,end=290)
dial(88,57,12);dial(174,62,10);dial(82,146,10);dial(164,157,13)
# spherical orbiting crystals with jewel facets
def sphere(x,y,r,purple=False):
 # mounting cradle
 circ(x,y,r+3,P['ink']);arc(x,y+1,r+2,r+2,P['brass'],start=10,end=165)
 dark,mid,lit,shine=('#30294e','#63568c','#ac8bc9','#eedbff') if purple else ('#144354','#267f92','#5ccecf','#ccfff0')
 circ(x,y,r,P['ink']);circ(x,y-1,r-1,dark)
 poly([(x-r+2,y-3),(x-3,y-r+1),(x+4,y-r+3),(x+r-2,y+1),(x+2,y+r-2),(x-r+3,y+3)],mid)
 poly([(x-r+2,y-3),(x-3,y-r+1),(x+3,y-r+3),(x+1,y),(x-5,y+3)],lit)
 poly([(x+1,y),(x+3,y-r+3),(x+r-2,y+1),(x+2,y+r-2)],dark)
 line(x-r+3,y+3,x+2,y+r-2,lit);line(x+1,y,x+2,y+r-2,mid)
 c.rect(x-4,y-r+3,3,2,shine);c.set(x-5,y-r+5,shine);c.set(x+r-3,y+1,lit)
 arc(x,y,r+2,r+2,P['gold'],start=35,end=145)
 line(x-3,y+r+3,x+3,y+r+3,P['light'])
sphere(68,80,12)
sphere(185,108,13,True)
sphere(109,158,10)
sphere(159,37,8,True)
sphere(51,128,7)
# orbit motion: small satellites, star jewels and luminous specks
for x,y in [(64,43),(196,43),(221,143),(91,188),(31,82)]:
 line(x-3,y,x+3,y,'#366b7d');line(x,y-3,x,y+3,'#366b7d');c.set(x,y,P['ice'])
for x,y in [(102,36),(149,72),(99,110),(152,128),(154,178),(209,92),(81,119)]:
 c.set(x,y,P['cyan']);c.set(x+1,y,P['teal'])
# brighter pinpoints on exposed bevels
for x,y in [(73,37),(54,63),(190,47),(48,96),(151,21),(85,171)]:
 c.line(x-2,y,x+2,y,P['light']);c.line(x,y-2,x,y+2,P['light']);c.set(x,y,P['white'])
assert result.stats()['colors_used'] <= 140
save('arcane-instrument-giant',result)
view(result)
finish(result)
