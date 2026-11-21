# ==============================================================
#  farm-sheep  -  32 x 32  -  Stardew-style fluffy ewe, side view
#  cozy, soft rounded shapes, gentle flat shading, no hard outline
# ==============================================================

c = new_canvas(32, 32, background=None, name="farm-sheep")

# ---------------- palette (warm + muted) ----------------
WOOL    = c.color("#f2ecdf", "wool")          # creamy fleece
WOOL_HI = c.color("#fbf7ec", "wool_light")    # lit crowns
WOOL_SH = c.color("#ded2bb", "wool_shade")    # soft underside
WOOL_DP = c.color("#c9bba1", "wool_deep")     # belly shadow
FACE    = c.color("#7b6d5e", "face")          # warm grey-brown face
FACE_HI = c.color("#8f8070", "face_light")
FACE_DP = c.color("#61544a", "face_shade")
EAR     = c.color("#e8c0b4", "ear_pink")      # pale pink ears
EAR_IN  = c.color("#d6a096", "ear_inner")
BLUSH   = c.color("#dba3a0", "blush")
LEG     = c.color("#55493f", "leg")
LEG_F   = c.color("#443a31", "leg_far")
HOOF    = c.color("#322b25", "hoof")
EYE     = c.color("#2e2823", "eye")
GLINT   = c.color("#f6f1e4", "glint")
NOSTRIL = c.color("#3e352e", "nostril")

PAL = {
    "W": WOOL, "H": WOOL_HI, "S": WOOL_SH, "D": WOOL_DP,
    "F": FACE, "L": FACE_HI, "G": FACE_DP,
    "P": EAR, "Q": EAR_IN,
    "l": LEG, "k": LEG_F, "o": HOOF,
    "E": EYE, "g": GLINT, "n": NOSTRIL, "B": BLUSH,
}


def row(y, *segs):
    for x0, x1, ch in segs:
        for x in range(x0, x1 + 1):
            c.set(x, y, PAL[ch])


def px(x, y, ch):
    c.set(x, y, PAL[ch])


# ---------------- little upturned tail tuft ----------------
row(5, (29, 30, "H"))
row(6, (28, 30, "H"))
row(7, (28, 29, "H"))

# ---------------- fleece dome : crowns + filled valleys ----------------
row(6, (9, 11, "H"), (19, 21, "H"))
row(7, (8, 13, "H"), (14, 17, "W"), (18, 22, "H"), (23, 27, "W"))
row(8, (6, 12, "H"), (13, 29, "W"))
row(9, (5, 29, "W"))
row(10, (5, 29, "W"))

# ---------------- head + body ----------------
row(11, (4, 5, "W"), (6, 11, "F"), (12, 12, "G"), (13, 29, "W"))
row(12, (4, 4, "W"), (5, 11, "F"), (12, 12, "G"), (13, 28, "W"), (29, 29, "S"))
row(13, (4, 4, "L"), (5, 11, "F"), (12, 12, "G"), (13, 28, "W"), (29, 29, "S"))
row(14, (4, 4, "L"), (5, 11, "F"), (12, 12, "G"), (13, 28, "W"), (29, 29, "S"))
row(15, (4, 4, "L"), (5, 11, "F"), (12, 12, "G"), (13, 28, "W"), (29, 29, "S"))
row(16, (4, 4, "L"), (5, 10, "F"), (11, 12, "G"), (13, 27, "W"), (28, 28, "S"))
row(17, (5, 10, "F"), (11, 12, "G"), (13, 26, "W"), (27, 28, "S"))
row(18, (6, 11, "F"), (12, 12, "G"), (13, 26, "W"), (27, 27, "S"))
row(19, (7, 12, "G"), (13, 25, "W"), (26, 26, "S"))
row(20, (11, 13, "S"), (14, 24, "W"), (25, 25, "S"))
row(21, (13, 16, "S"), (17, 22, "D"), (23, 25, "S"))

# ---------------- ears : pale pink, tipping down ----------------
row(9,  (3, 4, "P"))
row(10, (2, 4, "P"))
row(11, (1, 2, "Q"), (3, 3, "P"))
row(13, (2, 3, "P"))
row(14, (1, 3, "P"))
row(15, (0, 1, "Q"), (2, 3, "P"))

# ---------------- legs : under the chest and the rump ----------------
row(22, (13, 14, "l"), (15, 15, "k"), (23, 24, "l"), (25, 25, "k"))
row(23, (13, 14, "l"), (15, 15, "k"), (23, 24, "l"), (25, 25, "k"))
row(24, (13, 15, "o"), (23, 25, "o"))
row(25, (13, 15, "o"), (23, 25, "o"))

# ---------------- soft wool creases ----------------
px(17, 13, "S"); px(18, 13, "S")
px(21, 16, "S"); px(22, 16, "S")
px(16, 19, "S"); px(17, 19, "S")

# ---------------- face details ----------------
px(6, 12, "E"); px(7, 12, "E")
px(6, 13, "E"); px(7, 13, "E")
px(6, 12, "g")                      # catchlight
px(5, 15, "n")                      # nostril
px(6, 16, "G"); px(7, 16, "G")      # mouth
px(8, 15, "B"); px(9, 15, "B")      # blush

# ---------------- export + submit ----------------
save("farm-sheep", c, indexed=True)
finish(c)
