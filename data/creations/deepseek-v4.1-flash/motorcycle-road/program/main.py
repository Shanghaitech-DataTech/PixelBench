W = H = 64

# ---------- 1. motorcycle layer (white background removed) ----------
bike = input_canvas.copy(name="bike")
# all pure-white pixels are the studio backdrop (incl. enclosed gaps) -> transparent
for y in range(H):
    for x in range(W):
        if bike.get(x, y) == 1:
            bike.set(x, y, "transparent")
print("bike:", bike.stats_text())

# ---------- palette ----------
SKY1 = "#63c0e6"; SKY2 = "#8ad0ee"; SKY3 = "#b3e1f4"; SKY4 = "#d4eef9"
CLOUD = "#ffffff"; CLOUDS = "#dceef7"
HFAR = "#9cb894"; HFAR2 = "#8aa884"
HNEAR = "#77a668"; HNEAR2 = "#66955a"
FIELD = "#86bb60"; FIELDL = "#a3ce78"; FIELDD = "#6b9c47"; FIELDDD = "#57813a"
TREE = "#3f7a3e"; TREEL = "#529348"; TRUNK = "#6b4a2e"
ASPH = "#7d7d80"; ASPHL = "#8e8e92"; ASPHD = "#6a6a6e"
LINE = "#f3efdf"
SHOUL = "#b6a68a"; SHOULL = "#c8b99d"
SUN = "#ffe58e"; SUNC = "#fff4c6"
SHADOW = "#5b5b60"; SHADOW2 = "#69696e"
BIRD = "#4a5a63"

sc = new_canvas(W, H, background=SKY3, name="scene")

# ---------- 2. sky gradient ----------
sc.rect(0, 0, W, 9, SKY1)
sc.dither(0, 9, W, 4, [SKY1, SKY2], pattern="checker")
sc.rect(0, 13, W, 8, SKY2)
sc.dither(0, 21, W, 4, [SKY2, SKY3], pattern="checker")
sc.rect(0, 25, W, 20, SKY3)

# sun (upper right)
sc.circle(55, 5, 4, SUN)
sc.circle(55, 5, 2, SUNC)

# clouds
def cloud(x, y, w):
    sc.rect(x + 3, y, w - 8, 1, CLOUD)
    sc.rect(x + 1, y + 1, w - 3, 1, CLOUD)
    sc.rect(x, y + 2, w, 3, CLOUD)
    sc.rect(x + 1, y + 4, w - 4, 1, CLOUDS)
    sc.rect(x + w - 4, y + 3, 3, 2, CLOUDS)

cloud(5, 5, 16)
cloud(33, 10, 13)

# small birds
for bx, by in ((24, 7), (29, 4), (20, 12)):
    sc.set(bx, by, BIRD); sc.set(bx + 1, by + 1, BIRD); sc.set(bx + 2, by, BIRD)

# ---------- 3. distant hills ----------
sc.path("M0 30 Q10 20 20 27 Q27 32 35 26 Q45 18 53 27 Q59 32 64 26 "
        "L64 35 L0 35 Z", HFAR)
sc.path("M0 27 Q6 23 12 26 Q18 29 24 25 Q30 21 36 26 Q42 31 48 27 "
        "Q54 23 60 27 Q62 29 64 28 L64 35 L0 35 Z", HFAR2)

# ---------- 4. grassland ----------
sc.rect(0, 31, W, 13, FIELD)

# near hills sitting on the field
sc.path("M0 33 Q8 27 17 31 Q26 35 36 30 Q47 25 57 32 Q61 35 64 33 "
        "L64 38 L0 38 Z", HNEAR)
sc.path("M0 37 Q12 32 24 36 Q36 40 48 34 Q56 30 64 36 L64 40 L0 40 Z", HNEAR2)

# grass texture in front of the hills
sc.dither(0, 40, W, 2, [FIELDD, FIELD], pattern="checker")
sc.rect(0, 42, W, 1, FIELDD)
sc.rect(0, 43, W, 1, FIELDDD)
for x in range(0, W, 7):
    sc.set(x, 41, FIELDDD)
    sc.set(x + 3, 40, FIELDL)

# ---------- 5. trees on the horizon ----------
# left tree
sc.circle(4, 27, 3, TREE)
sc.set(3, 25, TREEL); sc.set(4, 24, TREEL)
sc.rect(3, 29, 2, 4, TRUNK)
# right tree
sc.circle(58, 25, 4, TREE)
sc.set(57, 22, TREEL); sc.set(58, 21, TREEL); sc.set(56, 23, TREEL)
sc.set(61, 26, TREEL); sc.set(54, 27, TREEL); sc.set(62, 27, TREE)
sc.set(63, 25, TREE); sc.set(63, 26, TREE)
sc.rect(58, 28, 2, 5, TRUNK)

# ---------- 6. country road ----------
sc.rect(0, 44, W, 1, SHOUL)          # gravel shoulder / verge
sc.set(0, 44, SHOULL)
sc.rect(0, 45, W, 15, ASPH)          # asphalt rows 45..59

# asphalt grain
for y in range(45, 60):
    for x in range(W):
        k = (x * 7 + y * 13) % 17
        if k == 0:
            sc.set(x, y, ASPHL)
        elif k == 8:
            sc.set(x, y, ASPHD)

# far edge line
sc.rect(0, 46, W, 1, LINE)
# dashed centre line (rows 51-52)
for x0 in range(0, W, 11):
    sc.rect(x0, 51, 6, 2, LINE)
# near edge line
sc.rect(0, 60, W, 1, LINE)

# foreground grass verge
sc.rect(0, 61, W, 3, FIELDD)
for x in range(1, W, 5):
    sc.set(x, 61, FIELD)
    sc.set(x + 1, 61, FIELDL)
    sc.set(x + 2, 62, FIELDDD)
for x in (9, 27, 45, 60):
    sc.set(x, 60, FIELDL)
    sc.set(x + 1, 61, FIELDL)
for x in range(3, W, 9):
    sc.rect(x, 62, 3, 1, FIELDDD)

# cast shadow of the bike on the tarmac
sc.ellipse(32, 49, 21, 1, SHADOW2)
sc.ellipse(32, 49, 12, 1, SHADOW)

# a little gravel scatter on the shoulder
for x in range(0, W, 6):
    sc.set(x + 2, 44, SHOULL)
for x in range(4, W, 11):
    sc.set(x, 43, SHOUL)

# ---------- 7. put the bike on the road ----------
sc.blit(bike, 0, 0)

print("RESULT:", sc.stats_text())
save("motorcycle-road", sc)

finish(sc)
