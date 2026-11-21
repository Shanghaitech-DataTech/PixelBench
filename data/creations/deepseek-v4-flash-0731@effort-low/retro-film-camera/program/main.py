from pixelbench_api import *
import math

c = new_canvas(32, 32)

DARK      = (25, 21, 19)
LEATHER   = (62, 36, 28)
LEATHER_L = (84, 52, 39)
LEATHER_D = (46, 27, 21)
GUN       = (28, 28, 33)
METAL     = (58, 58, 66)
SILVER    = (198, 206, 214)
GLASS1    = (30, 60, 86)
GLASS2    = (66, 112, 152)
GLASS3    = (110, 164, 200)
GLASS_HI  = (196, 226, 244)
REDDIAL   = (150, 30, 26)
SILVER_HI = (230, 236, 242)

# --- Viewfinder hump on top ---
c.rect(12, 3, 8, 6, DARK)
c.rect(13, 4, 6, 5, GUN)

# --- Metal top plate ---
c.rect(3, 9, 26, 4, DARK)
c.rect(4, 10, 24, 3, METAL)
c.line(5, 10, 27, 10, SILVER)

# --- Leather body ---
c.rect(3, 12, 26, 18, DARK)
c.rect(4, 13, 24, 16, LEATHER)

# leather grain (keep lens zone clear, zone around x10..22 y14..24)
for xx in range(4, 28):
    for yy in range(14, 28):
        if 10 <= xx <= 22 and 14 <= yy <= 24:
            continue
        if yy % 4 == 0:
            c.set(xx, yy, LEATHER_D)
        elif yy % 4 == 2 and xx % 3 == 0:
            c.set(xx, yy, LEATHER_L)

# --- Shutter button ---
c.circle(9, 10, 2, DARK)
c.circle(9, 10, 1, SILVER)
c.set(9, 9, SILVER_HI)

# --- Lens ---
cx, cy = 16, 19
c.circle(cx, cy, 7, DARK)
c.circle(cx, cy, 6, GUN)
for a in range(9):
    ang = a * 0.785
    px = round(cx + math.cos(ang) * 5.5)
    py = round(cy + math.sin(ang) * 5.5)
    c.set(px, py, DARK)
c.circle(cx, cy, 5, METAL)
c.circle(cx, cy, 4, DARK)
c.circle(cx, cy, 3, GLASS1)
c.circle(cx, cy, 2, GLASS2)
c.circle(cx, cy, 1, GLASS3)
c.set(cx, cy, (150, 194, 224))
c.circle(cx - 1, cy - 1, 1, GLASS_HI)

# --- red light ---
c.set(7, 25, REDDIAL)
c.set(8, 25, REDDIAL)

# --- bottom detail ---
c.line(4, 28, 27, 28, LEATHER_D)

print(c.stats_text())
finish(c)
