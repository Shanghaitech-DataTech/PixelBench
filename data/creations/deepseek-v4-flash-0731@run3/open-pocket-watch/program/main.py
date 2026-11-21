import math
from pixelbench_api import *

W = 64
c = new_canvas(W, W, background=(7, 5, 3), name="open_watch")

pal = {
    "bg": (7, 5, 3), "v0": (3, 2, 2),
    "g0": (24, 16, 8), "g1": (40, 27, 13), "g2": (60, 41, 19), "g3": (84, 59, 27),
    "g4": (114, 83, 38), "g5": (150, 110, 56), "g6": (186, 141, 74), "g7": (220, 174, 104),
    "g8": (242, 208, 140), "g9": (254, 232, 182), "gw": (255, 248, 226),
    "p0": (10, 8, 6), "p1": (17, 13, 9), "p2": (26, 20, 14), "p3": (40, 31, 21),
    "s0": (6, 6, 10), "s1": (20, 17, 24),
    "i0": (122, 104, 78), "i1": (166, 148, 114), "i2": (210, 196, 166), "i3": (238, 230, 206),
    "i4": (252, 248, 236),
    "h0": (13, 11, 9), "h1": (52, 44, 36),
    "red": (166, 32, 24), "redl": (214, 88, 58),
}
for name, rgba in pal.items():
    c.color(rgba, name)

def C(n): return c.color(n)

v0 = C("v0"); bg = C("bg")
g0 = C("g0"); g1 = C("g1"); g2 = C("g2"); g3 = C("g3"); g4 = C("g4"); g5 = C("g5")
g6 = C("g6"); g7 = C("g7"); g8 = C("g8"); g9 = C("g9"); gw = C("gw")
p0 = C("p0"); p1 = C("p1"); p2 = C("p2"); p3 = C("p3")
s0 = C("s0"); s1 = C("s1")
i0 = C("i0"); i1 = C("i1"); i2 = C("i2"); i3 = C("i3"); i4 = C("i4")
h0 = C("h0"); h1 = C("h1")
red = C("red"); redl = C("redl")

# ---------------- vignette ----------------
for yy in range(W):
    for xx in range(W):
        d = math.hypot(xx - 32, yy - 38)
        if d > 32:
            c.set(xx, yy, v0)

# ---------------- OPEN LID (concave bowl flipped open to the left) ----------------
c.ellipse(8, 36, 6.7, 15.5, g1)        # bowl outer rim
c.ellipse(8, 36, 6.0, 14.2, g2)
c.ellipse(8, 36, 5.2, 12.8, g4)
c.ellipse(8, 36, 4.3, 11.2, g6)
c.ellipse(8, 36, 3.5, 9.5, g7)
c.ellipse(8, 36, 2.8, 7.8, g8)
c.ellipse(8, 36, 2.0, 6.0, g9)
c.line(4, 26, 4, 46, g8)
c.line(3, 29, 3, 43, gw)
c.set(5, 24, g7); c.set(6, 48, g7)
c.set(7, 22, g6)
c.ellipse(8, 36, 6.0, 14.4, g3, fill=False)

# ---------------- CASE ----------------
c.circle(34, 38, 23, g1)
c.circle(34, 38, 22, g3)
c.circle(34, 38, 20, g5)
c.circle(34, 38, 19, g6, fill=False)
# engine-polished bezel shading
for a in range(130, 272, 8):
    rad = math.radians(a)
    c.set(round(34 + math.cos(rad) * 20), round(38 + math.sin(rad) * 20), g7)
for a in range(150, 252, 20):
    rad = math.radians(a)
    c.set(round(34 + math.cos(rad) * 21), round(38 + math.sin(rad) * 21), g8)
for a in range(320, 406, 18):
    rad = math.radians(a)
    c.set(round(34 + math.cos(rad) * 20), round(38 + math.sin(rad) * 20), g2)
c.set(25, 19, g9); c.set(23, 23, gw); c.set(27, 17, gw); c.set(30, 16, g8)
c.circle(34, 38, 22, g9, fill=False)

# hinge band joining lid to case (drawn over the seam)
c.rect(11, 32, 5, 13, g3)
c.rect(12, 33, 4, 11, g5)
c.line(12, 33, 12, 43, g8)
c.line(14, 34, 14, 42, g6)

# ---------------- INTERIOR (movement plate) ----------------
c.circle(34, 38, 18, p0)
c.circle(34, 38, 16, p1)
c.circle(34, 38, 14, p2)
c.circle(32, 35, 11, p3)
c.circle(38, 41, 8, p2)
c.circle(30, 31, 6, p1)
# engraved rings (engine turn)
for r in (15, 12, 10):
    c.circle(34, 38, r, g3, fill=False)
    for i in range(20):
        a = 2 * math.pi * i / 20
        c.set(round(34 + math.cos(a) * (r - 0.5)), round(38 + math.sin(a) * (r - 0.5)), g4)
