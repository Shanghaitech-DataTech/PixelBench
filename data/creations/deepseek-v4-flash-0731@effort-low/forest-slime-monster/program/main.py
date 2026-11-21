from pixelbench_api import *

OUTLINE = "#26301f"
BODY    = "#5a8a3c"
HILITE  = "#79b04a"
DMOSS   = "#3f6328"
FACE    = "#6fae4a"
BLUSH   = "#c98b6b"
ANTLER  = "#a5753f"
EYE     = "#ffe65c"
EYEBR   = "#fff6b0"
PUPIL   = "#241a00"
MUSH_R  = "#d23b2e"
MUSH_W  = "#f7f0e0"
MUSH_S  = "#e8d9b0"

c = new_canvas(32, 32, name="slime")

# ---- Body: broad blob with raised dome ----
c.ellipse(15, 19, 12, 10, BODY)      # main body x3-27, y9-29
c.ellipse(15, 11, 8, 5, BODY)        # raised head dome x7-23, y6-16
c.rect(9, 29, 14, 1, BODY)
c.ellipse(15, 18, 12, 11, BODY)      # squat the base

# ---- Outline the body fully ----
c.outline(OUTLINE)

# ---- Face region (lighter moss) ----
c.ellipse(15, 15, 6, 6, FACE)

# ---- Glowing eyes ----
for ex, ey in ((11, 13), (19, 13)):
    c.circle(ex, ey, 2, EYE, fill=False)
    c.circle(ex, ey, 1, EYEBR, fill=True)
c.set(11, 13, PUPIL); c.set(19, 13, PUPIL)

# ---- Friendly mouth ----
c.set(13, 17, PUPIL); c.set(14, 18, PUPIL)
c.set(15, 18, PUPIL); c.set(16, 18, PUPIL); c.set(17, 17, PUPIL)
c.set(14, 17, OUTLINE); c.set(15, 17, OUTLINE); c.set(16, 17, OUTLINE)

# ---- Blush cheeks ----
c.set(7, 16, BLUSH); c.set(8, 17, BLUSH)
c.set(23, 16, BLUSH); c.set(22, 17, BLUSH)

# ---- Moss/texture ----
c.circle(9, 11, 1, DMOSS); c.circle(23, 11, 1, DMOSS)
c.circle(10, 23, 2, DMOSS); c.circle(20, 23, 2, DMOSS)
c.circle(13, 24, 1, HILITE)
c.line(8, 24, 22, 24, DMOSS)
c.set(7, 23, DMOSS); c.set(23, 23, DMOSS)

# ---- Tiny antlers ----
# left (stalk at x10, branch toward x9/x11)
for yy, xx in ((4, 10), (5, 9), (5, 10), (5, 11), (6, 10), (7, 10), (8, 10)):
    c.set(xx, yy, ANTLER)
# right (mirrored about x=16: x9->23, x11->21)
for yy, xx in ((4, 22), (5, 23), (5, 22), (5, 21), (6, 22), (7, 22), (8, 22)):
    c.set(xx, yy, ANTLER)

# ---- Small red mushroom on back (center-top) ----
c.rect(15, 8, 2, 3, MUSH_S)          # stem
c.set(14, 10, MUSH_S); c.set(17, 10, MUSH_S)
c.ellipse(15, 7, 3, 2, MUSH_R)       # cap x12-18, y5-8
c.set(15, 4, MUSH_R)                 # cap top
c.set(14, 6, MUSH_W); c.set(16, 7, MUSH_W)

print(c.stats_text())
print(c.matrix_text(region=(2, 3, 29, 30), indices=False))

result = c
finish(result)
