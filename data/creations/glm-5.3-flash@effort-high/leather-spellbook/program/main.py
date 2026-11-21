# leather-spellbook: 32x32 RPG item portrait, <=8 colors, transparent bg
c = new_canvas(32, 32, background=None, name="leather-spellbook")

OUT    = c.color("#241a12", "outline")
LEA_D  = c.color("#4a2e1a", "leather_dark")
LEA_M  = c.color("#6b4423", "leather_mid")
LEA_L  = c.color("#8a5a30", "leather_light")
MET    = c.color("#aab4bc", "metal")
MET_D  = c.color("#5f6a72", "metal_dark")
GOLD   = c.color("#d9a441", "gold")
GOLD_D = c.color("#8a6420", "gold_dark")

# --- book silhouette (dark outline block) ---
c.rect(5, 4, 23, 24, OUT, fill=True)          # x5..27, y4..27

# --- leather body ---
c.rect(6, 5, 21, 22, LEA_M, fill=True)        # x6..26, y5..26

# --- spine (left band) ---
c.rect(6, 5, 4, 22, LEA_D, fill=True)         # x6..9
c.rect(6, 8, 4, 2, LEA_L, fill=True)          # ridge band 1
c.rect(6, 21, 4, 2, LEA_L, fill=True)         # ridge band 2
c.line(9, 5, 9, 26, OUT)                      # spine/cover seam

# --- cover shading ---
c.rect(10, 5, 17, 1, LEA_L, fill=True)        # top highlight
c.rect(10, 26, 17, 1, LEA_D, fill=True)       # bottom shade
c.rect(26, 6, 1, 20, LEA_D, fill=True)        # right shade

# --- metal corner caps (L shapes on cover corners) ---
def corner(cx, cy, sx, sy):
    # arm along x
    for i in range(4):
        c.set(cx + sx * i, cy, MET)
    # arm along y
    for i in range(1, 4):
        c.set(cx, cy + sy * i, MET)
    # dark accent on inner diagonal
    c.set(cx + sx * 2, cy + sy, MET_D)
    c.set(cx + sx, cy + sy * 2, MET_D)
    c.set(cx + sx, cy + sy, MET_D)

corner(10, 5, 1, 1)      # top-left
corner(26, 5, -1, 1)     # top-right
corner(10, 26, 1, -1)    # bottom-left
corner(26, 26, -1, -1)   # bottom-right

# --- gold clasp on right edge ---
c.rect(24, 12, 5, 8, OUT, fill=True)          # clasp outline block x24..28
c.rect(25, 13, 3, 6, GOLD, fill=True)         # x25..27, y13..18
c.rect(25, 13, 1, 6, GOLD_D, fill=True)       # left shading
c.rect(25, 18, 3, 1, GOLD_D, fill=True)       # bottom shading
c.set(27, 13, MET)                            # glint on clasp

# --- rune on cover ---
rune = [(18,13),(17,14),(18,14),(19,14),
        (16,15),(17,15),(18,15),(19,15),(20,15),
        (17,16),(18,16),(19,16),(18,17)]
for (x, y) in rune:
    c.set(x, y, GOLD)
c.set(18, 15, GOLD_D)

print(c.stats_text())

result = c
finish(result)
