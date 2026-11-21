from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="microscope")

INK    = c.color("#1b1c2b", "ink")
BODY   = c.color("#4a4f66", "body")
BODY_L = c.color("#767e9c", "body_l")
METAL  = c.color("#a7b0c9", "metal")
EYE    = c.color("#2f3350", "eyepiece")
GLASS  = c.color("#7fd4e8", "glass")
STAGE  = c.color("#39405c", "stage")
ACC    = c.color("#e8b64c", "accent")

# ---------------- ARM (C-curve on the right, behind everything) ----------------
arm = [(26, 29), (26, 9), (25, 6), (22, 5), (19, 6), (17, 8),
       (19, 9), (22, 9), (23, 12), (23, 29)]
c.poly(arm, BODY, fill=True)
c.poly(arm, INK, fill=False)                     # silhouette outline
c.line(25, 27, 25, 11, BODY_L)                   # highlight
c.circle(24, 16, 2, ACC)                         # focus knob
c.circle(24, 16, 2, INK, fill=False)

# ---------------- BODY TUBE (x11-15, y6-16) ----------------
c.rect(11, 6, 5, 10, EYE)
c.line(12, 6, 12, 15, BODY_L)                    # highlight
c.line(10, 6, 10, 15, INK)                       # outlines
c.line(16, 6, 16, 15, INK)

# ---------------- EYEPIECE (narrower, on top) ----------------
c.rect(12, 2, 3, 4, EYE)
c.rect(12, 2, 3, 1, METAL)                       # top rim
c.line(11, 2, 11, 5, INK)
c.line(15, 2, 15, 5, INK)
c.line(12, 1, 14, 1, INK)

# ---------------- NOSEPIECE ----------------
c.ellipse(13, 18, 4, 2, BODY)
c.ellipse(13, 18, 4, 2, INK, fill=False)

# ---------------- OBJECTIVES ----------------
c.poly([(12, 20), (15, 20), (14, 24), (13, 24)], METAL, fill=True)  # centre, long
c.rect(9, 20, 2, 2, METAL)                                          # left, short
c.rect(16, 20, 2, 2, METAL)                                         # right, short
c.line(9, 22, 10, 22, INK)
c.line(16, 22, 17, 22, INK)
c.set(13, 24, GLASS); c.set(14, 24, GLASS)                          # lens tips

# ---------------- STAGE (y25-26) ----------------
c.rect(4, 25, 17, 2, STAGE)
c.rect(4, 25, 17, 2, INK, fill=False)
c.rect(7, 24, 3, 1, METAL)                       # stage clips
c.rect(15, 24, 3, 1, METAL)
# sample slide on the stage
c.rect(9, 25, 5, 1, GLASS)

# ---------------- BASE (3/4: top face + front face) ----------------
c.poly([(5, 28), (12, 27), (27, 27), (27, 28)], METAL, fill=True)   # top face
c.rect(5, 28, 23, 2, BODY)                                          # front face
c.line(5, 28, 12, 27, INK)
c.line(12, 27, 27, 27, INK)
c.line(27, 27, 27, 29, INK)
c.line(5, 28, 5, 29, INK)
c.line(5, 29, 27, 29, INK)

# ---------------- ILLUMINATOR (light in the base) ----------------
c.rect(12, 28, 4, 1, GLASS)
c.line(11, 28, 11, 29, INK)
c.line(16, 28, 16, 29, INK)

# ---------------- sample slide on the stage ----------------
c.rect(9, 25, 5, 1, GLASS)

# ---------------- deliverable ----------------
finish(c)

print(c.stats_text())
print(c.matrix_text())
