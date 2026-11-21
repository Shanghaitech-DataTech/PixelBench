
W = H = 64

# ---------------- palette ----------------
SKY_T   = "#c9ebf8"
SKY_M   = "#a6d8f1"
SKY_B   = "#84c4e7"
CLOUD   = "#eefaff"
CLOUD_S = "#cfe9f6"

OUT     = "#20182a"

SKIN_L  = "#ffe8cb"
SKIN    = "#f8cda2"
SKIN_S  = "#dca578"
SKIN_D  = "#b57a5b"
BLUSH   = "#ef9f86"

HAIR_D  = "#4e2718"
HAIR    = "#8a4423"
HAIR_M  = "#b76a31"
HAIR_L  = "#e0a455"

NAVY_D  = "#131b32"
NAVY    = "#243357"
NAVY_L  = "#3c5281"
GOLD    = "#efc75e"
GOLD_D  = "#a87d2a"

RED_D   = "#881e29"
RED     = "#c53540"
RED_L   = "#e3645c"

GG_D    = "#272430"
GG      = "#4b4553"
GG_L    = "#6d6678"
GLASS_D = "#3a86a0"
GLASS   = "#6fc9de"
GLASS_L = "#d5f5fb"

IRIS_D  = "#17537a"
IRIS    = "#3ba0d2"
IRIS_L  = "#a7e7f8"
EYE_W   = "#f7fbff"
LASH    = "#2f1d29"
MOUTH   = "#a04a4a"

SHIRT   = "#f0e5cf"
SHIRT_S = "#c9b79a"
BELT    = "#5a3a25"

# ---------------- background ----------------
sky = new_canvas(W, H, SKY_T, name="sky")
sky.rect(0, 26, W, 20, SKY_M)
sky.rect(0, 46, W, 18, SKY_B)
sky.dither(0, 23, W, 4, [SKY_T, SKY_M], pattern="bayer4")
sky.dither(0, 44, W, 4, [SKY_M, SKY_B], pattern="bayer4")
sky.ellipse(8, 12, 7, 2, CLOUD)
sky.ellipse(13, 10, 4, 1, CLOUD)
sky.ellipse(8, 14, 6, 0, CLOUD_S)
sky.ellipse(56, 36, 6, 2, CLOUD)
sky.ellipse(56, 38, 5, 0, CLOUD_S)
sky.ellipse(6, 52, 7, 2, CLOUD)
sky.ellipse(6, 54, 6, 0, CLOUD_S)

# ---------------- character ----------------
ch = new_canvas(W, H, name="girl")

# ===== back hair mass =====
ch.poly([(21, 9), (28, 6), (35, 8), (41, 13), (44, 20), (44, 28),
         (42, 35), (38, 41), (30, 43), (22, 41), (17, 34), (15, 22), (17, 13)], HAIR_D)
# wind-swept locks trailing right, with sky gaps between them
ch.path("M40 10 C49 7 57 9 62 14 C54 13 46 15 41 19 Z", HAIR)
ch.path("M41 12 C48 11 55 13 60 16 C53 16 46 18 42 20 Z", HAIR_D)
ch.path("M43 23 C51 22 58 25 62 30 C55 27 48 27 43 29 Z", HAIR)
ch.path("M44 26 C51 26 57 28 61 31 C55 29 48 29 44 30 Z", HAIR_D)
ch.path("M41 34 C48 36 54 39 58 45 C52 40 46 38 40 38 Z", HAIR)
# small wisp left, swept low so it does not read as an ear
ch.path("M16 26 C12 27 10 30 9 33 C12 29 14 29 17 29 Z", HAIR)
ch.path("M16 27 C13 28 11 30 10 32 C13 30 15 30 17 30 Z", HAIR_D)

# ===== neck =====
ch.rect(27, 36, 8, 9, SKIN_S)
ch.rect(28, 36, 6, 8, SKIN)
ch.rect(28, 37, 5, 3, SKIN_D)

# ===== coat / shoulders =====
ch.poly([(8, 63), (9, 55), (12, 49), (17, 45), (24, 43), (33, 43),
         (41, 45), (48, 49), (53, 55), (54, 63)], NAVY)
