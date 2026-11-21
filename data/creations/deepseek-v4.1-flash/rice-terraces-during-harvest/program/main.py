import math

W = H = 64

# ---------------------------------------------------------------- helpers
def clamp(v, a=0.0, b=1.0):
    return a if v < a else (b if v > b else v)


def mix(c1, c2, k):
    k = clamp(k)
    return (c1[0] + (c2[0] - c1[0]) * k,
            c1[1] + (c2[1] - c1[1]) * k,
            c1[2] + (c2[2] - c1[2]) * k)


def hsh(x, y, s=0.0):
    v = math.sin(x * 12.9898 + y * 78.233 + s * 37.719) * 43758.5453
    return v - math.floor(v)


# ---------------------------------------------------------------- palette
GOLD = [(240, 228, 194), (232, 218, 178), (222, 206, 158), (214, 194, 138),
        (206, 180, 114), (200, 170, 96), (194, 160, 82), (188, 152, 72),
        (181, 144, 62), (174, 134, 54), (164, 124, 48), (154, 114, 42),
        (144, 104, 38), (134, 96, 34), (124, 88, 32)]
GOLD_HL = (248, 240, 208)
SHADOW = [(96, 68, 30), (80, 56, 26), (64, 45, 22), (52, 36, 18)]
EARTH = [(136, 114, 76), (112, 94, 62), (90, 76, 50), (74, 62, 42)]
GRASS = [(154, 162, 96), (124, 138, 76), (98, 112, 62), (78, 92, 50)]
FOREST = [(84, 104, 62), (64, 84, 50), (46, 64, 38)]
WATER = [(172, 190, 188), (136, 160, 164), (106, 130, 140)]
HAZE = (236, 230, 212)
ROOF = [(140, 142, 152), (118, 120, 130), (96, 98, 108), (76, 78, 88)]
ROOF_HI = (168, 170, 178)
WALL = (208, 196, 170)
FARWALL = (186, 168, 138)
FALLOW = [(180, 154, 112), (164, 136, 96), (146, 118, 80), (128, 102, 68)]
OUTL = [(46, 38, 28), (66, 54, 40)]
FHAT, FHATM = (248, 236, 194), (212, 192, 148)
FBODY, FBODYL = (50, 54, 72), (84, 90, 114)
FLEG = (36, 38, 54)
SHAD = (56, 46, 32)

PAL = []
for group in (GOLD, SHADOW, EARTH, GRASS, FOREST, WATER, ROOF, OUTL, FALLOW):
    PAL.extend(group)
PAL.extend([GOLD_HL, HAZE, ROOF_HI, WALL, FARWALL, FHAT, FHATM, FBODY, FBODYL, FLEG, SHAD])
PAL = list(dict.fromkeys(PAL))


def q(col):
    best, bd = None, 1e9
    r, g, b = col
    for p in PAL:
        d = (p[0] - r) ** 2 + (p[1] - g) ** 2 + (p[2] - b) ** 2
        if d < bd:
            bd, best = d, p
    return best


# ---------------------------------------------------------------- elevation
PX, PY = 58.0, -16.0
SP0 = 8.0
VAL_A = 12.0
VAL_S = 6.5


def elev(x, y):
    r = math.hypot((x - PX) * 0.80, (y - PY))
    dv = abs(0.87 * (x - PX) + 0.49 * (y - PY)) + 3.0 * math.sin(y * 0.07 + 0.6)
    h = r - VAL_A * math.exp(-(dv / VAL_S) ** 2)
    h += 2.4 * math.sin(x * 0.085 + y * 0.05 + 0.7)
    h += 1.7 * math.sin(y * 0.135 - x * 0.045 + 1.3)
    h += 0.8 * math.sin(x * 0.21 + y * 0.19)
    return h


def band_of(x, y):
    raw = max(elev(x, y), 0.0) / SP0
    return 1.6 * raw ** 0.8


BMIN = min(band_of(x, y) for y in range(H) for x in range(W))
BMAX = max(band_of(x, y) for y in range(H) for x in range(W))
NG = len(GOLD) - 1

