from pixelbench_api import *
import random

C = new_canvas(16, 16, background=None, name="dirt")

# Palette (Minecraft dirt style)
base      = C.color("#79553A")   # mid brown
dark1     = C.color("#5D4230")   # dark brown
dark2     = C.color("#453222")   # deepest brown
light1    = C.color("#8F6B4A")   # light brown
light2    = C.color("#A5805B")   # lighter brown
light3    = C.color("#B99468")   # highlight
stone1    = C.color("#6E6E6E")   # pebble dark
stone2    = C.color("#8C8C8C")   # pebble light

rng = random.Random(7)

# Base fill
C.rect(0, 0, 16, 16, base)

# Granular speckle noise
for y in range(16):
    for x in range(16):
        r = rng.random()
        if r < 0.16:
            C.set(x, y, dark1)
        elif r < 0.26:
            C.set(x, y, light1)
        elif r < 0.32:
            C.set(x, y, light2)

# Small dark clumps (2-3 px) for chunkiness
clumps = [(2,3),(9,1),(13,6),(5,8),(11,11),(1,13),(7,14),(14,12),(3,10),(9,6)]
for (cx, cy) in clumps:
    C.set(cx, cy, dark2)
    dx, dy = rng.choice([(1,0),(0,1),(1,1)])
    C.set((cx+dx) % 16, (cy+dy) % 16, dark1)

# Light clumps
lights = [(4,5),(12,3),(6,12),(14,9),(0,7)]
for (cx, cy) in lights:
    C.set(cx, cy, light3)
    dx, dy = rng.choice([(1,0),(0,1)])
    C.set((cx+dx) % 16, (cy+dy) % 16, light2)

# Tiny pebbles (gray)
pebbles = [(6,2),(12,8),(2,12),(10,14)]
for (px_, py_) in pebbles:
    C.set(px_, py_, stone1)
    C.set((px_+1) % 16, py_, stone2)

finish(C)
