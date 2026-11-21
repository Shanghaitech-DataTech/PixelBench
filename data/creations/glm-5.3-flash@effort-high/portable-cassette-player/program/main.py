from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="cassette-player")

BODY   = c.color("#3d4f78", "body")
BODY_D = c.color("#2b3a5c", "body_dark")
LIGHT  = c.color("#5f74a3", "body_light")
DARK   = c.color("#151c2c", "outline")
SILVER = c.color("#c9cedb", "silver")
GREY   = c.color("#8a93a6", "cable")
TAPE   = c.color("#6b4a2f", "tape")
REEL   = c.color("#e9ecf2", "reel")
RED    = c.color("#d8504a", "red")
ORANGE = c.color("#f2a63a", "orange")
WHITE  = c.color("#f5f7fa", "white")

# ---------------- body ----------------
c.rect(4, 4, 24, 24, DARK)          # outline block
c.rect(5, 5, 22, 22, BODY)          # inner body
# rounded corners
for cx, cy in [(4, 4), (26, 4), (4, 26), (26, 26)]:
    c.clear(cx, cy, 2, 2)
for x, y in [(5, 5), (26, 5), (5, 26), (26, 26)]:
    c.clear(x, y, 1, 1)
c.rect(6, 5, 20, 1, LIGHT)          # top sheen
c.rect(6, 26, 20, 1, BODY_D)        # bottom shade
c.rect(26, 6, 1, 20, BODY_D)        # right shade

# ---------------- cassette window ----------------
c.rect(7, 7, 18, 11, SILVER)        # silver frame  x7..24 y7..17
c.rect(8, 8, 16, 9, DARK)           # dark bezel    x8..23 y8..16
c.clear(9, 9, 14, 8)                # TRANSPARENT window x9..22 y9..16
# corner screws on the frame
for sx, sy in [(7, 7), (24, 7), (7, 17), (24, 17)]:
    c.set(sx, sy, GREY)

# two tape reels (drawn over the transparent window)
for cx in (12, 19):
    c.circle(cx, 12, 2, TAPE)       # tape wound on spool
    c.circle(cx, 12, 1, REEL)       # light hub
    c.set(cx, 12, DARK)             # spindle hole
c.line(15, 12, 16, 12, TAPE)        # tape bridging the reels
c.line(9, 15, 22, 15, TAPE)         # tape running along the bottom

# ---------------- volume control ----------------
c.line(8, 19, 23, 19, DARK)         # slider track
c.set(8, 18, DARK)                  # end tick
c.set(23, 18, DARK)                 # end tick
c.rect(15, 18, 2, 3, ORANGE)        # slider knob
c.set(6, 19, RED)                   # power LED

# ---------------- playback controls ----------------
# rewind
c.rect(7, 21, 4, 5, DARK)
c.set(9, 22, SILVER); c.set(9, 23, SILVER); c.set(9, 24, SILVER); c.set(8, 23, SILVER)
# play
c.rect(12, 21, 4, 5, RED)
c.set(14, 22, WHITE); c.set(14, 23, WHITE); c.set(14, 24, WHITE); c.set(15, 23, WHITE)
# fast forward
c.rect(17, 21, 4, 5, DARK)
c.set(18, 22, SILVER); c.set(18, 23, SILVER); c.set(18, 24, SILVER); c.set(19, 23, SILVER)
# stop
c.rect(22, 21, 4, 5, DARK)
c.rect(23, 23, 2, 2, SILVER)

# ---------------- headphone cable ----------------
c.rect(28, 11, 1, 3, SILVER)        # jack plug
c.set(29, 12, GREY)
c.path("M29 12 Q31 13 30 16 Q29 19 31 21 Q31 24 28 26 Q26 28 29 30",
       GREY, fill=False)

print(c.stats_text())
save("cassette-player", c)
finish(c)
