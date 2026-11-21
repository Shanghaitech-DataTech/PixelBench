import math

c = new_canvas(64, 64, name="output")


def mix(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def hx(t):
    return "#%02x%02x%02x" % t


def ramp(t, anchors):
    t = min(max(t, 0.0), 1.0)
    for i in range(len(anchors) - 1):
        t0, c0 = anchors[i]
        t1, c1 = anchors[i + 1]
        if t <= t1:
            return mix(c0, c1, (t - t0) / (t1 - t0))
    return anchors[-1][1]


GOLD = [(0.0, (124, 128, 90)), (0.22, (158, 150, 84)),
        (0.50, (198, 170, 90)), (0.75, (229, 198, 110)),
        (1.0, (247, 226, 152))]
WALLR = [(0.0, (120, 118, 94)), (0.45, (142, 118, 80)), (1.0, (104, 76, 48))]
LIPR = [(0.0, (176, 178, 148)), (0.5, (224, 208, 150)), (1.0, (253, 240, 186))]


# ------------------------------------------------- contour geometry
def wave(x, phase=0.0):
    return (0.62 * math.sin(x * 0.088 + 0.5 + phase)
            + 0.30 * math.sin(x * 0.165 - 1.2)
            + 0.14 * math.sin(x * 0.047 + 2.3))


HZ = [int(round(9 + 1.8 * math.sin(x * 0.10 + 0.8) + 1.2 * math.sin(x * 0.045))) for x in range(64)]

SPACING = [2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
N = len(SPACING)
bases, acc = [], 11.0
for s in SPACING:
    bases.append(acc)
    acc += s

bounds = []
for k in range(N):
    amp = 1.7 + 5.2 * (k / float(N - 1)) ** 1.25
    bounds.append([bases[k] + amp * wave(x) for x in range(64)])
bounds.append([90.0] * 64)

BAND = [[-1] * 64 for _ in range(64)]
for x in range(64):
    for k in range(N):
        y0 = int(round(bounds[k][x]))
        if k == 0:
            y0 = HZ[x] + 1          # band 0 reaches up to the hill crest, no gaps
        else:
            y0 = max(y0, HZ[x] + 1)
        y1 = min(int(round(bounds[k + 1][x])), 64)
        for y in range(y0, y1):
            BAND[y][x] = k

# ------------------------------------------------- band palettes
harvested = {11, 8, 5, 2}
green = {10, 6, 1}
fill_col, var_col, wall_col, lip_col = [], [], [], []
for k in range(N):
    t = k / float(N - 1)
    g = ramp(t, GOLD)
    if k in harvested:
        g = mix(g, (208, 192, 150), 0.40)
    if k in green:
        g = mix(g, (138, 156, 86), 0.42)
    # aerial haze on the far bands: cooler, lower contrast with distance
    haze = max(0.0, 0.34 - 0.075 * k)
    if haze > 0:
        g = mix(g, (172, 180, 158), haze)
    fill_col.append(hx(g))
    if k in harvested:
        v = mix(g, (162, 142, 100), 0.32)
    elif k in green:
        v = mix(g, (98, 118, 62), 0.30)
    else:
        v = mix(g, (108, 96, 54), 0.24)
    var_col.append(hx(v))
    wall_col.append(hx(ramp(round(t * 4) / 4.0, WALLR)))
    lip_col.append(hx(ramp(round(t * 3) / 3.0, LIPR)))

# ------------------------------------------------- sky, distant hills
for y in range(14):
    for x in range(64):
        if y > HZ[x]:
            continue
        if y <= 1:
            col = "#c9cfbf"
        elif y <= 3:
            col = "#b0baa3"
        elif y <= 5:
            col = "#94a084"
        elif y <= 7:
            col = "#7c886b"
        else:
            col = "#677557"
        c.set(x, y, col)

for x in range(64):
    hy = HZ[x]
    c.set(x, hy, "#52644a")
    c.set(x, hy - 1, "#5e7050" if (x % 3) else "#485a41")

# ------------------------------------------------- village
WALLC = "#b8ad92"
WALL2 = "#8e8671"
ROOF = "#7a4a37"
ROOF2 = "#5a352a"


def house(x, y, w, big=True):
    rh = 2 if big else 1
    c.rect(x, y, w, rh, ROOF)
    c.set(x, y, ROOF2)
    c.set(x + w - 1, y, ROOF2)
    c.rect(x, y + rh, w, 1, WALLC)
    c.set(x, y + rh, WALL2)
    c.set(x + w - 1, y + rh, WALL2)


house(16, 4, 4, True)
house(24, 6, 3, True)
house(33, 3, 4, True)
house(40, 6, 3, False)
house(10, 6, 3, False)
house(47, 4, 3, True)
house(55, 6, 3, False)
for (tx, ty) in [(22, 4), (31, 6), (38, 3), (45, 6), (52, 6), (14, 7), (8, 4),
                 (58, 4), (29, 2), (44, 2), (5, 7), (62, 6)]:
    c.set(tx, ty, "#3d5440")
    c.set(tx, ty + 1, "#304634")

# ------------------------------------------------- terrace fills
for y in range(64):
    for x in range(64):
        k = BAND[y][x]
        if k < 0:
            continue
        if k in harvested:
            use = ((x + 2 * (y % 2)) % 5 == 0) or ((x * 2 + y) % 13 == 0)
        else:
            use = ((x * 3 + y * 5) % 9 == 0) or ((x + y * 2) % 17 == 0)
        c.set(x, y, var_col[k] if use else fill_col[k])

# stubble rows on harvested terraces
for y in range(64):
    for x in range(64):
        k = BAND[y][x]
        if k in harvested and k >= 5:
            top = int(round(bounds[k][x]))
            if (y - top) % 2 == 1 and x % 2 == 0:
                c.set(x, y, var_col[k])

# flooded terraces: whole bands of water, so they read as paddies not puddles
POOL_NEAR = ["#aebaa4", "#c6cfb4", "#98a692"]
POOL_FAR = ["#97a294", "#a9b2a2", "#869186"]
for k in (9, 3):
    pool = POOL_NEAR if k >= 9 else POOL_FAR
    for x in range(64):
        y0 = max(int(round(bounds[k][x])), 1)
        y1 = min(int(round(bounds[k + 1][x])) - 1, 64)
        for y in range(y0, y1):
            if BAND[y][x] == k:
                if (x * 2 + y * 3) % 9 == 0:
                    col = pool[1]
                elif (x + y) % 11 == 0:
                    col = pool[2]
                else:
                    col = pool[0]
                c.set(x, y, col)

# ------------------------------------------------- walls and sunlit lips
for x in range(64):
    for k in range(N):
        y_top = max(int(round(bounds[k][x])), HZ[x] + 1)
        y_bot = min(int(round(bounds[k + 1][x])), 64)
        if y_bot - y_top < 1:
            continue
        if k >= 4 and y_bot - y_top >= 3 and x % 5 != 3:
            c.set(x, y_bot - 1, lip_col[k])
        if y_bot < 64 and BAND[y_bot][x] >= 0:
            c.set(x, y_bot, wall_col[BAND[y_bot][x]])

# ------------------------------------------------- footpaths along ridges
PATH = "#c6af8a"
PATH2 = "#a08a66"


def draw_path(x0, x1, k):
    pts = []
    for x in range(x0, x1 + 1):
        y = min(int(round(bounds[k + 1][x])) - 1, 63)
        if y < 1 or BAND[y][x] < 0:
            continue
        c.set(x, y, PATH)
        if y + 1 < 64:
            c.set(x, y + 1, PATH2)
        pts.append((x, y))
    return pts


p_near = draw_path(2, 46, 12)
p_low = draw_path(1, 40, 10)
p_hi = draw_path(26, 62, 7)

# ------------------------------------------------- farmers
STRAW = "#f2e2ac"
STRAWD = "#c3a96a"
DARK = "#3a2a1e"
SKIN = "#c2905e"


def farmer_big(x, y, shirt, shade):
    """Bent-over harvester, 5 wide x 7 tall, feet at (x+2, y+6)."""
    # conical straw hat, 5 wide
    for i, col in enumerate([STRAWD, STRAW, STRAW, STRAW, STRAWD]):
        c.set(x + i, y + 1, col)
    c.set(x + 2, y, STRAW)
    c.set(x + 1, y, STRAWD)
    c.set(x + 3, y, STRAWD)
    # head and torso leaning forward
    c.set(x + 2, y + 2, SKIN)
    c.set(x + 3, y + 2, SKIN)
    c.set(x + 1, y + 3, shirt)
    c.set(x + 2, y + 3, shirt)
    c.set(x + 3, y + 3, shade)
    # arm reaching down with sickle
    c.set(x + 4, y + 3, SKIN)
    c.set(x + 4, y + 4, "#9aa0a6")
    c.set(x + 1, y + 4, shade)
    c.set(x + 2, y + 4, shirt)
    c.set(x + 3, y + 4, shade)
    # legs
    c.set(x + 1, y + 5, DARK)
    c.set(x + 3, y + 5, DARK)
    c.set(x + 1, y + 6, DARK)
    c.set(x + 3, y + 6, DARK)


def farmer_mid(x, y, shirt, shade):
    """Standing farmer, 3 wide x 5 tall, feet at (x+1, y+4)."""
    c.set(x, y + 1, STRAWD)
    c.set(x + 1, y, STRAW)
    c.set(x + 1, y + 1, STRAW)
    c.set(x + 2, y + 1, STRAWD)
    c.set(x + 1, y + 2, shirt)
    c.set(x + 2, y + 2, shade)
    c.set(x, y + 2, SKIN)
    c.set(x + 1, y + 3, shirt)
    c.set(x + 2, y + 3, shade)
    c.set(x + 1, y + 4, DARK)


def place(pts, px, fn, shirt, shade, foot):
    for (x, y) in pts:
        if x == px:
            fn(x - 2, y - foot, shirt, shade)
            return y
    return None


place(p_low, 20, farmer_big, "#2f63a2", "#1f4472", 6)
place(p_hi, 46, farmer_mid, "#b03a2c", "#7d2720", 4)

# cut-rice bundles stacked beside the paths
BUND = "#e4ca88"
BUNDD = "#ab8d4e"
for (bx, pts) in [(10, p_low), (31, p_low), (34, p_hi), (56, p_hi), (14, p_near), (38, p_near)]:
    for (x, y) in pts:
        if x == bx:
            c.set(x, y - 1, BUND)
            c.set(x + 1, y - 1, BUNDD)
            c.set(x, y - 2, BUNDD)
            break

print(c.stats_text())
view(c)
save("rice-terraces", c)
finish(c)
