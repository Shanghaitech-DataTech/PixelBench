import math, random

rng = random.Random(11)

# ---------------- palette ----------------
CEIL="#e8eff3"; CEIL_LINE="#cfdae2"; CEIL_BASE="#c0d0da"
LIGHT="#ffffff"; GLOW="#f3fafc"
TILE_A="#edf5f8"; TILE_B="#bddfe9"; TILE_C="#a3d1df"
COL_HI="#f7fbfd"; COL_EDGE="#9bc5d3"
RIM="#f2fafc"; RIM_SH="#d7ebf2"
W0="#b2e1ee"; W1="#a1d7e7"; W2="#8fcce0"; W3="#7fc4d9"; W4="#71bbd1"
RIPL="#def3f9"; RIPD="#67acc2"; COLREF="#93cbdc"
REFL="#eefbfe"; REFS="#cdeef6"
SLIDE="#fbfdfe"; SLIDE_SH="#d8e6eb"; SLIDE_ED="#adc8d3"; MOUTH="#8aa7b3"
RING="#ffd23e"; RING_HI="#fff1a8"; RING_SH="#e8a41f"; RING_RF="#c9d28c"
SKIN="#f3c9a2"; SKIN_SH="#e0a87f"; HAIR="#4a3a2c"; HAIR_HI="#6b5644"

c = new_canvas(128, 128, background=W4, name="poolcore")

def stroke(pts, col):
    for (x0,y0),(x1,y1) in zip(pts, pts[1:]):
        c.line(x0,y0,x1,y1,col)

# ---------------- ceiling ----------------
c.rect(0,0,128,14,CEIL)
c.rect(0,12,128,1,CEIL_LINE)
c.rect(0,13,128,1,CEIL_BASE)
# fluorescent panels
for px0 in (24,64,102):
    c.rect(px0-2,2,22,8,GLOW)
    c.rect(px0,3,18,6,LIGHT)

# ---------------- back wall mosaic ----------------
for ty in range(14,58,4):
    for tx in range(0,128,4):
        col = TILE_A if ((tx//4)+(ty//4))%2==0 else TILE_B
        if rng.random()<0.045: col = TILE_C
        c.rect(tx,ty,4,4,col)

# ---------------- columns ----------------
for cx0 in (8,56,100):
    for ty in range(0,58,4):
        for i,tx in enumerate(range(cx0,cx0+10,4)):
            w = min(4, cx0+10-tx)
            col = TILE_A if (i+ty//4)%2==0 else REFS
            c.rect(tx,ty,w,4,col)
    c.rect(cx0,0,1,58,COL_HI)
    c.rect(cx0+9,0,1,58,COL_EDGE)

# ---------------- pool rim ----------------
c.rect(0,58,128,3,RIM)
c.rect(0,58,128,1,LIGHT)
c.rect(0,60,128,1,RIM_SH)

# ---------------- water ----------------
c.rect(0,61,128,10,W0)
c.rect(0,71,128,14,W1)
c.rect(0,85,128,15,W2)
c.rect(0,100,128,15,W3)
c.rect(0,115,128,13,W4)
c.rect(0,61,128,1,REFS)

# light reflections
for px0 in (24,64,102):
    c.dither(px0+2,62,16,7,[REFL,W0],"bayer4")
    c.dither(px0+4,69,12,9,[REFS,W1],"bayer4")
    for x in range(px0+3,px0+17,4):
        yend = 66 + rng.randint(14,30)
        for y in range(63,min(yend,98)):
            if (y+x)%3:
                lw = int(round(1.2*math.sin(y*0.35 + x*0.7)))
                c.set(x+lw,y,REFL)

# column reflections
for cx0 in (8,56,100):
    c.dither(cx0+1,62,8,6,[REFS,W0],"bayer4")
    for x in (cx0+2,cx0+6):
        for y in range(63,80):
            if (y*2+x)%3:
                lw = int(round(1.0*math.sin(y*0.3 + x)))
                c.set(x+lw,y,COLREF)

# ripples (sparse)
for y in range(64,127,5):
    yy = y + rng.randint(-1,1)
    for _ in range(rng.randint(1,2)):
        x0 = rng.randint(0,116)
        ln = rng.randint(3, 8 if y<100 else 12)
        col = RIPL if rng.random()<0.75 else RIPD
        c.line(x0,yy,x0+ln,yy,col)

# ---------------- water slide ----------------
top = [(-5,17),(9,20),(19,26),(26,34),(29,42),(28,50),(31,57),(38,61),(46,63)]
bot = [(47,69),(40,67),(35,60),(33,52),(33,45),(30,37),(23,31),(13,27),(-4,23)]
c.poly(top+bot, SLIDE)
c.poly(bot+[(50,72),(42,70),(36,62),(35,53)], SLIDE_SH)   # underside / thickness
c.ellipse(47,64,2,1,MOUTH)                                # mouth opening
c.line(44,62,50,63,SLIDE_ED)                              # lip
stroke([(4,19),(13,25),(21,33),(26,41),(27,49),(30,56),(37,60),(44,63)], SLIDE_SH)
c.poly(top+bot, SLIDE_ED, fill=False)

# splash
for (sx,sy) in [(41,67),(46,66),(43,69),(48,68),(40,70),(47,71),(44,71)]:
    c.set(sx,sy,LIGHT)
c.path("M 36 70 Q 45 75 54 70", RIPL, fill=False)
c.path("M 40 73 Q 46 77 52 73", REFS, fill=False)

# ---------------- girl in swim ring ----------------
c.ellipse(64,91,11,5,RING)           # ring body
c.ellipse(64,90,6,2,W2)              # hole (water inside)
c.ellipse(64,90,6,2,RING_SH,fill=False)  # inner seam
c.ellipse(64,89,5,2,SKIN_SH)         # shoulders / back shadow
c.ellipse(64,88,4,2,SKIN)            # shoulders / back
c.ellipse(64,86,4,2,HAIR)            # hair falling to shoulders
c.circle(64,82,3,HAIR)               # head from behind
c.set(62,81,HAIR_HI); c.set(66,83,HAIR_HI)
c.set(60,88,HAIR); c.set(68,88,HAIR) # hair tips on shoulders
c.set(61,90,SKIN_SH); c.set(67,90,SKIN_SH)
c.ellipse(55,88,2,1,SKIN)            # arms resting on ring
c.ellipse(73,88,2,1,SKIN)
c.path("M 53 91 A 11 5 0 0 0 75 91", RING, fill=False)   # front rim
# ring shading / highlight
for (px,py) in [(68,95),(69,95),(70,94),(71,94),(72,93),(73,92),(55,93),(56,94)]:
    c.set(px,py,RING_SH)
for (px,py) in [(57,87),(58,86),(59,86),(60,85)]:
    c.set(px,py,RING_HI)
c.set(56,87,LIGHT)
# ripples around ring
c.path("M 51 96 Q 64 102 77 96", RIPL, fill=False)
c.path("M 45 101 Q 64 110 83 101", REFS, fill=False)
# ring reflection
for (px,py) in [(60,99),(66,100),(63,103),(69,104),(58,102)]:
    c.set(px,py,RING_RF)

# sparkles
for (px,py) in [(30,90),(96,84),(108,110),(20,105)]:
    c.set(px,py,REFL)

view(c)
print(c.stats_text())
finish(c)
