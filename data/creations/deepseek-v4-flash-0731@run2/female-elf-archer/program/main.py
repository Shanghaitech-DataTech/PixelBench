from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="female-elf-archer")

def reg(hex_, name):
    return c.color(hex_, name)

INK      = reg("#2B2430", "ink")
SKIN     = reg("#F6C89E", "skin")
SKIN_SH  = reg("#DFA97C", "skin_sh")
SKIN_HI  = reg("#FBDCB6", "skin_hi")
CHEEK    = reg("#F0AE8F", "cheek")
LIP      = reg("#C97B78", "lip")
EYED     = reg("#3E2A1E", "eyed")
IRIS     = reg("#C8862F", "iris")
HAIR     = reg("#2E9E62", "hair")
HAIR_D   = reg("#1F7A4B", "hair_d")
HAIR_L   = reg("#54BE7E", "hair_l")
HAIR_HI  = reg("#84D9A6", "hair_hi")
HAIR_XD  = reg("#124F38", "hair_xd")
TUNIC    = reg("#A9D9A0", "tunic")
TUNIC_L  = reg("#C8E9BC", "tunic_l")
TUNIC_D  = reg("#7FBF7E", "tunic_d")
TUNIC_XD = reg("#4E9459", "tunic_xd")
TRIM     = reg("#EAF5DA", "trim")
BELT     = reg("#8A5A33", "belt")
BELT_D   = reg("#5F3D22", "belt_d")
GOLD     = reg("#D4AF37", "gold")
WOOD     = reg("#7A5226", "wood")
WOOD_D   = reg("#543715", "wood_d")
STR      = reg("#E2D2AC", "string")
QUI      = reg("#7E5A3A", "quiver")
QUI_D    = reg("#57391F", "quiver_d")
FLETCH   = reg("#C8643C", "fletch")
FLETCH2  = reg("#E8C860", "fletch2")
STEEL    = reg("#CBD0D9", "steel")
STEEL_D  = reg("#8E94A0", "steel_d")
BOOT     = reg("#6E4A2C", "boot")
BOOT_D   = reg("#4A3020", "boot_d")
BG_A     = reg("#E9F0E0", "bg_a")
BG_B     = reg("#C9D9BE", "bg_b")
LESS    = reg("#5E9E7A", "legging")
LESS_D  = reg("#3F7A5C", "leg_d")

def px(x, y, col):
    c.set(x, y, col)

# ---------------- backdrop ----------------
c.ellipse(32, 32, 24, 26, BG_B)
c.ellipse(32, 32, 22, 24, BG_A)
c.ellipse(32, 59, 12, 3, BG_B)

# ---------------- back hair ----------------
c.ellipse(33, 24, 11, 17, HAIR)          # x22..44, y7..41
c.rect(22, 8, 2, 28, HAIR_D)             # left rim shading
c.rect(43, 8, 2, 28, HAIR_D)             # right rim shading
c.rect(22, 36, 23, 5, HAIR_D)            # lower mass

# ---------------- bow (on back, far side = our left) ----------------
c.path("M14 12 Q5 30 21 46", WOOD, fill=True)
c.path("M15 12 Q6 30 22 46", WOOD, fill=True)
c.line(16, 13, 23, 45, STR)
px(14, 11, GOLD); px(15, 12, GOLD)
px(21, 46, GOLD); px(22, 45, GOLD)
px(14, 12, WOOD_D); px(15, 12, WOOD_D)
px(23, 45, WOOD_D); px(23, 46, WOOD_D)

