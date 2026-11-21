# Arcane instrument: giant brass astrolabe-orrery in a dark hall.
from math import sin, cos, pi

W = H = 256
c = new_canvas(W, H, background="#070912", name="arcane-instrument-giant")

# Compact fixed palette.
INK = "#080811"; DEEP = "#0d1020"; NIGHT = "#12172a"; STONE0 = "#171b2a"
STONE1 = "#22283a"; STONE2 = "#30374a"; STONE3 = "#4a5060"
BRASS0 = "#2a1c16"; BRASS1 = "#5a3820"; BRASS2 = "#8f5d28"; BRASS3 = "#c18a3c"
GOLD = "#e5b85a"; PALE = "#ffe39a"; COPPER = "#a94f2d"; RUST = "#65301f"
TEAL0 = "#123943"; TEAL = "#1b7f88"; CYAN = "#43d4cf"; ICE = "#b8fff1"
VIOLET = "#704b9a"; MAGENTA = "#c15ac7"; WHITE = "#fff5cf"; RED = "#ba3d38"

# Dark hall, vaulted masonry, floor and columns.
c.rect(0, 0, 256, 256, DEEP)
c.rect(0, 181, 256, 75, STONE0)
# Recessed arch behind the machine.
c.path("M24 181 V67 Q24 15 78 7 H178 Q232 15 232 67 V181 H217 V70 Q217 29 176 21 H80 Q39 29 39 70 V181 Z", STONE1)
c.path("M39 181 V70 Q39 29 80 21 H176 Q217 29 217 70 V181 H205 V72 Q205 40 174 33 H82 Q51 40 51 72 V181 Z", INK)
# Inner arch glow/shadow bands.
c.path("M52 179 V74 Q52 40 83 33 H173 Q204 40 204 74 V179", STONE2, fill=False)
c.path("M58 177 V76 Q58 47 85 40 H171 Q198 47 198 76 V177", NIGHT, fill=False)
# Columns.
for x in (8, 225):
    c.rect(x, 48, 23, 139, INK)
    c.rect(x+3, 51, 17, 133, STONE1)
    c.rect(x+6, 52, 4, 132, STONE2)
    c.rect(x+15, 52, 3, 132, STONE0)
    c.rect(x-2, 43, 27, 8, STONE2)
    c.rect(x, 40, 23, 4, STONE3)
    c.rect(x-3, 183, 29, 7, STONE2)
# Masonry seams.
for y in (72, 99, 126, 153):
    c.line(9, y, 30, y, STONE0); c.line(226, y, 246, y, STONE0)
for y in range(190, 256, 13):
    c.line(0, y, 255, y, "#101422")
for row, y in enumerate(range(190, 250, 13)):
    off = 0 if row % 2 else 18
    for x in range(off, 256, 37): c.line(x, y, x-7, y+13, "#101422")
# Subtle radial illumination behind core.
for r, col in [(62,"#101d2a"),(47,"#122b34"),(34,"#16414a")]:
    c.circle(128, 110, r, col)
# Pixel rays.
for ang in range(0, 360, 15):
    a = ang*pi/180
    r0, r1 = 35, 54 + (ang % 30)//2
    c.line(int(128+cos(a)*r0), int(110+sin(a)*r0), int(128+cos(a)*r1), int(110+sin(a)*r1), TEAL0)

# Pedestal and shadow.
c.ellipse(128, 235, 63, 12, INK)
c.poly([(82,211),(174,211),(185,228),(177,239),(79,239),(71,228)], INK)
c.poly([(85,210),(171,210),(180,227),(174,235),(82,235),(76,227)], STONE1)
c.rect(78, 210, 100, 8, STONE3)
c.rect(84, 218, 88, 4, STONE2)
c.poly([(96,181),(160,181),(169,209),(87,209)], INK)
c.poly([(101,182),(155,182),(163,207),(93,207)], STONE2)
c.rect(95, 180, 66, 6, STONE3)
c.line(101,186,93,206, STONE1); c.line(155,186,163,206, STONE0)
c.rect(108,190,40,14, INK)
c.rect(111,192,34,9, BRASS1)
c.text(115,194,"AEON",GOLD,font="5x7",spacing=1)
# Pedestal runes and gems.
for x in range(90,169,10):
    c.set(x,214,GOLD); c.set(x+2,216,BRASS3)
