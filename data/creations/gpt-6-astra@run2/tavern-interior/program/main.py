c = new_canvas(64,64,background='#1c1720',name='tavern')
# palette: plum shadows, walnut wood, honey light
ink='#19151c'; deep='#302029'; wood='#633b32'; mid='#895039'; light='#bb7947'; gold='#e4ac59'; cream='#ffe39a'
# back wall and side posts
c.rect(3,5,58,37,'#422b2c')
c.rect(8,8,47,26,'#50332f')
# wall boards
for x in [10,19,28,37,46,55]:
 c.line(x,8,x,33,'#3b272b')
 c.line(x+1,9,x+1,31,'#5c3a31')
# lamp glow, restrained concentric warm patches
for x in [14,47]:
 c.ellipse(x,18,10,13,'#57392e')
 c.ellipse(x,17,7,10,'#65432f')
 c.ellipse(x,16,5,7,'#795335')
# ceiling beams
c.rect(0,0,64,5,ink); c.rect(1,1,62,2,'#6c4536')
c.rect(2,4,5,37,ink); c.rect(3,4,3,35,'#704334');c.line(4,6,4,36,'#9a613e')
c.rect(58,4,5,39,ink); c.rect(59,4,3,37,'#613d32');c.line(59,7,59,37,'#94603d')
# bottle shelves, dark recess
c.rect(21,8,34,23,ink); c.rect(23,9,30,20,'#2f2529')
c.rect(23,10,30,1,'#58372f')
# bottles
def bottle(x,y,col,hi,h=7):
 c.rect(x+1,y,2,2,ink); c.rect(x+1,y,1,2,hi)
 c.rect(x,y+2,4,h-2,ink); c.rect(x+1,y+2,2,h-3,col)
 c.set(x+1,y+2,hi); c.rect(x+1,y+4,2,1,'#b7a16b')
for x,y,col,hi in [(24,11,'#427262','#87a579'),(30,10,'#98503d','#d58b53'),(36,11,'#547c72','#9eac86'),(44,10,'#795044','#b78658'),(49,11,'#4e7055','#a2a56e')]: bottle(x,y,col,hi)
c.rect(21,17,34,3,ink);c.rect(21,17,34,1,'#bc8050');c.rect(22,18,32,1,'#79503a')
for x,y,col,hi in [(24,22,'#99643d','#d4a45b'),(29,21,'#527766','#8cae7a'),(35,22,'#8d3e3a','#c16c50'),(41,21,'#4d7270','#8bab91'),(49,22,'#74633d','#b6a563')]: bottle(x,y,col,hi)
c.rect(21,28,35,3,ink);c.rect(21,28,35,1,'#bb7b47');c.rect(23,29,31,1,'#6e4233')
# little chalk menu on left
c.rect(8,21,10,11,ink); c.rect(9,22,8,9,'#9c6741'); c.rect(10,23,6,7,'#303330')
c.line(11,24,14,24,'#c5bc8d');c.line(11,26,13,26,'#8f9879');c.line(11,28,14,28,'#8f9879')
# floor
c.poly([(0,42),(63,42),(63,63),(0,63)],'#4e3030')
for y in [46,52,59]: c.line(0,y,63,y,'#2b2027'); c.line(0,y+1,63,y+1,'#734337')
for x,y in [(6,43),(33,43),(53,47),(17,47),(40,53),(7,53),(24,60),(56,60)]: c.line(x,y,x-2,min(y+5,63),'#302129')
for x,y,w in [(2,49,7),(23,49,9),(45,56,10),(13,57,7),(34,62,10),(54,44,6)]: c.line(x,y,x+w,y,'#81503b')
# bar silhouette and warm top
c.rect(6,34,50,14,ink)
c.rect(8,38,46,8,'#6f4032')
c.rect(10,39,12,6,'#42292a');c.rect(24,39,13,6,'#42292a');c.rect(39,39,13,6,'#42292a')
for x,w in [(11,10),(25,11),(40,11)]:
 c.rect(x,40,w,4,'#925236');c.line(x,40,x+w-1,40,'#b27543');c.line(x+w-1,41,x+w-1,43,'#5d3530')
c.rect(8,45,46,2,'#a2693e');c.rect(7,47,48,2,ink)
c.poly([(7,32),(53,32),(57,35),(5,35)],ink)
c.poly([(8,32),(52,32),(55,34),(6,34)],'#bf834b')
c.line(8,33,51,33,'#dfa25b');c.rect(5,35,52,2,'#6f4232');c.line(6,35,55,35,'#f0b96b')
# drinks on counter
bottle(37,27,'#416951','#89a16b',6)
def mug(x,y):
 c.rect(x+4,y+1,2,3,ink);c.rect(x+4,y+1,1,2,'#dbba79')
 c.rect(x,y,4,6,ink);c.rect(x+1,y+1,2,4,'#b97936');c.line(x+1,y+1,x+1,y+3,'#ffe2a0');c.rect(x,y,4,1,'#f8e4b1')
