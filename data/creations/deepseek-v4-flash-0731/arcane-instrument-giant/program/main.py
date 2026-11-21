import math, random
from pixelbench_api import new_canvas, flatten, finish

W = H = 256
CX, CY = 128, 118
ASP = 0.45
random.seed(11)

# ---------------- palette ----------------
BG0 = (8, 6, 14)
BG1 = (15, 12, 24)
BG2 = (24, 19, 36)
BG3 = (36, 28, 52)
BG4 = (52, 42, 72)
PIL  = (17, 13, 26)
PIL2 = (30, 24, 44)
H1  = (52, 30, 16)
H2  = (96, 56, 24)
H3  = (150, 86, 34)
FLB = (11, 9, 16)
FL2 = (26, 20, 16)
STK = (22, 20, 26)
STD = (38, 36, 44)
STM = (66, 62, 72)
STL = (104, 98, 110)
STH = (144, 136, 148)
BRO = (28, 18, 6)
BRD = (56, 40, 14)
BRM = (100, 72, 30)
BRL = (158, 114, 46)
BRH = (210, 160, 68)
BRB = (242, 196, 104)
GLD = (255, 212, 104)
CO0 = (74, 40, 20)
CO1 = (126, 64, 28)
CO2 = (186, 102, 42)
CO3 = (238, 152, 58)
CO4 = (255, 208, 112)
CO5 = (255, 248, 224)
WH  = (255, 255, 255)
RCD = (54, 152, 214)
RC  = (132, 242, 255)
RMD = (150, 74, 206)
RM  = (255, 120, 255)
CRB = (92, 190, 242)
CRL = (170, 242, 255)
CRH = (234, 254, 255)
VIB = (130, 102, 224)
VIL = (190, 152, 255)
VIH = (242, 228, 255)
EMB = (74, 186, 126)
EML = (152, 246, 194)
EMH = (226, 255, 240)
SL  = (130, 134, 142)
SLD = (76, 80, 88)

GLYPHS = [
    [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)],
    [(-1, -1), (0, -2), (1, -1), (1, 1), (0, 2), (-1, 1)],
    [(0, -2), (0, 0), (0, 2), (-1, 0), (1, 0), (-2, 1), (2, -1)],
    [(-1, -1), (0, -1), (1, -1), (0, 0), (-1, 1), (0, 1)],
    [(0, -2), (-1, 0), (0, 0), (0, 1), (1, 0), (0, 2)],
]


def ell(c, r, colour, fill=False):
    c.ellipse(CX, CY, r, int(r * ASP), colour, fill=fill)


def rune(c, x, y, halo, glyph, idx):
    c.circle(x, y, 3, halo)
    for dx, dy in GLYPHS[idx % len(GLYPHS)]:
        c.set(x + dx, y + dy, glyph)


def gear(c, cx, cy, r, teeth):
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        x = round(cx + math.cos(a) * (r - 1))
        y = round(cy + math.sin(a) * (r - 1))
        c.rect(x - 1, y - 1, 3, 3, BRD)
    c.circle(cx, cy, max(1, r - 2), BRM)
    c.circle(cx, cy, max(1, r - 5), BRL)
    c.circle(cx, cy, max(1, r - 8), BRH)
    c.circle(cx, cy, 2, BRD)
    c.circle(cx, cy, 1, BRB)


def dial(c, cx, cy, r):
    c.circle(cx, cy, r, BRD)
    c.circle(cx, cy, r - 1, BRL)
    c.circle(cx, cy, r - 3, STL)
    for i in range(12):
        a = 2 * math.pi * i / 12
        x1 = round(cx + math.cos(a) * (r - 2))
        y1 = round(cy + math.sin(a) * (r - 2))
        x2 = round(cx + math.cos(a) * (r - 4))
        y2 = round(cy + math.sin(a) * (r - 4))
        c.line(x1, y1, x2, y2, SLD)
    a = 0.9
    c.line(cx, cy, round(cx + math.cos(a) * (r - 4)), round(cy + math.sin(a) * (r - 4)), BRD)
    c.circle(cx, cy, 1, BRB)


def sphere(c, cx, cy, base, light, hi, ringcol):
    c.ellipse(cx, cy, 12, 5, ringcol, fill=False)
    c.circle(cx, cy, 7, base)
    c.circle(cx, cy, 5, light)
    c.circle(cx - 2, cy - 2, 2, hi)
    c.set(cx - 3, cy - 3, WH)
    c.set(cx + 1, cy + 3, ringcol)


# ---------------- background / hall ----------------
bg = new_canvas(W, H)
bg.rect(0, 0, W, H, BG0)
bg.ellipse(CX, 116, 128, 76, BG1)
bg.ellipse(CX, 116, 106, 62, BG2)
bg.ellipse(CX, 114, 88, 50, BG3)
bg.ellipse(CX, 112, 70, 40, BG4)
# columns
bg.rect(2, 4, 19, 218, PIL)
bg.rect(22, 4, 3, 218, PIL2)
bg.rect(234, 4, 19, 218, PIL)
bg.rect(231, 4, 3, 218, PIL2)
bg.ellipse(CX, 104, 122, 100, PIL, fill=False)
bg.ellipse(CX, 96, 130, 108, PIL2, fill=False)
# floor
bg.rect(0, 224, W, 32, FLB)
bg.rect(0, 224, W, 3, FL2)
bg.ellipse(128, 246, 62, 9, H2)
# warm halo behind instrument
bg.ellipse(CX, 116, 118, 64, H1)
bg.ellipse(CX, 116, 96, 52, H2)
bg.ellipse(CX, 116, 78, 42, H3)
# pedestal
bg.rect(66, 236, 124, 13, STD)
bg.rect(66, 236, 124, 2, STM)
bg.rect(84, 222, 88, 15, STM)
bg.rect(84, 222, 88, 2, STL)
bg.rect(102, 206, 52, 18, STM)
for fx in (110, 122, 134, 146):
    bg.rect(fx, 208, 1, 16, STK)