ch.poly([(8, 63), (9, 55), (12, 49), (17, 45), (22, 44), (17, 50),
         (13, 57), (12, 63)], NAVY_L)
ch.poly([(42, 46), (48, 49), (53, 55), (54, 63), (48, 63), (47, 54)], NAVY_D)
# shirt / inner
ch.poly([(28, 45), (35, 45), (35, 52), (32, 58), (28, 52)], SHIRT)
ch.poly([(32, 51), (35, 50), (35, 46), (33, 57)], SHIRT_S)
# lapels
ch.poly([(28, 44), (27, 57), (22, 51), (23, 46)], NAVY_L)
ch.poly([(35, 44), (37, 56), (41, 50), (40, 46)], NAVY)
ch.line(27, 47, 26, 56, GOLD_D)
ch.line(36, 47, 37, 55, GOLD_D)
# strap
ch.line(21, 51, 39, 62, BELT)
ch.line(22, 50, 40, 61, BELT)
ch.rect(31, 55, 3, 3, GOLD)
ch.set(32, 56, GOLD_D)
# epaulettes
ch.rect(13, 48, 5, 3, GOLD)
ch.rect(13, 50, 5, 1, GOLD_D)
ch.rect(45, 50, 5, 3, GOLD_D)
ch.rect(45, 50, 5, 1, GOLD)

# ===== scarf =====
ch.path("M38 39 C47 37 55 39 61 45 C53 44 46 46 39 46 Z", RED)
ch.path("M41 43 C48 42 54 43 60 46 C53 46 46 48 40 47 Z", RED_D)
ch.poly([(23, 40), (29, 38), (36, 39), (40, 42), (39, 46),
         (32, 48), (24, 47), (21, 44)], RED)
ch.poly([(23, 40), (29, 38), (33, 39), (29, 41), (23, 42), (21, 44)], RED_L)
ch.poly([(24, 47), (32, 48), (39, 46), (38, 48), (30, 50), (24, 49)], RED_D)

# ===== face =====
ch.ellipse(28, 24, 9, 10, SKIN)
ch.poly([(20, 28), (37, 28), (36, 33), (32, 38), (27, 38), (22, 34)], SKIN)
# light from the upper left
ch.poly([(19, 24), (23, 15), (29, 14), (25, 21), (22, 28), (20, 31)], SKIN_L)
ch.poly([(35, 17), (37, 22), (37, 29), (35, 34), (32, 37), (33, 28), (34, 21)], SKIN_S)
ch.poly([(27, 37), (32, 37), (35, 34), (31, 37), (28, 37)], SKIN_S)
# nose, mouth, blush
ch.set(19, 29, SKIN_L)
ch.set(19, 30, SKIN_S)
ch.set(20, 31, SKIN_S)
ch.set(21, 32, SKIN_S)
ch.line(22, 34, 25, 34, MOUTH)
ch.set(25, 33, MOUTH)
ch.set(23, 35, SKIN_S)
ch.set(24, 35, SKIN_S)
ch.line(21, 30, 21, 30, BLUSH)
ch.line(21, 29, 22, 29, BLUSH)
ch.line(32, 30, 34, 30, BLUSH)

# ===== eyes =====
# far eye (profile side, foreshortened)
ch.rect(20, 24, 4, 1, LASH)
ch.set(19, 25, LASH)
ch.rect(20, 25, 3, 1, IRIS_D); ch.set(23, 25, EYE_W)
ch.rect(20, 26, 2, 1, IRIS);   ch.set(22, 26, IRIS_L); ch.set(23, 26, EYE_W)
ch.set(20, 27, IRIS_L); ch.rect(21, 27, 2, 1, IRIS); ch.set(23, 27, EYE_W)
ch.rect(20, 28, 4, 1, SKIN_S)
ch.set(22, 25, GLASS_L)

