c = new_canvas(64, 64, name="output")

# ---------------- palette ----------------
WALL_T  = "#2b3645"
WALL_B  = "#3a4a5c"
TILE    = "#47596c"
BENCH   = "#7a6549"
BENCH_L = "#93795a"
BENCH_D = "#5a4a35"
EDGE    = "#3d3324"
CAB     = "#6b5a42"
CAB_D   = "#4b3f2e"
FLOOR   = "#232a33"

M_D   = "#23282f"
M     = "#49525f"
M_L   = "#6d788a"
CHR   = "#a8b6c4"

GLASS   = "#9fc4cf"
GLASS_D = "#6e95a3"
GLASS_L = "#d6ecf0"

LIQ_R = "#b8484a"
LIQ_G = "#5aa05c"
LIQ_B = "#4a7fc0"
LIQ_Y = "#d6b24a"

AMBER   = "#a3652a"
AMBER_L = "#c98a3e"
AMBER_D = "#6e441c"
BLUEB   = "#38618f"
BLUEB_L = "#5b86b8"
BLUEB_D = "#26456b"
CAP     = "#1e2228"
LABEL   = "#e6e0cd"
INK     = "#4a5568"

PAPER   = "#ece6d4"
PAPER_D = "#cdc5ae"
RULE    = "#8d9aad"

RUBBER   = "#a8403a"
RUBBER_L = "#cc6155"

# ---------------- room ----------------
c.rect(0, 0, 64, 40, WALL_T)
c.rect(0, 20, 64, 20, WALL_B)
for x in range(0, 64, 8):
    c.line(x, 20, x, 37, TILE)
for y in range(20, 40, 6):
    c.line(0, y, 63, y, TILE)

# wall poster (periodic-table-ish chart)
c.rect(21, 3, 13, 12, "#e8e4d6")
c.rect(22, 4, 11, 2, "#c2552f")
for i, col in enumerate(["#3f7fb5", "#4d9a5a", "#c9a23c", "#8f5bb0", "#c2552f"]):
    c.rect(22 + i * 2, 7, 2, 2, col)
for i, col in enumerate(["#4d9a5a", "#c9a23c", "#3f7fb5", "#c2552f", "#8f5bb0"]):
    c.rect(22 + i * 2, 10, 2, 2, col)
c.line(22, 13, 31, 13, RULE)

# wall shelf with small reagent bottles
c.rect(38, 19, 25, 2, BENCH_D)
c.rect(38, 19, 25, 1, BENCH)
for sx, col in [(40, "#7a9e52"), (44, "#9e5b52"), (48, "#52789e"),
                (52, "#9e8d52"), (56, "#6e5b9e"), (60, "#4f8f86")]:
    c.rect(sx, 14, 3, 5, col)
    c.set(sx, 14, GLASS_L)
    c.set(sx, 15, GLASS_L)
    c.rect(sx + 1, 12, 1, 2, CAP)
    c.set(sx, 16, LABEL)
    c.set(sx + 1, 16, LABEL)
    c.set(sx + 2, 16, LABEL)

# ---------------- bench ----------------
c.rect(0, 38, 64, 12, BENCH)
c.rect(0, 38, 64, 2, BENCH_L)
c.rect(0, 48, 64, 2, BENCH_D)
c.rect(0, 50, 64, 2, EDGE)
c.rect(0, 52, 64, 11, CAB)
c.line(0, 52, 63, 52, CAB_D)
for x in (15, 31, 47):
    c.line(x, 53, x, 62, CAB_D)
for x in (11, 27, 43, 59):
    c.line(x, 57, x + 1, 57, CHR)
c.rect(0, 63, 64, 1, FLOOR)

# ---------------- microscope (left) ----------------
c.rect(2, 36, 15, 3, M_D)              # foot
c.rect(2, 36, 15, 1, M)
c.rect(12, 20, 3, 16, M)               # arm
c.line(12, 20, 12, 35, M_L)
c.line(14, 21, 14, 35, M_D)
# tilted body tube, bottom at (8,25) rising to the left
for i in range(10):
    y = 25 - i
    x = 8 - (i + 1) // 2
    c.rect(x, y, 4, 1, M)
    c.set(x, y, M_L)
    c.set(x + 3, y, M_D)
c.rect(2, 13, 5, 3, M_L)               # eyepiece barrel
c.rect(2, 12, 5, 1, CHR)
c.rect(6, 25, 7, 2, M_D)               # nosepiece
c.rect(7, 25, 5, 1, M)
c.rect(8, 27, 2, 3, CHR)               # objective lens
c.set(10, 27, M_D)
c.rect(3, 30, 11, 2, M_L)              # stage
c.rect(3, 32, 11, 1, M_D)
c.rect(6, 29, 5, 1, GLASS_L)           # specimen slide
c.set(5, 29, M_D)
c.set(11, 29, M_D)
c.rect(7, 33, 3, 2, M)                 # condenser
c.rect(7, 35, 3, 1, M_D)
c.set(15, 31, CHR)                     # focus knobs
c.set(15, 32, CHR)
c.set(15, 28, M_L)

# ---------------- test-tube rack (centre) ----------------
RX = 19
tubes = [(RX + 2, LIQ_R), (RX + 6, LIQ_G), (RX + 10, LIQ_B), (RX + 14, LIQ_Y)]
for tx, liq in tubes:
    c.rect(tx, 23, 3, 13, GLASS)       # tube body
    c.rect(tx, 23, 1, 13, GLASS_L)     # left highlight
    c.rect(tx + 2, 24, 1, 11, GLASS_D)
    c.rect(tx, 28, 3, 7, liq)          # liquid column
    c.rect(tx, 28, 1, 7, GLASS_L)
    c.rect(tx, 35, 3, 1, GLASS_D)      # rounded bottom
    c.rect(tx, 23, 3, 1, GLASS_L)      # rim

