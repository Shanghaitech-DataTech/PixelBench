from pixelbench_api import new_canvas, finish
import random

W = H = 16
c = new_canvas(W, H)

def seed(x, y):
    x &= 7; y &= 7
    h = (x*131 + y*263 + 17) % 1024
    r = random.Random(h)
    return r.random()

def smooth(t):
    return t*t*(3-2*t)

def value_noise(x, y):
    xi = x // 4; yi = y // 4
    xf = (x % 4) / 4.0; yf = (y % 4) / 4.0
    def g(ix, iy):
        return seed(ix & 3, iy & 3)
    v00 = g(xi, yi); v10 = g(xi+1, yi)
    v01 = g(xi, yi+1); v11 = g(xi+1, yi+1)
    sx = smooth(xf); sy = smooth(yf)
    return (v00*(1-sx)+v10*sx)*(1-sy) + (v01*(1-sx)+v11*sx)*sy

cracks = [
    [(1,3),(3,2),(6,4),(8,3),(10,5),(13,4),(15,5)],
    [(0,8),(2,9),(4,7),(7,8),(9,10),(12,9),(14,11),(15,10)],
    [(4,12),(6,14),(8,12),(10,13),(12,15),(13,14)],
    [(6,1),(7,3),(8,6),(9,7)],
]

BL = (150,150,150)
LA = (134,134,134)
MD = (120,120,120)
DA = (105,105,105)
CR = (72,72,72)
CD = (48,48,48)

for y in range(H):
    for x in range(W):
        n = value_noise(x, y)
        if n < 0.38: col = DA
        elif n < 0.72: col = MD
        else: col = LA
        if n > 0.93 and ((x*7+y*13) % 9 == 0):
            col = BL
        c.set(x, y, col)

def draw_crack(pts, dark, core):
    for i in range(len(pts)-1):
        p0 = pts[i]; p1 = pts[i+1]
        steps = max(abs(p1[0]-p0[0]), abs(p1[1]-p0[1]), 1)
        for s in range(steps+1):
            px = p0[0] + (p1[0]-p0[0])*s/steps
            py = p0[1] + (p1[1]-p0[1])*s/steps
            for ox in (-16,0,16):
                for oy in (-16,0,16):
                    cx = int(round(px))+ox; cy = int(round(py))+oy
                    if 0 <= cx < 16 and 0 <= cy < 16:
                        c.set(cx, cy, dark)
        for s in range(steps-1):
            px = p0[0] + (p1[0]-p0[0])*(s+0.5)/steps
            py = p0[1] + (p1[1]-p0[1])*(s+0.5)/steps
            for ox in (-16,0,16):
                for oy in (-16,0,16):
                    cx = int(round(px))+ox; cy = int(round(py))+oy
                    if 0 <= cx < 16 and 0 <= cy < 16:
                        c.set(cx, cy, core)

for pts in cracks:
    draw_crack(pts, CR, CD)

speck = [(1,2),(5,3),(7,2),(9,2),(0,7),(3,8),(8,7),(11,8),(13,10),(15,9),
         (3,11),(7,13),(10,14),(5,13),(9,13),(6,0),(7,2),(8,5),(9,6),(5,6)]
for (x,y) in speck:
    for ox in (-16,0,16):
        for oy in (-16,0,16):
            cx = x+ox; cy = y+oy
            if 0 <= cx < 16 and 0 <= cy < 16:
                c.set(cx, cy, DA)

finish(c)
