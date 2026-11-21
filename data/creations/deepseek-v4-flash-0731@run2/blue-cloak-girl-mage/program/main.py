from pixelbench_api import *

c = new_canvas(64, 64, name="blue_cloak_girl_mage")

# ---- palette ----
SKIN = (244, 207, 180)
SKIN_SH = (222, 178, 150)
HAIR = (172, 116, 64)
HAIR_DK = (128, 82, 46)
HAIR_LT = (198, 146, 92)
EYE = (38, 38, 62)
WHITE = (255, 255, 255)
BLUSH = (236, 156, 148)
MOUTH = (176, 96, 96)
CLOAK = (26, 40, 106)
CLOAK_DK = (13, 22, 68)
CLOAK_LT = (72, 94, 174)
SHIRT = (98, 124, 184)
CLOTH_DK = (76, 98, 158)
TRIM = (210, 170, 90)
BOOT = (240, 240, 246)
BOOT_DK = (176, 180, 200)
SOLE = (92, 96, 120)
WOOD = (104, 64, 38)
WOOD_DK = (62, 38, 22)
AMB = (255, 176, 44)
AMB_HI = (255, 228, 128)
AMB_DK = (212, 118, 24)
GLOW = (255, 216, 112)
OUT = (10, 12, 32)

# ---- staff (drawn first, behind) ----
c.rect(44, 7, 3, 50, WOOD)      # shaft x44-46, y7-56
c.rect(46, 7, 1, 50, WOOD_DK)   # right-side shade
c.rect(43, 24, 4, 2, TRIM)      # gold band
c.rect(43, 22, 4, 2, TRIM)
c.rect(43, 55, 4, 3, WOOD_DK)   # ferrule/foot

# ---- hair back ----
c.ellipse(26, 14, 11, 12, HAIR)  # x15-37, y2-25
c.rect(15, 13, 3, 10, HAIR)      # side volume x15-17
c.rect(36, 13, 3, 10, HAIR)      # side volume x36-38
c.rect(15, 17, 1, 6, HAIR_DK)
c.rect(37, 17, 1, 6, HAIR_DK)

# ---- face ----
c.ellipse(26, 16, 8, 9, SKIN)    # x18-34, y7-24
c.rect(23, 23, 7, 5, SKIN_SH)    # neck x23-29, y23-27

# bangs
c.rect(18, 7, 17, 5, HAIR)       # forehead cap x18-34, y7-11
c.poly([(19, 11), (22, 17), (25, 11)], HAIR)
c.poly([(24, 11), (26, 15), (28, 11)], HAIR)
c.poly([(27, 11), (30, 17), (33, 11)], HAIR)
c.set(19, 3, HAIR_LT)
c.set(20, 3, HAIR_LT)
c.set(21, 3, HAIR_LT)
c.set(22, 3, HAIR_LT)
c.set(23, 4, HAIR_LT)

# eyes
c.rect(21, 13, 3, 4, EYE)
c.rect(28, 13, 3, 4, EYE)
c.set(21, 13, WHITE)
c.set(28, 13, WHITE)
c.set(22, 15, AMB)
c.set(29, 15, AMB)

# cheeks + mouth
c.set(19, 17, BLUSH)
c.set(20, 17, BLUSH)
c.set(32, 17, BLUSH)
c.set(33, 17, BLUSH)
c.rect(24, 20, 5, 1, MOUTH)

# hair highlights + chin shadow
c.set(34, 3, HAIR_LT)
c.set(33, 4, HAIR_LT)
c.set(35, 6, HAIR_LT)
c.set(20, 23, HAIR_DK)
c.set(22, 24, HAIR_DK)
c.set(28, 24, HAIR_DK)
c.set(30, 23, HAIR_DK)

# ---- robe ----
c.poly([(17, 27), (12, 45), (13, 50), (39, 50), (40, 45), (35, 27)], CLOAK)
c.poly([(21, 29), (19, 42), (21, 46), (31, 46), (33, 42), (31, 29)], SHIRT)
c.line(25, 32, 23, 44, CLOTH_DK)
c.line(27, 32, 29, 44, CLOTH_DK)
c.poly([(17, 27), (12, 45), (13, 50), (15, 50), (14, 45), (19, 27)], CLOAK_DK)
c.poly([(35, 27), (40, 45), (39, 50), (37, 50), (38, 45), (33, 27)], CLOAK_LT)
c.rect(15, 34, 23, 2, TRIM)      # belt
c.rect(23, 33, 7, 3, AMB)        # gold buckle
c.rect(13, 49, 27, 2, TRIM)      # hem trim

# ---- boots ----
c.rect(18, 46, 8, 12, BOOT)      # left boot x18-25, y46-57
c.rect(18, 46, 8, 2, BOOT_DK)
c.rect(18, 56, 8, 2, SOLE)
c.rect(27, 46, 8, 12, BOOT)      # right boot x27-34
c.rect(27, 46, 8, 2, BOOT_DK)
c.rect(27, 56, 8, 2, SOLE)

# ---- sleeve (right arm to staff) ----
c.ellipse(36, 38, 8, 7, CLOAK)   # sleeve x28-44, y31-44
c.rect(37, 32, 2, 8, CLOAK_LT)
c.rect(42, 38, 2, 6, CLOAK_DK)
# hand grasping staff (col 44-46)
c.rect(43, 39, 4, 5, SKIN)        # fist x43-46, y39-43
c.rect(43, 38, 4, 4, SKIN_SH)     # top of fist shade
c.rect(40, 41, 2, 2, SKIN)        # forearm bridge
c.set(43, 39, SKIN_SH)
c.set(46, 39, SKIN_SH)
c.set(43, 43, SKIN_SH)
c.set(46, 43, SKIN_SH)
c.rect(44, 42, 3, 2, WOOD_DK)     # fingers over shaft

# ---- silhouette outline ----
c.outline(OUT)

# ---- redraw glowing orb (keeps it bright on top) ----
c.circle(45, 6, 5, GLOW)
c.circle(45, 6, 4, AMB)
c.circle(45, 6, 2, AMB_HI)
c.set(45, 6, (255, 250, 215))
c.set(44, 5, WHITE)
c.set(39, 1, GLOW)
c.set(51, 7, GLOW)
c.set(49, 13, GLOW)
c.set(38, 10, AMB_HI)
c.set(47, 3, (255, 250, 215))

print(c.stats_text())
finish(c)
