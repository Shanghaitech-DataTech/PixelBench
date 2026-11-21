# Female Elf Archer - 64x64 RPG character sprite
# three-quarter view, standing, long green hair, bow + quiver on back

# ---------------- palette ----------------
OUT      = '#1c2418'
SKIN     = '#f2c9a2'
SKIN_SH  = '#d9a277'
SKIN_LT  = '#ffe3c6'
BLUSH    = '#e79a86'

HAIR_D   = '#22522c'
HAIR_M   = '#3b9147'
HAIR_L   = '#66c25e'
HAIR_H   = '#a9e78b'

CLOTH    = '#a9d97c'
CLOTH_SH = '#7fb259'
CLOTH_D  = '#548a41'
CLOTH_H  = '#d5efaa'

LEATHER  = '#8d5c33'
LEA_D    = '#5b3820'
LEA_L    = '#bb8854'
GOLD     = '#e2bb60'
GOLD_D   = '#96712f'

WOOD     = '#b87c40'
WOOD_D   = '#7c4d25'
WOOD_L   = '#d9a468'
SHAFT    = '#8a6134'
FLETCH   = '#eff2e6'
STRING   = '#cfc7ae'

EYE_W    = '#f6f9f3'
IRIS     = '#3fa26c'
IRIS_D   = '#1d5b3a'
PUPIL    = '#131b13'
LIP      = '#c96f68'
SHADOW   = '#33402f'

# ---------------- canvases ----------------
art = new_canvas(64, 64, name="art")
shd = new_canvas(64, 64, name="shadow")

shd.ellipse(27, 60, 14, 3, SHADOW)

# ================= 1. BOW (slung on back, behind everything) =================
art.path("M 44 12 C 61 20 62 43 47 57 L 49 55 C 58 42 57 21 46 14 Z",
         WOOD, fill=True)
art.path("M 46 14 C 57 21 58 42 49 55", WOOD_D, fill=False)
art.path("M 45 13 C 60 21 61 42 48 56", WOOD_L, fill=False)
# grip wrapping
for yy in (30, 32, 34):
    art.line(55, yy, 59, yy + 1, LEA_D)
# bow tips
art.set(44, 12, WOOD_D); art.set(45, 12, WOOD_D)
art.set(47, 57, WOOD_D); art.set(48, 57, WOOD_D)
# string
art.line(45, 13, 48, 56, STRING)

# ================= 2. QUIVER + ARROWS =================
art.poly([(38, 20), (46, 25), (35, 47), (27, 42)], LEA_D)
art.poly([(39, 21), (45, 25), (41, 33), (35, 29)], LEATHER)
art.line(38, 19, 46, 24, LEA_L)
art.line(31, 40, 37, 44, LEA_L)

def arrow(x0, y0, x1, y1, fx, fy):
    art.line(x0, y0, x1, y1, SHAFT)
    art.poly([(fx, fy - 3), (fx + 2, fy), (fx, fy + 3), (fx - 2, fy)], FLETCH)

arrow(40, 20, 42, 8, 42, 6)
arrow(42, 21, 48, 10, 48, 8)

# ================= 3. BACK HAIR =================
art.path(
    "M 26 3 C 34 3 39 8 40 16 C 41 26 42 38 40 48 C 39 52 34 53 33 48 "
    "C 35 39 35 30 33 24 L 19 24 C 17 32 17 41 19 48 C 18 53 12 52 11 47 "
    "C 9 36 11 21 15 13 C 18 6 21 3 26 3 Z", HAIR_M, fill=True)
# inner shading strands
art.line(38, 26, 37, 44, HAIR_D)
art.line(39, 30, 39, 42, HAIR_D)
art.line(13, 26, 14, 42, HAIR_D)
art.line(12, 32, 12, 40, HAIR_D)
art.line(35, 28, 35, 40, HAIR_L)
art.line(16, 28, 16, 40, HAIR_L)

# left side lock (behind torso/arm)
art.path("M 18 15 C 14 22 13 31 15 39 C 16 43 19 44 20 40 C 18 33 18 24 20 18 Z",
         HAIR_M, fill=True)
