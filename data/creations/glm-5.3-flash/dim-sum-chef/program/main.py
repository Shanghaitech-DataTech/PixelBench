# ============================================================
#  Dim Sum Chef - 32x32 front-facing character sprite
#  toque, smiling face, white jacket, flour-dusted teal apron,
#  bamboo steamer held in both hands with bao buns inside
# ============================================================

c = new_canvas(32, 32, background=None, name="dim_sum_chef")

# ---------------- palette ----------------
C_OUT    = c.color("#2B2018", "outline")
C_HAT    = c.color("#FDFCF7", "hat")
C_HATS   = c.color("#D9D3C0", "hat_shade")
C_HAIR   = c.color("#4A3226", "hair")
C_SKIN   = c.color("#F2C79B", "skin")
C_SKINS  = c.color("#D69C6A", "skin_shade")
C_BLUSH  = c.color("#E89A85", "blush")
C_MOUTH  = c.color("#B0564A", "mouth")
C_JKT    = c.color("#EDEDE2", "jacket")
C_JKTS   = c.color("#C2C2B4", "jacket_shade")
C_APRON  = c.color("#3E5C6B", "apron")
C_APRONS = c.color("#2C4450", "apron_shade")
C_FLOUR  = c.color("#FFFDF2", "flour")
C_BAM    = c.color("#C89355", "bamboo")
C_BAMS   = c.color("#A06F35", "bamboo_shade")
C_BAMD   = c.color("#7A4E22", "bamboo_dark")
C_BUN    = c.color("#F7E3B8", "bun")
C_BUNS   = c.color("#DBBB82", "bun_shade")
C_INTER  = c.color("#5C3A1E", "steamer_gap")
C_SHOE   = c.color("#4A3527", "shoe")
C_PANTS  = c.color("#5A5F6B", "trousers")

# ---------------- span painter ----------------
S = []
def sp(y, x0, x1, col):
    S.append((y, x0, x1, col))

# ---- toque ----
sp(0, 12, 19, C_HAT)
sp(1, 10, 21, C_HAT)
sp(2, 10, 21, C_HAT)
sp(3, 10, 21, C_HAT)
sp(4, 11, 20, C_HATS)                      # hat band
for yy in (1, 2, 3):                       # pleat seams
    sp(yy, 13, 13, C_HATS)
    sp(yy, 18, 18, C_HATS)

# ---- head ----
sp(5, 12, 19, C_HAIR)                      # fringe
sp(6, 11, 20, C_SKIN); sp(6, 11, 11, C_HAIR); sp(6, 20, 20, C_HAIR)
sp(7, 11, 20, C_SKIN); sp(7, 11, 11, C_HAIR); sp(7, 20, 20, C_HAIR)
sp(8, 11, 20, C_SKIN); sp(8, 13, 13, C_OUT); sp(8, 18, 18, C_OUT)
sp(9, 11, 20, C_SKIN); sp(9, 13, 13, C_OUT); sp(9, 18, 18, C_OUT)
sp(10, 11, 20, C_SKIN)
sp(10, 12, 12, C_BLUSH); sp(10, 19, 19, C_FLOUR)      # blush + flour smudge
sp(10, 15, 16, C_SKINS)                               # nose
sp(11, 11, 20, C_SKIN); sp(11, 14, 17, C_MOUTH)       # smile
sp(12, 12, 19, C_SKIN); sp(12, 12, 12, C_SKINS); sp(12, 19, 19, C_SKINS)

# ---- collar, torso, sleeves ----
sp(13, 11, 12, C_JKT); sp(13, 13, 14, C_JKTS)
sp(13, 15, 16, C_SKIN)                                 # neck
sp(13, 17, 18, C_JKTS); sp(13, 19, 20, C_JKT)
sp(14, 9, 22, C_JKT);  sp(14, 9, 9, C_JKTS);  sp(14, 22, 22, C_JKTS)
sp(15, 8, 23, C_JKT);  sp(15, 9, 9, C_JKTS);  sp(15, 22, 22, C_JKTS)
sp(16, 7, 24, C_JKT);  sp(16, 9, 9, C_JKTS);  sp(16, 22, 22, C_JKTS)
sp(17, 6, 25, C_JKT);  sp(17, 9, 9, C_JKTS);  sp(17, 22, 22, C_JKTS)
sp(18, 6, 25, C_JKT);  sp(18, 9, 9, C_JKTS);  sp(18, 22, 22, C_JKTS)
sp(16, 9, 9, C_FLOUR); sp(16, 22, 22, C_FLOUR)         # flour on jacket sides

