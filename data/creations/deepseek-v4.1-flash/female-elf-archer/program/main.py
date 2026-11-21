W = H = 64

bg = new_canvas(W, H, background="#0e1a20", name="bg")


def K(h, n=None):
    return bg.color(h, n)


# ---------------- palette ----------------
BG0 = K("#0e1a20", "bg0")
BG1 = K("#16262b", "bg1")
BG2 = K("#1e3234", "bg2")
BG3 = K("#26423a", "bg3")
BG4 = K("#305043", "bg4")

SKIN = K("#f0cba6", "skin")
SKIN_H = K("#ffe0c2", "skin_h")
SKIN_S = K("#d6a37d", "skin_s")
SKIN_D = K("#b17f5e", "skin_d")

HAIR_D = K("#173d26", "hair_d")
HAIR_M = K("#29663a", "hair_m")
HAIR_L = K("#3f8b4b", "hair_l")
HAIR_H = K("#69b972", "hair_h")

TUN = K("#a6cf87", "tun")
TUN_H = K("#cbe7af", "tun_h")
TUN_S = K("#7dab64", "tun_s")
TUN_D = K("#578549", "tun_d")
TUN_L = K("#3a6339", "tun_l")

LEA = K("#6b4a2f", "lea")
LEA_H = K("#90683f", "lea_h")
LEA_D = K("#412b1a", "lea_d")
BRASS = K("#d9b45c", "brass")

WOOD = K("#b99660", "wood")
FEATH = K("#e9e3c6", "feath")
FEATH_D = K("#a3b184", "feath_d")

EYE_W = K("#f4f6ea", "eye_w")
IRIS = K("#3f9463", "iris")
PUP = K("#0d1f18", "pup")
LIP = K("#c4746a", "lip")
BROW = K("#20452a", "brow")
DARK = K("#0a1512", "dark")
STRING = K("#c9cdb4", "string")

# ---------------- background ----------------
bg.rect(0, 0, W, H, BG0)
bg.ellipse(31, 28, 30, 28, BG1)
bg.ellipse(31, 24, 23, 21, BG2)
bg.ellipse(31, 22, 16, 15, BG3)
bg.ellipse(30, 20, 10, 10, BG4)


def quad(p0, p1, p2, n=16):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * t * (1 - t) * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * t * (1 - t) * p1[1] + t * t * p2[1]
        pts.append((int(round(x)), int(round(y))))
    return pts


# ---------------- bow (own layer, behind all, no outline) ----------------
bow = new_canvas(W, H, name="bow")
bouter = quad((50, 3), (63, 23), (50, 43))
binner = quad((50, 43), (56, 23), (50, 3))
bow.poly(bouter + binner, LEA)
for (x, y) in binner[1:-1]:
    bow.set(x, y, LEA_H)
for (x, y) in bouter[2:-2]:
    bow.set(x - 1, y, LEA_D)
bow.line(50, 4, 50, 42, STRING)
bow.set(50, 3, LEA_H)
bow.set(50, 43, LEA_H)

# ---------------- character layer ----------------
ch = new_canvas(W, H, name="char")

# ============ arrows ============
for (x0, y0, x1, y1) in ((19, 52, 5, 29), (22, 52, 10, 20), (24, 52, 14, 26)):
    ch.line(x0, y0, x1, y1, WOOD)
    ch.line(x0 + 1, y0, x1 + 1, y1, WOOD)
    ch.line(x0 + 2, y0, x1 + 2, y1, LEA_D)


def fletch(x, y):
    ch.set(x, y, FEATH)
    for dx in (-1, 0, 1):
        ch.set(x + dx, y + 1, FEATH)
    for dx in (-2, -1, 0, 1, 2):
        ch.set(x + dx, y + 2, FEATH if abs(dx) != 1 else FEATH_D)
    for dx in (-2, -1, 0, 1, 2):
        ch.set(x + dx, y + 3, FEATH)
    ch.set(x - 1, y + 4, FEATH_D)
    ch.set(x, y + 4, FEATH)
    ch.set(x + 1, y + 4, FEATH_D)


for (x, y) in ((5, 29), (10, 20), (14, 26)):
    fletch(x, y)

# ============ back hair ============
ch.ellipse(31, 18, 12, 12, HAIR_D)
ch.poly([(20, 14), (16, 22), (14, 32), (13, 42), (13, 51), (16, 57), (20, 54),
         (22, 46), (22, 34), (21, 22)], HAIR_D)
ch.poly([(42, 14), (46, 22), (47, 32), (48, 42), (48, 51), (45, 57), (41, 54),
         (40, 46), (40, 34), (41, 22)], HAIR_D)
ch.poly([(19, 18), (16, 26), (15, 36), (15, 46), (16, 52), (19, 54), (20, 45),
         (20, 34), (20, 24)], HAIR_M)
ch.poly([(43, 18), (45, 26), (46, 36), (46, 46), (45, 52), (42, 54), (41, 45),
         (41, 34), (41, 24)], HAIR_M)