art.line(16, 22, 16, 36, HAIR_L)

# ================= 4. LEGS + BOOTS =================
# back leg (image right)
art.poly([(28, 44), (35, 44), (35, 56), (29, 56)], CLOTH_D)
art.poly([(27, 52), (36, 52), (36, 58), (34, 60), (27, 60), (27, 56)], LEA_D)
art.line(28, 53, 35, 53, LEATHER)
# front leg (image left)
art.poly([(20, 44), (27, 44), (27, 57), (21, 57)], CLOTH_SH)
art.line(22, 46, 22, 55, CLOTH_D)
art.poly([(19, 51), (28, 51), (28, 58), (26, 61), (16, 61), (16, 57), (18, 54)],
         LEATHER)
art.poly([(16, 59), (28, 59), (28, 61), (16, 61)], LEA_D)
art.line(19, 52, 27, 52, LEA_L)

# ================= 5. TORSO =================
# neck
art.rect(24, 24, 6, 5, SKIN_SH)
art.rect(24, 24, 6, 2, '#c08c62')

# far arm (image right, behind torso)
art.poly([(31, 29), (37, 31), (38, 40), (35, 45), (31, 44)], CLOTH_D)
art.poly([(33, 44), (38, 44), (38, 51), (36, 53), (33, 52)], SKIN_SH)
art.line(34, 51, 37, 51, '#c08c62')

# tunic body
art.path("M 21 27 L 32 27 C 36 28 38 31 38 35 L 37 43 L 17 43 L 16 35 "
         "C 16 31 18 28 21 27 Z", CLOTH, fill=True)
art.path("M 32 27 C 36 28 38 31 38 35 L 37 43 L 31 43 Z", CLOTH_SH, fill=True)
art.path("M 34 30 C 37 32 38 34 38 36 L 37 43 L 34 43 Z", CLOTH_D, fill=True)
art.line(19, 30, 18, 40, CLOTH_H)
# neckline
art.poly([(23, 27), (30, 27), (27, 30)], CLOTH_D)
# seam between near arm and torso
art.line(21, 30, 21, 43, CLOTH_D)

# skirt / tunic tails
art.poly([(16, 41), (37, 41), (39, 49), (33, 51), (28, 49), (23, 51), (17, 49)],
         CLOTH)
art.poly([(28, 41), (37, 41), (39, 49), (33, 51), (28, 49)], CLOTH_SH)
art.line(16, 42, 38, 42, CLOTH_H)
art.poly([(17, 48), (39, 48), (39, 49), (33, 51), (28, 49), (23, 51), (17, 49)],
         CLOTH_D)

# belt
art.rect(16, 39, 22, 3, LEATHER)
art.rect(16, 39, 22, 1, LEA_L)
art.rect(16, 41, 22, 1, LEA_D)
art.rect(24, 38, 5, 5, GOLD)
art.rect(25, 39, 3, 3, GOLD_D)
art.rect(26, 40, 1, 1, GOLD)

# quiver strap across chest
art.line(32, 28, 21, 39, LEATHER)
art.line(33, 28, 22, 39, LEA_D)
art.line(32, 29, 22, 38, LEA_L)

# near arm (image left, in front)
art.path("M 17 29 C 14 31 13 36 14 41 L 16 46 L 21 45 L 20 38 L 21 31 Z",
         CLOTH, fill=True)
art.path("M 14 41 L 16 46 L 21 45 L 20 40 Z", CLOTH_SH, fill=True)
# bracer
art.poly([(14, 40), (21, 39), (21, 45), (15, 46)], LEATHER)
art.line(14, 41, 21, 40, LEA_L)
art.line(15, 45, 21, 44, LEA_D)
# hand
art.poly([(15, 45), (21, 45), (21, 50), (17, 51), (15, 49)], SKIN)
art.line(16, 49, 20, 49, SKIN_SH)

