import math
D='#161c2e'; WOOD='#6c513a'; MID='#97763d'; TAN='#bda759'; BR='#98694e'; GOLD='#dcaa46'; LIGHT='#f9e279'; YELLOW='#e1d968'; PLASTER='#bbae93'; CREAM='#e1dca3'
W,H=176,184

def make(angle,name):
    c=new_canvas(W,H,name=name)
    a=math.radians(angle); co=math.cos(a); si=math.sin(a); scale=1.16
    def p(x,y,z):
        return (round(88+scale*(x*co+(y-32)*si)),round(155+scale*(.7071*x*si-.7071*(y-32)*co-.7071*z)-scale*(.7071*34*si+.7071*32*co)))
    def poly3(pts,col,edge=None):
        q=[p(*v) for v in pts]; c.poly(q,col)
        if edge:c.poly(q,edge,fill=False)
    def stroke2(pts,col,w):
        for q,r in zip(pts,pts[1:]):
            dx=r[0]-q[0];dy=r[1]-q[1];n=max(1,math.hypot(dx,dy));ox=-dy/n*w/2;oy=dx/n*w/2
            c.poly([(round(q[0]+ox),round(q[1]+oy)),(round(r[0]+ox),round(r[1]+oy)),(round(r[0]-ox),round(r[1]-oy)),(round(q[0]-ox),round(q[1]-oy))],col)
            c.circle(*q,w//2,col);c.circle(*r,w//2,col)
    def stroke(pts,col,w):stroke2([p(*v) for v in pts],col,w)
    def front(pts,col):poly3([(x,-.5,z) for x,z in pts],col)
    window_shift=0
    def side(pts,col):poly3([(34,y,z-window_shift) for y,z in pts],col)
    def roofz(x):return 97-49*(abs(x)/43)**.67
    # Low dark foundation and plaster walls.
    side([(0,0),(64,0),(64,48),(0,48)],WOOD)
    side([(2,4),(62,4),(62,47),(2,47)],PLASTER)
    side([(4,10),(61,10),(61,43),(4,43)],CREAM)
    # Plaster wear, kept in angular clusters.
    for pts in [[(3,7),(17,7),(14,11),(7,11),(7,25),(3,27)],[(55,7),(62,7),(62,38),(59,35),(58,20)],[(9,42),(22,42),(19,39),(11,38)],[(44,44),(58,44),(58,40),(49,40)],[(18,13),(22,13),(22,16),(19,16)]]:side(pts,PLASTER)
    stroke([(34,0,0),(34,64,0),(34,64,48)],D,5)
    # Side sill and corner posts.
    for yy in [2,62]:
        side([(yy-3,2),(yy+3,2),(yy+3,46),(yy-3,46)],WOOD)
        side([(yy-1,5),(yy+2,6),(yy+1,20),(yy+2,32),(yy,45),(yy-2,43),(yy-1,27)],TAN)
        stroke([(34,yy+1,10),(34,yy,21),(34,yy+1,28)],MID,1)
    side([(0,1),(64,1),(64,5),(0,5)],WOOD)
    side([(4,5),(59,5),(58,7),(6,7)],TAN)
    # Single recessed arched window, on the right-hand wall.
    window_shift=5
    win=[(20,15),(20,34),(23,39),(29,42),(36,42),(42,39),(45,34),(45,15)]
    side(win,D)
    side([(22,17),(22,34),(25,38),(30,40),(36,40),(41,37),(43,33),(43,17)],MID)
    side([(25,20),(25,33),(28,36),(32,38),(36,37),(40,33),(40,20)],D)
    side([(27,23),(27,32),(30,35),(32,36),(32,23)],GOLD)
    side([(35,23),(35,36),(38,33),(39,31),(39,23)],TAN)
    side([(27,29),(29,31),(29,34),(27,32)],LIGHT)
    side([(25,21),(41,21),(41,24),(25,24)],GOLD)
    stroke([(34,22,29),(34,25,34),(34,31,36),(34,37,35)],LIGHT,2)
    side([(18,14),(47,14),(47,18),(18,18)],WOOD)
    side([(18,18),(47,18),(45,20),(20,20)],LIGHT)
    window_shift=0
    # Front facade and large arched entry.
    if angle<89:
        front([(-34,0),(34,0),(34,47),(24,58),(12,73),(0,93),(-12,73),(-24,58),(-34,47)],WOOD)
        front([(-30,4),(30,4),(30,47),(20,60),(0,87),(-20,60),(-30,47)],PLASTER)
        front([(-27,9),(27,9),(27,45),(17,58),(0,80),(-17,58),(-27,45)],CREAM)
        front([(-28,10),(-19,10),(-21,22),(-19,33),(-22,42),(-28,46)],TAN)
        front([(24,8),(29,7),(29,46),(23,42),(21,29)],TAN)
        front([(-19,48),(-13,58),(0,74),(15,56),(22,48),(16,49),(0,64),(-9,57)],YELLOW)
        # timber corner posts
        for xx in [-31,31]:
            front([(xx-3,2),(xx+3,2),(xx+3,45),(xx-3,45)],WOOD)
            front([(xx-1,5),(xx+2,8),(xx,22),(xx+2,32),(xx,43),(xx-2,43),(xx-1,29)],TAN)
        arch=[(-20,2),(-20,29),(-18,40),(-13,48),(-6,53),(2,54),(11,50),(18,42),(21,31),(21,2)]
        front(arch,D)
        front([(-17,3),(-17,29),(-15,40),(-10,47),(-4,50),(3,51),(10,47),(15,40),(18,30),(18,3)],MID)
        front([(-13,4),(-13,29),(-11,38),(-7,43),(0,46),(7,43),(12,36),(14,28),(14,4)],WOOD)
        front([(-10,5),(-10,29),(-8,36),(-3,41),(3,41),(8,35),(11,28),(11,5)],GOLD)
        front([(-10,5),(-10,20),(11,20),(11,5),(6,3),(-5,3)],BR)
        for xx in [-7,-1,6]: front([(xx,6),(xx+2,6),(xx+2,20),(xx,20)],MID)
        front([(-10,23),(11,23),(11,26),(-10,26)],D)
        front([(-12,20),(13,20),(13,23),(-12,23)],LIGHT)
        front([(-5,7),(-5,12),(-2,15),(3,15),(6,12),(6,7),(2,5),(-2,5)],GOLD)
        front([(7,17),(9,17),(9,19),(7,19)],LIGHT)
        stroke([(-17,-1,5),(-18,-1,29),(-16,-1,39),(-11,-1,47),(-4,-1,51),(3,-1,52),(11,-1,48)],TAN,3)
        stroke([(-15,-1,33),(-13,-1,40),(-7,-1,47),(0,-1,49)],LIGHT,2)
        stroke([(-34,0,0),(34,0,0)],D,5)
    # Curved roof surfaces: distant slope first, then near slope.
    for sign in [-1,1]:
        xs=[sign*v for v in [0,5,12,21,31,43]]
        pts=[(x,-6,roofz(x)) for x in xs]+[(x,71,roofz(x)) for x in reversed(xs)]
        poly3(pts,WOOD,D)
        # Golden tiles in staggered courses following the curved roof.
        for row,(u,v) in enumerate(zip([2,10,20,31],[10,20,31,41])):
            starts=[-4,11,27,43,59,69] if row%2==0 else [-4,3,19,35,51,69]
            for j,(ya,yb) in enumerate(zip(starts,starts[1:])):
                x1=sign*u;x2=sign*(v-.8)
                poly3([(x1,ya,roofz(x1)+.4),(x1,yb-1,roofz(x1)+.4),(x2,yb-1,roofz(x2)+.4),(x2,ya,roofz(x2)+.4)],GOLD if (row+j)%4 else TAN)
                # Short ochre chips and uneven tile joints echo the source roof.
                xx=sign*(v-1.3)
                stroke([(xx,ya+1,roofz(xx)+.6),(xx,min(ya+4,yb-2),roofz(xx)+.6)],BR,2)
                if yb-ya>10:
                    xx=sign*(u+3)
                    stroke([(xx,yb-2,roofz(xx)+.7),(sign*(u+5),yb-2,roofz(sign*(u+5))+.7)],BR,2)
                if j%3!=1:
                    xx=sign*(u+1.5)
                    stroke([(xx,ya+1,roofz(xx)+.7),(xx,min(ya+8,yb-2),roofz(xx)+.7)],LIGHT,2)
        # Outer eave timber.
        stroke([(sign*43,-7,roofz(43)),(sign*43,72,roofz(43))],D,7)
        stroke([(sign*43,-7,roofz(43)+1),(sign*43,72,roofz(43)+1)],MID,4)
        stroke([(sign*42,-5,roofz(42)+2),(sign*42,70,roofz(42)+2)],TAN,2)
    # Back roof verge, visible against the silhouette.
    for sign in [-1,1]:
        pts=[(sign*x,72,roofz(x)+1) for x in [0,5,12,21,31,44]]
        stroke(pts,D,6);stroke(pts,WOOD,4);stroke([(x,y,z+1) for x,y,z in pts],TAN,2)
    # Front carved gable fascia.
    for sign in [-1,1]:
        pts=[(sign*x,-8,roofz(x)) for x in [0,5,12,21,31,44]]
        stroke(pts,D,9);stroke(pts,WOOD,6);stroke([(x,y,z+1) for x,y,z in pts],MID,4)
        stroke([(x,y,z+3) for x,y,z in pts],TAN,2)
    # Thick ridge pole and grain, with a small carved front end.
    stroke([(0,-10,95),(0,-3,99),(0,68,99),(0,75,101)],D,9)
    stroke([(0,-10,96),(0,-3,100),(0,68,100),(0,75,102)],WOOD,6)
    stroke([(0,-9,98),(0,-3,102),(0,68,102),(0,75,103)],TAN,4)
    stroke([(0,2,102),(0,13,103),(0,22,101),(0,38,103),(0,49,101),(0,67,103)],MID,2)
    stroke([(0,7,104),(0,16,104)],LIGHT,1)
    if angle<89:
        front([(-6,83),(-6,87),(6,87),(6,83),(3,81),(-3,81)],YELLOW)
    return c
f1=make(45,'house_45')
f2=make(90,'house_90')
view(f1)
view(f2)
finish([f1,f2])
