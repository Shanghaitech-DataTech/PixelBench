import random, math
random.seed(9)
result=input_canvas.copy(name='Demon King castle')
pal={p['index']:p['rgba'] for p in input_canvas.palette()}
# Retain the original intricate pixel clusters in a nightmarish palette.
for y in range(128):
 for x in range(256):
  r,g,b,a=pal[input_canvas.get(x,y)]
  v=(r+g+b)/3
  if r>g*1.08 and r>b*1.08:
   col=(int(v*.65),int(v*.29),int(v*.36),255)
  elif v<16: col=(9,7,17,255)
  else:
   t=max(0,min(1,(v-20)/220))
   stops=[(13,12,27),(36,25,49),(74,36,65),(132,47,74),(204,79,97),(245,142,133)]
   u=t*5;i=min(4,int(u));f=u-i
   col=tuple(int(stops[i][k]*(1-f)+stops[i+1][k]*f) for k in range(3))+(255,)
  result.set(x,y,col)
# Blood moon replaces the original cold disc, leaving its halo and orbit.
result.circle(128,21,16,'#69263e')
result.circle(128,21,14,'#d64749')
result.circle(127,20,12,'#f46b57')
for y in range(8,35):
 for x in range(114,142):
  d=(x-128)**2+(y-21)**2
  if d<169:
   n=math.sin(x*.61+y*.31)+math.sin(y*.87-x*.25)
   if n>1.0 and random.random()<.8:result.set(x,y,'#cf4146')
   elif n<-.9 and random.random()<.7:result.set(x,y,'#ff9170')
   if x>135 and random.random()<.6:result.set(x,y,'#b93243')
# Demonic architecture grafted onto the original castle.
dark='#150f22'; stone='#362033'; edge='#83404c'; hot='#ff744d'; red='#d63740'
def tower(x,base,top,w):
 result.poly([(x-w,base),(x-w,top+8),(x,top),(x+w,top+8),(x+w,base)],dark)
 result.rect(x-w+1,top+9,w*2-1,base-top-9,stone)
 result.line(x-w+1,top+9,x-w+1,base,edge)
 result.poly([(x-w-2,top+10),(x,top-7),(x+w+2,top+10)],dark)
 result.line(x,top-7,x+w+2,top+10,'#693143')
 for yy in range(top+14,base-2,8):
  result.line(x,yy,x,yy+3,red);result.set(x,yy+1,hot)
 for yy in range(top+12,base,5):
  result.line(x-w+2,yy,x-w+3,yy,'#583044')
 # outward curved horns framing the roof
 result.poly([(x-w,top+7),(x-w-5,top+3),(x-w-6,top-5),(x-w-3,top),(x-1,top+5)],dark)
 result.poly([(x+w,top+7),(x+w+5,top+3),(x+w+6,top-5),(x+w+3,top),(x+1,top+5)],dark)
tower(112,96,73,4)
tower(151,96,69,5)
tower(135,82,53,4)
# The high black crown.
result.poly([(123,60),(124,46),(126,42),(128,28),(130,43),(132,46),(132,60)],dark)
result.line(128,35,128,52,'#803344')
result.line(127,47,127,51,hot)
result.poly([(124,47),(120,43),(119,35),(122,40),(126,43)],dark)
result.poly([(131,47),(136,42),(138,34),(134,39),(130,43)],dark)
# Great gate and jagged battlements on the existing foundation.
result.rect(121,91,23,14,stone)
result.line(121,91,144,91,edge)
for x in range(120,145,4):
 result.rect(x,88,2,4,dark)
result.poly([(127,105),(127,96),(131,92),(135,96),(135,105)],'#a12b3b')
result.poly([(129,105),(129,97),(131,94),(133,97),(133,105)],'#ff663f')
result.line(131,97,131,105,'#391529')
# Lava light runs down the original winding approach.
for y in range(106,128):
 for x in range(105,157):
  r,g,b,a=pal[input_canvas.get(x,y)]
  if r>g*1.08 and r>b*1.1 and r>115:
   result.set(x,y, '#f96142' if (x+y)%4 else '#ffb16a')
# Tiny infernal windows on the old walls.
for x,y in [(122,69),(127,63),(121,81),(137,85),(144,88),(106,93),(155,89),(117,87),(130,77)]:
 result.line(x,y,x,y+2,red);result.set(x,y,hot)
# Bats silhouetted against the storm.
for x,y in [(90,38),(172,30),(183,49),(70,60),(155,15)]:
 result.line(x-4,y-2,x-2,y,dark);result.line(x-2,y,x,y-1,dark)
 result.line(x,y-1,x+2,y,dark);result.line(x+2,y,x+4,y-2,dark);result.set(x,y+1,dark)
view(result)
finish(result)
