# 64x64 open mechanical pocket watch
c = new_canvas(64, 64, background="#08090b", name="open_pocket_watch")

# Palette: cool background, aged gold, steel, and high-contrast reflections.
bg1 = "#0d1013"; bg2 = "#15191c"; bg3 = "#202326"
black = "#050607"; deep = "#21160b"; brown = "#3a240d"; umber = "#593814"
bronze = "#75501f"; gold0 = "#956a28"; gold1 = "#b98736"; gold2 = "#d5a94f"
gold3 = "#efd476"; glint = "#fff0aa"; ivory = "#d8c99f"
steel0 = "#343b40"; steel1 = "#687178"; steel2 = "#b1bac0"; white = "#f4edd0"
red = "#7b2c1f"; ruby = "#c84b32"

# Subtle macro backdrop with hard pixel clusters.
c.rect(0, 0, 64, 64, bg1)
c.dither(0, 42, 64, 22, [bg1, bg2], pattern="bayer4")
c.rect(2, 3, 15, 2, bg2); c.rect(5, 5, 9, 1, bg3)
c.rect(49, 57, 12, 2, bg2); c.rect(53, 55, 8, 1, bg3)
c.set(3, 39, bg3); c.set(58, 17, bg3); c.set(61, 38, bg2)

# Open lid behind the watch, tilted to upper-left.
c.ellipse(18, 19, 14, 15, black)
c.ellipse(18, 19, 13, 14, bronze)
c.ellipse(18, 19, 11, 12, deep)
c.ellipse(18, 19, 10, 11, steel0)
c.ellipse(18, 19, 9, 10, bg2)
# Lid interior reflections and concentric machining.
c.path("M9 14 Q12 7 20 7 Q26 8 29 14", gold2, fill=False)
c.path("M7 19 Q8 10 15 7", gold3, fill=False)
c.path("M9 26 Q15 32 23 29", gold0, fill=False)
c.line(9, 11, 11, 9, glint); c.line(7, 16, 7, 21, gold3)
c.set(25, 9, gold3); c.set(28, 13, gold1); c.set(9, 27, umber)
# Hinge joining lid to body.
c.rect(18, 30, 9, 5, deep); c.rect(19, 30, 8, 3, gold1)
c.rect(20, 30, 2, 4, gold3); c.rect(24, 30, 2, 4, bronze)

# Chain, crown and bow at upper right.
# Chain links are dark under-lines plus alternating metal highlights.
chain_pts = [(43,17,47,12),(48,11,53,9),(54,9,58,11),(58,12,57,16),(58,17,61,20),(61,21,59,25)]
for x0,y0,x1,y1 in chain_pts:
    c.line(x0,y0,x1,y1,deep)
    c.set(x0,y0,gold2); c.set(x1,y1,gold3)
# Link gaps/details.
c.rect(48,10,4,2,gold0,fill=False); c.rect(54,9,4,3,gold1,fill=False)
c.rect(57,13,3,4,gold2,fill=False); c.rect(59,19,3,4,gold0,fill=False)
# Crown stem and ridged crown.
c.rect(39,14,5,5,deep); c.rect(40,14,3,6,gold1); c.set(41,14,gold3)
c.rect(42,10,7,5,deep); c.rect(43,10,5,4,gold1)
for x in (43,45,47): c.line(x,10,x,13,gold3)
# Bow loop.
c.ellipse(41,10,6,7,deep,fill=False); c.ellipse(41,10,5,6,gold2,fill=False)
c.line(37,5,40,3,gold3); c.line(42,3,46,6,gold1)

# Main watch case: heavy stepped rim.
c.circle(34,40,23,black)
c.circle(34,40,22,deep)
c.circle(34,40,21,gold0)
c.circle(34,40,19,gold3)
c.circle(34,40,18,bronze)
c.circle(34,40,17,deep)
# Case shadow and bright bevel segments.
c.path("M15 39 Q15 25 27 20", gold3, fill=False)
c.path("M18 51 Q24 60 37 61", gold2, fill=False)
c.path("M43 21 Q53 27 55 38", glint, fill=False)
c.path("M53 46 Q49 56 40 59", umber, fill=False)
c.line(17,32,18,27,glint); c.line(50,26,53,31,gold2)

