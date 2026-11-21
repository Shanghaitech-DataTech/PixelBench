import random
from math import hypot, sin, cos, pi, sqrt

c = new_canvas(128, 128, None, "cottage")

# ------------------------------------------------------------------ palette
SPEC = [
    ("sky0", "#150c28"), ("sky1", "#1e1236"), ("sky2", "#291743"),
    ("sky3", "#342052"), ("sky4", "#402861"), ("sky5", "#4c316f"),
    ("glow0", "#6b5c8c"), ("glow1", "#9486b6"),
    ("moon0", "#fdf7dc"), ("moon1", "#eee0b2"), ("moon2", "#dccb95"), ("moon3", "#c8b47e"),
    ("star0", "#fdf8e2"), ("star1", "#cfc6e8"),
    ("st0", "#2c2738"), ("st1", "#3b3548"), ("st2", "#4e4659"), ("st3", "#635a6c"),
    ("st4", "#7b7283"), ("st5", "#948ca4"),
    ("wd0", "#1f1611"), ("wd1", "#2f2119"), ("wd2", "#412d20"), ("wd3", "#553a29"), ("wd4", "#6b4a33"),
    ("ms0", "#1d2a22"), ("ms1", "#293e30"), ("ms2", "#36513e"), ("ms3", "#46674e"), ("ms4", "#5a7f60"),
    ("lit0", "#ffe9b0"), ("lit1", "#ffcf78"), ("lit2", "#ffab45"), ("lit3", "#e8852c"), ("lit4", "#b5621f"),
    ("leaf0", "#2a1828"), ("leaf1", "#3a1b2a"), ("leaf2", "#4a2330"), ("leaf3", "#5d2a31"),
    ("leaf4", "#6b3a2c"), ("leaf5", "#54284a"), ("leaf6", "#6a3a56"),
    ("bark0", "#161020"), ("bark1", "#221a2b"), ("bark2", "#302540"),
    ("gnd0", "#120d1a"), ("gnd1", "#1b1426"), ("gnd2", "#251c33"), ("gnd3", "#332845"),
    ("mist0", "#6a5d92"), ("mist1", "#8b7fb3"), ("mist2", "#b0a6cf"),
    ("ps0", "#8a8478"), ("ps1", "#686258"), ("ps2", "#4a4640"),
    ("far0", "#1a1226"), ("far1", "#251b38"),
    ("rim0", "#b3a8ce"), ("rim1", "#847aa4"),
    ("wp0", "#d08f42"), ("wp1", "#8a5c2c"),
]
P = {}
for _n, _h in SPEC:
    P[_n] = c.color(_h, _n)

CH = {
    "sky0": ".", "sky1": ":", "sky2": "-", "sky3": "=", "sky4": "+", "sky5": "*",
    "glow0": "g", "glow1": "G",
    "moon0": "O", "moon1": "o", "moon2": "c", "moon3": "u",
    "star0": "S", "star1": "s",
    "st0": "k", "st1": "h", "st2": "x", "st3": "n", "st4": "N", "st5": "5",
    "wd0": "w", "wd1": "v", "wd2": "t", "wd3": "r", "wd4": "R",
    "ms0": "m", "ms1": "1", "ms2": "2", "ms3": "3", "ms4": "4",
    "lit0": "!", "lit1": "a", "lit2": "b", "lit3": "c", "lit4": "#",
    "leaf0": "A", "leaf1": "B", "leaf2": "C", "leaf3": "D",
    "leaf4": "E", "leaf5": "F", "leaf6": "H",
    "bark0": "p", "bark1": "q", "bark2": "e",
    "gnd0": "_", "gnd1": ",", "gnd2": ";", "gnd3": "'",
    "mist0": "~", "mist1": "^", "mist2": '"',
    "ps0": "P", "ps1": "Q", "ps2": "Z",
    "far0": "f", "far1": "r",
    "rim0": "y", "rim1": "Y",
    "wp0": "W", "wp1": "9",
}

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def bay(x, y):
    return (BAYER[y & 3][x & 3] + 0.5) / 16.0


def vgrad(x0, y0, w, h, names):
    n = len(names)
    for y in range(y0, y0 + h):
        t = (y - y0) / max(1, h - 1) * (n - 1)
        i = min(int(t), n - 2)
        f = t - i
        for x in range(x0, x0 + w):
            c.set(x, y, names[i + 1] if f > bay(x, y) else names[i])


