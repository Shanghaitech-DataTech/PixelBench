import math
import random

# A restrained palette for polished brass, aged gold, and blued steel.
BG = '#0b111b'
c = new_canvas(64, 64, BG, name='open_pocket_watch')
G = ['#25170f','#442816','#66401e','#875724','#a8752d','#c5923e','#e4b252','#f6cd79','#ffe6a3','#fff3cd']
DARK = '#100e10'

# Dark, quietly faceted background and a contact shadow.
c.poly([(0,48),(25,39),(55,64),(0,64)], '#0d1521')
c.poly([(42,0),(63,0),(63,37),(53,28)], '#0e1621')
c.ellipse(37,45,25,18,'#080c13')
c.ellipse(18,21,15,18,'#080c13')

# Cover: an oblique elliptical polished gold lid, behind the case.
lcx,lcy=16.5,18.2
ang=math.radians(-35)
ca,sa=math.cos(ang),math.sin(ang)
for y in range(0,39):
    for x in range(0,36):
        dx,dy=x-lcx,y-lcy
        u=dx*ca+dy*sa
        v=-dx*sa+dy*ca
        r=math.sqrt((u/12.9)**2+(v/17.5)**2)
        t=math.atan2(v/17.5,u/12.9)
        if r>1.04: continue
        light=(-dx*.72-dy*.6)/19
        metal=4+int(light*3+1.1*math.cos(t*3+.6))
        metal=max(1,min(9,metal))
        if r>1.0: col=G[0]
        elif r>.943: col=G[min(9,metal+2)]
        elif r>.87: col=G[max(1,metal-1)]
        elif r>.818: col=G[min(9,metal+2)]
        elif r>.774: col=G[1]
        else:
            # The deep reflected stripe crosses the otherwise bright inner bowl.
            stripe=u+.38*v
            if stripe<-6.0: idx=7
            elif stripe<-3: idx=8
            elif stripe<-1.4: idx=6
            elif stripe<1.7: idx=3
            elif stripe<5.4: idx=2
            elif stripe<7.3: idx=4
            else: idx=6
            if v>7: idx=max(2,idx-1)
            if v<-9: idx=min(8,idx+1)
            col=G[idx]
        c.set(x,y,col)

# Fine engraved arcs inside the lid (in its own local plane).
def lidpoint(u,v):
    return (round(lcx+u*ca-v*sa),round(lcy+u*sa+v*ca))
for start,end,rr,col in [(25,155,.67,G[5]),(196,315,.67,G[4]),(210,295,.61,G[5])]:
    last=None
    for deg in range(start,end+1,4):
        t=math.radians(deg)
        p=lidpoint(12.9*rr*math.cos(t),17.5*rr*math.sin(t))
        if last: c.line(*last,*p,col)
        last=p
# Tiny hallmark in the cover, on the dark reflection.
for u,v in [(-1,-2),(0,-3),(1,-2),(0,-1)]:
    c.set(*lidpoint(u,v),G[6])
for v in (2,4):
    a=lidpoint(-2,v); b=lidpoint(2,v)
    c.line(*a,*b,G[4])

# Chain links, turned at different angles and interlocked.
def link(cx,cy,rx,ry,angle):
    aa=math.radians(angle)
    pts=[]
    for k in range(25):
        t=k*math.tau/24
        ux,uy=rx*math.cos(t),ry*math.sin(t)
        pts.append((round(cx+ux*math.cos(aa)-uy*math.sin(aa)),round(cy+ux*math.sin(aa)+uy*math.cos(aa))))
    for a,b in zip(pts,pts[1:]):
        c.line(a[0],a[1]+1,b[0],b[1]+1,G[0])
    for i,(a,b) in enumerate(zip(pts,pts[1:])):
        col=G[7] if 11<=i<=19 else G[4] if i<11 else G[2]
        c.line(*a,*b,col)
    c.set(round(cx-rx*.45),round(cy-ry*.7),G[9])
for p in [(41,2,3,1,8),(47,3,3,2,8),(53,4,3,2,18),(58,7,3,2,55),(58,12,3,2,130)]:
    link(*p)