# Dark movement plate and exposed golden bridges.
c.circle(34,40,15,steel0)
c.circle(34,40,14,deep)
c.path("M23 29 Q29 24 36 26 L34 31 Q29 30 26 35 L22 34 Z", gold1)
c.path("M39 27 Q48 30 49 38 L44 39 Q43 33 37 32 Z", gold0)
c.path("M23 45 Q27 53 37 54 L38 49 Q31 48 29 42 Z", bronze)
c.path("M39 44 Q45 42 49 46 Q47 52 42 55 L39 51 Z", gold1)
# Bridge bevels.
c.line(24,29,34,27,gold3); c.line(40,28,47,32,gold2)
c.line(24,46,30,51,gold2); c.line(41,53,46,48,gold3)

# Gear helper: toothed perimeter, hub, and spokes.
def gear(cx, cy, r, teeth, dark_col=deep, rim=gold2, hi=gold3):
    import math
    c.circle(cx, cy, r, dark_col)
    c.circle(cx, cy, r-1, rim, fill=False)
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        x = round(cx + math.cos(a) * (r + 1))
        y = round(cy + math.sin(a) * (r + 1))
        c.set(x, y, rim if i % 2 else hi)
    for i in range(0, teeth, 2):
        a = 2 * math.pi * i / teeth
        c.line(cx, cy, round(cx + math.cos(a)*(r-1)), round(cy + math.sin(a)*(r-1)), bronze)
    c.circle(cx, cy, 1, ivory)
    c.set(cx, cy, steel0)

# Meshing gear train.
gear(29,36,6,12)
gear(40,35,5,10, brown, gold1, gold3)
gear(38,46,6,12)
gear(26,47,4,8, deep, gold0, gold2)
# Small steel escapement and jewel bearings.
c.circle(46,43,3,steel1,fill=False); c.line(43,43,49,43,steel2); c.line(46,40,46,46,steel2)
c.circle(46,43,1,ruby); c.set(46,43,white)
for x,y in [(22,40),(34,28),(43,52),(31,53)]:
    c.circle(x,y,1,red); c.set(x,y,ruby)

# Fine screws on the bridges.
for x,y in [(25,30),(45,32),(25,49),(44,49)]:
    c.circle(x,y,1,steel2); c.set(x,y,steel0)

# Partial dial/chapter ring over the movement.
c.circle(34,40,16,ivory,fill=False)
c.circle(34,40,15,gold3,fill=False)
# Minute ticks, with heavier cardinal marks.
import math
for i in range(60):
    a = 2 * math.pi * i / 60 - math.pi/2
    ro = 15
    ri = 12 if i % 5 == 0 else 14
    x0 = round(34 + math.cos(a)*ri); y0 = round(40 + math.sin(a)*ri)
    x1 = round(34 + math.cos(a)*ro); y1 = round(40 + math.sin(a)*ro)
    c.line(x0,y0,x1,y1,white if i % 5 == 0 else gold2)
# Numeral-like block accents at 12, 3, 6, 9.
c.rect(33,24,2,3,white); c.rect(48,39,3,2,white)
c.rect(33,54,2,3,white); c.rect(18,39,3,2,white)

# Hands and center pin: dark outline then polished fill.
c.line(34,40,31,29,black); c.line(35,40,32,29,black)
c.line(34,40,45,44,black); c.line(34,41,45,45,black)
c.line(34,40,32,29,steel2); c.set(32,29,white)
c.line(34,40,44,44,gold3); c.set(45,44,glint)
c.circle(34,40,2,deep); c.circle(34,40,1,glint); c.set(34,40,steel0)

# Foreground case sparkle and grounded contact shadow.
c.line(12,62,48,62,black); c.line(19,61,44,61,bg3)
c.set(14,36,white); c.set(15,34,gold3); c.set(53,35,glint)
c.set(50,53,gold3); c.set(47,57,gold2); c.set(21,56,gold3)

view(c, scale=8, margin=0)
finish(c)