def wisp(cx, cy, rx, ry, strength, seed, c0="mist0", c1="mist1", flat=1.0):
    random.seed(seed)
    for y in range(int(cy - ry - 1), int(cy + ry + 2)):
        for x in range(int(cx - rx - 1), int(cx + rx + 2)):
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            d = sqrt(dx * dx + dy * dy)
            if d < 1.05:
                t = max(0.0, 1.0 - d) ** flat
                if bay(x, y) < t * strength:
                    c.set(x, y, c1 if (d < 0.4 and random.random() < 0.5) else c0)


# ------------------------------------------------------------------ sky
vgrad(0, 0, 128, 100, ["sky0", "sky1", "sky2", "sky3", "sky4", "sky5"])

random.seed(11)
for i in range(250):
    x = random.randrange(128)
    y = random.randrange(94)
    if hypot(x - 92, y - 24) < 27:
        continue
    c.set(x, y, "star0" if random.random() < 0.22 else "star1")
for (sx, sy) in [(16, 12), (50, 18), (74, 6), (8, 42), (110, 56), (62, 50),
                 (30, 56), (96, 2), (44, 64), (4, 24), (66, 28), (116, 70)]:
    if hypot(sx - 92, sy - 24) < 26:
        continue
    c.set(sx, sy, "star0")
    c.set(sx - 1, sy, "star1")
    c.set(sx + 1, sy, "star1")
    c.set(sx, sy - 1, "star1")
    c.set(sx, sy + 1, "star1")
    if sx % 3 == 0:
        if bay(sx, sy) > 0.4:
            c.set(sx - 2, sy, "sky5")
            c.set(sx + 2, sy, "sky5")
            c.set(sx, sy - 2, "sky5")
            c.set(sx, sy + 2, "sky5")

# ------------------------------------------------------------------ moon
MX, MY, MR = 92, 24, 12
for y in range(MY - 24, MY + 25):
    for x in range(MX - 24, MX + 25):
        d = hypot(x - MX, y - MY)
        if MR < d <= MR + 11:
            t = (MR + 11 - d) / 11.0
            if bay(x, y) < t * t * 1.05:
                c.set(x, y, "glow1" if d < MR + 4 else "glow0")
for y in range(MY - MR, MY + MR + 1):
    for x in range(MX - MR, MX + MR + 1):
        d = hypot(x - MX, y - MY)
        if d <= MR:
            ux = (x - MX) / MR
            uy = (y - MY) / MR
            cc = "moon1"
            if d > MR - 1.1:
                cc = "moon2"
            if ux * 0.65 + uy * 0.76 > 0.62 and d < MR - 1:
                cc = "moon2"
            if ux * 0.65 + uy * 0.76 > 0.86:
                cc = "moon3"
            if -(ux * 0.7 + uy * 0.7) > 0.55:
                cc = "moon0"
            c.set(x, y, cc)
c.circle(87, 19, 3, "moon2")
c.circle(87, 19, 1, "moon3")
c.circle(97, 29, 2, "moon2")
c.circle(95, 16, 2, "moon3")
c.circle(86, 30, 1, "moon2")
c.circle(99, 21, 1, "moon3")

# ------------------------------------------------------------------ distant forest
random.seed(23)
x = -8
while x < 140:
    top = random.randrange(56, 84)
    hw = random.randrange(4, 9)
    c.poly([(x - hw, 100), (x, top), (x + hw, 100)], "far1")
    x += random.randrange(4, 9)
x = -6
while x < 140:
    top = random.randrange(72, 96)
    hw = random.randrange(4, 8)
    c.poly([(x - hw, 102), (x, top), (x + hw, 102)], "far0")
    x += random.randrange(5, 10)
c.ellipse(64, 108, 90, 14, "far1")

# background mist
wisp(30, 92, 42, 5, 0.55, 201)
wisp(96, 90, 38, 5, 0.5, 202)
wisp(12, 84, 26, 4, 0.35, 203)
wisp(120, 82, 24, 4, 0.3, 204)
wisp(64, 78, 24, 3, 0.25, 205)

# ------------------------------------------------------------------ ground
for y in range(96, 128):
    t = (y - 96) / 31.0
    for x in range(128):
        c.set(x, y, "gnd0" if (t * 1.35) > bay(x, y) else "gnd1")
