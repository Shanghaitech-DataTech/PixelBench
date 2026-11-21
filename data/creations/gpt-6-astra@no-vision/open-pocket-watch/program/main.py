import math
c = new_canvas(64,64,background='#090e19',name='open-pocket-watch')
# A restricted, cool-shadow / warm-metal palette.
bg='#090e19'; dark='#17151b'; edge='#3b261e'; bronze='#6e4425'; shade='#98612d'; gold='#c28b3d'; light='#e8b857'; pale='#ffe39a'; white='#fff3c2'; steel='#637581'
# Subtle backdrop and grounded shadow.
c.ellipse(35,40,28,23,'#0c1420')
c.ellipse(38,57,23,5,'#050910')
# Raised open cover: exterior, stepped rim, recessed reflective interior.
c.ellipse(17,17,16,15,edge)
c.ellipse(17,16,16,14,gold)
c.ellipse(16,15,15,13,pale)
c.ellipse(17,16,14,12,bronze)
c.ellipse(17,16,13,11,light)
c.ellipse(17,16,11,9,shade)
c.ellipse(17,15,10,8,gold)
c.poly([(9,12),(13,9),(20,8),(26,12),(25,14),(16,20),(10,19)],light)
c.poly([(11,11),(16,8),(21,9),(13,17),(9,17)],pale)
c.poly([(16,22),(24,16),(27,15),(26,20),(22,23)],bronze)
c.line(6,11,10,6,white);c.line(11,5,20,3,white)
c.line(5,12,4,17,pale);c.line(8,25,15,29,shade)
c.line(18,27,24,24,light)
# Fine engraved concentric crest in the empty lid.
c.ellipse(18,16,6,5,shade,fill=False)
c.ellipse(18,16,5,4,light,fill=False)
c.poly([(18,12),(21,16),(18,20),(15,16)],gold,fill=False)
c.set(18,15,pale)
# Hinge knuckles between cover and body.
c.line(19,29,28,23,edge)
for x,y in [(20,27),(23,25),(26,23)]:
    c.rect(x,y,3,5,bronze);c.line(x,y,x,y+3,pale);c.set(x+1,y,white)
# Chain with interlocking individual links, trailing off toward the right.
for x,y,rx,ry in [(48,9,3,2),(52,6,2,3),(56,4,3,2),(60,6,2,3),(60,11,3,2),(59,16,2,3),(61,20,2,2)]:
    c.ellipse(x,y,rx,ry,edge,fill=False)
    c.ellipse(x,y-1,rx,ry,gold,fill=False)
    c.line(x-rx+1,y-ry,x,y-ry,pale)
# Bow and fluted winding crown, partly behind the case.
c.ellipse(45,13,5,5,bronze,fill=False)
c.ellipse(45,12,4,4,light,fill=False)
c.line(42,9,45,8,white)
c.poly([(41,15),(48,17),(46,23),(39,20)],edge)
c.line(41,16,47,18,light)
for x in range(40,47,2): c.line(x,18,x-1,20,gold)
# Heavy machined case and nested bright bevels.
c.ellipse(38,41,23,22,edge)
c.ellipse(38,40,23,22,bronze)
c.ellipse(38,39,22,22,gold)
c.ellipse(38,39,21,21,pale)
c.ellipse(38,40,20,20,shade)
c.ellipse(38,40,19,19,edge)
c.ellipse(38,40,18,18,light)
c.ellipse(38,40,16,16,dark)
# Deliberate case reflections, top left lit; bottom right reflected light.
c.path('M 17 36 Q 18 23 31 19',white,fill=False)
c.line(33,18,41,18,white)
c.path('M 59 39 Q 60 52 48 59',light,fill=False)
c.line(32,60,43,60,bronze)
c.line(35,61,42,61,gold)
c.line(18,43,20,49,light)
# Chapter ring: minute ticks, heavier five-minute indices.
for i in range(60):
    a=2*math.pi*i/60-math.pi/2
    r0=16.4 if i%5==0 else 17.5
    x0=round(38+math.cos(a)*r0);y0=round(40+math.sin(a)*r0)
    x1=round(38+math.cos(a)*18.1);y1=round(40+math.sin(a)*18.1)
    c.line(x0,y0,x1,y1,edge if i%5==0 else bronze)
# Skeleton movement: dark cavities and a gold foundation.
c.poly([(30,26),(38,25),(43,28),(41,33),(35,35),(32,42),(26,44),(23,40),(23,33)],bronze)
c.poly([(34,48),(46,42),(51,44),(51,49),(45,54),(36,55)],shade)
c.line(25,32,31,27,light)
c.ellipse(36,32,4,5,'#25232a')
c.ellipse(42,49,9,5,'#30241c')
# Individually cut teeth and open spokes reveal the darker plates underneath.
def gear(cx,cy,r,teeth):
    pts=[]
    for j in range(teeth*4):
        a=2*math.pi*j/(teeth*4)
        rr=r if j%4 in (1,2) else r-1
        pts.append((round(cx+rr*math.cos(a)),round(cy+rr*math.sin(a))))
    c.poly([(x,y+1) for x,y in pts],edge)
    c.poly(pts,gold)
    c.poly(pts,light,fill=False)
    c.circle(cx,cy,r-2,bronze)
    c.circle(cx,cy,r-3,dark)
    for j in range(5):
        a=j*2*math.pi/5-.3
        x=round(cx+(r-2)*math.cos(a));y=round(cy+(r-2)*math.sin(a))
        c.line(cx,cy,x,y,gold)
    c.circle(cx,cy,1,light)
    c.set(cx,cy,edge)
    c.line(cx-r+2,cy-2,cx-r+3,cy-3,pale)
gear(27,36,5,10)
gear(37,44,7,12)
gear(47,35,6,10)
gear(28,50,4,8)
gear(47,49,4,8)
# Smaller winding train at the top.
gear(37,29,3,7)
# Bridges with raised edges and blued screw heads.
c.poly([(31,26),(33,26),(35,34),(39,37),(38,40),(33,36)],gold)
c.line(31,26,34,34,pale)
c.line(34,34,38,37,light)
c.poly([(39,49),(42,49),(44,53),(40,55),(36,54)],gold)
c.line(37,53,41,54,pale)
for x,y in [(32,28),(41,52),(50,41),(25,43)]:
    c.circle(x,y,1,steel);c.set(x-1,y-1,pale);c.line(x-1,y,x+1,y,'#243142')
# Garnet bearings, small glints.
for x,y in [(37,44),(47,35)]:
    c.set(x,y,'#762a36');c.set(x,y-1,'#e2886d')
# Readable blued-steel hands, elevated over the open mechanism (10:08).
c.line(38,41,30,33,'#050b14');c.line(39,41,47,29,'#050b14')
c.poly([(38,40),(29,33),(30,32),(39,38)],'#344d62')
c.line(37,38,30,32,'#a5c1bf')
c.poly([(37,39),(46,28),(47,28),(40,40)],'#253d53')
c.line(39,38,46,29,'#a5c1bf')
c.line(38,40,42,45,steel)
c.circle(38,40,2,edge);c.circle(38,39,1,pale);c.set(38,39,white)
# A few crisp rim glints finish the metal.
c.set(22,26,white);c.line(53,24,55,26,pale);c.set(57,49,pale)
print(c.stats_text())
print(c.matrix_text(region=(21,25,52,53)))
save('open-pocket-watch',c)
finish(c)
