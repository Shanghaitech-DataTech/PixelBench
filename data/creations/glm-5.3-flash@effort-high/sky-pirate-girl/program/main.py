from pixelbench_api import *

bg = new_canvas(64, 64, name="bg")
ch = new_canvas(64, 64, name="char")

# ---------------- palette ----------------
SKY_T   = bg.color("#bfe8f8", "sky_top")
SKY_M   = bg.color("#a5d8f0", "sky_mid")
SKY_B   = bg.color("#8ec7e6", "sky_bot")
CLOUD   = bg.color("#ffffff", "cloud")
CLOUD2  = bg.color("#ddf1fb", "cloud2")
OUT     = bg.color("#2e2530", "outline")
SKIN    = bg.color("#f6cfa8", "skin")
SKIN_SH = bg.color("#dba47b", "skin_sh")
BLUSH   = bg.color("#f2a48c", "blush")
HAIR    = bg.color("#7c4a2c", "hair")
HAIR_SH = bg.color("#5a321c", "hair_sh")
HAIR_HI = bg.color("#a86a3e", "hair_hi")
EYE_W   = bg.color("#ffffff", "eye_white")
IRIS    = bg.color("#c9762e", "iris")
IRIS_D  = bg.color("#7c4212", "iris_dark")
GOG_F   = bg.color("#3c4048", "gog_frame")
GOG_L   = bg.color("#9fd8e8", "gog_lens")
GOG_L2  = bg.color("#e2f6fc", "gog_lens_hi")
STRAP   = bg.color("#5a4a38", "strap")
COAT    = bg.color("#2e3f66", "coat")
COAT_H  = bg.color("#46598c", "coat_hi")
COAT_S  = bg.color("#22304e", "coat_sh")
GOLD    = bg.color("#d9a94e", "gold")
SCARF   = bg.color("#c73a30", "scarf")
SCARF_S = bg.color("#96271f", "scarf_sh")
SCARF_H = bg.color("#e05a4a", "scarf_hi")

# ---------------- background: sky ----------------
for y in range(64):
    col = SKY_T if y < 22 else (SKY_M if y < 44 else SKY_B)
    bg.rect(0, y, 64, 1, col)
bg.dither(0, 20, 64, 2, [SKY_T, SKY_M], "checker")
bg.dither(0, 42, 64, 2, [SKY_M, SKY_B], "checker")

# clouds
bg.ellipse(10, 10, 7, 3, CLOUD2)
bg.ellipse(14, 9, 4, 2, CLOUD)
bg.ellipse(53, 20, 6, 3, CLOUD2)
bg.ellipse(56, 19, 3, 2, CLOUD)
bg.ellipse(7, 46, 6, 3, CLOUD2)
bg.ellipse(56, 57, 6, 3, CLOUD2)
bg.ellipse(53, 56, 4, 2, CLOUD)

# wind streaks
bg.line(2, 28, 11, 28, CLOUD2)
bg.line(52, 33, 61, 32, CLOUD2)
bg.line(3, 57, 13, 56, CLOUD2)
bg.line(48, 8, 58, 7, CLOUD2)

# ---------------- character ----------------
# back hair mass
ch.poly([(19,16),(24,10),(31,8),(38,10),(43,16),(44,26),(44,38),(41,44),
         (36,46),(24,46),(20,42),(18,32)], HAIR_SH)

# coat / shoulders
ch.poly([(6,64),(9,52),(15,45),(24,41),(38,41),(47,45),(53,52),(56,64)], COAT)
# lapels
ch.poly([(24,41),(29,43),(27,52),(20,47)], COAT_S)
ch.poly([(38,41),(33,43),(35,52),(42,47)], COAT_S)
ch.rect(29,43,4,9, COAT_S)                      # inner shirt
ch.line(24,41,20,47, GOLD)
ch.line(38,41,42,47, GOLD)
ch.set(31,47,GOLD); ch.set(31,51,GOLD)
# light on shoulders
ch.line(10,52,15,46, COAT_H)
ch.line(15,46,20,43, COAT_H)
ch.line(46,46,51,52, COAT_H)

