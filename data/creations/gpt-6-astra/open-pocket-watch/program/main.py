import math
result = new_canvas(64,64, '#0b1019', name='open-pocket-watch')
c=result
# Restricted warm metal ramp, with cool shadows.
gold=['#30201b','#52321d','#795023','#a7732d','#ca963e','#e5b653','#f4d47b','#fff0b4']
# Quiet, stepped background pools.
c.ellipse(32,40,29,23,'#101925')
c.ellipse(34,46,27,17,'#080d15')
c.ellipse(36,56,24,7,'#050910')
# Chain of interlocking gold links, receding toward the upper right.
links=[(53,24,3,2,-35),(57,21,3,2,-55),(59,17,2,3,5),(58,12,3,2,45),(54,9,3,2,15),(49,8,3,2,-10),(45,10,2,3,20),(46,14,3,2,25),(51,15,3,2,-5),(55,13,2,3,-20),(55,8,2,3,10),(58,4,3,2,-25),(61,4,2,3,-10)]
def ellipse_points(cx,cy,rx,ry,rot=0,n=60):
    a=math.radians(rot)
    return [(round(cx+rx*math.cos(t)*math.cos(a)-ry*math.sin(t)*math.sin(a)),round(cy+rx*math.cos(t)*math.sin(a)+ry*math.sin(t)*math.cos(a))) for t in [i*math.tau/n for i in range(n)]]
for cx,cy,rx,ry,rot in links:
    p=ellipse_points(cx,cy,rx,ry,rot)
    c.poly(p,'#211c1b',False)
    for i,(x,y) in enumerate(p):
        if 0<=x<64 and 0<=y<64:
            col=gold[6] if x<cx and y<=cy else gold[4] if y<cy else gold[2]
            c.set(x,y,col)
# Lid, lifted behind the movement. Pixel-quantized reflective bands.
def metal_ellipse(cx,cy,rx,ry,rotation,lid=False):
    a=math.radians(rotation); ca=math.cos(a);sa=math.sin(a)
    for y in range(64):
        for x in range(64):
            dx=x-cx;dy=y-cy
            u=(dx*ca+dy*sa)/rx;v=(-dx*sa+dy*ca)/ry
            r=math.hypot(u,v)
            if r>1: continue
            angle=math.atan2(v,u)
            light=(-u*.60-v*.80)/max(r,.001)
            if r>.97: idx=1
            elif r>.89: idx=max(1,min(7,int(4+3*light)))
            elif r>.83: idx=7 if light>.2 else 3
            elif r>.77: idx=1 if light>.0 else 5
            elif lid:
                idx=max(1,min(5,int(3-1.2*u-1.6*v)))
                # Fine, sparse brushed reflection across the inner lid.
                if (x+2*y)%13==0 and light>.2: idx=min(5,idx+1)
            else: continue
            c.set(x,y,gold[idx])
metal_ellipse(18,15,17,12,-36,True)
c.poly(ellipse_points(18,15,11.8,7.3,-36),'#b18138',False)
c.poly(ellipse_points(18,15,10.5,6,-36),'#65431f',False)
# Engraved floral flourish on the inner cover.
c.path('M 10 20 Q 16 19 20 13 Q 23 9 27 9 M 14 20 Q 13 15 17 15 M 19 15 Q 18 10 22 10 M 20 14 Q 25 15 25 11', '#c69946',False)
c.line(8,17,10,14,'#f4d47b')
c.set(6,15,'#fff0b4')
# Knurled pendant and bow at the upper right.
c.ellipse(48,24,5,5,'#402c21')
c.ellipse(48,23,4,4,'#d2a353')
c.ellipse(48,23,2,3,'#0b1019')
c.poly([(44,26),(48,23),(52,27),(48,31)],'#714923')
c.line(45,26,48,29,'#f4d47b')
c.line(47,25,50,28,'#e5b653')
c.line(49,25,51,27,'#fff0b4')
# Open-cover hinge, with individual polished knuckles.
c.poly([(20,25),(24,22),(32,28),(27,32)],'#422b1c')
for x,y in [(22,25),(25,26),(28,28)]:
    c.line(x,y,x+2,y+3,'#d6a347')
    c.set(x,y,'#fff0b4')
