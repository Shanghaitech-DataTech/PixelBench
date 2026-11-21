# Forest slime monster - 32x32 RPG enemy sprite
c = new_canvas(32, 32, name="forest-slime")

OUT    = "#1e3d1e"   # dark outline
BODY   = "#58b849"   # slime green
LIGHT  = "#8fdc6a"   # highlight
SHADE  = "#3a8a3a"   # shading
MOSS   = "#3f6d28"   # moss base
MOSSL  = "#61903c"   # moss specks
ANTLER = "#8a5a33"   # antler brown
ANTL   = "#b07a45"   # antler tip
EYE    = "#8ef0ff"   # glowing eye
WHITE  = "#ffffff"
GLOW   = "#4fc0c9"   # eye glow halo
BLUSH  = "#4aa54a"
CAP    = "#d8453c"   # mushroom cap
CAPD   = "#a8322c"   # cap underside
STEM   = "#f2e3c0"   # mushroom stem
SHADOW = "#17301c"   # ground shadow

# ---- body dome ----
pts = [(16,9),(21,10),(24,13),(26,17),(27,22),(27,27),(26,29),
       (6,29),(5,27),(5,22),(6,17),(8,13),(11,10)]
c.poly(pts, BODY)
c.outline(OUT)

# ---- ground shadow ----
c.line(8,29,24,29,SHADOW)
c.set(7,29,SHADOW); c.set(25,29,SHADOW)

# ---- moss cap on head ----
for y,(x0,x1) in {9:(15,17),10:(12,20),11:(10,22),12:(10,22)}.items():
    for x in range(x0,x1+1):
        c.set(x,y,MOSS)
for x0,x1 in [(10,12),(15,18),(21,22)]:      # scalloped fringe
    for x in range(x0,x1+1):
        c.set(x,13,MOSS)
for x in (11,17,21):
    c.set(x,14,MOSS)
for x,y in [(13,10),(18,11),(14,12),(19,12),(16,13),(11,13)]:
    c.set(x,y,MOSSL)

# ---- tiny antlers ----
for x,y in [(12,9),(12,8),(12,7),(11,6),(11,5),(13,6)]:
    c.set(x,y,ANTLER)
c.set(11,5,ANTL)
for x,y in [(20,9),(20,8),(20,7),(19,6),(19,5),(21,6)]:
    c.set(x,y,ANTLER)
c.set(19,5,ANTL)

# ---- glowing eyes ----
for cx in (12,20):
    for dy in (-1,0,1):
        for dx in (-1,0,1):
            c.set(cx+dx,19+dy,EYE)
    c.set(cx,19,WHITE)
    c.set(cx,17,GLOW); c.set(cx,21,GLOW)

# ---- mouth + blush ----
for x,y in [(14,23),(17,23),(15,24),(16,24)]:
    c.set(x,y,OUT)
for x,y in [(10,21),(9,21),(22,21),(23,21)]:
    c.set(x,y,BLUSH)

# ---- mushroom on back ----
c.rect(25,15,2,3,STEM)
for y,(x0,x1) in {12:(24,27),13:(23,28),14:(23,28)}.items():
    c.rect(x0,y,x1-x0+1,1,CAP)
c.rect(24,15,4,1,CAPD)
c.set(25,13,WHITE); c.set(27,14,WHITE)
for x in range(24,28): c.set(x,11,OUT)      # cap outline
c.set(23,12,OUT); c.set(29,13,OUT); c.set(29,14,OUT); c.set(28,15,OUT)
c.set(23,15,OUT)

# ---- moss specks on body ----
for x,y in [(7,19),(7,20),(8,25),(24,23),(23,24)]:
    c.set(x,y,MOSS)
c.set(8,19,MOSSL)

# ---- highlights & shading ----
for x,y in [(9,14),(10,14),(9,15),(10,15),(11,15),(9,16)]:
    c.set(x,y,LIGHT)
c.rect(7,28,19,1,SHADE)
c.rect(6,27,4,1,SHADE); c.rect(23,27,4,1,SHADE)
for y in (22,23,24,25):
    c.set(26,y,SHADE)

print(c.stats_text())
finish(c)
