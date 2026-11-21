from pixelbench_api import *
import math
import random

random.seed(17)
result = new_canvas(256, 256, background="#070912", name="arcane_instrument_giant")
c = result

# Compact palette.
INK = "#05060a"; DEEP = "#0a0d19"; NIGHT = "#101526"; BLUE = "#17223a"
STONE0 = "#171923"; STONE1 = "#242632"; STONE2 = "#373742"; STONE3 = "#50505a"
BRONZE0 = "#39230f"; BRONZE1 = "#684017"; BRONZE2 = "#996426"; BRASS = "#c78b38"
GOLD = "#e7b85c"; PALE = "#ffe39a"; COPPER = "#ad5629"; RUST = "#6f2d1d"
CYAN0 = "#123c4a"; CYAN1 = "#16738a"; CYAN2 = "#28c8d4"; CYAN3 = "#9ff7e9"
VIOLET = "#7752b6"; LILAC = "#c6a6ff"; WHITE = "#fff4cf"; RED = "#b84232"

# Dark vaulted hall.
c.rect(0, 0, 256, 256, DEEP)
c.dither(0, 0, 256, 184, [DEEP, NIGHT], pattern="bayer4")
# Recessed pointed arch and distant vault.
c.path("M18 184 L18 72 Q18 22 64 8 Q112 -6 128 20 Q144 -6 192 8 Q238 22 238 72 L238 184 Z", INK, True)
c.path("M28 181 L28 78 Q29 35 67 20 Q108 5 128 35 Q148 5 189 20 Q227 35 228 78 L228 181 Z", NIGHT, True)
c.path("M38 180 L38 82 Q38 45 72 31 Q109 17 128 48 Q147 17 184 31 Q218 45 218 82 L218 180 Z", DEEP, True)
# Vault ribs and masonry.
for off in (0, 3):
    c.path(f"M{29+off} 181 L{29+off} 78 Q30 36 67 20 Q108 5 128 35", STONE2 if off == 0 else STONE0, False)
    c.path(f"M{227-off} 181 L{227-off} 78 Q226 36 189 20 Q148 5 128 35", STONE2 if off == 0 else STONE0, False)
c.line(128, 20, 128, 177, STONE0)
for y in range(48, 174, 14):
    c.line(31, y, 47, y-2, STONE1); c.line(209, y-2, 225, y, STONE1)
for x in (10, 22, 234, 246):
    c.rect(x, 58, 7, 132, STONE0); c.line(x, 58, x, 189, STONE2)
    c.rect(x-2, 55, 11, 5, STONE2); c.rect(x-3, 188, 13, 5, STONE1)
# Tiny background lights.
for x,y in [(51,55),(205,54),(62,102),(194,97),(45,145),(211,137)]:
    c.set(x,y,CYAN1); c.set(x,y-1,CYAN2)

# Ground and monumental stone pedestal.
c.rect(0, 184, 256, 72, STONE0)
c.dither(0, 185, 256, 71, [STONE0, INK], pattern="checker")
c.poly([(76,256),(85,215),(171,215),(181,256)], STONE1)
c.poly([(81,256),(89,219),(128,224),(128,256)], STONE2)
c.poly([(175,256),(167,219),(128,224),(128,256)], STONE0)
c.rect(72, 207, 112, 10, INK); c.rect(75, 204, 106, 10, STONE2)
c.line(78,205,178,205,STONE3); c.line(75,214,181,214,INK)
c.rect(91, 187, 74, 20, STONE1); c.poly([(87,188),(97,179),(159,179),(169,188)], STONE2)
c.rect(94, 184, 68, 5, STONE3); c.line(99,188,157,188,INK)
# Pedestal inscriptions and cracks.
c.line(107,226,102,245,STONE0); c.line(102,245,107,252,STONE0)
c.line(153,224,157,239,STONE3); c.line(157,239,154,248,STONE3)
c.text(105,232,"SOL", BRONZE2, font="5x7")
c.line(94,220,162,220,STONE3)

# Instrument shadow and support stem.
c.ellipse(128, 190, 72, 10, INK, True)
c.rect(121, 159, 14, 29, BRONZE0); c.rect(124, 159, 8, 29, BRASS)
c.rect(119, 181, 18, 7, INK); c.rect(121, 180, 14, 5, GOLD)

