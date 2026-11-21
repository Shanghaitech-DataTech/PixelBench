import numpy as np
result=input_canvas.copy(name='output')
pal={p['index']:p['rgba'] for p in input_canvas.palette()}
# Preserve the source's mountain facets, forest silhouettes and pixel texture.
for y in range(147):
 for x in range(250):
  i=input_canvas.get(x,y)
  r,g,b,a=pal[i]
  if i<=71:
   # Cloudless sky: broad, restrained bands of atmospheric blue.
   t=min(1,(y//4)*4/100)
   color=(round(75+65*t),round(167+46*t),round(224+19*t))
  elif i<=172:
   t=max(0,min(1,(r-44)/168))
   color=(round(58+139*t),round(91+119*t),round(114+96*t))
  else:
   t=max(0,min(1,(r-20)/96))
   # Deep evergreen shade and olive-green needles under overhead light.
   color=(round(24+91*t),round(61+94*t),round(43+28*t))
  result.set(x,y,color)
view(result,scale=3,margin=0)
finish(result)
