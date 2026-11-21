# 32x32 dim sum chef, front-facing, holding bamboo steamer with buns.

c = new_canvas(32, 32, name="chef")

# ---- palette ----
WHITE   = c.color('#FAFAF5')   # hat / jacket
GRAY    = c.color('#C9C9C0')   # light shading
GRAY2   = c.color('#9A9A90')   # deeper shading / collar lines
SKIN    = c.color('#F2C9A0')
SKIN_D  = c.color('#D9A06F')
HAIR    = c.color('#5A4232')
EYE     = c.color('#2B2320')
CHEEK   = c.color('#EE9E8E')
MOUTH   = c.color('#8E4A42')
BTN     = c.color('#5A5A52')
BUN     = c.color('#F6E8C8')
BUN_D   = c.color('#DCC49A')
BAMBOO  = c.color('#C89358')
BAMBOO_D= c.color('#8F6234')
BAMBOO_L= c.color('#E2B47E')
APRON   = c.color('#BFD4E0')
APRON_D = c.color('#93AEBD')
FLOUR   = c.color('#FFFFFF')
PANTS   = c.color('#4E4E5A')
SHOE    = c.color('#33303A')

# ---- chef hat (toque) ----
c.rect(13, 2, 6, 1, WHITE)
c.rect(11, 3, 10, 1, WHITE); c.set(20, 3, GRAY)
for y in (4, 5, 6):
    c.rect(10, y, 12, 1, WHITE)
    c.set(20, y, GRAY); c.set(21, y, GRAY)
c.rect(11, 7, 10, 1, GRAY2)                 # band shadow line
c.rect(11, 8, 10, 1, WHITE)                 # band
c.set(11, 8, GRAY); c.set(20, 8, GRAY)

# ---- face ----
c.rect(12, 9, 8, 1, SKIN)
c.set(11, 9, HAIR); c.set(20, 9, HAIR)      # sideburns
c.rect(11, 10, 10, 1, SKIN)
c.set(13, 10, HAIR); c.set(18, 10, HAIR)    # brows
c.rect(11, 11, 10, 1, SKIN)
c.set(13, 11, EYE); c.set(18, 11, EYE)      # eyes
c.rect(11, 12, 10, 1, SKIN)
c.set(12, 12, CHEEK); c.set(19, 12, CHEEK)  # cheeks
c.set(11, 12, SKIN_D); c.set(20, 12, SKIN_D)
c.rect(12, 13, 8, 1, SKIN)
c.set(14, 13, MOUTH); c.set(17, 13, MOUTH)  # smile corners
c.rect(12, 14, 8, 1, SKIN)
c.set(15, 14, MOUTH); c.set(16, 14, MOUTH)  # smile bottom

# ---- neck & collar ----
c.rect(11, 15, 10, 1, WHITE)
c.rect(14, 15, 4, 1, SKIN)                  # neck
c.rect(9, 16, 14, 1, WHITE)                 # shoulders
c.set(15, 16, SKIN); c.set(16, 16, SKIN)    # open collar V
c.set(14, 16, GRAY2); c.set(17, 16, GRAY2)  # collar edges

# ---- jacket body & arms ----
c.rect(8, 17, 16, 1, WHITE)
c.set(13, 17, BTN); c.set(18, 17, BTN)      # double-breasted buttons
c.rect(8, 18, 16, 1, WHITE)
c.set(13, 18, BTN); c.set(18, 18, BTN)
c.rect(8, 19, 16, 1, WHITE)
c.set(8, 19, GRAY); c.set(23, 19, GRAY)     # sleeve shading
c.set(8, 20, WHITE); c.set(9, 20, WHITE)
c.set(22, 20, WHITE); c.set(23, 20, WHITE)

# ---- buns (above steamer rim) ----
for x in (10, 14, 18):
    c.set(x, 19, BUN_D); c.set(x + 1, 19, BUN); c.set(x + 2, 19, BUN_D)
c.set(13, 19, BAMBOO_D); c.set(17, 19, BAMBOO_D); c.set(21, 19, BAMBOO_D)
for x in (10, 14, 18):
    c.rect(x, 20, 3, 1, BUN)
c.set(13, 20, BAMBOO_D); c.set(17, 20, BAMBOO_D); c.set(21, 20, BAMBOO_D)

# ---- bamboo steamer (x10..21) ----
c.rect(10, 21, 12, 1, BAMBOO_L)             # bright top rim
c.set(10, 21, BAMBOO_D); c.set(21, 21, BAMBOO_D)
c.rect(10, 22, 12, 1, BAMBOO)
c.rect(10, 23, 12, 1, BAMBOO_D)             # woven band
c.rect(10, 24, 12, 1, BAMBOO)
c.rect(10, 25, 12, 1, BAMBOO_D)             # bottom band

# ---- hands gripping steamer sides ----
c.rect(8, 21, 2, 3, SKIN)
c.rect(22, 21, 2, 3, SKIN)
c.set(8, 23, SKIN_D); c.set(9, 23, SKIN_D)  # knuckle shading
c.set(22, 23, SKIN_D); c.set(23, 23, SKIN_D)
c.set(9, 22, SKIN_D); c.set(22, 22, SKIN_D)

# ---- jacket sides below hands ----
c.rect(8, 24, 2, 2, WHITE)
c.rect(22, 24, 2, 2, WHITE)

# ---- apron below steamer, flour-dusted ----
c.rect(9, 26, 14, 1, APRON)
c.rect(10, 27, 12, 1, APRON)
c.rect(10, 28, 12, 1, APRON_D)              # hem
c.set(9, 26, APRON_D); c.set(22, 26, APRON_D)
for fx, fy in [(11, 26), (15, 26), (13, 27), (19, 27), (17, 28), (12, 28)]:
    c.set(fx, fy, FLOUR)

# ---- legs & shoes ----
c.rect(11, 29, 4, 2, PANTS)
c.rect(17, 29, 4, 2, PANTS)
c.rect(10, 31, 5, 1, SHOE)
c.rect(17, 31, 5, 1, SHOE)

print(c.stats_text())
view(c)
finish(c)
