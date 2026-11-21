import math, random
random.seed(9)
result = new_canvas(64,64,background='#86968a',name='harvest')
c=result
# distant slopes
c.poly([(0,0),(64,0),(64,18),(51,13),(40,14),(26,7),(13,10),(0,6)],'#738b7e')
c.poly([(0,9),(12,5),(26,8),(38,16),(64,14),(64,32),(0,26)],'#566f60')
c.poly([(0,14),(15,10),(26,13),(34,20),(50,18),(64,23),(64,38),(0,36)],'#657c55')
# distant contour strips
c.path('M 0 15 Q 15 9 27 16 T 64 22 L 64 25 Q 42 23 30 21 T 0 18 Z','#969b58')
c.path('M 0 21 Q 13 15 25 21 T 64 28 L 64 30 Q 43 29 26 24 T 0 24 Z','#acaa60')
# village in the distance
for x,y in [(39,10),(47,12),(55,11)]:
 c.rect(x,y+2,6,4,'#454f42')
 c.rect(x,y+2,5,3,'#c6bc8c')
 c.poly([(x-1,y+2),(x+2,y-1),(x+6,y+1),(x+6,y+3),(x+2,y+1)],'#684e3e')
 c.line(x-1,y+2,x+2,y-1,'#997452')
 c.rect(x+2,y+3,1,2,'#625b48')
# foreground terraced hillside: nested contours as broad horizontal ribbons
# terrace boundaries sweep around the mountain's shoulder
bounds=[]
for base in [24,32,41,51,62,74]:
 arr=[]
 for x in range(64):
  y=round(base + 4.5*math.sin((x-8)/15) - 0.11*x)
  arr.append(y)
 bounds.append(arr)
# successive fields follow continuous ridges
for i in range(5):
 top,bot=bounds[i],bounds[i+1]
 field=['#c2ad53','#d7b84f','#e2bc4d','#e8c251','#f1cb60'][i]
 for x in range(64):
  for y in range(max(0,top[x]),min(64,bot[x])):
   dy=y-top[x]
   color= '#4f613b' if dy==0 else '#758044' if dy==1 else '#a18d39' if dy==2 else field
   c.set(x,y,color)
  # bright embankment lip
  if 0<=top[x]-1<64: c.set(x,top[x]-1,'#f5d77d')
 # rice stalks grouped in contour aligned patches
 for x in range(1,63):
  for y in range(max(0,top[x]+4),min(64,bot[x]-1)):
   if random.random()<0.20:
    c.set(x,y,['#a58b32','#b19332','#bd9632','#c39d39','#c49d3b'][i])
    if y>top[x]+4: c.set(x,y-1,'#f5d77d')
# narrow winding connector ridge at right
c.path('M 60 22 L 56 26 L 56 30 L 51 34 L 51 38 L 46 43 L 46 47 L 40 54 L 39 60 L 36 64 L 39 64 L 42 60 L 43 55 L 49 48 L 49 44 L 54 39 L 54 35 L 59 31 L 59 27 L 63 23 Z','#8b7a3d')
c.path('M 61 23 L 57 27 L 57 31 L 52 35 L 52 39 L 47 44 L 47 48 L 41 55 L 40 60 L 38 63','#dbbf74',fill=False)
# farmers standing on ridges; straw hats seen from above
for x,y,shirt in [(19,bounds[2][19]-1,'#446d77'),(47,bounds[1][47]-1,'#a2523b')]:
 c.ellipse(x+1,y+1,3,1,'#847338')
 c.set(x-1,y,'#3d493c');c.set(x+1,y,'#3d493c')
 c.rect(x-1,y-3,3,3,shirt)
 c.set(x-2,y-2,'#c59d69');c.set(x+2,y-2,'#c59d69')
 c.line(x+3,y-3,x+3,y+1,'#685337')
 c.ellipse(x,y-4,3,1,'#a47e3d')
 c.line(x-2,y-5,x+2,y-5,'#f6dfa0')
 c.line(x-2,y-4,x+2,y-4,'#e6c574')
 c.set(x,y-6,'#f6dfa0')
# tied harvested bundles
for x,y in [(7,34),(30,47),(56,52),(10,57)]:
 c.line(x-1,y+1,x+1,y+1,'#947830')
 c.poly([(x-2,y),(x,y-4),(x+2,y),(x+1,y+1)],'#faDA7e')
 c.line(x-1,y-1,x+1,y-1,'#9b7435')
view(result)
finish(result)
