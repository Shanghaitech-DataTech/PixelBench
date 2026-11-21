# offshore wind turbine maintenance platform - 64x64
import math

c = new_canvas(64, 64, name="output")

# ---------------- palette ----------------
SKY = ["#5fa9d8", "#72b5df", "#86c2e6", "#9ccfed", "#b2daf1", "#c8e4f5", "#dcf0fa"]
HAZE = "#c3dced"
CLOUD = "#f2f8fd"
CLOUD2 = "#dceaf5"

SEA = ["#3f7fa8", "#336a93", "#27557a", "#1d4466"]
SEA_HI = "#6fabcd"
SEA_DK = "#15314d"
FOAM = "#eff7fc"
FOAM2 = "#b6d6ea"

T_HI = "#e4e9ee"
T_LT = "#c6ccd4"
T_MD = "#9aa1ab"
T_SH = "#70777f"
T_LINE = "#565d66"

Y_HI = "#f6db57"
Y_LT = "#e9c63c"
Y_MD = "#c29c22"
Y_SH = "#8d7118"

STEEL_D = "#3b414a"
STEEL_DD = "#22262c"
STEEL_M = "#596169"
STEEL_L = "#7d858e"

ORANGE = "#ef7524"
ORANGE_D = "#bb4f16"
HELMET = "#fdfdf4"
GLOVE = "#2b3037"

FAR1 = "#eef4f9"
FAR1D = "#cbdbe8"
FAR2 = "#a9c3d6"

HORIZON = 42
CX = 38

# ---------------- sky ----------------
rows = [(0, 7), (7, 14), (14, 21), (21, 28), (28, 34), (34, 39), (39, 42)]
for (y0, y1), col in zip(rows, SKY):
    c.rect(0, y0, 64, y1 - y0, col)

# ---------------- clouds ----------------
c.ellipse(55, 7, 8, 1, CLOUD2)
c.ellipse(52, 6, 4, 1, CLOUD)
c.ellipse(59, 8, 4, 0, CLOUD)
c.ellipse(10, 12, 6, 1, CLOUD2)
c.ellipse(12, 11, 3, 0, CLOUD)
c.ellipse(14, 36, 8, 0, CLOUD2)

# ---------------- distant turbines ----------------
def far_turbine(cx, hub, r, col, shade, spin=0.0):
    c.rect(cx, hub + 1, 1, HORIZON - hub, col)
    c.set(cx, HORIZON - 1, shade)
    for k in range(3):
        a = math.radians(90 + spin + k * 120)
        ex = cx + r * math.cos(a)
        ey = hub - r * math.sin(a) * 0.95
        c.line(cx, hub, int(round(ex)), int(round(ey)), col)
    c.set(cx, hub, shade)
    c.set(cx - 1, hub, col)

far_turbine(9, 23, 7, FAR1, FAR1D, spin=20)
far_turbine(21, 30, 5, FAR2, FAR2, spin=-20)

# ---------------- ocean ----------------
c.rect(0, HORIZON, 64, 1, HAZE)
c.rect(0, 43, 64, 4, SEA[0])
c.rect(0, 47, 64, 5, SEA[1])
c.rect(0, 52, 64, 6, SEA[2])
c.rect(0, 58, 64, 6, SEA[3])
for x, y, w, a, b in [(0, 46, 13, SEA[0], SEA[1]), (20, 46, 17, SEA[0], SEA[1]),
                      (49, 46, 15, SEA[0], SEA[1]),
                      (3, 51, 19, SEA[1], SEA[2]), (33, 51, 25, SEA[1], SEA[2]),
                      (0, 57, 23, SEA[2], SEA[3]), (37, 57, 21, SEA[2], SEA[3])]:
    c.dither(x, y, w, 1, [a, b], pattern="checker")

