output=input_canvas.copy(name='output')
pal={p['index']:p['rgba'] for p in input_canvas.palette()}
# Find the continuous mountain skyline, excluding atmospheric stippling.
skyline=[]
for x in range(250):
 edge=110
 for y in range(60,110):
  if all(input_canvas.get(x,yy)>=72 for yy in range(y,y+4)):
   edge=y
   break
 skyline.append(edge)
# Clear midday atmosphere; broad, gentle blue bands retain pixel-art color fields.
sky=['#56ade6','#60b4e9','#6bbded','#79c6ef','#8bcff1','#a0daf4']
for y in range(147):
 for x in range(250):
  idx=input_canvas.get(x,y)
  r,g,b,a=pal[idx]
  if y<skyline[x]:
   color=sky[min(5,y//18)]
  elif idx<=171:
   # Cool slate and blue-grey rock, lightened by clear overhead daylight.
   t=max(0,min(1,(r-44)/168))
   color=(round(57+116*t),round(94+104*t),round(117+88*t))
  else:
   # Bring the conifers out of silhouette while retaining their branch detail.
   t=max(0,min(1,(r-20)/96))
   color=(round(23+85*t),round(55+89*t),round(36+35*t))
   if idx==201: color=(29,66,40)
  output.set(x,y,color)
view(output,scale=3,margin=0)
finish(output)
