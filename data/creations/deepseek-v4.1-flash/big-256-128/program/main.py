from pixelbench_api import *
import math

W, H = 256, 128
out = input_canvas.copy(name="output")
out.clear()

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def bay(x, y):
    return (BAYER[y & 3][x & 3] + 0.5) / 16.0


def h2(x, y, s=0):
    n = (int(x) * 374761393 + int(y) * 668265263 + int(s) * 1442695041) & 0xFFFFFFFF
    n = (n ^ (n >> 13)) * 1274126177 & 0xFFFFFFFF
    n = (n ^ (n >> 16)) & 0xFFFFFFFF
    return n / 4294967296.0


# ---------------------------------------------------------------- sky
SKY_STOPS = [(0, "#0a020e"), (16, "#120620"), (32, "#1b0828"), (48, "#260b2e"),
             (62, "#330e33"), (76, "#421036"), (90, "#56153a"), (102, "#742038"),
             (114, "#983038"), (128, "#b04a3e")]


def sky_px(x, y):
    for i in range(len(SKY_STOPS) - 1):
        y0, c0 = SKY_STOPS[i]
        y1, c1 = SKY_STOPS[i + 1]
        if y0 <= y < y1:
            t = (y - y0) / float(y1 - y0)
            return c1 if t > bay(x, y) else c0
    return SKY_STOPS[-1][1]


for y in range(H):
    for x in range(W):
        out.set(x, y, sky_px(x, y))

MCX, MCY, MR = 128, 20, 20
GLOW = ["#8e2038", "#6f1930", "#551329", "#3f0e23", "#2d0a1c"]


def glow_col(x, y):
    d = math.hypot(x - MCX, y - MCY)
    if d < MR:
        return None
    u = (d - MR) / 32.0
    if u >= 1.0:
        return None
    v = (1.0 - u) ** 1.4 * len(GLOW)
    i = int(v)
    if v - i > 0.5 and ((x + y) & 1) == 0:
        i += 1
    return GLOW[min(i, len(GLOW) - 1)]


for y in range(H):
    for x in range(W):
        g = glow_col(x, y)
        if g:
            out.set(x, y, g)

# ---------------------------------------------------------------- stars
for i in range(300):
    x = int(h2(i, 11, 3) * W)
    y = int(h2(i, 23, 5) * 98)
    d = math.hypot(x - MCX, y - MCY)
    if d < MR + 20:
        continue
    if y > 98 and h2(i, 31) < 0.7:
        continue
    r = h2(i, 41, 7)
    if r < 0.55:
        col = "#6d4a63"
    elif r < 0.82:
        col = "#a97d96"
    elif r < 0.95:
        col = "#e6c8d2"
    else:
        col = "#fff0f0"
    out.set(x, y, col)

# ---------------------------------------------------------------- blood moon
MOON_RAMP = ["#ff9558", "#ef6a3f", "#d8402f", "#bb2728", "#9a1a22", "#7c1419"]
CRATERS = [(-9, -6, 3), (6, -9, 2), (10, 4, 4), (-6, 8, 3), (-13, 4, 2),
           (2, 1, 5), (14, -3, 2), (-2, -13, 2)]

for y in range(MCY - MR - 2, MCY + MR + 3):
    for x in range(MCX - MR - 2, MCX + MR + 3):
        dx, dy = x - MCX, y - MCY
        d = math.hypot(dx, dy)
        if d > MR + 0.55:
            continue
        sh = (dx * 0.55 + dy * 0.84) / float(MR)
        val = (sh + 1.0) * 0.5 * (len(MOON_RAMP) - 1)
        i = int(val)
        if val - i > 0.5 and ((x + y) & 1) == 0:
            i += 1
        i = max(0, min(len(MOON_RAMP) - 1, i))
        col = MOON_RAMP[i]
        for (ax, ay, ar) in CRATERS:
            dd = math.hypot(dx - ax, dy - ay)
            if dd < ar:
                col = "#6b0f16"
            elif dd < ar + 1.0 and (dx - ax) * 0.6 + (dy - ay) * 0.8 < 0:
                col = MOON_RAMP[max(0, i - 2)]
        if d > MR - 1.2:
            if sh < -0.2:
                col = "#ffb277"
            elif sh > 0.35:
                col = "#47070d"
        out.set(x, y, col)

