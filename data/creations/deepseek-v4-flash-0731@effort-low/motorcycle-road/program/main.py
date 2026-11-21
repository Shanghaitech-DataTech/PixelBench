from pixelbench_api import *

inp = canvas(-1)
white = inp.color('#ffffff')

W,H = 96,64
out = new_canvas(W, H, name="output")

sky    = out.color('#7FBEEB')
sky2   = out.color('#A8D6F2')
hill   = out.color('#8FCD66')
grass  = out.color('#7FBF3F')
field  = out.color('#C9E397')
road   = out.color('#707070')
road2  = out.color('#5A5A5A')
road3  = out.color('#828282')
line   = out.color('#F0E040')
trunk  = out.color('#6B4226')
leaf   = out.color('#2E7D32')
cloud  = '#FFFFFF'

out.rect(0,0,W,11,sky)
out.rect(0,8,W,4,sky2)
for cx,cy in [(8,4),(30,6),(54,3),(70,6),(88,4)]:
    out.circle(cx,cy,2,cloud)
    out.circle(cx+3,cy,2,cloud)
    out.circle(cx+1,cy-1,2,cloud)
    out.circle(cx+2,cy,2,cloud)

out.rect(0,12,W,7,hill)
out.rect(0,18,W,5,field)
out.rect(0,22,W,16,grass)

out.poly([(30,38),(66,36),(70,60),(26,62)], road)
out.line(30,38,66,36, road2)
out.line(26,62,70,60, road3)

# dashed center line (proper: follow road)
for t in range(6):
    y0 = 38 + t*4
    x = 30 + int(t*40/24)
    out.rect(x, y0, 3, 1, line)

def tree(x, base):
    out.rect(x, base, 2, 5, trunk)
    out.circle(x+1, base-4, 3, leaf)
    out.circle(x-1, base-2, 3, leaf)
    out.circle(x+3, base-2, 3, leaf)
    out.circle(x+2, base-6, 2, leaf)
tree(3,36); tree(20,37); tree(74,37); tree(89,36)

dx=22; dy=4
for y in range(64):
    for x in range(64):
        idx = inp.get(x,y)
        if idx != white:
            out.set(x+dx, y+dy, idx)

print(out.matrix_text(region=(18,20,80,56)))
finish(out)

