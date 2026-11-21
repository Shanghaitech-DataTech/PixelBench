# ============ forest-slime-monster - 32x32 RPG enemy sprite ============
c = new_canvas(32, 32, name="forest-slime")

# ----- palette -----
OUT   = c.color("#1c2a15", "outline")
BODY  = c.color("#4fae4a", "body")
LITE  = c.color("#8ade6f", "body_light")
DARK  = c.color("#2f7a3d", "body_shade")
DEEP  = c.color("#1f5530", "body_deep")
MOSS  = c.color("#5d6e2a", "moss")
MOSSL = c.color("#8aa63a", "moss_light")
ANT   = c.color("#c9a06a", "antler")
ANTS  = c.color("#8f6a3e", "antler_shade")
CAP   = c.color("#d8483f", "cap_red")
CAPD  = c.color("#a02c2c", "cap_red_dark")
WHT   = c.color("#fff6e5", "white")
STEM  = c.color("#f0e3c0", "stem")
STEMS = c.color("#c9b489", "stem_shade")
GLOW  = c.color("#ffe95c", "eye_glow")
HALO  = c.color("#e2ff9a", "glow_halo")
BLUSH = c.color("#f0969f", "blush")


def px(x, y, col):
    c.set(x, y, col)


def stamp(rows, x0, y0, pal):
    painted = set()
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            col = pal.get(ch)
            if col is not None:
                px(x0 + i, y0 + j, col)
                painted.add((x0 + i, y0 + j))
    return painted


MPAL = {".": None, "O": OUT, "R": CAP, "r": CAPD, "W": WHT, "S": STEM, "s": STEMS}
APAL = {".": None, "A": ANT, "a": ANTS}

# ----- 1. red mushroom on the back (body drawn later hides the stem base) -----
MUSH = stamp([
    "....OO...",
    "...OWWO..",
    "..ORRRRO.",
    ".ORWRRWRO",
    ".OrrrrrrO",
    "...OSsO..",
    "...OSsO..",
    "...OSsO..",
], 11, 2, MPAL)

# ----- 2. tiny antlers -----
ANTLERS = stamp([
    "..A..",
    ".AA..",
    ".AA..",
    "..A..",
    "..AA.",
    "..AA.",
    "..a..",
], 8, 4, APAL) | stamp([
    "..A..",
    "..AA.",
    "..AA.",
    "..A..",
    ".AA..",
    ".AA..",
    "..a..",
], 19, 4, APAL)

# ----- 3. slime body dome -----
SPANS = [
    (10, 12, 19), (11, 10, 21), (12, 9, 22), (13, 8, 23), (14, 7, 24),
    (15, 6, 25), (16, 6, 25), (17, 5, 26), (18, 5, 26), (19, 4, 27),
    (20, 4, 27), (21, 4, 27), (22, 3, 28), (23, 3, 28), (24, 3, 28),
    (25, 3, 28), (26, 4, 27), (27, 4, 27), (28, 5, 26),
]
DRIPS = [(7, 29), (8, 29), (9, 29), (7, 30), (8, 30), (9, 30), (8, 31),
         (22, 29), (23, 29), (24, 29), (22, 30), (23, 30), (24, 30), (23, 31)]

region = set()
for y, a, b in SPANS:
    for x in range(a, b + 1):
        region.add((x, y))
region.update(DRIPS)

for x, y in region:
    px(x, y, BODY)

# -- light: top-left crescent + gloss --
for y, a, b in [(12, 10, 12), (13, 9, 12), (14, 8, 11), (15, 7, 10), (16, 7, 9),
                (17, 6, 8), (18, 6, 8), (19, 5, 7), (20, 5, 6), (21, 5, 6)]:
    for x in range(a, b + 1):
        px(x, y, LITE)
for x, y in [(10, 12), (11, 12), (10, 13), (11, 13)]:
    px(x, y, WHT)

# -- shade: right side + belly --
for y, a, b in [(13, 21, 22), (14, 22, 23), (15, 23, 24), (16, 23, 24),
                (17, 24, 25), (18, 24, 25), (19, 25, 26), (20, 25, 26),
                (21, 25, 26), (22, 26, 27), (23, 26, 27), (24, 26, 27),
                (25, 26, 27)]:
    for x in range(a, b + 1):
        px(x, y, DARK)
for x in range(12, 24):
    px(x, 26, DARK)
for x in range(6, 22):
    px(x, 27, DARK)
for x, y in [(24, 26), (25, 26), (26, 26), (22, 27), (23, 27), (24, 27), (25, 27)]:
    px(x, y, DEEP)

# -- shadow the mushroom casts on the head --
for x in range(14, 19):
    px(x, 11, DARK)

# -- silhouette outline --
for (x, y) in region:
    if any((x + dx, y + dy) not in region for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
        px(x, y, OUT)

# -- antler outline (outside the antlers, so they read on any background) --
for (x, y) in ANTLERS:
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in ANTLERS and (nx, ny) not in region and (nx, ny) not in MUSH:
            px(nx, ny, OUT)

# ----- 4. face -----
def eye(x0):
    s = set()
    for x in (x0 + 1, x0 + 2):
        s.add((x, 15)); s.add((x, 19))
    for y in (16, 17, 18):
        for x in range(x0, x0 + 4):
            s.add((x, y))
    return s

EYES = eye(10) | eye(18)
for x, y in EYES:
    px(x, y, GLOW)
px(11, 16, WHT); px(19, 16, WHT)

GLOWABLE = {BODY, LITE, DARK, DEEP}
for (x, y) in sorted(EYES):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in EYES and c.get(nx, ny) in GLOWABLE:
            px(nx, ny, HALO)

# smile
px(13, 22, OUT); px(18, 22, OUT)
for x in range(14, 18):
    px(x, 23, OUT)
# blush
for x, y in [(8, 21), (9, 21), (22, 21), (23, 21)]:
    px(x, y, BLUSH)

# ----- 5. moss clumps -----
for x, y, col in [
    (13, 12, MOSS), (14, 12, MOSSL), (13, 13, MOSS),
    (19, 12, MOSSL), (20, 12, MOSS), (20, 13, MOSS), (19, 13, MOSS),
    (24, 18, MOSS), (25, 18, MOSSL), (25, 19, MOSS), (24, 19, MOSS), (26, 19, MOSS),
    (5, 25, MOSS), (6, 25, MOSSL), (5, 26, MOSS), (6, 26, MOSS), (7, 26, MOSSL),
    (6, 27, MOSS), (26, 25, MOSS), (27, 25, MOSSL),
]:
    px(x, y, col)

print(c.stats_text())
print(c.matrix_text())
finish(c)
