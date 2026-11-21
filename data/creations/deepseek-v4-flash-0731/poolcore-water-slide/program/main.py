import math
from pixelbench_api import *

W = 128
H = 128
c = new_canvas(W, H, name="pool")

# ---- palette ----
CEIL = (224, 236, 244)
PANEL = (246, 251, 253)
WALLB = (184, 214, 230)
WALL_L = (158, 194, 214)
WALL_HI = (226, 240, 246)
GRD = (140, 180, 204)
DOOR = (64, 104, 124)
DOOR2 = (54, 92, 112)
SIGN = (38, 62, 72)
GREEN = (96, 214, 120)
RIM = (238, 244, 248)
W0 = (176, 214, 234)
W1 = (154, 200, 224)
W2 = (134, 186, 214)
W3 = (114, 170, 202)
W4 = (96, 154, 190)
REFL = (202, 228, 242)
REFL2 = (188, 220, 238)
RIP = (196, 226, 240)
RIP2 = (180, 214, 234)
SLD = (244, 248, 252)
SLD_SH = (206, 220, 232)
SLD_DK = (156, 182, 202)
WHITE = (252, 254, 255)
YEL = (246, 198, 64)
YEL_DK = (212, 158, 40)
YEL_HI = (252, 228, 132)
HAIR = (64, 46, 36)
HAIR_DK = (48, 34, 28)
HAIR_HI = (96, 74, 58)
SKIN = (240, 200, 166)
SUIT = (122, 172, 206)

# ---- ceiling ----
c.rect(0, 0, W, 24, CEIL)
for x in range(0, W, 16):
    c.rect(x + 2, 3, 12, 6, PANEL)
    c.rect(x + 2, 14, 12, 6, PANEL)

# ---- back wall mosaic ----
c.rect(0, 24, W, 60, WALLB)
ys = [24, 30, 36, 41, 46, 50, 54, 58, 61, 64, 67, 70, 73, 76, 79, 81, 83]
for y in ys:
    c.line(0, y, W - 1, y, WALL_L)
for x in range(0, W, 8):
    c.line(x, 24, x, 83, WALL_L)
c.rect(4, 24, 26, 2, WALL_HI)
c.rect(36, 24, 56, 2, WALL_HI)
c.rect(98, 24, 26, 2, WALL_HI)

# ---- doorway + EXIT sign ----
c.rect(49, 30, 30, 54, WALL_HI)
c.rect(51, 31, 26, 53, DOOR)
c.rect(53, 34, 22, 50, DOOR2)
c.rect(51, 31, 26, 3, (84, 124, 144))
c.rect(50, 24, 28, 8, SIGN)
c.text(53, 25, "EXIT", GREEN, font="5x7")

# ---- tiled columns ----
for cx in (14, 102):
    c.rect(cx, 24, 12, 60, WALL_HI)
    for x in range(cx + 3, cx + 10, 4):
        c.line(x, 24, x, 83, WALL_L)
    for y in ys[1:]:
        c.line(cx, y, cx + 11, y, WALL_L)
    c.rect(cx + 9, 24, 3, 60, WALL_L)
    c.line(cx + 11, 24, cx + 11, 83, GRD)
    c.rect(cx, 24, 2, 60, (232, 244, 250))

# ---- floor edge / coping ----
c.rect(0, 83, W, 1, (150, 190, 212))
c.rect(0, 84, W, 2, RIM)
for x in range(0, W, 8):
    c.line(x, 84, x, 85, WALL_L)

# ---- slide support legs ----
c.rect(106, 42, 3, 43, SLD)
c.rect(121, 42, 3, 43, SLD)

# ---- pool water ----
c.rect(0, 86, W, 10, W0)
c.rect(0, 96, W, 10, W1)
c.rect(0, 106, W, 9, W2)
c.rect(0, 115, W, 7, W3)
c.rect(0, 122, W, 6, W4)
c.dither(0, 95, W, 1, [W0, W1])
c.dither(0, 105, W, 1, [W1, W2])
c.dither(0, 114, W, 1, [W2, W3])
c.dither(0, 121, W, 1, [W3, W4])

# ---- pool floor mosaic seen through water ----
for x in range(0, W, 8):
    c.line(x, 99, x, 127, (148, 194, 218))
    c.line(x + 4, 104, x + 4, 127, (134, 180, 206))
    c.line(x + 2, 112, x + 2, 127, (120, 166, 196))