buf = [[None] * W for _ in range(H)]
tag = [[""] * W for _ in range(H)]

for y in range(H):
    far = clamp((18.0 - y) / 18.0)
    for x in range(W):
        band = band_of(x, y)
        i = math.floor(band)
        t = band - i
        dband = (band - BMIN) / (BMAX - BMIN)
        d = clamp(dband * (1.0 - 0.42 * far))
        idx = int(round(d * NG))
        idx = int(clamp(idx, 0, NG))

        gi = int(i - BMIN)
        green = 0.0
        if gi == 6:
            green = 0.42
        elif gi == 5:
            green = 0.20
        elif gi == 9:
            green = 0.10
        fallow = gi in (4, 8)

        bw = 0.09 + 0.035 * hsh(i, 3)
        if t < bw:
            ec = EARTH[int(hsh(i, 7) * 3.99)]
            if far > 0.35:
                ec = mix(ec, FARWALL, 0.50 * far)
            col = mix(ec, SHADOW[1], 0.25)
            tag[y][x] = "W"
        else:
            u = (t - bw) / (1.0 - bw)
            if u < 0.14:
                idx = min(NG, idx + (3 if far < 0.5 else 2))
                tag[y][x] = "s"
            elif u < 0.26 + 0.08 * far:
                idx = min(NG, idx + (1 if far < 0.55 else 0))
                tag[y][x] = "r"
            else:
                uu = (u - 0.26) / 0.74
                rowno = (band * 3.1) % 1.0
                n = hsh(x, y, 0.7)
                if idx >= 5 and rowno < 0.26 and uu > 0.2 and uu < 0.95:
                    idx = max(0, idx - 1)
                    tag[y][x] = "L"
                else:
                    if n > 0.91:
                        idx = max(0, idx - 1)
                    elif n > 0.83:
                        idx = min(NG, idx + 1)
                    tag[y][x] = "R"
            col = GOLD[idx]
            if green > 0:
                col = mix(col, GRASS[0], green)
            if fallow and green == 0:
                col = mix(col, FALLOW[int(clamp(dband * 3.99, 0, 3))], 0.62)

        fr = clamp((BMIN + 2.4 - band) / 0.55)
        if fr > 0:
            fc = mix(FOREST[0], FOREST[2], hsh(x, y, 2.3))
            col = mix(col, fc, fr * 0.92)
            tag[y][x] = "F"
        buf[y][x] = col


# ---------------------------------------------------------------- features
def put(x, y, col, tg="o"):
    if 0 <= x < W and 0 <= y < H:
        buf[y][x] = col
        tag[y][x] = tg


def is_wall(x, y):
    b = band_of(x, y)
    return (b - math.floor(b)) < 0.095


def snap(x, y, r=4):
    best, bd = (x, y), 1e9
    for yy in range(y - r, y + r + 1):
        for xx in range(x - r, x + r + 1):
            if 0 <= xx < W and 0 <= yy < H and is_wall(xx, yy):
                d = (xx - x) ** 2 + (yy - y) ** 2
                if d < bd:
                    bd, best = d, (xx, yy)
    return best


def house(x, y, w, h, hi=0):
    for j in range(h):
        for k in range(w):
            put(x + k + 1, y + j + 1, SHAD, "h")
    for j in range(h):
        for k in range(w):
            c = ROOF[hi] if j < h / 2 else ROOF[hi + 1]
            put(x + k, y + j, c, "h")
    ry = y + h // 2
    for k in range(1, w - 1):
        put(x + k, ry, ROOF_HI, "h")


def tree(x, y, big=False):
    put(x + 1, y + 1, SHAD, "t")
    if big:
        for j in range(3):
            for k in range(3):
                put(x + k, y + j, FOREST[1] if (k + j) % 3 else FOREST[2], "t")
        put(x + 1, y + 1, FOREST[0], "t")
        put(x + 2, y, FOREST[0], "t")
    else:
        put(x, y, FOREST[1], "t")
        put(x + 1, y, FOREST[0], "t")
        put(x, y + 1, FOREST[2], "t")
        put(x + 1, y + 1, FOREST[1], "t")