# neck
ch.rect(27,33,7,9, SKIN)
ch.rect(27,34,7,3, SKIN_SH)

# face (three-quarter, chin slightly left of centre)
ch.poly([(23,20),(24,15),(28,12),(33,12),(37,15),(39,20),(39,25),(37,30),
         (33,35),(29,37),(25,33),(23,28)], SKIN)
ch.rect(27,35,6,2, SKIN_SH)   # jaw shadow

# side locks
ch.poly([(21,19),(19,26),(20,34),(23,40),(25,34),(23,26),(23,20)], HAIR)
ch.poly([(40,19),(43,26),(43,36),(40,42),(38,36),(39,26)], HAIR)
ch.line(20,26,21,36, HAIR_SH)
ch.line(42,26,41,38, HAIR_SH)

# bangs (jagged bottom, swept)
ch.poly([(21,18),(22,13),(26,10),(31,9),(36,10),(40,13),(41,18),
         (38,15),(36,21),(33,15),(30,22),(27,15),(24,21),(22,15)], HAIR)
# wind-swept strands to the right
ch.poly([(41,13),(50,10),(54,12),(45,16)], HAIR)
ch.poly([(41,17),(52,17),(54,20),(43,20)], HAIR)
# wind-blown loose strands (filled so they keep hair colour inside the outline)
ch.poly([(42,22),(50,23),(51,25),(43,24)], HAIR)
ch.poly([(44,26),(51,27),(50,29),(45,28)], HAIR_SH)
# highlights
ch.line(25,12,30,11, HAIR_HI)
ch.line(33,11,37,12, HAIR_HI)
ch.line(23,16,24,19, HAIR_HI)

# goggles pushed up on the forehead
ch.rect(20,13,23,2, STRAP)
ch.circle(26,15,3, GOG_F)
ch.circle(26,15,2, GOG_L)
ch.circle(35,15,3, GOG_F)
ch.circle(35,15,2, GOG_L)
ch.rect(29,15,4,1, GOG_F)
ch.set(25,14,GOG_L2); ch.set(34,14,GOG_L2)
ch.set(22,15,GOG_F); ch.set(39,15,GOG_F)

# eyes (viewer-right eye wider: three-quarter)
def eye(x, y, w):
    ch.rect(x, y+1, w, 4, EYE_W)
    ch.rect(x+1, y+1, 3, 4, IRIS)
    ch.rect(x+2, y+1, 1, 4, IRIS_D)
    ch.set(x+1, y+2, EYE_W)
    ch.rect(x, y, w, 2, OUT)
eye(24, 23, 4)
eye(33, 23, 5)
# brows - confident (inner ends lower, slight frown of focus)
ch.line(24,20,27,21, HAIR_SH)
ch.line(33,21,38,20, HAIR_SH)
# nose + smirk
ch.set(32,30,SKIN_SH); ch.set(31,30,SKIN_SH)
ch.line(29,32,33,31, OUT)
ch.set(33,30,OUT)
# blush
ch.rect(24,29,3,1, BLUSH)
ch.rect(35,29,3,1, BLUSH)

# scarf around neck, tail whipping right
ch.rect(22,37,19,5, SCARF)
ch.rect(22,37,19,1, SCARF_H)
ch.rect(22,41,19,1, SCARF_S)
ch.rect(36,39,4,5, SCARF)
ch.poly([(38,42),(50,45),(57,52),(49,51),(41,47)], SCARF)
ch.line(40,44,50,49, SCARF_S)
ch.poly([(38,45),(46,51),(43,53),(37,48)], SCARF_S)

# crisp silhouette
ch.outline(OUT)

result = flatten([bg, ch], name="result")
print(result.stats_text())
print("FACE REGION (18,8)-(46,42):")
print(result.matrix_text(region=(18, 8, 46, 42)))
print("RIGHT HAIR REGION (36,6)-(58,28):")
print(result.matrix_text(region=(36, 6, 58, 28)))
print("BODY REGION (4,36)-(60,63):")
print(result.matrix_text(region=(4, 36, 60, 63)))
print("VIEW:", view(result, scale=8, margin=0))
save("sky-pirate-girl", result)
finish(result)