for yy, col in [(99, (158, 202, 224)), (105, (146, 190, 214)), (111, (132, 178, 206)), (117, (120, 164, 196))]:
    c.line(0, yy, W - 1, yy, col)

# ---- surface reflections ----
for x in range(0, W, 8):
    c.line(x, 86, x, 89, (162, 200, 222))
for xc in [10, 26, 42, 58, 74, 90, 106, 122]:
    c.rect(xc - 3, 86, 6, 5, REFL2)
    c.rect(xc - 2, 91, 4, 5, REFL)
    c.rect(xc - 1, 96, 2, 5, (178, 216, 236))
for (cy, rx, ry, col) in [(99, 34, 2, RIP2), (107, 46, 3, RIP2), (114, 56, 4, RIP)]:
    c.ellipse(64, cy, rx, ry, col, fill=False)
c.ellipse(64, 123, 26, 4, (176, 214, 234), fill=False)
for (sx, sy) in [(30, 103), (98, 117), (70, 125)]:
    c.rect(sx, sy, 2, 1, (216, 238, 246))
    c.rect(sx + 7, sy + 6, 2, 1, (216, 238, 246))

# ---- slide platform ----
c.rect(104, 28, 24, 14, SLD)
c.rect(104, 28, 24, 2, (252, 254, 255))
c.rect(104, 40, 24, 2, SLD_SH)
for x in range(104, 129, 4):
    c.line(x, 30, x, 41, SLD_SH)
c.line(104, 34, 127, 34, SLD_SH)
c.line(104, 37, 127, 37, SLD_SH)

# ---- water slide tube ----
P0 = (120, 30)
P1 = (110, 62)
P2 = (84, 90)
pts = []
n = 40
for i in range(n + 1):
    t = i / n
    a = (1 - t) ** 2
    b = 2 * (1 - t) * t
    g = t * t
    cx = int(a * P0[0] + b * P1[0] + g * P2[0])
    cy = int(a * P0[1] + b * P1[1] + g * P2[1])
    r = 6.0 - 3.0 * t
    pts.append((cx, cy, r))
for (cx, cy, r) in pts:
    c.circle(cx, cy, int(r), SLD)
for (cx, cy, r) in pts:
    rr = int(r)
    c.ellipse(cx, cy + int(r * 0.55), max(1, int(r * 0.55)), max(1, int(r * 0.3)), SLD_SH)
    c.ellipse(cx, cy - int(r * 0.45), max(1, int(r * 0.4)), max(1, int(r * 0.2)), WHITE)

# ---- slide entry + reflection ----
c.rect(81, 88, 7, 2, (250, 252, 254))
for rx, ry in [(8, 2), (12, 3), (16, 3)]:
    c.ellipse(84, 90, rx, ry, (250, 252, 254), fill=False)
c.rect(82, 92, 7, 6, REFL)
c.rect(83, 98, 5, 5, (178, 214, 234))
c.ellipse(84, 100, 10, 3, RIP, fill=False)
c.ellipse(84, 108, 15, 4, RIP2, fill=False)

# ---- girl floating in yellow ring ----
c.ellipse(62, 103, 14, 5, (120, 170, 200))
c.ellipse(62, 97, 4, 4, SUIT)
c.circle(62, 92, 4, HAIR)
c.circle(61, 89, 2, HAIR_HI)
c.circle(62, 95, 2, HAIR_DK)
c.ellipse(62, 103, 11, 5, YEL)
c.ellipse(62, 103, 7, 3, W1)
c.ellipse(62, 100, 8, 2, YEL_HI, fill=False)
c.circle(53, 100, 2, SKIN)
c.circle(71, 100, 2, SKIN)
c.ellipse(62, 106, 9, 2, YEL_DK, fill=False)
c.rect(60, 108, 4, 4, (210, 172, 104))
c.rect(61, 112, 2, 6, (186, 150, 88))
c.ellipse(62, 111, 13, 3, RIP, fill=False)
c.ellipse(62, 116, 19, 4, RIP, fill=False)
c.ellipse(62, 121, 26, 4, (176, 214, 234), fill=False)

print(c.stats_text())
finish(c)