random.seed(41)
for i in range(240):
    x = random.randrange(128)
    y = random.randrange(98, 128)
    r = random.random()
    if r < 0.32:
        c.set(x, y, "gnd2")
    elif r < 0.40:
        c.set(x, y, "gnd3")
for y in range(100, 118):
    for x in range(80, 112):
        d = hypot((x - 96) / 16.0, (y - 112) / 8.0)
        if d < 1 and bay(x, y) < (1 - d) * 0.4:
            c.set(x, y, "gnd3")
# warm light pools on the ground in front of the cottage


# ------------------------------------------------------------------ helpers
def stone_wall(x0, y0, w, h, seed=5, base_cols=("st2", "st2", "st3", "st1", "st2")):
    c.rect(x0, y0, w, h, "st2")
    random.seed(seed)
    row = 0
    yy = y0
    while yy < y0 + h:
        bh = 6
        off = 0 if row % 2 == 0 else 5
        xx = x0 - off
        while xx < x0 + w:
            bw = 10 + random.choice([0, 0, 2])
            bx0 = max(x0, xx)
            bx1 = min(x0 + w, xx + bw)
            if bx1 - bx0 > 1:
                base = random.choice(base_cols)
                c.rect(bx0, yy, bx1 - bx0, min(bh, y0 + h - yy), base)
                c.line(bx0, yy, bx1 - 1, yy, "st1")
                if base != "st1":
                    c.line(bx0 + 1, yy + 1, bx1 - 2, yy + 1, "st3" if base != "st3" else "st4")
            xx += bw
        yy += bh
        row += 1
    c.line(x0, y0, x0, y0 + h - 1, "st1")
    c.line(x0 + w - 1, y0, x0 + w - 1, y0 + h - 1, "st0")


def puff(cx, cy, r, seed, cols, rmin=2, rmax=4, weight=1.4, ry=0.85):
    random.seed(seed)
    n = max(1, int(r * r * 0.55))
    for i in range(n):
        a = random.uniform(0, 2 * pi)
        rr = r * sqrt(random.random())
        x = int(cx + cos(a) * rr)
        y = int(cy + sin(a) * rr * ry)
        rad = random.randint(rmin, rmax)
        idx = int((random.random() ** weight) * len(cols))
        c.circle(x, y, rad, cols[min(idx, len(cols) - 1)])


def canopy(cx, cy, r, seed):
    # moonlit rim, offset up-right
    puff(cx + 2, cy - 2, r, seed, ["rim1", "rim0", "rim0"], 2, 4, 0.9)
    # dark mass
    puff(cx, cy, r, seed, ["leaf0", "leaf0", "leaf1", "leaf1", "leaf2"], 2, 4, 0.8)
    # mid tone puffs
    puff(cx, cy - r * 0.3, r * 0.8, seed + 1, ["leaf1", "leaf2", "leaf3", "leaf2"], 2, 3, 1.1)
    # warm accents
    random.seed(seed + 2)
    for i in range(int(r * 1.3)):
        a = random.uniform(0, 2 * pi)
        rr = r * sqrt(random.random()) * 0.92
        x = int(cx + cos(a) * rr)
        y = int(cy + sin(a) * rr * 0.8)
        c.circle(x, y, random.choice([1, 2]), random.choice(["leaf3", "leaf4", "leaf5", "leaf6", "leaf2"]))
    # dark underside
    puff(cx, cy + r * 0.55, r * 0.7, seed + 3, ["leaf0", "leaf0", "leaf1"], 2, 3, 0.5)


def limb(x0, y0, x1, y1, w, base="bark1", shade="bark0", light="rim1"):
    for i in range(w):
        c.line(x0 + i, y0, x1 + i, y1, base)
    if light:
        c.line(x0 + w - 1, y0, x1 + w - 1, y1, light)
        c.line(x0 + w - 2, y0, x1 + w - 2, y1, "bark2")
    if shade:
        c.line(x0, y0, x1, y1, shade)


