result = new_canvas(32,32,background='#71352d',name='carpet')
# Symmetric woven ground, including matching outermost rows and columns.
for y in range(32):
 for x in range(32):
  u=min(x,31-x); v=min(y,31-y)
  result.set(x,y,['#71352d','#793b30'][(u+v)%2])
# Double gold selvedge framing the floral band.
for k,col in [(0,'#ad693c'),(1,'#d49a57'),(7,'#b57542'),(8,'#e0af68')]:
 result.rect(k,k,32-2*k,32-2*k,col,fill=False)
# Floral rosettes along four borders, reflected around the center.
def flower(cx,cy):
 for dx,dy in [(0,-2),(-2,0),(2,0),(0,2)]:
  result.set(cx+dx,cy+dy,'#dd9a62')
 for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
  result.set(cx+dx,cy+dy,'#b95339')
 result.set(cx,cy,'#f0c981')
for p in [4,12,19,27]:
 flower(p,4); flower(p,27)
for p in [12,19]:
 flower(4,p); flower(27,p)
# Small sage leaves separate the blossoms.
for p in [8,9,15,16,22,23]:
 result.set(p,4,'#929367');result.set(p,27,'#929367')
 result.set(4,p,'#929367');result.set(27,p,'#929367')
# Stepped, concentric lozenge. Half-pixel center keeps opposing edges identical.
for y in range(9,23):
 for x in range(9,23):
  d=abs(x-15.5)+abs(y-15.5)
  if d<=7:
   col={7:'#472f2a',6:'#e5b76e',5:'#b97140',4:'#d39851',3:'#4f6250',2:'#80916b',1:'#f0c981'}[int(d)]
   result.set(x,y,col)
# Four small palmettes in the inner-field corners.
for x,y,sx,sy in [(10,10,1,1),(21,10,-1,1),(10,21,1,-1),(21,21,-1,-1)]:
 result.set(x,y,'#d39851')
 result.set(x+sx,y,'#a05a36');result.set(x,y+sy,'#a05a36')
view(result)
preview=new_canvas(96,96,background='#71352d',name='repeat_check')
for y in range(3):
 for x in range(3): preview.blit(result,x*32,y*32)
view(preview)
assert all(result.get(0,y)==result.get(31,y) for y in range(32))
assert all(result.get(x,0)==result.get(x,31) for x in range(32))
save('seamless-carpet-pattern',result)
finish(result)
