# Forest slime monster - 32x32 RPG enemy sprite
c = new_canvas(32, 32, name="output")

# ---------------- palette ----------------
OUT    = "#16241a"   # near-black green outline
BODY   = "#5cb24e"   # mid green jelly
BODY2  = "#7ecb5f"   # light green
BODY3  = "#a9e57f"   # lighter
BODYW  = "#dcf7b6"   # specular
BODYD  = "#3d8a41"   # dark green
BODYE  = "#2a6a34"   # darkest green
MOSS   = "#2f7a37"
MOSSL  = "#4ea64a"
MOSSD  = "#1e5428"
ANT_D  = "#6b4423"   # antler dark
ANT_L  = "#c08d55"   # antler light
EYED   = "#1b2f1e"   # eye socket
EYEG   = "#a4e04a"   # glow
EYE    = "#e9ff7c"   # bright
EYEW   = "#ffffff"   # core
GLOW   = "#b7ef8a"   # light spill on body
CAP    = "#d8443a"   # mushroom red
CAPD   = "#a02c26"
CAPH   = "#f07961"
SPOT   = "#f8efdb"
STEM   = "#eeddc0"
STEMD  = "#bfa883"
MOUTH  = "#20301e"
TONGUE = "#e08a86"
BLUSH  = "#e2907c"
SHAD1  = "#16241a99"
SHAD2  = "#16241a4d"

# ---------------- body silhouette ----------------
SIL = {
    11: (13, 18),
    12: (11, 20),
    13: (10, 21),
    14: (9, 22),
    15: (8, 23),
    16: (7, 24),
    17: (7, 24),
    18: (6, 25),
    19: (6, 25),
    20: (5, 26),
    21: (5, 26),
    22: (5, 26),
    23: (4, 27),
    24: (4, 27),
    25: (4, 27),
    26: (4, 27),
    27: (5, 26),
    28: (7, 24),
    29: (10, 21),
}


def in_sil(x, y):
    if y not in SIL:
        return False
    a, b = SIL[y]
    return a <= x <= b


# 1px erosion of the silhouette -> the jelly interior
INN = {}
for y in range(32):
    xs = [x for x in range(32)
          if in_sil(x, y) and in_sil(x - 1, y) and in_sil(x + 1, y)
          and in_sil(x, y - 1) and in_sil(x, y + 1)]
    if xs:
        INN[y] = (min(xs), max(xs))


def in_inn(x, y):
    if y not in INN:
        return False
    a, b = INN[y]
    return a <= x <= b


def cfill(x0, y0, x1, y1, col):
    """fill a rect clipped to the jelly interior"""
    for y in range(y0, y1 + 1):
        if y not in INN:
            continue
        a, b = INN[y]
        for x in range(max(x0, a), min(x1, b) + 1):
            c.set(x, y, col)


def cellipse(cx, cy, rx, ry, col):
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            dx = (x - cx) / float(rx)
            dy = (y - cy) / float(ry)
            if dx * dx + dy * dy <= 1.0 and in_inn(x, y):
                c.set(x, y, col)


def px(pts, col):
    for p in pts:
        c.set(p[0], p[1], col)


def mirror(pts):
    return [(31 - x, y) for (x, y) in pts]


# ---------------- ground shadow ----------------
px([(x, 30) for x in range(9, 23)], SHAD1)
px([(7, 30), (8, 30), (23, 30), (24, 30)], SHAD2)
px([(x, 31) for x in range(11, 21)], SHAD2)

# ---------------- mushroom (behind body, over right shoulder) ----------------
CAP_OUT = {
    11: (23, 25),
    12: (22, 26),
    13: (20, 28),
    14: (19, 29),
    15: (19, 29),
    16: (20, 28),
    17: (23, 27),
}
CAP_IN = {
    12: (23, 25),
    13: (21, 27),
    14: (20, 28),
    15: (20, 28),
    16: (21, 27),
}
for y, (a, b) in CAP_OUT.items():
    c.rect(a, y, b - a + 1, 1, OUT)
# stem
c.rect(24, 16, 3, 4, OUT)
c.rect(25, 16, 2, 3, STEM)
c.set(26, 17, STEMD)
c.set(26, 18, STEMD)
# cap
for y, (a, b) in CAP_IN.items():
    c.rect(a, y, b - a + 1, 1, CAP)
c.rect(21, 16, 7, 1, CAPD)          # gill band
c.set(22, 15, CAPD); c.set(23, 16, CAPD)
px([(23, 13), (24, 12), (25, 12), (23, 12), (22, 14)], CAPH)
px([(24, 13), (26, 14), (22, 15), (27, 13)], SPOT)

