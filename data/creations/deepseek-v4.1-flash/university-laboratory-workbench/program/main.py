# =====================================================================
#  University laboratory workbench -- 64 x 64 pixel art
#  microscope, test-tube rack, dropper, labelled bottles, open notebook
# =====================================================================

c = new_canvas(64, 64, name="result")

# ----------------------------- palette -------------------------------
WALL_D  = "#232C38"
WALL    = "#2E3A4A"
WALL_L  = "#3A4A5E"
TILE    = "#4A5E74"
GROUT   = "#334154"

BENCH_BACK     = "#7A5530"
BENCH_TOP      = "#A87A4E"
BENCH_TOP_HI   = "#C89A6A"
BENCH_FRONT_HI = "#B08154"
BENCH_FRONT    = "#7E5632"
BENCH_FRONT_L  = "#8A6038"
BENCH_FRONT_D  = "#553818"
BENCH_EDGE     = "#3A2716"
SH1 = "#6B4A2A"
SH2 = "#8A6440"

MI_HI, MI, MI_D, MI_DD = "#64727F", "#44505C", "#303A45", "#212932"
CH_HI, CH, CH_D, CH_DD = "#F2F6FA", "#C4CFDA", "#8A99A8", "#5E6C7C"
BRASS, BRASS_D         = "#C9A24A", "#8A6B28"
GL_HI, GL, GL_D, GL_DD = "#EAF6FB", "#BCDFEC", "#84AEC0", "#54798C"

L_BLUE,  L_BLUE_D  = "#3FA3DE", "#2A6EA6"
L_GREEN, L_GREEN_D = "#57C46B", "#2F8A47"
L_RED,   L_RED_D   = "#E25B4C", "#A83A2E"
L_YEL,   L_YEL_D   = "#F0C244", "#B98A26"

WOOD_HI, WOOD, WOOD_D = "#8A5E38", "#6B4527", "#4A2F1A"

NB_COVER, NB_COVER_HI  = "#2F5C7E", "#43718F"
PAGE, PAGE_D, PAGE_DD  = "#F2EAD6", "#D8CDB0", "#B4A585"
INK, RULE              = "#5E6672", "#C3CBD2"

RUB_HI, RUB, RUB_D     = "#E58C76", "#C25A44", "#8E3A2C"

CAP_NAVY, CAP_NAVY_HI  = "#171D25", "#4E5A66"
AMBER, AMBER_D, AMBER_HI = "#C98A3A", "#8A5A22", "#E8B268"
LABEL, LABEL_D         = "#F3EEDD", "#D9D0B8"
RED_STRIPE, GRN_STRIPE = "#D94F4F", "#3E9D6B"


# ----------------------------- helpers -------------------------------
def H(x0, x1, y, col):
    c.rect(x0, y, x1 - x0 + 1, 1, col)


def V(x, y0, y1, col):
    c.rect(x, y0, 1, y1 - y0 + 1, col)


# =====================================================================
#  1. WALL  (y 0..41)
# =====================================================================
c.rect(0, 0, 64, 12, WALL_D)      # y 0..11  dark upper wall
c.rect(0, 12, 64, 16, WALL)       # y 12..27
c.rect(0, 28, 64, 6, WALL_L)      # y 28..33
c.dither(0, 11, 64, 1, [WALL_D, WALL], pattern="checker")
c.dither(0, 27, 64, 1, [WALL, WALL_L], pattern="checker")

# tiled back-splash just above the bench
c.rect(0, 34, 64, 8, TILE)        # y 34..41
for x in range(7, 64, 8):
    V(x, 34, 41, GROUT)
H(0, 63, 37, GROUT)

# ---- pendant lamp above the microscope ----
V(12, 0, 3, MI_DD)                 # flex
c.rect(11, 4, 3, 1, CH_DD)         # x 11..13
c.rect(10, 5, 5, 1, CH_DD)         # x 10..14
c.rect(9, 6, 7, 1, CH_DD)          # x 9..15
c.rect(8, 7, 9, 1, CH_DD)          # x 8..16
c.rect(7, 8, 11, 1, CH_D)          # x 7..17  rim
c.set(11, 4, CH_D)                 # highlight down the left slope
c.set(10, 5, CH_D)
c.set(9, 6, CH_D)
c.set(8, 7, CH_D)
c.set(7, 8, CH_HI)
c.rect(10, 8, 5, 1, L_YEL_D)       # glowing inner rim   x 10..14
c.rect(11, 9, 3, 1, L_YEL_D)       # bulb                x 11..13
c.set(12, 9, L_YEL)

