from pixelbench_api import *

OUT   = (40, 44, 56)
MET   = (182, 190, 204)
MID   = (136, 144, 160)
DARK  = (96, 104, 122)
BLUE  = (62, 114, 224)
LBLUE = (134, 182, 255)
KNOB  = (240, 132, 74)
STAGE = (160, 166, 182)
BASEH = (120, 128, 146)
BASED = (80, 86, 102)
WHITE = (248, 252, 254)

c = new_canvas(32, 32)

# ---- base (draw first = behind) ----
c.rect(8, 22, 17, 2, OUT).rect(9, 22, 15, 1, BASEH)
c.rect(7, 24, 19, 3, OUT).rect(8, 24, 17, 2, BASED)
c.rect(6, 26, 6, 2, OUT).rect(7, 26, 4, 1, BASED)
c.rect(19, 26, 6, 2, OUT).rect(20, 26, 4, 1, BASED)

# ---- arm (right side, three-quarter) ----
c.rect(19, 10, 5, 12, OUT).rect(20, 10, 3, 11, MID)
c.rect(17, 12, 3, 3, OUT).rect(17, 12, 1, 2, KNOB)

# ---- tube ----
c.rect(11, 5, 5, 8, OUT).rect(12, 5, 3, 8, MET)
c.rect(15, 8, 5, 2, OUT).rect(16, 8, 3, 2, MID).rect(18, 8, 2, 2, KNOB)

# ---- eyepiece ----
c.rect(11, 0, 5, 2, OUT).rect(12, 0, 3, 2, BLUE).set(12, 0, LBLUE).set(14, 1, LBLUE)
c.rect(11, 2, 5, 3, OUT).rect(12, 2, 3, 3, MET)

# ---- connection from nosepiece down to objective ----
c.rect(16, 10, 4, 3, OUT).rect(17, 10, 2, 3, MID)

# ---- objective ----
c.rect(13, 13, 6, 1, OUT).rect(14, 13, 4, 1, MID)
c.rect(14, 14, 4, 3, OUT).rect(15, 14, 2, 3, MET).rect(15, 15, 2, 1, DARK)
c.rect(14, 17, 4, 2, OUT).rect(15, 17, 2, 2, BLUE).set(15, 17, LBLUE).set(16, 18, LBLUE)

# ---- left knob ----
c.rect(9, 8, 2, 2, OUT).rect(10, 8, 1, 2, KNOB)

# ---- stage ----
c.rect(6, 19, 14, 3, OUT).rect(7, 19, 12, 1, STAGE).rect(7, 20, 12, 2, MID)
c.rect(11, 19, 5, 1, WHITE).set(14, 19, BLUE)

print(c.stats_text())
print(c.matrix_text())

finish(c)
