import math

W = H = 64
c = new_canvas(W, H, name="rice-terraces-harvest")


# ---------------- palette ----------------
def C(hexv, name):
    return c.color(hexv, name=name)


FOREST   = C("#33502c", "forest")
FOREST_D = C("#26401f", "forest_dark")
TREE_L   = C("#4d6b36", "tree_light")
HAZE     = C("#d9ca97", "valley_haze")
MIST     = C("#e9dfb4", "mist")
ROOF     = C("#5c4632", "roof")
ROOF_L   = C("#77593d", "roof_ridge")
WALL     = C("#c7b184", "wall")
DOOR     = C("#3f3222", "door")
PATH     = C("#ddcda4", "ridge_path")
PATH_D   = C("#bda97c", "path_wear")
F1       = C("#d9c684", "paddy_far_a")
F2       = C("#cbb972", "paddy_far_b")
M1       = C("#d2ad58", "paddy_mid_a")
M2       = C("#c19a45", "paddy_mid_b")
N1       = C("#d6a94e", "paddy_near_a")
N2       = C("#c99f42", "paddy_near_b")
N3       = C("#b78d33", "paddy_near_c")
STUB     = C("#dfc67e", "stubble_field")
STUB_L   = C("#b89a4e", "stubble_cut")
BUND_F   = C("#a98c55", "bund_far")
BUND_FD  = C("#8a7142", "bund_far_dark")
MUD      = C("#6b4b26", "bund")
MUD_D    = C("#52381b", "bund_dark")
WATER    = C("#4c6a5e", "channel")
WATER_L  = C("#7e9c8c", "channel_glint")
SHADE    = C("#a8843a", "band_shade")
SHADE_L  = C("#bb9a4d", "band_shade_soft")
FAR_DOT  = C("#b7ab72", "far_rice")
SHIRT    = C("#4f5f7a", "farmer_shirt")
STALK_D  = C("#a37c2c", "rice_dark")
STALK_L  = C("#eed88f", "rice_light")
SHEAF    = C("#8a651f", "sheaf")
SHEAF_L  = C("#e8cf7a", "sheaf_bind")
HAT      = C("#f0e4c2", "hat")
HAT_D    = C("#d2c193", "hat_shade")
BODY     = C("#3c3833", "farmer")
BASKET   = C("#a3763a", "basket")


# ---------------- terrace geometry ----------------
LEVELS = [9, 12, 15, 18, 21, 24, 29, 34, 39, 44, 51, 58, 69]


def contour(x, j):
    """Boundary line j: wavy contour following the hillside."""
    a = 1.6 + 0.28 * j
    return (LEVELS[j]
            + a * math.sin((x - 10) / 9.0)
            + 0.7 * math.sin((2.0 * x + 3.0 * j) / 7.0))


def ic(x, j):
    return int(round(contour(x, j)))


def rnd(x, y, s=0):
    v = (x * 374761393 + y * 668265263 + s * 2654435761) & 0xFFFFFFFF
    v ^= v >> 13
    v = (v * 1274126177) & 0xFFFFFFFF
    v ^= v >> 16
    return (v & 0xFFFF) / 65535.0


tops = [[ic(x, j) for x in range(W)] for j in range(13)]

# 1. distant valley floor behind the village
c.rect(0, 0, W, 13, HAZE)
for x in range(W):
    y = tops[0][x] - 1
    if y > 3 and rnd(x, y, 3) < 0.5:
        c.set(x, y, F2)
    y = tops[0][x] - 2
    if y > 3 and rnd(x, y, 4) < 0.3:
        c.set(x, y, F1)

# 2. forest crest along the top edge
c.rect(0, 0, W, 3, FOREST)
for x in range(W):
    if (x * 7 + 3) % 5 < 2:
        c.set(x, 1, FOREST_D)
    if x % 3 == 1:
        c.set(x, 0, TREE_L)


