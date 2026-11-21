from pixelbench_api import *

# 64x64 portrait canvas
c = new_canvas(64, 64, name="output")

# --- Palette ---
SKIN = "#f0c8a0"
SKIN_SH = "#d8a884"
SKIN_LT = "#f8dcc0"
HAIR = "#7a4a2a"
HAIR_DK = "#5a3420"
HAIR_LT = "#9a6a3a"
GOGGLE = "#8a6a2a"
GOGGLE_DK = "#5a4a1a"
GOGGLE_LT = "#c8a84a"
LENS = "#4aa8e8"
LENS_DK = "#2a6a98"
LENS_LT = "#88d0f8"
COAT = "#2a4a7a"
COAT_DK = "#1a3260"
COAT_LT = "#4a6a9a"
SCARF = "#c83030"
SCARF_DK = "#982020"
SCARF_LT = "#e85050"
GOLD = "#d8b848"
SKY = "#78b8e8"
SKY_DK = "#5898c8"
CLOUD = "#f0f8ff"
EYE = "#3a6a3a"
EYE_DK = "#1a3a1a"
EYE_LT = "#ffffff"
LIP = "#c86060"
BLUSH = "#f0a878"

# --- Background ---
for y in range(64):
    col = SKY if y < 42 else SKY_DK
    for x in range(64):
        c.set(x, y, col)

# Clouds
c.ellipse(8, 8, 6, 2, CLOUD)
c.ellipse(15, 6, 4, 2, CLOUD)
c.ellipse(50, 12, 5, 2, CLOUD)
c.ellipse(56, 10, 3, 2, CLOUD)
c.ellipse(12, 56, 5, 2, CLOUD)
c.ellipse(53, 55, 5, 2, CLOUD)

# Wind streaks in sky
c.line(4, 22, 10, 20, CLOUD)
c.line(58, 30, 63, 28, CLOUD)
c.line(60, 22, 63, 22, CLOUD)

# --- Wind-swept hair back (dark underlayer) ---
# Head base silhouette - larger head
c.ellipse(32, 30, 14, 16, HAIR_DK)

# Wind trails to the right
c.poly([(44, 16), (56, 8), (63, 12), (56, 20), (46, 22)], HAIR_DK)
c.poly([(42, 12), (52, 4), (62, 6), (55, 14), (44, 17)], HAIR_DK)
c.poly([(44, 24), (54, 22), (60, 26), (54, 32), (46, 30)], HAIR_DK)
# Lower flowing hair behind neck
c.poly([(40, 36), (52, 40), (58, 48), (52, 54), (46, 46), (42, 40)], HAIR_DK)

# Wind sweep on the left
c.poly([(22, 16), (12, 10), (6, 14), (14, 22), (24, 20)], HAIR_DK)
c.poly([(24, 16), (16, 12), (8, 16), (16, 23), (24, 21)], HAIR)
c.line(18, 14, 22, 18, HAIR_LT)

# --- Goggles pushed up on hair (large, prominent) ---
# Headband strap
c.line(16, 18, 48, 18, GOGGLE_DK)
c.line(17, 17, 47, 17, GOGGLE_DK)

# Left goggle (further eye, slightly smaller, at upper-left of forehead, slightly angled)
c.circle(25, 16, 5, GOGGLE)
c.circle(25, 16, 4, GOGGLE_DK)
c.circle(25, 16, 3, LENS)
c.circle(25, 16, 2, LENS_DK)
c.set(23, 15, LENS_LT)
c.set(24, 14, LENS_LT)
c.set(27, 17, LENS_DK)
c.set(22, 13, GOGGLE_LT)
c.set(24, 12, GOGGLE_LT)

# Right goggle (near eye, larger)
c.circle(36, 15, 6, GOGGLE)
c.circle(36, 15, 5, GOGGLE_DK)
c.circle(36, 15, 4, LENS)
c.circle(36, 15, 3, LENS_DK)
c.set(34, 13, LENS_LT)
c.set(35, 12, LENS_LT)
c.set(38, 17, LENS_DK)
c.set(39, 17, LENS_DK)
c.set(32, 11, GOGGLE_LT)
c.set(38, 11, GOGGLE_LT)
c.set(33, 12, GOGGLE_LT)

# Bridge
c.line(29, 14, 30, 14, GOGGLE_LT)
c.line(29, 15, 30, 15, GOGGLE_LT)
c.line(30, 16, 31, 16, GOGGLE_LT)

# --- Face ---
c.ellipse(32, 34, 11, 13, SKIN)

# --- Ear (right side, visible in 3/4 view) ---
c.circle(42, 35, 2, SKIN)
c.set(44, 35, SKIN)
c.set(43, 36, SKIN_SH)
c.set(44, 36, SKIN_SH)
c.set(42, 34, SKIN_SH)

# --- Eyes (below goggles, confident) ---
# Left eye (partially hidden behind hair for 3/4 view)
c.rect(25, 30, 5, 3, EYE_LT)   # sclera
c.rect(26, 30, 5, 3, EYE)      # iris
c.rect(27, 30, 4, 3, EYE_DK)   # pupil
c.set(26, 30, EYE_LT)          # catch light
c.line(25, 29, 30, 29, HAIR_DK) # upper lid
c.line(26, 33, 29, 33, HAIR_DK) # lower lid

