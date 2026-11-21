from pixelbench_api import new_canvas, finish
import random

W = H = 16
c = new_canvas(W, H, name="rpg-grass-material")

base   = c.color("#4d8c3a")
mid    = c.color("#42823a")
dark   = c.color("#3a732d")
light  = c.color("#69ab50")
vlight = c.color("#79bb59")
tuft   = c.color("#2c5523")
flower = c.color("#f9d84e")
dirt   = c.color("#8a6a44")
dirtd  = c.color("#6f5536")

def h2(x, y):
    n = ((x % W) * 374761393 + (y % H) * 668265263 + 0x5f3759df) & 0xffffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0xffffffff
    return n

# base fill
c.rect(0, 0, W, H, base)

# interleaved speckles (periodic hash -> seamless)
for y in range(H):
    for x in range(W):
        r = (h2(x, y) & 0xffff) / 65536.0
        if r < 0.26:
            c.set(x, y, dark)
        elif r < 0.50:
            c.set(x, y, light)
        elif r < 0.58:
            c.set(x, y, vlight)
        elif r < 0.68:
            c.set(x, y, mid)

def wset(x, y, col):
    c.set(x % W, y % H, col)

rng = random.Random(20240607)

# small darker grass tufts (3-pixel blade clusters, wrap-around)
for _ in range(6):
    x = rng.randrange(W)
    y = rng.randrange(H)
    wset(x, y, tuft)
    wset(x + 1, y, tuft)
    wset(x, y + 1, tuft)

# sparse bare-dirt patches
for _ in range(2):
    x = rng.randrange(W)
    y = rng.randrange(H)
    wset(x, y, dirt)
    wset(x + 1, y, dirt)
    wset(x, y + 1, dirt)
    if rng.random() < 0.5:
        wset(x + rng.randrange(2), y + rng.randrange(2), dirtd)

# a few tiny yellow flowers (plus shapes, wrap-around)
for _ in range(3):
    x = rng.randrange(W)
    y = rng.randrange(H)
    wset(x, y, flower)
    wset(x + 1, y, flower)
    wset(x - 1, y, flower)
    wset(x, y + 1, flower)
    wset(x, y - 1, flower)

print(c.stats_text())
print(c.matrix_text())
finish(c)
