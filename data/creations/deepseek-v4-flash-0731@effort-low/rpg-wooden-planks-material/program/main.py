from pixelbench_api import *

# Palette
baseL   = (203,154,92)    # light wood
baseD   = (168,116,60)    # dark wood
grainD  = (122,82,36)
grainV  = (94,62,28)
seam    = (58,36,14)
shade   = (128,88,42)     # joint shadow
light   = (219,175,114)   # light grain highlight
knot    = (70,44,18)
knotC   = (46,29,12)

c = new_canvas(16,16)
bases = {0:baseL, 4:baseD, 8:baseL, 12:baseD}

# 4 vertical boards of width 4
for x0 in [0,4,8,12]:
    c.rect(x0,0,4,16,bases[x0])

# vertical grain lines (inside boards)
grain_map = {
    0: {1:grainD,3:light},
    4: {0:grainV,3:grainD},
    8: {2:grainV,1:light},
   12: {0:grainD,2:grainV},
}
for x0, offs in grain_map.items():
    for off,col in offs.items():
        c.line(x0+off,0,x0+off,15,col)

# dark seam grooves between planks (incl. tile seam at x=15)
for sx in [3,7,11,15]:
    c.line(sx,0,sx,15,seam)
    # shading right of groove to deepen it
    c.line((sx+1)%16,0,(sx+1)%16,15,shade)

# alternating board ends (brick joints): even cols at y=5, odd cols at y=13
for x0 in [0,8]:
    c.rect(x0,5,4,1,seam)
    c.rect(x0,6,4,1,shade)
for x0 in [4,12]:
    c.rect(x0,13,4,1,seam)
    c.rect(x0,14,4,1,shade)

# knots (avoid seams/edges for clean tiling)
c.ellipse(10,3,1,1,knot)     # knot in board2
c.set(9,2,knotC); c.set(10,2,knot); c.set(11,3,knot)
# tiny knot in board0
c.set(2,10,knot); c.set(3,10,knotC); c.set(2,11,knot); c.set(3,11,knotC)

print(c.stats_text())
print(c.matrix_text(region=(0,0,15,15)))
finish(c)
