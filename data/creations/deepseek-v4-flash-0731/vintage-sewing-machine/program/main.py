from pixelbench_api import *

c = new_canvas(48, 48, name="sewing")

BLACK = c.color("#0B0B0D")
SHADOW = c.color("#141419")
BODY = c.color("#1F1F26")
MID = c.color("#32323B")
LIGHT = c.color("#4E4E5A")
HI = c.color("#7A7A88")
SILVER = c.color("#C6C6D0")
GOLD = c.color("#D8A83C")
DGOLD = c.color("#8A6A1E")
RED = c.color("#C23333")
DRED = c.color("#7E1E26")
LRED = c.color("#E2604E")
CREAM = c.color("#E8DCC0")

# ---------------- FABRIC ----------------
c.rect(0, 33, 33, 3, RED)          # x0..32, y33..35, lying on the bed
c.rect(0, 33, 33, 1, LRED)         # lit top edge
c.rect(1, 35, 4, 1, DRED)          # shadow line where it drapes
c.line(6, 33, 6, 34, DRED)         # wrinkle
c.line(22, 33, 22, 34, DRED)       # wrinkle

# ---------------- BED / STAND ----------------
c.rect(4, 36, 40, 4, BODY)         # bed x4..43, y36..39
c.rect(4, 36, 40, 1, MID)          # bed top face
c.rect(4, 39, 40, 1, BLACK)        # bed lower shade

# stand
c.rect(9, 40, 4, 4, BODY)          # left leg  x9..12 y40..43
c.rect(9, 40, 4, 1, MID)
c.rect(35, 40, 6, 4, BODY)         # right leg x35..40
c.rect(35, 40, 6, 1, MID)
c.rect(3, 43, 42, 4, SHADOW)        # base plate x3..44 y43..46
c.rect(3, 43, 42, 1, BODY)
c.rect(3, 46, 42, 1, BLACK)

# ---------------- BODY ----------------
c.rect(33, 12, 9, 26, BODY)        # pillar   x33..41 y12..37
c.rect(18, 14, 15, 9, BODY)        # arm      x18..32 y14..22
c.rect(8, 13, 10, 13, BODY)        # head     x8..17  y13..25

# top highlights
c.line(18, 14, 32, 14, LIGHT)
c.line(34, 12, 40, 12, LIGHT)
c.line(9, 13, 15, 13, LIGHT)
c.line(8, 13, 8, 24, MID)          # front edge shade

# gold scroll decal on the arm
c.rect(20, 16, 9, 1, GOLD)
c.set(21, 15, GOLD)
c.set(27, 15, GOLD)

# throat plate on bed under the needle
c.rect(10, 36, 8, 1, SILVER)
c.rect(10, 36, 8, 1, BLACK)        # recessed slot line
c.line(11, 36, 17, 36, SILVER)     # plate edges either side of slot
c.set(11, 35, SILVER)               # plate lip shows above the slot

# thread path from spool to the needle
c.line(27, 12, 13, 15, CREAM)
c.line(13, 15, 12, 22, CREAM)

# head face details
c.circle(12, 19, 3, MID)            # rounded side cap on the head
c.circle(12, 19, 1, GOLD)
c.line(18, 22, 32, 22, SHADOW)      # under-arm shadow
c.set(13, 26, SHADOW)               # dark slot where the needle bar drops

# ---------------- NEEDLE BAR / PRESSER FOOT ----------------
c.rect(12, 23, 2, 9, SILVER)       # needle bar x12..13 y23..31
c.rect(13, 31, 1, 3, SILVER)       # needle down to the cloth
c.rect(13, 33, 1, 1, HI)
c.rect(15, 24, 2, 6, MID)          # presser foot bar x15..16 y24..29
c.rect(9, 30, 7, 2, BODY)          # presser foot x9..15 y30..31
c.rect(9, 30, 7, 1, MID)           # foot top
c.rect(12, 26, 1, 1, LIGHT)        # bar shine
c.set(15, 27, LIGHT)

# ---------------- HANDWHEEL ----------------
c.circle(40, 22, 7, BLACK)         # rim     x33..46 y15..28
c.circle(40, 22, 5, BODY)          # recessed disk
c.line(40, 22, 37, 18, MID)
c.line(40, 22, 43, 18, MID)
c.line(40, 22, 37, 26, MID)
c.line(40, 22, 43, 26, MID)
c.circle(40, 22, 1, SHADOW)
c.set(40, 22, SILVER)
c.set(35, 18, LIGHT)                # rim shine
c.set(35, 20, LIGHT)
c.set(44, 26, LIGHT)                # rim reflection
c.rect(38, 18, 3, 3, GOLD)         # hub crank knob
c.set(40, 20, SILVER)               # knob shine

# ---------------- SPOOL & WINDER ----------------
c.rect(28, 7, 2, 3, MID)           # spool pin  x28..29 y7..9
c.rect(26, 10, 6, 4, CREAM)        # spool      x26..31 y10..13
c.line(26, 11, 31, 11, GOLD)       # thread winding
c.rect(28, 9, 2, 1, SILVER)        # thread tail off the spool
c.line(29, 10, 22, 10, CREAM)      # leading thread to the head
c.circle(38, 9, 3, MID)             # bobbin winder wheel on pillar
c.set(38, 9, BODY)

# ---------------- FINISH ----------------
print(c.stats_text())
print(c.matrix_text())
finish(c)
