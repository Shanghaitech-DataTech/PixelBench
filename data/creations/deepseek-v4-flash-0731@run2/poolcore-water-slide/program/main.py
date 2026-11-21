from pixelbench_api import *

def R(v):
    return int(round(v))

def P(pts):
    return [(R(x), R(y)) for x, y in pts]

c = new_canvas(128, 128)

# ---------------- palette ----------------
ceil   = c.color('#d9eaf4')
ceil_sh = c.color('#c6dfec')
frame  = c.color('#a9cee0')
light  = c.color('#e9f9ff')
lcore  = c.color('#f7feff')
wall   = c.color('#c6e3f1')
wtint  = c.color('#b8d9eb')
grout  = c.color('#97c3d8')
swall  = c.color('#aacedf')
door   = c.color('#1f3c49')
doorin = c.color('#102a35')
col1   = c.color('#f0f8fc')
col2   = c.color('#c9e3f0')
wf     = c.color('#aee0f2')
wm     = c.color('#8ed0ea')
wn     = c.color('#76c1e2')
wd     = c.color('#5cadd5')
wh     = c.color('#d9f4ff')
wr     = c.color('#c5ebfa')
wref   = c.color('#a4d8ee')
sl     = c.color('#f9fdfe')
sls    = c.color('#d2e7f1')
slc    = c.color('#aadaee')
ring   = c.color('#ffd94e')
ringsh = c.color('#e4a63c')
ringh  = c.color('#ffe986')
skin   = c.color('#f0c59c')
skin2  = c.color('#d6a077')
hair   = c.color('#5d4635')
hair2  = c.color('#453223')
suit   = c.color('#ddeef5')
suit2  = c.color('#b3d2e4')

# ---------------- helpers ----------------
def bez(p0, p1, p2, p3, n=64):
    out = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t**3 * p3[1]
        out.append((x, y))
    return out

def offs(pts, w):
    res = []
    n = len(pts)
    for i, pt in enumerate(pts):
        if i == 0:
            nx, ny = pts[1][0] - pt[0], pts[1][1] - pt[1]
        elif i == n - 1:
            nx, ny = pt[0] - pts[i - 1][0], pt[1] - pts[i - 1][1]
        else:
            nx, ny = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        L = (nx * nx + ny * ny) ** 0.5 or 1.0
        # perpendicular offset
        res.append((pt[0] - ny / L * w, pt[1] + nx / L * w))
    return res

# ---------------- ceiling ----------------
c.poly(P([(0, 0), (128, 0), (106, 28), (22, 28)]), ceil)
c.poly(P([(22, 28), (106, 28), (107, 20), (21, 20)]), ceil_sh)
c.line(24, 25, 104, 22, frame)
c.line(21, 18, 107, 11, frame)
c.line(18, 9, 110, 4, frame)
for k in (-0.5, -0.25, 0, 0.25, 0.5):
    xb = 64 + 78 * k
    xf = 64 + 124 * k
    c.poly(P([(xb - 2.2, 28.8), (xb + 2.2, 28.8), (xf + 6.4, 1.2), (xf - 6.4, 1.2)]), light)
    c.line(R(xb), 28, R(xf), 1, lcore)

# ---------------- back wall ----------------
c.line(22, 28, 106, 28, frame)
for i in range(10):
    for j in range(6):
        cc = wall if (i + j) % 2 == 0 else wtint
        c.rect(22 + i * 8, 28 + j * 6, 8, 6, cc)
for i in range(1, 10):
    c.line(22 + i * 8, 28, 22 + i * 8, 63, grout)
for j in range(1, 6):
    c.line(22, 28 + j * 6, 102, 28 + j * 6, grout)
# back columns
for cx in (37.0, 91.0):
    c.rect(R(cx - 3), 28, 6, 36, col1)
    c.rect(R(cx - 1), 28, 2, 36, col2)
    c.line(R(cx), 28, R(cx), 63, frame)
# arched doorway (dark, uncanny)
c.poly(P([(54, 58), (74, 58), (74, 64), (54, 64)]), door)
c.path("M 54 58 A 10 10 0 0 1 74 58 L 74 64 L 54 64 Z", door)
c.rect(58, 44, 8, 20, doorin)
c.rect(44, 40, 2, 6, doorin)
c.rect(82, 40, 2, 6, doorin)

# ---------------- side walls ----------------
c.poly(P([(22, 28), (0, 0), (0, 128), (22, 64)]), swall)
c.poly(P([(106, 28), (128, 0), (128, 128), (106, 64)]), swall)
for k in (0.15, 0.3, 0.5, 0.7, 0.85):
    Ax = 22 - 22 * k
    Ay = 28 - 28 * k
    c.line(R(Ax), R(Ay), R(22 - 22 * k), R(64 + 64 * k), grout)
    Ax = 106 + 22 * k
    c.line(R(Ax), R(Ay), R(106 + 22 * k), R(64 + 64 * k), grout)
for (yb, yf) in [(33, 16), (43, 42), (53, 72), (61, 102)]:
    c.line(22, yb, 0, yf, grout)
    c.line(106, yb, 128, yf, grout)