# ---------------- antlers (behind body) ----------------
def antler(skel):
    for (x, y) in skel:
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx * dx + dy * dy <= 1:
                    c.set(x + dx, y + dy, ANT_D)
    px(skel, ANT_L)


# antlers: hand-authored fork shapes (left, then mirrored)
L_ANT_D = [(9, 7), (10, 7), (12, 7), (13, 7), (8, 7),
           (10, 8), (11, 8), (12, 8),
           (12, 9), (12, 10), (12, 11),
           (12, 12), (13, 12),
           (12, 13), (13, 13)]
L_ANT_L = [(9, 6), (13, 6), (8, 6),          # tine tips
           (11, 9), (11, 10), (11, 11)]      # lit beam edge
px(L_ANT_D, ANT_D)
px(L_ANT_L, ANT_L)
px(mirror(L_ANT_D), ANT_D)
px(mirror(L_ANT_L), ANT_L)

# ---------------- body ----------------
for y, (a, b) in SIL.items():
    c.rect(a, y, b - a + 1, 1, OUT)
for y, (a, b) in INN.items():
    c.rect(a, y, b - a + 1, 1, BODY)

# shading: dark toward bottom
cfill(0, 24, 31, 25, BODYD)
cfill(0, 26, 31, 29, BODYE)
# right side shadow
for y in range(13, 26):
    if y in INN:
        a, b = INN[y]
        n = 1 if y < 18 else 2
        for x in range(b - n + 1, b + 1):
            c.set(x, y, BODYD)
# left rim shadow (thin)
for y in range(15, 26):
    if y in INN:
        a, b = INN[y]
        c.set(a, y, BODYD)

# big soft light upper-left
cellipse(13, 17, 6, 5, BODY2)
cellipse(11, 15, 3, 2, BODY3)

# bounce light along the very bottom inner edge
cols = {}
for y, (a, b) in INN.items():
    for x in range(a, b + 1):
        cols.setdefault(x, []).append(y)
for x, ys in cols.items():
    ym = max(ys)
    if ym >= 24:
        c.set(x, ym, BODY2)

# ---------------- moss on the crown ----------------
moss_rows = {
    12: [(13, 18)],
    13: [(11, 20)],
    14: [(10, 13), (15, 17), (19, 21)],
    15: [(11, 12), (20, 21)],
}
for y, spans in moss_rows.items():
    for (a, b) in spans:
        for x in range(a, b + 1):
            if in_inn(x, y):
                c.set(x, y, MOSS)
px([(12, 13), (13, 12), (14, 12), (17, 12), (19, 13), (15, 13)], MOSSL)
px([(10, 14), (14, 14), (18, 14), (21, 14), (13, 15), (20, 15)], MOSSD)
# moss patch on left shoulder
px([(7, 19), (8, 18), (8, 19), (9, 19), (7, 20), (8, 20)], MOSS)
px([(8, 18), (9, 19)], MOSSL)
px([(7, 21), (8, 21)], MOSSD)
# small moss tuft right hip
px([(23, 22), (24, 22), (24, 23), (23, 23)], MOSS)
px([(24, 22)], MOSSL)

# ---------------- face ----------------
L_EYED = [(11, 17), (12, 17), (13, 17),
          (10, 18), (14, 18),
          (10, 19), (14, 19),
          (10, 20), (14, 20),
          (11, 21), (12, 21), (13, 21)]
L_EYE = {(11, 18): EYE, (12, 18): EYEW, (13, 18): EYE,
         (11, 19): EYEW, (12, 19): EYE, (13, 19): EYEG,
         (11, 20): EYEG, (12, 20): EYEG, (13, 20): EYEG}
L_GLOW = [(9, 17), (15, 17), (9, 18), (15, 18), (9, 20), (15, 20), (9, 21), (15, 21),
          (11, 16), (12, 16), (13, 16), (11, 22), (12, 22), (13, 22)]

px(L_EYED, EYED)
for (x, y), col in L_EYE.items():
    c.set(x, y, col)
for (x, y), col in L_EYE.items():
    c.set(31 - x, y, col)
px(mirror(L_EYED), EYED)
px(L_GLOW, GLOW)
px(mirror(L_GLOW), GLOW)

# mouth: small open smile
px([(14, 23), (15, 23), (16, 23), (17, 23)], MOUTH)
px([(15, 24), (16, 24)], TONGUE)

# blush
px([(9, 22), (10, 22)], BLUSH)
px(mirror([(9, 22), (10, 22)]), BLUSH)

# little jelly speckles
px([(20, 25), (11, 26), (17, 27), (23, 25)], BODY3)

# specular highlight
px([(10, 14), (11, 14), (10, 15)], BODYW)

print(c.stats_text())
view(c)
save("forest_slime", c)
finish(c)
