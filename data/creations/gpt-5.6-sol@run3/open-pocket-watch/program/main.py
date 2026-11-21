import math

# 64x64 open mechanical pocket watch, drawn with a compact indexed-style palette.
c = new_canvas(64, 64, background="#090a0d", name="open-pocket-watch")

# Palette
BG = "#090a0d"
BLACK = "#050506"
SHADOW = "#17120d"
DEEP = "#2b1d10"
BRONZE = "#5a3515"
COPPER = "#8a5120"
GOLD_D = "#9b6928"
GOLD = "#c9953d"
GOLD_L = "#e9c56a"
PALE = "#ffe9a4"
WHITE = "#fff4c9"
STEEL_D = "#34363a"
STEEL = "#777a7b"
STEEL_L = "#c4c5bc"
RED = "#9c3427"
RUBY = "#e05a3f"

# Background vignette / hard macro glints.
c.rect(0, 0, 64, 64, BG)
c.dither(2, 43, 22, 17, [BG, "#0f1013"], pattern="bayer4")
c.line(1, 58, 16, 63, "#15130f")
c.set(4, 8, "#242018").set(5, 8, "#8a6c38").set(6, 8, "#292319")

# Open lid behind the movement.
c.circle(18, 19, 17, BLACK)
c.circle(18, 19, 16, BRONZE)
c.circle(18, 19, 14, GOLD_D)
c.circle(18, 19, 13, SHADOW)
c.circle(18, 19, 12, "#292720")
# Lid's inset reflection, curved metal bands.
c.path("M7 18 Q8 8 17 6 Q25 5 30 13", GOLD_L, fill=False)
c.path("M7 21 Q8 30 16 32 Q23 33 28 27", COPPER, fill=False)
c.path("M9 14 Q14 8 22 8", PALE, fill=False)
c.line(9, 13, 9, 20, GOLD)
c.line(27, 13, 29, 19, GOLD_D)
c.line(11, 27, 16, 30, GOLD_L)
c.line(21, 30, 25, 27, BRONZE)
# Dark mirror-like lid interior facets.
c.poly([(11,17),(18,10),(26,13),(24,21),(17,27),(10,24)], "#22231f")
c.line(12, 17, 18, 11, STEEL)
c.line(18, 11, 24, 13, STEEL_D)
c.line(11, 24, 17, 27, "#49463a")
c.line(24, 14, 23, 20, GOLD_D)
c.set(13,16,WHITE).set(14,15,GOLD_L).set(23,23,GOLD)

# Hinge joining lid and body.
c.rect(25, 28, 7, 5, BLACK)
c.rect(25, 29, 7, 3, GOLD_D)
c.set(26,29,GOLD_L).set(30,31,BRONZE)

# Watch chain behind the case, upper-right and right edge.
chain = [(48,8),(52,6),(57,7),(60,10),(59,14),(56,16),(58,19),(62,21),(63,25)]
for (x0,y0),(x1,y1) in zip(chain, chain[1:]):
    c.line(x0,y0,x1,y1,BLACK)
    # one-pixel metallic offset
    c.line(x0,y0,x1,y1,GOLD_D)
for x,y in [(48,8),(52,6),(57,7),(60,10),(59,14),(56,16),(58,19),(62,21)]:
    c.circle(x,y,2,BLACK,fill=False)
    c.set(x,y,GOLD_L)
c.set(61,22,PALE).set(63,25,GOLD)

# Pendant bow and crown.
c.circle(43,11,5,BLACK,fill=False)
c.circle(43,11,4,GOLD_D,fill=False)
c.set(40,9,GOLD_L).set(46,12,COPPER)
c.rect(40,14,7,4,BLACK)
c.rect(41,14,5,3,GOLD_D)
c.line(41,15,45,15,GOLD_L)
for x in (41,43,45): c.set(x,17,BRONZE)

# Main case silhouette and stepped gold rim.
c.circle(40,39,23,BLACK)
c.circle(40,39,22,DEEP)
c.circle(40,39,21,GOLD_D)
c.circle(40,39,19,GOLD_L)
c.circle(40,39,18,BRONZE)
c.circle(40,39,17,"#211a11")
# Rim shadow / rim specular segmentation.
c.path("M24 36 Q25 23 37 19 Q48 17 56 27", PALE, fill=False)
c.path("M23 42 Q26 55 39 59 Q52 58 58 47", "#684018", fill=False)
c.line(27,26,31,22,WHITE)
c.line(32,21,39,19,GOLD_L)
c.line(53,26,57,33,GOLD)
c.line(24,45,27,51,COPPER)
c.line(48,56,53,52,GOLD)

