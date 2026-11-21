import math
from pixelbench_api import *

def thick_line(c, x0, y0, x1, y1, w, col):
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy)
    if L == 0:
        c.rect(int(x0 - w / 2), int(y0 - w / 2), w, w, col)
        return
    px = -dy / L * (w - 1) / 2
    py = dx / L * (w - 1) / 2
    c.poly([(x0 + px, y0 + py), (x1 + px, y1 + py), (x1 - px, y1 - py), (x0 - px, y0 - py)], col)

W = H = 128
scene = new_canvas(W, H, name="standoff")

# ---- palette ----
OUT   = scene.color("#0c0812")
SKY1  = scene.color("#0a0716")
SKY2  = scene.color("#110d24")
SKY3  = scene.color("#1c1535")
SKY4  = scene.color("#2a1f47")
SKY5  = scene.color("#3a2a56")
SKY6  = scene.color("#4a3763")
SKYH  = scene.color("#5f4470")
CLD   = scene.color("#221840")
CLDD  = scene.color("#17112e")
HILL  = scene.color("#0e0a22")
GNDD  = scene.color("#150f22")
GNDL  = scene.color("#2b1f38")
GNDH  = scene.color("#48325e")
MOON  = scene.color("#f6e6b4")
MOONL = scene.color("#fff7da")
MOONH = scene.color("#d6b474")
LIT   = scene.color("#ffe67f")
LITG  = scene.color("#c9a24c")
WIND  = scene.color("#8f6fb0")
WIND2 = scene.color("#5b457c")
SHAD  = scene.color("#080610")
KR    = scene.color("#d43a2c")
KRD   = scene.color("#8f231a")
KRL   = scene.color("#ff6a48")
PR    = scene.color("#ff4a3a")
PRL   = scene.color("#ff9a50")
STEEL = scene.color("#c8cfdb")
STEELD = scene.color("#88919e")
STELL = scene.color("#f2f6ff")
GOLD = scene.color("#e8b64a")
BRND  = scene.color("#4a2f1e")
EYEK  = scene.color("#ffb31a")
RG    = scene.color("#3f9c4f")
RGD   = scene.color("#1f5427")
RGL   = scene.color("#7ad96e")
GLV   = scene.color("#6b4a2c")
GLVD  = scene.color("#3c2a18")
EYE   = scene.color("#c8ff5a")

# ---- sky bands ----
scene.rect(0, 0, 128, 21, SKY1)
scene.rect(0, 21, 128, 14, SKY2)
scene.rect(0, 35, 128, 14, SKY3)
scene.rect(0, 49, 128, 14, SKY4)
scene.rect(0, 63, 128, 12, SKY5)
scene.rect(0, 75, 128, 10, SKY6)
scene.rect(0, 85, 128, 7, SKYH)

# ---- moon ----
scene.circle(64, 38, 18, MOONH)
scene.circle(64, 38, 13, MOON)
scene.circle(60, 34, 7, MOONL)

# ---- clouds ----
scene.rect(0, 20, 42, 5, CLD)
scene.rect(88, 18, 40, 6, CLD)
scene.rect(22, 44, 58, 4, CLDD)
scene.rect(96, 48, 30, 4, CLDD)
scene.rect(2, 60, 30, 3, CLD)

# ---- hills ----
scene.poly([(0, 94), (14, 82), (34, 90), (56, 84), (82, 92), (104, 82), (127, 88), (127, 96), (0, 96)], HILL)

# ---- ground ----
scene.rect(0, 96, 128, 32, GNDD)
scene.rect(0, 96, 128, 2, GNDL)
scene.rect(0, 106, 128, 2, GNDH)
scene.rect(52, 96, 24, 3, GNDH)
scene.line(14, 112, 30, 112, CLDD)
scene.line(86, 114, 104, 112, HILL)
scene.line(52, 120, 74, 120, CLDD)

# ---- lightning ----
bolt = [(64, 12), (58, 30), (65, 38), (59, 50), (65, 58), (61, 70), (64, 84)]
for i in range(len(bolt) - 1):
    thick_line(scene, bolt[i][0], bolt[i][1], bolt[i + 1][0], bolt[i + 1][1], 5, LITG)
for i in range(len(bolt) - 1):
    thick_line(scene, bolt[i][0], bolt[i][1], bolt[i + 1][0], bolt[i + 1][1], 2, LIT)
for i in range(len(bolt) - 1):
    thick_line(scene, bolt[i][0], bolt[i][1], bolt[i + 1][0], bolt[i + 1][1], 1, MOONL)
thick_line(scene, 59, 50, 54, 58, 2, LIT)
thick_line(scene, 64, 12, 66, 16, 2, LIT)
scene.ellipse(63, 89, 6, 3, LITG)
scene.ellipse(63, 92, 3, 2, LIT)
scene.set(63, 89, MOONL)
scene.circle(68, 43, 2, MOONH)
scene.circle(70, 36, 1, MOONH)
scene.circle(60, 45, 1, MOONH)