crests = [
    (2, 44, 3), (11, 45, 2), (24, 44, 3), (52, 44, 3), (59, 45, 3),
    (4, 48, 4), (15, 49, 3), (25, 48, 4), (52, 49, 4), (59, 48, 3),
    (1, 53, 5), (11, 55, 4), (20, 54, 5), (52, 55, 5), (59, 53, 4),
    (3, 59, 8), (16, 61, 6), (27, 60, 7), (45, 61, 8), (56, 58, 5),
]
for x, y, w in crests:
    c.rect(x, y, w, 1, SEA_HI)
    c.rect(x + 1, y + 1, max(1, w - 2), 1, SEA_DK)
# rolling swells in the near water: a crest lip with a trough under it
swells = [(0, 57, 11), (14, 58, 9), (26, 57, 10), (42, 58, 10), (54, 57, 10)]
for x, y, w in swells:
    c.rect(x + 1, y, w - 2, 1, SEA_HI)
    c.set(x, y + 1, SEA_HI)
    c.set(x + w - 1, y + 1, SEA_HI)
    c.rect(x + 2, y + 1, w - 4, 1, SEA_DK)
for x, y, w in [(6, 58, 6), (31, 62, 9), (54, 57, 4), (19, 50, 4), (8, 62, 4)]:
    c.rect(x, y, w, 1, FOAM2)

# ---------------- main turbine tower ----------------
def tower_row(y):
    w = 9 + round(y * 5 / 33)
    return CX - w // 2, w

for y in range(0, 34):
    left, w = tower_row(y)
    for i in range(w):
        if i == 0:
            col = T_HI
        elif i < w * 0.40:
            col = T_LT
        elif i < w * 0.74:
            col = T_MD
        else:
            col = T_SH
        c.set(left + i, y, col)

for y in (11, 23):
    left, w = tower_row(y)
    c.rect(left, y, w, 1, T_LINE)
    c.set(left, y, T_MD)

# tower access door above the deck
c.rect(CX - 2, 28, 4, 6, STEEL_D)
c.rect(CX - 2, 28, 1, 6, STEEL_M)
c.set(CX + 1, 31, STEEL_L)

# ---------------- transition piece (yellow monopile top) ----------------
TP_L, TP_R, TP_TOP, TP_BOT = 29, 48, 37, 53
TPW = TP_R - TP_L + 1
for x in range(TP_L, TP_R + 1):
    i = x - TP_L
    if i == 0:
        col = Y_HI
    elif i < TPW * 0.40:
        col = Y_LT
    elif i < TPW * 0.74:
        col = Y_MD
    else:
        col = Y_SH
    c.rect(x, TP_TOP, 1, TP_BOT - TP_TOP + 1, col)

c.rect(TP_L, TP_TOP, TPW, 1, Y_SH)
c.rect(TP_L, TP_TOP + 1, TPW, 1, Y_MD)   # shadow cast by the deck overhang
c.rect(TP_L, 44, TPW, 1, Y_SH)
c.rect(TP_L, 45, TPW, 1, Y_HI)
# access hatch and a small cabinet on the yellow face
c.rect(31, 46, 2, 4, Y_SH)
c.rect(31, 46, 1, 4, Y_MD)
c.rect(45, 46, 2, 4, Y_SH)
c.rect(45, 46, 1, 4, Y_MD)

# boat-landing frame on the near face
c.rect(TP_L, 38, 1, 16, STEEL_D)
c.rect(TP_R, 38, 1, 16, STEEL_M)
c.rect(TP_L, 50, TPW, 1, STEEL_M)
c.rect(TP_L, 41, TPW, 1, STEEL_D)
c.line(TP_L + 1, 50, TP_L + 4, 41, STEEL_D)
c.line(TP_R - 1, 50, TP_R - 4, 41, STEEL_D)

# ---------------- platform deck, grating and railing ----------------
D_L, D_R = 25, 52
DW = D_R - D_L + 1
c.rect(D_L, 34, DW, 1, Y_HI)
c.dither(D_L, 35, DW, 1, [Y_MD, Y_SH], pattern="checker")
c.rect(D_L, 36, DW, 1, STEEL_D)
# cantilever brackets under the deck edge
c.line(26, 37, 30, 41, STEEL_D)
c.line(51, 37, 47, 41, STEEL_M)
c.line(27, 37, 31, 41, STEEL_M)
c.line(50, 37, 46, 41, STEEL_D)