c.circle(128,225,5,INK); c.circle(128,225,3,TEAL); c.set(127,224,ICE)

# Rear suspension pylons.
for x, lean in [(55,8),(201,-8)]:
    c.line(x,176,x+lean,61,INK); c.line(x+1,176,x+lean+1,61,BRASS2)
    for y in range(73,174,18):
        xx = int(x + lean*(176-y)/115)
        c.circle(xx,y,3,INK); c.circle(xx,y,1,GOLD)

# Outer astrolabe body: multiple circular rims.
for r,col in [(80,INK),(78,BRASS1),(76,GOLD),(73,BRASS0),(70,BRASS3),(68,INK),(66,BRASS2),(63,INK)]:
    c.circle(128,108,r,col,fill=False)
# Cardinal crown and supports.
for ang in range(0,360,15):
    a=ang*pi/180
    rr=80; x=int(128+cos(a)*rr); y=int(108+sin(a)*rr)
    ln=7 if ang%45==0 else 4
    x2=int(128+cos(a)*(rr-ln)); y2=int(108+sin(a)*(rr-ln))
    c.line(x,y,x2,y2, PALE if ang%45==0 else BRASS3)
    if ang%45==0: c.circle(x,y,2,INK); c.set(x,y,GOLD)
# Ornamental top finial.
c.poly([(128,18),(122,28),(125,36),(128,31),(131,36),(134,28)],INK)
c.poly([(128,21),(125,28),(128,33),(131,28)],GOLD)
c.circle(128,17,3,INK); c.circle(128,17,1,ICE)

# Engraved concentric face rings.
for r,col in [(57,BRASS3),(54,BRASS1),(50,GOLD),(47,BRASS2),(42,INK),(38,BRASS3)]:
    c.circle(128,108,r,col,fill=False)
# Radial spokes and rune glyphs.
for ang in range(0,360,15):
    a=ang*pi/180
    r0=42; r1=61
    p0=(int(128+cos(a)*r0),int(108+sin(a)*r0))
    p1=(int(128+cos(a)*r1),int(108+sin(a)*r1))
    c.line(*p0,*p1, BRASS2 if ang%30 else GOLD)
for i,ang in enumerate(range(0,360,30)):
    a=ang*pi/180; x=int(128+cos(a)*45); y=int(108+sin(a)*45)
    # tiny luminous rune: stem plus alternating hooks
    c.line(x,y-2,x,y+2,CYAN)
    c.set(x+(1 if i%2 else -1),y-1,ICE)
    c.set(x+(-1 if i%2 else 1),y+1,TEAL)

# Great tilted orbital hoops, black underdrawing then metals.
for ry, col in [(24,BRASS3),(34,GOLD),(48,BRASS2)]:
    c.ellipse(128,108,91,ry,INK,fill=False)
    c.ellipse(128,107,89,ry,col,fill=False)
# Crossing vertical celestial meridians.
for rx,col in [(24,GOLD),(39,BRASS3),(55,BRASS2)]:
    c.ellipse(128,108,rx,88,INK,fill=False)
    c.ellipse(127,108,rx,86,col,fill=False)
# Horizontal axis caps.
for x in (36,220):
    c.circle(x,108,6,INK); c.circle(x,108,4,BRASS3); c.line(x-2,108,x+2,108,PALE)

# Gear helper.
def gear(cx,cy,r,teeth,base,hi):
    for i in range(teeth):
        a=2*pi*i/teeth; x=int(cx+cos(a)*(r+2)); y=int(cy+sin(a)*(r+2))
        c.rect(x-1,y-1,3,3,INK); c.set(x,y,hi)
    c.circle(cx,cy,r+1,INK); c.circle(cx,cy,r,base)
    c.circle(cx,cy,max(2,r-3),INK,fill=False)
    for i in range(0,teeth,2):
        a=2*pi*i/teeth
        c.line(cx,cy,int(cx+cos(a)*(r-2)),int(cy+sin(a)*(r-2)),hi)
    c.circle(cx,cy,2,INK); c.set(cx,cy,PALE)