# ---- wind ----
scene.line(20, 34, 34, 34, WIND2)
scene.line(54, 42, 64, 42, WIND)
scene.line(68, 46, 78, 46, WIND2)
scene.line(56, 60, 66, 60, WIND)
scene.line(42, 28, 50, 28, WIND2)
scene.line(84, 32, 92, 32, WIND2)

# ---- shadows ----
scene.ellipse(35, 97, 12, 3, SHAD)
scene.ellipse(81, 96, 14, 3, SHAD)

# ---- knight (left) ----
k = new_canvas(W, H, name="knight")
k.poly([(30, 50), (16, 64), (14, 84), (23, 91), (33, 86), (35, 56)], KRD)
k.rect(32, 45, 6, 6, KR)
k.rect(24, 74, 6, 14, KRD)
k.rect(23, 86, 8, 10, STEELD)
k.rect(33, 74, 8, 14, KR)
k.rect(32, 86, 9, 10, STEEL)
k.rect(26, 50, 17, 26, KR)
k.rect(26, 72, 17, 3, STEELD)
k.rect(34, 54, 7, 8, KRL)
k.circle(29, 48, 4, KRD)
k.circle(40, 47, 5, KR)
k.circle(43, 44, 2, KRL)
k.rect(28, 32, 12, 14, KR)
k.circle(34, 37, 6, KR)
k.rect(33, 36, 9, 3, OUT)
k.set(41, 37, EYEK)
k.set(40, 38, EYEK)
k.poly([(30, 32), (32, 24), (35, 29), (38, 23), (40, 31)], PR)
k.set(33, 25, PRL)
k.poly([(22, 56), (18, 61), (18, 70), (23, 76), (28, 76), (30, 66), (30, 58)], STEEL)
k.rect(23, 63, 6, 2, GOLD)
k.rect(25, 62, 2, 6, GOLD)
thick_line(k, 42, 52, 45, 47, 5, KR)
k.circle(46, 45, 2, STEEL)
k.rect(45, 47, 5, 5, BRND)
k.rect(43, 52, 9, 3, GOLD)
k.rect(46, 28, 4, 16, STEEL)
k.rect(47, 30, 1, 10, STELL)
k.poly([(46, 28), (50, 28), (48, 24)], STELL)
k.outline(OUT)
k.set(41, 42, KRL)
k.set(30, 38, KRL)
k.set(40, 28, PRL)

# ---- rogue (right) ----
r = new_canvas(W, H, name="rogue")
r.poly([(82, 52), (93, 58), (93, 91), (82, 97), (68, 95), (62, 88), (64, 62)], RGD)
r.poly([(72, 60), (88, 64), (88, 88), (80, 92), (70, 86), (68, 68)], RG)
r.rect(71, 79, 18, 3, GLVD)
r.rect(72, 88, 7, 7, GLVD)
r.rect(84, 88, 7, 7, GLVD)
r.circle(80, 44, 8, RG)
r.rect(73, 40, 11, 10, RG)
r.poly([(74, 41), (63, 46), (67, 52), (75, 48)], RGD)
r.poly([(76, 44), (85, 44), (86, 51), (77, 53)], GLVD)
r.set(78, 46, EYE)
r.set(77, 47, RGL)
thick_line(r, 82, 54, 89, 47, 4, RGD)
r.circle(90, 46, 2, GLV)
r.rect(88, 28, 3, 15, STELL)
r.poly([(88, 28), (91, 28), (89, 25)], STELL)
thick_line(r, 75, 58, 66, 64, 4, RGD)
r.circle(65, 65, 2, GLV)
r.poly([(63, 63), (55, 64), (55, 68), (63, 67)], STELL)
r.set(57, 65, MOONL)
r.outline(OUT)
r.set(68, 54, RGL)
r.set(66, 60, RGL)
r.set(65, 66, RGL)
r.set(63, 52, RGL)

# ---- compose ----
scene.blit(k, 0, 0)
scene.blit(r, 0, 0)

# ---- final sparks ----
scene.set(52, 26, MOONL)
scene.set(56, 44, LIT)
scene.set(50, 60, LITG)
scene.set(66, 36, LITG)
scene.set(60, 70, LIT)
scene.set(66, 56, MOONL)
scene.set(50, 76, LIT)
scene.set(58, 80, MOONL)
scene.set(54, 68, MOONL)
scene.set(70, 62, LIT)
scene.set(64, 74, LITG)
scene.set(62, 44, MOONL)
scene.set(54, 40, LIT)
scene.set(72, 55, MOONL)

print(scene.stats_text())
print("K-HEAD:")
print(scene.matrix_text(region=(14, 16, 52, 58)))
print("MID:")
print(scene.matrix_text(region=(44, 20, 78, 60)))
print("ROGUE-HEAD:")
print(scene.matrix_text(region=(58, 34, 100, 60)))
print("LOWER:")
print(scene.matrix_text(region=(14, 80, 110, 98)))

finish(scene)
