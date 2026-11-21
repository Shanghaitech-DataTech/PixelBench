import math
from pixelbench_api import *

c = new_canvas(64, 64, name="watch")

def col(spec, name=None):
    return c.color(spec, name=name)

# palette
BG       = col((18, 12, 6), "bg")
G_DEEP   = col((40, 24, 8), "g_deep")
G_DARK   = col((70, 44, 14), "g_dark")
G_DARK2  = col((96, 62, 20), "g_dark2")
G_MID    = col((128, 86, 28), "g_mid")
G_MID2   = col((160, 112, 40), "g_mid2")
G_LIGHT  = col((198, 148, 62), "g_light")
G_BRIGHT = col((235, 188, 92), "g_bright")
G_PALE   = col((252, 226, 158), "g_pale")
G_WHITE  = col((255, 250, 224), "g_white")
STEEL_D  = col((26, 18, 12), "steel_d")
LINE_D   = col((12, 8, 4), "line_d")
RUBY     = col((176, 46, 56), "ruby")
RUBY_HI  = col((240, 120, 128), "ruby_hi")

def arc(cx, cy, r, a1, a2, color):
    x1 = cx + r * math.cos(a1); y1 = cy + r * math.sin(a1)
    x2 = cx + r * math.cos(a2); y2 = cy + r * math.sin(a2)
    large = 1 if abs(a2 - a1) > math.pi else 0
    sweep = 1 if a2 >= a1 else 0
    d = f"M {x1:.3f} {y1:.3f} A {r} {r} 0 {large} {sweep} {x2:.3f} {y2:.3f}"
    c.path(d, color, fill=False)

def gear(cx, cy, r, teeth, base, hole, bright, phase=0.0):
    c.circle(cx, cy, r, base, fill=True)
    # protruding teeth
    for i in range(teeth):
        a = phase + 2 * math.pi * i / teeth
        tx = round(cx + (r + 1) * math.cos(a))
        ty = round(cy + (r + 1) * math.sin(a))
        c.rect(tx - 1, ty - 1, 2, 2, base, fill=True)
    # centre hole and spokes
    c.circle(cx, cy, max(1, round(r * 0.4)), hole, fill=True)
    if r >= 6:
        for i in range(4):
            a = phase + math.pi / 2 * i + math.pi / 4
            sx = round(cx + (r * 0.7) * math.cos(a))
            sy = round(cy + (r * 0.7) * math.sin(a))
            c.circle(sx, sy, max(1, round(r * 0.15)), hole, fill=True)
    # specular rim
    arc(cx, cy, r, -2.7, -1.0, bright)

# ---------------- open lid (left) ----------------
L = (-6, 34)
LR = 23
c.circle(L[0], L[1], LR, G_DARK, fill=True)
c.circle(L[0], L[1], LR - 1, G_MID, fill=True)
c.circle(L[0], L[1], LR - 2, G_DARK2, fill=True)
c.circle(L[0], L[1], LR - 2, G_MID2, fill=False)
for rr in (18, 14, 10):
    c.circle(L[0], L[1], rr, G_DARK, fill=False)
c.circle(L[0], L[1], 8, G_LIGHT, fill=True)
c.circle(L[0], L[1], 6, G_DARK2, fill=True)
c.circle(L[0], L[1], 4, G_LIGHT, fill=True)
c.circle(L[0], L[1], 2, G_DARK, fill=True)
arc(L[0], L[1], LR - 1, -1.35, -0.35, G_PALE)
arc(L[0], L[1], LR - 2, -1.3, -0.45, G_BRIGHT)
arc(L[0], L[1], LR - 1, 0.45, 1.35, G_DEEP)

# ---------------- watch case (right) ----------------
W = (40, 34)
R = 23
c.circle(W[0], W[1], R, G_DEEP, fill=True)
c.circle(W[0], W[1], R - 1, G_DARK, fill=True)
c.circle(W[0], W[1], R - 2, G_MID, fill=True)
c.circle(W[0], W[1], R - 3, G_LIGHT, fill=True)
c.circle(W[0], W[1], R - 4, BG, fill=True)

# bezel light/shadow arcs
arc(W[0], W[1], R - 1, -2.7, -1.0, G_BRIGHT)
arc(W[0], W[1], R - 2, -2.7, -1.0, G_PALE)
arc(W[0], W[1], R - 1, -2.5, -2.0, G_WHITE)
arc(W[0], W[1], R - 1, 0.4, 1.9, G_DEEP)

