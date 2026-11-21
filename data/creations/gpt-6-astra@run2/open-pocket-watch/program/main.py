import math
c = new_canvas(64,64,background='#0b111c',name='open_pocket_watch')
# Restrained blue-black studio backdrop.
c.ellipse(35,51,28,12,'#0d1521')
c.ellipse(35,55,24,7,'#080c13')
# The open cover, hinged behind the movement.
c.ellipse(18,18,17,15,'#03080e')
c.ellipse(18,17,17,15,'#6d3e1b')
c.ellipse(17,16,16,14,'#d89a42')
c.ellipse(17,15,15,13,'#fff0a1')
c.ellipse(18,16,14,12,'#9c642b')
c.ellipse(18,16,13,11,'#e2ae54')
c.ellipse(18,17,12,10,'#4e321d')
c.ellipse(18,16,11,9,'#a66d30')
c.ellipse(17,15,10,8,'#c69042')
c.ellipse(15,13,8,6,'#dca855')
# Brushed inset, and thin reflected light at the lip.
for x,y,l in [(10,9,9),(8,11,9),(7,13,7),(8,15,5),(12,19,10),(16,21,7)]:
    c.line(x,y,x+l,y,'#e4b964' if y<16 else '#b57e36')
c.path('M 3 17 Q 2 5 15 2 M 5 19 Q 4 24 10 27','#fff6c5',False)
c.path('M 22 5 Q 32 10 31 19 Q 30 25 24 28','#6f431f',False)
c.path('M 9 21 Q 17 28 26 21','#f4cc75',False)
# Engraved floral rosette in the lid.
c.ellipse(18,16,4,3,'#b57e36',False)
c.line(18,12,18,20,'#b57e36'); c.line(14,16,22,16,'#b57e36')
c.set(18,16,'#f4cc75')
# Chain: individually articulated links, looping out to the right.
def link(cx,cy,rx,ry,ang):
    pts=[]
    for i in range(20):
        a=2*math.pi*i/20; x=rx*math.cos(a); y=ry*math.sin(a)
        pts.append((round(cx+x*math.cos(ang)-y*math.sin(ang)),round(cy+x*math.sin(ang)+y*math.cos(ang))))
    c.poly(pts,'#9c642b',False)
    for i in range(9,17):
        c.line(*pts[i],*pts[(i+1)%20],'#f4cc75')
for p in [(45,14,3,2,-.9),(49,10,3,2,-.8),(53,6,3,2,-.6),(58,5,3,2,.3),(61,9,2,3,-.3),(60,14,2,3,.4),(57,18,3,2,-.5),(57,22,2,3,-.3)]: link(*p)
# Bow and fluted winding crown.
c.ellipse(41,17,5,5,'#bd8237',False)
c.ellipse(41,16,4,4,'#ffe6a0',False)
c.rect(38,18,7,7,'#613c21')
c.rect(38,18,7,5,'#d89a42')
for x in [39,41,43]: c.line(x,18,x,22,'#ffe6a0')
# Hinge barrel.
c.poly([(19,27),(24,24),(29,29),(23,33)],'#5b3820')
for x,y in [(20,27),(22,26),(24,27)]: c.line(x,y,x+4,y+4,'#e4b964')
# Massive polished case, with offset rings and directional reflections.
c.ellipse(35,42,23,21,'#03080e')
c.ellipse(35,41,23,21,'#6f431f')
c.ellipse(35,40,23,21,'#b57e36')
c.ellipse(34,39,22,20,'#f4cc75')
c.ellipse(35,40,21,20,'#dfaa51')
c.ellipse(35,40,20,19,'#694421')
c.ellipse(35,40,19,18,'#ffe6a0')
c.ellipse(35,40,18,17,'#302a25')
c.path('M 13 37 Q 13 25 28 20 M 18 53 Q 26 62 40 59','#fff6c5',False)
c.path('M 47 24 Q 58 31 56 43 M 50 54 L 46 57','#fff0a1',False)
c.path('M 57 44 Q 54 58 39 61','#8b5726',False)
# Dark skeleton movement bed, flecks of machined gold plate.
c.ellipse(35,40,16,15,'#533e25')
c.poly([(24,29),(34,26),(45,29),(48,35),(40,39),(37,49),(29,52),(22,46)],'#8b652f')
c.poly([(25,32),(33,28),(40,31),(35,37),(28,41),(22,39)],'#bd934b')
c.poly([(34,42),(48,36),(49,46),(41,53),(34,51)],'#a77c39')
# Perimeter dial index ring, minute and hour batons.
for i in range(60):
    a=i*math.pi/30-math.pi/2
    r1=16 if i%5==0 else 17
    x0=round(35+math.cos(a)*r1); y0=round(40+math.sin(a)*r1*.94)
    x1=round(35+math.cos(a)*18); y1=round(40+math.sin(a)*17)
    c.line(x0,y0,x1,y1,'#fff0a1' if i%5==0 else '#bda573')
# Toothed wheels with recessed webs and bright machined edges.
def gear(cx,cy,r,n):
    pts=[]
    for j in range(n):
        for k,rr in [(0,r-1),(1,r),(2,r),(3,r-1)]:
            a=2*math.pi*(j+k/4)/n
            pts.append((round(cx+rr*math.cos(a)),round(cy+rr*math.sin(a))))
    c.poly([(x,y+1) for x,y in pts],'#211b18')
    c.poly(pts,'#e1b35e')
    c.poly(pts,'#8e622b',False)
    # small upper rim glints on each tooth
    for x,y in pts:
        if y<cy: c.set(x,y,'#ffe6a0')
    c.circle(cx,cy,r-2,'#9c7134')
    c.circle(cx,cy,r-3,'#302a25')
    for j in range(5):
        a=j*math.pi*2/5-.6
        x=round(cx+(r-3)*math.cos(a)); y=round(cy+(r-3)*math.sin(a))
        c.line(cx,cy,x,y,'#c99847')
        if y<cy: c.set(x,y,'#f4cc75')
    c.circle(cx,cy,2,'#dca855')
    c.set(cx,cy,'#3b2920'); c.set(cx-1,cy-1,'#fff6c5')
gear(42,33,7,12)
gear(30,32,5,10)
gear(26,44,7,12)
gear(39,46,7,12)
gear(47,44,4,8)
# Curved bridge with polished edge and screw heads.
c.poly([(29,49),(32,45),(35,46),(33,52),(29,54),(25,52)],'#3b2920')
c.poly([(29,49),(32,46),(34,46),(32,51),(29,53),(26,51)],'#dfaa51')
c.line(27,50,30,51,'#fff0a1')
for x,y in [(22,36),(46,30),(30,51),(42,52)]:
    c.circle(x,y,1,'#c5c6aa'); c.line(x-1,y,x+1,y,'#303942'); c.set(x,y-1,'#f5edcf')
# Blued steel hands with thin silver reflections. Both pivot on the same arbor.
c.line(35,41,30,27,'#100f15')
c.poly([(34,40),(33,34),(30,26),(31,35),(35,42)],'#263b4a')
c.line(34,38,30,27,'#c3d9d7')
c.poly([(35,39),(45,35),(49,35),(46,38),(36,42)],'#142532')
c.line(36,39,47,36,'#8eb4bc')
c.line(32,44,39,36,'#e4b964')
c.circle(35,40,2,'#654221')
c.circle(35,40,1,'#fff0a1'); c.set(35,40,'#c99847')
result=c
view(result,scale=8,margin=0)
finish(result)
