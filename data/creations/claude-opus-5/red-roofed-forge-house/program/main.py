c = new_canvas(128, 128, name="output")

# ---- palette ----
GR1="#5d8f45"; GR2="#4a7a37"; GR3="#3b6029"
SOIL="#6d5338"; SOIL2="#56402b"
W1="#c9a97a"; W2="#a98a5e"; W3="#846844"; W4="#5e4a30"   # plaster/wood walls
ST1="#8d8d93"; ST2="#6e6e76"; ST3="#52525a"              # stone base
R1="#e05b3a"; R2="#c14328"; R3="#9a301c"; R4="#f08a5d"   # red tiles
RD="#6d1f12"
WD1="#8b5a2b"; WD2="#6b4320"; WD3="#4a2d14"; WD4="#a9713a"
G1="#ffe9a8"; G2="#ffb13d"; G3="#ff6a1f"; G4="#8a2a08"
SM1="#b9bcc4"; SM2="#8e929b"
BLK="#2a1f18"
OUT="#2b2119"

def lerp(a,b,t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
def I(p): return (int(round(p[0])), int(round(p[1])))

# ---- ground ----
c.poly([(64,36),(122,66),(64,120),(6,90)], GR2)
c.poly([(64,40),(118,68),(64,116),(10,88)], GR1)
# dirt yard patch
c.poly([(64,56),(108,78),(64,108),(20,86)], SOIL)
c.poly([(64,60),(104,80),(64,104),(24,84)], SOIL2)

# ---- geometry ----
L=(22,86); T=(64,64); R=(106,86); B=(64,108)
H=24
Lp=(22,62); Tp=(64,40); Rp=(106,62); Bp=(64,84)

# stone foundation
c.poly([(20,88),(64,110),(64,100),(20,78)], ST3)
c.poly([(64,110),(108,88),(108,78),(64,100)], ST2)
c.poly([(20,78),(64,100),(108,78),(64,56)], ST1)

# walls
c.poly([L,B,Bp,Lp], W2)      # front-left face
c.poly([B,R,Rp,Bp], W1)      # front-right face

# timber framing on left face
for s in (0.0,0.25,0.5,0.75,1.0):
    a=I(lerp(L,B,s)); b=I(lerp(Lp,Bp,s))
    c.line(a[0],a[1],b[0],b[1],W3)
for s in (0.0,0.5,1.0):
    a=I(lerp(T,R,0)); 
for k in (0,1):
    pass
c.line(22,62,64,84,W3); c.line(22,74,64,96,W3)
# right face framing
for s in (0.25,0.5,0.75):
    a=I(lerp(B,R,s)); b=I(lerp(Bp,Rp,s))
    c.line(a[0],a[1],b[0],b[1],W2)
c.line(64,84,106,62,W2); c.line(64,96,106,74,W2)

# gable triangles (above wall top)
rA=(43,31); rB=(85,53)
c.poly([Lp,Tp,rA], W3)
c.poly([Bp,Rp,rB], W2)
c.poly([Lp,Tp,rA], W3, fill=False)

# ---- door with furnace glow (front-left face) ----
d1=(35,93); d2=(46,99)
c.poly([d1,d2,(46,80),(35,74)], BLK)
c.poly([(36,91),(45,96),(45,80),(36,75)], G4)
c.poly([(37,90),(44,94),(44,81),(37,77)], G3)
c.poly([(38,88),(43,91),(43,82),(38,79)], G2)
c.poly([(39,87),(42,88),(42,83),(39,81)], G1)
# glow spill on ground
c.poly([(33,95),(48,103),(52,100),(36,92)], G4)
c.poly([(35,95),(47,101),(49,99),(37,93)], G3)

# ---- forge window (front-right face) ----
c.poly([(79,100),(90,94),(90,81),(79,87)], WD3)
c.poly([(81,98),(88,94),(88,83),(81,87)], G4)
c.poly([(82,96),(87,93),(87,84),(82,88)], G2)
c.poly([(83,94),(86,92),(86,86),(83,88)], G1)

# small upper window left face
c.poly([(26,78),(32,81),(32,72),(26,69)], WD3)
c.poly([(27,78),(31,80),(31,73),(27,71)], G3)

# ---- roof ----
oA_L=(17,65); oA_B=(66,91)     # overhanging eave, slope A (front-left)
oB_T=(66,37); oB_R=(111,59)    # eave slope B (back-right)
slopeA=[oA_L,oA_B,rB,rA]
slopeB=[oB_T,oB_R,rB,rA]
c.poly(slopeA, R2)
c.poly(slopeB, R3)

# tiles slope A
for i in range(9):
    t=i/8.0
    a=I(lerp(oA_L,rA,t)); b=I(lerp(oA_B,rB,t))
    col = R1 if i%2==0 else R2
    c.line(a[0],a[1],b[0],b[1],col)
for i in range(9):
    t=(i+0.5)/8.0
    if t>1: break
    a=I(lerp(oA_L,rA,t)); b=I(lerp(oA_B,rB,t))
    c.line(a[0],a[1],b[0],b[1],RD)
# vertical tile seams slope A
for j in range(1,8):
    s=j/8.0
    a=I(lerp(oA_L,oA_B,s)); b=I(lerp(rA,rB,s))
    c.line(a[0],a[1],b[0],b[1],RD)

# tiles slope B (darker, back side)
for i in range(7):
    t=i/6.0
    a=I(lerp(oB_T,rA,t)); b=I(lerp(oB_R,rB,t))
    col = R2 if i%2==0 else R3
    c.line(a[0],a[1],b[0],b[1],col)
for j in range(1,8):
    s=j/8.0
    a=I(lerp(oB_T,oB_R,s)); b=I(lerp(rA,rB,s))
    c.line(a[0],a[1],b[0],b[1],RD)

# ridge cap
c.line(rA[0],rA[1],rB[0],rB[1],R4)
c.line(rA[0],rA[1]+1,rB[0],rB[1]+1,R1)
# eave edge highlight
c.line(oA_L[0],oA_L[1],oA_B[0],oA_B[1],R4)
c.line(oA_L[0],oA_L[1]+1,oA_B[0],oA_B[1]+1,RD)

# ---- chimney ----
c.poly([(70,44),(78,48),(78,36),(70,32)], ST2)
c.poly([(78,48),(86,44),(86,32),(78,36)], ST3)
c.poly([(70,32),(78,36),(86,32),(78,28)], ST1)
c.poly([(74,32),(78,34),(82,32),(78,30)], BLK)
c.line(70,44,70,32,ST3)
# smoke
for (x,y,r,col) in [(79,24,2,SM1),(76,18,3,SM2),(80,12,3,SM1),(77,6,4,SM2)]:
    c.circle(x,y,r,col)

# ---- wooden sign ----
c.line(16,92,16,72,WD2)
c.line(17,93,17,73,WD3)
c.line(16,73,24,73,WD2)
c.poly([(18,86),(26,90),(26,78),(18,74)], WD1)
c.poly([(19,85),(25,88),(25,79),(19,76)], WD4)
c.line(21,80,23,81,WD3)
c.line(21,83,23,84,WD3)
c.set(20,75,WD3); c.set(25,77,WD3)

# ---- barrels (stacked) ----
def barrel(x,y,w,h):
    c.ellipse(x,y+h,w//2,w//4,WD2)
    c.rect(x-w//2,y,w,h,WD1)
    c.ellipse(x,y,w//2,w//4,WD4)
    c.line(x-w//2,y+h//3,x+w//2-1,y+h//3,WD3)
    c.line(x-w//2,y+2*h//3,x+w//2-1,y+2*h//3,WD3)
    c.line(x-w//2,y,x-w//2,y+h,WD3)
    c.line(x+w//2-1,y,x+w//2-1,y+h,WD2)

barrel(88,100,12,12)
barrel(100,94,12,12)
barrel(94,88,12,12)

# crate / anvil near door
c.poly([(54,104),(62,108),(62,101),(54,97)], WD2)
c.poly([(62,108),(70,104),(70,97),(62,101)], WD3)
c.poly([(54,97),(62,101),(70,97),(62,93)], WD1)

# logs
c.ellipse(28,102,3,2,WD4); c.rect(28,100,10,5,WD2); c.ellipse(38,102,3,2,WD1)

c.outline(OUT)
view(c)
finish(c)