# Main case, raised from a dark undercut.
c.ellipse(35,43,23,20,'#30201b')
metal_ellipse(35,41,23,20,0)
# Skeleton dial: pale gold chapter ring around a dark mechanical well.
c.ellipse(35,41,19,16,'#e5c984')
c.ellipse(35,41,18,15,'#a0834b')
c.ellipse(35,41,16,13,'#302a24')
c.ellipse(35,41,15,12,'#171d22')
# Graduated minute track, stronger hour indices.
for i in range(60):
    t=i*math.tau/60-math.pi/2
    major=i%5==0
    r0=.85 if major else .94
    x0=round(35+18*r0*math.cos(t));y0=round(41+15*r0*math.sin(t))
    x1=round(35+18*math.cos(t));y1=round(41+15*math.sin(t))
    c.line(x0,y0,x1,y1,'#503d2c' if major else '#78603a')
# Movement plates and cut-outs.
c.poly([(22,35),(25,30),(34,30),(37,34),(34,39),(25,40)],'#a77932')
c.line(25,31,33,31,'#e5b653')
c.poly([(41,31),(47,34),(49,44),(45,48),(41,45),(42,39)],'#8c6029')
c.line(47,36,48,42,'#e5b653')
c.poly([(27,47),(34,44),(44,47),(44,50),(36,53),(28,51)],'#b48638')
c.line(29,51,36,52,'#f4d47b')
# Deep circular recesses beneath the train.
for x,y,r in [(25,42,7),(35,48,6),(43,40,6),(34,34,4)]:
    c.circle(x,y,r+1,'#0b131b')
    c.circle(x,y,r,'#6b4b28')
# Toothed wheels, open spokes, hubs and highlighted tooth faces.
def gear(cx,cy,r,teeth,phase=0):
    p=[]
    for i in range(teeth):
        for f,rr in [(0,r-.8),(.16,r),(.57,r),(.74,r-.8)]:
            t=phase+(i+f)*math.tau/teeth
            p.append((round(cx+rr*math.cos(t)),round(cy+rr*math.sin(t))))
    c.poly(p,'#d8a548')
    c.poly(p,'#9f6e2c',False)
    for x,y in p:
        if y<cy and x<=cx+2:c.set(x,y,'#ffe395')
    c.circle(cx,cy,max(1,r-2),'#533b24')
    c.circle(cx,cy,max(1,r-3),'#151d22')
    for i in range(5):
        t=phase+i*math.tau/5
        ex=round(cx+(r-2)*math.cos(t));ey=round(cy+(r-2)*math.sin(t))
        c.line(cx,cy,ex,ey,'#c4913c')
        if ey<cy:c.set(ex,ey,'#f4d47b')
    c.circle(cx,cy,2,'#e5b653')
    c.circle(cx,cy,1,'#795023')
    c.set(cx,cy,'#f9e2a2')
gear(25,42,7,12,.14)
gear(35,48,5,10,.4)
gear(43,40,6,11,.23)
gear(34,34,4,8,.1)
# Steel balance bridge and jewel bearings.
c.line(22,48,29,37,'#463d2f')
c.line(23,48,30,37,'#e7c778')
c.line(24,48,31,37,'#9b7338')
c.circle(26,43,2,'#cda765')
c.circle(26,43,1,'#562533')
c.set(25,42,'#e29483')
for x,y in [(25,32),(44,33),(47,46),(29,50)]:
    c.circle(x,y,1,'#ead59a')
    c.line(x-1,y,x+1,y,'#635443')
    c.set(x,y-1,'#fff0b4')
# Blued steel hands, pale beveled edges, and central pin.
c.line(36,42,31,31,'#080e15')
c.line(36,42,47,37,'#080e15')
c.poly([(34,41),(29,31),(32,33),(36,40)],'#7fabb3')
c.line(34,39,30,31,'#e1f1dc')
c.line(35,41,46,36,'#8ab8be')
c.line(36,41,46,37,'#d6e7d2')
c.line(35,41,32,46,'#567885')
c.circle(35,41,2,'#261f1c')
c.circle(35,41,1,'#e5b653')
c.set(34,40,'#fff5cc')
# Hard glints on the polished case, with darker lower-edge reflections.
c.path('M 15 36 L 16 33 L 18 30 L 22 27', '#fff0b4',False)
c.line(19,52,23,55,'#f4d47b')
c.line(28,59,37,60,'#ca963e')
c.line(38,59,44,58,'#ffe395')
c.line(55,37,56,42,'#fff0b4')
c.set(55,35,'#fff5cc')
assert tuple(result.stats()['size']) == (64,64)
assert result.stats()['colors_used'] <= 86
view(result)
save('open-pocket-watch',result)
finish(result)
