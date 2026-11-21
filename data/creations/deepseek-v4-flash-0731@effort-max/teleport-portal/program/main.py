import math
from pixelbench_api import *

W = H = 48
c = new_canvas(W, H, name="portal")

fx = fy = 23.5  # exact centre of the 48x48 grid

# palette (well under the 86 visible-colour limit)
void  = c.color((18, 10, 34))
p1    = c.color((84, 40, 170))
p2    = c.color((124, 64, 208))
p3    = c.color((166, 98, 242))
p4    = c.color((208, 142, 255))
mag   = c.color((255, 118, 232))
white = c.color((255, 245, 255))
glowA = c.color((150, 92, 255, 60))
glowB = c.color((182, 118, 255, 110))
halo  = c.color((232, 186, 255, 200))
star  = c.color((240, 214, 255, 235))

def d2(x, y):
    return math.hypot(x - fx, y - fy)

def ring(r, colour):
    for y in range(H):
        for x in range(W):
            if abs(d2(x, y) - r) <= 0.5:
                c.set(x, y, colour)

def disc(r, colour):
    for y in range(H):
        for x in range(W):
            if d2(x, y) <= r:
                c.set(x, y, colour)

def spiral(start_r, end_r, turns, colour_for, phase):
    n = int((end_r - start_r) * 6)
    prev = None
    for i in range(n + 1):
        t = i / n * (2 * math.pi * turns)
        r = start_r + (end_r - start_r) * (i / n)
        th = phase + t
        x = round(fx + r * math.cos(th))
        y = round(fy + r * math.sin(th))
        colour = colour_for(r)
        if prev is not None and (abs(x - prev[0]) + abs(y - prev[1])) > 1:
            c.line(prev[0], prev[1], x, y, colour)
        else:
            c.set(x, y, colour)
        prev = (x, y)

def col_for(r):
    if r < 6:
        return p4
    if r < 10:
        return p3
    if r < 14:
        return p2
    return p1

# --- 1) glowing halo (outer luminous rings, translucent) ---
ring(21.6, glowA)
ring(20.4, glowB)
ring(19.4, halo)

# --- 2) dark void at the mouth of the portal ---
disc(14.6, void)

# --- 3) purple energy vortex: three sweeping spiral arms ---
for k in range(3):
    spiral(2.5, 17.5, 1.9, col_for, phase=k * 2 * math.pi / 3)

# faint energy haze just inside the halo
ring(17.5, glowB)

# --- 4) dashed spin rings suggesting rotation ---
for rr, cc in ((9.3, p2), (12.4, p1)):
    for y in range(H):
        for x in range(W):
            d = d2(x, y)
            if abs(d - rr) <= 0.45:
                seg = (math.degrees(math.atan2(y - fy, x - fx)) % 90) // 22
                if seg % 2 == 0:
                    c.set(x, y, cc)

# inner accelerating arc ring
for y in range(H):
    for x in range(W):
        d = d2(x, y)
        if 5.6 <= d <= 6.4:
            seg = (math.degrees(math.atan2(y - fy, x - fx)) % 60) // 20
            if seg % 2 == 0:
                c.set(x, y, p4)

# --- 5) blazing white/magenta core ---
disc(2.6, white)
ring(4.2, mag)

# --- 6) sparkle glints riding the halo at the four diagonals ---
def sparkle(px, py, colour):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        c.set(round(px + dx), round(py + dy), colour)

for k in range(4):
    a = math.radians(45 + k * 90)
    sparkle(fx + 20.2 * math.cos(a), fy + 20.2 * math.sin(a), star)

# --- 7) stray energy motes ---
parts = [(10, 10), (38, 9), (39, 38), (9, 39), (16, 44), (33, 44), (4, 21), (44, 26)]
for (ax, ay) in parts:
    c.set(ax, ay, glowB)

print(c.stats_text())
finish(c)
