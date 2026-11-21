from pixelbench_api import *

c = new_canvas(32, 32)

OUTLN = c.color((42, 42, 47), "outline")
HAT = c.color((244, 244, 244), "hat")
HAT_SH = c.color((192, 192, 192), "hat_sh")
SKIN = c.color((234, 186, 154), "skin")
SKIN_SH = c.color((212, 160, 126), "skin_sh")
HAIR = c.color((64, 48, 44), "hair")
WHITE = c.color((236, 236, 240), "white")
WHITE_SH = c.color((200, 200, 208), "white_sh")
APRON = c.color((226, 226, 234), "apron")
APRON_SH = c.color((184, 184, 196), "apron_sh")
CREAM = c.color((248, 244, 232), "cream")
STEAM = c.color((168, 118, 68), "steam")
STEAM_S = c.color((122, 82, 44), "steam_sh")
STEAM_L = c.color((198, 148, 94), "steam_light")
BUN = c.color((252, 248, 242), "bun")
BUN_SH = c.color((220, 206, 192), "bun_sh")
EYE = c.color((32, 32, 38), "eye")
MOUTH = c.color((122, 64, 54), "mouth")
STEAMW = c.color((228, 228, 234, 165), "steam_wisp")

# ============ HEAD ============
# Hat puffy top rows 1-8
# outline
for x in range(9, 23): c.set(x, 1, OUTLN)
c.set(8, 2, OUTLN); c.set(23, 2, OUTLN)
c.rect(8, 2, 1, 2, OUTLN); c.rect(23, 2, 1, 2, OUTLN)
c.set(7, 4, OUTLN); c.set(24, 4, OUTLN)
c.rect(7, 4, 1, 2, OUTLN); c.rect(24, 4, 1, 2, OUTLN)
c.set(8, 6, OUTLN); c.set(23, 6, OUTLN)
c.rect(8, 6, 1, 1, OUTLN); c.rect(23, 6, 1, 1, OUTLN)
c.set(9, 7, OUTLN); c.set(22, 7, OUTLN)

# hat fill
c.rect(10, 2, 12, 1, HAT)
c.rect(9, 3, 14, 1, HAT)
c.rect(8, 4, 16, 1, HAT)
c.rect(8, 5, 16, 1, HAT)
c.rect(9, 6, 14, 1, HAT)
# lump shading
for lx in (10, 13, 16, 19):
    c.set(lx, 5, HAT_SH)
    c.set(lx, 6, HAT_SH)

# hat band rows 7-9
c.rect(9, 7, 14, 3, HAT)
c.rect(9, 7, 14, 1, HAT_SH)
c.rect(9, 9, 14, 1, HAT_SH)
# band outline sides (short)
c.set(9, 7, OUTLN); c.set(22, 7, OUTLN)
c.set(9, 8, OUTLN); c.set(22, 8, OUTLN)
c.set(9, 9, OUTLN); c.set(22, 9, OUTLN)

# ============ FACE rows 9-20 ============
# face fill (rows 9-20), 13 wide
c.rect(10, 9, 12, 11, SKIN)
# face side outline
c.set(9, 10, OUTLN); c.set(22, 10, OUTLN)
c.rect(9, 11, 1, 8, OUTLN)
c.rect(22, 11, 1, 8, OUTLN)
c.set(9, 18, OUTLN); c.set(22, 18, OUTLN)
# chin outline bottom
c.rect(10, 19, 12, 1, OUTLN)

# forehead shadow
c.rect(11, 9, 10, 1, SKIN_SH)

# hair sides
c.rect(9, 11, 1, 3, HAIR)
c.rect(22, 11, 1, 3, HAIR)
c.set(10, 11, HAIR); c.set(21, 11, HAIR)

# eyes + brows
c.rect(12, 12, 2, 1, HAIR)
c.rect(18, 12, 2, 1, HAIR)
c.set(12, 13, EYE); c.set(13, 13, EYE)
c.set(18, 13, EYE); c.set(19, 13, EYE)

# cheeks
c.rect(11, 15, 2, 1, SKIN_SH)
c.rect(19, 15, 2, 1, SKIN_SH)

# mouth smile
c.rect(14, 16, 4, 1, MOUTH)
c.set(13, 16, MOUTH); c.set(18, 16, MOUTH)
c.set(14, 17, SKIN_SH); c.set(17, 17, SKIN_SH)

