from math import sin, cos, pi

W = H = 256
c = new_canvas(W, H, background="#070912", name="arcane_instrument_giant")

# Restricted, high-contrast palette.
INK = "#080912"
DEEP = "#0d1020"
NIGHT = "#12182a"
STONE0 = "#171b29"
STONE1 = "#23283a"
STONE2 = "#34384a"
STONE3 = "#4a4b58"
BRONZE0 = "#24170f"
BRONZE1 = "#4b2d17"
BRONZE2 = "#785027"
BRASS0 = "#a87432"
BRASS1 = "#d2a64b"
BRASS2 = "#e4bd63"
GOLD = "#f3d477"
PALE = "#fff0af"
CYAN0 = "#164458"
CYAN1 = "#2b8292"
CYAN2 = "#65d6d2"
ICE = "#c9fff0"
VIOLET0 = "#35214f"
VIOLET1 = "#754b9e"
VIOLET2 = "#c68aeb"
RED0 = "#51201e"
RED1 = "#a3472f"
EMBER = "#ef9650"

# Dark hall, block masonry and towering recess.
c.rect(0, 0, 256, 256, DEEP)
c.rect(8, 0, 18, 210, INK)
c.rect(230, 0, 18, 210, INK)
c.rect(27, 0, 5, 196, STONE0)
c.rect(224, 0, 5, 196, STONE0)
# Central arched void and ribs.
c.path("M38 196 L38 75 Q40 14 128 7 Q216 14 218 75 L218 196 Z", STONE1)
c.path("M45 196 L45 77 Q48 23 128 15 Q208 23 211 77 L211 196 Z", STONE0)
c.path("M53 196 L53 80 Q57 34 128 25 Q199 34 203 80 L203 196 Z", "#0a0d18")
for x, y, w in [(0,32,38),(218,32,38),(0,74,48),(208,74,48),(0,119,53),(203,119,53),(0,164,45),(211,164,45)]:
    c.rect(x,y,w,3,STONE2)
