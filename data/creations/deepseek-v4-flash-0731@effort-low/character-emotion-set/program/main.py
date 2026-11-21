from pixelbench_api import *

OUT = (30, 30, 30)
SKIN = (255, 198, 152)
SKIN_SH = (238, 178, 132)
HAIR = (90, 58, 34)
HAIR_DRK = (70, 45, 26)
EYE = (26, 22, 22)
MOUTH = (150, 42, 48)
OUTFIT = (66, 86, 158)
OUTFIT_DRK = (52, 70, 132)
CHEEK = (242, 138, 138)

c = new_canvas(64, 64)


def bust(ox, oy):
    # neck
    c.rect(14 + ox, 25 + oy, 4, 3, SKIN)
    # head ring
    c.ellipse(16 + ox, 19 + oy, 7, 8, OUT)
    c.ellipse(16 + ox, 19 + oy, 6, 7, SKIN)
    # lower face shading edges
    c.ellipse(16 + ox, 21 + oy, 6, 5, SKIN_SH)
    c.ellipse(16 + ox, 20 + oy, 6, 6, SKIN)
    # hair cap
    c.ellipse(16 + ox, 13 + oy, 8, 4, OUT)
    c.ellipse(16 + ox, 13 + oy, 7, 3, HAIR)
    # shoulders / outfit
    c.rect(5 + ox, 28 + oy, 22, 4, OUT)
    c.rect(6 + ox, 28 + oy, 20, 3, OUTFIT_DRK)
    c.rect(7 + ox, 29 + oy, 18, 2, OUTFIT)


def eyes(ox, oy, pts):
    for x, y in pts:
        c.set(x + ox, y + oy, EYE)


# ---------------- CALM ----------------
bust(0, 0)
eyes(0, 0, [(12, 19), (13, 19), (19, 19), (20, 19)])
eyes(0, 0, [(12, 17), (13, 17), (19, 17), (20, 17)])  # flat brows
# gentle small smile
for x, y in [(14, 22), (15, 23), (16, 23), (17, 23), (18, 22)]:
    c.set(x, y, MOUTH)

# ---------------- SMILING ----------------
bust(32, 0)
eyes(32, 0, [(12, 17), (13, 16), (19, 16), (20, 17)])  # raised brows
eyes(32, 0, [(12, 19), (13, 18), (19, 18), (20, 19)])  # happy ^^ eyes
# blush
for x, y in [(11, 21), (12, 22), (20, 21), (21, 22)]:
    c.set(x + 32, y, CHEEK)
# big open smile
smile = [(11, 23), (12, 24), (13, 24), (14, 24), (15, 24), (16, 24),
        (17, 24), (18, 24), (19, 24), (20, 23),
        (13, 25), (14, 25), (15, 25), (16, 25), (17, 25),
        (14, 26), (15, 26), (16, 26)]
for x, y in smile:
    c.set(x + 32, y, MOUTH)

# ---------------- ANGRY ----------------
bust(0, 32)
# angry brows inner-low
eyes(0, 32, [(12, 16), (13, 17), (14, 18), (18, 18), (19, 17), (20, 16)])
eyes(0, 32, [(12, 19), (13, 19), (19, 19), (20, 19)])  # squint eyes
# frown
for x, y in [(12, 22), (13, 23), (14, 24), (15, 24), (16, 24), (17, 24),
            (18, 23), (19, 22)]:
    c.set(x, y + 32, MOUTH)

# ---------------- SURPRISED ----------------
bust(32, 32)
eyes(32, 32, [(11, 15), (12, 15), (13, 15), (19, 15), (20, 15), (21, 15)])  # high brows
c.rect(32 + 12, 32 + 19, 2, 2, OUT)   # wide left eye
c.rect(32 + 12, 32 + 19, 2, 2, EYE)
c.rect(32 + 19, 32 + 19, 2, 2, OUT)
c.rect(32 + 19, 32 + 19, 2, 2, EYE)
c.ellipse(32 + 16, 32 + 24, 2, 2, MOUTH)  # open O mouth
c.ellipse(32 + 17, 32 + 25, 2, 1, (255, 120, 120))  # tongue hint

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=False))
print(c.matrix_text(region=(32, 0, 63, 31), indices=False))
print(c.matrix_text(region=(0, 32, 31, 63), indices=False))
print(c.matrix_text(region=(32, 32, 63, 63), indices=False))

finish(c)
