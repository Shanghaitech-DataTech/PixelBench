from pixelbench_api import *

c = new_canvas(256, 256, background=None, name="hero")

# ---- Core palette ----
O  = c.color((4, 7, 14))           # outline black
RD = c.color((22, 29, 44))         # robe dark
RM = c.color((36, 47, 68))         # robe mid
RL = c.color((58, 76, 104))        # robe light
HT = c.color((90, 68, 36))         # hat main
HD = c.color((55, 40, 20))         # hat dark
HL = c.color((125, 96, 54))        # hat light
HR = c.color((72, 54, 28))         # hat rim
SK = c.color((210, 172, 144))      # skin
SS = c.color((158, 124, 98))       # skin shadow
SD = c.color((114, 86, 66))        # deep skin shadow
SWB = c.color((192, 202, 222))     # sword bright (steel)
SWD = c.color((126, 136, 162))     # sword dark steel
SWG = c.color((172, 130, 60))     # sword gold
SA  = c.color((156, 60, 48))      # sash red
SAL = c.color((198, 92, 74))      # sash light
SAD = c.color((106, 40, 34))      # sash dark
HA  = c.color((14, 20, 28))       # hair black
HAH = c.color((34, 42, 56))       # hair highlight

# Background
MF  = c.color((80, 96, 126))      # mountain far
MN  = c.color((58, 71, 98))       # mountain near
MI  = c.color((140, 155, 180))    # mist
MIL = c.color((118, 133, 158))    # mist light
GC  = c.color((42, 52, 44))       # ground
GD  = c.color((26, 34, 27))       # ground dark
GL  = c.color((58, 68, 58))       # ground light

# ============ BACKGROUND ============
# Sky: pale misty blue gradient
for y in range(110):
    t = y / 110.0
    r = 174 - int(t * 40)
    g = 189 - int(t * 44)
    b = 209 - int(t * 45)
    c.rect(0, y, 256, 1, c.color((r, g, b)))

# Far mountains (two layers)
c.poly([(0, 70), (14, 36), (30, 58), (48, 28), (66, 52), (84, 26), (102, 48),
       (120, 34), (140, 56), (158, 30), (178, 52), (198, 32), (218, 56), (240, 40), (256, 54), (256, 72), (0, 72)], MF)

c.poly([(0, 115), (20, 76), (40, 100), (62, 78), (88, 112), (112, 84), (138, 108),
       (164, 86), (192, 112), (220, 90), (256, 110), (256, 118), (0, 118)], MN)

# Mist bands
for x in range(0, 256, 2):
    for y in range(58, 78, 2):
        if (x*3 + y*7) % 14 == 0:
            c.set(x, y, MIL)
    for y in range(100, 118, 2):
        if (x*5 + y) % 16 == 0:
            c.set(x, y, MIL)

# Ground with texture
import random
random.seed(42)
for y in range(120, 256):
    c.rect(0, y, 256, 1, GC)
for i in range(450):
    x = random.randint(0, 255)
    y = random.randint(120, 255)
    v = random.randint(0, 100)
    if v < 32: c.set(x, y, GD)
    elif v < 60: c.set(x, y, GL)

# ============ THREE-QUARTER FULL-BODY SWORDSMAN ============
# Layout:
# - Wide douli hat at top, y~20-90
# - Face below hat, y~85-113
# - Robe body y~112-250
# - Sword held at right side
# - Figure centered, x~55-200

# =========== DOULI HAT (wide conical, tilted down) ===========
hcx = 122
htop = 24

# Hat outer brim shape (wide ellipse)
# First draw the hat as an inverted cone
for row in range(66):
    t = row / 66.0
    half_w = int(38 * (0.25 + 0.75 * t))
    col = HL if t < 0.15 else (HT if t < 0.68 else HD)
    cx_shift = int(t * 4)
    c.line(hcx - half_w + cx_shift, htop + row, hcx + half_w + cx_shift, htop + row, col)

# Hat top tip
c.circle(hcx + 1, htop + 3, 5, HL)

# Wide brim flaring out wider
for row in range(52, 92):
    t = (row - 52) / 40.0
    hw = int(38 + t * 34)
    c.line(hcx - hw, htop + row, hcx + hw + 4, htop + row, HD)

