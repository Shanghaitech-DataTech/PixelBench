from pixelbench_api import *

W = H = 64
c = new_canvas(W, H)

# ---------------- sky background ----------------
SKY = ["#68b4e2","#74bee8","#80c8ee","#8ed2f2","#9cdaf4","#aae2f6","#b8eaf8","#c6f0fa","#d4f6fc","#e0fafd","#ecfefe","#f6ffff","#fcffff","#ffffff","#ffffff","#ffffff"]
for i, sc in enumerate(SKY):
    c.rect(0, i * 4, 64, 4, sc)

CLOUD = "#f2f6fc"; CLOUDD = "#c8dcf0"
def cloud(cx, cy, r=3):
    d = r - 1
    c.circle(cx, cy, r, CLOUD)
    c.circle(cx - r, cy, d, CLOUD)
    c.circle(cx + r, cy, d, CLOUD)
    c.circle(cx - 2, cy + 1, d, CLOUD)
    c.circle(cx + 2, cy + 1, d, CLOUD)
    c.circle(cx, cy + 2, d, CLOUDD)
cloud(48, 7); cloud(6, 11); cloud(56, 28); cloud(3, 33)

# ---------------- palette ----------------
NAVY = "#2a4a74"; NAVYHI = "#4a7cac"; NAVYD = "#1a3050"
BR = "#4a3620"
RED = "#d32030"; REDHI = "#f25a62"; REDD = "#9c1622"
HAIR = "#c78a34"; HAIRHI = "#e8b860"; HAIRD = "#9a6220"
SKIN = "#f6c89a"; SKSH = "#e2a878"
EYEL = "#26263a"; G = "#f8f8fc"; IRIS = "#46c8e8"; PUP = "#202436"
RIM = "#b8c8d8"; LENS = "#e8b030"; LENSH = "#f8e080"
GOLD = "#f0c040"; GOLDD = "#c09020"
SH = "#e8ecf4"; PINK = "#f0a98e"; LIP = "#b8404a"
SKYIDS = set(range(1, 17))  # palette ids 1..16 are the sky ramp/clouds

# ---------------- coat (back layer) ----------------
c.poly([(24, 37), (38, 37), (46, 41), (52, 52), (52, 64), (10, 64), (10, 50), (16, 41)], NAVY)
c.ellipse(16, 52, 9, 11, NAVY)     # left shoulder
c.ellipse(47, 50, 9, 10, NAVY)     # right shoulder
for p in [(13, 43), (14, 42), (15, 41), (16, 41), (17, 42), (18, 43), (12, 45), (11, 47)]:
    c.set(p[0], p[1], NAVYHI)
c.ellipse(49, 54, 6, 7, NAVYD)
c.poly([(26, 37), (35, 37), (39, 46), (33, 52), (24, 47)], SH)  # shirt

# ---------------- hair mass (wind-swept) ----------------
c.ellipse(31, 16, 13, 12, HAIR)
for (a, b, r) in [(16,11,2),(13,9,2),(10,10,2),(8,13,2),(14,14,4),(11,16,3),(40,14,4),(42,13,3),(8,23,2),(10,20,2),(14,19,2),(18,20,2),(9,17,2),(43,16,2),(7,21,1),(5,22,1),(6,24,1),(12,13,2)]:
    c.circle(a, b, r, HAIR)
for (a, b) in [(14,11),(11,13),(9,15),(12,20),(44,12),(45,14)]:
    c.circle(a, b, 1, HAIR)
for (a, b) in [(15,10),(13,9),(11,19),(29,5),(31,4),(33,6),(24,7),(41,11),(42,10)]:
    c.set(a, b, HAIRHI)

# ---------------- goggles ----------------
c.rect(18, 7, 26, 3, BR)
for a, b in [(44, 9), (45, 10), (46, 12), (47, 13), (48, 15)]:
    c.set(a, b, BR)
for xc in (29, 36):
    c.circle(xc, 10, 2, LENS)
    c.circle(xc, 10, 3, RIM, fill=False)
    c.set(xc - 1, 8, LENSH); c.set(xc, 8, LENSH)
    c.set(xc, 11, LENSH)

# ---------------- neck + face ----------------
c.rect(27, 32, 10, 7, SKIN)
c.rect(32, 33, 3, 5, SKSH)
c.ellipse(31, 22, 9, 10, SKIN)
c.ellipse(37, 22, 4, 9, SKSH)
c.rect(22, 14, 2, 13, HAIR)          # left side lock
c.set(23, 27, HAIR); c.set(22, 29, HAIR)
# right hair volume hugging the face (drawn after face so it covers the cheek edge)
for (a, b, r) in [(46,20,3),(44,23,3),(48,22,2),(46,25,2),(44,28,2),(42,30,2),(41,32,2),(43,27,2),(45,14,2),(47,16,2)]:
    c.circle(a, b, r, HAIR)
