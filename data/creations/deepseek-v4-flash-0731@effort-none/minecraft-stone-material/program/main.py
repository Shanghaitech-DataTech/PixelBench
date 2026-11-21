from pixelbench_api import *

W = H = 16
c = new_canvas(W, H, background=None, name="stone")

# Palette (<=10 colors)
c.color((122, 122, 125), name="base")       # 0 base stone (dominant)
c.color((134, 134, 137), name="light")      # 1
c.color((110, 110, 113), name="dark")       # 2
c.color((144, 144, 147), name="light2")     # 3 accent
c.color((40, 40, 44), name="crack")        # 4 deep crack
c.color((64, 64, 68), name="crackedge")    # 5 sunken edge
c.color((100, 100, 104), name="dark2")     # 6

c.rect(0, 0, W, H, "base")

def px(x, y, col):
    c.set(x % W, y % H, col)

def hashv(x, y):
    h = x * 374761393 + y * 668265263
    h = (h ^ (h >> 13)) * 1274126177
    h = h ^ (h >> 16)
    return h & 0x7fffffff

# Fine tileable speckle - deviate only ~13% of pixels from base
for y in range(H):
    for x in range(W):
        h = hashv(x, y)
        r = h % 52
        if r == 0:
            px(x, y, "light2")
        elif r == 1 or r == 2:
            px(x, y, "light")
        elif r == 3 or r == 4:
            px(x, y, "dark")
        elif r == 5 or r == 6:
            px(x, y, "dark2")

# --- Cracks (seamless via wrap) ---
def seg(x0, y0, x1, y1, col):
    x = x0; y = y0
    dx = abs(x1-x0); sx = 1 if x0<x1 else -1
    dy = -abs(y1-y0); sy = 1 if y0<y1 else -1
    err = dx+dy
    while True:
        px(x, y, col)
        if x==x1 and y==y1: break
        e2 = 2*err
        if e2 >= dy: err += dy; x += sx
        if e2 <= dx: err += dx; y += sy

def poly(pts, col, closed=True):
    n = len(pts)
    rng = range(n) if closed else range(n-1)
    for i in rng:
        p0 = pts[i]; p1 = pts[(i+1) % n]
        for ox in (-W, 0, W):
            for oy in (-H, 0, H):
                seg(p0[0]+ox, p0[1]+oy, p1[0]+ox, p1[1]+oy, col)

# Main jagged crack
poly([(0,5),(3,4),(6,5),(9,3),(12,5),(16,4)], "crack")
poly([(2,5),(5,6),(8,4),(11,6),(15,4)], "crackedge")

# Vertical branch from main crack to bottom
poly([(9,3),(10,6),(9,9),(10,12),(9,15)], "crack")

# Upper small crack zone
poly([(5,0),(6,2),(5,4),(7,5),(8,4)], "crack")
poly([(6,1),(7,3),(6,5),(8,6)], "crackedge")

# Lower area crack fragments
poly([(0,13),(2,12),(4,13),(5,14)], "crack")
poly([(13,8),(14,10),(15,11),(16,12)], "crack")
poly([(11,14),(12,13),(14,14),(15,16)], "crack")

print(c.stats_text())
view(c)
finish(c)
