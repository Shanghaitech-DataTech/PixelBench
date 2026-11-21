from pixelbench_api import *

c = new_canvas(32, 32)

OUT    = c.color("#151515")
M_DARK = c.color("#7d7d7d")
M_MID  = c.color("#a9a9a9")
M_LIT  = c.color("#d7d7d7")
M_HI   = c.color("#f4f4f4")
M_SH   = c.color("#3f3f3f")

# Mail hauberk silhouette (broader shoulders, straight torso, flared hem)
rows = {
 3: [12, 19],
 4: [10, 21],
 5: [7, 24],
 6: [5, 26],
 7: [5, 26],
 8: [5, 26],
 9: [6, 25],
 10:[6, 25],
 11:[7, 24],
 12:[7, 24],
 13:[8, 23],
 14:[8, 23],
 15:[9, 22],
 16:[9, 22],
 17:[10,21],
 18:[10,21],
 19:[10,21],
 20:[11,20],
 21:[11,20],
 22:[11,20],
 23:[12,19],
}

# Fill base
for y,(x0,x1) in rows.items():
    for x in range(x0,x1+1):
        c.set(x,y,M_MID)
# Outline
for y,(x0,x1) in rows.items():
    c.set(x0,y,OUT); c.set(x1,y,OUT)
# inner rim shadow
for y,(x0,x1) in rows.items():
    if x0+1<=x1: c.set(x0+1,y,M_DARK)
    if x1-1>=x0: c.set(x1-1,y,M_DARK)

# Chainmail texture: ring bands with clean interlock
def band(oy):
    flip=(oy//2)%2==1
    base=8 if flip else 6
    for rx in range(base,28,4):
        # upper row of the oval ring
        for dx,col in ((0,M_LIT),(1,M_MID),(2,M_DARK)):
            px,py=rx+dx,oy
            if py in rows and rows[py][0]<px<rows[py][1]: c.set(px,py,col)
        # lower row
        for dx,col in ((0,M_MID),(1,M_DARK)):
            px,py=rx+dx,oy+1
            if py in rows and rows[py][0]<px<rows[py][1]: c.set(px,py,col)
        # gap (dark hole) at right end of the oval
        px,py=rx+3,oy+1
        if py in rows and rows[py][0]<px<rows[py][1]: c.set(px,py,M_SH)

oy=5
while oy<23:
    band(oy); oy+=2

# Neck cavity
for y in (3,4):
    x0,x1=rows[y]
    for x in range(x0+1,x1):
        c.set(x,y,M_SH)

# Pauldron caps + shading (light from upper-left)
for x in range(8,17):
    if rows[5][0]<x<rows[5][1]: c.set(x,5,M_HI)
for x in range(6,9):
    if rows[6][0]<x<rows[6][1]: c.set(x,6,M_LIT)
for x in range(23,26):
    if rows[5][0]<x<rows[5][1]: c.set(x,5,M_DARK)

# chest sheen (smooth left highlight column-ish)
for y in (8,9,10):
    x0,x1=rows[y]
    lit = [M_LIT,M_HI if y==8 else M_LIT, M_MID]
    for i,x in enumerate(range(x0+2,x0+5)):
        if rows[y][0]<x<rows[y][1]: c.set(x,y,lit[i] if i<len(lit) else M_MID)

# right body shading (subtle, last 1 column)
for y in range(7,20):
    x0,x1=rows[y]
    x=x1-1
    if rows[y][0]<x<rows[y][1]:
        cur=c.get(x,y)
        if cur not in (OUT,): c.set(x,y,M_DARK)

# belt
for y in (16,17,18):
    x0,x1=rows[y]
    for x in range(x0+1,x1):
        c.set(x,y,M_SH)
# buckle
for x in range(14,18):
    if rows[16][0]<x<rows[16][1]:
        c.set(x,16,M_MID); c.set(x,17,M_LIT); c.set(x,18,M_DARK)
c.set(14,16,OUT); c.set(17,16,OUT)

# hem dark bottom edge
for y in (22,23):
    x0,x1=rows[y]
    for x in range(x0+1,x1):
        c.set(x,y,M_DARK)

print(c.stats_text())
save("chainmail_armor", c)
finish(c)
