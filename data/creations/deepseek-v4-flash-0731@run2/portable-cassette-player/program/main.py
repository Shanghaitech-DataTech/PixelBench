from pixelbench_api import *

c = new_canvas(32, 32, name="cassette")

GOLD = c.color("#d9a441")
OUT  = c.color("#232c36")
BODY = c.color("#7f8b99")
HIL  = c.color("#9aa7b5")
FACE = c.color("#b0bbc7")
FR   = c.color("#3a4450")
REEL = c.color("#dfe6ee")
BTN  = c.color("#4b5868")
RED  = c.color("#e2574c")
PLG  = c.color("#c9d2dc")
CBL  = c.color("#1d2733")

# ---- body ----
c.rect(3, 4, 26, 24, BODY)
c.rect(3, 4, 26, 24, OUT, fill=False)
c.line(5, 5, 26, 5, HIL)
c.rect(5, 6, 22, 20, FACE)

# ---- cassette window (transparent interior) ----
c.clear(8, 12, 17, 6)                       # erase interior -> transparent
c.rect(7, 11, 18, 8, FR, fill=False)     # window frame
c.line(8, 14, 8, 16, FR)                  # tape, left side
c.line(23, 14, 23, 16, FR)                 # tape, right side
c.line(8, 17, 23, 17, FR)                  # tape, bottom run
c.rect(14, 12, 2, 5, FR)                   # tape between reels

# ---- two tape reels ----
for cx in (11, 18):
    c.circle(cx, 14, 2, FR)                # reel disc
    c.circle(cx, 14, 1, REEL)              # light hub
    for (hx, hy) in [(cx,13),(cx,14),(cx,15),(cx-1,14),(cx+1,14)]:
        c.set(hx, hy, FR)                   # reel holes

# ---- playback buttons ----
for bx in (5, 11, 17, 23):
    c.rect(bx, 20, 4, 4, BTN)
    c.rect(bx, 20, 4, 1, HIL)

# REW  (left-pointing chevron)
for (xx, yy) in [(5,21),(6,21),(7,21),(5,22),(6,22),(5,23)]:
    c.set(xx, yy, OUT)
# PLAY (right-pointing triangle)
for (xx, yy) in [(11,21),(12,21),(13,21),(12,22),(13,22),(13,23)]:
    c.set(xx, yy, RED)
# FF   (right-pointing double chevron)
for (xx, yy) in [(17,21),(18,21),(19,21),(20,21),(18,22),(19,22),(20,22),(19,23),(20,23)]:
    c.set(xx, yy, OUT)
# STOP
for (xx, yy) in [(24,21),(25,21),(26,21),(24,22),(25,22),(26,22),(24,23),(25,23),(26,23)]:
    c.set(xx, yy, OUT)

# ---- gold design stripe ----
c.line(5, 24, 26, 24, GOLD)

# ---- volume dial ----
c.circle(24, 8, 2, FR)
c.set(24, 8, OUT)
c.set(25, 7, OUT)

# ---- headphone cable + plug ----
c.path("M 18 26 Q 15 28 14 29", CBL, fill=False)
c.rect(14, 29, 6, 2, PLG)
c.rect(14, 29, 6, 2, OUT, fill=False)
c.rect(14, 31, 6, 1, GOLD)

print(c.stats_text())
print(c.matrix_text(region=(3, 4, 28, 31), indices=True))

finish(c)
