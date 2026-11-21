import random, math
from pixelbench_api import new_canvas, flatten, finish

random.seed(9071)
W = H = 128

# ---------- palette (target <= 86 visible colours) ----------
SKY = [(14, 4, 30), (20, 9, 42), (27, 14, 52), (35, 20, 62),
      (44, 27, 72), (53, 35, 80), (64, 43, 88), (72, 49, 94)]
GLOW1 = (206, 170, 128)
GLOW2 = (148, 112, 100)
MOON1 = (247, 235, 205)
MOON2 = (224, 206, 164)
MOON3 = (202, 183, 141)
MOON4 = (230, 214, 178)
STAR1 = (236, 226, 255)
STAR2 = (255, 252, 240)
HILL1 = (54, 36, 98)
HILL2 = (38, 26, 60)
HILL3 = (34, 20, 62)
GR1 = (28, 18, 46)
GR2 = (22, 14, 38)
WALL = (104, 94, 110)
GROUT = (54, 46, 64)
BEAM = (66, 48, 36)
BEAMDK = (52, 38, 32)
CHIM = (74, 54, 66)
CHIMT = (58, 42, 56)
CHIMH = (92, 70, 80)
STONE1 = (118, 108, 126)
STONE2 = (92, 82, 104)
FRAME = (58, 38, 34)
WIN1 = (255, 176, 90)
WIN2 = (255, 142, 62)
DOOR = (78, 48, 40)
HANDLE = (238, 200, 124)
ROOF1 = (72, 38, 48)
ROOF2 = (58, 30, 42)
RIDGE = (46, 24, 34)
MOSSD = (72, 102, 62)
MOSSL = (108, 134, 86)
MOSSDK = (56, 80, 52)
STDK = (64, 32, 44)
STLT = (50, 26, 38)
RIM = (66, 46, 34)
PILL = (58, 38, 30)
WINCH = (86, 58, 42)
WINCHL = (120, 88, 60)
BUCK = (102, 72, 52)
WELLIN = (24, 16, 34)
POOL1 = (98, 62, 54)
POOL2 = (120, 76, 56)
POOL3 = (150, 96, 60)
POOL4 = (126, 80, 56)
SLAB1 = (100, 94, 118)
SLAB2 = (118, 108, 136)
SLAB3 = (84, 78, 106)
SLABH = (140, 132, 156)
TRUNK = (40, 26, 42)
TRDK = (28, 18, 32)
RIMT = (62, 44, 62)
BRCH = (52, 36, 54)
LDA = (44, 26, 50)
LDB = (30, 18, 40)
LMA = (84, 40, 66)
LMB = (62, 34, 60)
LIA = (132, 72, 58)
LIB = (150, 94, 62)
FOG1 = (86, 78, 104)
FOG2 = (108, 98, 122)
FOG3 = (132, 122, 146)
FF1 = (255, 236, 150)
FF2 = (255, 246, 196)

bg = new_canvas(W, H)

