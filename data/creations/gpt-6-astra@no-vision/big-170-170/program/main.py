import random, math
import numpy as np
rng=random.Random(170)
output=input_canvas.copy(name='output')
# Clear the entire figure silhouette, using undisturbed ground and sky at matching heights.
erase=new_canvas(170,170)
erase.poly([(74,69),(84,68),(87,92),(83,110),(102,113),(110,127),(119,146),(119,161),(106,164),(88,161),(85,151),(50,153),(42,144),(40,122),(38,118),(45,112),(61,111),(77,113),(77,92),(73,89),(70,83),(70,74)],'#ffffff')
erase.rect(38,110,43,13,'#ffffff')
_,_,raw=erase.to_rgba(); em=np.frombuffer(raw,dtype=np.uint8).reshape(170,170,4)[:,:,3]>0
for y in range(170):
 for x in range(170):
  if em[y,x]:
   if y<108:
    sx=45+(x*3+y//4)%22
   elif y<122:
    sx=134+(x+y)%15
   elif y<150:
    sx=136+(x*7+y*3)%32
   else:
    sx=3+(x*7+y)%24
   output.set(x,y,input_canvas.get(sx,y))
# Restore the cabinet front, leaving the original side panel and silhouette.
output.poly([(81,60),(117,53),(117,145),(81,145)],'#1e1a53')
output.line(81,61,81,143,'#16133d')
output.line(82,61,116,54,'#363469')
output.line(116,55,116,145,'#59528b')
# Lit glass display with its receding upper and lower edges.
output.poly([(84,63),(114,58),(114,101),(84,106)],'#b591bd')
output.poly([(86,64),(112,60),(112,99),(86,104)],'#b6d8d9')
for y in range(63,104):
 for x in range(86,113):
  top=64-(x-86)//6
  if top<=y<=103-(x-86)//6:
   output.set(x,y,rng.choice(['#c4dce0','#d7e6df','#d7e6df','#b9d3d9']))
# Four shelves, three drinks each. Small clustered highlights keep original pixel scale.
for row in range(4):
 for col in range(3):
  x=88+col*8; y=65+row*10-col
  cols=[('#4c9fa0','#94ddc9'),('#5a61aa','#9ea8e0'),('#46818f','#8fd2dd')]
  dark,light=cols[(col+row)%3]
  output.rect(x+1,y,3,1,'#eef3dd')
  output.rect(x+1,y+1,3,2,dark)
  output.rect(x,y+3,5,5,dark)
  output.line(x+1,y+3,x+1,y+6,light)
  output.rect(x,y+5,5,2,'#c2dcd3')
  output.set(x+4,y+7,'#34576c')
 for x in range(86,113):
  sy=73+row*10-(x-86)//7
  output.set(x,sy,'#57677f'); output.set(x,sy+1,'#8fa2b1')
output.line(85,64,85,104,'#e2e8e2')
output.line(113,60,113,100,'#8884b1')
# Lower service panel and payment controls.
output.poly([(84,108),(113,103),(113,141),(84,141)],'#25205a')
output.line(84,108,111,104,'#3c3774')
output.rect(105,108,8,12,'#111d32')
output.rect(106,109,6,3,'#3c7a86')
output.rect(107,110,4,1,'#9ee0ce')
output.rect(107,114,4,1,'#070f22')
output.set(107,117,'#b6c9cb'); output.set(110,117,'#739f9d')
output.poly([(87,123),(110,120),(110,131),(87,134)],'#0d162c')
output.line(88,124,109,121,'#565183')
output.poly([(89,126),(108,123),(108,128),(89,131)],'#080e20')
output.line(89,132,109,129,'#48476a')
for x in range(87,101,3): output.line(x,137,x,139,'#121b36')
output.line(83,143,115,143,'#373063')
output.rect(83,145,5,5,'#11192b')
output.rect(111,145,5,5,'#11192b')
# Cool the whole scene with a restrained storm-night grade.
pal={p['index']:p['rgba'] for p in output.palette()}
remap={}
for idx,rgba in pal.items():
 r,g,b,a=rgba
 remap[idx]=output.color((int(r*.80),int(g*.87),min(255,int(b*.94+5)),a))
for y in range(170):
 for x in range(170): output.set(x,y,remap[output.get(x,y)])
# Branching lightning, embedded in the existing cloud bands.
light=new_canvas(170,170,name='lightning')
bolts=[[(65,0),(61,9),(65,15),(57,25),(62,25),(53,38),(56,38),(49,51),(51,45),(51,41)],[(57,25),(49,23),(46,29),(42,32)],[(61,9),(70,15),(72,22),(78,27)],[(150,0),(146,7),(151,12),(142,21),(146,21),(139,32)],[(146,7),(138,10),(134,16)]]
for pts in bolts:
 for a,b in zip(pts,pts[1:]):
  for ox,oy in [(-1,0),(1,0),(0,-1),(0,1)]: light.line(a[0]+ox,max(0,a[1]+oy),b[0]+ox,max(0,b[1]+oy),'#89a9ec35')
for pts in bolts:
 for a,b in zip(pts,pts[1:]): light.line(*a,*b,'#c4d5f6cc')
for pts in [bolts[0],bolts[3]]:
 for a,b in zip(pts,pts[1:]): light.line(*a,*b,'#e5f6ffed')
output=flatten([output,light],name='storm_scene')
# Low puddles retain the road's texture; cold reflections below the machine.
water=new_canvas(170,170,name='standing_water')
water.poly([(37,151),(59,147),(83,151),(111,151),(125,157),(119,165),(97,167),(66,164),(46,164),(32,160)],'#315c7a5c')
water.poly([(2,139),(16,136),(26,138),(29,142),(16,145),(3,144)],'#38627765')
water.poly([(135,139),(150,136),(166,139),(169,146),(153,148),(136,145)],'#345e7766')
for y in range(151,170,2):
 for j in range(3):
  x=84+j*9+rng.randint(-5,4); length=rng.randint(3,10)
  water.line(x,y,min(125,x+length),y,rng.choice(['#a7cedc70','#8596c276','#739db769','#bce8d561']))
for x,y,w in [(3,141,17),(9,144,12),(37,157,17),(42,161,21),(65,165,11),(133,142,13),(149,146,15),(119,159,18)]:
 water.line(x,y,x+w,y,'#7faac16b')
# Broken lightning reflection in the left puddle.
for x,y,w in [(55,150,3),(52,152,6),(53,154,4),(48,157,8),(49,160,4),(45,163,8)]: water.line(x,y,x+w,y,'#b0c5e18a')
output=flatten([output,water],name='wet_scene')
# Rain is genuinely translucent, composited over the varying scene colours.
rain=new_canvas(170,170,name='translucent_rain')
for i in range(270):
 x=rng.randrange(3,169); y=rng.randrange(0,166)
 length=rng.choices([2,3,4,6,8],[5,5,4,2,1])[0]
 length=min(length,169-y)
 alpha=rng.choice([42,55,66,80,96])
 rain.line(x,y,x-max(1,length//3),y+length,(151,194,222,alpha))
 if i%8==0 and y+length<169:
  rain.set(x-max(1,length//3),y+length,(196,226,241,130))
# Larger foreground drops have a faint body and a sharply lit lower bead.
for x,y in [(17,30),(46,63),(66,101),(145,62),(154,112),(22,97),(137,23),(7,64),(62,18),(119,35),(34,156),(128,129)]:
 rain.line(x,y,x-2,y+6,'#b4d6e773')
 rain.line(x-1,y+4,x-2,y+7,'#c5e8f594')
 rain.set(x-2,y+8,'#e1f6ffb0')
output=flatten([output,rain],name='rain_scene')
# Clinging beads, roof runoff, and splashes on the saturated ground.
beads=new_canvas(170,170,name='water_beads')
for x,y in [(85,58),(94,56),(105,54),(115,53),(121,57),(128,60),(131,78),(131,99),(131,122),(116,88),(116,117),(82,111),(35,84),(35,104),(35,129)]:
 beads.set(x,y,'#86bfd298'); beads.set(x,y+1,'#c5e8e9c0')
 if x in (94,121,131): beads.line(x,y+2,x,y+4,'#70abc06b')
for i in range(80):
 x=rng.randrange(2,168); y=rng.randrange(128,169)
 if 80<x<133 and y<151: continue
 beads.set(x,y,'#92bed4a0')
 beads.set(x+1,y,'#577b96a0')
 if i%3==0: beads.set(x,y-1,'#d0e8efb4')
# Restrained elliptical ripple fragments and tiny crown splashes.
for x,y,rx in [(14,140,4),(47,155,5),(68,160,4),(97,155,5),(130,162,5),(151,144,4),(158,158,5),(25,152,3),(59,137,3)]:
 beads.line(x-rx+1,y+1,x+rx-1,y+1,'#81afc280')
 beads.set(x-rx,y,'#a4d2dd93'); beads.set(x+rx,y,'#a4d2dd93')
 beads.line(x-2,y-2,x-1,y-1,'#b8dce6aa'); beads.set(x+2,y-2,'#b8dce6aa')
result=flatten([output,beads],name='output_thunderstorm')
print(result.stats_text())
print(result.matrix_text(region=(81,103,117,143)))
save('thunderstorm',result)
finish(result)
