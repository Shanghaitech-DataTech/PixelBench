from pixelbench_api import new_canvas, finish

c = new_canvas(48, 48)

# palette
K = c.color("#1b1b22")   # body black
KD = c.color("#101015")  # body dark
G = c.color("#2a2a33")  # body grey
GH = c.color("#3d3d49")  # highlight grey
S = c.color("#9aa0ab")   # steel
SB = c.color("#d7dbe3")  # steel bright
SD = c.color("#5f6570")  # steel dark
GOLD = c.color("#c9a227")
GOL = c.color("#e8c95c")
GOD = c.color("#8a6d14")
WL = c.color("#7a5230")  # wood light
WM = c.color("#5a3a22")  # wood mid
WD = c.color("#3a2410")  # wood dark
DW = c.color("#22130a")  # wood darkest
R = c.color("#c01830")  # red fabric
RD = c.color("#7d0a1c")  # red dark
RL = c.color("#e25468")  # red light
RF = c.color("#55060f")  # red fold line

# --- ground shadow (soft)
c.ellipse(24, 43, 17, 1, (70, 70, 85, 150))

# --- wooden base (slightly angled: bright top face + dark front)
c.rect(10, 35, 30, 1, WL)
c.rect(10, 36, 30, 2, WM)
c.rect(10, 38, 30, 4, WD)
c.rect(10, 42, 30, 1, DW)
c.rect(15, 38, 1, 4, DW)
c.rect(22, 39, 1, 3, DW)
c.rect(29, 38, 1, 4, DW)
c.rect(34, 39, 1, 3, DW)

# --- metal bed
c.rect(10, 33, 30, 2, S)
c.rect(10, 33, 30, 1, SB)
c.rect(10, 34, 30, 1, SD)

# --- machine body
c.rect(11, 11, 28, 5, K)          # arm
c.rect(11, 11, 28, 1, G)          # arm top
c.rect(13, 13, 24, 1, GOD)         # gold trim
c.circle(22, 13, 1, GOD)
c.circle(27, 13, 1, GOD)
c.rect(31, 15, 8, 19, K)          # pillar
c.rect(31, 15, 8, 1, G)
c.circle(33, 20, 2, GOD, fill=False)
c.rect(33, 22, 1, 5, GOD)
c.rect(35, 29, 2, 3, GOD)          # presser lifter knob
c.rect(11, 13, 9, 16, K)          # head
c.rect(11, 13, 1, 6, GH)           # head front edge
c.rect(12, 14, 6, 7, G)            # face panel
c.circle(13, 16, 1, GOD)
c.circle(16, 19, 1, GOD)
c.rect(15, 24, 4, 2, GOD)          # needle clamp
c.rect(12, 21, 8, 1, GOD)          # gold band on head

# --- spool with red thread on the arm
c.rect(17, 6, 4, 4, SD)
c.rect(17, 7, 4, 2, R)
c.rect(17, 7, 4, 1, RL)
c.rect(17, 9, 4, 1, SD)

# --- bobbin winder pulley
c.circle(37, 11, 2, G)
c.circle(37, 11, 1, GOL)

# --- handwheel (front-right, slightly angled)
c.circle(38, 21, 6, KD)
c.circle(38, 21, 5, G)
c.circle(38, 21, 4, GOL, fill=False)
c.line(38, 16, 38, 26, GOLD)
c.line(33, 21, 43, 21, GOLD)
c.line(34, 17, 42, 25, GOLD)
c.circle(38, 21, 2, GOLD)
c.circle(38, 21, 1, GOL)

# --- gold thread line from spool to needle
c.line(17, 10, 15, 13, GOL)
c.line(15, 13, 15, 23, GOL)
c.line(15, 23, 16, 25, GOL)

# --- red fabric under the needle, draping over the base
c.rect(9, 31, 16, 2, R)
c.rect(9, 31, 12, 1, RL)
c.rect(13, 33, 11, 6, RD)
c.rect(15, 34, 1, 5, RF)
c.rect(18, 34, 1, 5, RF)
c.rect(21, 34, 1, 5, RF)
c.rect(16, 34, 1, 4, "#9c1026")
c.rect(13, 39, 11, 1, R)
c.rect(13, 40, 11, 1, RF)
c.rect(13, 38, 11, 1, R)   # pull fabric a touch further down
c.set(15, 38, GOL)          # stitch gleam
c.rect(12, 32, 6, 1, RD)   # presser shadow on fabric

# --- needle bar, needle, presser foot (in front of fabric)
c.rect(13, 26, 2, 5, SD)
c.rect(12, 30, 6, 2, SD)
c.rect(12, 31, 6, 1, SB)
c.rect(16, 24, 2, 8, SB)
c.rect(16, 32, 2, 1, SB)

print(c.stats_text())
print(c.matrix_text())
finish(c)