mug(14,28);mug(44,29)
c.line(27,29,27,32,'#cebe96');c.line(26,32,28,32,'#e8c58b');c.rect(25,27,5,2,ink);c.line(26,28,28,28,'#e5cc97');c.line(26,27,28,27,'#ac785c')
# barrel at left, dark hoops and curved wooden staves
def barrel(x,y):
 c.ellipse(x+5,y+6,6,8,ink)
 c.rect(x,y+2,11,10,wood)
 c.ellipse(x+5,y+6,5,7,'#93603b')
 c.line(x+3,y+1,x+2,y+11,'#d3954f');c.line(x+7,y+1,x+8,y+12,'#55352b');c.line(x+5,y+2,x+5,y+12,'#6b4030')
 c.rect(x,y+3,11,2,'#393538');c.line(x+1,y+3,x+9,y+3,'#777269')
 c.rect(x,y+10,11,2,'#393538');c.line(x+1,y+10,x+9,y+10,'#777269')
 c.ellipse(x+5,y,5,2,ink);c.ellipse(x+5,y,4,1,'#b9834c');c.line(x+2,y,x+7,y,'#79503a')
 c.set(x+2,y+4,'#b0a17c');c.set(x+2,y+11,'#b0a17c')
barrel(1,42)
barrel(52,44)
# three bar stools with angled legs and cushioned wooden seats
for x,y in [(19,48),(34,50),(47,48)]:
 c.ellipse(x,y+10,6,2,'#302128')
 c.line(x-3,y+2,x-4,y+10,ink);c.line(x+3,y+2,x+4,y+10,ink)
 c.line(x-2,y+2,x-3,y+9,'#b17a46');c.line(x+2,y+2,x+3,y+9,'#7f4e35')
 c.line(x-3,y+7,x+3,y+7,ink);c.line(x-2,y+6,x+2,y+6,'#bd874b')
 c.ellipse(x,y,6,3,ink);c.ellipse(x,y-1,5,2,'#a16339');c.line(x-3,y-2,x+3,y-2,'#e0a45b');c.line(x-3,y+1,x+3,y+1,'#65382d')
# hanging lanterns, bright yellow panes
for x,y in [(14,12),(47,8)]:
 c.line(x,4,x,y-2,ink);c.set(x+1,5,'#a27a50')
 c.rect(x-2,y-2,5,2,ink)
 c.poly([(x-3,y),(x+3,y),(x+4,y+6),(x-4,y+6)],ink)
 c.rect(x-2,y,5,5,'#eeb755');c.rect(x-1,y+1,3,4,'#ffe7a0');c.line(x,y,x,y+4,'#fff1bd')
 c.line(x-3,y+5,x+3,y+5,'#9e6437');c.line(x-4,y+6,x+4,y+6,ink);c.set(x,y+7,'#b87e43')
# drifting smoke, muted small stepped clusters
c.path('M 6 19 Q 7 16 10 17 Q 14 19 17 16 Q 19 14 23 15', '#8b705142',fill=False)
c.path('M 31 6 Q 34 4 38 6 Q 41 9 44 7', '#b6a17b28',fill=False)
# composite smoke transparency against scene
# replace partial alpha marks by compositing a separate accurate haze layer below
# final output is opaque via flatten
result = flatten([new_canvas(64,64,background='#50352e',name='underpaint'),c],name='tavern-interior')
# faint warm haze curling through the open space above the bar
result.path('M 17 26 Q 14 24 17 22 Q 20 20 18 18', '#8a6547', fill=False)
result.set(17,25,'#a27a50')
# Consolidate near-identical shades to keep the small scene palette economical.
from collections import Counter
w,h,raw = result.to_rgba()
pixels = [tuple(raw[i:i+4]) for i in range(0,len(raw),4)]
counts = Counter(pixels)
parent = {p:p for p in counts}
while len(counts)>80:
 colors=list(counts)
 a,b=min(((a,b) for i,a in enumerate(colors) for b in colors[i+1:]), key=lambda pair: sum((pair[0][k]-pair[1][k])**2 for k in range(3)))
 if counts[a]>counts[b]: a,b=b,a
 for p in parent:
  if parent[p]==a: parent[p]=b
 counts[b]+=counts.pop(a)
for y in range(h):
 for x in range(w): result.set(x,y,parent[pixels[y*w+x]])
view(result)
finish(result)