# ============ TORSO rows 20-28 ============
# uniform torso
c.rect(9, 20, 14, 8, WHITE)
# outline
c.rect(8, 20, 1, 8, OUTLN)
c.rect(23, 20, 1, 8, OUTLN)
c.rect(9, 20, 14, 1, OUTLN)
c.rect(9, 27, 14, 1, OUTLN)

# apron bib at chest
c.rect(9, 20, 14, 1, APRON)
c.rect(10, 21, 12, 1, APRON)
# bib sides/diagonal outline
c.set(9, 20, APRON_SH); c.set(22, 20, APRON_SH)
c.set(10, 21, APRON_SH); c.set(21, 21, APRON_SH)
# apron main body
c.rect(10, 22, 12, 6, APRON)
c.set(9, 22, APRON_SH); c.set(22, 22, APRON_SH)
c.rect(10, 27, 12, 1, APRON_SH)
# apron side lines
c.rect(9, 23, 1, 4, APRON_SH)
c.rect(22, 23, 1, 4, APRON_SH)
# flour dust
c.set(13, 23, CREAM); c.set(15, 24, CREAM); c.set(18, 23, CREAM)
c.set(12, 25, CREAM); c.set(17, 25, CREAM); c.set(14, 26, CREAM)
c.set(16, 24, WHITE); c.set(19, 26, WHITE)
# apron pocket
c.set(14, 25, APRON_SH); c.set(15, 25, APRON_SH)
c.set(14, 26, APRON_SH); c.set(15, 26, APRON_SH)

# ============ ARMS (white sleeves) ============
c.rect(8, 21, 2, 5, WHITE)
c.rect(22, 21, 2, 5, WHITE)
c.set(8, 20, OUTLN); c.set(9, 20, OUTLN)
c.set(22, 20, OUTLN); c.set(23, 20, OUTLN)
c.set(7, 21, OUTLN); c.set(24, 21, OUTLN)
c.set(7, 23, OUTLN); c.set(24, 23, OUTLN)
c.set(8, 24, WHITE_SH); c.set(22, 24, WHITE_SH)
c.set(8, 25, WHITE_SH); c.set(22, 25, WHITE_SH)

# ============ HANDS gripping steamer sides rows 23-27 ============
# left hand
c.set(8, 24, SKIN); c.set(8, 25, SKIN)
c.set(8, 26, SKIN); c.set(8, 27, SKIN)
c.set(7, 25, SKIN)
c.rect(7, 26, 2, 2, SKIN)
c.set(6, 26, SKIN); c.set(6, 27, SKIN)
# right hand
c.set(23, 24, SKIN); c.set(23, 25, SKIN)
c.set(23, 26, SKIN); c.set(23, 27, SKIN)
c.set(24, 25, SKIN)
c.rect(23, 26, 2, 2, SKIN)
c.set(25, 26, SKIN); c.set(25, 27, SKIN)

# ============ BAMBOO STEAMER rows 25-29 ============
# steamer body
c.rect(8, 26, 16, 1, STEAM)
c.rect(8, 27, 16, 1, STEAM)
c.rect(8, 28, 16, 1, STEAM)
c.rect(8, 29, 16, 1, STEAM_S)
# steamer outline
c.rect(7, 26, 1, 4, OUTLN)
c.rect(24, 26, 1, 4, OUTLN)
c.rect(8, 29, 16, 1, OUTLN)
# bamboo grain
for gx in (10, 13, 16, 19, 22):
    c.set(gx, 26, STEAM_L)
for gx in (9, 12, 15, 18, 21):
    c.set(gx, 27, STEAM_L)
for gx in (10, 13, 16, 19, 22):
    c.set(gx, 27, STEAM_S)
for gx in (11, 14, 17, 20):
    c.set(gx, 28, STEAM_S)
c.set(9, 28, STEAM); c.set(22, 28, STEAM)

# ============ STEAMER LID + BUNS ============
# lid top
c.rect(8, 24, 16, 1, STEAM_L)
c.rect(8, 23, 16, 1, STEAM_L)
c.set(7, 23, OUTLN); c.set(24, 23, OUTLN)
c.set(7, 24, OUTLN); c.set(24, 24, OUTLN)
# lid band
c.rect(9, 25, 14, 1, STEAM)
c.set(8, 25, OUTLN); c.set(23, 25, OUTLN)