c.set(19, 10, HAIR); c.set(20, 10, HAIR)
# left lower hair volume: filled swept mass beside the jaw
c.poly([(6,18),(12,17),(21,19),(21,28),(17,32),(11,31),(7,26),(5,22)], HAIR)
for (a, b) in [(9,20),(14,21),(16,24),(12,27),(7,24),(19,26)]:
    c.set(a, b, HAIRHI)
# fill jaw peephole right of neck
for (a, b) in [(37,32),(38,32),(37,33),(38,33),(36,31),(38,31)]:
    c.set(a, b, SKIN)
# fill hair beside left jaw (chin area) and small top notch
for a in range(18, 27):
    for b in range(26, 34):
        if c.get(a, b) in SKYIDS:
            c.set(a, b, HAIR)
c.set(17, 18, HAIR)
c.rect(39, 14, 3, 13, HAIR)          # right side lock
c.set(39, 26, HAIR); c.set(40, 28, HAIR); c.set(41, 30, HAIR)

# ---------------- bangs over forehead ----------------
for xc in (26, 30, 34):
    c.ellipse(xc, 15, 3, 3, HAIR)
    c.poly([(xc - 2, 16), (xc + 2, 16), (xc, 19)], HAIR)
for a, b in [(27, 15), (28, 14), (31, 14), (32, 13), (35, 15), (36, 14), (26, 13)]:
    c.set(a, b, HAIRHI)

# ---------------- face features ----------------
for a, b in [(24, 21), (25, 20), (26, 20), (27, 21)]:
    c.set(a, b, HAIRD)
for a, b in [(34, 20), (35, 20), (36, 21), (37, 22)]:
    c.set(a, b, HAIRD)
def anime_eye(x0, y0):
    for x in range(x0, x0 + 6):
        c.set(x, y0, EYEL)
    for x in (x0, x0 + 5):
        c.set(x, y0 + 1, EYEL); c.set(x, y0 + 2, EYEL); c.set(x, y0 + 3, EYEL); c.set(x, y0 + 4, EYEL)
    for x in range(x0 + 1, x0 + 5):
        c.set(x, y0 + 1, IRIS)
    for x in range(x0 + 1, x0 + 4):
        c.set(x, y0 + 2, IRIS); c.set(x, y0 + 3, IRIS)
    c.set(x0 + 2, y0 + 2, PUP)
    c.set(x0 + 1, y0 + 1, G); c.set(x0 + 3, y0 + 3, G)
anime_eye(25, 22)
anime_eye(34, 22)
c.set(29, 28, SKSH); c.set(30, 29, SKSH); c.set(31, 29, SKSH)
# confident smirk (corners up)
for a, b in [(29, 30), (30, 31), (31, 31), (32, 31), (33, 31), (34, 30)]:
    c.set(a, b, LIP)
for a, b in [(26, 28), (27, 28), (35, 28), (36, 28), (25, 29), (36, 29)]:
    c.set(a, b, PINK)

# ---------------- scarf ----------------
c.poly([(21, 34), (40, 34), (41, 37), (38, 40), (24, 40), (20, 37)], RED)
c.rect(22, 39, 17, 2, REDD)
for a, b in [(23, 35), (27, 35), (31, 35), (35, 35), (37, 36)]:
    c.set(a, b, REDHI)
c.poly([(20, 41), (16, 44), (12, 43), (8, 45), (5, 44), (3, 47), (6, 50), (9, 47), (13, 46), (17, 47), (20, 45)], RED)
c.set(14, 36, REDD); c.set(10, 37, REDD); c.set(18, 35, REDHI); c.set(8, 45, REDHI); c.set(5, 46, REDHI)
c.poly([(17, 47), (14, 50), (11, 51), (9, 53), (10, 55), (12, 52), (15, 52), (18, 50)], REDD)

# ---------------- coat details ----------------
c.rect(10, 60, 44, 4, NAVYD)
c.line(24, 38, 22, 46, NAVYD)
c.line(37, 38, 39, 46, NAVYD)
c.set(23, 44, GOLD); c.set(23, 48, GOLD); c.set(21, 53, GOLD)
c.line(13, 50, 36, 54, BR)
c.line(12, 51, 35, 55, BR)
c.rect(34, 50, 3, 2, GOLD)
c.set(35, 51, NAVYD)
for a, b in [(50, 44), (51, 46), (52, 48), (51, 50)]:
    c.set(a, b, NAVYHI)

# ---------------- wind dashes ----------------
c.set(4, 18, "#ffffff"); c.set(6, 19, "#ffffff"); c.set(3, 26, "#ffffff"); c.set(5, 30, "#ffffff"); c.set(7, 31, "#ffffff")

print(c.stats_text())
print(c.matrix_text(region=(16, 18, 50, 36)))
finish(c)

