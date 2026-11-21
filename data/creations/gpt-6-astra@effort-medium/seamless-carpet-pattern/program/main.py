result = new_canvas(32,32,background='#71382f',name='carpet')
# Symmetric coordinates keep opposite edges identical, including the weave.
for y in range(32):
 for x in range(32):
  a=min(x,31-x); b=min(y,31-y)
  col=['#71382f','#7d4033'][(a+b)%2]
  if a==0 or b==0: col='#d39959'
  elif a==1 or b==1: col='#482f2b'
  elif a==7 or b==7: col='#482f2b'
  elif a==8 or b==8: col='#d39959'
  elif a>=9 and b>=9: col=['#a34f37','#ac593b'][(a+b)%2]
  result.set(x,y,col)
# Rosettes and leaf stitches in a continuous border.
cream='#edc583'; gold='#cb8b48'; dark='#482f2b'; leaf='#8a824d'
def flower(cx,cy):
 for dx,dy in [(0,-2),(-2,0),(2,0),(0,2)]:
  result.set(cx+dx,cy+dy,gold)
 for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
  result.set(cx+dx,cy+dy,cream)
 result.set(cx,cy,'#a34f37')
for t in [4,12,19,27]:
 flower(t,4); flower(t,27)
for t in [12,19]:
 flower(4,t); flower(27,t)
for t in [8,15,16,23]:
 for q in [3,5,26,28]:
  result.set(t,q,leaf); result.set(q,t,leaf)
# Stepped medallion with nested diamonds.
for y in range(9,23):
 for x in range(9,23):
  d=abs(x-15.5)+abs(y-15.5)
  if d<=7:
   col=dark if d==7 else gold if d==6 else cream if d==5 else '#633b30' if d==4 else '#88794a' if d==3 else '#d39959' if d==2 else '#edc583'
   result.set(x,y,col)
for x,y in [(10,10),(21,10),(10,21),(21,21)]: result.set(x,y,cream)
view(result)
preview=new_canvas(96,96,name='repeat_check')
for y in range(3):
 for x in range(3): preview.blit(result,x*32,y*32)
view(preview)
save('carpet',result)
finish(result)
