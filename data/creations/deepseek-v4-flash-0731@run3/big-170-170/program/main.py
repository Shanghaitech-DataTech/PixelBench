from pixelbench_api import *
import random

src = input_canvas
out = src.copy(name='output')
W, H = 170, 170

# ---------- 1) REMOVE THE CHARACTER ----------
# Character bbox approx x=55..117, y=55..127. Behind it: background wall
# (left of machine) and street ground; the vending machine spans x=80..117.

def fill_from_donors(x0, y0, x1, y1, donors):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            d = donors[(x - x0) % len(donors)]
            out.set(x, y, src.get(d, y))

bg_donors = list(range(42, 54))                       # wall/background columns
gd_donors = list(range(42, 54)) + list(range(118, 130))  # street columns
fill_from_donors(55, 55, 79, 99, bg_donors)   # wall left of machine
fill_from_donors(55, 100, 117, 127, gd_donors)  # street below machine (machine drawn over 56..104)

# --- rebuild the vending machine the character was hiding ---
m = new_canvas(38, 49)  # placed at (80, 56) -> x80..117, y56..104
frame = '#1e1a53'
bright = '#ffeae3'
white = '#fceee8'
m.rect(0, 0, 38, 49, frame, fill=True)
m.rect(2, 1, 34, 3, bright, fill=True)
for bx, bc in ((4, '#605ce4'), (13, '#75d47c'), (22, '#c16c41'), (30, '#a570db')):
    m.rect(bx, 2, 3, 2, bc, fill=True)
m.rect(1, 5, 36, 17, white, fill=True)   # glass window
rows = [
    (7,  [(2, '#a570db'), (11, '#75d47c'), (20, '#c16c41'), (29, '#605ce4')]),
    (12, [(2, '#c16c41'), (11, '#605ce4'), (20, '#75d47c'), (29, '#a570db')]),
    (17, [(2, '#75d47c'), (11, '#c16c41'), (20, '#a570db'), (29, '#605ce4')]),
]
for ry, cans in rows:
    for cx, cc in cans:
        m.rect(cx, ry, 5, 5, cc, fill=True)
        m.rect(cx, ry, 5, 1, '#ffffff', fill=True)
m.rect(1, 23, 36, 5, '#0e3b50', fill=True)
for bx in (3, 9, 15, 21, 27, 33):
    m.rect(bx, 24, 3, 3, '#605ce4', fill=True)
m.rect(1, 29, 36, 7, bright, fill=True)
m.rect(3, 31, 8, 4, '#84423a', fill=True)
m.rect(13, 31, 8, 4, '#75293b', fill=True)
m.rect(23, 31, 8, 4, '#c16c41', fill=True)
m.rect(0, 37, 38, 5, '#1e1a53', fill=True)
m.rect(0, 42, 38, 4, '#0e3b50', fill=True)
m.rect(0, 46, 38, 3, '#0a2e3f', fill=True)
out.blit(m, 80, 56)

# ---------- 2) THUNDERSTORM: wet ground ----------
# darken the street for a wet look
for y in range(100, 170):
    for x in range(0, 170):
        rgba = out.palette()[out.get(x, y)]['rgba']
        if rgba[3] == 0:
            continue
        out.set(x, y, (max(0, int(rgba[0] * 0.70)), max(0, int(rgba[1] * 0.76)), max(0, int(rgba[2] * 0.86)), 255))

random.seed(7)
# puddle shine streaks on the wet ground
for _ in range(260):
    y = random.randint(102, 167)
    x = random.randint(0, 166)
    L = random.randint(4, 9)
    for i in range(L):
        if x + i < 170:
            out.set(x + i, y, (130, 168, 202, 70))
            out.set(x + i, y, (150, 184, 214, 80))
    out.set(x + 2, y, (175, 202, 228, 120))
# light glints / clinging droplets on the wet ground
for _ in range(130):
    x = random.randint(0, 169)
    y = random.randint(100, 168)
    out.set(x, y, (198, 220, 240, 150))
    if random.random() < 0.5 and x + 1 < 170:
        out.set(x + 1, y + 1, (178, 204, 230, 120))
# droplets clinging to the vending machine glass
for _ in range(70):
    x = random.randint(81, 115)
    y = random.randint(58, 98)
    out.set(x, y, (188, 212, 238, 140))
    out.set(x + 1, y + 1, (166, 194, 226, 110))

# ---------- 3) LIGHTNING IN THE BACKGROUND ----------
bolt = [(39, 3), (33, 13), (41, 17), (27, 32), (37, 38), (25, 47)]
def bolt_poly(pts, col):
    for i in range(len(pts) - 1):
        out.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], col)
for dx in (-2, -1, 0, 1, 2):
    for dy in (-2, -1, 0, 1, 2):
        bolt_poly(bolt, (110, 155, 255, 42))
bolt_poly(bolt, (165, 198, 255, 120))
bolt_poly(bolt, (224, 234, 255, 255))
bolt_poly([(33, 13), (21, 9), (15, 17)], (190, 214, 255, 150))
bolt_poly([(37, 38), (47, 47)], (200, 220, 255, 160))
bolt_poly([(27, 32), (19, 40)], (200, 220, 255, 120))

# ---------- 4) THUNDERSTORM: rain as semi-transparent droplets ----------
random.seed(11)
for _ in range(360):
    x = random.randint(-8, 168)
    y = random.randint(-8, 165)
    for i in range(5):
        xx, yy = x + i, y + i * 2
        if 0 <= xx < 170 and 0 <= yy < 170:
            out.set(xx, yy, (150, 182, 214, 74))
    if 0 <= x < 170 and 0 <= y < 170:
        out.set(x, y, (188, 212, 238, 150))

print(out.stats_text())
finish(out)