# Right eye (fully visible, larger for closer view)
c.rect(34, 29, 7, 4, EYE_LT)   # sclera
c.rect(35, 29, 6, 4, EYE)      # iris
c.rect(36, 29, 5, 4, EYE_DK)   # pupil
c.set(36, 29, EYE_LT)          # catch light
c.set(39, 31, EYE_LT)          # secondary light
c.line(33, 28, 43, 28, HAIR_DK) # upper lid
c.line(34, 33, 42, 33, HAIR_DK) # lower lid
# Upper lid emphasis
c.set(34, 29, HAIR_DK)
c.set(35, 29, HAIR_DK)
c.set(41, 29, HAIR_DK)
c.set(42, 29, HAIR_DK)

# --- Confident brows ---
c.line(25, 27, 30, 26, HAIR_DK)
c.line(34, 26, 43, 27, HAIR_DK)

# --- Front bangs (wind-swept right) ---
# Bangs covering forehead, slightly overlapping goggles
c.poly([(18, 18), (30, 16), (42, 18), (50, 24), (46, 28), (38, 25), (28, 24), (20, 23)], HAIR)
c.poly([(38, 19), (48, 21), (56, 27), (50, 33), (44, 29)], HAIR)
c.poly([(43, 23), (54, 25), (60, 31), (54, 37), (48, 33)], HAIR_LT)
# Bang highlights
c.line(22, 20, 36, 18, HAIR_LT)
c.line(40, 21, 54, 27, HAIR_LT)
# Extra bang strand over right eye area
c.line(44, 24, 50, 30, HAIR)

# --- Nose hint ---
c.set(36, 37, SKIN_SH)
c.set(37, 38, SKIN_SH)

# --- Mouth - confident smirk ---
# Clean upper lip line
c.set(33, 40, LIP)
c.set(34, 40, LIP)
c.set(35, 40, LIP)
c.set(36, 40, LIP)
c.set(37, 39, LIP)
c.set(38, 39, LIP)
c.set(39, 39, LIP)
c.set(40, 40, LIP)
# Lower lip hint
c.set(34, 41, LIP)
c.set(35, 41, LIP)

# --- Cheeks ---
c.set(25, 37, BLUSH)
c.set(26, 37, BLUSH)
c.set(26, 38, BLUSH)
c.set(27, 38, BLUSH)
c.set(40, 37, BLUSH)
c.set(41, 37, BLUSH)
c.set(42, 38, BLUSH)

# --- Neck ---
c.rect(29, 44, 7, 6, SKIN_SH)
c.rect(28, 44, 3, 4, "#c09070")
c.set(29, 49, "#c09070")

# --- Red scarf (wind-swept right) ---
# Scarf wrap around neck
c.poly([(20, 47), (45, 47), (48, 52), (44, 56), (24, 56), (20, 52)], SCARF)
c.line(21, 48, 44, 48, SCARF_LT)
c.line(22, 53, 40, 53, SCARF_DK)
# Scarf wrap detail
c.line(25, 50, 42, 50, SCARF_DK)
# Knot
c.circle(47, 51, 3, SCARF)
c.circle(48, 51, 2, SCARF_DK)
c.set(47, 49, SCARF_LT)
# Scarf tail streaming right
c.poly([(47, 49), (56, 47), (63, 50), (58, 56), (52, 55), (49, 52)], SCARF)
c.poly([(49, 50), (56, 49), (61, 51), (56, 55), (51, 53)], SCARF_LT)
# Secondary lower tail streaming right
c.poly([(46, 53), (55, 53), (62, 57), (56, 61), (50, 58)], SCARF_DK)
# Scarf tail tips
c.set(61, 49, SCARF)
c.set(62, 50, SCARF_DK)
c.set(60, 56, SCARF_DK)
c.set(61, 58, SCARF_DK)

# --- Coat shoulders ---
c.poly([(10, 52), (52, 52), (57, 56), (55, 63), (46, 63), (32, 63), (20, 63), (12, 61), (8, 56)], COAT)

# Coat lapel
c.poly([(24, 50), (34, 50), (35, 56), (30, 59), (25, 56)], COAT_DK)
c.poly([(40, 50), (48, 50), (47, 56), (42, 58), (39, 55)], COAT_DK)
# Gold trim
c.line(25, 51, 33, 51, GOLD)
c.line(41, 51, 47, 51, GOLD)

# Coat highlights
c.poly([(14, 54), (22, 54), (24, 58), (16, 60)], COAT_LT)
c.poly([(48, 54), (56, 54), (52, 60), (46, 58)], COAT_LT)
# Additional coat shading details
c.line(36, 53, 44, 53, COAT_DK)
c.line(20, 56, 28, 56, COAT_DK)
c.line(12, 58, 22, 58, COAT_DK)

# Coat edge shading
c.line(18, 62, 46, 62, COAT_DK)
c.line(12, 57, 18, 61, COAT_DK)
c.line(46, 61, 52, 57, COAT_DK)

# Buttons
c.set(37, 55, GOLD)
c.set(36, 58, GOLD)
c.set(35, 60, GOLD)

# --- Hair falling on right shoulder ---
c.poly([(42, 38), (50, 42), (54, 48), (52, 55), (48, 52), (46, 45)], HAIR)
c.line(44, 40, 50, 46, HAIR_LT)
c.line(48, 44, 52, 52, HAIR_DK)
# hair locks on left side
c.poly([(18, 16), (12, 18), (8, 22), (14, 26), (20, 22)], HAIR)
c.line(14, 18, 18, 22, HAIR_LT)
# Extra top hair strand flowing right
c.line(40, 8, 50, 6, HAIR_LT)
c.line(44, 10, 54, 9, HAIR_LT)

save("sky_pirate_girl", c)
print("Stats:")
print(c.stats_text())

finish(c)