# 3. village in the distance
def house(x, y, w):
    c.rect(x, y, w, 3, ROOF)
    c.line(x, y + 1, x + w - 1, y + 1, ROOF_L)
    c.rect(x + 1, y + 3, w - 2, 1, WALL)
    c.set(x + w // 2, y + 3, DOOR)


house(7, 2, 5)
house(17, 3, 4)
house(26, 2, 4)
house(38, 3, 5)
house(49, 2, 4)


def tree3(x, y):
    c.circle(x, y, 1, FOREST)
    c.set(x, y, TREE_L)


for (tx, ty) in [(3, 5), (15, 6), (24, 4), (35, 6), (46, 5), (57, 6), (61, 3)]:
    tree3(tx, ty)

# 4. paddy bands between contours (light + hazy far, rich near)
BAND_COLORS = [F1, F2, F1, F2, F1, M1, M2, M1, M2, N1, N2, N3]
for j in range(12):
    pts = [(x, tops[j][x]) for x in range(W)]
    pts += [(x, tops[j + 1][x]) for x in range(W - 1, -1, -1)]
    c.poly(pts, BAND_COLORS[j], fill=True)

# haze wisps drifting over the far terraces
for j in range(1, 5):
    for x in range(W):
        if rnd(x, j, 91) < 0.045:
            y = int(round(contour(x, j) + 0.5 * (contour(x, j + 1) - contour(x, j))))
            if tops[j][x] < y < tops[j + 1][x]:
                c.set(x, y, MIST)

# relief shade just above each bund (mid + near ground only)
for j in range(5, 12):
    for x in range(W):
        yb = tops[j + 1][x]
        if yb - 1 > tops[j][x]:
            c.set(x, yb - 1, SHADE_L if j < 8 else SHADE)

# 5. rice rows following the contours + scattered plants
for j in range(12):
    base = BAND_COLORS[j]
    dot_main = STALK_D if base in (F1, M1, N1) else STALK_L
    dot_alt = STALK_L if dot_main is STALK_D else STALK_D
    if j < 5:
        dot_main, dot_alt = FAR_DOT, F2
    if j < 5:
        rows = [(0.5, 0.5)]
        dens = 0.05
    elif j < 9:
        rows = [(0.35, 0.6), (0.72, 0.55)]
        dens = 0.08
    else:
        rows = [(0.28, 0.7), (0.55, 0.7), (0.8, 0.6)]
        dens = 0.10
    for x in range(W):
        ytf = contour(x, j)
        ybf = contour(x, j + 1)
        for (t, p) in rows:
            y = int(round(ytf + t * (ybf - ytf)))
            if 0 <= y < H and rnd(x, y, 11 + j) < p:
                c.set(x, y, dot_alt if rnd(x, y, 31 + j) < 0.25 else dot_main)
        for y in range(int(ytf) + 1, min(int(ybf), H - 1) + 1):
            if rnd(x, y, 57 + j) < dens:
                c.set(x, y, dot_alt if rnd(x, y, 71 + j) < 0.3 else dot_main)

# 6. bunds, ridge paths, mist line, water channel
PATH_J = {3, 7, 10}
for j in range(1, 12):
    for x in range(W):
        y = tops[j][x]
        if j in PATH_J:
            c.set(x, y, PATH_D if x % 7 == 3 else PATH)
        elif j == 5:
            c.set(x, y, MUD if x % 5 == 0 else MIST)
        elif j == 8:
            c.set(x, y, WATER_L if x % 9 == 4 else WATER)
        elif j <= 4:
            c.set(x, y, BUND_FD if x % 5 == 2 else BUND_F)
        else:
            c.set(x, y, MUD_D if x % 5 == 2 else MUD)


# 7. harvested stubble patches
def patch(j, x0, x1):
    for x in range(x0, x1 + 1):
        yt = int(math.ceil(contour(x, j))) + 1
        yb = int(math.floor(contour(x, j + 1))) - 1
        for y in range(max(yt, 0), min(yb, H - 1) + 1):
            c.set(x, y, STUB)
            if (x + y) % 2 == 0 and rnd(x, y, 5) < 0.55:
                c.set(x, y, STUB_L)


patch(9, 38, 62)
patch(11, 6, 30)


# 8. sheaf stacks
def sheaf(x, j):
    y = int(round((contour(x, j) + contour(x, j + 1)) / 2)) - 1
    c.set(x, y, SHEAF)
    c.set(x + 1, y, SHEAF)
    c.set(x, y + 1, SHEAF_L)
    c.set(x + 1, y + 1, SHEAF)
    c.set(x + 1, y + 2, MUD_D)


for (sx, sj) in [(50, 9), (30, 9), (14, 10), (50, 11), (56, 11), (44, 8)]:
    sheaf(sx, sj)

# 9. village path switchbacking down to the ridges
segs = [((26, 7), (22, 12)), ((22, 12), (27, 16)), ((27, 16), (23, 21)),
        ((23, 21), (28, 25)), ((28, 25), (24, 30)), ((24, 30), (28, 33)),
        ((28, 33), (26, 37))]
for (a, b) in segs:
    c.line(a[0], a[1], b[0], b[1], PATH)
    L = max(abs(b[0] - a[0]), abs(b[1] - a[1]))
    for i in range(0, L + 1, 4):
        t = (i / L) if L else 0.0
        c.set(int(round(a[0] + (b[0] - a[0]) * t)),
              int(round(a[1] + (b[1] - a[1]) * t)), PATH_D)


# 10. lone trees on the slopes
def tree2(x, y):
    c.set(x, y, FOREST)
    c.set(x + 1, y, FOREST)
    c.set(x, y + 1, TREE_L)
    c.set(x + 1, y + 1, FOREST)
    c.set(x + 1, y + 2, MUD_D)


tree2(2, 29)
tree2(60, 41)
tree2(8, 47)


# 11. two farmers on the narrow ridges
def farmer(x, y, pole=False, shirt=BODY):
    c.set(x, y - 2, HAT)
    c.set(x + 1, y - 2, HAT_D)
    c.set(x, y - 1, HAT_D)
    c.set(x + 1, y - 1, HAT)
    c.set(x, y, shirt)
    c.set(x + 1, y, MUD_D)
    if pole:
        c.set(x - 1, y - 1, MUD)
        c.set(x + 2, y - 1, MUD)
        c.set(x - 1, y, BASKET)
        c.set(x + 2, y, BASKET)


farmer(20, tops[7][20], shirt=SHIRT)
farmer(42, tops[10][42], pole=True)

# ---------------- report ----------------
print(c.stats_text())
print("palette size:", len(c.palette()))
print("--- village / far zone ---")
print(c.matrix_text(region=(0, 0, 40, 16)))
print("--- farmer A ---")
print(c.matrix_text(region=(14, 32, 34, 44)))
print("--- farmer B ---")
print(c.matrix_text(region=(34, 42, 54, 54)))

view(c)
save("rice-terraces-harvest", c)
finish(c)