bg.rect(108, 200, 40, 8, STL)
bg.rect(108, 200, 40, 3, STH)
bg.rect(108, 200, 40, 1, STH)
bg.ellipse(128, 202, 24, 6, STH)
bg.set(112, 216, RCD)
bg.set(136, 216, RCD)
bg.set(124, 208, RCD)
bg.set(130, 224, RCD)

# ---------------- instrument ----------------
inst = new_canvas(W, H)
# massive outer rim
inst.ellipse(CX, CY, 100, 45, BRM)
inst.ellipse(CX, CY, 86, 39, "transparent")
inst.ellipse(CX, CY, 97, 44, BRD, fill=False)
inst.ellipse(CX, CY, 89, 40, BRH, fill=False)
# moat + plate
inst.ellipse(CX, CY, 83, 37, BRD)
inst.ellipse(CX, CY, 78, 35, BRL)
inst.ellipse(CX, CY, 66, 30, BRM)
# rivets
for i in range(16):
    a = 2 * math.pi * i / 16
    x = round(CX + math.cos(a) * 91)
    y = round(CY + math.sin(a) * 91 * ASP)
    inst.set(x, y, BRH)
# spokes
for i in range(24):
    a = 2 * math.pi * i / 24
    x = round(math.cos(a) * 78)
    y = round(math.sin(a) * 78 * ASP)
    inst.line(CX, CY, CX + x, CY + y, BRD)
# engraved grooves
for r in (70, 60, 50, 42):
    ell(inst, r, BRD)
    ell(inst, r - 1, BRH)
ell(inst, 46, BRD)
# dials + gears on the ring
gear(inst, 213, 105, 11, 8)
gear(inst, 43, 131, 9, 8)
gear(inst, 83, 102, 7, 8)
dial(inst, 189, 134, 8)
dial(inst, 128, 161, 8)
# glow runes along rings
rims = [RC, RM, GLD, RC, RM, RC, GLD, RM]
rimh = [RCD, RMD, GLD, RCD, RMD, RCD, GLD, RMD]
for i in range(8):
    a = 2 * math.pi * i / 8
    x = round(CX + math.cos(a) * 90)
    y = round(CY + math.sin(a) * 90 * ASP)
    rune(inst, x, y, rimh[i], rims[i], i)
for i in range(8):
    a = 2 * math.pi * i / 8 + math.pi / 8
    x = round(CX + math.cos(a) * 54)
    y = round(CY + math.sin(a) * 54 * ASP)
    rune(inst, x, y, rimh[(i + 2) % 8], rims[(i + 2) % 8], i + 3)
# radiant rays
for i in range(12):
    a = 2 * math.pi * i / 12
    col = CO2 if i % 2 == 0 else CO1
    inst.line(CX, CY, round(CX + math.cos(a) * 30), round(CY + math.sin(a) * 30 * ASP), col)
for i in range(12):
    a = 2 * math.pi * i / 12 + math.pi / 12
    inst.line(CX, CY, round(CX + math.cos(a) * 22), round(CY + math.sin(a) * 22 * ASP), CO3)
# crown finial
inst.rect(125, 44, 6, 20, BRD)
inst.circle(128, 42, 5, BRD)
inst.circle(128, 41, 3, BRL)
inst.circle(127, 39, 2, BRH)
inst.set(127, 38, WH)
# orbiter arms + crystal spheres
sphere(inst, 221, 129, CRB, CRL, CRH, RCD)
sphere(inst, 103, 76, VIB, VIL, VIH, RMD)
sphere(inst, 60, 149, EMB, EML, EMH, RCD)
# orbit moons
for i, a in enumerate([45, 225, 300]):
    aa = math.pi * a / 180.0
    if a == 45:
        mcol = RC
    elif a == 225:
        mcol = RM
    else:
        mcol = RC
    x = round(CX + math.cos(aa) * 42)
    y = round(CY + math.sin(aa) * 42 * ASP) + 4
    inst.circle(x, y, 2, mcol)
    inst.set(x, y, WH)
# levitation beam
inst.rect(CX - 2, 165, 4, 8, CO4)
inst.rect(CX - 4, 171, 8, 9, CO3)
inst.rect(CX - 7, 178, 14, 9, CO2)
inst.rect(CX - 11, 185, 22, 8, CO1)
inst.rect(CX - 15, 191, 30, 8, CO0)
inst.ellipse(128, 197, 17, 5, CO0)
# central radiant core
inst.ellipse(CX, CY, 24, 11, CO0)
inst.ellipse(CX, CY, 18, 8, CO1)
inst.ellipse(CX, CY, 13, 6, CO2)
inst.ellipse(CX, CY, 9, 4, CO3)
inst.ellipse(CX, CY, 6, 3, CO4)
inst.ellipse(CX, CY, 4, 2, CO5)
inst.circle(CX, CY, 2, WH)
# sparks / dust motes (after outline so they stay crisp)
for _ in range(26):
    a = random.uniform(0, 2 * math.pi)
    r = random.uniform(102, 124)
    x = round(CX + math.cos(a) * r)
    y = round(CY + math.sin(a) * r)
    cset = random.choice([RCD, RMD, RCD, GLD])
    inst.set(x, y, cset)

# ---------------- compose ----------------
result = flatten([bg, inst])

print(inst.stats_text())
print("palette size:", len(inst.palette()))
st = result.stats()
print("final:", st["size"], "colors_used:", st["colors_used"], "coverage:", st["coverage"])

finish(result)