# near eye
ch.rect(29, 24, 5, 1, LASH)
ch.set(34, 24, LASH); ch.set(34, 25, LASH)
ch.set(29, 25, EYE_W); ch.rect(30, 25, 3, 1, IRIS_D); ch.set(33, 25, EYE_W)
ch.set(29, 26, EYE_W); ch.rect(30, 26, 2, 1, IRIS); ch.set(32, 26, IRIS_L); ch.set(33, 26, EYE_W)
ch.set(29, 27, EYE_W); ch.set(30, 27, IRIS_L); ch.rect(31, 27, 2, 1, IRIS); ch.set(33, 27, EYE_W)
ch.rect(29, 28, 5, 1, SKIN_S)
ch.set(31, 25, GLASS_L)

# brows: confident, inner ends down
ch.line(19, 22, 22, 21, HAIR_D)
ch.line(29, 21, 33, 22, HAIR_D)
ch.set(34, 23, HAIR_D)

# ===== goggles pushed up on the forehead =====
ch.rect(26, 15, 4, 3, GG)
ch.rect(26, 16, 4, 1, GG_D)
ch.rect(37, 14, 5, 3, GG)
ch.rect(37, 15, 5, 1, GG_D)
ch.rect(17, 16, 3, 3, GG)
ch.rect(17, 17, 3, 1, GG_D)
# far lens
ch.ellipse(23, 16, 3, 3, GG)
ch.ellipse(23, 16, 2, 2, GLASS)
ch.ellipse(23, 16, 3, 3, GG_D, fill=False)
ch.set(22, 15, GLASS_L)
ch.rect(22, 18, 2, 1, GLASS_D)
# near lens
ch.circle(33, 16, 4, GG)
ch.circle(33, 16, 3, GLASS)
ch.circle(33, 16, 4, GG_D, fill=False)
ch.set(31, 14, GLASS_L)
ch.set(32, 13, GLASS_L)
ch.rect(31, 18, 4, 1, GLASS_D)
ch.set(30, 15, GG_L)
ch.set(36, 15, GG_L)

# ===== front bangs and side locks =====
ch.poly([(16, 15), (18, 9), (23, 6), (30, 5), (37, 8), (41, 12), (41, 15),
         (38, 11), (35, 13), (32, 9), (28, 12), (24, 9), (20, 12), (18, 16)], HAIR)
ch.poly([(19, 12), (23, 8), (29, 7), (26, 11), (21, 14)], HAIR_M)
ch.line(22, 8, 19, 14, HAIR_L)
ch.line(27, 7, 25, 11, HAIR_L)
ch.poly([(34, 8), (38, 11), (41, 15), (38, 12), (35, 14)], HAIR_D)
# left side lock, clear of the face
ch.poly([(17, 14), (18, 21), (18, 29), (16, 25), (15, 18)], HAIR)
ch.poly([(16, 18), (17, 24), (17, 29), (15, 24)], HAIR_D)
# right side lock
ch.poly([(41, 13), (43, 21), (42, 32), (39, 28), (38, 17)], HAIR)
ch.poly([(42, 19), (43, 26), (42, 32), (40, 27)], HAIR_D)
# strand falling over the near goggle rim
ch.line(36, 11, 38, 19, HAIR_M)
ch.line(37, 11, 39, 18, HAIR)
# hair highlights across the crown and the trailing locks
ch.line(24, 7, 30, 6, HAIR_M)
ch.line(31, 6, 35, 9, HAIR_M)
ch.set(26, 6, HAIR_L)
ch.set(28, 5, HAIR_L)
ch.line(44, 11, 50, 11, HAIR_M)
ch.line(46, 24, 52, 25, HAIR_M)
ch.line(44, 36, 49, 39, HAIR_M)
# earring under the near side lock
ch.set(38, 30, GOLD)
ch.set(38, 31, GOLD_D)

# ---------------- outline pass ----------------
def silhouette(src, color):
    out = new_canvas(W, H, name="sil")
    pal = {p["index"]: p["rgba"] for p in src.palette()}
    solid = set()
    for y in range(H):
        for x in range(W):
            rgba = pal.get(src.get(x, y))
            if rgba is not None and rgba[3] > 0:
                solid.add((x, y))
    for (x, y) in solid:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in solid:
                out.set(nx, ny, color)
    return out

sil = silhouette(ch, OUT)
result = flatten([sky, sil, ch], name="output")
print(result.stats_text())
view(result)
finish(result)
