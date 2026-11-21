result = new_canvas(32,32)
c=result
edge='#65402c'; dark='#956039'; mid='#c48b4d'; gold='#e6b66d'; light='#f8d994'; inner='#795039'
# lifted lid, tilted upward on the left
c.poly([(3,10),(5,7),(21,3),(25,4),(28,7),(27,9),(10,14),(5,13)],edge)
c.poly([(4,10),(6,8),(22,4),(25,5),(26,7),(9,12),(5,12)],gold)
c.line(6,9,22,5,light)
c.line(8,11,25,6,mid)
c.line(10,12,26,8,dark)
# bamboo slats on lid
for x,y in [(10,8),(14,7),(18,6),(22,5)]:
 c.line(x,y,x+2,y+2,mid)
# handle
c.poly([(13,6),(13,3),(15,2),(18,2),(20,4),(17,5),(17,4),(15,4),(15,6)],edge)
c.line(14,3,17,3,gold)
# basket body
c.rect(3,20,26,6,edge)
c.ellipse(16,25,12,5,edge)
c.rect(4,21,24,5,mid)
c.ellipse(16,25,11,4,mid)
c.ellipse(16,24,11,3,gold)
c.rect(5,21,22,4,gold)
# vertical woven divisions
for x in [6,10,15,20,25]:
 c.line(x,23,x,27,mid)
c.line(8,28,23,28,dark)
c.line(9,29,22,29,gold)
# interior and rim
c.ellipse(16,20,13,5,edge)
c.ellipse(16,19,12,5,gold)
c.ellipse(16,19,10,4,inner)
c.line(7,17,11,15,light)
# three dumplings, rear one and two foreground
cream='#fff0c7'; shade='#d7b77e'; white='#fff9e3'; crease='#bb9464'
def dumpling(x,y):
 c.poly([(x-4,y+2),(x-4,y),(x-2,y-3),(x,y-4),(x+2,y-3),(x+4,y),(x+4,y+2),(x+2,y+3),(x-2,y+3)],shade)
 c.poly([(x-3,y+1),(x-3,y-1),(x,y-4),(x+2,y-2),(x+3,y+1),(x+2,y+2),(x-2,y+2)],cream)
 c.line(x,y-3,x-2,y,crease)
 c.line(x+1,y-2,x+2,y,shade)
 c.set(x,y-2,white)
 c.line(x-2,y+1,x+1,y+1,white)
dumpling(16,16)
dumpling(10,20)
dumpling(22,20)
# front lip arcs keep food nestled
c.path('M 3 20 Q 4 25 16 25 Q 28 25 29 20',edge,fill=False)
c.path('M 4 21 Q 7 24 16 24 Q 25 24 28 21',light,fill=False)
# light steam above uncovered side
steam='#d8e7df'
c.line(23,13,24,12,steam)
c.line(24,12,24,10,steam)
c.set(23,9,steam)
c.line(28,15,29,14,steam)
c.line(29,13,28,12,steam)
view(result)
finish(result)