# railing: posts, top rail, mid rail
for px in (25, 29, 33, 43, 47, 52):
    c.rect(px, 29, 1, 5, STEEL_D)
c.rect(D_L, 28, DW, 1, STEEL_M)
c.rect(D_L, 31, DW, 1, STEEL_D)
c.rect(D_L, 33, DW, 1, STEEL_M)

# deck crane on the left edge
c.rect(26, 23, 2, 11, STEEL_D)
c.rect(26, 23, 1, 11, STEEL_M)
c.line(27, 23, 33, 20, STEEL_M)
c.line(27, 24, 33, 21, STEEL_D)
c.rect(33, 21, 1, 5, STEEL_L)
c.set(33, 26, STEEL_D)

# ---------------- ladder on the boat landing ----------------
c.rect(34, 37, 8, 17, STEEL_D)          # shadowed recess behind the ladder
c.rect(34, 37, 1, 17, STEEL_DD)
c.rect(41, 37, 1, 17, STEEL_DD)
c.rect(34, 37, 8, 1, STEEL_DD)
LAD_L, LAD_R = 35, 40
c.rect(LAD_L, 38, 1, 16, STEEL_L)
c.rect(LAD_R, 38, 1, 16, STEEL_M)
for y in range(39, 54, 2):
    c.rect(LAD_L + 1, y, LAD_R - LAD_L - 1, 1, STEEL_M)
    c.set(LAD_L + 1, y, STEEL_L)

# ---------------- technician in safety gear, climbing ----------------
BX = 36   # body columns 36..39
# gloved hands gripping an upper rung
c.set(BX, 42, GLOVE)
c.set(BX + 3, 42, GLOVE)
# white hard hat
c.rect(BX + 1, 43, 2, 1, HELMET)
# arms up the stiles, shoulders in a hi-vis jacket
c.set(BX, 43, ORANGE_D)
c.set(BX + 3, 43, ORANGE_D)
c.rect(BX, 44, 4, 1, ORANGE)
c.set(BX, 44, ORANGE_D)
c.set(BX + 3, 44, ORANGE_D)
# torso: reflective band, then harness over the jacket
c.rect(BX + 1, 45, 2, 1, HELMET)
c.rect(BX, 46, 4, 1, ORANGE)
c.set(BX, 46, ORANGE_D)
c.set(BX + 3, 46, ORANGE_D)
# hips and legs, one knee raised to the next rung
c.rect(BX + 1, 47, 2, 1, STEEL_M)
c.set(BX, 47, ORANGE_D)
c.set(BX + 1, 48, STEEL_M)
c.set(BX + 2, 48, STEEL_L)
c.set(BX + 1, 49, GLOVE)
c.set(BX + 3, 49, GLOVE)
c.set(BX + 3, 48, STEEL_M)

# ---------------- wash and foam at the waterline ----------------
# dark shadow of the pile on the water, then a broken ring of foam
c.rect(29, 54, 20, 1, SEA_DK)
for x, y, w in [(28, 52, 7), (37, 52, 4), (43, 52, 6),
                (29, 53, 6), (36, 53, 5), (44, 53, 5)]:
    c.rect(x, y, w, 1, FOAM)
for x, y, w in [(25, 54, 4), (31, 55, 6), (40, 55, 5), (47, 54, 5),
                (27, 56, 4), (34, 57, 5), (43, 56, 4)]:
    c.rect(x, y, w, 1, FOAM2)
c.set(28, 53, FOAM2)
c.set(49, 53, FOAM2)
c.dither(28, 55, 8, 1, [FOAM2, SEA[2]], pattern="checker")
c.dither(41, 56, 8, 1, [FOAM2, SEA[2]], pattern="checker")

# navigation light on the deck corner, and gulls for scale
c.set(52, 27, Y_HI)
c.set(52, 28, STEEL_D)
for bx, by in [(57, 19), (61, 22)]:
    c.set(bx - 1, by, STEEL_M)
    c.set(bx, by - 1, STEEL_M)
    c.set(bx + 1, by, STEEL_M)

view(c)
print(c.stats_text())
result = c
finish(result)
