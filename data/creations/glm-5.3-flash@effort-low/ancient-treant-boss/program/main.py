from pixelbench_api import *
import random

random.seed(11)
W = H = 256

# ---------- palette ----------
C = {}
def reg(name, hexv):
    C[name] = c0.color(hexv, name=name)

c0 = new_canvas(W, H, None, name="base")  # just to register palette
names = {
 "sky_top":"#08120c", "sky_mid":"#0e2214", "sky_low":"#16321b",
 "ray":"#3f6b35", "ray2":"#57854a",
 "far_tree":"#0c1f11", "far_tree2":"#122b17",
 "ground_d":"#15240f", "ground":"#1e3213", "ground_l":"#2b4519",
 "moss_g":"#3f5c22", "moss_l":"#5a7a2e",
 "bark_d":"#1d1409", "bark":"#332413", "bark_l":"#4a3620", "bark_hl":"#5f4830",
 "leaf_d":"#16300f", "leaf":"#234a16", "leaf_l":"#35651f",
 "eye":"#7dff5a", "eye_c":"#d9ffb2",
 "outline":"#060c07",
 "vine":"#2f5420", "root":"#2a1d0f", "root_l":"#3d2b17",
 "mist":"#2c4a2a",
}
for k,v in names.items(): reg(k,v)

# ---------- layer 1: sky ----------
sky = new_canvas(W,H,None,"sky")
def lerp(a,b,t):
    return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
top=(8,18,12); mid=(14,34,20); low=(22,50,27)
for y in range(H):
    if y<130: col=lerp(top,mid,y/130)
    else: col=lerp(mid,low,(y-130)/126)
    sky.rect(0,y,W,1,col)

# god rays (separate translucent layer)
rays = new_canvas(W,H,None,"rays")
for (x0,slope,w,alpha) in [(150,1.6,14,"#57854a30"),(185,1.6,10,"#57854a26"),
                           (120,1.6,18,"#57854a22"),(210,1.6,8,"#57854a2c"),
                           (95,1.6,12,"#57854a1e")]:
    pts=[]
    for y in range(0,H,4):
        pts.append((x0+slope*y, y))
    for i,(px,py) in enumerate(pts):
        rays.rect(int(px),py,w,4,alpha)

# distant forest silhouettes
far = new_canvas(W,H,None,"far")
for i in range(26):
    x = random.randint(-5,W)
    h = random.randint(60,120)
    w = random.randint(8,18)
    col = C["far_tree"] if i%2 else C["far_tree2"]
    far.rect(x,205-h,w,h,col)
    for j in range(3):
        far.ellipse(x+w//2+random.randint(-6,6), 205-h-random.randint(0,10),
                    random.randint(6,12), random.randint(5,9), col)
# canopy vignette top
for i in range(40):
    far.ellipse(random.randint(0,W), random.randint(-8,26), random.randint(10,22),
                random.randint(6,12), C["far_tree"])
for i in range(24):
    far.ellipse(random.randint(0,W), random.randint(20,48), random.randint(8,16),
                random.randint(5,9), C["far_tree2"])

# mist band
mist = new_canvas(W,H,None,"mist")
for y in range(185,215):
    a = int(40*abs(y-200)/15)
    mist.rect(0,y,W,1,(44,74,42,max(0,40-a)))

# ---------- ground ----------
ground = new_canvas(W,H,None,"ground")
ground.rect(0,205,W,51,C["ground"])
ground.rect(0,205,W,3,C["ground_l"])
for i in range(500):
    x=random.randint(0,W-1); y=random.randint(206,H-1)
    r=random.random()
    col = C["ground_d"] if r<0.45 else (C["ground_l"] if r<0.8 else C["moss_g"])
    ground.set(x,y,col)
# small ferns / tufts
for i in range(26):
    x=random.randint(2,W-3); y=random.randint(210,250)
    for dx in (-2,-1,0,1,2):
        ground.line(x,y, x+dx, y-random.randint(2,4), C["moss_g"] if dx%2 else C["moss_l"])

# ---------- treant ----------
t = new_canvas(W,H,None,"treant")
O=C["outline"]; BD=C["bark_d"]; BK=C["bark"]; BL=C["bark_l"]; BH=C["bark_hl"]

# trunk body polygon (drawn dark then lit)
body=[(116,64),(146,64),(152,110),(162,160),(172,205),(184,238),(84,238),
      (96,205),(104,160),(112,110)]
t.poly(body, BK)
# shading: left dark edge, right light edge
t.poly([(116,64),(112,110),(104,160),(96,205),(84,238),(100,238),(110,200),
        (118,155),(124,105),(124,64)], BD)
t.poly([(146,64),(152,110),(162,160),(172,205),(184,238),(166,238),(158,200),
        (148,155),(140,105),(140,64)], BL)
# bark ridges (vertical cracks)
for x0 in (128,134,141,120,147):
    y0=random.randint(70,80); y1=random.randint(190,225)
    xx=x0
    for y in range(y0,y1,3):
        t.set(xx,y,BD)
        if random.random()<0.4: xx+=random.choice((-1,0,1))
# knot
t.ellipse(133,150,4,5,BD); t.ellipse(133,150,2,3,BK)