# ---------------- quiver & arrows (near side = our right) ----------------
c.poly([(44, 14), (51, 13), (54, 33), (47, 35)], QUI, fill=True)
c.line(44, 14, 51, 13, QUI_D)
c.line(46, 16, 45, 6, WOOD)
c.line(48, 17, 48, 4, WOOD)
c.line(50, 17, 51, 6, WOOD)
px(44, 5, STEEL); px(45, 5, STEEL); px(45, 6, STEEL)
px(47, 3, STEEL); px(48, 3, STEEL); px(48, 4, STEEL)
px(51, 5, STEEL); px(52, 6, STEEL)
px(45, 14, FLETCH); px(46, 14, FLETCH); px(46, 15, FLETCH2); px(47, 16, FLETCH)
px(48, 15, FLETCH); px(49, 16, FLETCH2); px(50, 16, FLETCH)
px(46, 19, QUI_D); px(45, 26, QUI_D); px(52, 24, QUI_D)
px(49, 18, QUI_D); px(51, 27, QUI_D)
px(47, 18, FLETCH2)

# ---------------- neck ----------------
c.rect(30, 24, 7, 4, SKIN)
c.rect(31, 25, 5, 2, SKIN_SH)

# ---------------- torso ----------------
c.rect(26, 27, 15, 3, TUNIC)
c.rect(27, 30, 13, 4, TUNIC)
c.rect(28, 33, 11, 4, TUNIC)
c.rect(29, 36, 10, 5, TUNIC)
c.rect(26, 27, 1, 14, TUNIC_XD)
c.rect(39, 27, 2, 14, TUNIC_D)
c.rect(29, 31, 12, 5, TUNIC_L)
c.rect(30, 27, 8, 2, TUNIC_D)
c.rect(31, 29, 7, 2, TRIM)

# belt
c.rect(28, 40, 11, 3, BELT)
c.rect(31, 41, 5, 3, GOLD)
px(33, 41, BELT_D); px(33, 42, BELT_D); px(33, 43, BELT_D)

# ---------------- skirt ----------------
c.rect(28, 44, 11, 2, TUNIC)
c.rect(27, 46, 13, 3, TUNIC)
c.rect(26, 49, 15, 3, TUNIC)
c.rect(25, 52, 16, 3, TUNIC)
c.rect(25, 53, 16, 2, TUNIC_D)
c.rect(25, 54, 16, 2, TUNIC_XD)

# ---------------- arms ----------------
# far arm (our left)
c.rect(24, 28, 2, 7, TUNIC)
c.rect(23, 34, 3, 6, TUNIC_D)
c.rect(23, 39, 3, 4, SKIN)
c.rect(24, 42, 3, 5, SKIN)
c.rect(24, 45, 3, 2, SKIN_SH)
# near arm (our right)
c.rect(40, 28, 3, 7, TUNIC)
c.rect(41, 34, 3, 6, TUNIC_D)
c.rect(41, 39, 3, 4, SKIN)
c.rect(41, 42, 3, 5, SKIN)
c.rect(41, 45, 3, 2, SKIN_SH)

# ---------------- legs & boots ----------------
c.rect(27, 55, 5, 4, LESS)
c.rect(32, 55, 6, 4, LESS)
c.rect(31, 55, 1, 4, LESS_D)
c.rect(27, 58, 6, 4, BOOT)
c.rect(33, 58, 6, 4, BOOT)
c.rect(26, 61, 7, 1, BOOT_D)
c.rect(32, 61, 7, 1, BOOT_D)

# ---------------- head ----------------
c.ellipse(33, 17, 6, 8, SKIN)   # x27..39, y9..25

# ears
left_ear = [(22,9), (22,10), (23,10), (23,11), (24,11), (24,12), (25,12),
           (25,13), (26,13), (26,14), (26,15)]
right_ear = [(42,10), (42,11), (41,11), (41,12), (40,12), (40,13), (39,13),
            (39,14), (38,14), (38,15)]
for x, y in left_ear:
    px(x, y, SKIN)
for x, y in right_ear:
    px(x, y, SKIN)

