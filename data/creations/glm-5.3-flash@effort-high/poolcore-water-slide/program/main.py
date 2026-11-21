import math
from pixelbench_api import new_canvas, finish

c = new_canvas(128, 128, background=None, name="poolcore")

# ---- palette ----
CEIL  = c.color('#dfe8ee', 'ceiling')
CEILD = c.color('#bccdd8', 'ceiling_edge')
LIGHT = c.color('#ffffff', 'light')
LIGHTF= c.color('#c9d9e2', 'light_frame')
WALL  = c.color('#c4dbe8', 'wall_tile')
GROUT = c.color('#e9f3f8', 'grout')
WALLD = c.color('#aecbdc', 'wall_tile_dark')
COL   = c.color('#d6e6f0', 'column')
COLG  = c.color('#f2f9fc', 'column_grout')
COLD  = c.color('#9db9c9', 'column_edge')
W1    = c.color('#a9d6ea', 'water_far')
W2    = c.color('#8cc4de', 'water_mid')
W3    = c.color('#72b2d2', 'water_near')
RIP   = c.color('#d9f1fa', 'ripple')
RIPD  = c.color('#63a3c4', 'ripple_dark')
REFL  = c.color('#c2e4f2', 'reflection')
SLIDE = c.color('#f7fbfd', 'slide')
SLIDES= c.color('#cfdde6', 'slide_shade')
POST  = c.color('#c2d4de', 'post')
POSTD = c.color('#a8bfcc', 'post_shade')
COPING= c.color('#eef6fa', 'coping')
COPD  = c.color('#b9cfdc', 'coping_edge')
DECK  = c.color('#c9dde9', 'deck')
DECKG = c.color('#e6f1f7', 'deck_grout')
DECKD = c.color('#b3cddd', 'deck_dark')
YEL   = c.color('#f5c93b', 'ring')
YELD  = c.color('#d9a625', 'ring_shade')
YELH  = c.color('#ffe98c', 'ring_hi')
HAIR  = c.color('#4b352a', 'hair')
HAIRH = c.color('#6b4d3a', 'hair_hi')
SKIN  = c.color('#f2c9a6', 'skin')
SUIT  = c.color('#e87d9d', 'suit')

# ---- ceiling with fluorescent panels ----
c.rect(0, 0, 128, 18, CEIL)
for lx in (6, 52, 98):
    c.rect(lx, 5, 24, 7, LIGHTF)
    c.rect(lx + 1, 6, 22, 5, LIGHT)
c.line(0, 17, 127, 17, CEILD)
c.line(0, 18, 127, 18, GROUT)  # glow line where wall meets ceiling

# ---- tiled back wall ----
c.rect(0, 19, 128, 41, WALL)
for yy in range(19, 60, 4):
    c.line(0, yy, 127, yy, GROUT)
for xx in range(0, 128, 4):
    c.line(xx, 19, xx, 59, GROUT)
