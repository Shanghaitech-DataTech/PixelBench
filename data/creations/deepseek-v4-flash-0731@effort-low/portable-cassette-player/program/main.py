from pixelbench_api import *

OUT  = (40, 44, 52)
BODY = (116, 158, 206)
HIL  = (152, 188, 228)
LIN  = (188, 210, 236)
DRK  = (54, 60, 70)
BTN  = (198, 208, 220)
REEL = (50, 55, 62)
HUB  = (224, 232, 240)
CAB  = (190, 74, 86)
JACK = (60, 66, 76)
VOL  = (84, 90, 100)
VOLT = (232, 150, 80)

c = new_canvas(32, 32, name="cassette")

# ---- headphone cable (draped across the top) ----
for d in (0, 1):
    c.line(17 + d, 5, 17 + d, 1, CAB)
    c.line(17 + d, 1, 10 + d, 0, CAB)
    c.line(10 + d, 0, 6 + d, 3, CAB)
c.circle(17, 5, 1, JACK)

# ---- body ----
body_path = "M6,3 H27 A2,2 0 0 1 29,5 V28 A2,2 0 0 1 27,30 H6 A2,2 0 0 1 4,28 V5 A2,2 0 0 1 6,3 Z"
c.path(body_path, BODY)
c.path(body_path, OUT, fill=False)
c.line(5, 4, 27, 4, HIL)

# ---- transparent cassette window + frame ----
c.clear(9, 7, 18, 14)          # x9..26, y7..20 transparent
c.rect(9, 7, 18, 14, DRK, fill=False)
c.line(10, 8, 25, 8, LIN)

# two tape reels
for cx in (12, 22):
    c.circle(cx, 13, 4, REEL, fill=False)
    c.circle(cx, 13, 3, REEL)
    c.circle(cx, 13, 1, HUB)

# speaker grille on the left strip
for yy in (9, 12, 15, 18):
    c.set(5, yy, DRK)

# ---- playback controls (5 buttons) ----
def btn(bx):
    c.rect(bx, 22, 4, 5, BTN)
    c.rect(bx, 22, 4, 5, DRK, fill=False)

# rewind
btn(6)
c.poly([(7, 23), (7, 26), (6, 24)], DRK)
c.poly([(9, 23), (9, 26), (8, 24)], DRK)
c.line(6, 25, 7, 25, DRK)
c.line(8, 25, 9, 25, DRK)
c.line(9, 24, 9, 26, DRK)
#   -> points give triangular bars

# play
btn(11)
c.poly([(13, 22), (13, 27), (15, 25)], DRK)

# record
btn(16)
c.circle(18, 24, 2, DRK)

# stop
btn(21)
c.rect(23, 23, 3, 3, DRK)

# fast-forward
btn(26)
c.poly([(28, 22), (28, 27), (30, 25)], DRK)

# ---- volume wheel on the right ----
c.circle(29, 22, 1, VOL)
c.circle(29, 22, 1, OUT, fill=False)
c.line(30, 21, 30, 23, VOLT)

# ---- screws ----
for (sx, sy) in ((6, 5), (6, 28)):
    c.set(sx, sy, OUT)

# ---- TRANSPARENT reels visible through window already; ensure window stays transparent
# (cleared earlier)

print(c.stats_text())
finish(c)
