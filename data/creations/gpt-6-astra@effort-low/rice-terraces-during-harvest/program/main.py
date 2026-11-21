import math
result = new_canvas(64,64,background='#9cae91',name='harvest')
c=result
# distant wooded mountain slopes
c.poly([(0,8),(10,3),(20,6),(32,0),(45,3),(55,0),(63,4),(63,24),(0,24)],'#728d76')
c.poly([(0,14),(13,9),(26,13),(40,6),(51,9),(63,5),(63,28),(0,28)],'#536f59')
# village clearing
c.poly([(30,12),(41,9),(58,11),(63,16),(58,22),(34,23),(24,18)],'#9b9a65')
c.path('M 37 16 Q 46 17 54 23 L 60 28', '#d0bc7c',False)
# tiny houses
for x,y in [(34,11),(46,10),(54,14)]:
 c.rect(x,y+3,7,5,'#d8c394');c.rect(x+5,y+3,2,5,'#ac9a74')
 c.poly([(x-1,y+3),(x+3,y),(x+8,y+3),(x+8,y+4),(x-1,y+4)],'#655b4c')
 c.line(x,y+2,x+3,y,'#98846a');c.rect(x+3,y+5,2,3,'#635e4b')
# contour fields: distant to foreground, broad looping mountain contours
curves=[(20,5,0),(27,7,2),(35,9,4),(44,10,6),(54,11,8),(65,12,10),(77,12,12)]
# boundary curves rise at sides and dip through central valley
for i,(base,amp,phase) in enumerate(curves):
 def yy(x): return int(base + amp*math.sin((x+phase-10)*math.pi/65) + 2*math.sin((x+phase)*math.pi/32))
 pts=[(x,yy(x)) for x in range(64)]
 dirt=['#77805a','#777448','#71683b','#665b32','#534c2d','#45442b','#3a3c29'][i]
 gold=['#c6bb69','#d2bd58','#dfbd4e','#e4b747','#efbe4e','#e5ac3d','#dca03a'][i]
 c.poly(pts+[(63,64),(0,64)],dirt)
 top=[(x,y+3) for x,y in pts]
 c.poly(top+[(63,64),(0,64)],gold)
 for x,y in pts:
  if 0<=y<64:c.set(x,y,'#afac63' if i<3 else '#a09448')
 # rice clumps following curvature, kept clear of next terrace
 nextbase=curves[i+1][0] if i<6 else 100
 for x in range(1,64,3):
  y=yy(x)+5+(x//3%2)
  if y<64:
   c.set(x,y,'#f1d276' if i<4 else '#f6d171')
   if y+1<64:c.set(x,y+1,'#b18a35')
# leafy edge at upper left
for x,y,r in [(1,13,4),(6,12,3),(12,13,3),(18,15,3),(23,17,2)]:
 c.circle(x,y,r,'#4e6847');c.line(x-1,y-2,x+1,y-2,'#728352')
# two small farmers on separate winding ridges
for x,y in [(24,34),(47,51)]:
 c.line(x,y+2,x-1,y+4,'#453e2c');c.line(x+1,y+2,x+2,y+4,'#453e2c')
 c.rect(x-1,y,4,3,'#eee0ab' if x==24 else '#a65735')
 c.set(x-2,y+1,'#b68652');c.set(x+3,y+1,'#b68652')
 c.rect(x,y-2,2,2,'#b17c45')
 c.line(x-3,y-2,x+3,y-2,'#74552c')
 c.line(x-2,y-3,x+2,y-3,'#f5d17b');c.line(x-1,y-4,x+1,y-4,'#e9b85f')
 c.line(x+4,y,x+5,y+4,'#6e5830')
# tied harvested sheaves
for x,y in [(13,44),(35,52),(57,34),(7,29)]:
 c.line(x,y,x-2,y+3,'#936c2e');c.line(x,y,x+2,y+3,'#936c2e')
 c.line(x,y-2,x-1,y+2,'#f6d47b');c.line(x+1,y-2,x+1,y+2,'#f6d47b');c.line(x-1,y,x+1,y,'#8a6730')
view(c)
finish(result)
