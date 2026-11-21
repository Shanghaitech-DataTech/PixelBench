import math
result = new_canvas(48,48, name='teleport_portal')
# Concentric, stepped aura surrounding a spiralling energy aperture.
cx,cy=23.5,23.5
for y in range(48):
 for x in range(48):
  dx,dy=x-cx,y-cy
  r=math.hypot(dx,dy)
  a=math.atan2(dy,dx)
  col=None
  if r<17.5:
   phase=(a-0.30*r+0.8)%(2*math.pi/3)
   if phase<0.19: col='#f9deff'
   elif phase<0.39: col='#d596ff'
   elif phase<0.67: col='#9b50e8'
   elif phase<1.02: col='#6730b3'
   elif phase<1.42: col='#3e2175'
   else: col='#24183f'
   if r<3.1: col='#e5bbff' if r>1.5 else '#fff0ff'
  elif r<18.5: col='#6c32b6'
  elif r<19.6: col='#e6b3ff'
  elif r<20.6: col='#a85eed'
  elif r<21.5: col='#482469'
  elif r<22.3 and (x+y)%2==0: col='#312047'
  if col: result.set(x,y,col)
# Interrupted bright arcs make the halo feel energetic rather than mechanical.
for radius,start,end,col in [(19,192,266,'#fff0ff'),(19,12,90,'#f9deff'),(20,194,249,'#cc91ff'),(18,94,142,'#e4aeff')]:
 for deg in range(start,end):
  a=math.radians(deg)
  result.set(round(cx+radius*math.cos(a)),round(cy+radius*math.sin(a)),col)
# Four detached magical sparks, kept within the transparent canvas.
for x,y in [(7,7),(41,10),(6,38),(39,40)]:
 result.set(x,y,'#fff0ff')
 result.set(x-1,y,'#a85eed')
 result.set(x+1,y,'#a85eed')
 result.set(x,y-1,'#d596ff')
 result.set(x,y+1,'#a85eed')
# Export the first animation frame separately while keeping the required
# single submitted canvas as the second frame.
frame1 = new_canvas(48,48,name='teleport_portal_frame_1')
for y in range(48):
 for x in range(48):
  dx,dy=x-cx,y-cy
  r=math.hypot(dx,dy)
  if r<17.5:
   phase=(math.atan2(dy,dx)-0.30*r+0.8+math.pi/6)%(2*math.pi/3)
   col=('#f9deff' if phase<0.19 else '#d596ff' if phase<0.39 else '#9b50e8' if phase<0.67 else '#6730b3' if phase<1.02 else '#3e2175' if phase<1.42 else '#24183f')
   if r<3.1: col='#e5bbff' if r>1.5 else '#fff0ff'
   frame1.set(x,y,col)
  elif r<18.5: frame1.set(x,y,'#6c32b6')
  elif r<19.6: frame1.set(x,y,'#482469')
save('teleport_portal_frame_1',frame1)
view(result)
save('teleport_portal_frame_2',result)
finish(result)