# ---------------- interior tiled columns in the pool ----------------
for t in (0.3, 0.66):
    for side in (-1, 1):
        x = 64 + side * (42 + 22 * t)
        ytop = 28 - 28 * t
        ybot = 64 + 64 * t
        w = 8.5 + 6.5 * t
        c.rect(R(x - w / 2), R(ytop), R(w), R(ybot - ytop), col1)
        c.rect(R(x - w * 0.4), R(ytop), R(w * 0.58), R(ybot - ytop), col2)

# ---------------- water ----------------
c.poly(P([(22, 64), (106, 64), (128, 128), (0, 128)]), wm)
c.poly(P([(22, 64), (106, 64), (104, 70), (24, 70)]), wf)
c.poly(P([(24, 70), (104, 70), (96, 90), (32, 90)]), wn)
c.poly(P([(32, 90), (96, 90), (128, 128), (0, 128)]), wn)
c.poly(P([(40, 100), (88, 100), (128, 128), (0, 128)]), wd)
c.line(22, 64, 106, 64, wh)

# shore dashes
for i in range(24):
    t = (i + 0.5) / 24.0
    y = 64 + 64 * t
    c.line(R(22 - 22 * t), R(y), R(22 - 22 * t) + 3, R(y), wh)
    c.line(R(106 + 22 * t), R(y), R(106 + 22 * t) + 3, R(y), wh)

# ceiling reflections on the water
for k in (-0.5, -0.25, 0, 0.25, 0.5):
    xb = 64 + 78 * k
    c.rect(R(xb) - 2, 66, 4, 12, wref)
    c.rect(R(xb) - 1, 66, 2, 9, wh)
# column reflections
for t in (0.3, 0.66):
    for side in (-1, 1):
        x = 64 + side * (42 + 22 * t)
        yb = 64 + 64 * t
        w = 8.5 + 6.5 * t
        c.rect(R(x - w * 0.36), R(yb) + 3, R(w * 0.64), 12, wref)
        c.rect(R(x - w * 0.18), R(yb) + 4, R(w * 0.36), 9, wh)

# gentle caustic ripples / waves on the water
for (xx, yo) in [(28, 72), (42, 74), (56, 77), (70, 79), (83, 79), (34, 86), (62, 88), (24, 90),
                (46, 97), (70, 96), (94, 92), (36, 106), (58, 106), (80, 104), (48, 114), (68, 112), (30, 100)]:
    c.path("M %d %d q 5 3 10 0" % (xx, yo), wh)
for (xx, yo) in [(33, 70), (80, 76), (52, 84), (28, 95), (60, 102), (46, 112), (72, 110), (90, 98)]:
    c.line(xx, yo, xx + 5, yo, wh)

# ---------------- white water slide ----------------
pts = bez((114, 36), (119, 58), (102, 74), (93, 88))
An = offs(pts, 5.4)
c.poly(P(An + offs(pts, -5.4)[::-1]), sl)
c.poly(P(offs(pts, 2.2) + offs(pts, -2.2)[::-1]), slc)
c.poly(P(offs(pts, 5.4) + offs(pts, 3.6)[::-1]), sls)
c.poly(P(offs(pts, -5.4) + offs(pts, -3.4)[::-1]), lcore)
# tuck the tip into the water
c.ellipse(93, 88, 7, 4, wn)
# entry ripples
c.ellipse(93, 89, 9.5, 4.0, wr, False)
c.ellipse(93, 89, 13, 5.6, wr, False)
c.ellipse(93, 89, 16.5, 7.0, wr, False)
# slide reflection on the water
c.rect(R(86), 92, 12, 5, wref)
c.rect(R(88), 93, 8, 7, wh)

# ---------------- girl floating in a yellow ring, from behind ----------------
# reflection
c.ellipse(58, 99, 9, 3.0, wref)
c.ellipse(58, 100, 6.5, 2.2, wh)
# ripples around her
c.ellipse(58, 90.5, 13.5, 5.2, wr, False)
c.ellipse(58, 90.5, 16.5, 6.8, wr, False)
c.ellipse(58, 93, 18.5, 8.5, wr, False)
# torso (back, swimsuit)
c.rect(54, 77, 8, 8, suit)
c.rect(56, 79, 4, 5, suit2)
# ring
c.ellipse(58, 89, 11, 4.4, ring)
c.ellipse(58, 91.5, 9.5, 2.7, ringsh)
c.ellipse(58, 87.6, 8.6, 1.8, ringh)
# head (back of head / hair)
c.circle(58, 74, 4, hair)
c.circle(56.8, 75.2, 2.2, hair2)
# arms over the ring
c.rect(R(54.0), 78, 3, 7, skin)
c.rect(R(59.0), 78, 3, 7, skin)
c.rect(R(54.0), 80, 1, 5, skin2)
c.rect(R(59.0), 80, 1, 5, skin2)
# more sparkles
for (xx, yo, _z) in [(40, 76, 4), (74, 82, 5), (56, 104, 4), (84, 100, 4), (70, 110, 5), (44, 116, 4)]:
    c.line(xx, yo, xx + 3, yo, wh)

print(c.stats_text())

result = c
finish(result)
