import math, random
random.seed(8)
out=input_canvas.copy(name='output')
pal=input_canvas.palette()
# Remap the original illustration, preserving its intricate hand-pixelled textures.
colors={}
for p in pal:
 r,g,b,a=p['rgba']; i=p['index']
 if a==0: continue
 lum=(r*.23+g*.55+b*.22)/255
 if i==6: col=(10,7,16)
 elif b>r*1.12 and b>g*1.05:
  col=(int(15+109*lum),int(10+37*lum),int(20+50*lum))
 elif max(r,g,b)-min(r,g,b)<35 and lum>.7:
  col=(int(80+105*lum),int(25+52*lum),int(35+49*lum))
 else:
  col=(int(17+145*lum),int(9+56*lum),int(16+50*lum))
 colors[i]=col
for y in range(128):
 for x in range(256):
  idx=input_canvas.get(x,y)
  r,g,b=colors[idx]
  # The original luminous disc becomes a deep red blood moon, retaining its silhouette and spire.
  if (x-128)**2+(y-21)**2 < 15**2 and y<35:
   pr,pg,pb,pa=pal[idx]['rgba']
   l=(pr+pg+pb)/765
   if l>.52: r,g,b=(int(140+95*l),int(20+35*l),int(32+35*l))
  out.set(x,y,(r,g,b))
# Black iron horns and spikes rising from the keep, with narrow red edge light.
dark='#170d1a'; mid='#3d1727'; edge='#8d3540'; glow='#eb674d'
out.poly([(104,87),(105,69),(102,61),(99,57),(100,66),(99,71),(98,84)],dark)
out.line(103,68,101,61,edge)
out.poly([(151,87),(150,68),(153,60),(157,55),(155,66),(157,73),(158,86)],dark)
out.line(152,68,155,61,edge)
# battlement teeth punctuate the castle silhouette
for x,y,h in [(89,91,8),(95,88,7),(110,83,9),(116,78,7),(138,80,9),(145,84,7),(162,91,8)]:
 out.poly([(x-2,y),(x,y-h),(x+2,y)],dark)
 out.set(x,y-h,edge)
# Gothic windows, burning with infernal light
for x,y in [(111,92),(119,87),(137,87),(146,93),(102,99),(153,100),(128,77)]:
 out.rect(x-1,y,3,5,dark)
 out.set(x,y,glow); out.rect(x,y+1,1,3,'#b02f32')
# A pair of ragged pennants on the central spire
out.line(128,28,128,43,dark)
out.poly([(129,32),(139,34),(135,37),(130,37)],'#6d1423')
out.line(130,33,136,34,'#b72f35')
# small ember sparks across lower sky
for x,y in [(38,67),(48,79),(59,61),(75,80),(83,57),(168,66),(176,79),(188,59),(205,76),(221,64),(231,88),(28,91),(195,96),(74,100)]:
 out.set(x,y,'#b94a45')
 if x%3==0: out.set(x,y-1,'#e7825b')
view(out)
finish(out)