# ---- wall clock ----
c.set(34, 2, CH_D)                 # hanging pin
c.circle(34, 7, 4, CH_D)           # bezel
c.circle(34, 7, 3, PAGE_D)         # dial
c.set(32, 5, PAGE)                 # glass glint
c.line(34, 7, 34, 5, INK)          # minute hand
c.line(34, 7, 36, 8, INK)          # hour hand
c.set(34, 7, CH_DD)                # spindle

# =====================================================================
#  2. BENCH TOP  (y 42..53)
# =====================================================================
c.rect(0, 42, 64, 12, BENCH_TOP)      # y 42..53
c.rect(0, 42, 64, 2, BENCH_BACK)      # far edge (in shade)
c.rect(0, 50, 64, 4, BENCH_TOP_HI)    # near edge (catching light)
# wood grain
H(6, 20, 46, BENCH_TOP_HI)
H(31, 47, 45, BENCH_TOP_HI)
H(49, 60, 48, BENCH_TOP_HI)
H(14, 32, 51, BENCH_TOP)
H(40, 56, 52, BENCH_TOP)

# =====================================================================
#  3. BENCH FRONT + DRAWER  (y 54..63)
# =====================================================================
DRAWER = "#96683C"
c.rect(0, 54, 64, 10, BENCH_FRONT)
H(0, 63, 54, BENCH_FRONT_HI)
H(0, 63, 55, BENCH_EDGE)
H(0, 63, 63, BENCH_FRONT_D)
# two drawer fronts
for x0 in (5, 34):
    c.rect(x0, 57, 25, 6, DRAWER)
    H(x0, x0 + 24, 57, BENCH_FRONT_D)      # shadow under the top rail
    H(x0, x0 + 24, 62, BENCH_FRONT_D)      # shadow above the bottom rail
    V(x0, 57, 62, BENCH_EDGE)              # side groove
    V(x0 + 24, 57, 62, BENCH_EDGE)
    c.rect(x0 + 9, 59, 7, 1, CH)           # chrome pull
    c.rect(x0 + 9, 60, 7, 1, CH_D)

# =====================================================================
#  4. CONTACT SHADOWS on the bench top (y 45..46)
# =====================================================================
c.rect(4, 45, 17, 1, SH1)
c.rect(7, 46, 11, 1, SH2)
c.rect(22, 45, 7, 1, SH1)
c.rect(30, 45, 7, 1, SH1)
c.rect(37, 45, 22, 1, SH1)
c.rect(40, 46, 16, 1, SH2)

# =====================================================================
#  5. MICROSCOPE  (x 2..20, y 14..44)
# =====================================================================
# heavy base -- three stepped top faces, then a front face
c.rect(8, 40, 12, 1, MI)          # x 8..19
c.rect(5, 41, 15, 1, MI)          # x 5..19
c.rect(3, 42, 18, 1, MI)          # x 3..20
c.rect(3, 43, 18, 1, MI_D)
c.rect(3, 44, 18, 1, MI_DD)
H(8, 11, 40, MI_HI)
H(5, 8, 41, MI_HI)
H(3, 7, 42, MI_HI)

# pillar / limb
c.rect(14, 30, 5, 12, MI)         # x 14..18, y 30..41
V(14, 30, 41, MI_HI)
V(18, 30, 41, MI_D)

# horizontal arm block joining pillar to the body tube
c.rect(11, 24, 8, 7, MI)          # x 11..18, y 24..30
H(11, 18, 24, MI_HI)
V(18, 24, 30, MI_D)

# coarse-focus knob on the pillar
c.circle(16, 33, 2, MI_D)
c.circle(16, 33, 1, CH_D)
c.set(15, 32, CH_HI)

# eyepiece
c.rect(5, 14, 7, 1, MI_DD)        # x 5..11
c.rect(5, 15, 7, 1, MI_D)
c.set(6, 15, MI_HI)
c.rect(6, 16, 5, 1, CH_D)         # x 6..10

# chrome body tube (y 17..30)
for y in range(17, 31):
    c.set(6, y, CH_HI)
    c.set(7, y, CH)
    c.set(8, y, CH)
    c.set(9, y, CH_D)
    c.set(10, y, CH_DD)

# brass collar
c.rect(6, 21, 5, 2, BRASS)
c.rect(9, 21, 2, 2, BRASS_D)

# nose-piece + objective
c.rect(6, 31, 5, 2, MI_D)
H(6, 10, 31, MI)
c.rect(7, 33, 2, 2, MI_D)
V(7, 33, 34, MI)
c.set(8, 34, CH)                  # lens

# mechanical stage
c.rect(2, 36, 13, 2, MI)          # x 2..14, y 36..37
H(2, 14, 36, MI_HI)
H(2, 14, 37, MI_D)

# glass slide on the stage + spring clips
c.rect(6, 35, 6, 1, GL)           # x 6..11
c.set(9, 35, GL_HI)
c.set(5, 35, MI_D)
c.set(12, 35, MI_D)