ch.line(17, 26, 15, 44, HAIR_D)
ch.line(44, 26, 46, 44, HAIR_D)
ch.line(18, 30, 17, 40, HAIR_L)
ch.line(44, 30, 45, 40, HAIR_L)
ch.line(19, 46, 18, 52, HAIR_L)
ch.line(43, 46, 44, 52, HAIR_L)
ch.line(15, 26, 14, 40, HAIR_L)
ch.line(16, 31, 15, 44, HAIR_D)
ch.line(46, 26, 47, 40, HAIR_L)
ch.line(45, 31, 46, 44, HAIR_D)
ch.set(14, 34, HAIR_H)
ch.set(47, 34, HAIR_H)
ch.set(16, 48, HAIR_L)
ch.set(45, 48, HAIR_L)

# ============ front hair cap ============
ch.ellipse(31, 17, 10, 10, HAIR_M)
ch.path("M23 16 Q26 8 35 8", HAIR_L, fill=False)
ch.path("M24 17 Q28 10 36 10", HAIR_L, fill=False)
ch.path("M28 9 Q34 8 38 11", HAIR_H, fill=False)
ch.set(26, 9, HAIR_H)
ch.set(27, 8, HAIR_H)
ch.set(32, 7, HAIR_H)
ch.set(37, 12, HAIR_L)

# ============ neck / chest skin ============
ch.poly([(25, 28), (38, 28), (38, 41), (25, 41)], SKIN)
ch.poly([(26, 28), (38, 28), (37, 33), (27, 33)], SKIN_S)   # under-jaw shadow
ch.rect(34, 30, 4, 11, SKIN_S)                              # side shadow
ch.rect(28, 32, 6, 2, SKIN)

# ============ torso / tunic ============
body = [(8, 64), (8, 56), (10, 49), (13, 43), (17, 39), (21, 37), (25, 36),
        (29, 35), (33, 35), (37, 36), (41, 38), (45, 41), (48, 45), (49, 53),
        (49, 64)]
ch.poly(body, TUN)

# shadow side (viewer right)
ch.poly([(33, 35), (37, 36), (41, 38), (45, 41), (48, 45), (49, 53), (49, 64),
         (36, 64), (34, 52), (33, 43)], TUN_S)
ch.poly([(43, 44), (48, 46), (49, 53), (49, 64), (44, 64), (43, 53)], TUN_D)
# lit shoulder (viewer left)
ch.poly([(9, 56), (11, 48), (14, 43), (18, 39), (22, 37), (26, 36), (28, 40),
         (23, 41), (19, 44), (16, 48), (13, 56)], TUN_H)

# V-neck opening
ch.poly([(27, 35), (36, 35), (34, 41), (31, 44), (28, 39)], SKIN)
ch.poly([(29, 35), (35, 35), (33, 40), (31, 42), (29, 38)], SKIN_S)
ch.line(27, 35, 31, 44, TUN_H)
ch.line(36, 35, 32, 43, TUN_H)
ch.line(26, 36, 30, 45, TUN_D)
ch.line(37, 36, 33, 44, TUN_D)

# fabric folds
ch.line(19, 46, 16, 63, TUN_S)
ch.line(20, 46, 17, 63, TUN)
ch.line(41, 47, 43, 63, TUN_D)
ch.line(14, 53, 13, 63, TUN_H)
ch.line(11, 58, 11, 63, TUN_S)
ch.line(24, 51, 23, 63, TUN_S)
# hair shadow cast on the tunic
ch.line(25, 40, 25, 50, TUN_S)
ch.line(37, 40, 37, 48, TUN_D)

# quiver strap
ch.line(16, 40, 44, 63, LEA)
ch.line(17, 40, 45, 63, LEA_H)
ch.line(15, 40, 43, 63, LEA_D)
ch.rect(33, 55, 4, 4, LEA)
ch.rect(34, 56, 2, 2, BRASS)

# ============ face ============
ch.ellipse(31, 22, 9, 9, SKIN)          # x22..40 y13..31
ch.rect(38, 14, 2, 15, SKIN_S)
ch.set(37, 24, SKIN_S)
ch.set(37, 25, SKIN_S)
ch.ellipse(31, 32, 6, 1, SKIN_S)        # jaw shadow
ch.ellipse(25, 20, 4, 4, SKIN_H)        # lit cheek
ch.rect(25, 14, 8, 2, SKIN_H)           # forehead highlight

# ============ bangs ============
ch.poly([(21, 12), (27, 11), (26, 17), (22, 17)], HAIR_M)
ch.poly([(26, 11), (31, 10), (31, 16), (26, 17)], HAIR_M)
ch.poly([(30, 10), (35, 11), (35, 16), (30, 16)], HAIR_M)
ch.poly([(34, 11), (41, 13), (40, 19), (35, 17)], HAIR_M)
ch.line(26, 12, 25, 16, HAIR_D)
ch.line(31, 10, 31, 15, HAIR_D)
ch.line(35, 11, 35, 16, HAIR_D)
ch.set(24, 13, HAIR_H)
ch.set(28, 12, HAIR_H)
ch.set(33, 12, HAIR_H)
ch.set(38, 14, HAIR_H)
ch.set(23, 15, HAIR_L)
ch.set(29, 14, HAIR_L)
ch.set(34, 14, HAIR_L)
for x in range(27, 36):
    ch.set(x, 17, SKIN_S)