# Individual wall blocks.
for y in range(10, 194, 22):
    offset = 0 if (y//22)%2 == 0 else 10
    for x in list(range(-8+offset,35,20)) + list(range(221+offset,261,20)):
        c.line(x,y,x+15,y,STONE3)
        c.line(x+16,y+1,x+16,y+15,STONE0)
# Distant floor rays and sparks.
c.poly([(0,255),(77,190),(91,190),(48,255)], STONE0)
c.poly([(256,255),(179,190),(165,190),(211,255)], STONE0)
c.poly([(96,255),(117,184),(124,184),(117,255)], NIGHT)
c.poly([(160,255),(139,184),(132,184),(142,255)], NIGHT)
for x,y in [(37,42),(217,59),(27,107),(231,143),(57,24),(197,29),(16,186),(241,187)]:
    c.set(x,y,BRASS1); c.set(x+1,y,GOLD); c.set(x,y+1,BRONZE2)

# Pedestal: broad carved base beneath the floating apparatus.
c.poly([(61,213),(195,213),(212,229),(207,255),(48,255),(44,229)], INK)
c.poly([(66,211),(190,211),(202,225),(197,250),(58,250),(53,225)], STONE1)
c.rect(50,225,155,7,STONE2)
c.line(54,233,201,233,INK)
c.rect(64,236,128,14,STONE0)
c.rect(70,239,116,3,STONE2)
c.poly([(79,211),(91,193),(165,193),(178,211)], INK)
c.poly([(87,210),(96,197),(160,197),(169,210)], STONE2)
c.rect(101,190,54,9,STONE1)
c.rect(105,187,46,5,STONE3)
# Pedestal glyph plate.
c.rect(111,238,34,10,INK)
c.line(116,243,121,239,BRASS0); c.line(121,239,126,245,BRASS0)
c.circle(128,243,3,BRASS1,fill=False)
c.line(132,245,139,240,BRASS0)

# Floating shadow and lower levitation glow.
c.ellipse(128,191,47,6,INK)
c.ellipse(128,188,34,4,CYAN0,fill=False)
c.line(105,188,151,188,CYAN1)
for x in range(109,149,4):
    c.set(x,189,CYAN2)

CX,CY = 128,108
# Rear support cage and radial struts.
c.circle(CX,CY,83,INK)
c.circle(CX,CY,80,BRONZE1,fill=False)
c.circle(CX,CY,77,BRASS0,fill=False)
for a in range(0,360,15):
    r1,r2 = 63,78
    x1=int(CX+cos(a*pi/180)*r1); y1=int(CY+sin(a*pi/180)*r1)
    x2=int(CX+cos(a*pi/180)*r2); y2=int(CY+sin(a*pi/180)*r2)
    c.line(x1,y1,x2,y2,INK)
    c.set(x2,y2,BRASS1)

# Outer engraved astrolabe band, dark edging with two brass tracks.
c.circle(CX,CY,72,INK,fill=False)
c.circle(CX,CY,71,BRASS2,fill=False)
c.circle(CX,CY,68,BRASS1,fill=False)
c.circle(CX,CY,64,BRONZE0,fill=False)
c.circle(CX,CY,63,BRASS0,fill=False)
# Cardinal finials.
for a in [0,45,90,135,180,225,270,315]:
    ca,sa=cos(a*pi/180),sin(a*pi/180)
    x=int(CX+ca*73); y=int(CY+sa*73)
    c.circle(x,y,4,INK)
    c.circle(x,y,2,BRASS1)
    c.set(x,y,GOLD)
# Engraved tick marks.
for a in range(0,360,6):
    ca,sa=cos(a*pi/180),sin(a*pi/180)
    r0=65 if a%30 else 62
    x0=int(CX+ca*r0); y0=int(CY+sa*r0)
    x1=int(CX+ca*68); y1=int(CY+sa*68)
    c.line(x0,y0,x1,y1,GOLD if a%30==0 else BRONZE2)

# Tilted orbital ellipses give the machine depth.
for rx,ry,col in [(79,24,BRASS1),(74,35,BRONZE2),(55,70,BRASS0)]:
    c.ellipse(CX,CY,rx,ry,INK,fill=False)
    c.ellipse(CX,CY-1,rx,ry,col,fill=False)
# Diagonal orbit rails as paired segmented chords.
c.line(65,158,191,58,INK); c.line(67,158,193,58,BRASS1)
c.line(59,65,197,151,INK); c.line(59,63,197,149,BRONZE2)

# Inner armillary rings.
c.circle(CX,CY,48,INK,fill=False)
c.circle(CX,CY,46,BRASS1,fill=False)
c.circle(CX,CY,38,BRONZE1,fill=False)
c.circle(CX,CY,36,GOLD,fill=False)
c.ellipse(CX,CY,18,45,INK,fill=False)
c.ellipse(CX,CY,16,44,BRASS0,fill=False)
c.ellipse(CX,CY,43,17,INK,fill=False)
c.ellipse(CX,CY,42,15,BRASS1,fill=False)

# Rune blocks along middle ring: luminous angular sigils.
for i,a in enumerate(range(0,360,30)):
    ca,sa=cos(a*pi/180),sin(a*pi/180)
    x=int(CX+ca*55); y=int(CY+sa*55)
    col = CYAN2 if i%3 else VIOLET2
    c.set(x,y,col)
    c.set(x+int(sa),y-int(ca),col)
    if i%2==0: c.set(x-int(ca),y-int(sa),PALE)
# Four larger etched runes.
for x,y,flip in [(126,48,1),(126,166,-1),(67,106,1),(186,106,-1)]:
    col=CYAN2
    c.line(x-2,y,x+2,y,col); c.line(x,y-3,x,y+3,col)
    c.set(x+2*flip,y-2,col); c.set(x-2*flip,y+2,col)

# Side gear clusters.
def gear(cx,cy,r,teeth,metal):
    c.circle(cx,cy,r+3,INK)
    for a in range(0,360,360//teeth):
        ca,sa=cos(a*pi/180),sin(a*pi/180)
        x=int(cx+ca*(r+3)); y=int(cy+sa*(r+3))
        c.rect(x-1,y-1,3,3,metal)
    c.circle(cx,cy,r,metal)
    c.circle(cx,cy,r-3,BRONZE0)
    c.circle(cx,cy,2,INK)
    for a in range(0,360,60):
        c.line(cx,cy,int(cx+cos(a*pi/180)*(r-2)),int(cy+sin(a*pi/180)*(r-2)),GOLD)

gear(52,128,11,12,BRASS0)
gear(205,126,10,10,BRONZE2)
gear(68,160,8,8,BRASS1)
gear(188,157,7,8,BRASS0)
gear(54,91,6,8,BRONZE2)
# Small alchemical dial faces.
for x,y,r in [(83,177,9),(173,178,9),(35,116,7),(220,104,7)]:
    c.circle(x,y,r+1,INK)
    c.circle(x,y,r,BRASS0)
    c.circle(x,y,r-2,STONE0)
    c.line(x,y,x+int(r*.55),y-int(r*.45),PALE)
    c.set(x,y,RED1)

# Suspended chains, counterweights and pointers.
for x,top,bottom in [(42,136,177),(213,137,181)]:
    for y in range(top,bottom,4):
        c.set(x,y,BRASS1); c.set(x+1,y+1,BRONZE2)
    c.poly([(x-4,bottom),(x+5,bottom),(x+3,bottom+11),(x-2,bottom+11)],INK)
    c.rect(x-2,bottom+1,5,8,BRASS0)
c.line(78,66,97,88,INK); c.line(79,65,98,87,GOLD)
c.poly([(96,84),(103,91),(95,93)],RED1)
c.line(177,70,160,91,INK); c.line(176,69,159,90,BRASS1)
c.poly([(157,88),(166,90),(160,96)],CYAN1)

# Orbiting crystal spheres with facets and cast glints.
def crystal(cx,cy,r,base,mid,hi):
    c.circle(cx,cy,r+2,INK)
    c.circle(cx,cy,r,base)
    c.poly([(cx-r+1,cy),(cx,cy-r+1),(cx+1,cy+1),(cx-r//2,cy+r-1)],mid)
    c.poly([(cx,cy-r+1),(cx+r-1,cy-1),(cx+1,cy+1)],hi)
    c.set(cx-1,cy-r+1,PALE); c.set(cx-r+1,cy,hi)

crystal(199,84,7,CYAN0,CYAN1,ICE)
crystal(62,72,6,VIOLET0,VIOLET1,VIOLET2)
crystal(185,151,6,RED0,RED1,EMBER)
crystal(75,143,5,CYAN0,CYAN1,CYAN2)
crystal(132,36,5,VIOLET0,VIOLET1,PALE)
# tiny orbit beads.
for x,y,col in [(48,108,CYAN2),(92,44,GOLD),(168,49,VIOLET2),(208,111,EMBER),(157,172,CYAN2),(103,174,GOLD)]:
    c.circle(x,y,3,INK); c.circle(x,y,1,col)

# Central housing, layered aperture and radiant core.
c.circle(CX,CY,27,INK)
c.circle(CX,CY,24,BRONZE2)
# Eight mechanical jaws.
for a in range(0,360,45):
    ca,sa=cos(a*pi/180),sin(a*pi/180)
    p1=(int(CX+ca*15-sa*4),int(CY+sa*15+ca*4))
    p2=(int(CX+ca*24-sa*2),int(CY+sa*24+ca*2))
    p3=(int(CX+ca*24+sa*2),int(CY+sa*24-ca*2))
    p4=(int(CX+ca*15+sa*4),int(CY+sa*15-ca*4))
    c.poly([p1,p2,p3,p4],BRASS1)
    c.line(CX,CY,int(CX+ca*22),int(CY+sa*22),GOLD)
c.circle(CX,CY,17,INK)
c.circle(CX,CY,14,CYAN0)
c.circle(CX,CY,11,CYAN1)
c.circle(CX,CY,8,CYAN2)
c.circle(CX,CY,5,ICE)
c.circle(CX-2,CY-2,2,PALE)
c.set(CX-3,CY-4,"#ffffff")
# Core rays, intentionally broken by dark pixels for a pixel-energy effect.
for a,l in [(0,34),(30,26),(60,31),(90,37),(120,28),(150,32),(180,35),(210,27),(240,31),(270,38),(300,29),(330,33)]:
    ca,sa=cos(a*pi/180),sin(a*pi/180)
    c.line(int(CX+ca*18),int(CY+sa*18),int(CX+ca*l),int(CY+sa*l),CYAN2)
    c.set(int(CX+ca*(l-4)),int(CY+sa*(l-4)),PALE)

# Foreground clamps and bright rim highlights.
c.line(82,184,105,169,INK); c.line(83,183,106,168,BRASS0)
c.line(174,184,151,169,INK); c.line(173,183,150,168,BRASS0)
c.rect(78,181,9,5,BRASS2); c.rect(169,181,9,5,BRASS2)
# Selective dark outline reinforcement.
for x,y in [(38,58),(217,58),(46,195),(210,195),(61,213),(195,213)]:
    c.set(x,y,INK)

# Sparse foreground dust motes.
for x,y,col in [(22,205,BRONZE2),(33,218,CYAN1),(224,210,BRASS1),(238,225,VIOLET1),(17,235,STONE3),(219,241,BRONZE2),(90,221,GOLD),(164,218,CYAN2)]:
    c.set(x,y,col)

result = c
view(result, size=768, margin=0)
finish(result)
