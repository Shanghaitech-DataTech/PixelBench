from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="sky_pirate_girl")

SKY1 = '#7EC8EF'; SKY2 = '#9FD9F5'; SKY3 = '#C2E9FB'
CLOUD = '#FFFFFF'; CLOUD_SH = '#DDF1FD'
SKIN = '#FFE4CA'; SKIN_SH = '#F4C79E'; SKIN_D = '#DFAA7C'
BLUSH = '#F8A9A1'
HAIR_A = '#FFD97A'; HAIR_B = '#F0B558'; HAIR_C = '#CD9138'; HAIR_D = '#8F5E22'
EYE_C = '#34C6BB'; EYE_D = '#0C6264'
LENS = '#BEE7F8'; LENS_HI = '#F6FCFF'
GOG = '#5A3D2B'; GOG_D = '#33221A'
COAT_A = '#18345F'; COAT_B = '#2C5490'; COAT_C = '#4B79BA'; COAT_D = '#0F2240'
TRIM = '#F7F2E2'
SCARF_A = '#E54242'; SCARF_B = '#C0262E'; SCARF_C = '#F26969'; SCARF_D = '#8C1520'

# --- sky ---
for y in range(H):
    col = SKY1 if y < 18 else (SKY2 if y < 36 else SKY3)
    c.rect(0, y, W, 1, col)

# --- clouds ---
c.ellipse(10, 6, 6, 3, CLOUD)
c.ellipse(18, 4, 4, 3, CLOUD)
c.ellipse(5, 10, 3, 2, CLOUD)
c.ellipse(52, 7, 5, 3, CLOUD)
c.ellipse(59, 11, 4, 2, CLOUD)
c.ellipse(48, 12, 3, 2, CLOUD_SH)
c.ellipse(35, 59, 12, 2, CLOUD)
c.ellipse(18, 61, 10, 2, CLOUD_SH)

# --- back hair ---
c.ellipse(31, 10, 17, 12, HAIR_B)
c.poly([(28,5),(31,1),(36,4),(40,8)], HAIR_B)
c.poly([(23,12),(19,8),(15,10),(11,14),(8,20),(5,27),(3,35),(3,42),(7,45),(10,40),(12,33),(14,27),(17,21)], HAIR_B)
c.poly([(41,9),(45,6),(49,10),(47,15),(43,12)], HAIR_B)
c.poly([(43,13),(47,12),(50,16),(48,21),(44,18)], HAIR_B)

# --- face ---
c.poly([(25,14),(29,10),(34,9),(41,11),(45,17),(45,24),(42,31),(37,36),(34,38),(29,35),(24,30),(22,23)], SKIN)
c.ellipse(23, 25, 2, 3, SKIN)
c.ellipse(23, 25, 1, 2, SKIN_D)
c.rect(29, 36, 10, 9, SKIN)
c.rect(35, 38, 4, 6, SKIN_SH)
c.line(41, 27, 39, 33, SKIN_SH)
c.set(31, 36, SKIN_SH)

# --- bangs ---
c.poly([(23,14),(27,9),(34,8),(40,10),(44,14),(42,18),(38,15),(34,19),(30,16),(26,18)], HAIR_B)
c.poly([(28,15),(30,16),(29,20),(26,18)], HAIR_C)
c.poly([(33,17),(36,16),(35,20),(32,19)], HAIR_C)
c.ellipse(33, 10, 13, 5, HAIR_A)
c.line(30, 8, 29, 14, HAIR_C)
c.line(36, 9, 37, 15, HAIR_C)
c.line(21, 9, 12, 22, HAIR_C)
c.line(16, 11, 8, 27, HAIR_C)
c.set(4, 40, HAIR_D); c.set(7, 43, HAIR_D)
c.line(45, 12, 49, 18, HAIR_C)

# --- goggles ---
c.rect(22, 14, 23, 3, GOG)
c.rect(24, 15, 8, 6, GOG_D)
c.rect(26, 16, 5, 4, LENS)
c.rect(34, 15, 7, 6, GOG_D)
c.rect(36, 16, 4, 4, LENS)
c.rect(31, 16, 3, 3, GOG)
c.rect(27, 16, 2, 1, LENS_HI)
c.rect(37, 16, 2, 1, LENS_HI)
c.line(20, 22, 24, 20, GOG)
c.line(17, 24, 20, 22, GOG)

