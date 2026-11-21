import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
arr = np.array(rgba).reshape(h,w,4)

# ---- 1. Remove the character (warm-coloured blob in the middle) ----
r,g,b,a = arr[...,0].astype(int),arr[...,1].astype(int),arr[...,2].astype(int),arr[...,3]
warm = (r>60)&(r>b+15)&(r>g+5)
# restrict to character zone
zone = np.zeros_like(warm)
zone[55:150, 40:125] = True
warm &= zone
# dilate by 3
def dil(m,rad):
    out=m.copy()
    for dy in range(-rad,rad+1):
        for dx in range(-rad,rad+1):
            if dx*dx+dy*dy>rad*rad: continue
            out |= np.roll(np.roll(m,dy,0),dx,1)
    return out
cmask = dil(warm,3)

# inpaint: for each removed pixel, take nearest non-removed pixel colour (scan left/right)
res = arr.copy()
H,W = cmask.shape
ys,xs = np.where(cmask)
for y,x in zip(ys,xs):
    # search outward horizontally
    for d in range(1,W):
        for xx in ((x-d,),(x+d,)):
            xx=xx[0]
            if 0<=xx<W and not cmask[y,xx]:
                res[y,x]=arr[y,xx]; break
        else:
            continue
        break
c2 = c.copy(name="work")
from pixelbench_api import new_canvas
# write pixels back
for y in range(H):
    for x in range(W):
        if cmask[y,x]:
            rr,gg,bb,aa = res[y,x]
            c2.set(x,y,(int(rr),int(gg),int(bb),int(aa)))

# ---- 2. Wet ground: droplets / shine on lower part ----
rng = np.random.RandomState(7)
wet_blue=(90,140,160,110)
wet_dark=(30,60,80,120)
for i in range(260):
    x=rng.randint(0,170); y=rng.randint(120,170)
    if rng.rand()<0.5:
        c2.set(x,y,wet_blue)
        if rng.rand()<0.5: c2.set(x+1,y,wet_blue)
    else:
        c2.set(x,y,wet_dark)
# horizontal wet streaks
for i in range(40):
    x=rng.randint(0,160); y=rng.randint(120,170); ln=rng.randint(3,10)
    for k in range(ln):
        c2.set(min(169,x+k),y,(120,160,180,70))

# ---- 3. Lightning in the background (sky, upper area) ----
bolt=(240,240,220,235)
glow=(120,130,150,120)
def bolt_path(x0,y0,x1,y1,jag,segs):
    pts=[(x0,y0)]
    for i in range(1,segs):
        t=i/segs
        px=x0+(x1-x0)*t+rng.randint(-jag,jag)
        py=y0+(y1-y0)*t
        pts.append((int(px),int(py)))
    pts.append((x1,y1))
    return pts
# main bolt
pts=bolt_path(120,0,95,55,8,8)
for i in range(len(pts)-1):
    c2.line(*pts[i],*pts[i+1],bolt)
# branches
p2=bolt_path(pts[3][0],pts[3][1],pts[3][0]+22,pts[3][1]+18,6,4)
for i in range(len(p2)-1):
    c2.line(*p2[i],*p2[i+1],(200,205,200,200))
p3=bolt_path(pts[5][0],pts[5][1],pts[5][0]-20,pts[5][1]+15,6,4)
for i in range(len(p3)-1):
    c2.line(*p3[i],*p3[i+1],(200,205,200,200))
# glow around bolt
for (px,py) in pts:
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        c2.set(px+dx,py+dy,glow)
# second faint bolt
pts2=bolt_path(40,0,55,40,7,6)
for i in range(len(pts2)-1):
    c2.line(*pts2[i],*pts2[i+1],(190,195,190,150))

# ---- 4. Rain: semi-transparent droplets ----
rain=(170,200,220,110)
rain2=(140,180,205,90)
for i in range(900):
    x=rng.randint(0,170); y=rng.randint(0,170)
    ln=rng.randint(2,5)
    col = rain if rng.rand()<0.6 else rain2
    for k in range(ln):
        c2.set(x,y+k,col)

result = c2
print(result.stats_text())
finish(result)