# Outer halo silhouette and heavy frame rings.
c.circle(128, 110, 91, INK, False)
c.circle(128, 110, 90, INK, False)
for r,col in [(88,BRONZE1),(87,BRASS),(86,GOLD),(83,BRONZE2),(82,INK),(79,BRASS),(78,BRONZE0)]:
    c.circle(128,110,r,col,False)
# Cardinal finials.
for x,y,pts in [
    (128,18,[(128,8),(122,18),(128,27),(134,18)]),
    (128,202,[(128,212),(122,202),(128,193),(134,202)]),
    (36,110,[(26,110),(36,104),(45,110),(36,116)]),
    (220,110,[(230,110),(220,104),(211,110),(220,116)])]:
    c.poly(pts, INK); c.circle(x,y,4,BRASS); c.set(x,y,PALE)

# Outer ring segmented plates, ticks, studs, glowing rune marks.
for i in range(48):
    a = math.radians(i*7.5)
    r0 = 80 if i%2 else 78
    r1 = 85 if i%4 else 88
    x0=int(round(128+math.cos(a)*r0)); y0=int(round(110+math.sin(a)*r0))
    x1=int(round(128+math.cos(a)*r1)); y1=int(round(110+math.sin(a)*r1))
    c.line(x0,y0,x1,y1,GOLD if i%3 else BRONZE0)
for i in range(16):
    a=math.radians(i*22.5+11)
    x=int(128+84*math.cos(a)); y=int(110+84*math.sin(a))
    c.circle(x,y,2,INK); c.set(x,y,PALE)
# Rune-like luminous clusters around circumference.
for i in range(12):
    a=math.radians(i*30+15)
    x=int(128+74*math.cos(a)); y=int(110+74*math.sin(a))
    tx=-math.sin(a); ty=math.cos(a)
    c.line(x-int(tx*2),y-int(ty*2),x+int(tx*2),y+int(ty*2),CYAN2)
    if i%2==0: c.set(x+int(math.cos(a)*2),y+int(math.sin(a)*2),CYAN3)

# Great crossing orbital bands, outlined in dark.
for rx,ry,col in [(74,31,INK),(73,30,BRASS),(70,28,BRONZE1),(49,72,INK),(48,71,GOLD),(45,68,BRONZE1)]:
    c.ellipse(128,110,rx,ry,col,False)
# Diagonal armatures.
for d,col in [(0,INK),(2,BRONZE1),(4,BRASS)]:
    c.line(72+d,53,181+d,165,col)
    c.line(70+d,166,179+d,54,col)
# Joint clamps along diagonals.
for x,y in [(82,63),(102,84),(154,136),(175,157),(79,159),(101,137),(155,82),(178,59)]:
    c.circle(x,y,4,INK); c.rect(x-2,y-2,5,5,BRASS); c.set(x,y,PALE)

# Inner machinery plate.
c.circle(128,110,52,INK,True)
c.circle(128,110,49,BRONZE0,True)
c.circle(128,110,46,NIGHT,True)
c.circle(128,110,44,BRONZE1,False)
c.circle(128,110,42,BRASS,False)
# Four radial rails.
for a in range(0,360,45):
    rad=math.radians(a)
    c.line(int(128+17*math.cos(rad)),int(110+17*math.sin(rad)),int(128+40*math.cos(rad)),int(110+40*math.sin(rad)),INK)
    c.line(int(128+19*math.cos(rad)),int(110+19*math.sin(rad)),int(128+38*math.cos(rad)),int(110+38*math.sin(rad)),BRASS)

# Gear helper.
def gear(cx,cy,r,teeth,base,hi):
    pts=[]
    for i in range(teeth*2):
        a=math.pi*2*i/(teeth*2)
        rr=r if i%2==0 else r-2
        pts.append((int(round(cx+math.cos(a)*rr)),int(round(cy+math.sin(a)*rr))))
    c.poly(pts,INK); c.circle(cx,cy,r-3,base,True)
    c.circle(cx,cy,max(2,r-6),hi,False); c.circle(cx,cy,2,INK,True); c.set(cx,cy,PALE)

