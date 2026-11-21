import random
random.seed(8)
result=input_canvas.copy(name='output')
pal={p['index']:p['rgba'] for p in input_canvas.palette()}
# Retain the original pixel clusters and lighting, with a haunted crimson palette.
for y in range(128):
 for x in range(256):
  r,g,b,a=pal[input_canvas.get(x,y)]
  l=(r+g+b)/3
  if max(r,g,b)<8: col=(9,6,17)
  elif r>g*1.08 and r>b*1.1:
   col=(int(r*.65),int(g*.40),int(b*.48))
  elif g>r*1.5 and g>b*.98: col=(int(g*.72),int(g*.19),int(b*.24))
  else:
   col=(int(15+l*.68),int(7+l*.23),int(21+l*.43))
  result.set(x,y,col)
# Moon: retain its original silhouette and glowing rim, add irregular seas.
for y in range(4,39):
 for x in range(110,146):
  d=((x-128)**2+(y-21)**2)**.5
  if d<=16:
   if d>15: col='#8d293f'
   elif d>14: col='#d3474e'
   else:
    v=random.random()
    col='#ee6757' if v>.15 else '#dc504e'
    if (x-135)**2/32+(y-23)**2/56<1 or (x-124)**2/23+(y-29)**2/12<1 or (x-126)**2/40+(y-13)**2/8<1:
     col='#b83b48' if v>.25 else '#d95050'
   result.set(x,y,col)
result.path('M 115 20 Q 115 11 125 8', '#ff9270',fill=False)
# Obsidian turrets with red-lit stone edges.
def tower(x,y,w,h):
 result.rect(x,y,w,h,'#211322')
 result.rect(x+1,y,1,h,'#7e3b48')
 result.line(x,y+h-1,x+w-1,y+h-1,'#492435')
 result.poly([(x-2,y),(x+w//2,y-12),(x+w+1,y)],'#140f20')
 result.line(x-2,y,x+w//2,y-12,'#9c4751')
 result.rect(x-1,y,w+2,2,'#512b3c')
 for yy in range(y+4,y+h-2,7):
  result.rect(x+w//2,yy,1,3,'#ef6145')
  result.set(x+w//2,yy,'#ffb06a')
 for yy in range(y+3,y+h-1,4):
  result.line(x+1,yy,x+2,yy,'#49283a')
tower(100,89,6,17)
tower(153,83,7,27)
tower(116,77,6,20)
tower(138,69,6,27)
# Crown horns clasp the narrow central spire.
result.poly([(125,66),(119,58),(118,48),(122,55),(127,58),(129,48),(131,58),(136,54),(139,45),(138,59),(132,66)],'#1b1021')
result.path('M 125 65 L 120 58 L 118 48 M 132 65 L 137 58 L 139 45','#9a4550',fill=False)
result.line(128,47,128,29,'#251425')
result.set(128,29,'#ff925d')
# Demonic eyes in the crown.
result.line(124,60,126,61,'#ff8b50')
result.line(131,61,133,60,'#ff8b50')
# Lava-lit gate and arrow slit windows integrated into the fortress.
result.poly([(126,112),(126,104),(129,100),(132,104),(132,112)],'#130e1a')
result.path('M 125 112 L 125 104 L 129 99 L 133 104 L 133 112','#a44443',fill=False)
result.line(129,104,129,111,'#f36a42')
for x,y in [(110,98),(117,100),(140,101),(146,98),(151,105),(123,85),(133,78),(128,72),(136,91)]:
 result.rect(x,y,1,3,'#ff784c')
# The original winding approach becomes a river of embers.
for y in range(114,128):
 for x in range(114,155):
  r,g,b,a=pal[input_canvas.get(x,y)]
  if r>g*1.08 and r>100:
   result.set(x,y,'#ed633f' if (x+y)%3 else '#ffae61')
# Tattered pennants.
for x,y in [(103,76),(156,69),(142,55)]:
 result.line(x,y,x,y-7,'#271321')
 result.poly([(x+1,y-7),(x+9,y-5),(x+5,y-3),(x+8,y-2),(x+1,y-3)],'#aa3445')
# Small bat silhouettes against the lit cloud bands.
for x,y in [(82,51),(170,40),(190,64),(63,76),(164,27)]:
 result.poly([(x-5,y-2),(x-3,y-3),(x,y),(x+3,y-3),(x+5,y-2),(x+2,y-1),(x,y+2),(x-2,y-1)],'#170e20')
view(result)
finish(result)
