from pixelbench_api import new_canvas, finish

c = new_canvas(128, 128, background="#0a0a18", name="standoff")

def col(h): return c.color(h)

# ---- palette ----
SKY_TOP = col("#0a0a18"); SKY_MID = col("#14142e"); SKY_LOW = col("#1c1c38"); GLOW = col("#352a52")
MOON    = col("#f0e0a8"); MOON_SH = col("#cfb878")
GROUND_D = col("#0b0b12"); GROUND_M = col("#17171f"); OUT = col("#040406")
K_DARK = col("#551010"); K_MID = col("#8f1818"); K_BR = col("#cc2222"); K_HI = col("#ff5a3a")
K_PUM  = col("#e2381a"); K_GOLD = col("#e8b84a"); STEEL = col("#b6c2ce")
K_BELT = col("#240a08"); K_BOOT = col("#38140f")
R_DK = col("#0e3418"); R_MD = col("#1e632c"); R_BR = col("#3a9c48"); R_HD = col("#2a7a38")
FACE = col("#0a1208"); EYE = col("#c4ff5c"); GLOVE = col("#122e0e")
SPARK = col("#fff2c0")

# ---- sky ----
c.rect(0, 0, 128, 128, SKY_TOP)
c.rect(0, 26, 128, 128, SKY_MID)
c.rect(0, 54, 128, 128, SKY_LOW)
c.rect(0, 80, 128, 20, GLOW)

# stars
for (sx, sy) in [(14, 12), (28, 30), (44, 18), (80, 10), (100, 22), (112, 34), (18, 52), (70, 16), (96, 6), (120, 14), (10, 36), (58, 12)]:
    c.set(sx, sy, MOON)
c.set(64, 52, MOON)

# ---- moon in the gap ----
c.circle(64, 44, 13, MOON)
c.ellipse(64, 52, 10, 4, MOON_SH)

# ---- ground ----
c.rect(0, 104, 128, 24, GROUND_D)
c.ellipse(14, 112, 13, 5, GROUND_M)
c.ellipse(48, 115, 10, 4, GROUND_M)
c.ellipse(96, 113, 13, 5, GROUND_M)
c.rect(0, 118, 128, 10, GROUND_M)

# ================= KNIGHT (left, red armor) =================
# plume flowing back
for (px, py) in [(36, 25), (31, 22), (26, 23), (22, 26), (19, 30)]:
    c.circle(px, py, 2, K_PUM)
# helmet
c.ellipse(36, 35, 10, 9, K_MID)
c.ellipse(36, 35, 10, 3, K_BR)
c.rect(26, 40, 20, 3, OUT)
# neck
c.rect(33, 45, 6, 4, K_DARK)
# shoulders
c.ellipse(28, 50, 9, 6, K_BR)
c.ellipse(45, 50, 9, 6, K_BR)
c.ellipse(45, 50, 7, 3, K_HI)
# torso
c.rect(27, 53, 20, 18, K_MID)
c.rect(29, 55, 16, 9, K_BR)
c.line(30, 57, 44, 57, K_HI)
# kite shield on the facing side
c.ellipse(28, 65, 6, 11, K_DARK)
c.poly([(28, 54), (33, 59), (33, 71), (28, 76), (23, 71), (23, 59)], OUT)
c.circle(28, 65, 2, K_GOLD)
# belt
c.rect(27, 71, 20, 4, K_BELT)
c.rect(34, 71, 6, 3, K_GOLD)
# tassets
c.poly([(27, 75), (47, 75), (45, 85), (29, 85)], K_MID)
# legs
c.rect(29, 85, 8, 19, K_DARK)
c.rect(37, 85, 8, 19, K_DARK)
# boots
c.rect(28, 103, 10, 9, K_BOOT)
c.rect(37, 103, 10, 9, K_BOOT)
# right arm raised, sword
c.line(45, 54, 52, 49, K_MID)
c.circle(52, 49, 3, K_DARK)
# crossguard + grip
c.line(48, 53, 57, 45, K_GOLD)
c.line(51, 51, 54, 47, K_BELT)
# blade (3px wide) pointing up-right
c.line(52, 48, 63, 27, STEEL)
c.line(51, 49, 62, 28, STEEL)
c.line(53, 47, 64, 26, STEEL)
# clash spark at the blade crossing
c.circle(64, 21, 2, MOON)
for (sx, sy) in [(61, 21), (64, 19), (67, 23), (69, 26), (62, 26), (66, 18), (63, 20), (65, 20), (63, 22), (65, 22), (60, 24), (68, 24)]:
    c.set(sx, sy, SPARK)
c.set(64, 21, EYE)

# ================= ROGUE (right, green cloak) =================
# cape behind
c.poly([(96, 48), (118, 56), (120, 90), (106, 82)], R_DK)
# pointed hood
c.poly([(92, 20), (84, 36), (100, 36)], R_HD)
c.ellipse(92, 40, 11, 10, R_HD)
c.ellipse(93, 41, 9, 4, R_BR)
# face shadow under hood
c.rect(83, 43, 18, 7, FACE)
# glowing eyes
c.rect(86, 45, 3, 2, EYE)
c.rect(95, 45, 3, 2, EYE)
# left arm raised, dagger
c.line(84, 52, 77, 48, R_MD)
c.circle(76, 47, 2, GLOVE)
# dagger blade pointing up-left
c.line(77, 46, 66, 25, STEEL)
c.line(76, 47, 65, 26, STEEL)
c.line(75, 48, 64, 27, STEEL)
# crossguard
c.line(72, 51, 79, 44, K_GOLD)
# cloak body
c.poly([(81, 48), (102, 48), (107, 108), (77, 108)], R_MD)
c.poly([(81, 48), (88, 50), (84, 100), (79, 102)], R_DK)
c.line(97, 52, 101, 102, R_BR)
# hem
c.line(78, 106, 106, 106, R_DK)
# boots hint
c.rect(80, 106, 10, 6, OUT)
c.rect(98, 106, 10, 6, OUT)

# ---- embers between them ----
for (ex, ey) in [(58, 64), (68, 72), (62, 80), (70, 62), (60, 70)]:
    c.set(ex, ey, EYE)

print(c.stats_text())
print(c.stats_text())

finish(c)
