output = input_canvas.copy(name='output')
pal = {p['index']: p['rgba'] for p in input_canvas.palette()}
# Locate solid ridgelines so twilight haze speckles can become clear sky.
ridge=[]
for x in range(250):
 ridge.append(next((y for y in range(60,140) if all(input_canvas.get(x,yy)-1>70 for yy in range(y,y+4))),140))
for y in range(147):
 for x in range(250):
  idx=input_canvas.get(x,y)
  i=idx-1
  r,g,b,a=pal[idx]
  if i<=70 or y<ridge[x]:
   t=min(1,(y//12)*12/108)
   color=(round(91+48*t),round(184+27*t),round(229+11*t))
  elif i<170:
   t=max(0,min(1,(r-44)/168))
   color=(round(57+133*t),round(87+115*t),round(106+83*t))
  else:
   t=max(0,min(1,(r-20)/96))
   # Distinguish cool shaded foliage from the warmer, lit needle clusters.
   warm=max(0,min(1,(r-b-12)/50))
   color=(round(22+64*t+17*warm),round(53+75*t+13*warm),round(39+35*t-16*warm))
  output.set(x,y,color)
view(output)
finish(output)
