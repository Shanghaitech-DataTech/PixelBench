from pixelbench_api import *

W, H = 58, 64
OX, OY = 6, 2

OUT   = '#101010'
GRAYD = '#5A565A'
GRAYL = '#858086'
GRAYM = '#A9A5AB'
STEEL = '#A8A098'
SHINE = '#FFFFD5'
GOLD  = '#C67B02'
GOLDL = '#FFCC43'
BROWN = '#512A13'
BROWNL= '#AF7A18'
GLOVE = '#702125'
GLOVEL= '#804018'
WHITE = '#FFFFFF'
CAPE  = '#D6007F'
CAPED = '#690036'
SHADOW= '#17003599'

f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, OX, OY)

f2 = f1.copy(name="frame2")

# ---- erase raised hammer / haft / gauntlet (pink cape pixels protected) ----
PINK = {8, 9, 12, 13, 14, 17}
def keep(x, y):
    idx = f2.get(x, y)
    if idx == 0 or idx in PINK:
        return True
    if idx == 1:
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if f2.get(nx, ny) in PINK:
                return True
    return False

ZONES = [(0,7,17),(8,9,22),(10,10,24),(11,11,25),(12,12,26),(13,13,29),
         (14,14,30),(15,21,33),(22,22,36),(23,23,35),(24,24,36),(25,25,36)]
for y0, y1, x0 in ZONES:
    for y in range(y0, y1 + 1):
        for x in range(x0, 50):
            if not keep(x, y):
                f2.set(x, y, None)
f2.set(22, 9, OUT)  # helmet edge outline

# ---- cape top / right edge rebuilt where the arm used to cover it ----
f2.set(36, 25, CAPED)
f2.set(38, 26, CAPED); f2.set(39, 26, OUT); f2.set(40, 26, OUT)
f2.set(39, 25, OUT)
for y in range(20, 25):
    f2.set(41, y, CAPED); f2.set(42, y, OUT)

# ---- white motion trail: tapered swoosh along the swing arc ----
P0, P1, P2 = (28.0, 3.0), (52.0, 10.0), (51.0, 34.0)
N = 30
pts = []
for i in range(N + 1):
    t = i / float(N)
    x = (1 - t) ** 2 * P0[0] + 2 * t * (1 - t) * P1[0] + t * t * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * t * (1 - t) * P1[1] + t * t * P2[1]
    r = 1.5 + 2.5 * t
    pts.append((int(round(x)), int(round(y)), r))
for x, y, r in pts:
    f2.circle(x, y, int(round(r + 1)), GRAYD)
for x, y, r in pts:
    f2.circle(x, y, int(round(r)), WHITE)
for i in range(2, N - 1, 4):
    x, y, r = pts[i]
    f2.set(x, y, SHINE)

# ---- pauldron on the right shoulder ----
f2.line(37, 16, 38, 16, OUT)
f2.set(36, 17, OUT); f2.set(37, 17, GRAYM); f2.set(38, 17, GRAYM); f2.set(39, 17, OUT)
f2.set(35, 18, OUT); f2.set(36, 18, GRAYL); f2.set(37, 18, GRAYM); f2.set(38, 18, GRAYM)
f2.set(39, 18, GRAYD); f2.set(40, 18, OUT)
f2.set(35, 19, OUT); f2.set(36, 19, GRAYL); f2.set(37, 19, GRAYM); f2.set(38, 19, GRAYM)
f2.set(39, 19, GRAYD); f2.set(40, 19, OUT)
f2.set(35, 20, OUT); f2.set(36, 20, GRAYD); f2.set(37, 20, GRAYM); f2.set(38, 20, GRAYD)
f2.set(39, 20, GRAYD); f2.set(40, 20, OUT)
f2.set(35, 21, OUT); f2.set(36, 21, GOLD); f2.set(37, 21, GOLD); f2.set(38, 21, GOLD)
f2.set(39, 21, GOLD); f2.set(40, 21, OUT)
f2.line(35, 22, 40, 22, OUT)

# ---- arm hanging down from the pauldron ----
for y in range(23, 32):
    f2.set(36, y, OUT); f2.set(37, y, GRAYD); f2.set(38, y, GRAYL); f2.set(39, y, OUT)
# fist
f2.rect(36, 32, 4, 4, GLOVE)
f2.set(37, 33, GLOVEL)
for px, py in [(35,32),(35,33),(35,34),(35,35),(40,32),(40,33),(40,34),(40,35),
               (36,36),(37,36),(38,36),(39,36)]:
    f2.set(px, py, OUT)

# ---- haft angled down-right ----
f2.line(38, 35, 46, 42, BROWN)
f2.line(39, 36, 47, 43, BROWN)
f2.line(37, 35, 45, 42, BROWNL)
f2.line(40, 36, 48, 43, OUT)
f2.line(37, 34, 45, 41, OUT)

# ---- hammer head slammed down at lower right ----
f2.rect(42, 38, 13, 10, OUT)
f2.rect(43, 39, 11, 8, GRAYM)
f2.rect(44, 39, 9, 1, STEEL)
f2.set(45, 40, SHINE); f2.set(46, 40, SHINE); f2.set(46, 41, SHINE); f2.set(47, 41, SHINE)
f2.rect(43, 46, 11, 1, GRAYD)
f2.rect(43, 39, 1, 8, GRAYL)
f2.rect(53, 39, 1, 8, GRAYL)
f2.rect(47, 39, 1, 8, GOLD)
# impact sparks
f2.set(40, 49, GOLDL); f2.set(56, 49, GOLDL); f2.set(48, 50, GOLDL)

# ---- footing: left foot (viewer right) steps forward ----
f2.rect(26, 48, 11, 13, None)   # old lower leg + foot
f2.rect(37, 55, 2, 6, None)     # old shadow remnant
shin = [(30,48),(31,49),(32,50),(33,51),(34,52),(35,53),(36,54)]
for x, y in shin:
    f2.set(x, y, GRAYD)
    f2.set(x + 1, y, GRAYL)
    f2.set(x - 1, y, OUT)
    f2.set(x + 2, y, OUT)
f2.rect(34, 54, 4, 1, GOLD)
f2.rect(34, 55, 9, 3, GRAYD)
f2.rect(41, 55, 2, 2, GOLDL)
for py in (55, 56, 57):
    f2.set(33, py, OUT)
    f2.set(43, py, OUT)
f2.line(33, 58, 43, 58, OUT)
f2.rect(36, 58, 8, 3, SHADOW)
f2.rect(38, 61, 5, 1, SHADOW)

view(f1)
view(f2)
finish([f1, f2])