# ---- steamer far rim ----
sp(15, 10, 21, C_BAMS)

# ---- steamer opening + bao buns ----
# dark interior shows around and between the buns
sp(16, 10, 21, C_INTER)
for yy in (17, 18):
    sp(yy, 10, 10, C_INTER); sp(yy, 13, 14, C_INTER)
    sp(yy, 17, 18, C_INTER); sp(yy, 21, 21, C_INTER)
# three bao, 2 px wide, dark gaps keep them clearly separated
sp(16, 11, 12, C_BUN); sp(16, 15, 16, C_BUN); sp(16, 19, 20, C_BUN)
for yy in (17, 18):
    sp(yy, 11, 12, C_BUN); sp(yy, 12, 12, C_BUNS)
    sp(yy, 15, 16, C_BUN); sp(yy, 16, 16, C_BUNS)
    sp(yy, 19, 20, C_BUN); sp(yy, 20, 20, C_BUNS)

# ---- bamboo steamer body ----
sp(19, 6, 25, C_BAMS)                                  # top rim
sp(19, 6, 6, C_BAMD); sp(19, 25, 25, C_BAMD)
for yy in (20, 21, 22, 23):
    sp(yy, 6, 25, C_BAM)
sp(24, 6, 25, C_BAMD)                                  # base hoop
for yy in (20, 21, 22, 23):                            # vertical weave
    for xx in (9, 13, 17, 21):
        sp(yy, xx, xx, C_BAMS)
sp(22, 10, 12, C_BAMS); sp(22, 14, 16, C_BAMS); sp(22, 18, 20, C_BAMS)

# ---- hands gripping the rim ----
# left
for yy in (18, 19, 20, 21):
    sp(yy, 4, 8, C_OUT)
sp(18, 5, 7, C_SKIN); sp(19, 5, 7, C_SKIN); sp(20, 5, 7, C_SKIN)
sp(19, 7, 7, C_SKINS); sp(20, 7, 7, C_SKINS)
# right
for yy in (18, 19, 20, 21):
    sp(yy, 23, 27, C_OUT)
sp(18, 24, 26, C_SKIN); sp(19, 24, 26, C_SKIN); sp(20, 24, 26, C_SKIN)
sp(19, 24, 24, C_SKINS); sp(20, 24, 24, C_SKINS)

# ---- flour-dusted apron ----
sp(25, 9, 22, C_APRONS)                                # waistband / steamer shadow
sp(26, 9, 22, C_APRON)
sp(27, 9, 22, C_APRON)
sp(28, 9, 22, C_APRONS)                                # hem
sp(26, 11, 11, C_FLOUR); sp(26, 16, 16, C_FLOUR); sp(26, 20, 20, C_FLOUR)
sp(27, 10, 10, C_FLOUR); sp(27, 13, 14, C_FLOUR); sp(27, 18, 18, C_FLOUR)

# ---- trousers + shoes ----
sp(29, 10, 13, C_PANTS); sp(29, 18, 21, C_PANTS)
sp(30, 10, 14, C_SHOE); sp(30, 17, 21, C_SHOE)
sp(31, 9, 14, C_SHOE);  sp(31, 17, 22, C_SHOE)

# ---------------- paint ----------------
for yy, x0, x1, col in S:
    for xx in range(x0, x1 + 1):
        c.set(xx, yy, col)

# clean dark contour around the whole silhouette
c.outline(C_OUT)

print(c.stats_text())
print(c.matrix_text())

save("dim_sum_chef", c)
finish(c)
