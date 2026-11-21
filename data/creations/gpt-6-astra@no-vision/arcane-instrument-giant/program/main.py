import math, random
import numpy as np

# The complete scene uses a deliberately restricted, opaque pixel palette.
W=H=256
c=new_canvas(W,H,name='The Aureate Engine')
INK='#070b13'
BG=['#060a12','#080e18','#0b1420','#0e1b29','#132333','#182b3a','#203443','#2a4150']
STONE=['#101722','#18212c','#222d38','#2e3b46','#3d4a52','#526168','#68767a','#87908b']
G=['#171319','#2b2020','#463026','#63432c','#855b33','#ab793f','#c99a50','#e4bd70','#f5db97','#fff1c1']
T=['#10242e','#143d46','#1c5d61','#2b8582','#45b5a6','#72deca','#adf3dc','#e4fff0']
BLUE=['#102338','#173c55','#245e78','#348ca1','#58bfd0','#8ae7e5','#d8fff4']
V=['#211d37','#3b2e59','#5c467f','#8862a3','#ba8aca','#e5bcea','#fff0ff']
A=['#432c22','#764527','#ac662d','#d9953b','#efbf63','#ffe39b','#fff6d4']
rng=random.Random(719)

def pt(x,y,r,t): return (x+r*math.cos(t),y+r*math.sin(t))
def ip(p): return (int(round(p[0])),int(round(p[1])))
def linew(x0,y0,x1,y1,w,col):
    dx=x1-x0;dy=y1-y0;l=math.hypot(dx,dy)
    if l<0.01:
        c.circle(round(x0),round(y0),max(0,w//2),col); return
    nx=-dy/l*(w-1)/2;ny=dx/l*(w-1)/2
    c.poly([ip((x0+nx,y0+ny)),ip((x1+nx,y1+ny)),ip((x1-nx,y1-ny)),ip((x0-nx,y0-ny))],col)
    c.line(round(x0),round(y0),round(x1),round(y1),col)
    if w>2:
        c.circle(round(x0),round(y0),(w-1)//2,col)
        c.circle(round(x1),round(y1),(w-1)//2,col)

def arc(x,y,r,start,end,col):
    last=None
    for i in range(max(2,int(abs(end-start)*r*1.8))+1):
        t=start+(end-start)*i/max(2,int(abs(end-start)*r*1.8))
        p=ip(pt(x,y,r,t))
        if last: c.line(*last,*p,col)
        last=p

def polyoutline(points,col,edge=INK):
    pp=[ip(p) for p in points]
    for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
        c.poly([(x+dx,y+dy) for x,y in pp],edge)
    c.poly(pp,col)

def ring(x,y,ro,ri,pal=G):
    for yy in range(max(0,int(y-ro-1)),min(256,int(y+ro+2))):
        for xx in range(max(0,int(x-ro-1)),min(256,int(x+ro+2))):
            dx=xx-x;dy=yy-y;r=math.hypot(dx,dy)
            if ri<=r<=ro:
                light=(-.56*dx-.83*dy)/max(1,r)
                if ro-r<1.05 or r-ri<.85: col=INK
                elif ro-r<2.1: col=pal[max(3,min(len(pal)-1,int(6+2*light)))]
                elif r-ri<1.9: col=pal[3 if light<.1 else 5]
                elif ro-r<3 and ro-ri>8: col=pal[2]
                else: col=pal[max(2,min(len(pal)-1,int(5+1.8*light)))]
                c.set(xx,yy,col)

def orbitpoint(x,y,a,b,ang,t):
    ca=math.cos(ang);sa=math.sin(ang)
    return (x+a*math.cos(t)*ca-b*math.sin(t)*sa,y+a*math.cos(t)*sa+b*math.sin(t)*ca)

def orbit(x,y,a,b,ang,width,front=None,etch=True):
    ca=math.cos(ang);sa=math.sin(ang)
    ex=int(math.sqrt((a*ca)**2+(b*sa)**2)+width+2)
    ey=int(math.sqrt((a*sa)**2+(b*ca)**2)+width+2)
    for yy in range(max(0,y-ey),min(256,y+ey+1)):
        for xx in range(max(0,x-ex),min(256,x+ex+1)):
            dx=xx-x;dy=yy-y;X=dx*ca+dy*sa;Y=-dx*sa+dy*ca
            q=math.hypot(X/a,Y/b)
            if q<.01:continue
            t=math.atan2(Y/b,X/a)
            if front is True and t<0:continue
            if front is False and t>=0:continue
            grad=math.hypot(math.cos(t)/a,math.sin(t)/b)
            d=(q-1)/grad
            if abs(d)>width/2+1:continue
            light=-.55*math.cos(t+ang)-.83*math.sin(t+ang)
            if abs(d)>width/2:col=INK
            elif d<-width/2+1:col=G[8 if light>-.3 else 6]
            elif d>width/2-1:col=G[2]
            else:col=G[max(3,min(7,int(5.4+light*1.5)))]
            c.set(xx,yy,col)
    if etch:
        for k in range(64):
            t=k*2*math.pi/64
            if front is True and math.sin(t)<-.01:continue
            if front is False and math.sin(t)>=-.01:continue
            p=orbitpoint(x,y,a,b,ang,t)
            # normal to the projected ellipse
            nx=math.cos(t)/a*ca-math.sin(t)/b*sa
            ny=math.cos(t)/a*sa+math.sin(t)/b*ca
            n=math.hypot(nx,ny);nx/=n;ny/=n
            if k%4==0:
                c.circle(*ip(p),1,G[2]); c.set(*ip((p[0]-.4,p[1]-.7)),G[8])
            else:
                c.line(*ip((p[0]-nx,p[1]-ny)),*ip((p[0]+nx,p[1]+ny)),G[3])

# Wall, broad pools of cold reflected light, and the receding vaulted hall.
for y in range(256):
    for x in range(256):
        d=math.sqrt(((x-125)/142)**2+((y-96)/166)**2)
        idx=max(0,min(4,int(5.2-d*4.3)))
        if y>211:idx=max(0,idx-1)
        c.set(x,y,BG[idx])
c.poly([(30,0),(62,0),(175,214),(146,214)],BG[3])
c.poly([(36,0),(43,0),(152,210),(140,210)],BG[4])
c.poly([(216,0),(225,0),(171,200),(164,200)],BG[2])
# Paired arches: fine outlines emerge from black masonry, not a bright border.
for inset,col in [(0,STONE[2]),(5,STONE[3]),(9,STONE[1])]:
    l=19+inset;r=237-inset
    c.path(f'M {l} 214 L {l} 90 Q {l} {10+inset} 128 {3+inset} Q {r} {10+inset} {r} 90 L {r} 214',col,fill=False)
for x,flip in [(12,False),(230,True)]:
    c.rect(x,91,14,119,STONE[1])
    c.rect(x+3,93,4,115,STONE[3] if not flip else STONE[2])
    c.rect(x+8,93,2,113,STONE[0])
    for yy in [91,116,145,174,203]:
        c.line(x,yy,x+13,yy,STONE[0]);c.line(x+3,yy+1,x+7,yy+1,STONE[2])
    c.rect(x-3,85,20,6,STONE[2]);c.line(x-3,85,x+16,85,STONE[4])
    c.rect(x-4,208,22,7,STONE[2]);c.line(x-4,208,x+17,208,STONE[4])
# Arch stone divisions, wall slit windows.
for x in [3,246]:
    c.rect(x,52,7,113,INK)
    c.line(x+2,55,x+2,160,BG[4]);c.line(x+3,55,x+3,160,BG[2])
for a in [3.38,3.66,3.95,4.23,4.67,5.1,5.45,5.75,6.02]:
    x=128+104*math.cos(a);y=90+86*math.sin(a)
    if 0<=y<82:c.line(round(x),round(y),round(128+112*math.cos(a)),max(0,round(90+94*math.sin(a))),STONE[1])
# Small cold lamps, deliberately subdued compared with the central engine.
for x,y in [(18,66),(239,70)]:
    c.line(x,0,x,y-9,STONE[1]);c.rect(x-3,y-7,7,12,INK)
    c.rect(x-2,y-5,5,8,STONE[3]);c.rect(x-1,y-4,2,6,T[3]);c.set(x-1,y-4,T[5])
    c.line(x-4,y+5,x+4,y+5,STONE[2])
# Floor blocks and converging seams.
c.rect(0,215,256,41,BG[2])
for xx in [0,32,63,97,159,193,225,255]:
    c.line(128,192,xx,255,STONE[1])
    c.line(128,195,xx,255,BG[1])
for yy in [218,225,237,253]:
    c.line(0,yy,255,yy,BG[1]);c.line(0,yy+1,255,yy+1,BG[3])
# Cast shadow under the pedestal.
c.ellipse(129,246,65,8,BG[0]);c.ellipse(131,245,52,6,INK)
# Stone pedestal, with a polished oval cap and a faceted weighty base.
polyoutline([(76,235),(180,235),(184,242),(176,249),(81,249),(72,242)],STONE[1])
c.poly([(76,236),(180,236),(176,242),(81,242)],STONE[3])
c.line(81,243,176,243,STONE[4]);c.line(80,247,176,247,STONE[0])
polyoutline([(83,211),(174,211),(174,234),(160,241),(96,241),(82,234)],STONE[3])
c.poly([(83,213),(101,220),(101,239),(83,232)],STONE[2])
c.poly([(157,220),(174,213),(174,233),(157,240)],STONE[1])
c.rect(102,220,55,19,STONE[3]);c.line(105,236,153,236,STONE[2])
c.ellipse(128,212,50,11,INK);c.ellipse(128,210,49,10,STONE[4])
c.ellipse(128,208,46,8,STONE[2]);c.ellipse(128,207,40,6,STONE[3])
arc(128,211,47,.1,3.05,STONE[5]) if False else None
# Front rim and carved border.
c.path('M 80 211 Q 128 233 176 211',STONE[6],fill=False)
c.path('M 83 215 Q 128 235 173 215',STONE[0],fill=False)
for x in range(93,168,6):
    yy=round(219+4*(1-((x-128)/40)**2))
    c.line(x,yy,x,yy+3,STONE[1]);c.set(x-1,yy,STONE[5])
# Chipped stone and intentional cracks.
for pts in [[(89,224),(92,227),(90,231),(94,235)],[(164,226),(161,230),(164,233)],[(111,240),(116,237),(118,238)],[(79,240),(85,241),(88,244)]]:
    for p,q in zip(pts,pts[1:]):c.line(*p,*q,STONE[0])
for x,y in [(99,234),(150,228),(112,225),(164,237),(88,219),(170,215),(119,245),(154,244)]:
    c.line(x,y,x+2,y,STONE[5]);c.set(x+2,y+1,STONE[2])
# Inlaid bronze plaque and its alchemical seal.
polyoutline([(117,221),(139,221),(144,229),(139,237),(117,237),(112,229)],G[2])
c.poly([(118,223),(138,223),(141,229),(137,235),(119,235),(115,229)],STONE[0])
c.circle(128,228,5,G[5],fill=False);c.line(128,222,128,234,T[3]);c.line(123,231,133,231,T[4])
c.poly([(124,230),(128,224),(132,230)],T[4],fill=False)
# A projected levitation sigil, visibly detached from the machine.
for rx,ry,col in [(38,6,T[1]),(32,5,T[2]),(22,3,T[3])]:c.ellipse(128,204,rx,ry,col,fill=False)
for i in range(16):
    t=i*math.pi/8;p=(128+35*math.cos(t),204+5.5*math.sin(t))
    c.set(*ip(p),T[5] if i%4==0 else T[3])
c.line(128,190,128,202,T[2]);c.line(127,194,127,201,T[3]);c.set(128,198,T[6])
for x,y in [(120,198),(138,195),(111,201),(145,200)]:c.set(x,y,T[3]);c.set(x,y-1,T[2])

CX,CY=128,102
# A dark blue astronomical glass plate. It is transparent-looking but uses no alpha.
for y in range(34,171):
    for x in range(60,197):
        rr=math.hypot(x-CX,y-CY)
        if rr<69:
            illumination=max(0,1-rr/80)+max(0,(120-y)/150)
            c.set(x,y,[BG[2],BG[3],BG[4]][min(2,int(illumination*1.8))])
# Engraved chart circles and a web of constellation lines.
for r in [62,50,37]:c.circle(CX,CY,r,T[0],fill=False)
for ang in [0,.55,1.12,1.68,2.26,2.82]:
    p=ip(pt(CX,CY,66,ang));q=ip(pt(CX,CY,66,ang+math.pi));c.line(*p,*q,T[0])
for constellation in [[(80,75),(94,84),(100,73),(112,69)],[(146,46),(152,66),(164,74)],[(75,117),(89,122),(94,132),(111,129)],[(148,127),(147,141),(157,149),(166,141)]]:
    for p,q in zip(constellation,constellation[1:]):c.line(*p,*q,T[1])
    for p in constellation:
        c.set(*p,T[3]);c.set(p[0]+1,p[1],T[2])
for i in range(90):
    x=rng.randint(64,192);y=rng.randint(38,167)
    if math.hypot(x-CX,y-CY)<65:
        c.set(x,y,T[1] if i%5 else T[2])
# Dark backdrops and the rear portions of the two inclined gimbals.
O1=(128,102,94,34,math.radians(-26),6)
O2=(128,102,85,29,math.radians(68),5)
orbit(*O1,front=False)
orbit(*O2,front=False)
# Outer structural torus and two concentric precision-scaled rims.
ring(CX,CY,84,68)
c.circle(CX,CY,79,G[3],fill=False)
c.circle(CX,CY,71,G[2],fill=False)
arc(CX,CY,82,math.radians(196),math.radians(281),G[8])
arc(CX,CY,69,math.radians(294),math.radians(350),G[5])
ring(CX,CY,62,57)
ring(CX,CY,43,40)
for i in range(96):
    t=i*2*math.pi/96;r1=63 if i%4==0 else 65
    p=ip(pt(CX,CY,r1,t));q=ip(pt(CX,CY,67,t));c.line(*p,*q,G[6] if i%4==0 else G[3])
for i in range(48):
    t=i*math.pi/24;p=ip(pt(CX,CY,55,t));q=ip(pt(CX,CY,56 if i%4 else 53,t));c.line(*p,*q,T[2])
# Script glyphs are drawn as tiny tangent-aligned engravings, not font text.
GLYPHS=[
 [((-2,-2),(0,2)),((0,2),(2,-2)),((-1,0),(1,0))],
 [((-2,2),(-2,-2)),((-2,-2),(2,-2)),((0,-2),(0,2)),((-1,1),(2,1))],
 [((-2,0),(0,-2)),((0,-2),(2,0)),((2,0),(0,2)),((0,2),(-2,0)),((0,-2),(0,2))],
 [((-2,-2),(2,2)),((2,-2),(-2,2)),((0,-3),(0,-1))],
 [((-2,2),(2,2)),((0,2),(0,-2)),((-2,-1),(2,-1)),((0,-3),(1,-3))],
 [((-2,-2),(-2,2)),((-2,2),(2,0)),((2,0),(-2,-2)),((0,-1),(0,2))],
 [((-2,1),(0,3)),((0,3),(2,1)),((0,2),(0,-3)),((-2,-1),(2,-1))],
 [((-2,-2),(2,-2)),((2,-2),(-1,2)),((-1,2),(2,2)),((0,-1),(2,0))],
 [((-2,0),(0,-2)),((0,-2),(2,0)),((0,-2),(0,3)),((-1,2),(1,2))],
 [((-2,-2),(-2,2)),((-2,0),(2,0)),((2,-2),(2,2)),((-1,-3),(1,-3))]
]
def rune(x,y,angle,k,col,scale=1):
    ca=math.cos(angle);sa=math.sin(angle)
    def tr(p):return ip((x+scale*(p[0]*ca-p[1]*sa),y+scale*(p[0]*sa+p[1]*ca)))
    for p,q in GLYPHS[k%len(GLYPHS)]:
        P=tr(p);Q=tr(q);c.line(P[0]+1,P[1]+1,Q[0]+1,Q[1]+1,G[2]);c.line(*P,*Q,col)
for i in range(32):
    t=i*2*math.pi/32+.045;p=pt(CX,CY,75,t)
    rune(*p,t+math.pi/2,i,T[5] if i%4==0 else (T[3] if i%4==1 else G[7]))
# Tiny paired rivets, clamps and cardinal mounting blocks.
for i in range(12):
    t=i*math.pi/6
    for r in [69,82]:
        x,y=ip(pt(CX,CY,r,t));c.circle(x,y,1,G[1]);c.set(x,y-1,G[8]);c.set(x,y,G[5])
for t in [0,math.pi/2,math.pi,3*math.pi/2]:
    p=pt(CX,CY,83,t);q=pt(CX,CY,87,t)
    linew(*p,*q,11,INK);linew(*p,*q,7,G[5]);linew(p[0]-1,p[1]-1,q[0]-1,q[1]-1,3,G[8])
# Main bearing axles with visible screw slots.
for x in [43,213]:
    c.circle(x,102,8,INK);c.circle(x,102,6,G[3]);c.circle(x-1,101,4,G[6]);c.circle(x-1,101,2,G[2]);c.line(x-2,100,x,102,STONE[5]);c.set(x-3,99,G[9])
# A gothic compass crown, and a plumb-shaped counterweight beneath the machine.
polyoutline([(119,20),(121,14),(125,14),(128,5),(131,14),(135,14),(137,20),(133,25),(123,25)],G[4])
c.line(128,8,128,20,G[9]);c.line(121,18,135,18,G[7]);c.circle(128,20,4,INK);c.circle(128,20,2,T[4]);c.set(127,19,T[7])
polyoutline([(122,181),(134,181),(135,187),(131,191),(128,198),(125,191),(121,187)],G[3])
c.poly([(124,183),(128,185),(128,195),(125,190)],G[7]);c.line(123,181,133,181,G[8]);c.set(128,190,T[5])
# Mechanical frame arms, beveled and engraved.
for t in [math.radians(36),math.radians(137),math.radians(222),math.radians(306)]:
    p=pt(CX,CY,23,t);q=pt(CX,CY,63,t)
    linew(*p,*q,8,INK);linew(*p,*q,5,G[4]);linew(p[0]-1,p[1]-1,q[0]-1,q[1]-1,2,G[7]);linew(*pt(CX,CY,31,t),*pt(CX,CY,54,t),1,G[1])
    bx,by=ip(pt(CX,CY,47,t));c.circle(bx,by,3,INK);c.circle(bx,by,2,G[6]);c.set(bx-1,by-1,G[9]);c.set(bx,by,G[2])

def gear(x,y,r,n=14,phase=0):
    # A true toothed silhouette, pierced spokes, inner race and slotted axle.
    points=[]
    for i in range(n):
        for f,rr in [(0,.84),(.17,1),(.62,1),(.8,.84)]:
            points.append(pt(x,y,r*rr,phase+2*math.pi*(i+f)/n))
    polyoutline(points,G[5])
    c.poly([ip(p) for p in points],G[1],fill=False)
    # Individual tooth top facets.
    for i in range(n):
        t=phase+(i+.35)*2*math.pi/n
        p=pt(x,y,r*.89,t);q=pt(x,y,r*.98,t)
        c.line(*ip(p),*ip(q),G[8] if math.sin(t)<.3 else G[3])
    c.circle(x,y,max(2,round(r*.73)),G[2])
    c.circle(x,y,max(2,round(r*.64)),G[6])
    c.circle(x,y,max(1,round(r*.5)),INK)
    for i in range(5 if r>13 else 4):
        t=phase+i*2*math.pi/(5 if r>13 else 4)
        p=pt(x,y,r*.19,t);q=pt(x,y,r*.6,t)
        linew(*p,*q,3 if r>13 else 2,G[4]);c.line(*ip((p[0]-1,p[1]-1)),*ip((q[0]-1,q[1]-1)),G[7])
    c.circle(x,y,max(2,round(r*.22)),G[2]);c.circle(x-1,y-1,max(1,round(r*.15)),G[7]);c.line(x-2,y-1,x,y+1,INK)
    if r>=12:
        for i in range(12):
            t=i*math.pi/6;p=ip(pt(x,y,r*.61,t));c.set(*p,G[8] if i<7 else G[4])

# The asymmetric train of interlocking wheels, largely visible through open rings.
gear(94,67,15,13,.1)
gear(109,52,9,10,.24)
gear(167,65,14,12,.2)
gear(178,87,8,10,.15)
gear(77,127,11,12,.2)
gear(83,145,20,17,.13)
gear(107,157,11,11,.34)
gear(130,164,10,12,.2)
gear(164,146,21,18,.05)
gear(182,125,10,11,.15)
# Separate alchemical dials mounted over two of the gear hubs.
def dial(x,y,r,kind=0):
    c.circle(x+1,y+2,r+1,INK)
    ring(x,y,r,r-3)
    c.circle(x,y,r-4,STONE[0])
    c.circle(x,y,r-5,T[1],fill=False)
    for i in range(24):
        t=i*math.pi/12
        p=ip(pt(x,y,r-4,t));q=ip(pt(x,y,r-(6 if i%3==0 else 5),t))
        c.line(*p,*q,G[7] if i%3==0 else G[3])
    if kind==0:
        c.poly([ip(pt(x,y,r-6,-math.pi/2+i*math.pi*2/3)) for i in range(3)],T[3],fill=False)
        c.circle(x,y,4,T[2],fill=False);c.line(x,y-7,x,y+7,G[7]);c.line(x-3,y+4,x+3,y+4,G[7])
    elif kind==1:
        for off in [0,math.pi]:
            c.poly([ip(pt(x,y,r-6,-math.pi/2+off+i*math.pi*2/3)) for i in range(3)],G[6],fill=False)
        c.circle(x,y,4,T[3],fill=False)
        c.line(x-7,y+3,x+6,y-6,T[5]);c.circle(x,y,1,G[9])
    else:
        c.circle(x,y,4,G[6],fill=False);c.line(x-4,y-5,x+5,y+4,G[7]);c.line(x-2,y+6,x+5,y-4,T[4])
    c.set(x-1,y-1,T[6])
dial(83,145,13,0)
dial(164,146,14,1)
dial(167,65,9,2)
# Small exposed pinions, silver screws, and copper capillary conduits.
for x,y,r in [(103,121,7),(151,91,7),(116,66,6),(145,155,5),(68,101,6)]:gear(x,y,r,8,.18)
for path in ['M 86 133 L 86 121 L 99 113','M 172 133 L 176 116 L 164 107','M 103 71 L 110 78 L 110 87','M 148 153 L 146 139 L 140 134']:
    c.path(path,G[2],fill=False)
for path in ['M 85 133 L 85 120 L 98 112','M 171 132 L 175 116 L 163 107','M 102 71 L 109 79 L 109 87','M 147 153 L 145 140 L 139 135']:
    c.path(path,G[7],fill=False)
# The central radiant reactor, surrounded by alternating cage teeth and a runic race.
for y in range(71,134):
    for x in range(97,160):
        rr=math.hypot(x-CX,y-CY)
        if rr<30 and rr>21:
            if rr<24:col=A[1]
            elif rr<27:col=G[1]
            else:col=BG[4] if (x+y)%2 else G[1]
            c.set(x,y,col)
for i in range(16):
    t=i*math.pi/8;p=pt(CX,CY,23,t);q=pt(CX,CY,28,t)
    linew(*p,*q,4,INK);linew(*p,*q,2,G[6]);c.set(*ip(q),G[8])
ring(CX,CY,26,21)
for i in range(12):
    t=i*math.pi/6;p=pt(CX,CY,23.2,t)
    c.set(*ip(p),T[5]);c.set(*ip(pt(CX,CY,23.2,t+.035)),T[3])
# The sunburst is faceted and stepped, not anti-aliased.
sun=[]
for i in range(32):
    t=i*math.pi/16;rr=21 if i%4==0 else (17 if i%2==0 else 12)
    sun.append(pt(CX,CY,rr,t))
polyoutline(sun,A[3])
c.poly([ip(pt(CX,CY,18 if i%2==0 else 10,i*math.pi/8)) for i in range(16)],A[5])
c.circle(CX,CY,14,A[2]);c.circle(CX,CY,12,A[4]);c.circle(CX-1,CY-1,10,A[5]);c.circle(CX-2,CY-2,7,A[6])
c.poly([(125,92),(131,97),(133,104),(128,112),(123,106),(121,100)],G[9])
c.poly([(126,94),(131,101),(128,108),(124,102)],'#ffffe4')
c.line(116,102,140,102,A[6]);c.line(128,90,128,114,A[6])
c.rect(125,98,6,7,'#ffffee');c.line(123,99,133,99,'#ffffee')
# Four little jewel-cage prongs catch the brilliance.
for t in [math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4]:
    p=pt(CX,CY,18,t);q=pt(CX,CY,13,t)
    linew(*p,*q,3,G[2]);linew(p[0]-.6,p[1]-.6,q[0]-.6,q[1]-.6,1,G[9])
# The near halves cross OVER the body, making the spatial gyroscope legible.
orbit(*O2,front=True)
orbit(*O1,front=True)
# The lower sweep carries a second sequence of luminous inlaid glyphs.
for i,t in enumerate([.17,.34,.51,.70,.91,1.16,1.40,1.65,1.88,2.12,2.36,2.59,2.81,3.00]):
    x,y=orbitpoint(*O1[:5],t)
    p=orbitpoint(*O1[:5],t+.01)
    angle=math.atan2(p[1]-y,p[0]-x)
    rune(x,y,angle,i+3,T[5] if i%3==0 else T[3],.65)
# Two small bearing collars on the front arc.
for O,t in [(O1,1.05),(O1,2.12),(O2,1.45)]:
    x,y=ip(orbitpoint(*O[:5],t))
    c.circle(x,y,4,INK);c.circle(x,y,3,G[5]);c.circle(x-1,y-1,1,G[9]);c.set(x+1,y+1,G[2])

# Crystal satellites, cut into polygonal facets and held by brass claws.
def crystal(x,y,r,pal,phase=0):
    # Small ordered-dither aureole around each, using already dark palette colours.
    for yy in range(max(0,y-r-5),min(256,y+r+6)):
        for xx in range(max(0,x-r-5),min(256,x+r+6)):
            d=math.hypot(xx-x,yy-y)
            if r+1<d<r+5 and (xx+2*yy)%4==0:c.set(xx,yy,pal[0])
    c.circle(x,y+2,r+2,INK)
    c.circle(x,y,r+1,INK)
    N=10
    outer=[pt(x,y,r,-math.pi/2+i*math.pi*2/N) for i in range(N)]
    inner=[pt(x-1,y-1,r*.52,-math.pi/2+i*math.pi*2/N) for i in range(N)]
    c.poly([ip(p) for p in outer],pal[2])
    for i in range(N):
        j=(i+1)%N
        bright=[4,3,2,1,1,2,3,4,5,5][i]
        c.poly([ip(outer[i]),ip(outer[j]),ip(inner[j]),ip(inner[i])],pal[min(bright,len(pal)-1)])
    # Asymmetrical central prism, with opposed saturated facets.
    c.poly([ip(p) for p in inner],pal[4])
    c.poly([ip(inner[8]),ip(inner[0]),ip(inner[2]),(x+2,y),(x-3,y+2)],pal[5])
    c.poly([(x+2,y),ip(inner[2]),ip(inner[4]),ip(inner[5]),(x-1,y+2)],pal[3])
    c.line(*ip(outer[8]),*ip(inner[8]),pal[6]);c.line(*ip(inner[8]),*ip(inner[0]),pal[6])
    c.line(*ip(inner[0]),*ip(inner[2]),pal[5]);c.line(*ip(inner[5]),*ip(outer[5]),pal[4])
    c.line(x-r+3,y-3,x-2,y-r+3,pal[6])
    c.rect(x-r//3,y-r//2,3,2,pal[-1]);c.set(x-r//3-1,y-r//2+2,pal[5])
    # Opposing little golden mounts, with black gaps against the crystal.
    for s in [-1,1]:
        c.line(x+s*(r-1),y+2,x+s*(r+2),y+4,G[2])
        c.line(x+s*(r-1),y+1,x+s*(r+1),y+3,G[7])
        c.set(x+s*(r+1),y+2,G[9])
    if r>=9:
        sx=x-r//2;sy=y-r//2
        c.line(sx-3,sy,sx+3,sy,pal[-1]);c.line(sx,sy-3,sx,sy+3,pal[-1]);c.set(sx+1,sy+1,pal[-1])

# The large blue orb and the amethyst at the upper pole are the strongest satellites.
crystal(212,74,12,BLUE)
crystal(96,24,10,V)
crystal(50,149,9,T)
crystal(157,181,8,A)
# A tiny moon in a secondary epicycle.
ring(183,48,9,7)
crystal(183,48,5,BLUE)
# Suspended star sparks and a few specs of dust lit by the core.
def sparkle(x,y,col,sz=2):
    c.line(x-sz,y,x+sz,y,col);c.line(x,y-sz,x,y+sz,col)
    if sz>2:c.set(x-1,y-1,col)
for x,y,col,sz in [(225,69,BLUE[4],2),(104,16,V[4],2),(45,139,T[3],2),(169,185,A[4],2),(125,72,A[4],1),(149,110,A[5],1)]:sparkle(x,y,col,sz)
for i in range(60):
    x=rng.randint(30,226);y=rng.randint(12,211)
    d=math.hypot(x-128,y-102)
    if d>89 and rng.random()<.65:
        c.set(x,y,[BG[5],G[3],T[1]][i%3])
# Polished directional streaks on the outer rim, kept broken and pixel-sharp.
for r,s,e in [(83,3.65,3.92),(81,4.1,4.35),(80,4.66,4.83),(70,5.55,5.75)]:arc(CX,CY,r,s,e,G[9] if r>80 else G[7])

# Local, quantised reflections bind the lighting to the brass rather than
# spreading an airbrushed glow across the dark outlines. All tones are finite.
WARM=['#3d2820','#634027','#926033','#bd8a47','#ddb266','#f1ce84','#ffe6a9','#fff4d2']
COOL=['#173038','#234b51','#357078','#52949a','#77b7b8','#a2d6cd','#d2efdc','#eff8de']
AMETHYST=['#302638','#514052','#76586a','#9c788a','#b99ba6','#dabdc2','#ecd5d5','#fae5da']
gidx={c.color(col):i for i,col in enumerate(G[1:9])}
widx=[c.color(col) for col in WARM]
bidx=[c.color(col) for col in COOL]
vidx=[c.color(col) for col in AMETHYST]
bgidx={c.color(col):i for i,col in enumerate(BG[:6])}
stoneidx={c.color(col):i for i,col in enumerate(STONE[:7])}
REFSTONE=['#193039','#293e47','#3b5158','#526568','#677b7b','#82918d','#a6aba0']
sidx=[c.color(col) for col in REFSTONE]
# Static pixel pattern to keep reflected light transitions crisp and ordered.
bayer=[[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]]
for y in range(256):
    for x in range(256):
        old=c.get(x,y)
        if old in gidx:
            i=gidx[old]
            core=math.hypot(x-128,y-102)
            blue=math.hypot(x-212,y-74)
            violet=math.hypot(x-96,y-24)
            green=math.hypot(x-50,y-149)
            if core<47:
                # Raised inner teeth are hot with light from the central sun.
                amount=min(1,(48-core)/19)
                if bayer[y%4][x%4]<amount*16:c.set(x,y,widx[min(7,i+int(core<30))])
            elif min(blue,green)<28:
                d=min(blue,green);amount=min(1,(29-d)/12)
                if bayer[y%4][x%4]<amount*16:c.set(x,y,bidx[i])
            elif violet<25:
                amount=min(1,(26-violet)/10)
                if bayer[y%4][x%4]<amount*16:c.set(x,y,vidx[i])
        elif old in bgidx and 50<x<204 and 26<y<180:
            r=math.hypot(x-128,y-102)
            if 26<r<43:
                i=bgidx[old]
                if bayer[y%4][x%4]<(43-r)/17*10:
                    c.set(x,y,[BG[3],BG[3],BG[4],BG[5],G[1],G[1]][i])
        elif old in stoneidx and 195<y<222:
            # The levitation seal gives the top of the altar a cold reflected rim.
            d=math.sqrt(((x-128)/1.6)**2+((y-202)*2)**2)
            if d<35 and bayer[y%4][x%4]<(35-d)/35*16:
                c.set(x,y,sidx[stoneidx[old]])
# Crisp glints, two-stage highlights and light falling into the screw heads.
for x,y in [(109,79),(146,83),(101,112),(147,125)]:
    if 0<=x<256 and 0<=y<256:
        c.set(x,y,G[9]);c.set(x+1,y,A[4])
# Beam motes kept sparse so the open negative spaces remain readable.
for x,y in [(60,31),(57,26),(69,40),(76,50),(62,45),(154,192),(139,191),(115,195),(156,204),(100,207)]:
    if y<100:c.set(x,y,STONE[3])
    else:c.set(x,y,T[2])

print(c.stats_text())
print(c.matrix_text(region=(111,89,145,114)))
# Coarse value thumbnail for inspecting composition through the text-only channel.
w,h,data=c.to_rgba();arr=np.frombuffer(data,dtype=np.uint8).reshape(h,w,4)
chars=' .:-=+*#%@'
print('VALUE THUMBNAIL')
for yy in range(0,256,4):
    s=''
    for xx in range(0,256,4):
        tile=arr[yy:yy+4,xx:xx+4,:3]
        lum=tile[:,:,0]*.2126+tile[:,:,1]*.7152+tile[:,:,2]*.0722
        val=float(np.percentile(lum,75))
        s+=chars[min(9,int(val/255*10))]
    print(s)
result=c
save('aureate_engine',result)
finish(result)
