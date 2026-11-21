from pixelbench_api import *
import random

random.seed(7)

c = new_canvas(128, 128, name="alley")

def col(h): return c.color(h)

# ---- palette ----
sky0 = col('#050512')
sky1 = col('#09091f')
sky2 = col('#0e0e2b')
sky3 = col('#15153a')
sky4 = col('#1c1c46')
build  = col('#07070f')
build2 = col('#0c0c1a')
build3 = col('#121226')
build4 = col('#181831')
pav    = col('#0a0a13')
pav2   = col('#10101c')
distant= col('#1a1a38')
dwin   = col('#ffe27a')

pink  = col('#ff0090')
cyan  = col('#00c0ff')
yel   = col('#ffcc00')
grn   = col('#00e08a')
red   = col('#ff3b3b')
softy = col('#ffd75e')
softc = col('#59dfff')
white = col('#e8ecff')

pudbase  = col('#141538')
puddark  = col('#0e0f26')
refl_c   = col('#1f5f8a')
refl_p   = col('#6b1f5e')
refl_y   = col('#6b5a20')

vend_d  = col('#0d1a2e')
vend_l  = col('#1c3a55')
vend_g  = col('#16324a')

coatshade = col('#0f0e20')
coathl    = col('#241f4a')
hair      = col('#05050c')
umbli     = col('#bfe9ff')
umbrib    = col('#7ab8e0')
skin      = col('#3a2d4a')
leg       = col('#0a0a16')

rain  = col('#5f8fc4')
rain2 = col('#b8d0ee')