# ============ side locks ============
ch.poly([(22, 12), (19, 22), (18, 32), (17, 42), (18, 50), (22, 52), (24, 45),
         (24, 34), (24, 22), (24, 14)], HAIR_M)
ch.poly([(40, 12), (42, 22), (43, 32), (44, 42), (43, 51), (40, 53), (38, 47),
         (38, 34), (38, 22), (38, 14)], HAIR_M)
ch.line(21, 14, 19, 30, HAIR_L)
ch.line(19, 31, 18, 46, HAIR_L)
ch.line(41, 15, 42, 30, HAIR_L)
ch.line(42, 31, 43, 46, HAIR_L)
ch.line(20, 33, 19, 40, HAIR_D)
ch.line(42, 34, 42, 42, HAIR_D)
ch.set(20, 40, HAIR_H)
ch.set(21, 41, HAIR_H)
ch.set(19, 26, HAIR_H)
ch.set(42, 36, HAIR_H)
ch.set(41, 38, HAIR_H)
ch.set(43, 24, HAIR_H)
ch.line(24, 16, 23, 34, HAIR_D)
ch.line(38, 16, 39, 34, HAIR_D)
ch.line(21, 46, 20, 51, HAIR_D)
ch.line(41, 46, 42, 51, HAIR_D)

# ============ ears ============
ch.poly([(38, 17), (40, 13), (43, 13), (41, 18), (38, 24)], SKIN)
ch.poly([(39, 18), (41, 14), (41, 18), (39, 22)], SKIN_S)
ch.line(38, 18, 38, 24, SKIN_D)
ch.set(42, 14, SKIN_H)
ch.poly([(24, 17), (22, 13), (19, 13), (21, 18), (24, 24)], SKIN)
ch.poly([(23, 18), (21, 14), (21, 18), (23, 22)], SKIN_S)
ch.line(24, 18, 24, 24, SKIN_D)
ch.set(20, 14, SKIN_H)

# ============ face features ============
for x in range(24, 29):
    ch.set(x, 18, BROW)
for x in range(32, 37):
    ch.set(x, 18, BROW)
ch.set(23, 19, BROW)
ch.set(37, 19, BROW)
for x in range(24, 29):
    ch.set(x, 20, DARK)
for x in range(32, 37):
    ch.set(x, 20, DARK)
ch.set(23, 20, DARK)
ch.set(37, 20, DARK)
for x in range(25, 28):
    ch.set(x, 21, IRIS)
    ch.set(x, 22, IRIS)
for x in range(33, 36):
    ch.set(x, 21, IRIS)
    ch.set(x, 22, IRIS)
for x in (24, 28, 32, 36):
    ch.set(x, 21, EYE_W)
    ch.set(x, 22, EYE_W)
ch.set(26, 22, PUP)
ch.set(34, 22, PUP)
for x in (25, 26, 27):
    ch.set(x, 23, SKIN_S)
for x in (33, 34, 35):
    ch.set(x, 23, SKIN_S)
# nose
ch.set(31, 20, SKIN_S)
ch.set(30, 21, SKIN_S)
ch.set(30, 22, SKIN_S)
ch.set(29, 23, SKIN_S)
ch.set(28, 24, SKIN_H)
ch.set(29, 24, SKIN_S)
ch.set(28, 25, SKIN_D)
ch.set(27, 25, SKIN_S)
ch.set(29, 25, SKIN_S)
# mouth
for x in range(28, 33):
    ch.set(x, 28, LIP)
ch.set(27, 28, SKIN_D)
ch.set(33, 28, SKIN_D)
ch.set(29, 29, SKIN_S)
ch.set(30, 29, SKIN_S)
ch.set(31, 29, SKIN_S)
ch.set(30, 31, SKIN_S)

# ============ outer outline (character only) ============
cw, chh, data = ch.to_rgba()


def op(x, y):
    if x < 0 or y < 0 or x >= W or y >= H:
        return False
    return data[(y * W + x) * 4 + 3] > 0


ol = new_canvas(W, H, name="outline")
for y in range(H):
    for x in range(W):
        if not op(x, y) and (op(x - 1, y) or op(x + 1, y) or op(x, y - 1) or op(x, y + 1)):
            ol.set(x, y, DARK)

out = flatten([bg, bow, ol, ch], name="portrait")
save("portrait", out)

print(out.stats_text())
for r in ((0, 0, 63, 21), (0, 22, 63, 43), (0, 44, 63, 63)):
    print(out.matrix_text(region=r))
finish(out)