# ---------------------------------------------------------------- clouds
def cloud(x0, x1, ybase, thick, body, hi, seed):
    n = max(1, x1 - x0)
    for x in range(x0, x1):
        t = (x - x0) / float(n)
        bell = math.sin(math.pi * max(0.0, min(1.0, t))) ** 0.7
        hh = thick * bell
        if hh < 1.2:
            continue
        top = ybase - hh * 0.5 + 2.0 * h2(x, seed, 2) - 1.0
        for y in range(int(math.floor(top)), int(math.floor(top + hh)) + 1):
            if (top + hh) - y < 1.0 and h2(x, y, seed) < 0.5:
                continue
            out.set(x, y, hi if y <= top + 1.0 else body)


cloud(-8, 74, 10, 6, "#1c0a24", "#341030", 3)
cloud(112, 208, 6, 5, "#1c0a24", "#341030", 9)
cloud(-12, 104, 46, 9, "#190820", "#300e2a", 17)
cloud(96, 264, 40, 9, "#1a0922", "#34102c", 21)
cloud(150, 256, 56, 7, "#170720", "#2c0c28", 33)

# ---------------------------------------------------------------- distant ridge
for x in range(W):
    top = int(104 + 7 * math.sin(x * 0.052 + 0.4) + 4 * math.sin(x * 0.131 + 1.9)
              + 2 * math.sin(x * 0.31 + 3.1))
    for y in range(max(0, top), H):
        out.set(x, y, "#1a0714")
    out.set(x, max(0, top), "#2c0d1e")

# ---------------------------------------------------------------- castle
FAR = "#1d0a17"
FAR_HI = "#33112a"
STONE = "#150712"
STONE_L = "#4a1a2e"
STONE_LL = "#6b2a3c"
CB = 126
WIN1 = "#ff9a3c"
WIN2 = "#ffd88a"
WIN3 = "#a8301a"
DARK = "#0a0208"


def tower(cx, half, top, sh, body=STONE, edge=STONE_L, cren=True):
    x0 = cx - half
    w = 2 * half + 1
    out.rect(x0, top, w, CB - top, body)
    if cren:
        for i in range(0, w, 4):
            out.rect(x0 + i, top - 3, 2, 3, body)
    out.poly([(x0 - 1, top), (cx, top - sh), (x0 + w, top)], body)
    # moon-facing rim light
    if cx < MCX:
        out.line(x0 + w - 1, top, x0 + w - 1, CB - 1, edge)
        out.line(x0 + w, top, cx + 1, top - sh, edge)
        out.line(x0 + 1, top - sh + 1, cx - 1, top - 2, "#2a0c1c")
    else:
        out.line(x0, top, x0, CB - 1, edge)
        out.line(x0 - 1, top, cx - 1, top - sh, edge)
        out.line(x0 + w - 1, top - sh + 1, cx + 1, top - 2, "#2a0c1c")
    out.set(cx, top - sh - 1, edge)
    out.set(cx, top - sh - 2, body)


