from pixelbench_api import *

c = new_canvas(64, 64, name="dragon_hatchling")

OUT = c.color((22, 30, 20))
G1 = c.color((88, 168, 76))
G2 = c.color((56, 116, 56))
G3 = c.color((128, 200, 100))
MEM = c.color((58, 98, 70))
MEM2 = c.color((76, 128, 88))
BEL = c.color((238, 228, 186))
BEL2 = c.color((202, 182, 140))
BONE = c.color((238, 220, 168))
EYE = c.color((255, 208, 64))
PUP = c.color((60, 40, 20))
MOU = c.color((110, 30, 40))
TETH = c.color((250, 250, 240))

M = 63
def mir(pts):
    return [(M - x, y) for x, y in pts]

# --- wings (half spread, behind body) ---
WL = [(24, 26), (8, 16), (4, 24), (10, 29), (6, 34), (16, 35), (24, 33)]
c.poly(WL, MEM)
c.poly(mir(WL), MEM)
c.poly([(15, 27), (8, 20), (5, 26), (11, 30)], MEM2)
c.poly(mir([(15, 27), (8, 20), (5, 26), (11, 30)]), MEM2)
c.line(22, 27, 8, 16, BONE)
c.line(22, 27, 4, 24, BONE)
c.line(22, 30, 6, 34, BONE)
c.line(M - 22, 27, M - 8, 16, BONE)
c.line(M - 22, 27, M - 4, 24, BONE)
c.line(M - 22, 30, M - 6, 34, BONE)

# --- tail (spiked) ---
c.poly([(43, 44), (57, 41), (61, 46), (56, 52), (43, 51)], G1)
c.poly([(48, 41), (50, 34), (53, 41)], BONE)
c.poly([(54, 42), (57, 36), (58, 43)], BONE)
c.poly([(58, 44), (61, 38), (62, 45)], BONE)
c.poly([(55, 49), (58, 47), (56, 51)], BONE)

# --- body ---
c.ellipse(32, 40, 16, 14, G1)
c.ellipse(32, 45, 9, 7, BEL)
c.ellipse(32, 48, 6, 3, BEL2)
c.ellipse(32, 53, 6, 2, BEL)
for x, y in ((22, 34), (28, 31), (36, 31), (42, 34), (19, 42), (45, 42), (26, 27), (38, 27)):
    c.set(x, y, G3)

# --- front legs ---
c.ellipse(20, 50, 5, 6, G1)
c.ellipse(44, 50, 5, 6, G1)
c.ellipse(20, 56, 4, 3, G2)
c.ellipse(44, 56, 4, 3, G2)
for pts in ([(16, 58), (17, 60), (19, 58)], [(19, 58), (20, 61), (22, 58)], [(22, 58), (23, 60), (24, 58)],
           [(40, 58), (41, 60), (43, 58)], [(43, 58), (44, 61), (46, 58)], [(46, 58), (47, 60), (49, 58)]):
    c.poly(pts, BONE)

# --- head ---
c.ellipse(32, 16, 13, 12, G1)
c.ellipse(32, 10, 5, 3, G3)

# horns
c.poly([(23, 8), (24, 1), (28, 7)], BONE)
c.poly([(41, 8), (40, 1), (36, 7)], BONE)

# eyes (angled, angry)
c.poly([(17, 13), (26, 11), (26, 16), (19, 17)], EYE)
c.poly([(47, 13), (38, 11), (38, 16), (45, 17)], EYE)
c.rect(23, 12, 2, 5, PUP)
c.rect(39, 12, 2, 5, PUP)

# open mouth growl
c.ellipse(32, 25, 12, 4, MOU)
c.poly([(24, 21), (26, 21), (25, 25)], TETH)
c.poly([(30, 21), (32, 21), (31, 25)], TETH)
c.poly([(36, 21), (38, 21), (37, 24)], TETH)
c.poly([(27, 28), (29, 28), (28, 25)], TETH)
c.poly([(33, 28), (35, 28), (34, 25)], TETH)
c.poly([(22, 23), (24, 23), (23, 26)], TETH)
c.poly([(40, 23), (42, 23), (41, 26)], TETH)
c.poly([(23, 30), (41, 30), (37, 34), (27, 34)], G2)

# --- strong silhouette ---
c.outline(OUT)

print(c.stats_text())
print(c.matrix_text())
finish(c)