def window(x, y, w, h):
    c.rect(x - 2, y - 2, w + 4, h + 4, "wd0")
    c.rect(x - 1, y - 1, w + 2, h + 2, "wd1")
    c.rect(x, y, w, h, "lit2")
    c.rect(x + 1, y + 1, w - 2, h - 2, "lit1")
    c.rect(x + 2, y + 2, w - 4, h - 4, "lit0")
    c.line(x + w // 2, y, x + w // 2, y + h - 1, "wd1")
    c.line(x, y + h // 2, x + w - 1, y + h // 2, "wd1")
    # sill
    c.line(x - 2, y + h + 2, x + w + 1, y + h + 2, "st4")
    c.line(x - 1, y + h + 3, x + w, y + h + 3, "st1")


def glow(cx, cy, rad, strength):
    for yy in range(int(cy - rad), int(cy + rad) + 1):
        for xx in range(int(cx - rad), int(cx + rad) + 1):
            d = hypot(xx - cx, yy - cy) / rad
            if d < 1.0 and bay(xx, yy) < (1.0 - d) ** 2 * strength:
                nm = c.color_name(c.get(xx, yy))
                if nm in ("lit0", "lit1", "lit2", "lit3", "lit4",
                          "wd0", "wd1", "wd2", "wd3", "wd4"):
                    continue
                c.set(xx, yy, "lit3" if d < 0.45 else "lit4")


# ------------------------------------------------------------------ cottage
stone_wall(15, 78, 45, 33, seed=5)
c.line(15, 78, 59, 78, "st4")

# --- roof triangle
PEAK = (37, 30)
LEAV = (6, 78)
REAV = (68, 78)

for y in range(PEAK[1], LEAV[1] + 1):
    t = (y - PEAK[1]) / float(LEAV[1] - PEAK[1])
    lx = int(PEAK[0] - (PEAK[0] - LEAV[0]) * t)
    rx = int(PEAK[0] + (REAV[0] - PEAK[0]) * t)
    c.line(lx, y, lx + int((rx - lx) * 0.32), y, "ms1")
    c.line(lx, y, lx + 1, y, "ms0")
    c.line(rx - 2, y, rx, y, "ms3")
    if rx - lx > 8 and y % 3 == 0:
        c.set(rx - 1, y, "ms4")

# shingle courses
for y in range(PEAK[1] + 5, LEAV[1], 7):
    t = (y - PEAK[1]) / float(LEAV[1] - PEAK[1])
    lx = int(PEAK[0] - (PEAK[0] - LEAV[0]) * t) + 2
    rx = int(PEAK[0] + (REAV[0] - PEAK[0]) * t) - 2
    x = lx
    while x < rx:
        c.line(x, y, min(x + 5, rx), y, "ms1")
        if x + 6 < rx:
            c.set(x + 6, y, "ms0")
        x += 9

# moss patches
random.seed(57)
for i in range(110):
    t = random.random() ** 1.2
    y = int(PEAK[1] + 4 + t * (LEAV[1] - PEAK[1] - 4))
    tt = (y - PEAK[1]) / float(LEAV[1] - PEAK[1])
    lx = int(PEAK[0] - (PEAK[0] - LEAV[0]) * tt) + 1
    rx = int(PEAK[0] + (REAV[0] - PEAK[0]) * tt) - 1
    if rx - lx < 3:
        continue
    x = random.randrange(lx, rx)
    if x < PEAK[0]:
        cc = random.choice(["ms1", "ms0", "ms2", "ms3", "ms1", "ms2"])
    else:
        cc = random.choice(["ms3", "ms4", "ms3", "ms2", "ms4", "ms3"])
    c.circle(x, y, random.choice([1, 1, 2]), cc)

# rake highlight on the moonlit slope
for y in range(PEAK[1], LEAV[1] + 1):
    t = (y - PEAK[1]) / float(LEAV[1] - PEAK[1])
    rx = int(PEAK[0] + (REAV[0] - PEAK[0]) * t)
    c.set(rx, y, "rim0" if y % 4 else "rim1")
    if y % 4 == 0:
        c.set(rx - 1, y, "rim1")
c.set(PEAK[0], PEAK[1], "rim0")
c.set(PEAK[0] - 1, PEAK[1] + 1, "rim1")
c.set(PEAK[0] + 1, PEAK[1] + 1, "rim0")

# eave board + moss drips
c.line(LEAV[0], LEAV[1], REAV[0], LEAV[1], "ms0")
c.line(LEAV[0] + 1, LEAV[1] + 1, REAV[0] - 1, LEAV[1] + 1, "ms0")
random.seed(61)
for i in range(44):
    x = random.randrange(LEAV[0] + 2, REAV[0] - 1)
    d = random.choice([1, 1, 2, 2, 3])
    for k in range(d):
        c.set(x, LEAV[1] + 2 + k, random.choice(["ms1", "ms0", "ms2"]))
c.line(15, 79, 59, 79, "st1")

# --- wooden gable
GPEAK = (37, 52)
c.poly([(16, 78), GPEAK, (58, 78)], "wd2")
for y in range(GPEAK[1], 78):
    t = (y - GPEAK[1]) / float(78 - GPEAK[1])
    lx = int(37 - 21 * t)
    rx = int(37 + 21 * t)
    if (y - GPEAK[1]) % 5 == 0 and rx - lx > 3:
        c.line(lx + 1, y, rx - 1, y, "wd0")
    c.set(rx, y, "wd4" if y % 2 else "wd3")
    c.set(lx, y, "wd0")
    c.set(lx - 1, y, "wd1")
    c.set(rx + 1, y, "wd1")

# --- chimney
stone_wall(48, 24, 9, 24, seed=9)
c.line(48, 24, 56, 24, "st4")
c.line(47, 23, 57, 23, "st3")
c.line(47, 22, 57, 22, "rim1")
c.line(47, 23, 47, 26, "st1")
c.line(57, 23, 57, 26, "st0")
c.line(48, 25, 56, 25, "st1")

random.seed(71)
for i in range(800):
    y = 21 - int(random.random() ** 1.5 * 24)
    x = 52 + int(sin(y * 0.22) * 4) + int(random.gauss(0, 2.2))
    if 0 <= y < 24 and random.random() < 0.38:
        c.set(x, y, random.choice(["mist1", "mist0", "mist1", "glow0"]))

# --- windows & door
window(17, 85, 9, 11)
window(47, 85, 9, 11)
glow(21, 90, 7.5, 0.5)
glow(51, 90, 7.5, 0.5)
window(33, 65, 8, 9)
glow(37, 69, 6.0, 0.35)

# door: dark frame with an arched head
c.rect(28, 91, 13, 19, "wd0")
c.poly([(28, 91), (34, 85), (40, 91)], "wd0")
# warm interior, arched
c.rect(29, 92, 11, 18, "lit2")
c.poly([(29, 92), (34, 87), (39, 92)], "lit2")
c.rect(30, 94, 9, 16, "lit1")
c.poly([(30, 94), (34, 90), (38, 94)], "lit1")
c.rect(31, 96, 7, 14, "lit0")
c.poly([(31, 96), (34, 92), (37, 96)], "lit0")
# ajar wooden panel on the left
c.rect(29, 92, 6, 18, "wd2")
c.line(29, 92, 34, 92, "wd0")
c.line(29, 93, 34, 93, "wd1")
c.line(29, 92, 29, 109, "wd0")
c.line(31, 94, 31, 109, "wd0")
c.line(33, 94, 33, 109, "wd1")
c.line(34, 94, 34, 109, "wd3")
c.set(34, 103, "lit2")
# bright core of the opening beside the panel
c.rect(36, 96, 2, 13, "lit0")
c.line(38, 94, 38, 109, "lit1")
c.line(35, 94, 35, 110, "lit2")
glow(36, 99, 7.0, 0.5)

# stone threshold step under the door
c.rect(27, 110, 15, 3, "st3")
c.line(27, 110, 41, 110, "st4")
c.line(27, 112, 41, 112, "st1")
c.line(27, 111, 41, 111, "lit4")
c.set(33, 111, "lit3")
c.set(34, 111, "lit3")
c.set(35, 111, "lit3")

# lantern hanging under the eave, above the door
c.line(35, 79, 35, 81, "wd1")
c.line(32, 81, 38, 81, "wd2")
c.rect(33, 82, 5, 4, "wd0")
c.rect(34, 83, 3, 2, "lit1")
c.set(35, 83, "lit0")
c.set(34, 82, "lit2")
c.set(36, 82, "lit2")
glow(35, 83, 5.0, 0.55)

# ------------------------------------------------------------------ well
WX, WY = 94, 100
for y in range(WY, WY + 15):
    rx = 10 + int((y - WY) * 0.13)
    c.line(WX - rx, y, WX + rx, y, "st2")
c.ellipse(WX, WY + 15, 12, 3, "st1")
for y in range(WY + 3, WY + 14, 4):
    rx = 10 + int((y - WY) * 0.13)
    c.line(WX - rx, y, WX + rx, y, "st1")
random.seed(83)
for i in range(60):
    yy = random.randrange(WY + 2, WY + 14)
    xx = random.randrange(WX - 11, WX + 12)
    c.set(xx, yy, random.choice(["st3", "st3", "st1", "st2"]))
for y in range(WY, WY + 15):
    rx = 10 + int((y - WY) * 0.13)
    c.set(WX + rx, y, "st4" if y % 2 else "st3")
    c.set(WX + rx - 1, y, "st3")
    c.set(WX - rx, y, "st1")
# coping + dark opening
c.ellipse(WX, WY - 1, 12, 5, "st3")
c.ellipse(WX, WY - 1, 10, 4, "st2")
c.ellipse(WX, WY - 1, 7, 3, "gnd0")
c.ellipse(WX, WY - 1, 5, 2, "st0")
c.set(WX + 2, WY - 1, "glow1")
c.set(WX + 3, WY - 1, "glow1")
c.set(WX + 1, WY, "glow0")
for x in range(WX + 2, WX + 13):
    d = (x - WX) / 12.0
    y = WY - 1 - int(round(5 * sqrt(max(0.0, 1 - d * d))))
    c.set(x, y, "rim0")
for x in range(WX - 12, WX + 3):
    d = (x - WX) / 12.0
    y = WY - 1 - int(round(5 * sqrt(max(0.0, 1 - d * d))))
    c.set(x, y, "st4" if d > -0.2 else "st3")

# posts, crossbar, crank, rope, bucket
for px in (WX - 9, WX + 9):
    c.line(px, WY - 1, px, WY - 21, "wd1")
    c.line(px + 1, WY - 1, px + 1, WY - 21, "wd3")
    c.line(px + 2, WY - 1, px + 2, WY - 21, "wd2")
    c.set(px + 1, WY - 22, "wd4")
c.line(WX - 9, WY - 21, WX + 11, WY - 21, "wd3")
c.line(WX - 9, WY - 20, WX + 11, WY - 20, "wd2")
c.line(WX - 9, WY - 22, WX + 11, WY - 22, "wd4")
c.line(WX - 9, WY - 23, WX + 11, WY - 23, "rim1")
c.line(WX + 11, WY - 21, WX + 14, WY - 17, "wd3")
c.line(WX + 12, WY - 21, WX + 15, WY - 17, "wd1")
c.set(WX + 15, WY - 17, "wd4")
c.set(WX + 14, WY - 16, "wd4")
c.line(WX + 1, WY - 19, WX + 1, WY - 9, "ps0")
c.line(WX + 2, WY - 19, WX + 2, WY - 9, "ps1")
c.poly([(WX - 3, WY - 9), (WX + 5, WY - 9), (WX + 4, WY - 3), (WX - 2, WY - 3)], "wd3")
c.line(WX - 3, WY - 9, WX + 5, WY - 9, "wd4")
c.line(WX - 2, WY - 4, WX + 4, WY - 4, "wd1")
c.line(WX - 3, WY - 8, WX - 3, WY - 4, "wd2")
c.line(WX + 5, WY - 8, WX + 5, WY - 4, "wd2")

# ------------------------------------------------------------------ trees
# left ancient gnarled trunk
limb(0, 128, 2, 112, 14)
limb(2, 114, 8, 98, 12, light="rim0")
limb(8, 100, 1, 84, 11, light="rim0")
limb(1, 86, 9, 70, 9, light="rim0")
limb(9, 72, 3, 56, 7, light="rim0")
limb(3, 58, 10, 42, 6, light="rim0")
limb(10, 44, 4, 24, 4)
# root flares
limb(2, 122, 16, 126, 4, light=None)
limb(0, 114, 10, 118, 3, light=None)
# branches
limb(8, 78, 26, 68, 3)
limb(24, 70, 36, 60, 2)
limb(9, 62, 28, 54, 3)
limb(26, 56, 38, 48, 2)
limb(2, 99, 11, 93, 3, light=None)
limb(10, 46, 22, 34, 2)
# right ancient gnarled trunk
limb(127, 128, 121, 112, 13)
limb(121, 114, 126, 96, 11, light="rim0")
limb(126, 98, 116, 82, 10, light="rim0")
limb(116, 84, 122, 66, 8, light="rim0")
limb(122, 68, 112, 52, 6, light="rim0")
limb(112, 54, 118, 36, 5, light="rim0")
limb(118, 38, 112, 18, 4)
# root flares
limb(118, 124, 127, 128, 4, light=None)
# branches
limb(118, 74, 104, 66, 3)
limb(112, 58, 100, 48, 3)
limb(116, 42, 128, 30, 3, light=None)
limb(120, 88, 106, 82, 3, light=None)

GROUPS = [(9, 22, 17), (28, 8, 12), (16, 46, 6), (2, 50, 9),
          (119, 12, 14), (126, 40, 10), (107, 42, 7)]
for (cx, cy, r) in GROUPS:
    canopy(cx, cy, r, int(cx * 7 + cy * 3) + 1)

# foreground undergrowth
random.seed(191)
for i in range(46):
    x = random.randrange(0, 18)
    y = random.randrange(108, 128)
    c.circle(x, y, random.choice([2, 3, 3]), random.choice(["leaf0", "leaf1", "bark0", "gnd0"]))
for i in range(40):
    x = random.randrange(112, 128)
    y = random.randrange(112, 128)
    c.circle(x, y, random.choice([2, 3, 3]), random.choice(["leaf0", "leaf1", "bark0", "gnd0"]))

# ------------------------------------------------------------------ path (in front)
slabs = [(34, 114, 5, 2), (32, 118, 6, 3), (38, 121, 6, 3), (45, 123, 7, 3),
         (54, 126, 8, 3), (27, 123, 6, 3), (20, 127, 7, 3), (61, 122, 6, 3),
         (69, 119, 6, 2), (78, 116, 6, 2), (68, 126, 7, 3), (60, 128, 8, 3)]
for (sx, sy, rx, ry) in slabs:
    c.ellipse(sx, sy + 1, rx, ry, "ps2")
    c.ellipse(sx, sy, rx, ry, "ps1")
    c.ellipse(sx - 1, sy - 1, rx - 1, ry - 1, "ps0")
    if rx > 4:
        c.set(sx + 1, sy, "ps1")

# warm light pooling over the path and the ground by the door
wisp(35, 116, 10, 4, 0.5, 301, "wp1", "wp0")
wisp(45, 123, 8, 3.5, 0.3, 302, "wp1", "wp0")

# glow-capped mushrooms beside the path
for (mx, my, mr) in [(47, 117, 2), (51, 120, 1), (44, 120, 1)]:
    c.circle(mx, my, mr, "lit2")
    c.set(mx, my - 1, "lit0")
    c.set(mx + 1, my, "lit3")
    c.line(mx, my + 1, mx, my + 2, "ps0")
    c.line(mx + 1, my + 1, mx + 1, my + 2, "ps1")

# ------------------------------------------------------------------ fireflies & low mist
random.seed(151)
ff = 0
while ff < 24:
    x = random.randrange(4, 124)
    y = random.randrange(96, 122)
    n = c.color_name(c.get(x, y))
    if n in ("lit0", "lit1", "lit2"):
        continue
    c.set(x, y, "lit0" if random.random() < 0.45 else "lit3")
    ff += 1

wisp(10, 118, 22, 3.5, 0.30, 213)
wisp(120, 121, 20, 3.5, 0.28, 214)
wisp(64, 126, 38, 3, 0.22, 211)


# ------------------------------------------------------------------ report
def dump(x0, y0, x1, y1, step=1, title=""):
    inv = {}
    for n, i in P.items():
        inv[i] = CH.get(n, "?")
    print("--- %s ---" % title)
    for y in range(y0, y1 + 1, step):
        row = ""
        for x in range(x0, x1 + 1, step):
            row += inv.get(c.get(x, y), " ")
        print("%3d %s" % (y, row))


print("COLOURS:", len(c.palette()))
print(c.stats_text())
dump(0, 0, 127, 127, 2, "whole x2")
dump(12, 74, 64, 114, 1, "facade")
dump(80, 72, 112, 116, 1, "well")
save("magic_forest_cottage", c)
finish(c)
