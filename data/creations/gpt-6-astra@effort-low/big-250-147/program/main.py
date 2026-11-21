result = input_canvas.copy(name='output')
pal = {p['index']:p['rgba'] for p in input_canvas.palette()}
for y in range(147):
 for x in range(250):
  idx=input_canvas.get(x,y); n=idx-1
  r,g,b,a=pal[idx]
  if n<=70:
   # Clear atmospheric blue, growing paler near the horizon.
   t=min(y,104)/104
   col=(round(65+58*t),round(158+42*t),round(222+16*t))
  elif n<168:
   # Cooler shaded rock and natural warm stone on exposed facets.
   warm=max(0,min(1,(r-b-16)/65))
   v=(r-44)/168
   cool=(int(60+106*v),int(91+107*v),int(115+98*v))
   stone=(int(115+105*v),int(123+88*v),int(112+64*v))
   col=tuple(round(cool[k]*(1-warm)+stone[k]*warm) for k in range(3))
  else:
   v=max(0,(r-20)/96)
   col=(round(24+96*v),round(57+103*v),round(35+53*v))
  result.set(x,y,col)
# Remove the old sunset's isolated atmospheric dither above the ridgeline.
for x in range(250):
 ridge=110
 for y in range(60,110):
  if all(input_canvas.get(x,yy)-1>=71 for yy in range(y,y+4)):
   ridge=y
   break
 for y in range(ridge):
  t=min(y,104)/104
  result.set(x,y,(round(65+58*t),round(158+42*t),round(222+16*t)))
view(result)
finish(result)