# ---- sky gradient (rows 0..72) ----
steps = [sky0,sky1,sky2,sky3,sky4]
n = len(steps)
for y in range(73):
    c.rect(0,y,128,1,steps[min(y* n // 73, n-1)])

# distant central building (receding alley end)
c.rect(50,34,28,50,distant)
# windows on distant building
for (wx,wy) in [(54,38),(60,38),(66,38),(72,38),(54,45),(60,45),(66,45),(72,45),
                (54,56),(60,56),(66,56),(72,56),(56,70),(66,70)]:
    c.rect(wx,wy,3,3,dwin)
# small sky-glare behind distant building
c.rect(46,40,36,2,sky4)

# ---- left tower ----
c.rect(0,14,48,86,build)
c.rect(0,14,48,82,build)
# left tower face lighter edge + windows
c.rect(0,20,48,60,build2)
for yy in range(24,78,8):
    c.rect(3,yy,6,4,col('#10102a'))
    c.rect(34,yy,10,4,col('#10102a'))

# ---- right tower ----
c.rect(80,16,48,86,build)
c.rect(84,16,44,80,build3)
for yy in range(22,80,9):
    c.rect(88,yy,7,5,col('#14142f'))

# roofline details on towers
c.rect(0,10,6,10,build)
c.rect(2,4,4,6,build)
c.rect(122,8,6,14,build)
c.rect(124,2,4,6,build)

# antenna cables hang from roof corners
for ax in (0,10,116,127):
    c.line(ax,14, ax, 30, build)

# ---- ground / pavement ----
c.rect(0,102,128,26,pav)
# ground gradient darker where wet
for y in range(102,128):
    shade = pav if y < 112 else pav2
    c.rect(0,y,128,1,shade)

# pavement seams
for sx in range(0,128,16):
    c.line(sx,102,sx,127,pav)
c.line(0,113,127,113,pav)
c.line(0,121,127,121,pav)

# ---- neon sign on LEFT tower (pink) ----
# glow
c.rect(8,30,30,30,col((255,0,144,45)))
c.rect(10,32,26,26,col((255,0,144,80)))
c.rect(11,33,24,24,col('#7a0a55'))
c.rect(11,33,24,23,pink)
c.text(15,37,'NET', pink, font='5x7')
c.rect(15,45,16,3,col('#ff5ab0'))
# sign border highlights
c.line(11,33,11,56,white)

# ---- neon sign on RIGHT tower (cyan vertical) ----
c.rect(92,28,26,44,col((0,160,255,45)))
c.rect(94,29,22,42,col((0,160,255,80)))
c.rect(95,30,20,40,col('#062a4a'))
c.rect(95,30,20,40,cyan)
c.text(98,34,'PIX',cyan,font='5x7')
c.text(98,44,'ART',cyan,font='5x7')
c.line(98,54,112,54,cyan)

# yellow sign on right
c.rect(88,64,34,12,col((255,180,0,45)))
c.rect(89,65,32,10,col((180,120,0,80)))
c.rect(90,66,30,8,yel)
c.text(94,67,'BAR', build2, font='5x7')

# green small sign left
c.rect(8,62,22,8,col((0,220,140,40)))
c.rect(9,63,20,6,grn)
c.text(10,64,'DX', build, font='5x7')

# ---- light pools on ground reflecting neon ----
# pink pool under left sign
c.ellipse(26,116,16,8,col((255,0,144,60)))
c.ellipse(24,116,10,5,refl_p)
# cyan pool under right sign
c.ellipse(104,119,20,8,col((0,160,255,55)))
c.ellipse(102,118,13,5,refl_c)
# yellow pool
c.ellipse(70,124,26,4,col((255,190,0,40)))

# ---- power cables across top, sagging ----
import math
def cable(x0,y0,x1,y1,sag,colr):
    pts=[]
    steps_n=24
    for i in range(steps_n+1):
        t=i/steps_n
        x=x0+(x1-x0)*t
        y=y0+(y1-y0)*t + sag*4*t*(1-t)
        pts.append((x,y))
    for i in range(len(pts)-1):
        c.line(round(pts[i][0]),round(pts[i][1]),round(pts[i+1][0]),round(pts[i+1][1]),colr)

cable(0,18,48,26,4,build3)
cable(80,16,128,20,4,build3)
cable(14,24,126,24,9,build3)
cable(2,12,126,12,5,build2)
# short dropper lines
c.line(34,16,34,30,build3)
c.line(96,17,96,30,build3)

# ---- vending machines (left, on ground) ----
c.rect(52,86,16,34,vend_d)
c.rect(53,87,14,16,vend_g)
c.rect(72,90,14,30,vend_d)
c.rect(72,90,14,6,col((0,220,140,70)))
c.rect(73,91,13,9,grn)
c.rect(73,100,2,6,white)
c.rect(80,100,2,6,white)
# vending interior rows
c.rect(54,90,11,14,col('#0a1825'))
for ry in range(91,103,4):
    c.rect(55,ry,3,3,col((80,220,255,90)))
    c.rect(60,ry,3,3,col((255,120,180,90)))
    c.rect(64,ry,4,3,col((255,200,80,90)))

# ---- person with transparent umbrella, center ----
# umbrella first (behind nothing important)
umb_x,umb_y=84,70
# umbrella stick
c.line(84,86,84,112,umbbuild:=col('#20202c'))
# hand on stick
c.line(80,94,88,92,coathl)
# dome (semi-transparent cyan)
dome=col((175,225,255,90))
c.path(f"M66,{umb_y} A18,20 0 0 1 102,{umb_y} Z", dome, fill=True)
# umbrella ribs
c.line(66,70,84,86,umbrib)
c.line(84,86,102,70,umbrib)
c.line(75,68,84,86,umbrib)
c.line(93,68,84,86,umbrib)
c.line(84,50,84,86,umbrib)
# umbrella tip
c.rect(83,64,3,4,col((30,60,100)))
# head (under umbrella)
c.rect(80,88,9,10,skin)
c.rect(80,88,9,3,hair)
c.rect(81,91,7,2,hair)
# body / coat
c.poly([(79,96),(89,96),(92,116),(76,116)],coathl)
c.poly([(82,98),(86,98),(88,112),(80,112)],coatshade)
# arm to umbrella
c.poly([(89,98),(100,96),(101,94),(89,96)],coathl)
# umbrella stick continue past hand, visible
c.line(84,86,84,100,umbbuild)
# legs
c.rect(80,112,4,8,leg)
c.rect(86,112,4,8,leg)
# reflection in puddle below person
c.line(80,120,92,120,coathl, )

# person rim light from sign (cyan edge)
c.line(89,97,89,112,col((90,180,255,120)))

# ---- rain ----
for _ in range(170):
    x=random.randint(0,127)
    y=random.randint(0,124)
    colr = rain if random.random()<0.7 else rain2
    ln=random.randint(3,5)
    c.line(x,y,x,y+ln,colr)

# a brighter gouache mist near light pools
for _ in range(40):
    x=random.randint(14,36); y=random.randint(112,126)
    c.set(x,y,col((150,190,255,70)))

finish(c)
print(c.stats_text())