# --- brows ---
c.line(25, 20, 32, 19, HAIR_D)
c.line(34, 19, 40, 20, HAIR_D)

# --- eyes ---
c.rect(26, 22, 8, 7, EYE_D)
c.rect(27, 23, 6, 5, EYE_C)
c.rect(29, 24, 3, 3, EYE_D)
c.rect(28, 23, 2, 2, EYE_C)
c.rect(27, 23, 2, 1, LENS_HI)
c.rect(31, 26, 1, 1, LENS_HI)
c.rect(35, 22, 6, 6, EYE_D)
c.rect(36, 23, 4, 4, EYE_C)
c.rect(37, 24, 2, 2, EYE_D)
c.rect(36, 23, 2, 1, LENS_HI)
c.line(27, 28, 33, 28, EYE_D)
c.line(36, 27, 40, 27, EYE_D)

# --- nose, mouth, blush ---
c.set(42, 28, SKIN_D)
c.set(42, 29, SKIN_D)
c.line(30, 31, 36, 32, SKIN_D)
c.line(36, 32, 38, 30, SKIN_D)
c.rect(28, 29, 2, 1, BLUSH)
c.rect(37, 29, 2, 1, BLUSH)
c.rect(34, 37, 3, 2, SKIN_SH)

# --- coat ---
c.poly([(12,47),(18,44),(27,43),(40,44),(51,48),(55,56),(54,63),(10,63),(9,55),(7,55),(8,61),(10,63)], COAT_B)
c.poly([(12,47),(18,44),(27,43),(29,45),(28,51),(25,57),(18,59),(10,56),(8,51),(9,48)], COAT_A)
c.poly([(40,44),(51,48),(55,56),(54,63),(44,62),(43,55),(41,49)], COAT_C)
c.line(43, 45, 45, 51, COAT_D)
c.line(54, 50, 54, 63, COAT_D)
c.rect(10, 62, 44, 1, COAT_D)
c.rect(30, 49, 2, 2, COAT_C)
c.rect(30, 54, 2, 2, COAT_C)
c.rect(31, 49, 1, 1, TRIM)
c.rect(31, 54, 1, 1, TRIM)
c.line(12, 52, 19, 49, COAT_C)
c.line(27, 48, 27, 55, COAT_D)

# --- collar band (white V) ---
c.poly([(26,41),(31,37),(38,37),(43,41),(43,45),(39,44),(36,46),(31,46),(28,44)], TRIM)
c.line(27, 44, 31, 45, COAT_D)
c.line(38, 45, 42, 44, COAT_D)
c.poly([(32,38),(37,38),(36,42),(33,42)], COAT_D)

# --- scarf knot over collar ---
c.poly([(30,43),(37,43),(38,49),(32,49)], SCARF_A)
c.rect(32, 44, 3, 2, SCARF_B)
c.rect(31, 46, 5, 1, SCARF_B)
c.set(33, 43, SCARF_C)
c.set(35, 43, SCARF_C)
# scarf tails down the chest
c.poly([(31,48),(37,48),(35,57),(31,63),(25,63),(27,55)], SCARF_A)
c.poly([(26,50),(29,50),(27,58),(23,62),(20,60)], SCARF_C)
c.poly([(37,49),(41,49),(39,58),(36,63),(33,63),(32,55)], SCARF_B)
c.rect(27, 55, 7, 1, SCARF_D)

# --- silhouette outlines ---
c.line(12, 48, 8, 56, COAT_D)
c.line(22, 13, 17, 20, HAIR_D)
c.line(17, 20, 11, 30, HAIR_D)

# --- wind streaks ---
c.line(60, 20, 52, 22, CLOUD)
c.line(0, 30, 8, 28, CLOUD)
c.line(2, 48, 10, 46, CLOUD_SH)
# hair sparkle
for p in [(17, 8), (45, 10), (39, 7)]:
    c.set(p[0], p[1], HAIR_A)

print(c.stats_text())
print(c.matrix_text(region=(2, 2, 50, 40)))
print(c.matrix_text(region=(2, 40, 58, 63)))

finish(c)
