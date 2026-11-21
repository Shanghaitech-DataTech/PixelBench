from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="player")

outline = c.color("#151a26")
body = c.color("#46547a")
body_light = c.color("#60709f")
reel = c.color("#c9d2e8")
hub = c.color("#2c3550")
btn = c.color("#e7ebf6")
dial = c.color("#93a2cc")
cable = c.color("#38415c")
led = c.color("#e05a5a")

# ---- body: rounded rect silhouette with 1px dark border, corners cut ----
c.rect(3, 4, 26, 22, outline)                 # dark block x3..28, y4..25
for cx, cy in ((3, 4), (27, 4), (3, 24), (27, 24)):
    c.clear(cx, cy, 2, 2)                      # clip 2x2 corners
c.rect(4, 5, 24, 20, body)                    # inner body x4..27, y5..24
c.rect(5, 5, 22, 1, body_light)               # top highlight

# ---- transparent cassette window with two tape reels ----
c.clear(8, 8, 15, 10)                          # window x8..22, y8..17
c.circle(11, 12, 3, reel)                       # left reel
c.circle(18, 12, 3, reel)                       # right reel
c.circle(11, 12, 1, hub)
c.circle(18, 12, 1, hub)
c.rect(12, 14, 8, 1, hub)                       # tape band between reels
c.set(11, 12, None)                             # spindle holes
c.set(18, 12, None)
c.rect(8, 8, 15, 10, outline, fill=False)      # window frame on top

# ---- playback controls: rewind / play / pause / stop ----
for x in (8, 12, 16, 20):
    c.rect(x, 20, 3, 3, btn)
c.poly([(9, 20), (9, 22), (8, 21)], outline)    # rewind (<<)
c.poly([(10, 20), (10, 22), (9, 21)], outline)
c.poly([(12, 20), (12, 22), (14, 21)], outline) # play (>)
c.rect(16, 20, 1, 3, outline)                   # pause (||)
c.rect(18, 20, 1, 3, outline)
c.rect(20, 20, 3, 3, outline)                   # stop (square)

# ---- volume dial (recessed knob, right of window) ----
c.circle(25, 11, 2, outline)
c.circle(25, 11, 1, dial)
c.set(26, 10, outline)                           # knob marker

# ---- power led ----
c.set(6, 6, led)

# ---- headphone cable trailing from the bottom ----
c.line(13, 25, 13, 27, cable)
c.line(13, 27, 10, 30, cable)
c.circle(10, 30, 1, cable)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))
finish(c)