# Brim outer edge
c.ellipse(hcx + 2, htop + 88, 72, 14, O, fill=False)

# Hat weave rings (radial lines on dome)
for row in range(6, 62, 7):
    t = row / 62.0
    half_w = int(38 * (0.25 + 0.75 * t))
    cx_shift = int(t * 4)
    c.line(hcx - half_w + cx_shift, htop + row, hcx + half_w + cx_shift, htop + row, HR)

# Hat chinstrap hint at brim edge
c.line(hcx + 5, htop + 88, hcx + 5, htop + 108, HD)
c.line(hcx + 5, htop + 106, hcx + 18, htop + 112, HD)

# =========== FACE below hat ===========
fxx = 128
# Face: narrow jaw with skin tones
for y in range(88, 114):
    t = (y - 88) / 26.0
    half_w = int(19 - t * 7)
    col = SD if t < 0.2 else (SK if t < 0.65 else SS)
    c.line(fxx - half_w, y, fxx + half_w + 5, y, col)

# Shadow under hat brim
for y in range(88, 96):
    c.line(fxx - 19 + int((y - 88) * 0.3), y, fxx + 24 - int((y - 88) * 0.3), y, SD)

# Chin
for y in range(108, 115):
    half_w = int(11 - (y - 108) * 1.5)
    if half_w > 1:
        c.line(fxx - half_w + 1, y, fxx + half_w + 4, y, SS)

# Face outline
c.line(fxx - 17, 88, fxx - 9, 113, O)
c.line(fxx + 23, 88, fxx + 15, 113, O)
c.line(fxx - 9, 112, fxx + 15, 112, O)

# Eyes barely visible under hat
c.set(fxx + 10, 90, O)
c.set(fxx + 15, 90, O)
c.set(fxx + 9, 88, SD)
c.set(fxx + 14, 88, SD)

# Nose
c.line(fxx + 2, 95, fxx + 3, 100, SS)
c.line(fxx + 2, 99, fxx + 7, 99, SS)

# Mouth
c.line(fxx + 1, 105, fxx + 9, 105, O)

# =========== NECK ===========
for y in range(112, 124):
    c.line(fxx - 7, y, fxx + 10, y, SS)
c.line(fxx - 7, 112, fxx - 6, 124, O)
c.line(fxx + 10, 112, fxx + 9, 124, O)

# =========== HAIR flowing loose ===========
# Hair cascades down behind the figure
for y in range(88, 215):
    t = (y - 88) / 127.0
    hl = int(24 + t * 24)
    hr = int(25 + t * 26)
    shift = int(t * 20)
    c.line(60 - hl + shift, y, 192 + hr + shift, y, HA)

# Hair highlights
for y in range(94, 210, 4):
    t = (y - 94) / 116.0
    c.line(int(72 + t * 20), y, int(88 + t * 28), y, HAH)

# =========== ROBE: long flowing dark robe ===========
bcx = 127

# Body: shoulders + flowing robe down to bottom
for y in range(118, 250):
    t = (y - 118) / 132.0
    # shoulder to body to flair
    if t < 0.1:
        hw = 52 + int(t * 28)
    elif t < 0.4:
        hw = 57 + int(t * 8)
    elif t < 0.75:
        hw = 65
    else:
        hw = 65 + int((t - 0.75) * 60)
    c.line(bcx - hw + 5, y, bcx + hw + 8, y, RD)

# Robe bottom hem detail (flowing, asymmetric)
c.poly([(62, 230), (48, 248), (56, 242), (46, 252), (66, 249), (82, 253), (76, 242),
        (96, 252), (110, 246), (128, 253), (144, 246), (162, 253), (176, 247),
        (196, 253), (204, 248), (214, 253), (200, 238)], RD)

# =========== RED SASH ===========
# Sash wrapping around, with flowing tails
for y in range(144, 166):
    t = (y - 144) / 22.0
    lx = int(74 + t * 16)
    rx = int(176 - t * 17)
    c.line(lx, y, rx, y + 8, SA)

# Knot at the side 
c.circle(166, 150, 12, SA)

# Sash trailing ribbon
c.poly([(162, 152), (174, 170), (182, 194), (196, 220), (186, 202), (174, 174), (158, 154)], SA)

