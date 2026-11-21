from pixelbench_api import *

c = new_canvas(64, 64, background="#090807", name="open-pocket-watch")

# Palette
bg2 = "#12100d"; bg3 = "#1c1711"
shadow = "#23170b"; deep = "#3a240d"; brown = "#58370f"
bronze = "#805017"; brass = "#a86d20"; gold = "#d0922f"
lightgold = "#efbd58"; shine = "#ffe59a"; white = "#fff3c4"
copper = "#b85d24"; copper_hi = "#e78a3d"; redbrown = "#672714"
steel = "#8b8b7e"; steel_hi = "#d3d2b8"; black = "#070605"
cream = "#e8d6a5"; dialmid = "#bca66f"; dialshadow = "#6f5d37"
blue = "#27394a"

# Subtle macro backdrop and cast shadow.
c.dither(0, 0, 64, 64, ["#090807", bg2], pattern="bayer4")
c.ellipse(34, 39, 29, 20, "#050403")
c.ellipse(18, 27, 17, 18, "#080604")

# Chain behind the watch: paired pixel links.
chain_pts = [(45,5),(50,4),(55,6),(58,10),(56,14),(59,18),(62,21)]
for i in range(len(chain_pts)-1):
    x0,y0=chain_pts[i]; x1,y1=chain_pts[i+1]
    c.line(x0,y0,x1,y1,deep)
    c.line(x0,y0+1,x1,y1+1,gold)
for x,y in chain_pts[:-1]:
    c.circle(x,y,2,brown,fill=False)
    c.set(x,y-2,lightgold)
    c.set(x+1,y-1,gold)
# Crown and bow.
c.circle(40,8,5,deep)
c.circle(40,8,3,bg2)
c.line(37,5,43,11,brass); c.line(43,5,37,11,brass)
c.rect(38,11,5,4,deep); c.rect(39,11,3,3,gold)
c.set(39,11,shine)

# Open lid/dial at upper-left, dark outer rim then gold rim.
c.circle(20,27,18,shadow)
c.circle(20,27,17,bronze)
c.circle(20,27,15,lightgold)
c.circle(20,27,13,dialshadow)
c.circle(20,27,12,cream)
# Dial mottling / shadowed lower edge.
c.path("M9 27 Q11 38 21 40 Q29 39 32 31 Q27 37 20 37 Q12 36 9 27Z", dialmid)
c.path("M9 25 Q11 15 20 14 Q27 14 31 21 Q24 17 17 18 Q12 19 9 25Z", "#f3e4b8")
# Rim speculars.
c.path("M7 26 Q8 14 18 10", shine, fill=False)
c.path("M22 10 Q32 12 37 21", gold, fill=False)
c.line(9,35,14,40,brown)

# Dial tick marks: radial pixel lines.
import math
for i in range(12):
    a = math.radians(i*30-90)
    r0 = 9 if i%3 else 8
    x0=round(20+math.cos(a)*r0); y0=round(27+math.sin(a)*r0)
    x1=round(20+math.cos(a)*11); y1=round(27+math.sin(a)*11)
    c.line(x0,y0,x1,y1,deep)
# Minute ticks as single pixels.
for i in range(60):
    if i%5:
        a=math.radians(i*6-90)
        c.set(round(20+math.cos(a)*10.5),round(27+math.sin(a)*10.5),bronze)
# Hands and pinion.
c.line(20,27,16,20,black); c.line(20,27,27,29,black)
c.line(20,26,16,20,steel_hi); c.line(21,27,27,29,steel)
c.circle(20,27,2,deep); c.set(20,26,shine)
# Tiny dial print blocks.
c.rect(17,33,7,1,dialshadow); c.set(19,33,cream); c.set(22,33,cream)

# Hinge connecting dial to movement.
c.rect(31,35,8,8,deep)
c.rect(32,36,6,6,brass)
c.line(33,36,33,41,shine); c.line(37,37,37,41,brown)