def gwin(cx, ytop, w, h, col, top_only=False):
    for i in range(h):
        ww = 1 if i == 0 else (max(1, w - 2) if i == 1 else w)
        if top_only and i > 0:
            ww = w
        out.rect(cx - ww // 2, ytop + i, ww, 1, col)


def windows(cx, ys, w=3, seed=1):
    for yy in ys:
        r = h2(cx, yy, seed)
        if r < 0.68:
            gwin(cx, yy, w, w + 3, WIN1)
            out.set(cx, yy + 1, WIN2)
        elif r < 0.9:
            gwin(cx, yy, w, w + 2, WIN3)
        else:
            gwin(cx, yy, w, w + 2, "#3a1220")


def archwin(cx, ytop, w, h, col, edge, bars=True):
    x0 = cx - w // 2
    out.rect(x0, ytop + w // 2, w, h - w // 2, col)
    out.poly([(x0 - 1, ytop + w // 2 + 1), (cx, ytop - 1),
              (x0 + w, ytop + w // 2 + 1)], col)
    if edge:
        out.line(x0 - 1, ytop + w // 2, x0 - 1, ytop + h, edge)
    if bars:
        out.rect(cx - 1, ytop, 1, h - 2, DARK)
        out.rect(x0, ytop + h // 2, w, 1, DARK)


# back layer
for (cx, half, top, sh) in [(100, 5, 84, 9), (156, 5, 84, 9),
                            (74, 4, 90, 8), (182, 4, 90, 8),
                            (46, 4, 94, 7), (210, 4, 94, 7)]:
    tower(cx, half, top, sh, body=FAR, edge=FAR_HI)

# wall band with battlements
out.rect(0, 100, W, CB - 100, "#100510")
for x in range(0, W, 6):
    out.rect(x, 96, 3, 6, "#100510")
for x in range(2, W, 13):
    out.rect(x, 100, 1, CB - 100, "#240b1c")
for x in range(0, W, 6):
    out.rect(x, 96, 3, 1, "#3a1526")

# main towers
MAIN = [(128, 14, 62, 15), (100, 9, 71, 19), (156, 9, 71, 19),
        (72, 8, 79, 15), (184, 8, 79, 15), (46, 7, 87, 12),
        (210, 7, 87, 12), (21, 6, 95, 10), (235, 6, 95, 10)]
for (cx, half, top, sh) in MAIN:
    tower(cx, half, top, sh)

# castle body detail: masonry lines
for x in range(4, W, 5):
    if h2(x, 7) < 0.5:
        out.rect(x, 104, 1, 10, "#1e0818")

# windows
windows(100, [81, 93, 108, 118], 3, 5)
windows(156, [81, 93, 108, 118], 3, 9)
windows(72, [89, 101, 113], 3, 13)
windows(184, [89, 101, 113], 3, 17)
windows(46, [97, 109, 120], 3, 21)
windows(210, [97, 109, 120], 3, 25)
windows(21, [105, 117], 2, 29)
windows(235, [105, 117], 2, 33)
windows(128, [104, 116], 3, 37)
windows(100, [88], 3, 41)
windows(156, [88], 3, 45)

# keep rose / arched window
archwin(128, 74, 11, 16, "#c83c18", "#ffb066")
gwin(128, 76, 7, 3, "#ffd88a")
out.set(128, 74, "#ffe8b8")
# small flanking windows on keep
gwin(120, 96, 2, 5, WIN1)
gwin(136, 96, 2, 5, WIN3)
gwin(120, 110, 2, 4, WIN3)
gwin(136, 110, 2, 4, WIN1)

# ---------------------------------------------------------------- gate
GX, GW = 128, 18
for i in range(24):
    y = 100 + i
    if i < 6:
        ww = GW - 2 * (6 - i)
        ww = max(1, ww)
    elif i < 8:
        ww = GW - 3
    else:
        ww = GW
    out.rect(GX - ww // 2, y, ww, 1, DARK)
for y in range(104, CB):
    for x in range(GX - GW // 2 + 1, GX + GW // 2):
        u = (y - 104) / 20.0
        if h2(x, y, 77) < 0.12 + 0.55 * u:
            out.set(x, y, "#c1360f" if h2(x, y, 91) < 0.45 else "#7d1c0c")
for y in range(105, CB, 4):
    out.rect(GX - GW // 2 + 1, y, GW - 2, 1, "#2a0c14")
out.rect(GX - 1, 104, 1, 22, "#2a0c14")
# gate arch outline
out.line(GX - GW // 2, 108, GX - GW // 2, CB - 1, "#3f1626")
out.line(GX + GW // 2, 108, GX + GW // 2, CB - 1, "#3f1626")

# torches
for tx in (GX - 13, GX + 13):
    out.rect(tx, 106, 1, 6, "#231019")
    out.set(tx, 105, "#ff9a3c")
    out.set(tx, 104, "#ffcf72")
    out.set(tx + 1, 105, "#c84410")

# ---------------------------------------------------------------- foreground
for x in range(W):
    d = abs(x - 128) / 128.0
    top = int(122 + 6 * (1 - d) ** 2)
    for y in range(top, H):
        out.set(x, y, DARK)

# dead trees / spikes at corners
def spike(x, base, hgt, half, col):
    for i in range(hgt):
        ww = max(1, int(half * (1 - i / float(hgt)) * 2) + 1)
        out.rect(x - ww // 2, base - i, ww, 1, col)


spike(6, 127, 22, 3, DARK)
spike(18, 127, 14, 2, DARK)
spike(249, 127, 24, 3, DARK)
spike(238, 127, 13, 2, DARK)
spike(30, 128, 9, 2, DARK)
spike(226, 128, 8, 2, DARK)

# road in front of the gate
for i in range(8):
    y = 123 + i
    if y >= H:
        break
    ww = 16 + 3 * i
    out.rect(128 - ww // 2, y, ww, 1, "#2b0f1b" if i % 2 == 0 else "#1c0812")

print(out.stats_text())

pal_ = out.palette()


def ch(x, y):
    r, g, b, a = pal_[out.get(x, y)]['rgba']
    lum = (r * 0.3 + g * 0.6 + b * 0.1)
    return ' .:-=+*#%@'[min(9, max(0, int(lum / 16)))]


def dump(x0, y0, x1, y1, step=1):
    print('    ' + ''.join(str(x % 10) for x in range(x0, x1, step)))
    for y in range(y0, y1, step):
        print(f'{y:3d} ' + ''.join(ch(x, y) for x in range(x0, x1, step)))


dump(0, 0, 256, 128, 2)
save("stage1", out)
finish(out)