gear(100,104,13,10,BRONZE2,GOLD)
gear(155,103,12,9,COPPER,BRASS)
gear(109,135,10,8,COPPER,GOLD)
gear(151,135,9,8,BRONZE2,BRASS)
gear(128,78,9,8,BRONZE1,GOLD)
# Extra pinions.
for x,y in [(92,122),(165,120),(122,145),(139,145)]:
    c.circle(x,y,5,INK); c.circle(x,y,3,BRASS); c.set(x,y,PALE)

# Central radiant core, stepped pixel glow and cage.
c.circle(128,111,18,CYAN0,True)
c.dither(115,98,27,27,[CYAN0,CYAN1],pattern="checker")
c.circle(128,111,13,CYAN1,True)
c.circle(128,111,9,CYAN2,True)
c.poly([(128,99),(137,110),(128,123),(119,110)],CYAN3)
c.poly([(128,103),(133,110),(128,118),(123,110)],WHITE)
c.set(128,109,"#ffffff"); c.set(127,110,WHITE)
# Core cage.
c.circle(128,111,20,BRASS,False); c.circle(128,111,21,INK,False)
c.line(128,89,128,97,GOLD); c.line(128,125,128,133,GOLD)
c.line(106,111,114,111,GOLD); c.line(142,111,150,111,GOLD)
for x,y in [(128,90),(128,132),(107,111),(149,111)]: c.circle(x,y,2,PALE)

# Alchemical dials on lower inner frame.
for cx,label in [(93,"I"),(163,"V")]:
    c.circle(cx,151,10,INK); c.circle(cx,151,8,STONE1); c.circle(cx,151,7,BRASS,False)
    c.line(cx,151,cx+3,146,RED); c.set(cx,151,PALE)
    c.text(cx-2,155,label,GOLD,font="5x7")
# Fine chain/weights.
for x in (61,195):
    c.line(x,92,x,156,BRONZE1)
    for y in range(94,154,5): c.set(x,y,GOLD)
    c.poly([(x,156),(x-4,165),(x+4,165)],BRASS)
    c.circle(x,166,3,INK); c.set(x,165,GOLD)

# Orbiting crystal spheres in front of rings.
crystals=[(57,105,7,CYAN2),(198,88,8,VIOLET),(185,149,7,CYAN1),(88,44,6,LILAC),(150,42,5,CYAN2),(66,139,5,VIOLET)]
for x,y,r,col in crystals:
    c.circle(x,y,r+1,INK,True)
    c.circle(x,y,r,col,True)
    c.dither(x-r+1,y-r+1,2*r-1,2*r-1,[col,CYAN0 if col!=VIOLET else VIOLET],pattern="checker")
    c.line(x-r+2,y-2,x,y-r+2,CYAN3 if col!=VIOLET else LILAC)
    c.set(x-1,y-2,WHITE)
    c.circle(x,y,r+2,BRASS,False)

# Top crown, hanging pointers, and scattered highlights.
c.poly([(111,28),(117,20),(122,29),(128,15),(134,29),(139,20),(145,28)],INK)
c.line(112,28,144,28,GOLD)
for x in range(116,142,6): c.line(x,28,x,34,BRASS)
c.poly([(128,34),(124,42),(128,48),(132,42)],CYAN2); c.set(128,39,WHITE)
# Engraved micro-details and bolts.
for i in range(28):
    a=math.radians(i*13+4)
    r=60
    x=int(128+r*math.cos(a)); y=int(110+r*math.sin(a))
    c.set(x,y,BRASS if i%2 else GOLD)
for x,y in [(47,75),(208,73),(48,176),(208,176),(112,57),(145,58),(111,166),(145,165)]:
    c.circle(x,y,2,INK); c.set(x,y,GOLD)

# Foreground edge sparks and hard dark contour accents.
for x,y in [(42,113),(214,119),(77,70),(183,72),(77,178),(178,177)]:
    c.set(x,y,CYAN3); c.set(x+1,y,CYAN1)
c.line(75,204,181,204,STONE3)
c.line(82,255,174,255,INK)

view(result, scale=2, margin=0)
finish(result)
