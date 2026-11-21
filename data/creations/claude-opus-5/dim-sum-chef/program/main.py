c = new_canvas(32, 32, name="output")

OL     = "#241a14"
SKIN   = "#edb98a"
SKIN_S = "#cf9268"
HAIR   = "#2b1d16"
HAT    = "#fbfdff"
HAT_S  = "#d4dae3"
JKT    = "#f2f5f8"
JKT_S  = "#c7d0da"
APR    = "#cdb68d"
APR_S  = "#a8906a"
FLR    = "#fffdf6"
BAM    = "#c7974f"
BAM_L  = "#e4ba7b"
BAM_D  = "#8c6227"
BUN    = "#ffeccd"
BUN_S  = "#e6c795"
BUN_D  = "#c9a46d"
RED    = "#b4463a"

# ================= hat (rows 0-5) =================
c.rect(11, 0, 10, 1, OL)
c.rect(9, 1, 14, 3, OL)
c.rect(10, 4, 12, 2, OL)
c.rect(12, 0, 8, 1, HAT)
c.rect(10, 1, 12, 2, HAT)
c.rect(10, 3, 12, 1, HAT_S)
c.rect(11, 4, 10, 1, HAT)
c.rect(11, 5, 10, 1, HAT_S)
c.rect(19, 1, 3, 1, HAT_S)
c.set(21, 2, HAT_S)

# ================= head (rows 6-14) =================
c.rect(10, 6, 12, 9, OL)
c.rect(11, 6, 10, 2, HAIR)
c.rect(11, 8, 10, 5, SKIN)
c.rect(11, 13, 10, 1, SKIN)
c.rect(12, 14, 8, 1, SKIN_S)
c.set(11, 8, HAIR)
c.set(20, 8, HAIR)
c.rect(13, 9, 2, 1, OL)           # eyes
c.rect(17, 9, 2, 1, OL)
c.set(16, 11, SKIN_S)             # nose
c.set(12, 11, SKIN_S)             # cheeks
c.set(19, 11, SKIN_S)
c.rect(15, 12, 2, 1, OL)          # mouth
c.set(20, 12, SKIN_S)
c.set(20, 13, SKIN_S)

# ================= jacket (rows 15-31) =================
c.rect(8, 15, 16, 17, OL)
c.rect(9, 16, 14, 16, JKT)
c.rect(10, 15, 12, 1, JKT)
c.rect(22, 16, 1, 16, JKT_S)
c.rect(4, 16, 5, 9, OL)           # left sleeve
c.rect(5, 17, 3, 7, JKT)
c.rect(7, 17, 1, 7, JKT_S)
c.rect(23, 16, 5, 9, OL)          # right sleeve
c.rect(24, 17, 3, 7, JKT)
c.rect(26, 17, 1, 7, JKT_S)

c.rect(13, 15, 6, 1, RED)         # mandarin collar
c.set(13, 16, RED)
c.set(18, 16, RED)
c.rect(14, 16, 4, 1, JKT_S)
c.set(15, 17, RED)                # frog buttons
c.set(16, 19, RED)

# ================= apron (rows 17-31) =================
c.rect(10, 17, 12, 15, APR)
c.rect(10, 17, 12, 1, APR_S)
c.rect(21, 18, 1, 14, APR_S)
c.line(12, 17, 13, 15, APR)       # bib straps
c.line(19, 17, 18, 15, APR)
c.set(14, 16, APR)
c.set(17, 16, APR)
c.rect(10, 20, 12, 1, APR_S)      # waist band
c.set(13, 17, APR_S)
c.set(18, 17, APR_S)
for fx, fy in [(11, 18), (14, 18), (19, 19), (12, 19), (20, 18),
               (11, 31), (14, 30), (17, 31), (20, 30), (12, 30),
               (6, 19), (25, 20), (15, 30), (18, 30)]:
    c.set(fx, fy, FLR)

# ================= buns (rows 21-24) =================
def bun(x0, mark=None):
    # dome, 6 px wide (x0..x0+5), rows 20-24
    c.rect(x0 + 2, 20, 2, 1, OL)
    c.set(x0 + 1, 21, OL)
    c.set(x0 + 4, 21, OL)
    c.rect(x0 + 2, 21, 2, 1, BUN)
    for y in (22, 23, 24):
        c.set(x0, y, OL)
        c.set(x0 + 5, y, OL)
        c.rect(x0 + 1, y, 4, 1, BUN)
    c.set(x0 + 4, 22, BUN_S)
    c.rect(x0 + 3, 23, 2, 1, BUN_S)
    c.rect(x0 + 1, 24, 4, 1, BUN_S)
    c.set(x0 + 4, 24, BUN_D)
    c.set(x0 + 1, 22, BUN)
    if mark:
        c.set(x0 + 2, 22, mark)

bun(7)
bun(13, RED)
bun(19)

# ================= bamboo steamer (rows 24-29) =================
c.rect(5, 24, 1, 6, OL)
c.rect(26, 24, 1, 6, OL)
c.rect(6, 25, 20, 1, BAM_L)
c.rect(6, 26, 20, 1, BAM)
c.rect(6, 27, 20, 1, BAM)
c.rect(6, 28, 20, 1, BAM_D)
c.rect(5, 29, 22, 1, OL)
for wx in (8, 11, 14, 17, 20, 23):
    c.set(wx, 26, BAM_D)
    c.set(wx, 27, BAM_D)
c.set(6, 25, BAM)
c.set(25, 25, BAM)

# ================= hands gripping the rim =================
c.rect(2, 23, 5, 6, OL)
c.rect(3, 24, 3, 4, SKIN)
c.rect(3, 27, 3, 1, SKIN_S)
c.set(5, 24, SKIN_S)
c.rect(25, 23, 5, 6, OL)
c.rect(26, 24, 3, 4, SKIN)
c.rect(26, 27, 3, 1, SKIN_S)
c.set(26, 24, SKIN_S)

view(c)
print(c.stats_text())
finish(c)