for j in range(19, 60, 4):
    for i in range(0, 128, 4):
        if (i // 4 * 7 + j // 4 * 3) % 5 == 0:
            c.rect(i, j, 3, 3, WALLD)

# ---- tiled columns ----
for cx in (12, 107):
    c.rect(cx, 19, 10, 41, COL)
    for yy in range(19, 60, 4):
        c.line(cx, yy, cx + 9, yy, COLG)
    for xx in range(cx, cx + 10, 4):
        c.line(xx, 19, xx, 59, COLG)
    c.line(cx, 19, cx, 59, COLD)
    c.line(cx + 9, 19, cx + 9, 59, COLD)
    # capital and base
    c.rect(cx - 1, 19, 12, 3, COLG)
    c.line(cx - 1, 21, cx + 10, 21, COLD)
    c.rect(cx - 1, 56, 12, 4, COLG)
    c.line(cx - 1, 56, cx + 10, 56, COLD)

# ---- pool water ----
c.rect(0, 60, 128, 19, W1)
c.rect(0, 79, 128, 20, W2)
c.rect(0, 99, 128, 16, W3)

# ripples
for y in range(63, 114, 4):
    for x in range(0, 128):
        off = int(1.6 * math.sin(x / 7.0 + y * 0.9))
        if (x + y) % 2 == 0:
            c.set(x, y + off, RIP)
        if (x * 3 + y) % 7 == 0:
            c.set(x, y + off + 2, RIPD)

# light reflections on water
for lx in (18, 64, 110):
    for y in range(62, 104, 2):
        dx = int(2 * math.sin(y / 5.0 + lx))
        if (y // 2) % 2 == 0:
            c.set(lx + dx, y, REFL)
            c.set(lx + dx + 1, y, REFL)

# ---- coping and foreground deck ----
c.rect(0, 115, 128, 3, COPING)
c.line(0, 117, 127, 117, COPD)
c.rect(0, 118, 128, 10, DECK)
for yy in range(118, 128, 4):
    c.line(0, yy, 127, yy, DECKG)
for xx in range(0, 128, 4):
    c.line(xx, 118, xx, 127, DECKG)
for j in range(118, 128, 4):
    for i in range(0, 128, 4):
        if (i // 4 * 5 + j * 2) % 6 == 0:
            c.rect(i, j, 3, 3, DECKD)

# ---- slide reflection in water ----
for y in range(62, 84, 2):
    dx = int(3 * math.sin(y / 4.0))
    if (y // 2) % 2 == 0:
        c.set(100 + dx, y, REFL)
        c.set(101 + dx, y, REFL)

# ---- water slide (white tube on posts) ----
# support posts first
c.rect(114, 32, 2, 28, POST)
c.line(115, 32, 115, 59, POSTD)
c.rect(103, 50, 2, 10, POST)
c.line(103, 50, 103, 59, POSTD)

def bez(p0, p1, p2, p3, t):
    mt = 1 - t
    x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
    y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
    return x, y

def tube(p0, p1, p2, p3, n=70, shade=SLIDES, body=SLIDE):
    pts = [bez(p0, p1, p2, p3, i / n) for i in range(n + 1)]
    for (x, y) in pts:
        c.circle(int(x) + 1, int(y) + 1, 4, shade)
    for (x, y) in pts:
        c.circle(int(x), int(y), 4, body)
    for k, (x, y) in enumerate(pts):
        if k % 3 == 0:
            c.set(int(x) - 2, int(y) - 2, LIGHT)
            c.set(int(x) - 1, int(y) - 2, LIGHT)

tube((95, 14), (122, 24), (122, 44), (98, 56))
tube((98, 56), (92, 59), (88, 60), (84, 61), n=30)

# splash where slide meets water
for (sx, sy) in [(82, 60), (84, 59), (86, 60), (81, 62), (87, 62), (83, 58), (85, 58)]:
    c.set(sx, sy, RIP)

# ---- girl floating in yellow swim ring (seen from behind) ----
# ripple rings around the float
c.ellipse(60, 93, 18, 10, RIP, fill=False)
c.ellipse(60, 93, 22, 13, RIPD, fill=False)

# ring: shade, body, hole
c.ellipse(60, 93, 15, 8, YELD)
c.ellipse(60, 91, 15, 8, YEL)
c.ellipse(60, 92, 8, 4, W2)
c.rect(56, 89, 9, 4, SUIT)      # lower back visible in the ring hole

# back and shoulders
c.ellipse(60, 84, 7, 6, SKIN)
# swimsuit straps over shoulders
c.line(55, 80, 55, 86, SUIT)
c.line(65, 80, 65, 86, SUIT)
# hair from behind
c.ellipse(60, 74, 6, 8, HAIR)
for (hx, hy) in [(57, 70), (62, 72), (59, 76), (63, 78), (57, 79)]:
    c.set(hx, hy, HAIRH)
# arms resting on the ring
c.rect(48, 87, 3, 3, SKIN)
c.rect(69, 87, 3, 3, SKIN)
# ring highlights
for (hx, hy) in [(49, 88), (52, 85), (68, 85), (71, 88), (60, 83), (55, 84), (65, 84)]:
    c.set(hx, hy, YELH)

# faint reflection of the girl below
for y in range(104, 114, 2):
    dx = int(2 * math.sin(y / 3.0))
    if (y // 2) % 2 == 0:
        c.set(59 + dx, y, RIPD)
        c.set(60 + dx, y, RIPD)

print(c.stats_text())
finish(c)
