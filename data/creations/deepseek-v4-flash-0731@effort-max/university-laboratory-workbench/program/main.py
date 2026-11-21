from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# ---------------- palette ----------------
WALL  = "#e6ddc8"
PAPER = "#f4f0e2"
PLINE = "#ded6c0"
CLIP  = "#8a8a94"
CLK   = "#f0ead8"
INK   = "#3a3a44"
SHELF = "#a07048"
SEAM  = "#7d5330"
T_TOP = "#c8945c"
T_HI  = "#d9a96f"
FRONT = "#9c6a38"
PLANK = "#6d4526"
MIC_D = "#23232c"
MIC_M = "#43434f"
MIC_L = "#666675"
MIC_H = "#8f8fa0"
LENS  = "#3c6a9e"
SLIDE = "#cfe0f2"
KNOB  = "#2d2d38"
GL    = "#cfe0ee"
GD    = "#a9c0d6"
GH    = "#eef4fa"
RED  = "#d94f4f"
BLU  = "#4f7fd9"
GRN  = "#4f9e4f"
YEL  = "#e8c93d"
TEAL = "#3fa39e"
AMB  = "#d9a04f"
AMD  = "#bd8238"
CAPW = "#e8e4d8"
CAPG = "#b8b2a0"
CORK = "#a05a3a"
LAB  = "#f2efe4"
LL   = "#b0a888"
CV   = "#3f6f94"
CD   = "#31587a"
CH   = "#4f83a8"
PG   = "#f6f2e4"
CR   = "#d8cbb4"
PN   = "#d9b33d"
TP   = "#c98a6a"
ER   = "#d97a8a"
BL   = "#b8453a"
BD   = "#8f322b"

# ---------------- wall ----------------
c.rect(0, 0, 64, 64, WALL)

# clipboard (top-left)
c.rect(5, 3, 13, 8, PAPER)
c.rect(8, 2, 7, 2, CLIP)
c.rect(6, 5, 11, 1, PLINE)
c.rect(6, 7, 10, 1, PLINE)
c.rect(6, 9, 8, 1, PLINE)

# clock (top-centre)
c.circle(27, 7, 3, CLK)
c.line(27, 7, 27, 5, INK)
c.line(27, 7, 29, 7, INK)

# shelf with labeled bottles (top-right)
c.rect(38, 12, 24, 2, SHELF)
c.rect(38, 14, 24, 1, SEAM)

# bottle A (wide jar)
c.rect(41, 8, 6, 5, GL)          # body x41..46, y8..12
c.rect(42, 6, 5, 2, CAPW)         # cap
c.rect(42, 7, 5, 1, CAPG)
c.rect(46, 8, 1, 5, GD)           # right edge
c.rect(42, 10, 4, 3, AMB)         # amber liquid
c.rect(45, 10, 1, 3, AMD)
c.rect(42, 9, 4, 2, LAB)          # label
c.rect(43, 9, 2, 1, BLU)          # label stripe
c.rect(42, 9, 1, 1, CAPG)          # label tick

# bottle B (slender bottle)
c.rect(52, 7, 5, 5, GL)           # body x52..56, y7..11
c.rect(56, 7, 1, 5, GD)
c.rect(53, 5, 4, 2, GL)           # neck
c.rect(53, 3, 4, 2, CORK)         # cork cap
c.rect(53, 9, 3, 4, TEAL)         # teal liquid
c.rect(54, 8, 3, 2, LAB)          # label
c.rect(54, 8, 1, 1, INK)          # label tick

# ---------------- bench ----------------
c.rect(0, 46, 64, 3, T_TOP)        # worktop y46..48
c.rect(0, 46, 64, 1, T_HI)
c.rect(0, 49, 64, 15, FRONT)       # bench front y49..63
c.rect(0, 49, 64, 1, SEAM)
for x in range(8, 64, 8):
    c.rect(x, 50, 1, 13, PLANK)
