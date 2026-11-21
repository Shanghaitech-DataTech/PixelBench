import math
from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, background=(9, 7, 9), name="open-pocket-watch")

GL = (16, 12, 11)
IK = (4, 3, 4)
SH = (13, 10, 9)
GDK = (52, 41, 26)
GD2 = (78, 61, 39)
GMD = (110, 86, 54)
GOL = (143, 114, 73)
GLT = (178, 146, 96)
GHI = (210, 178, 126)
GBR = (236, 206, 156)
GWH = (252, 230, 184)
SDK = (52, 58, 65)
SST = (102, 110, 120)
SLT = (164, 173, 185)
CRE = (233, 221, 198)
RB = (19, 14, 11)
RD = (186, 72, 48)


def wheel(x, y, r, teeth, rim, body, dark, hi, br):
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        col = rim if math.sin(a) < 0.2 else dark
        c.line(round(x + r * math.cos(a)), round(y + r * math.sin(a)),
               round(x + (r + 3) * math.cos(a)), round(y + (r + 3) * math.sin(a)), col)
    c.circle(x, y, r, dark)
    c.circle(x, y, r - 1, body)
    c.circle(x - 1, y - 1, max(1, r - 2), rim)
    c.circle(x, y, max(1, r - 3), hi)
    c.circle(x, y, max(1, r - 4), dark)
    c.circle(x, y, max(1, r - 5), body)
    c.circle(x, y, 1, br)


def link(x, y):
    c.circle(x, y, 3, GDK)
    c.circle(x, y, 2, GOL)
    c.set(x - 1, y - 2, GLT)
    c.set(x - 1, y - 1, GBR)


# vignette glow + floor shadow
c.ellipse(32, 34, 30, 29, GL)
c.ellipse(34, 60, 19, 3, IK)

# case: rim rings first, then recessed movement plate
c.circle(33, 35, 25, GDK)
c.circle(33, 35, 24, GOL)
c.circle(33, 35, 23, GMD)
c.circle(33, 35, 22, GD2)
c.circle(33, 35, 20, RB)
c.circle(32, 34, 19, SH)

# gear train
wheel(32, 26, 9, 12, GOL, GMD, GDK, GLT, GBR)
wheel(18, 17, 5, 8, GLT, GOL, GDK, GHI, GBR)
wheel(46, 18, 5, 8, GMD, GOL, GDK, GLT, GBR)
wheel(20, 33, 4, 6, GLT, GOL, GDK, GBR, GLT)
wheel(45, 34, 4, 6, GOL, GMD, GDK, GLT, GBR)
wheel(13, 27, 3, 6, GMD, GOL, GDK, GHI, GBR)
wheel(51, 28, 3, 6, GOL, GMD, GDK, GLT, GBR)

# dial
c.circle(33, 50, 11, GD2)
c.circle(33, 49, 10, CRE)
c.circle(33, 49, 7, GD2, fill=False)
for i in range(12):
    a = -math.pi / 2 + 2 * math.pi * i / 12
    r0 = 8.4
    r1 = 6.6 if i % 3 == 0 else 7.4
    c.line(round(33 + r0 * math.cos(a)), round(50 + r0 * math.sin(a)),
           round(33 + r1 * math.cos(a)), round(50 + r1 * math.sin(a)), GDK)
c.ellipse(33, 56, 7, 3, RB)

# hands
c.line(34, 52, 43, 46, SH)
c.line(33, 51, 42, 45, GDK)
c.line(32, 50, 40, 45, GLT)
c.line(31, 49, 39, 45, GHI)
c.line(34, 52, 26, 42, SH)
c.line(33, 51, 25, 41, SDK)
c.line(32, 50, 26, 42, SST)
c.line(34, 51, 43, 50, RD)
c.line(33, 51, 27, 52, RD)
c.circle(33, 51, 2, GD2)
c.circle(33, 50, 1, GBR)
c.set(32, 49, GWH)

# bezel engraving highlights on the rim
c.path("M 15 17 A 24 24 0 0 1 50 17", GHI, fill=False)
c.path("M 19 20 A 20 20 0 0 1 47 20", GBR, fill=False)
for sx, sy in [(14, 23), (52, 24), (14, 48), (52, 47)]:
    c.circle(sx, sy, 1, GLT)
    c.set(sx, sy, GHI)
c.set(30, 12, GWH)

# open lid above the case
c.ellipse(33, 5, 25, 8, GDK)
c.ellipse(33, 4, 24, 7, GOL)
c.ellipse(33, 4, 22, 6, GD2)
c.ellipse(33, 3, 20, 4.5, GLT)
c.ellipse(33, 3, 16, 3.2, GDK, fill=False)
c.ellipse(33, 2, 12, 2.4, GHI, fill=False)
c.ellipse(33, 1.5, 8, 1.5, GBR, fill=False)
c.set(28, 2, GWH)
c.set(31, 1, GWH)

# hinge + crown
c.rect(27, 8, 12, 3, GDK)
c.rect(28, 7, 10, 2, GOL)
c.rect(30, 7, 6, 1, GLT)
c.rect(6, 24, 4, 6, GDK)
c.rect(7, 25, 3, 5, GOL)
c.rect(7, 24, 3, 2, GLT)

# chain
link(4, 7)
link(7, 12)
link(8, 17)
link(8, 21)

# glass glints
c.set(24, 43, GLT)
c.set(27, 41, GLT)
c.set(30, 39, GLT)
c.set(33, 38, GWH)
c.set(25, 44, GLT)
c.set(36, 40, GLT)

print(c.stats_text())
finish(c)