# Suspension bow and crown.
link(53.5,16,4,3,-39)
c.line(51,18,48,22,G[0])
c.line(53,18,50,23,G[3])
c.line(52,18,49,22,G[8])
c.poly([(48,17),(53,21),(49,26),(44,22)],G[1])
c.poly([(48,18),(52,21),(48,25),(45,22)],G[5])
for ax,ay in [(47,19),(49,20),(50,22)]:
    c.line(ax,ay,ax-2,ay+3,G[2])
    c.set(ax,ay,G[8])

# Cover hinge, visible on the upper-left shoulder.
c.poly([(16,26),(20,23),(28,29),(23,35)],G[0])
c.line(18,26,25,32,G[7])
c.line(17,28,24,34,G[3])
for i in range(4):
    c.line(18+i*2,26+i*2,16+i*2,29+i*2,G[5])
    c.set(18+i*2,26+i*2,G[9])

# Case. The lower rim has a heavier edge, describing the thickness.
c.ellipse(37,41,23,22,G[0])
for y in range(17,64):
    for x in range(13,62):
        dx,dy=x-37,y-39
        r=math.hypot(dx,dy)
        t=math.atan2(dy,dx)
        if r>22.3: continue
        lighting=(-dx*.8-dy*.64)/22
        idx=4+int(lighting*3+1.3*math.cos(3*t-1.0))
        idx=max(1,min(8,idx))
        if r>21.6: col=G[max(0,idx-2)]
        elif r>20.6: col=G[min(9,idx+2)]
        elif r>19.5: col=G[idx]
        elif r>18.7: col=G[max(0,idx-3)]
        elif r>17.1: col='#463523'
        else: col='#36261b'
        c.set(x,y,col)
# Strong broken gleams along the rim, and a lower reflected edge.
for start,end,r,col in [(194,242,21,G[9]),(245,278,20.3,G[7]),(20,66,21,G[6]),(70,124,21.4,G[7])]:
    last=None
    for deg in range(start,end+1,3):
        a=math.radians(deg); p=(round(37+r*math.cos(a)),round(39+r*math.sin(a)))
        if last:c.line(*last,*p,col)
        last=p

# Skeleton base plate, recesses and fixed, bevelled bridges.
c.poly([(22,29),(29,23),(39,22),(48,27),(51,32),(45,34),(39,31),(32,33),(28,39),(21,40)],G[3])
c.line(23,29,31,24,G[6])
c.line(31,24,39,23,G[7])
c.poly([(49,39),(54,39),(52,49),(45,55),(32,57),(25,51),(29,46),(37,48),(42,44)],G[3])
c.line(46,53,51,48,G[5])
# Wheel pockets are cut right through the movement into darkness.
for gx,gy,rr in [(27,38,8),(39,31,8),(46,42,7),(35,49,8)]:
    c.circle(gx,gy,rr,DARK)
    c.circle(gx,gy,rr,G[1],fill=False)

# Toothed wheels: ring, radial spokes, hub and individually lit tooth flanks.
def gear(cx,cy,r,teeth,phase=0,spokes=4,tone=0):
    mask=set()
    for y in range(cy-r-1,cy+r+2):
        for x in range(cx-r-1,cx+r+2):
            dx,dy=x-cx,y-cy
            rad=math.hypot(dx,dy)
            a=math.atan2(dy,dx)
            tooth=((a-phase)*teeth/math.tau)%1
            limit=r if .16<tooth<.70 else r-1.15
            spoke=abs(math.sin((a-phase)*spokes/2))*rad<.65
            if rad<=limit and (rad>=r-2.4 or rad<=1.45 or spoke):mask.add((x,y))
    for x,y in mask:
        if (x+1,y+1) not in mask:c.set(x+1,y+1,G[0])
    for x,y in sorted(mask,key=lambda p:p[1]):
        dx,dy=x-cx,y-cy
        rad=math.hypot(dx,dy)
        top=(x-1,y-1) not in mask
        bottom=(x+1,y+1) not in mask
        idx=5+tone
        if top:idx=8+tone
        elif bottom:idx=2+tone
        elif dx+dy<-2:idx=6+tone
        elif dx+dy>3:idx=4+tone
        c.set(x,y,G[max(1,min(9,idx))])
    c.set(cx,cy,G[1]);c.set(cx-1,cy-1,G[9])
    c.set(cx+1,cy,G[4])