# head: gnarled branch crown
hx,hy=131,58
t.rect(hx-9,hy,18,12,BK)  # head block
t.rect(hx-9,hy,4,12,BD); t.rect(hx+5,hy,4,12,BL)
# horns / crown branches
for (dx,ang) in [(-14,-2.2),(-7,-2.7),(0,-3.14),(7,2.7),(14,2.2)]:
    import math
    x1,y1=hx+dx//2, hy-2
    x2=x1+int(dx*1.4); y2=hy-14-abs(dx)//3
    t.line(x1,y1,x2,y2,BK)
    t.line(x1+1,y1,x2+1,y2,BL if dx>0 else BD)
    t.line(x2,y2,x2+random.randint(-3,3),y2-4,BK)
# foliage clumps on crown
for (fx,fy,r) in [(105,44,9),(118,36,10),(131,32,11),(145,36,10),(158,44,9),
                  (112,50,7),(150,50,7)]:
    t.ellipse(fx,fy,r,int(r*0.75),C["leaf_d"])
for (fx,fy,r) in [(112,42,7),(126,35,8),(140,36,8),(153,44,6)]:
    t.ellipse(fx,fy,r,int(r*0.7),C["leaf"])
for (fx,fy) in [(110,40),(124,33),(139,34),(151,42),(131,30)]:
    t.ellipse(fx,fy,3,2,C["leaf_l"])

# arms: left (viewer left) raised, right lowered forward
def limb(pts, w, col_main, col_edge):
    for i in range(len(pts)-1):
        (x0,y0),(x1,y1)=pts[i],pts[i+1]
        t.line(x0,y0,x1,y1,col_main)
        for k in range(1,w):
            t.line(x0,y0+k,x1,y1+k,col_main)
        t.line(x0,y0,x1,y1,col_edge)
        t.line(x0,y0+w-1,x1,y1+w-1,col_edge)

# left arm: shoulder (114,105) -> out-up to elbow (72,86) -> up to hand (52,58)
limb([(116,104),(88,92),(66,74),(54,58)],7,BK,BD)
# right arm: shoulder (150,108) -> out-down (196,120) -> hand (216,140)
limb([(148,106),(180,114),(204,128),(218,142)],7,BK,BL)
# twig claws
def claws(cx,cy,dxs,up=True):
    for dx in dxs:
        L=random.randint(7,12)
        t.line(cx+dx,cy, cx+dx+random.randint(-2,2), cy-L, BK)
        t.line(cx+dx+1,cy, cx+dx+2, cy-L+2, BD)
claws(54,58,(-6,-2,2,6))
claws(218,142,(-2,3,8,13))
# extra gnarly twigs off arms
for (ax,ay,dx,dy) in [(84,92,-4,-8),(70,80,-3,-7),(186,114,5,-6),(198,124,4,-7)]:
    t.line(ax,ay,ax+dx,ay+dy,BK)

# hanging vines from arms and crown
for (vx,vy,vl) in [(70,80,26),(88,96,20),(60,62,18),(196,118,24),(206,132,18),
                   (110,44,16),(150,46,14),(131,26,12)]:
    xx=vx
    for y in range(vy,vy+vl):
        t.set(xx,y,C["vine"])
        if random.random()<0.35: xx+=random.choice((-1,1))
        if y==vy+vl-1: t.set(xx,y+1,C["moss_l"])

# glowing eyes in trunk
for ex in (123,139):
    t.ellipse(ex,92,4,3,C["eye"])
    t.ellipse(ex,92,2,2,C["eye_c"])
# angry brow cracks
t.line(118,86,127,89,BD); t.line(144,86,135,89,BD)
# jagged mouth crack
t.line(122,106,127,109,BD); t.line(127,109,133,106,BD); t.line(133,106,139,109,BD)
t.line(124,112,138,112,BD)

# moss patches on trunk
for (mx,my,r) in [(112,120,5),(150,130,6),(120,175,7),(146,190,6),(104,150,4),
                  (160,165,5),(134,215,6),(96,190,4)]:
    t.ellipse(mx,my,r,int(r*0.6),C["moss_g"])
    t.ellipse(mx-1,my-1,max(1,r-3),1,C["moss_l"])

# roots rising from ground
def root(pts,w):
    for i in range(len(pts)-1):
        (x0,y0),(x1,y1)=pts[i],pts[i+1]
        t.line(x0,y0,x1,y1,C["root"])
        for k in range(1,w): t.line(x0,y0+k,x1,y1+k,C["root"])
        t.line(x0,y0,x1,y1,C["root_l"])
root([(96,232),(74,238),(52,246),(30,252)],5)
root([(168,232),(192,238),(214,246),(236,252)],5)
root([(104,236),(92,246),(80,254)],4)
root([(160,236),(172,246),(184,254)],4)
root([(120,238),(114,250),(108,255)],3)
root([(146,238),(152,250),(158,255)],3)
# root knuckles
for (kx,ky) in [(52,244),(214,244),(80,252),(184,252)]:
    t.ellipse(kx,ky,3,2,C["root_l"])

# dark outline around treant silhouette
t.outline(C["outline"])

# ---------- composite ----------
scene = flatten([sky, rays, far, mist, ground, t], name="scene", background="#08120c")

# glow around eyes on the composite
for ex in (123,139):
    scene.ellipse(ex,92,6,5,"#7dff5a20")
    scene.ellipse(ex,92,8,7,"#7dff5a12")

# foreground silhouette grass at very bottom for depth
for i in range(60):
    x=random.randint(0,W-1)
    h=random.randint(3,9)
    scene.rect(x,255-h,1,h,C["outline"] if i%3 else C["ground_d"])

print(scene.stats_text())
save("ancient-treant-boss", scene, indexed=True)
finish(scene)