c.rect(RX, 36, 19, 3, BENCH_D)         # base block
c.rect(RX, 36, 19, 1, BENCH)
c.rect(RX, 30, 1, 6, BENCH_D)          # end posts
c.rect(RX + 18, 30, 1, 6, BENCH_D)
c.rect(RX, 30, 19, 2, BENCH)           # upper rail in front of tubes
c.line(RX, 31, RX + 18, 31, BENCH_D)
for tx, liq in tubes:
    c.rect(tx, 30, 3, 1, M_D)          # rail holes

# ---------------- labeled bottles (right) ----------------
# amber reagent bottle
c.rect(39, 28, 7, 10, AMBER)
c.rect(39, 28, 2, 10, AMBER_L)
c.rect(45, 29, 1, 9, AMBER_D)
c.rect(41, 25, 3, 3, AMBER)
c.set(41, 25, AMBER_L)
c.set(41, 26, AMBER_L)
c.rect(40, 23, 5, 2, CAP)
c.rect(39, 31, 7, 4, LABEL)
c.line(40, 32, 44, 32, INK)
c.line(40, 33, 43, 33, RULE)
c.line(40, 34, 44, 34, RULE)
c.rect(39, 37, 7, 1, AMBER_D)

# blue solvent bottle
c.rect(48, 30, 6, 8, BLUEB)
c.rect(48, 30, 2, 8, BLUEB_L)
c.rect(53, 31, 1, 7, BLUEB_D)
c.rect(50, 28, 2, 2, BLUEB)
c.set(50, 28, BLUEB_L)
c.rect(49, 26, 4, 2, CAP)
c.rect(48, 32, 6, 3, LABEL)
c.line(49, 33, 52, 33, INK)
c.line(49, 34, 51, 34, RULE)
c.rect(48, 37, 6, 1, BLUEB_D)

# beaker with blue solution
c.rect(56, 30, 7, 8, GLASS)
c.rect(56, 30, 1, 8, GLASS_L)
c.rect(62, 31, 1, 7, GLASS_D)
c.rect(56, 33, 7, 5, LIQ_B)
c.rect(56, 33, 7, 1, "#6fa3d8")
c.rect(56, 37, 7, 1, GLASS_D)
c.set(56, 34, GLASS_L)
c.set(57, 31, GLASS_L)
c.set(60, 32, "#c9dde8")               # graduation marks
c.set(60, 34, "#c9dde8")

# ---------------- dropper / pipette on bench (front left) ----------------
# glass barrel, thin, angled down to the left
for i in range(9):
    x = 5 + i
    y = 46 - (i // 3)
    c.set(x, y, GLASS_L)
    c.set(x, y + 1, GLASS_D)
c.set(4, 47, CHR)                      # tip
c.set(3, 48, LIQ_B)                    # drop
c.rect(14, 43, 4, 3, RUBBER)           # bulb
c.set(14, 43, RUBBER_L)
c.set(15, 43, RUBBER_L)
c.set(17, 45, "#7d2a26")
c.set(13, 44, RUBBER)
c.set(13, 45, GLASS_D)

# ---------------- open notebook (front right) ----------------
c.poly([(25, 44), (37, 43), (37, 48), (24, 47)], PAPER)
c.poly([(38, 43), (50, 44), (51, 48), (38, 48)], PAPER)
c.line(37, 43, 37, 48, PAPER_D)
c.line(38, 43, 38, 48, PAPER_D)
c.poly([(25, 44), (37, 43), (37, 48), (24, 47)], PAPER_D, fill=False)
c.poly([(38, 43), (50, 44), (51, 48), (38, 48)], PAPER_D, fill=False)
NOTE = "#9aa3b2"
# handwriting as single-pixel dashes, left page
for x in (27, 29, 31, 33):
    c.set(x, 45, NOTE)
for x in (26, 28, 30, 32, 34):
    c.set(x, 46, NOTE)
for x in (26, 28, 30):
    c.set(x, 47, NOTE)
# right page: notes plus a tiny plotted curve
for x in (40, 42, 44, 46, 48):
    c.set(x, 47, NOTE)
c.set(41, 45, NOTE)
c.set(43, 44, NOTE)
c.set(45, 44, NOTE)
c.set(47, 45, NOTE)

# ---------------- contact shadows on bench top ----------------
SHADOW = "#6b5840"
c.rect(2, 39, 15, 1, SHADOW)
c.rect(19, 39, 19, 1, SHADOW)
c.rect(39, 39, 7, 1, SHADOW)
c.rect(48, 39, 6, 1, SHADOW)
c.rect(56, 39, 7, 1, SHADOW)
c.set(17, 39, BENCH_L)
c.set(38, 39, BENCH_L)

print(c.stats_text())
# ---------------- final polish ----------------
# soft vignette in the upper corners
c.rect(0, 0, 3, 3, "#222b37")
c.rect(61, 0, 3, 3, "#222b37")
c.set(3, 0, "#263140")
c.set(0, 3, "#263140")
c.set(60, 0, "#263140")
c.set(63, 3, "#263140")
# bench front edge catch-light
c.line(0, 50, 63, 50, "#4a3e2d")
view(c)
finish(c)