# ================= 6. HEAD =================
# skull
art.ellipse(27, 16, 8, 8, SKIN)
art.poly([(20, 18), (34, 18), (32, 24), (29, 27), (25, 27), (21, 23)], SKIN)
# jaw / cheek shading (right side = away from light)
art.poly([(31, 18), (34, 18), (32, 24), (29, 27), (28, 26), (31, 22)], SKIN_SH)
art.line(33, 14, 34, 20, SKIN_SH)
# forehead highlight
art.line(22, 12, 26, 11, SKIN_LT)

# ---- face ----
# eyes (wide gap between them)
art.rect(20, 17, 5, 3, EYE_W)
art.rect(28, 17, 5, 3, EYE_W)
art.rect(21, 17, 3, 3, IRIS)
art.rect(29, 17, 3, 3, IRIS)
art.rect(21, 17, 1, 3, IRIS_D)
art.rect(29, 17, 1, 3, IRIS_D)
art.set(22, 18, PUPIL); art.set(30, 18, PUPIL)
art.set(23, 17, EYE_W); art.set(31, 17, EYE_W)
# lids / lashes
art.line(19, 16, 24, 16, OUT)
art.line(27, 16, 32, 16, OUT)
art.set(19, 17, OUT); art.set(32, 18, OUT)
# brows
art.line(19, 15, 24, 14, HAIR_D)
art.line(27, 14, 32, 15, HAIR_D)
# nose
art.set(19, 21, SKIN_SH); art.set(20, 22, SKIN_SH)
art.set(19, 22, '#c08c62')
# mouth
art.line(22, 24, 23, 24, LIP)
art.set(24, 24, SKIN_SH)
# blush
art.set(21, 22, BLUSH); art.set(27, 22, BLUSH)

# ================= 7. FRONT HAIR =================
art.path(
    "M 18 17 C 16 9 21 3 27 3 C 34 3 39 8 38 17 L 36 10 L 34 13 L 31 9 "
    "L 28 13 L 25 9 L 22 13 L 20 10 Z", HAIR_M, fill=True)
# hair cap volume
art.path("M 18 15 C 17 8 22 3 27 3 C 33 3 38 7 38 15 C 36 9 32 6 27 6 "
         "C 22 6 19 9 18 15 Z", HAIR_L, fill=True)
art.path("M 20 9 C 22 5 24 4 27 4 C 31 4 34 6 35 9 C 33 7 30 6 27 6 "
         "C 24 6 22 7 20 9 Z", HAIR_H, fill=True)
# lock on the right side of the face, over the shoulder
art.path("M 38 15 C 40 21 40 29 38 36 C 37 39 34 39 34 36 C 36 29 36 21 35 16 Z",
         HAIR_M, fill=True)
art.path("M 38 15 C 40 21 40 29 38 36 C 38 37 37 38 37 38 C 39 29 39 21 36 16 Z",
         HAIR_D, fill=True)
art.line(36, 19, 36, 31, HAIR_L)

# small circlet
art.line(19, 11, 24, 9, GOLD)
art.set(21, 10, GOLD_D)

# ear (pointed, up-right) drawn after hair so it reads over the lock
art.poly([(33, 17), (37, 15), (42, 12), (39, 17), (37, 20), (35, 22), (33, 20)],
         SKIN)
art.poly([(36, 16), (40, 13), (38, 17), (36, 19), (35, 20)], SKIN_SH)
art.line(37, 17, 39, 14, '#c08c62')
art.line(34, 20, 36, 21, SKIN_SH)

# ================= 8. OUTLINE + FLATTEN =================
def outline_layer(src, colour):
    w, h, rgba = src.to_rgba()
    m = [[rgba[4 * (y * w + x) + 3] > 0 for x in range(w)] for y in range(h)]
    base = new_canvas(w, h, name="outline_layer")
    offs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for y in range(h):
        for x in range(w):
            if m[y][x]:
                continue
            for dx, dy in offs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and m[ny][nx]:
                    base.set(x, y, colour)
                    break
    return base

ol = outline_layer(art, OUT)
result = flatten([shd, ol, art], name="elf_archer")

print(result.stats_text())
view(result)
save("elf_archer", result, indexed=True)
finish(result)