# dial chapter ring
for i in range(60):
    a = -math.pi / 2 + i * 2 * math.pi / 60
    c.set(round(W[0] + 18 * math.cos(a)), round(W[1] + 18 * math.sin(a)), G_DARK2)
for i in range(12):
    a = -math.pi / 2 + i * 2 * math.pi / 12
    dx = math.cos(a); dy = math.sin(a)
    px = -dy; py = dx
    x1 = W[0] + 16 * dx; y1 = W[1] + 16 * dy
    x2 = W[0] + 19 * dx; y2 = W[1] + 19 * dy
    c.line(round(x1), round(y1), round(x2), round(y2), G_BRIGHT)
    c.line(round(x1 + px), round(y1 + py), round(x2 + px), round(y2 + py), G_BRIGHT)

# gear train
gear(33, 29, 8, 10, G_MID2, BG, G_BRIGHT, phase=0.0)
gear(46, 36, 6, 9, G_MID, BG, G_BRIGHT, phase=0.35)
gear(36, 43, 5, 8, G_DARK2, BG, G_LIGHT, phase=0.7)
gear(45, 25, 5, 8, G_LIGHT, BG, G_BRIGHT, phase=0.2)
gear(27, 37, 4, 7, G_DARK2, BG, G_LIGHT, phase=0.5)

# ruby pivot jewels
c.circle(33, 29, 1, RUBY, fill=True)
c.set(32, 28, RUBY_HI)
for (jx, jy) in [(46, 36), (36, 43), (45, 25), (27, 37)]:
    c.set(jx, jy, RUBY)
    c.set(jx - 1, jy - 1, RUBY_HI)

# ---------------- hands ----------------
def hand(angle, length, hw, color, outline):
    dx = math.cos(angle); dy = math.sin(angle)
    px = -dy; py = dx
    cx, cy = W
    tailx = cx - dx * 3; taily = cy - dy * 3
    tipx = cx + dx * length; tipy = cy + dy * length
    pts_o = [
        (round(tailx + px * (hw + 0.8)), round(taily + py * (hw + 0.8))),
        (round(tailx - px * (hw + 0.8)), round(taily - py * (hw + 0.8))),
        (round(tipx - px * 0.9), round(tipy - py * 0.9)),
        (round(tipx + px * 0.9), round(tipy + py * 0.9)),
    ]
    pts = [
        (round(tailx + px * hw), round(taily + py * hw)),
        (round(tailx - px * hw), round(taily - py * hw)),
        (round(tipx - px * 0.4), round(tipy - py * 0.4)),
        (round(tipx + px * 0.4), round(tipy + py * 0.4)),
    ]
    c.poly(pts_o, outline, fill=True)
    c.poly(pts, color, fill=True)

hand(7 * math.pi / 6, 10, 1.5, G_BRIGHT, LINE_D)   # hour -> 10
hand(-math.pi / 6, 15, 1.0, G_PALE, LINE_D)        # minute -> 2

c.circle(W[0], W[1], 2, G_PALE, fill=True)
c.circle(W[0], W[1], 1, G_DARK, fill=True)
c.set(W[0], W[1], G_WHITE)

# ---------------- crown ----------------
c.rect(36, 5, 8, 7, G_MID, fill=True)
for x in (38, 40, 42):
    c.line(x, 5, x, 11, G_DARK)
c.rect(36, 4, 8, 2, G_LIGHT, fill=True)
c.set(40, 4, G_WHITE)

# ---------------- chain (draped top-left) ----------------
chain_pts = [(40, 4), (37, 3), (34, 2), (31, 2), (28, 2), (25, 3),
             (22, 4), (19, 5), (16, 6), (13, 7), (10, 8), (7, 9),
             (4, 10), (1, 11)]
for i in range(len(chain_pts) - 1):
    c.line(chain_pts[i][0], chain_pts[i][1], chain_pts[i + 1][0], chain_pts[i + 1][1], G_DARK)
for i, (x, y) in enumerate(chain_pts):
    color = G_LIGHT if i % 2 == 0 else G_MID
    c.circle(x, y, 1, color, fill=True)
    c.set(x, y, G_DARK)
    c.set(x - 1, y - 1, G_BRIGHT)

# hinge between lid and case
c.circle(17, 34, 2, G_DARK, fill=True)
c.circle(17, 34, 1, G_LIGHT, fill=True)
c.set(16, 33, G_PALE)

print(c.stats_text())
print(c.matrix_text())
finish(c)