def farmer(x, y):
    put(x + 1, y + 5, SHAD, "f")
    put(x + 2, y + 5, SHAD, "f")
    put(x + 1, y, FHAT, "f")
    put(x + 2, y, FHAT, "f")
    put(x, y + 1, FHATM, "f")
    put(x + 1, y + 1, FHAT, "f")
    put(x + 2, y + 1, FHAT, "f")
    put(x + 3, y + 1, FHATM, "f")
    put(x + 1, y + 2, FBODY, "f")
    put(x + 2, y + 2, FBODY, "f")
    put(x, y + 3, FBODYL, "f")
    put(x + 1, y + 3, FBODY, "f")
    put(x + 2, y + 3, FBODY, "f")
    put(x + 1, y + 4, FLEG, "f")
    put(x + 2, y + 4, FLEG, "f")


def bundle(x, y):
    put(x, y, GOLD[1], "b")
    put(x + 1, y, GOLD[0], "b")
    put(x + 2, y, GOLD[2], "b")
    put(x, y + 1, GOLD[5], "b")
    put(x + 1, y + 1, GOLD[4], "b")
    put(x + 2, y + 1, GOLD[6], "b")
    put(x, y + 2, SHADOW[1], "b")
    put(x + 1, y + 2, SHADOW[1], "b")
    put(x + 2, y + 2, SHADOW[1], "b")


# village (far, top-left)
house(6, 5, 5, 3, 0)
house(14, 6, 4, 3, 1)
house(21, 4, 4, 2, 0)
house(11, 10, 4, 2, 1)
house(19, 11, 3, 2, 2)
house(26, 7, 3, 2, 1)
tree(3, 9, True)
tree(12, 3)
tree(28, 5, True)
tree(16, 14)
tree(9, 14)

# forest fringe at the summit (top right)
for (tx, ty) in ((44, 1), (49, 2), (54, 1), (58, 3), (61, 1),
                 (46, 5), (52, 5), (57, 6), (62, 6)):
    tree(tx, ty)

# farmers on narrow ridges
fa = snap(37, 47, 5)
fb = snap(23, 52, 5)
print("farmer A wall", fa, " farmer B wall", fb)
farmer(fa[0] - 2, fa[1] - 4)
farmer(fb[0] - 2, fb[1] - 4)
bundle(fa[0] + 5, fa[1] + 2)
bundle(fa[0] + 9, fa[1] + 1)

# ---------------------------------------------------------------- canvas
c = new_canvas(W, H, background=None, name="result")
for y in range(H):
    for x in range(W):
        c.set(x, y, q(buf[y][x]))

used = {}
for y in range(H):
    for x in range(W):
        used[c.get(x, y)] = used.get(c.get(x, y), 0) + 1
print("distinct palette entries used:", len(used))
print(c.stats_text())

print("tag map (W wall, s shadow, r rice-dark, R rice, F forest, h house, t tree, f farmer, b bundle):")
for y in range(H):
    print("%2d %s" % (y, "".join((tag[y][x] or ".") for x in range(W))))

ramp = " ..::--==++**xX#%@"
print("luma map:")
for y in range(H):
    row = ""
    for x in range(W):
        r, g, b = buf[y][x]
        L = (0.30 * r + 0.59 * g + 0.11 * b) / 255.0
        row += ramp[min(len(ramp) - 1, int((1.0 - L) * len(ramp)))]
    print("%2d %s" % (y, row))

print("village region:")
print(c.matrix_text(region=(1, 1, 32, 17)))
print("farmer A region:")
print(c.matrix_text(region=(32, 39, 50, 51)))

hist = {}
for y in range(H):
    for x in range(W):
        gi = int(math.floor(band_of(x, y)) - BMIN)
        hist[gi] = hist.get(gi, 0) + 1
print("terrace-band histogram:", dict(sorted(hist.items())))

# ---------------------------------------------------------------- export
print(save("rice_terraces_harvest", c))
finish(c)
