# =================================================================
# 64x64 pixel art - university laboratory workbench
# =================================================================

c = new_canvas(64, 64, background="#c3d2d8", name="lab-workbench")

# ----------------------------- palette -----------------------------
WALL     = c.color("#c3d2d8", "wall")
WALL_SH  = c.color("#aebfc7", "wall_shade")
PANE     = c.color("#e9f5f8", "window_glass")
PANE_SH  = c.color("#cfe4ea", "window_glass_shade")
FRAME    = c.color("#8fa3ad", "window_frame")
WOOD_L   = c.color("#c99a5f", "wood_light")
WOOD_M   = c.color("#a87b45", "wood_mid")
WOOD_D   = c.color("#7c5527", "wood_dark")
WOOD_DD  = c.color("#5c3d1c", "wood_dark_line")
WOOD_SH  = c.color("#8f6636", "wood_shadow")
MET_D    = c.color("#3f454d", "metal_dark")
MET_M    = c.color("#5c646e", "metal_mid")
MET_L    = c.color("#8b95a0", "metal_light")
INK      = c.color("#26292e", "ink")
WHITE    = c.color("#f4f6f7", "paper_white")
GREY     = c.color("#9aa4ac", "grey")
SPINE    = c.color("#c9d2d8", "rule_line")
GLASS    = c.color("#dceef2", "glass")
GLASS_SH = c.color("#b7d5de", "glass_shade")
GREEN    = c.color("#4fae62", "liquid_green")
BLUE     = c.color("#3f7fd0", "liquid_blue")
RED      = c.color("#cc4b4b", "liquid_red")
AMBER    = c.color("#d99a3a", "liquid_amber")
AMBER_L  = c.color("#e8b45f", "liquid_amber_light")
RUBBER   = c.color("#a83a3a", "rubber_bulb")
RUBBER_L = c.color("#c95c5c", "rubber_light")
COVER    = c.color("#3d4750", "notebook_cover")

# ----------------------------- wall --------------------------------
c.rect(0, 35, 64, 3, WALL_SH)          # shadow band above the bench

# window (right)
c.rect(44, 3, 19, 19, FRAME)           # frame  x44..62  y3..21
c.rect(45, 4, 17, 17, PANE)            # glass  x45..61  y4..20
for i in range(6):                     # reflection streak
    c.set(47 + i, 18 - i, PANE_SH)
    c.set(48 + i, 18 - i, PANE_SH)
c.rect(52, 4, 1, 17, FRAME)            # mullions
c.rect(45, 12, 17, 1, FRAME)
c.rect(43, 21, 21, 1, WOOD_L)          # sill
c.rect(43, 22, 21, 1, WOOD_M)

# periodic-table poster (left)
c.rect(2, 2, 17, 15, FRAME)            # frame  x2..18  y2..16
c.rect(3, 3, 15, 13, WHITE)            # board  x3..17  y3..15
cells = [
    (5, 4, GREEN), (9, 4, BLUE), (13, 4, AMBER),
    (5, 8, RED), (9, 8, MET_L), (13, 8, WALL_SH),
    (5, 12, BLUE), (9, 12, AMBER), (13, 12, GREEN),
]
for (x, y, col) in cells:
    c.rect(x, y, 3, 3, col)
for (x, y) in ((5, 4), (13, 4), (9, 8), (13, 12), (5, 12)):
    c.set(x + 1, y + 1, INK)           # hint of a symbol

# clipboard notice (lower left)
c.rect(2, 22, 7, 11, WOOD_M)           # board  x2..8  y22..32
c.rect(2, 22, 7, 1, WOOD_L)
c.rect(3, 21, 4, 2, MET_M)             # clip
c.rect(3, 24, 5, 8, WHITE)             # paper  x3..7  y24..31
c.rect(4, 25, 3, 1, GREY)
c.rect(4, 27, 4, 1, GREY)
c.rect(4, 29, 3, 1, GREY)

# wall shelf with small vessels (centre)
c.rect(21, 16, 20, 2, WOOD_M)          # shelf  x21..40  y16..17
c.rect(21, 16, 20, 1, WOOD_L)
c.set(22, 18, MET_D); c.set(22, 19, MET_D)
c.set(39, 18, MET_D); c.set(39, 19, MET_D)
c.rect(26, 12, 4, 4, GLASS)            # bottle
c.rect(29, 12, 1, 4, GLASS_SH)
c.rect(27, 14, 2, 2, GREEN)
c.rect(27, 10, 2, 2, GLASS)
c.rect(27, 9, 2, 1, MET_D)
c.rect(32, 12, 4, 4, GLASS)            # jar
c.rect(35, 12, 1, 4, GLASS_SH)
c.rect(33, 14, 2, 2, AMBER)
c.rect(32, 11, 4, 1, MET_D)
c.rect(38, 13, 3, 3, GLASS)            # vial
c.rect(40, 13, 1, 3, GLASS_SH)
c.rect(38, 12, 3, 1, MET_D)