# Dense gear trains around core.
gear(94,91,11,10,BRASS2,GOLD); gear(161,92,10,9,COPPER,BRASS3)
gear(98,132,9,8,COPPER,GOLD); gear(158,132,12,12,BRASS1,BRASS3)
gear(128,145,8,8,BRASS2,GOLD); gear(128,71,7,8,BRASS1,PALE)
# Linkage rods.
c.line(101,98,118,106,PALE); c.line(138,106,153,97,BRASS3)
c.line(104,128,119,116,BRASS3); c.line(137,117,151,128,GOLD)

# Alchemical dial plates.
for cx,cy in [(74,117),(183,117),(111,158),(146,158)]:
    c.circle(cx,cy,7,INK); c.circle(cx,cy,5,BRASS2); c.circle(cx,cy,3,STONE0,fill=False)
    c.line(cx,cy,cx+2,cy-3,PALE); c.set(cx,cy,RED)
# Chains hanging from lower rim.
for x in (69,187):
    for y in range(153,184,5):
        c.circle(x + ((y//5)%2),y,2,BRASS1,fill=False)
    c.poly([(x-4,184),(x+4,184),(x,191)],INK)
    c.poly([(x-2,184),(x+2,184),(x,188)],MAGENTA)

# Orbiting crystal spheres, placed on hoops.
def crystal(cx,cy,r,col):
    c.circle(cx,cy,r+2,INK)
    c.poly([(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)],col)
    c.poly([(cx,cy-r),(cx,cy),(cx-r,cy)],ICE)
    c.line(cx,cy-r,cx,cy+r,WHITE)
    c.set(cx-1,cy-1,WHITE)

crystal(55,84,6,TEAL); crystal(200,133,7,VIOLET); crystal(165,37,5,MAGENTA)
crystal(82,165,5,CYAN); crystal(213,91,4,TEAL); crystal(91,43,4,VIOLET)
# Orbit pins and small planets.
for cx,cy,col in [(44,122,RED),(181,54,GOLD),(187,157,CYAN),(69,61,COPPER)]:
    c.circle(cx,cy,4,INK); c.circle(cx,cy,2,col); c.set(cx-1,cy-1,PALE)

# Central containment housing and radiant core.
c.circle(128,109,29,INK)
c.circle(128,109,26,BRASS1)
for ang in range(0,360,45):
    a=ang*pi/180
    c.line(int(128+cos(a)*18),int(109+sin(a)*18),int(128+cos(a)*25),int(109+sin(a)*25),GOLD)
c.circle(128,109,20,INK)
c.circle(128,109,17,TEAL0)
c.circle(128,109,13,TEAL)
c.circle(128,109,9,CYAN)
c.circle(128,109,5,ICE)
c.circle(128,109,2,WHITE)
# Four core clamps.
for ang in (0,90,180,270):
    a=ang*pi/180
    x=int(128+cos(a)*22); y=int(109+sin(a)*22)
    c.rect(x-2,y-2,5,5,INK); c.set(x,y,GOLD)
# Angular energy fissures.
c.line(128,92,125,101,ICE); c.line(125,101,128,106,CYAN)
c.line(139,110,134,112,ICE); c.line(134,112,131,119,CYAN)
c.line(119,113,123,110,WHITE); c.line(123,110,120,104,CYAN)

# Foreground engraved band for dimensional overlap.
c.ellipse(128,109,91,33,INK,fill=False)
c.ellipse(128,110,89,32,GOLD,fill=False)
for ang in range(10,180,14):
    a=ang*pi/180
    x=int(128+89*cos(a)); y=int(110+32*sin(a))
    c.rect(x-1,y-1,3,2,INK); c.set(x,y,PALE)

# Spark motes and selective hard highlights.
for x,y in [(42,35),(212,39),(30,105),(229,146),(53,192),(202,194),(103,24),(152,22),(18,25),(239,68)]:
    c.set(x,y,CYAN); c.set(x+1,y,TEAL0)
for x,y in [(76,78),(106,51),(147,50),(178,81),(171,145),(88,145)]:
    c.set(x,y,PALE)

# Dark pixel outline accents along silhouette and pedestal contact.
c.line(78,239,178,239,INK)
c.line(88,209,168,209,INK)

result = c
view(result, scale=2, margin=0)
finish(result)