# sub-stage mirror
c.rect(6, 38, 6, 2, GL_D)         # x 6..11
H(6, 10, 38, GL_HI)

# =====================================================================
#  6. LABELLED BOTTLES  (x 22..28 and 30..36)
# =====================================================================
# ---- bottle A : tall clear bottle, blue reagent, white label ----
c.rect(23, 24, 5, 3, CAP_NAVY)    # screw cap
V(23, 24, 26, CAP_NAVY_HI)
c.rect(24, 27, 3, 2, GL)          # neck
V(24, 27, 28, GL_HI)
c.rect(23, 29, 5, 1, GL)          # shoulder
c.rect(22, 30, 7, 1, GL)
for y in range(31, 45):           # body
    c.set(22, y, GL_HI)
    c.set(23, y, L_BLUE)
    c.set(24, y, L_BLUE)
    c.set(25, y, L_BLUE)
    c.set(26, y, L_BLUE_D)
    c.set(27, y, GL_D)
    c.set(28, y, GL_DD)
# label
c.rect(22, 34, 7, 7, LABEL)       # x 22..28, y 34..40
V(22, 34, 40, LABEL_D)
V(28, 34, 40, LABEL_D)
c.rect(23, 35, 5, 1, RED_STRIPE)
c.rect(24, 37, 3, 1, INK)
c.rect(24, 39, 2, 1, INK)

# ---- bottle B : short amber bottle, green-striped label ----
c.rect(31, 29, 5, 3, AMBER_D)     # cap
V(31, 29, 31, AMBER)
c.rect(32, 32, 3, 2, AMBER)       # neck
c.rect(31, 34, 5, 1, AMBER)       # shoulder
c.rect(30, 35, 7, 1, AMBER)
for y in range(36, 45):           # body
    c.set(30, y, AMBER_HI)
    c.set(31, y, AMBER)
    c.set(32, y, AMBER)
    c.set(33, y, AMBER)
    c.set(34, y, AMBER)
    c.set(35, y, AMBER_D)
    c.set(36, y, AMBER_D)
# label
c.rect(30, 37, 7, 6, LABEL)       # x 30..36, y 37..42
V(30, 37, 42, LABEL_D)
V(36, 37, 42, LABEL_D)
c.rect(31, 38, 5, 1, GRN_STRIPE)
c.rect(32, 40, 3, 1, INK)
c.rect(32, 41, 2, 1, INK)

# =====================================================================
#  7. TEST-TUBE RACK  (x 38..58)
# =====================================================================
# end posts
c.rect(39, 34, 2, 7, WOOD)        # x 39..40
c.rect(56, 34, 2, 7, WOOD)        # x 56..57
V(39, 34, 40, WOOD_HI)
V(56, 34, 40, WOOD_HI)
# upper rail
c.rect(39, 32, 19, 3, WOOD)       # x 39..57, y 32..34
H(39, 57, 32, WOOD_HI)
H(39, 57, 34, WOOD_D)


def test_tube(x0, top, ltop, liq, liqd):
    c.set(x0, top, GL_HI)
    c.set(x0 + 1, top, GL_HI)
    c.set(x0 + 2, top, GL_D)
    for y in range(top + 1, 44):
        c.set(x0, y, GL_HI)
        if y < ltop:
            c.set(x0 + 1, y, GL)
            c.set(x0 + 2, y, GL_D)
        else:
            c.set(x0 + 1, y, liq)
            c.set(x0 + 2, y, liqd)


test_tube(41, 21, 28, L_BLUE,  L_BLUE_D)
test_tube(45, 21, 25, L_GREEN, L_GREEN_D)
test_tube(49, 21, 31, L_RED,   L_RED_D)
test_tube(53, 21, 23, L_YEL,   L_YEL_D)

# base block (hides the tube feet)
H(38, 58, 41, WOOD_HI)
c.rect(38, 42, 21, 2, WOOD)
H(38, 58, 44, WOOD_D)

# =====================================================================
#  8. DROPPER lying on the bench (x 39..54, y 46..50)
# =====================================================================
c.rect(40, 46, 3, 1, RUB)
c.rect(39, 47, 5, 3, RUB)
c.rect(40, 50, 3, 1, RUB)
V(42, 47, 50, RUB_D)
H(40, 42, 50, RUB_D)
c.set(40, 47, RUB_HI)
c.set(40, 48, RUB_HI)
c.set(41, 46, RUB_HI)
# collar + glass tube + tapered tip
c.rect(44, 47, 1, 3, CH_D)
c.rect(44, 48, 9, 1, GL_HI)       # x 44..52
c.rect(44, 49, 9, 1, GL_D)
c.set(53, 48, GL_HI)
c.set(54, 48, GL_D)
# soft shadow
H(39, 54, 51, SH2)