# ----------------------------- bench -------------------------------
c.rect(0, 38, 64, 18, WOOD_L)          # top    y38..55
c.rect(0, 38, 64, 1, WOOD_M)           # back edge
c.rect(23, 39, 1, 17, WOOD_M)          # plank seams
c.rect(42, 39, 1, 17, WOOD_M)
c.rect(0, 56, 64, 1, WOOD_M)           # front edge of the top
c.rect(0, 57, 64, 1, WOOD_D)
c.rect(0, 58, 64, 6, WOOD_D)           # cabinet y58..63
c.rect(0, 61, 64, 1, WOOD_DD)          # drawer seam
c.rect(10, 59, 5, 1, MET_L)            # drawer handles
c.rect(38, 59, 5, 1, MET_L)
c.rect(10, 62, 5, 1, MET_L)
c.rect(38, 62, 5, 1, MET_L)
for x in (10, 14, 38, 42):
    c.set(x, 59, MET_D)
    c.set(x, 62, MET_D)

# --------------------------- microscope ----------------------------
c.rect(6, 43, 17, 1, WOOD_SH)          # contact shadow
c.rect(7, 39, 14, 1, MET_M)            # base bevel
c.rect(6, 40, 16, 3, MET_D)            # base   x6..21  y40..42
c.rect(8, 40, 12, 1, MET_L)            # machined edge
c.rect(10, 18, 5, 3, MET_D)            # eyepiece x10..14  y18..20
c.rect(11, 18, 3, 1, INK)              # eyecup
c.set(10, 19, MET_L)
c.line(12, 21, 15, 26, MET_L)          # eyepiece tube, 3 px band
c.line(13, 21, 16, 26, MET_M)
c.line(14, 21, 17, 26, MET_D)
c.rect(16, 25, 1, 15, MET_L)           # arm y25..39
c.rect(17, 25, 1, 15, MET_M)
c.rect(18, 25, 1, 15, MET_D)
c.rect(19, 32, 2, 3, MET_D)            # focus knob
c.set(19, 33, MET_L)
c.rect(8, 34, 11, 1, MET_M)            # stage x8..18
c.rect(8, 35, 11, 1, MET_D)
c.rect(10, 33, 8, 1, GLASS)            # slide
c.set(14, 33, BLUE); c.set(15, 33, BLUE)
c.rect(12, 27, 7, 2, MET_D)            # nosepiece x12..18
c.rect(13, 29, 1, 4, MET_L)            # long objective
c.set(13, 33, INK)
c.rect(16, 29, 1, 2, MET_L)            # short objective
c.set(16, 31, INK)
c.rect(11, 36, 5, 2, MET_M)            # condenser
c.rect(12, 36, 3, 1, MET_L)
c.rect(13, 38, 2, 1, MET_M)            # post to the base

# -------------------------- test-tube rack -------------------------
c.rect(24, 42, 17, 1, WOOD_SH)         # contact shadow
tubes = ((26, GREEN), (31, BLUE), (36, RED))
for (x, liq) in tubes:
    c.rect(x, 27, 3, 11, GLASS)        # tube y27..37
    c.rect(x + 2, 27, 1, 11, GLASS_SH)
    c.rect(x, 27, 3, 1, GLASS_SH)      # rim
    c.set(x + 1, 27, GLASS)            # opening
    c.rect(x, 33, 3, 5, liq)           # liquid
    c.set(x, 30, WHITE)                # highlight
for x in (24, 29, 34, 39):             # top plate between the tubes
    c.rect(x, 31, 2, 2, WOOD_M)
    c.rect(x, 31, 2, 1, WOOD_L)
c.rect(24, 38, 17, 4, WOOD_M)          # base y38..41
c.rect(24, 38, 17, 1, WOOD_L)