gear(27,38,7,12,.18,4,0)
gear(39,31,7,12,.41,5,0)
gear(46,42,6,10,.10,4,1)
gear(35,49,7,12,.39,5,-1)
# Concentric bearing seats and axle pins.
for x,y in [(27,38),(39,31),(46,42),(35,49)]:
    c.circle(x,y,1,G[4])
    c.set(x,y,'#171d20')
    c.set(x-1,y-1,G[8])
    c.set(x+1,y+1,G[2])

# Curved bridge secures the central hand arbor without hiding the train.
c.poly([(22,44),(24,42),(34,39),(37,37),(40,38),(42,46),(40,49),(37,43),(29,44)],G[0])
c.poly([(22,43),(24,41),(34,38),(37,36),(39,37),(41,45),(39,47),(36,41),(29,43)],G[5])
c.line(24,41,34,38,G[8])
c.line(34,38,37,36,G[8])
c.line(39,38,40,44,G[7])
# Screws, with cool steel slots, and two ruby bearings.
def screw(x,y):
    c.circle(x,y,2,G[1])
    c.circle(x,y,1,'#85968e')
    c.set(x-1,y-1,'#e2e8c7')
    c.line(x-1,y+1,x+1,y-1,'#243033')
screw(24,43)
screw(49,51)
screw(31,25)
c.set(39,45,'#4b1421');c.set(39,44,'#c66b54')
c.set(27,38,'#631d28');c.set(27,37,'#edb185')

# Minute track and twelve longer baton hour markers.
for k in range(60):
    a=math.radians(k*6-90)
    if k%5==0:
        r0,r1=16.1,18.0
        col=G[8]
    else:
        r0,r1=18.0,18.0
        col=G[5] if k%2 else G[6]
    x0,y0=round(37+r0*math.cos(a)),round(39+r0*math.sin(a))
    x1,y1=round(37+r1*math.cos(a)),round(39+r1*math.sin(a))
    c.line(x0,y0,x1,y1,col)

# Engraved machining lines on the solid bridge and small gold reflections.
c.line(26,41,30,40,G[4])
c.line(27,42,31,41,G[6])
c.set(33,39,G[7])
c.set(35,38,G[9])
c.set(40,43,G[8])
# Ribbing and reflected edge light on the heavy lower case wall.
for deg in range(10,91,9):
    a=math.radians(deg)
    x,y=round(37+22.0*math.cos(a)),round(40+21.6*math.sin(a))
    c.set(x,y,G[3])
    if deg<65:c.set(x-1,y,G[5])
for x,y,col in [(52,54,G[8]),(51,55,G[8]),(50,56,G[7]),(43,60,G[8]),(42,60,G[8]),(41,61,G[6]),(18,29,G[9]),(17,31,G[8])]:
    c.set(x,y,col)
# A few very fine scratches following the cover's brushed inner surface.
for u,v,length in [(-6,-5,2),(-5,2,2),(-4,7,2),(5,5,1)]:
    p=lidpoint(u,v); q=lidpoint(u,v+length)
    c.line(*p,*q,G[7] if u<0 else G[5])

# Blued steel hands: dark undercuts, broad roots, narrow silver-blue edges.
c.line(38,40,47,26,'#0a0d13')
c.line(38,41,27,31,'#0a0d13')
c.poly([(37,42),(34,38),(25,31),(29,32),(39,38)],'#10242c')
c.poly([(37,40),(34,37),(26,31),(29,32),(38,38)],'#426977')
c.line(27,32,36,38,'#c5ddd2')
c.poly([(35,40),(38,35),(47,24),(43,33),(39,41)],'#11252d')
c.poly([(36,39),(39,35),(46,26),(41,35),(38,40)],'#477b85')
c.line(37,38,46,26,'#b4dbd6')
# Slender sweep seconds hand and gold centre boss.
c.line(32,34,48,50,'#a75a34')
c.set(48,50,G[8])
c.circle(37,39,2,G[1])
c.circle(37,39,1,G[7])
c.set(36,38,G[9]); c.set(37,39,'#d39a3f'); c.set(38,40,G[2])

result=c
view(result,scale=8,margin=0)
print(result.stats_text())
save('open_pocket_watch',result)
finish(result)