# ---- Three buns peeking above the lid ----
# left bun (dome centered ~x12), rows 19-23
c.set(11, 20, BUN); c.set(12, 20, BUN); c.set(13, 20, BUN)
c.set(11, 21, BUN); c.set(12, 21, BUN); c.set(13, 21, BUN)
c.set(10, 22, BUN); c.set(11, 22, BUN); c.set(12, 22, BUN); c.set(13, 22, BUN)
c.set(10, 23, BUN); c.set(11, 23, BUN); c.set(12, 23, BUN); c.set(13, 23, BUN)
# left bun dome cap
c.set(11, 19, BUN); c.set(12, 19, BUN)

# center bun (dome centered ~x16), rows 18-23
c.set(15, 20, BUN); c.set(16, 20, BUN); c.set(17, 20, BUN)
c.set(14, 21, BUN); c.set(15, 21, BUN); c.set(16, 21, BUN); c.set(17, 21, BUN); c.set(18, 21, BUN)
c.set(14, 22, BUN); c.set(15, 22, BUN); c.set(16, 22, BUN); c.set(17, 22, BUN); c.set(18, 22, BUN)
c.set(14, 23, BUN); c.set(15, 23, BUN); c.set(16, 23, BUN); c.set(17, 23, BUN); c.set(18, 23, BUN)
c.set(16, 19, BUN); c.set(17, 19, BUN); c.set(15, 19, BUN)
c.set(16, 18, BUN)

# right bun (dome centered ~x20), rows 19-23
c.set(19, 20, BUN); c.set(20, 20, BUN); c.set(21, 20, BUN)
c.set(19, 21, BUN); c.set(20, 21, BUN); c.set(21, 21, BUN)
c.set(19, 22, BUN); c.set(20, 22, BUN); c.set(21, 22, BUN); c.set(22, 22, BUN)
c.set(19, 23, BUN); c.set(20, 23, BUN); c.set(21, 23, BUN); c.set(22, 23, BUN)
c.set(20, 19, BUN); c.set(21, 19, BUN)

# bun shading - tops and creases
# left bun top sheen
c.set(12, 19, BUN_SH); c.set(11, 20, BUN_SH)
# center bun top
c.set(16, 18, BUN_SH)
# right bun top
c.set(20, 19, BUN_SH); c.set(21, 20, BUN_SH)
# bottom shading of each bun (meeting lid)
c.rect(10, 22, 4, 1, BUN_SH)
c.rect(19, 22, 4, 1, BUN_SH)
c.rect(14, 22, 5, 1, BUN_SH)
# creases between buns (dark separation)
c.set(13, 21, BUN_SH); c.set(14, 21, BUN_SH)
c.set(13, 22, BUN_SH); c.set(14, 22, BUN_SH)
c.set(18, 21, BUN_SH); c.set(19, 21, BUN_SH)
c.set(18, 22, BUN_SH); c.set(19, 22, BUN_SH)
# bun tops pleat dots
c.set(13, 19, BUN_SH); c.set(14, 19, BUN_SH)
c.set(18, 19, BUN_SH); c.set(19, 19, BUN_SH)

# ============ LEGS (peek below steamer) ============
c.rect(11, 30, 4, 2, WHITE_SH)
c.rect(18, 30, 4, 2, WHITE_SH)
# feet/shoes outline
c.rect(10, 31, 6, 1, OUTLN)
c.rect(17, 31, 6, 1, OUTLN)
c.rect(11, 30, 4, 1, OUTLN)
c.rect(18, 30, 4, 1, OUTLN)
# shoe color
c.rect(10, 31, 6, 1, (50, 50, 58))
c.rect(17, 31, 6, 1, (50, 50, 58))
# shoe highlight
c.set(11, 31, OUTLN); c.set(14, 31, OUTLN)
c.set(18, 31, OUTLN); c.set(21, 31, OUTLN)

# ============ STEAM WISPS (above hat, floating) ============
c.set(14, 2, STEAMW); c.set(15, 2, STEAMW)
c.set(16, 1, STEAMW); c.set(17, 1, STEAMW)
c.set(17, 0, STEAMW)
c.set(13, 4, STEAMW); c.set(14, 4, STEAMW)
c.set(15, 3, STEAMW); c.set(16, 3, STEAMW)
c.set(18, 3, STEAMW)
c.set(19, 2, STEAMW)

print(c.stats_text())
view(c)
finish(c)