# Main exposed movement casing, lower right.
c.circle(41,41,20,shadow)
c.circle(41,41,19,bronze)
c.circle(41,41,17,gold)
c.circle(41,41,15,deep)
# Plate fragments behind gear train.
c.path("M27 35 Q31 25 43 24 L48 28 L46 34 L39 35 L37 42 L29 43Z", brass)
c.path("M45 26 Q56 31 58 41 L54 45 L49 41 L50 35Z", gold)
c.path("M30 46 L38 42 L45 44 L49 54 Q38 59 30 52Z", bronze)
c.path("M42 36 L55 42 L53 52 L45 55 L39 48Z", "#6f4514")
# Plate bevel highlights.
c.line(29,34,35,27,lightgold); c.line(36,27,43,26,shine)
c.line(49,29,55,37,lightgold); c.line(30,50,36,55,gold)

# Gear helper: teeth and concentric rings.
def gear(cx,cy,r,teeth,base,hi,hub=2):
    for i in range(teeth):
        a=math.radians(i*360/teeth)
        x=round(cx+math.cos(a)*(r+1)); y=round(cy+math.sin(a)*(r+1))
        c.set(x,y,hi if i%3==0 else base)
    c.circle(cx,cy,r,deep)
    c.circle(cx,cy,r-1,base)
    # spokes cut dark then highlighted
    for i in range(0,teeth,2):
        a=math.radians(i*360/teeth)
        x=round(cx+math.cos(a)*(r-2)); y=round(cy+math.sin(a)*(r-2))
        c.line(cx,cy,x,y,deep)
    c.circle(cx,cy,hub,hi)
    c.set(cx,cy,white)

# Meshing train.
gear(37,34,6,14,gold,lightgold,2)
gear(48,37,5,12,brass,gold,1)
gear(43,47,7,16,copper,copper_hi,2)
gear(31,46,4,10,brass,lightgold,1)
gear(52,48,4,10,gold,shine,1)
# Jewel bearings.
for x,y in [(34,29),(53,33),(36,52),(49,53)]:
    c.circle(x,y,2,deep); c.circle(x,y,1,"#9e1e1b"); c.set(x,y,"#ff6a48")

# Balance wheel, lower-left of movement.
c.circle(32,53,6,lightgold,fill=False)
c.circle(32,53,5,bronze,fill=False)
for a in range(0,360,45):
    x=round(32+math.cos(math.radians(a))*5); y=round(53+math.sin(math.radians(a))*5)
    c.line(32,53,x,y,brass)
c.circle(32,53,2,deep); c.set(32,52,shine)
# Escapement fork.
c.line(26,48,29,51,steel_hi); c.line(26,48,28,46,steel)
c.set(25,47,shine)

# Screws on movement plate.
for x,y in [(43,27),(55,42),(41,56),(27,39)]:
    c.circle(x,y,1,steel)
    c.set(x,y,steel_hi)
    c.set(x+1,y,deep)

# Outer case bevel, interrupted glints and lower dark contour.
c.path("M24 40 Q24 26 38 22 Q50 20 58 31", lightgold, fill=False)
c.path("M58 33 Q63 47 53 57 Q41 65 29 57", brown, fill=False)
c.line(29,58,38,61,bronze); c.line(40,61,48,59,gold)
c.set(27,32,white); c.set(28,29,shine); c.set(52,25,shine)
c.set(59,40,lightgold); c.set(57,52,gold)

# High-contrast pixel reflections and scratches.
c.line(34,24,40,23,white)
c.line(53,29,56,34,shine)
c.line(24,42,24,48,gold)
c.set(25,50,shine); c.set(29,57,lightgold)
c.line(45,58,51,55,lightgold)
# A few black occlusion accents improve gear separation.
c.set(42,39,black); c.set(44,40,black); c.set(39,43,black)
c.set(48,44,black); c.set(35,40,black)

finish(c)
view(c, scale=8, margin=0)
