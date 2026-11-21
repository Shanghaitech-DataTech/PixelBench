from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# ---------------- palette ----------------
WALL   = (226, 222, 214)
GROUT  = (204, 200, 192)
EDGE   = (140, 102, 64)
TOP    = (178, 134, 92)
LIP    = (158, 118, 76)
FRONT  = (118, 84, 52)
GRAIN  = (140, 100, 60)
SHADE  = (92, 62, 38)

BODY   = (46, 52, 66)     # microscope metal
DARK   = (28, 32, 42)
LITE   = (96, 104, 124)
METAL  = (172, 180, 198)
GLINT  = (140, 200, 235)

GLASS  = (185, 205, 220)
GD     = (150, 170, 185)
LABEL  = (242, 240, 234)
TXT    = (70, 80, 110)
BLAU   = (56, 120, 225)
GRN    = (70, 180, 95)
CAPA   = (70, 120, 180)
CAPAH  = (120, 170, 220)
CAPB   = (205, 140, 60)
RW     = (166, 120, 78)
TG     = (200, 215, 225)
TGH    = (218, 230, 240)
OR     = (228, 150, 40)
BEAK   = (190, 215, 230)
LIQY   = (235, 205, 90)
STEMC  = (170, 190, 205)
BULB   = (175, 65, 55)
BULBH  = (205, 130, 110)
COV    = (52, 92, 150)
PG     = (248, 246, 240)
SP     = (186, 192, 204)
RULE   = (205, 210, 220)
INK    = (40, 50, 90)

# ---------------- room ----------------
c.rect(0, 0, 64, 64, WALL)
for gx in (15, 31, 47):
    c.rect(gx, 0, 1, 44, GROUT)

c.rect(0, 43, 64, 1, EDGE)
c.rect(0, 44, 64, 3, TOP)
c.rect(0, 47, 64, 1, LIP)
c.rect(0, 48, 64, 15, FRONT)
c.rect(0, 63, 64, 1, SHADE)
for gx in (9, 22, 36, 52):
    c.rect(gx, 49, 1, 12, GRAIN)

# ---------------- microscope ----------------
c.rect(3, 42, 18, 5, BODY)          # base   3..20, 42..46
c.rect(3, 42, 18, 1, LITE)
c.rect(3, 45, 18, 1, DARK)
c.rect(8, 12, 9, 4, BODY)           # arm bridge  8..16, 12..15
c.rect(7, 12, 5, 31, BODY)          # pillar     7..11, 12..42
c.rect(7, 13, 1, 29, LITE)
c.rect(13, 12, 5, 18, BODY)         # tube       13..17, 12..29
c.rect(13, 13, 1, 16, LITE)
c.rect(12, 8, 7, 4, BODY)           # eyepiece   12..18, 8..11
c.rect(13, 8, 5, 1, DARK)
c.rect(14, 29, 3, 3, BODY)          # objective  14..16, 29..31
c.rect(14, 31, 3, 1, DARK)
c.rect(9, 32, 10, 3, BODY)          # stage       9..18, 32..34
c.rect(10, 33, 8, 1, LITE)
c.rect(13, 35, 3, 3, DARK)          # condenser  13..15, 35..37
c.circle(14, 39, 2, METAL)           # mirror     12..16, 37..41
c.circle(8, 37, 2, METAL)            # focus knob  6..10, 35..39
c.circle(8, 37, 1, DARK)
c.set(12, 39, GLINT)
c.rect(14, 32, 3, 1, TGH)            # glass slide on stage
c.set(15, 32, BULB)                   # small specimen

# ---------------- labeled bottles ----------------
c.rect(22, 26, 8, 21, GLASS, fill=False)   # A body  22..29, 26..46
c.rect(24, 32, 4, 14, BLAU)                 # A liquid
c.rect(23, 34, 6, 8, LABEL)                  # A label
c.rect(24, 36, 4, 1, TXT)
c.rect(24, 38, 4, 1, TXT)
c.rect(25, 21, 3, 5, GLASS, fill=False)      # A neck 25..27, 21..25
c.rect(24, 18, 5, 4, CAPA)                    # A cap  24..28, 18..21
c.rect(24, 18, 5, 1, CAPAH)

c.rect(30, 31, 6, 16, GLASS, fill=False)    # B body  30..35, 31..46
c.rect(32, 35, 3, 11, GRN)                   # B liquid
c.rect(31, 37, 4, 5, LABEL)                   # B label
c.rect(32, 39, 2, 1, TXT)
c.rect(31, 27, 3, 4, GLASS, fill=False)      # B neck  31..33, 27..30
c.rect(30, 24, 5, 4, CAPB)                    # B cap   30..34, 24..27

# ---------------- test-tube rack ----------------
c.rect(36, 31, 2, 16, RW)
c.rect(44, 31, 2, 16, RW)
c.rect(36, 33, 10, 2, RW)
c.rect(36, 41, 10, 2, RW)

c.rect(38, 18, 3, 24, TG, fill=False)         # tube 1   38..40, 18..41
c.rect(38, 24, 3, 16, OR)
c.rect(38, 18, 3, 1, TGH)
c.rect(41, 18, 3, 24, TG, fill=False)         # tube 2   41..43, 18..41
c.rect(41, 28, 3, 12, BLAU)
c.rect(41, 18, 3, 1, TGH)

# ---------------- beaker with dropper ----------------
c.rect(46, 37, 8, 10, BEAK)                    # beaker  46..53, 37..46
c.rect(47, 40, 6, 6, LIQY)                     # liquid 47..52, 40..45
c.rect(46, 37, 8, 1, (214, 230, 240))
c.set(48, 41, BEAK)                             # bubbles in liquid
c.set(50, 42, BEAK)
c.set(51, 41, BEAK)
c.rect(49, 26, 2, 19, STEMC)                    # dropper stem 49..50, 26..44
c.rect(48, 21, 4, 5, BULB)                       # rubber bulb 48..51, 21..25
c.rect(48, 21, 4, 1, BULBH)

# ---------------- open notebook ----------------
c.rect(54, 38, 10, 9, COV)                      # cover 54..63, 38..46
c.rect(55, 39, 4, 7, PG)                          # left page  55..58, 39..45
c.rect(60, 39, 4, 7, PG)                          # right page 60..63, 39..45
c.rect(59, 39, 1, 7, SP)                           # spine
c.rect(56, 41, 3, 1, RULE)
c.rect(56, 43, 3, 1, RULE)
c.set(60, 44, INK)
c.set(61, 43, INK)
c.set(62, 42, INK)
c.set(62, 41, INK)
c.circle(62, 40, 1, INK, fill=False)

print(c.stats_text())

finish(c)
