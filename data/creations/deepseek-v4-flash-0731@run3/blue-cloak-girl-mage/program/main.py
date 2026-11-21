from pixelbench_api import *

INK = (22, 20, 30)
SKIN = (255, 224, 200)
SKIN_SH = (236, 178, 142)
HAIR = (232, 176, 75)
HAIR_D = (196, 128, 50)
HAIR_L = (250, 216, 132)
CLOAK = (46, 60, 105)
CLOAK_D = (30, 40, 74)
CLOAK_L = (68, 88, 150)
CLOAK_H = (105, 128, 190)
EYE = (255, 168, 58)
EYE_D = (70, 48, 60)
MOUTH = (206, 110, 100)
BLUSH = (252, 178, 148)
BOOT = (242, 242, 242)
BOOT_S = (202, 202, 210)
BOOT_D = (148, 148, 160)
WOOD = (112, 72, 46)
WOOD_D = (72, 46, 30)
GOLD = (255, 192, 52)
GLOW = (255, 226, 124)
GLOW_F = (255, 214, 100)
CORE = (255, 252, 216)
BELT = (96, 62, 42)
BELT_D = (60, 40, 30)
SHADOW = (38, 40, 58)

c = new_canvas(64, 64)

# ---- ground shadow ----
c.ellipse(32, 59, 16, 2, SHADOW)

# ---- staff (behind character) ----
c.circle(48, 9, 7, GLOW_F)
c.circle(48, 9, 5, GLOW)
c.circle(48, 9, 3, GOLD)
c.circle(48, 9, 1, CORE)
c.rect(46, 13, 5, 2, GOLD)
c.rect(48, 15, 2, 43, WOOD)
c.rect(49, 15, 1, 43, WOOD_D)

# ---- robe ----
robe = [(24, 23), (40, 23), (43, 30), (45, 44), (44, 50), (38, 52), (26, 52), (20, 50), (19, 44), (21, 30)]
c.poly(robe, INK, fill=False)
c.poly(robe, CLOAK)
c.ellipse(25, 40, 4, 11, CLOAK_D)
c.ellipse(39, 40, 4, 11, CLOAK_L)
c.ellipse(42, 45, 3, 6, CLOAK_H)
c.rect(31, 28, 1, 22, CLOAK_D)
c.rect(33, 28, 1, 22, CLOAK_D)
c.line(20, 50, 44, 50, CLOAK_D)

# ---- belt ----
c.rect(23, 37, 18, 3, BELT)
c.rect(23, 37, 18, 1, BELT_D)
c.rect(30, 37, 4, 3, GOLD)
c.rect(31, 37, 2, 1, BELT_D)

# ---- hood behind head ----
c.ellipse(32, 25, 11, 8, CLOAK_D)

# ---- hair back ----
c.circle(32, 15, 9, HAIR)
c.circle(32, 15, 9, INK, fill=False)
c.rect(23, 17, 2, 13, HAIR)
c.rect(39, 17, 2, 13, HAIR)
c.rect(24, 28, 2, 2, HAIR)
c.rect(38, 28, 2, 2, HAIR)

# ---- face ----
c.circle(32, 16, 6, SKIN)
c.rect(30, 21, 5, 2, SKIN_SH)

# ---- bangs ----
c.ellipse(32, 14, 7, 5, HAIR)
for x in (26, 29, 32, 35, 37):
    c.set(x, 18, HAIR_D)
for x in (27, 30, 33, 36):
    c.set(x, 11, HAIR_L)
c.set(32, 9, HAIR_L)
c.set(24, 29, HAIR_D)
c.set(39, 29, HAIR_D)

# hair shine
for (x, y) in [(25, 10), (26, 11), (27, 12), (28, 13), (37, 9), (36, 12), (40, 14)]:
    c.set(x, y, HAIR_L)
c.set(25, 12, HAIR_D)
c.set(39, 12, HAIR_D)

# ---- face details ----
# eyes
c.rect(27, 16, 3, 2, INK)
c.set(28, 16, EYE)
c.set(28, 17, EYE_D)
c.rect(34, 16, 3, 2, INK)
c.set(35, 16, EYE)
c.set(35, 17, EYE_D)
# mouth + blush
c.rect(31, 20, 3, 1, MOUTH)
c.set(27, 18, BLUSH)
c.set(27, 19, BLUSH)
c.set(36, 18, BLUSH)
c.set(36, 19, BLUSH)

# ---- collar ----
c.rect(28, 23, 8, 2, INK)
c.rect(29, 23, 6, 1, CLOAK_L)

# ---- sleeves / arms ----
# left sleeve peeking at side
c.poly([(26, 30), (23, 26), (20, 27), (18, 31), (18, 38), (19, 40), (22, 40), (24, 37)], CLOAK)
c.rect(19, 38, 4, 3, INK)
c.rect(20, 39, 2, 2, SKIN)
# right sleeve to staff
c.poly([(38, 26), (41, 24), (44, 27), (46, 32), (44, 34), (41, 31)], CLOAK)
c.rect(44, 31, 5, 4, INK)
c.rect(45, 32, 3, 2, SKIN)
# cuff shade
c.set(41, 30, CLOAK_D)
c.set(42, 31, CLOAK_D)

# ---- boots ----
c.rect(24, 50, 7, 9, INK)
c.rect(25, 51, 5, 8, BOOT)
c.rect(28, 54, 2, 5, BOOT_S)
c.rect(25, 57, 5, 1, BOOT_D)
c.rect(34, 50, 7, 9, INK)
c.rect(35, 51, 5, 8, BOOT)
c.rect(38, 54, 2, 5, BOOT_S)
c.rect(35, 57, 5, 1, BOOT_D)

# ---- staff glow sparkles ----
c.set(42, 4, GLOW)
c.set(55, 5, GLOW)
c.set(57, 10, GLOW_F)
c.set(51, 3, CORE)
c.set(44, 7, GLOW)
c.set(48, 20, GLOW)

print(c.stats_text())
print(c.matrix_text(region=(22, 8, 46, 24)))
print(c.matrix_text(region=(16, 44, 54, 62)))

finish(c)