# ---------------- SKY ----------------
for y in range(0, 88):
    bg.rect(0, y, W, 1, SKY[min(7, y // 11)])

MX, MY, MR = 96, 19, 14
for py in range(max(0, MY - 27), min(W, MY + 28)):
    sk = SKY[min(7, py // 11)]
    for px in range(max(0, MX - 27), min(W, MX + 28)):
        d = math.hypot(px - MX, py - MY)
        if d < MR + 4.6:
            bg.set(px, py, GLOW1)
        elif d < MR + 8.6:
            bg.set(px, py, GLOW2)
bg.circle(MX, MY, MR, MOON1)
bg.circle(MX + 4, MY + 3, MR - 4, MOON2)
bg.circle(MX + 6, MY + 5, MR - 7, MOON3)
bg.circle(MX - 4, MY + 1, 2, MOON4)
bg.circle(MX + 3, MY - 4, 1, MOON3)

for _ in range(46):
    x = random.randint(1, 126); y = random.randint(1, 70)
    if math.hypot(x - MX, y - MY) < 38:
        continue
    bg.set(x, y, STAR1 if random.random() < 0.75 else STAR2)
for x, y in [(18, 12), (8, 30), (30, 6), (60, 8), (84, 10), (120, 12),
            (110, 34), (40, 18), (70, 14), (12, 42), (58, 26), (124, 20)]:
    bg.set(x, y, STAR2)

# ---------------- BACKGROUND HILLS / GROUND ----------------
for x in range(W):
    h = 70 + int(7 * math.sin(x * 0.32) + 4 * math.sin(x * 0.10 + 2.0))
    h = max(58, min(77, h))
    for y in range(h, 82):
        bg.set(x, y, HILL1)
bg.rect(0, 82, W, 6, HILL2)
for x in range(W):
    h = 80 + int(6 * math.sin(x * 0.21 + 4.0) + 3 * math.sin(x * 0.07))
    for y in range(h, 90):
        bg.set(x, y, HILL3)
bg.rect(0, 88, W, 20, GR1)
bg.rect(0, 108, W, 20, GR2)
bg.ellipse(70, 86, 50, 6, HILL1)

# ---------------- COTTAGE ----------------
ct = new_canvas(W, H)
ct.rect(76, 37, 13, 19, CHIM)
ct.rect(74, 34, 17, 5, CHIMT)
ct.rect(77, 35, 9, 2, CHIMH)

ct.rect(34, 64, 60, 36, WALL)
for yy in (67, 74, 81, 88, 95):
    ct.rect(34, yy, 60, 1, GROUT)
    off = 0 if (yy // 7) % 2 == 0 else 6
    for x0 in range(38, 90, 12):
        ct.rect(x0 + off, yy, 1, 6, GROUT)
ct.rect(34, 64, 6, 36, BEAMDK)
ct.rect(88, 64, 6, 36, BEAMDK)
ct.rect(34, 64, 60, 5, BEAM)
ct.rect(40, 69, 3, 3, STONE1)
ct.rect(58, 76, 2, 2, STONE1)
ct.rect(84, 82, 3, 3, STONE2)
ct.rect(46, 92, 2, 3, STONE1)

for wx in (42, 80):
    ct.ellipse(wx + 6, 82, 9, 9, WIN1)
    ct.rect(wx - 1, 73, 15, 24, FRAME)
    ct.rect(wx, 74, 13, 22, WIN1)
    ct.rect(wx, 84, 13, 12, WIN2)
    ct.rect(wx + 5, 74, 2, 22, FRAME)
    ct.rect(wx, 74, 13, 2, FRAME)

ct.rect(57, 64, 22, 36, FRAME)
ct.circle(68, 64, 10, FRAME)
ct.rect(59, 64, 18, 36, DOOR)
ct.circle(68, 66, 8, DOOR)
ct.rect(59, 64, 18, 2, FRAME)
ct.rect(59, 70, 18, 2, FRAME)
ct.set(73, 84, HANDLE)

ct.poly([(64, 36), (26, 66), (102, 66)], ROOF1)
ct.poly([(64, 40), (29, 66), (99, 66)], ROOF2)
for yy in (47, 52, 57, 62):
    hh = yy - 36
    x0 = int(round(64 - hh * 38 / 30))
    x1 = int(round(64 + hh * 38 / 30))
    ct.rect(x0, yy, x1 - x0, 1, RIDGE)
ct.rect(44, 31, 21, 4, MOSSL)
ct.rect(53, 30, 10, 3, MOSSL)
MOSS = [MOSSD, MOSSL, MOSSDK]
for i in range(16):
    t = i / 15
    x = round(60 + (30 - 60) * t + random.randint(-2, 2))
    y = round(40 + (66 - 40) * t + random.randint(-1, 1))
    ct.ellipse(x, y, random.randint(2, 4), random.randint(1, 2), random.choice(MOSS))
for i in range(16):
    t = i / 15
    x = round(62 + (98 - 62) * t + random.randint(-2, 2))
    y = round(42 + (66 - 42) * t + random.randint(-1, 1))
    ct.ellipse(x, y, random.randint(2, 4), random.randint(1, 2), random.choice(MOSS))
for i in range(9):
    ct.set(50 + i * 3, 35, random.choice(MOSS))

# well
ct.poly([(20, 76), (4, 86), (36, 86)], STDK)
ct.poly([(20, 79), (7, 86), (33, 86)], STLT)
for i in range(8):
    t = i / 7
    x = round(20 + (4 - 20) * t + random.randint(-1, 1))
    y = round(77 + (86 - 77) * t + random.randint(-1, 1))
    ct.ellipse(x, y, random.randint(2, 3), 1, random.choice(MOSS))
for i in range(8):
    t = i / 7
    x = round(20 + (36 - 20) * t + random.randint(-1, 1))
    y = round(77 + (86 - 77) * t + random.randint(-1, 1))
    ct.ellipse(x, y, random.randint(2, 3), 1, random.choice(MOSS))
ct.rect(10, 90, 4, 18, PILL)
ct.rect(28, 90, 4, 18, PILL)
ct.rect(10, 88, 22, 3, RIM)
ct.rect(14, 93, 14, 4, BUCK)
ct.circle(11, 82, 3, WINCH)
ct.circle(11, 81, 2, WINCHL)
ct.ellipse(20, 110, 10, 4, STONE1)
ct.ellipse(20, 109, 9, 3, STONE2)
ct.ellipse(20, 107, 6, 2, WELLIN)
ct.rect(19, 93, 4, 4, WELLIN)

# light pools
ct.poly([(38, 98), (57, 98), (63, 118), (32, 118)], POOL1)
ct.poly([(40, 98), (55, 98), (59, 112), (36, 112)], POOL2)
ct.poly([(76, 98), (96, 98), (102, 118), (70, 118)], POOL1)
ct.poly([(78, 98), (93, 98), (97, 112), (74, 112)], POOL2)
ct.poly([(58, 99), (80, 99), (90, 122), (48, 122)], POOL3)
ct.poly([(60, 99), (78, 99), (84, 114), (54, 114)], POOL4)

# stone path
rows = [(102, 56, 80), (106, 52, 86), (111, 48, 92), (116, 44, 98), (121, 40, 104), (126, 36, 110)]
for (yy, xa, xb) in rows:
    n = max(2, (xb - xa) // 9)
    for i in range(n):
        x = round(xa + (xb - xa) * (i + 0.5) / n + random.randint(-2, 2))
        ct.ellipse(x, yy, 5, 3, random.choice([SLAB1, SLAB2, SLAB3]))
        ct.rect(x - 3, yy - 1, 3, 1, SLABH)
for x in range(30, 100, 5):
    ct.line(x, 128, x + 1, 128 - random.randint(3, 6), GR2)

# ---------------- TREES ----------------
tr = new_canvas(W, H)
spineL = [(0, 128, 10), (3, 112, 8), (5, 98, 7), (8, 86, 6), (10, 76, 5),
         (11, 68, 4), (12, 62, 3), (13, 57, 3)]
for (x, y, r) in spineL:
    tr.circle(x, y, r, TRUNK)
tr.ellipse(4, 124, 14, 7, TRUNK)
tr.line(2, 126, 10, 58, TRDK)
tr.line(6, 120, 12, 66, TRDK)
tr.line(7, 128, 11, 78, RIMT)
for (x, y, r) in [(11, 70, 3), (15, 60, 3), (20, 55, 2), (26, 52, 2), (30, 51, 2)]:
    tr.circle(x, y, r, TRUNK)
tr.line(26, 52, 33, 56, TRUNK)
tr.line(15, 60, 17, 54, BRCH)
for (x, y, r) in [(9, 84, 3), (4, 74, 2), (1, 66, 2)]:
    tr.circle(x, y, r, TRUNK)
for (x, y, r) in [(3, 108, 5), (1, 96, 4)]:
    tr.circle(x, y, r, TRUNK)

tr.ellipse(126, 124, 13, 7, TRUNK)
spineR = [(128, 128, 9), (126, 112, 8), (123, 98, 7), (121, 86, 6), (118, 76, 5),
         (116, 68, 4), (113, 61, 3)]
for (x, y, r) in spineR:
    tr.circle(x, y, r, TRUNK)
tr.line(118, 126, 112, 62, TRDK)
tr.line(122, 120, 115, 72, RIMT)
for (x, y, r) in [(114, 66, 3), (106, 58, 2), (98, 53, 2), (92, 51, 2)]:
    tr.circle(x, y, r, TRUNK)
tr.line(98, 53, 90, 48, BRCH)
tr.line(113, 60, 110, 52, BRCH)


def cluster(cx, cy, r, cols, n):
    for _ in range(n):
        a = random.uniform(0, 6.283)
        d = random.uniform(0, r)
        x = round(cx + math.cos(a) * d)
        y = round(cy + math.sin(a) * d)
        tr.circle(x, y, random.choice([2, 2, 3]), random.choice(cols))


LD = [LDA, LDB]
LM = [LMA, LMB]
LI = [LIA, LIB]
cluster(16, 30, 14, LD, 84)
cluster(120, 30, 13, LD, 70)
cluster(6, 42, 10, LD, 60)
cluster(110, 44, 10, LD, 52)
cluster(22, 26, 11, LM, 60)
cluster(114, 26, 10, LM, 55)
cluster(28, 36, 9, LM, 48)
cluster(106, 38, 9, LM, 50)
cluster(78, 46, 6, LM, 26)
cluster(96, 44, 6, LM, 24)
cluster(18, 22, 8, LI, 30)
cluster(116, 22, 8, LI, 30)
cluster(108, 34, 7, LI, 26)
cluster(38, 30, 6, LI, 18)
cluster(34, 44, 6, LM, 20)
cluster(88, 48, 5, LI, 16)
FG = [LIA, LIB, LMA, LMB]
for _ in range(30):
    tr.set(random.randint(28, 112), random.randint(110, 126), random.choice(FG))

# ---------------- COMPOSITE ----------------
result = flatten([bg, ct, tr], name="magic_forest_cottage")

# ---------------- MIST (solid bands, low colour cost) ----------------
def wavy_band(c, y0, amp, h, col):
    for x in range(W):
        y = y0 + int(amp * math.sin(x * 0.18 + random.uniform(0, 2)))
        result.rect(x, y, 1, random.randint(h - 1, h + 1), col)

wavy_band(result, 94, 2, 2, FOG1)
for x in range(W):
    y = 106 + int(2 * math.sin(x * 0.22))
    if 44 < x < 96 and random.random() < 0.5:
        continue
    result.rect(x, y, 1, random.randint(2, 4), FOG2)
for x in range(W):
    y = 116 + int(2 * math.sin(x * 0.3))
    result.rect(x, y, 1, random.randint(3, 6), FOG2)
result.rect(0, 124, W, 4, FOG3)
# soft fog patch near the well
result.rect(2, 100, 40, 2, FOG1)
result.rect(86, 102, 40, 2, FOG1)

# warm light glows cast onto the mist in front of the cottage
result.ellipse(60, 100, 22, 3, POOL2)
result.ellipse(82, 101, 18, 3, POOL2)
result.ellipse(70, 108, 26, 4, POOL3)
result.ellipse(66, 113, 18, 3, POOL4)
result.ellipse(56, 105, 9, 3, POOL4)
result.ellipse(88, 106, 9, 3, POOL4)

# keep a few bright path slabs visible through fog
for (yy, xa, xb) in [(111, 48, 92), (121, 40, 104)]:
    for i in range(3):
        x = xa + (xb - xa) * (i + 0.5) // 3
        result.ellipse(x, yy, 4, 2, SLAB1)
        result.rect(x - 2, yy - 1, 2, 1, SLABH)

# ---------------- FIREFLIES (solid) ----------------
for (x, y) in [(34, 94), (50, 106), (84, 100), (26, 86), (96, 98), (24, 116),
              (78, 116), (44, 120), (92, 122), (60, 108), (36, 98), (100, 110)]:
    result.set(x, y, FF1)
    result.set(x + 1, y, FF1)
for (x, y) in [(30, 114), (88, 118), (52, 108), (70, 114), (40, 120), (98, 116)]:
    result.set(x, y, FF2)
for (x, y) in [(40, 96), (90, 104), (58, 112)]:
    result.set(x, y, FF2)

print(result.stats_text())
print("colors used:", result.stats()["colors_used"])
finish(result)