# face features
# brows
px(27, 13, HAIR_D); px(28, 12, HAIR_D); px(29, 12, HAIR_D); px(30, 13, HAIR_D)
px(35, 12, HAIR_D); px(36, 12, HAIR_D); px(37, 13, HAIR_D)
# far eye
px(28, 16, EYED); px(29, 15, EYED); px(30, 15, EYED); px(31, 15, EYED)
px(29, 16, IRIS); px(30, 16, IRIS); px(31, 16, EYED)
# near eye
px(35, 15, EYED); px(36, 15, EYED); px(37, 15, EYED); px(38, 16, EYED)
px(36, 16, IRIS); px(37, 16, IRIS); px(38, 17, EYED)
# nose
px(36, 18, SKIN_SH); px(37, 19, SKIN_SH)
# mouth
px(31, 21, LIP); px(32, 21, LIP); px(33, 21, LIP); px(34, 21, LIP); px(33, 22, LIP)
# cheeks
px(28, 18, CHEEK); px(29, 18, CHEEK); px(35, 18, CHEEK)
# chin light
px(33, 23, SKIN_HI)
# neck shade under chin
px(30, 25, SKIN_SH); px(31, 25, SKIN_SH); px(33, 25, SKIN_SH); px(35, 25, SKIN_SH)

# ---------------- front hair (bangs) ----------------
c.rect(24, 7, 16, 5, HAIR)          # y7..11 x24..39
c.rect(25, 9, 3, 4, HAIR)           # sides
c.rect(38, 9, 3, 4, HAIR)
c.rect(26, 12, 15, 1, HAIR)
px(28, 13, HAIR); px(29, 14, HAIR); px(31, 13, HAIR); px(34, 13, HAIR)
px(36, 13, HAIR); px(37, 14, HAIR); px(38, 13, HAIR)
px(26, 13, HAIR); px(25, 13, HAIR); px(27, 14, HAIR)
px(39, 12, HAIR); px(40, 13, HAIR)
c.rect(26, 7, 9, 2, HAIR_L)
px(30, 8, HAIR_HI); px(34, 8, HAIR_HI); px(31, 9, HAIR_HI)
# strand highlights
px(24, 9, HAIR_L); px(39, 9, HAIR_L); px(38, 11, HAIR_L)
px(35, 13, HAIR_L); px(26, 15, HAIR_L); px(25, 19, HAIR_L); px(24, 22, HAIR_L)
px(40, 14, HAIR_L); px(40, 18, HAIR_L); px(39, 22, HAIR_L)

# ---------------- front locks ----------------
c.rect(24, 12, 3, 6, HAIR)          # x24..26 y12..17
c.rect(23, 16, 3, 12, HAIR)         # x23..25 y16..27
c.rect(19, 13, 4, 10, HAIR)         # x19..22 fill between bow and lock
px(20, 25, HAIR); px(21, 26, HAIR); px(19, 23, HAIR); px(19, 24, HAIR)
px(22, 24, HAIR); px(23, 24, HAIR); px(22, 25, HAIR); px(21, 25, HAIR)
px(22, 29, HAIR); px(23, 28, HAIR); px(20, 26, HAIR)
c.rect(24, 24, 1, 4, HAIR_D)
c.rect(40, 12, 3, 5, HAIR)          # x40..42 y12..16
c.rect(39, 16, 3, 13, HAIR)         # x39..41 y16..28
px(38, 23, HAIR); px(38, 26, HAIR); px(37, 25, HAIR)
c.rect(40, 20, 1, 8, HAIR_D)
px(39, 26, HAIR); px(38, 27, HAIR)

# ---------------- decorations ----------------
# quiver strap across chest? (diagonal strap to hold quiver)
c.line(30, 29, 41, 42, QUI_D)

print(c.stats_text())
print("---- head ----")
print(c.matrix_text(region=(16, 3, 48, 28)))
print("---- body ----")
print(c.matrix_text(region=(16, 24, 50, 48)))
print("---- lower ----")
print(c.matrix_text(region=(16, 46, 46, 63)))

finish(c)
