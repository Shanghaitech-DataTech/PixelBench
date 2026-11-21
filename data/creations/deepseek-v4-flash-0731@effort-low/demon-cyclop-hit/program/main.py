from pixelbench_api import *

src = input_canvas
w,h=37,33
PAL={1:(20,27,27),2:(255,225,141),3:(173,188,58),4:(116,163,52),5:(200,150,107),6:(252,226,202)}
DX=5
W=46
S={(x,y):PAL[src.get(x,y)] for y in range(h) for x in range(w) if src.get(x,y) in PAL}
DARK=PAL[1]
k=0.10
RED=[(196,34,58),(235,70,30),(180,28,30),(150,35,25)]

# ---------- Frame 1: original picture ----------
f1 = new_canvas(W,h,name="f1")
for (x,y),col in S.items():
    f1.set(DX+x,y,col)

# ---------- Frame 2: recoil pose ----------
f2 = new_canvas(W,h,name="f2")
for (x,y),col in S.items():
    lift = 3 if (x<=7 and y>=24) else 0
    ny=y-lift
    nx=DX+x+round(k*(h-y))
    f2.set(nx,ny,col)
px=[(x,y) for y in range(12,20) for x in range(20,44) if f2.get(x,y)==1]
for x,y in px: f2.set(x,y,'transparent')
for x,y in px:
    if y-1>=0: f2.set(x,y-1,DARK)
for y in (24,25):
    for x in range(30,40):
        if f2.get(x,y) in (3,4,5):
            f2.set(x,y,DARK)

# ---------- Frame 3: impact, red filter over monster ----------
f3 = f2.copy(name="f3")
for y in range(h):
    for x in range(W):
        cid=f3.get(x,y)
        base={1:(20,27,27),2:(255,225,141),3:(173,188,58),
              4:(116,163,52),5:(200,150,107),6:(252,226,202)}.get(cid)
        if base is not None:
            r=min(255,int(base[0]*0.80+196*0.60))
            g=int(base[1]*0.45)
            b=int(base[2]*0.40)
            f3.set(x,y,(r,g,b))
# white impact flash on torso using f2's original coloring to locate body
for yy in range(19,26):
    for xx in range(23,31):
        if f2.get(xx,yy) in (2,3,4,5):
            f3.set(xx,yy,(255,235,225))

print("f2 full")
print(f2.matrix_text(region=None))
finish([f1,f2,f3])
print("done")