c.line(24, 21, 29, 26, g4)
c.line(21, 27, 24, 31, g3)

# ---------------- GEARS ----------------
def gear(cx, cy, r, n, body, dark, hole, bright, phase=0.0):
    for i in range(n):
        a = 2 * math.pi * i / n - math.pi / 2
        tx = round(cx + math.cos(a) * r); ty = round(cy + math.sin(a) * r)
        c.set(tx, ty, body)
        if ty < cy:
            c.set(tx, ty, bright)
        c.set(round(cx + math.cos(a) * (r - 1)), round(cy + math.sin(a) * (r - 1)), body)
    if r >= 5:
        c.circle(cx, cy, r - 1, body)
        c.circle(cx, cy, r - 2, dark)
        c.circle(cx, cy, r - 3, body)
    if r >= 6:
        for k in range(3):
            a = phase + 2 * math.pi * k / 3
            c.line(cx, cy, round(cx + math.cos(a) * (r - 2)), round(cy + math.sin(a) * (r - 2)), body)
        c.circle(cx, cy, 2, hole)
        c.circle(cx, cy, 1, body)
        c.set(cx, cy, red)
    for a in range(135, 272, 9):
        rad = math.radians(a)
        c.set(round(cx + math.cos(rad) * (r - 1)), round(cy + math.sin(rad) * (r - 1)), bright)
    for a in range(315, 406, 12):
        rad = math.radians(a)
        c.set(round(cx + math.cos(rad) * (r - 1)), round(cy + math.sin(rad) * (r - 1)), dark)

gear(29, 30, 9, 10, g6, g2, p0, g9, phase=0.4)
gear(40, 29, 9, 10, g5, g1, p0, g8, phase=1.5)
gear(35, 37, 6, 8, g7, g3, p0, g8, phase=2.1)
gear(22, 39, 5, 8, g6, g2, p0, g9, phase=0.8)
gear(47, 37, 5, 8, g5, g1, p0, g8, phase=2.7)
gear(46, 45, 4, 7, g6, g2, p0, g8, phase=1.1)
gear(23, 47, 4, 7, g5, g2, p0, g9, phase=0.2)
# small screw heads on the plate
for (sx, sy) in [(20, 28), (48, 28), (33, 20), (45, 48)]:
    c.circle(sx, sy, 1, s1)
    c.line(sx - 1, sy, sx + 1, sy, h1)
    c.set(sx, sy - 1, s0)

# ---------------- DIAL (bottom) ----------------
c.circle(37, 50, 8, i1)
c.circle(37, 50, 7, i2)
c.circle(36, 48, 5.5, i3)
c.circle(35, 47, 4.2, i4)
# tick marks
for i in range(12):
    a = 2 * math.pi * i / 12
    x1 = round(37 + math.cos(a) * 5.6); y1 = round(50 + math.sin(a) * 5.6)
    c.set(x1, y1, i0)
    x2 = round(37 + math.cos(a) * 4.5); y2 = round(50 + math.sin(a) * 4.5)
    if i % 3 == 0:
        c.set(x2, y2, i0)
c.circle(37, 50, 5.8, i0, fill=False)
# hands (10:10)
c.line(37, 49, 33, 47, h1)   # hour hand (thick)
c.line(37, 48, 33, 47, h1)
c.line(37, 49, 42, 45, h0)   # minute hand
c.line(37, 48, 42, 45, h0)
c.line(37, 49, 41, 46, g9)   # minute highlight
c.line(37, 49, 40, 52, redl) # seconds hand
c.set(33, 46, g9)
# centre jewel
c.circle(37, 50, 1, red)
c.set(37, 49, redl)

# ---------------- CROWN ----------------
c.rect(30, 7, 8, 12, g3)
for x in range(30, 38, 2):
    c.line(x, 8, x, 16, g1)
c.rect(31, 6, 6, 3, g6)
c.rect(32, 5, 4, 2, g7)
c.set(33, 4, g8)
c.line(34, 5, 36, 5, gw)
c.rect(30, 12, 8, 4, g5)
c.rect(31, 11, 6, 3, g6)

# ---------------- CHAIN (draped to the upper right) ----------------
def chainlink(px, py):
    c.ellipse(px, py, 2, 1.5, g6, fill=False)
    c.ellipse(px, py, 1.2, 0.8, g3, fill=False)
    c.set(px - 1, py - 1, g8)
    c.set(px + 1, py, g2)
    c.set(px, py - 1, g9)
chainlink(41, 6)
chainlink(46, 4)
chainlink(51, 3)
chainlink(56, 2)
chainlink(60, 2)

# ---------------- final glints ----------------
c.line(24, 14, 29, 18, gw)
c.set(30, 12, g9)
c.set(19, 21, gw)
c.set(35, 27, g9)
c.set(45, 20, g8)
c.set(24, 44, g8)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

finish(c)