# Sash highlighting
for y in range(146, 162, 3):
    c.line(112, y, 135, y, SAL)

# Second sash swap
for y in range(158, 174):
    t = (y - 158) / 16.0
    c.line(int(120 - t * 15), y, int(188 + t * 6), y + 6, SA)

# =========== SWORD (Jian) held vertical ===========
# Sword on right side, hand resting on it
sx = 182
blade_bot = 228

# Blade (long straight steel)
for y in range(94, blade_bot):
    c.set(sx, y, SWB)
    c.set(sx + 1, y, SWD)
    c.set(sx + 2, y, SWB)

# Blade lines for edge effect
for y in range(94, blade_bot, 2):
    c.set(sx + 3, y, SWD)
    c.set(sx - 1, y, SWD)

# Blade tip at top
for y in range(88, 94):
    t = (y - 88) / 6.0
    hw = max(0, int(2.5 - t * 2))
    for xx in range(sx, sx + hw):
        c.set(xx, y, SWB)

# Guard (cross-guard)
for x in range(sx - 16, sx + 19):
    c.set(x, 94, O)
    c.set(x, 95, SWG)

# Handle above guard
for y in range(80, 93):
    for xx in range(sx, sx + 3):
        c.set(xx, y, SWD)

# Pommel (ornate end)
c.circle(sx + 1, 78, 3, SWG)
c.circle(sx + 1, 75, 2, SWG)
c.circle(sx + 1, 73, 1, SWB)

# Hand gripping the sword
for y in range(112, 126):
    c.line(sx - 7, y, sx + 9, y, SK)
c.line(sx - 7, 112, sx - 7, 126, O)
c.line(sx + 9, 112, sx + 9, 126, O)

# Fingers
for y in range(114, 124, 2):
    c.set(sx + 10, y, SS)
    c.set(sx + 10, y + 1, SS)

# =========== SLEEVE over sword arm ===========
c.poly([(150, 116), (175, 110), (192, 138), (186, 164), (172, 150), (158, 130)], RM)

# =========== LEFT SIDE ARM ===========
for y in range(118, 178):
    t = (y - 118) / 60.0
    c.line(int(70 + t * 8), y, int(88 - t * 5), y + 3, RM)

# =========== ROBE FOLDS & details ===========
folds = [(82, 202), (97, 220), (113, 210), (130, 222), (146, 214), (164, 224)]
for fx, fy in folds:
    for y in range(122, fy):
        t = (y - 122) / max(1, fy - 122)
        px = int(fx + t * (fy - fx) * 0.35)
        if (fx * 17 + y * 5) % 3 == 0:
            c.set(px, y, RM)

# Shoulder highlights
for y in range(118, 130):
    c.line(100, y, 112, y, RL)

# Chest highlight
for y in range(132, 150, 2):
    c.line(106, y, 118, y, RM)

# =========== COLLAR / neckline ===========
for y in range(118, 144):
    t = (y - 118) / 26.0
    c.line(int(104 + t * 24), y, int(122 + t * 34), y, RM)

# =========== FIGURE OUTLINES ===========
# Full body outer silhouette
points_l = [(76, 118), (60, 148), (50, 186), (44, 218), (48, 250), (55, 255)]
for i in range(len(points_l) - 1):
    c.line(points_l[i][0], points_l[i][1], points_l[i+1][0], points_l[i+1][1], O)

points_r = [(186, 114), (200, 148), (208, 184), (212, 218), (208, 250), (216, 255)]
for i in range(len(points_r) - 1):
    c.line(points_r[i][0], points_r[i][1], points_r[i+1][0], points_r[i+1][1], O)

# Shoulder cape/fold
c.line(80, 122, 102, 117, RL)
c.line(152, 116, 176, 112, RL)

# =========== GROUND SHADOW ===========
c.ellipse(128, 252, 72, 10, GD)

# =========== Final touches ===========
# Mist curling around figure's feet
for x in range(0, 256, 2):
    for y in range(210, 250):
        if (x * 7 + y * 3) % 35 == 0:
            c.set(x, y, MIL)

# Small rock details near figure base
c.poly([(40, 200), (48, 188), (55, 196), (48, 210)], MN)
c.poly([(200, 205), (210, 194), (218, 202), (212, 215)], MN)

print(c.stats_text())
finish(c)
