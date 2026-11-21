import random
from pixelbench_api import new_canvas, finish

rng = random.Random(20250412)

W = H = 16

BASE   = (74, 110, 48)   # mid grass green
LIGHT  = (118, 160, 72)  # light grass speckle
DARK   = (46, 76, 30)    # dark grass speckle
DIRT   = (116, 82, 44)   # bare dirt
DIRT2  = (96, 66, 34)
FLOWER = (252, 214, 74)  # flower center
PETAL  = (252, 240, 150) # pale petal / accent

c = new_canvas(W, H)

# Base grass fill with speckle noise (per-pixel)
for y in range(H):
    for x in range(W):
        r = rng.random()
        if r < 0.24:
            col = DARK
        elif r < 0.52:
            col = BASE
        else:
            col = LIGHT
        c.set(x, y, col)

# Sparse bare-dirt patches (avoid borders for seamless tiling)
def interior_area(minx, miny, maxx, maxy):
    return rng.randint(minx, maxx), rng.randint(miny, maxy)

patches = 3
for _ in range(patches):
    cx, cy = interior_area(3, 3, 11, 12)
    # little dirt blob
    wpx = rng.randint(2, 3)
    hpx = rng.randint(2, 3)
    for dy in range(hpx):
        for dx in range(wpx):
            if rng.random() < 0.75:
                col = DIRT if rng.random() < 0.6 else DIRT2
                c.set(min(W-1, cx+dx), min(H-1, cy+dy), col)

# A few single dirt flecks scattered widely
for _ in range(5):
    x, y = rng.randint(0, 15), rng.randint(0, 15)
    c.set(x, y, DIRT)

# Darker grass tufts: small 2-3 pixel clusters
for _ in range(7):
    x, y = rng.randint(2, 13), rng.randint(2, 13)
    c.set(x, y, DARK)
    # tiny extension
    if rng.random() < 0.8:
        dx, dy = rng.choice([(1,0),(0,1),(-1,0),(0,-1)])
        c.set((x+dx)%W, (y+dy)%H, DARK)

# Tiny yellow flowers (small cross)
flowers = 3
for _ in range(flowers):
    x, y = rng.randint(3, 12), rng.randint(3, 12)
    c.set(x, y, FLOWER)
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        if rng.random() < 0.7:
            c.set((x+dx)%W, (y+dy)%H, PETAL)

print(c.stats_text())
finish(c)