# =====================================================================
#  9. OPEN LAB NOTEBOOK lying on the bench (x 4..36, y 45..52)
# =====================================================================
book_rows = [(45, 12, 28), (46, 11, 29), (47, 10, 30), (48, 9, 31),
             (49, 8, 32), (50, 7, 33), (51, 6, 34), (52, 5, 35)]

for (y, x0, x1) in book_rows:                      # cover
    c.rect(x0, y, x1 - x0 + 1, 1, NB_COVER)
H(12, 28, 45, NB_COVER_HI)                         # top cover highlight

for (y, x0, x1) in book_rows[1:]:                  # pages inside cover
    c.rect(x0 + 2, y, x1 - x0 - 3, 1, PAGE)
    c.set(x0 + 2, y, PAGE_D)
    c.set(x1 - 2, y, PAGE_D)

for y in range(46, 53):                            # fold / spine
    c.set(19, y, PAGE_D)
    c.set(20, y, PAGE_DD)
    c.set(21, y, PAGE_D)

# ruled lines
H(13, 18, 47, RULE)
H(22, 27, 47, RULE)
H(11, 18, 49, RULE)
H(22, 29, 49, RULE)
H(9, 18, 51, RULE)
H(22, 31, 51, RULE)
# writing above the rules
H(14, 17, 46, INK)
H(23, 25, 46, INK)
H(12, 16, 48, INK)
H(23, 26, 48, INK)
H(10, 12, 50, INK)
H(24, 25, 50, INK)

# shadow under the notebook
H(4, 36, 53, SH1)

# =====================================================================
# 10. WALL SHELF with a cylinder and a flask  (x 44..61, y 7..15)
# =====================================================================
c.rect(44, 14, 18, 1, WOOD_HI)
H(44, 61, 15, WOOD_D)
c.rect(46, 16, 2, 1, WOOD_D)
c.rect(58, 16, 2, 1, WOOD_D)

# graduated cylinder (x 46..49)
for y in range(6, 14):
    c.set(46, y, GL_HI)
    c.set(47, y, GL)
    c.set(48, y, GL)
    c.set(49, y, GL_D)
for y in range(9, 14):
    c.set(47, y, L_BLUE)
    c.set(48, y, L_BLUE_D)
c.rect(45, 6, 5, 1, GL_HI)          # flared rim

# conical flask (x 53..59)
c.rect(53, 12, 7, 2, GL)
c.rect(54, 11, 5, 1, GL)
c.rect(55, 10, 3, 1, GL)
c.rect(55, 8, 3, 2, GL)
c.rect(54, 7, 5, 1, GL_HI)          # rim
V(53, 12, 13, GL_HI)
c.set(54, 11, GL_HI)
c.set(55, 10, GL_HI)
V(55, 8, 9, GL_HI)
V(59, 12, 13, GL_D)
c.set(58, 11, GL_D)
c.set(57, 10, GL_D)
V(57, 8, 9, GL_D)
c.rect(54, 12, 5, 2, L_GREEN)       # reagent
c.rect(55, 11, 3, 1, L_GREEN)
c.set(56, 11, L_GREEN_D)

# =====================================================================
GRP = {}
def grp(key, cols):
    for col in cols:
        GRP[c.color(col)] = key

grp('.', [WALL_D, WALL, WALL_L, TILE, GROUT, BENCH_BACK, BENCH_TOP, BENCH_TOP_HI,
          BENCH_FRONT_HI, BENCH_FRONT, BENCH_FRONT_L, BENCH_FRONT_D, BENCH_EDGE,
          SH1, SH2])
grp('M', [MI_HI, MI, MI_D, MI_DD, BRASS, BRASS_D])
grp('C', [CH_HI, CH, CH_D, CH_DD])
grp('G', [GL_HI, GL, GL_D, GL_DD])
grp('L', [L_BLUE, L_BLUE_D, L_GREEN, L_GREEN_D, L_RED, L_RED_D, L_YEL, L_YEL_D])
grp('W', [WOOD_HI, WOOD, WOOD_D])
grp('P', [NB_COVER, NB_COVER_HI, PAGE, PAGE_D, PAGE_DD, INK, RULE])
grp('R', [RUB_HI, RUB, RUB_D])
grp('A', [AMBER, AMBER_D, AMBER_HI])
grp('N', [CAP_NAVY, CAP_NAVY_HI])
grp('l', [LABEL, LABEL_D])

lines = []
for y in range(64):
    row = ""
    for x in range(64):
        row += GRP.get(c.get(x, y), '?')
    lines.append("%02d|%s|" % (y, row))
print("   " + "".join(str(x % 10) for x in range(64)))
print("\n".join(lines))

save("lab_bench", c)
print(c.stats_text())
finish(c)
