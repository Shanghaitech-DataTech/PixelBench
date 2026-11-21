from pixelbench_api import *

c = new_canvas(32, 32, name="microscope")

OUT   = c.color("#262a30")
SOOT  = c.color("#3a4048")
DARK  = c.color("#5c6672")
MID   = c.color("#97a2b0")
LIGHT = c.color("#c9d4e0")
PALE  = c.color("#eef2f8")
ACC   = c.color("#4f9fe8")
ACCD  = c.color("#2e6aa8")

def R(x, y, w, h, col):
    c.rect(x, y, w, h, col)

# ---- arm (right pillar) ----
R(22, 8, 3, 19, MID)
R(22, 8, 3, 1, LIGHT)
R(23, 9, 1, 16, LIGHT)

# ---- truss under stage ----
c.poly([(13, 22), (22, 22), (21, 25), (14, 25)], SOOT)

# ---- base ----
R(5, 26, 22, 4, DARK)
R(5, 26, 22, 1, LIGHT)
R(5, 27, 22, 1, MID)
R(6, 29, 20, 1, SOOT)

# ---- stage ----
R(4, 20, 22, 2, DARK)
R(4, 20, 22, 1, LIGHT)
R(4, 21, 22, 1, ACCD)

# ---- slide on stage ----
R(15, 20, 3, 1, PALE)

# ---- objective ----
R(16, 14, 4, 3, MID)
R(16, 16, 4, 1, ACCD)
R(16, 17, 4, 1, ACC)
R(17, 18, 2, 1, ACC)
R(17, 19, 2, 1, SOOT)

# ---- body tube ----
R(16, 9, 4, 6, MID)
R(16, 9, 4, 1, LIGHT)
R(17, 10, 1, 3, LIGHT)
R(16, 13, 4, 1, ACCD)

# ---- head ----
R(13, 6, 11, 3, MID)
R(13, 6, 11, 1, LIGHT)

# ---- eyepiece ----
R(15, 3, 5, 4, MID)
R(16, 1, 3, 1, DARK)
R(16, 2, 3, 1, PALE)
R(14, 4, 7, 1, ACC)

# ---- focus knobs on arm ----
R(25, 12, 3, 4, ACC)
R(25, 12, 1, 4, ACCD)
R(25, 16, 3, 2, ACCD)

# ---- clean silhouette ----
c.outline(OUT)

print(c.stats_text())
print(c.matrix_text())

finish(c)