# ----------------------------- bottles -----------------------------
c.rect(44, 43, 15, 1, WOOD_SH)         # contact shadow
# tall reagent bottle
c.rect(44, 29, 7, 14, GLASS)           # body x44..50  y29..42
c.rect(44, 29, 1, 14, GLASS_SH)
c.rect(50, 29, 1, 14, GLASS_SH)
c.rect(45, 42, 5, 1, GLASS_SH)
c.rect(46, 25, 3, 4, GLASS)            # neck
c.set(48, 28, GLASS_SH)
c.rect(45, 23, 5, 2, MET_D)            # cap
c.set(45, 23, MET_L); c.set(49, 24, INK)
c.rect(45, 29, 5, 14, AMBER)           # liquid
c.rect(45, 29, 5, 1, AMBER_L)
c.rect(44, 32, 7, 7, WHITE)            # label
c.rect(45, 33, 5, 1, GREY)
c.rect(45, 35, 4, 1, GREY)
c.rect(45, 37, 3, 1, GREY)
# medium bottle
c.rect(53, 32, 6, 11, GLASS)           # body x53..58  y32..42
c.rect(53, 32, 1, 11, GLASS_SH)
c.rect(58, 32, 1, 11, GLASS_SH)
c.rect(54, 42, 4, 1, GLASS_SH)
c.rect(55, 29, 2, 3, GLASS)            # neck
c.set(56, 31, GLASS_SH)
c.rect(54, 27, 4, 2, MET_D)            # cap
c.rect(54, 36, 4, 7, BLUE)             # liquid
c.rect(53, 33, 6, 3, WHITE)            # label
c.rect(54, 34, 4, 1, GREY)
# small bottle in front
c.rect(50, 45, 5, 1, WOOD_SH)          # contact shadow
c.rect(50, 37, 5, 8, GLASS)            # body x50..54  y37..44
c.rect(50, 37, 1, 8, GLASS_SH)
c.rect(54, 37, 1, 8, GLASS_SH)
c.rect(51, 44, 3, 1, GLASS_SH)
c.rect(51, 36, 3, 1, GLASS)            # neck
c.rect(51, 34, 3, 2, MET_D)            # cap
c.rect(51, 41, 3, 4, RED)              # liquid
c.rect(50, 38, 5, 2, WHITE)            # label
c.set(51, 39, GREY); c.set(52, 39, GREY)

# ----------------------------- beaker ------------------------------
c.rect(2, 49, 6, 1, WOOD_SH)           # contact shadow
c.set(1, 43, GLASS)                    # spout
c.set(0, 44, GLASS)                    # spout lip
c.rect(2, 43, 6, 6, GLASS)             # body x2..7  y43..48
c.rect(2, 43, 6, 1, GLASS_SH)          # rim
c.rect(7, 44, 1, 5, GLASS_SH)          # right wall in shade
c.set(2, 44, WHITE)                    # left wall highlight
c.rect(3, 46, 4, 3, GREEN)             # liquid
c.rect(5, 45, 2, 1, GREY)              # graduation mark

# ------------------------ dropper (front right) --------------------
c.rect(45, 53, 14, 1, WOOD_SH)         # contact shadow
c.rect(45, 48, 5, 3, RUBBER)           # bulb x45..49  y48..50
c.set(46, 47, RUBBER); c.set(47, 47, RUBBER); c.set(48, 47, RUBBER)
c.set(46, 51, RUBBER); c.set(47, 51, RUBBER); c.set(48, 51, RUBBER)
c.set(46, 48, RUBBER_L)
c.rect(50, 48, 8, 2, GLASS)            # tube x50..57  y48..49
c.set(50, 49, GLASS_SH)
c.rect(53, 48, 5, 1, BLUE)             # liquid drawn up to the tip
c.set(58, 48, GLASS)                   # taper
c.set(58, 49, GLASS_SH)
c.set(59, 49, GLASS_SH)                # tip
c.set(59, 51, BLUE)                    # drop
c.set(59, 52, BLUE)

# ---------------------- open laboratory notebook -------------------
c.rect(13, 55, 27, 1, WOOD_SH)         # contact shadow
c.poly([(15, 43), (37, 43), (39, 55), (13, 55)], COVER)
c.poly([(16, 44), (36, 44), (38, 54), (14, 54)], WHITE)
c.rect(26, 44, 1, 10, SPINE)           # fold
c.rect(27, 44, 1, 10, GREY)
for y in (45, 48, 51):                 # spiral rings along the fold
    c.set(26, y, INK)
for y in (46, 48, 50, 52):             # ruled lines
    c.rect(17, y, 9, 1, SPINE)
    c.rect(28, y, 9, 1, SPINE)
c.rect(18, 46, 6, 1, GREY)             # handwriting, left page
c.rect(18, 48, 5, 1, GREY)
c.rect(18, 50, 7, 1, GREY)
c.rect(18, 52, 4, 1, GREY)
c.rect(29, 46, 6, 1, GREY)             # right page: notes
c.rect(31, 47, 2, 2, GREY)             # flask sketch: neck
c.line(31, 49, 28, 53, GREY)           # body, left side
c.line(32, 49, 35, 53, GREY)           # body, right side
c.rect(28, 53, 8, 1, GREY)             # base
c.rect(30, 52, 4, 1, GREEN)            # liquid

# ---------------------------- pencil -------------------------------
c.rect(0, 52, 13, 1, WOOD_SH)          # contact shadow
c.rect(2, 50, 9, 2, AMBER)             # body x2..10
c.set(0, 50, RUBBER); c.set(0, 51, RUBBER)
c.set(1, 50, MET_L); c.set(1, 51, MET_L)
c.set(11, 50, WOOD_L); c.set(11, 51, WOOD_L)
c.set(12, 50, INK)                     # graphite tip

# ----------------------------- finish ------------------------------
print(c.stats_text())
import os
if os.environ.get("LAB_INSPECT") != "1":
    finish(c)