# Skeleton dial chapter ring: dark field plus gold tick marks.
# Cardinal ticks are longer; minute ticks surround the movement.
for i in range(48):
    a = 2*math.pi*i/48 - math.pi/2
    r0 = 14 if i % 4 else 13
    r1 = 16
    col = PALE if i % 4 == 0 else GOLD
    x0,y0 = round(40+math.cos(a)*r0), round(39+math.sin(a)*r0)
    x1,y1 = round(40+math.cos(a)*r1), round(39+math.sin(a)*r1)
    c.line(x0,y0,x1,y1,col)

# Gear helper: alternating-tooth polygon, dark under-ring, hub and holes.
def gear(cx, cy, teeth, ro, ri, color, inner, phase=0):
    pts=[]
    for i in range(teeth*4):
        a=phase + 2*math.pi*i/(teeth*4)
        r=ro if i%4 in (1,2) else ri
        pts.append((round(cx+math.cos(a)*r), round(cy+math.sin(a)*r)))
    c.poly(pts, BLACK)
    pts2=[]
    for i in range(teeth*4):
        a=phase + 2*math.pi*i/(teeth*4)
        r=(ro-1) if i%4 in (1,2) else max(ri-1,1)
        pts2.append((round(cx+math.cos(a)*r), round(cy+math.sin(a)*r)))
    c.poly(pts2, color)
    c.circle(cx,cy,max(2,ri-2),inner)
    c.circle(cx,cy,1,BLACK)
    c.set(cx,cy,PALE)

# Plates and bridges beneath the gears.
c.poly([(29,28),(39,24),(51,28),(48,34),(35,36)], GOLD_D)
c.poly([(31,48),(36,36),(51,36),(53,46),(44,52)], COPPER)
c.line(30,29,42,25,GOLD_L)
c.line(36,37,49,35,GOLD)
c.line(34,48,45,51,GOLD_L)
c.circle(30,30,2,STEEL_D); c.set(30,30,STEEL_L)
c.circle(50,45,2,STEEL_D); c.set(50,45,STEEL_L)

# Clearly meshing train, sized and placed to interlock.
gear(36,35,12,9,7,GOLD,GOLD_D,0.04)
gear(47,31,10,7,5,GOLD_L,COPPER,0.18)
gear(48,42,12,8,6,COPPER,GOLD_D,0.02)
gear(35,47,9,6,4,GOLD_L,BRONZE,0.15)

# Spoke cutouts simulated with dark radial slots.
for cx,cy,n,r in [(36,35,6,6),(47,31,5,4),(48,42,6,5),(35,47,5,3)]:
    for i in range(n):
        a=2*math.pi*i/n
        x1,y1=round(cx+math.cos(a)*2),round(cy+math.sin(a)*2)
        x2,y2=round(cx+math.cos(a)*r),round(cy+math.sin(a)*r)
        c.line(x1,y1,x2,y2,SHADOW)
    c.circle(cx,cy,1,STEEL_D)
    c.set(cx,cy,PALE)

# Balance wheel and ruby bearings add mechanical detail.
c.circle(29,42,6,BLACK,fill=False)
c.circle(29,42,5,GOLD_L,fill=False)
c.line(24,42,34,42,GOLD_D)
c.line(29,37,29,47,GOLD_D)
c.circle(29,42,2,RED)
c.set(29,42,RUBY).set(28,41,PALE)
for x,y in [(42,27),(41,48),(52,37)]:
    c.circle(x,y,2,DEEP)
    c.circle(x,y,1,RED)
    c.set(x,y,RUBY)

# Central cannon pinion and blued-steel hands over the visible movement.
c.circle(40,39,2,BLACK)
c.circle(40,39,1,STEEL_L)
c.line(40,39,34,27,BLACK)
c.line(39,39,33,28,STEEL_L)
c.set(34,28,WHITE)
c.line(40,39,51,36,BLACK)
c.line(41,38,51,35,STEEL_L)
c.set(50,35,WHITE)
c.set(40,39,PALE)

# Foreground case lip and hard reflections for depth.
c.path("M23 43 Q25 55 38 60", GOLD, fill=False)
c.path("M38 60 Q51 60 58 49", BRONZE, fill=False)
c.line(27,52,32,56,GOLD_L)
c.line(33,57,39,59,PALE)
c.set(25,38,WHITE).set(25,39,GOLD_L)
c.set(56,32,PALE).set(57,33,GOLD_L)
c.set(53,52,GOLD_L).set(52,53,PALE)

# Tiny screw heads and engraved dots.
for x,y in [(31,25),(53,28),(55,46),(42,54),(27,48)]:
    c.set(x,y,STEEL_L)
    c.set(x+1,y,STEEL_D)

view(c, scale=8, margin=0)
finish(c)