c.rect(0, 58, 64, 1, PLANK)
c.circle(22, 57, 1, PLANK)          # drawer knobs
c.circle(40, 57, 1, PLANK)

# ---------------- microscope (left) ----------------
c.ellipse(13, 46, 9, 2, MIC_D)     # base x4..22, y44..48
c.ellipse(13, 46, 8, 1, MIC_M)
c.rect(15, 20, 4, 24, MIC_M)       # arm x15..18, y20..43
c.rect(15, 21, 1, 20, MIC_L)
c.rect(9, 15, 10, 6, MIC_D)        # head
c.rect(10, 16, 8, 4, MIC_M)
c.rect(10, 16, 8, 1, MIC_H)
c.rect(5, 11, 5, 2, MIC_D)         # eyepiece
c.rect(7, 13, 4, 3, MIC_D)
c.rect(4, 11, 2, 1, MIC_H)
c.rect(13, 21, 5, 9, MIC_L)        # body tube x13..17, y21..29
c.rect(17, 21, 1, 9, MIC_D)
c.rect(12, 29, 4, 4, MIC_M)        # objective
c.rect(11, 33, 3, 2, MIC_D)
c.rect(6, 36, 12, 2, MIC_L)        # stage
c.rect(6, 37, 12, 1, MIC_D)
c.rect(7, 35, 7, 1, SLIDE)         # specimen slide
c.circle(13, 35, 2, LENS)          # condenser lens
c.rect(12, 33, 3, 2, MIC_D)        # objective
c.circle(18, 39, 2, KNOB)          # focus knob

# ---------------- test-tube rack (centre) ----------------
for x0, lc in [(25, RED), (28, GRN), (31, YEL), (34, BLU)]:
    c.rect(x0, 28, 2, 14, GL)      # glass body y28..41
    c.rect(x0 - 1, 27, 4, 2, GL)   # rim
    c.rect(x0, 28, 2, 1, GH)
    c.rect(x0, 35, 2, 8, lc)       # liquid y35..42
    c.rect(x0, 35, 2, 1, GH)
c.rect(22, 30, 2, 15, SEAM)        # side rails
c.rect(36, 30, 2, 15, SEAM)
c.rect(24, 31, 12, 2, SHELF)       # top bar y31..32
c.rect(24, 42, 12, 4, SHELF)       # bottom bar y42..45
c.rect(27, 43, 10, 1, PLANK)       # slot strip

# ---------------- dropper (front) ----------------
c.circle(14, 47, 2, BL)              # rubber bulb x12..16, y45..49
c.rect(12, 48, 5, 1, BD)
c.rect(16, 46, 13, 2, GL)            # pipette tube x16..28
c.rect(16, 46, 13, 1, GH)

# ---------------- open notebook (right, front) ----------------
c.rect(40, 40, 22, 19, CV)         # cover x40..61, y40..58
c.rect(40, 40, 22, 1, CH)
c.rect(40, 58, 22, 1, CD)
c.rect(49, 41, 2, 17, CD)           # spine x49..50
c.rect(42, 42, 7, 14, PG)           # left page x42..48
c.rect(51, 42, 8, 14, PG)           # right page x51..58
c.rect(49, 42, 2, 14, CR)            # crease
c.rect(43, 44, 4, 1, LL)
c.rect(43, 47, 4, 1, LL)
c.rect(43, 50, 4, 1, LL)
c.rect(43, 53, 4, 1, LL)
c.rect(52, 44, 6, 1, LL)
c.rect(52, 47, 6, 1, LL)
c.rect(52, 50, 6, 1, LL)
c.rect(52, 53, 5, 1, LL)
c.rect(44, 45, 2, 1, INK)
c.rect(43, 48, 1, 1, INK)
c.rect(53, 46, 2, 1, INK)
c.rect(52, 43, 1, 1, RED)
c.rect(52, 51, 7, 2, PN)             # pencil
c.rect(59, 51, 2, 1, TP)
c.rect(51, 51, 1, 2, ER)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

finish(c)
