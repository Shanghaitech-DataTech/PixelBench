import math, random
from pixelbench_api import new_canvas, finish

W = H = 128
rng = random.Random(11)
c = new_canvas(W, H, name="magic_forest_cottage")

sky = [c.color(h, f"sky{i}") for i, h in enumerate(
    ["#0b0520", "#110a2e", "#180f3d", "#20154e", "#291c61", "#332375", "#3e2c88", "#4a3698"])]
moon = c.color("#f8eecb", "moon")
moonsh = c.color("#e6d8a8", "moonsh")
halo = c.color("#8270b4", "halo")
halo2 = c.color("#a590d2", "halo2")
tree_far = c.color("#0a0616", "tree_far")
tree_mid = c.color("#101422", "tree_mid")
mist = [c.color("#9678be", "mist0"), c.color("#a084c8", "mist1"), c.color("#aa90d2", "mist2"),
        c.color("#b69edc", "mist3")]
ground_c = c.color("#171023", "ground")
ground_dark = c.color("#120c1e", "ground_dark")
ground_lit = c.color("#1e1630", "ground_lit")
trunk_d = c.color("#160f22", "trunk_d")
trunk = c.color("#241a30", "trunk")
leaf = [c.color("#2e0f1e", "leaf1"), c.color("#3d1528", "leaf2"), c.color("#4d1c34", "leaf3"),
        c.color("#5d2340", "leaf4"), c.color("#6c2a48", "leaf5"), c.color("#451c3a", "leaf6"),
        c.color("#552244", "leaf7")]
stone = [c.color("#33333e", "stone0"), c.color("#3a3a46", "stone1"), c.color("#45454f", "stone2"),
         c.color("#50505c", "stone3"), c.color("#5a5a66", "stone4")]
wood = [c.color("#3a2417", "wood0"), c.color("#4a2f1f", "wood1"), c.color("#5c3b26", "wood2"),
        c.color("#6e482e", "wood3")]
roofc = [c.color("#241c12", "roof0"), c.color("#2d2418", "roof1"), c.color("#3a2e1e", "roof2")]
moss = [c.color("#252e1e", "moss0"), c.color("#2e3a24", "moss1"), c.color("#3c4c2e", "moss2"),
        c.color("#4a5c38", "moss3")]
win = [c.color("#ffb84d", "win0"), c.color("#ff9a2e", "win1"), c.color("#ff7a1a", "win2"),
       c.color("#7a4510", "win3")]
glowc = [c.color("#f49a46", "glow0"), c.color("#f7ad5e", "glow1"), c.color("#d67d33", "glow2")]
well_d = c.color("#080414", "well_d")
ropec = c.color("#1e1410", "rope")
pathc = [c.color("#3c3c48", "path0"), c.color("#4a4a56", "path1"), c.color("#5a5a66", "path2"),
        c.color("#66666e", "path3")]
firef = [c.color("#ffe89a", "ff0"), c.color("#ffd45a", "ff1")]


def branch(pts, start_r, color):
    n = len(pts)
    L = []
    for i in range(n - 1):
        L.append(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]))
    T = sum(L)
    ti = 0.0
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        steps = int(L[i]) + 1
        for s in range(steps + 1):
            t = (ti + s / steps) / T
            r = max(1, int(round(start_r * (1.0 - 0.5 * t))))
            c.circle(round(x0 + (x1 - x0) * s / steps), round(y0 + (y1 - y0) * s / steps), r, color)
        ti += L[i]


def canopy(cx, cy, rad, colors, density=16):
    for i in range(density):
        a = rng.uniform(0.0, math.tau)
        d = rng.uniform(0.0, rad)
        r = rng.uniform(1.5, rad * 0.85)
        c.circle(round(cx + math.cos(a) * d), round(cy + math.sin(a) * d), max(1, round(r)), rng.choice(colors))


def slab(x, y, w, h):
    c.rect(x, y, w, h, pathc[2])
    c.rect(x + 1, y + 1, w - 2, 2, pathc[3])
    c.rect(x + 2, y + 1, 1, h - 2, pathc[0])
    c.rect(x + w // 2, y + 1, 1, h - 2, pathc[0])


# ---- sky gradient ----
for y in range(80):
    c.rect(0, y, W, 1, sky[min(7, y // 10)])

# ---- stars ----
for i in range(85):
    x = rng.randint(2, 125)
    y = rng.randint(2, 46)
    if (x - 96) ** 2 + (y - 20) ** 2 < 130:
        continue
    c.set(x, y, moonsh if rng.random() < 0.5 else moon)

# ---- full moon ----
c.circle(96, 20, 17, halo)
c.circle(96, 20, 12, halo2)
c.circle(96, 20, 10, moon)
c.circle(99, 22, 8, moonsh)
c.circle(91, 17, 2, moonsh)
c.circle(97, 24, 3, moonsh)
c.circle(94, 14, 1, moonsh)
c.circle(101, 19, 1, moonsh)

# ---- distant tree line ----
for x in range(W):
    h1 = 62 + int(6 * math.sin(x * 0.09) + 3 * math.sin(x * 0.23 + 1.3))
    for yy in range(h1, 81):
        c.set(x, yy, tree_far)
for x in range(W):
    h2 = 66 + int(5 * math.sin(x * 0.16 + 0.7) + 2 * math.sin(x * 0.31 + 2.0))
    for yy in range(h2, 81):
        c.set(x, yy, tree_mid)

# ---- ground ----
c.rect(0, 80, W, 48, ground_c)
c.ellipse(102, 110, 25, 16, ground_lit)
c.rect(0, 80, W, 4, ground_lit)

# ---- mist bank ----
for y in range(58, 90):
    for x in range(W):
        v = math.sin(x * 0.15 + y * 0.7)
        if v > 0.25:
            lv = 3
        elif v > -0.05:
            lv = 2
        elif v > -0.5:
            lv = 1
        else:
            lv = 0
        c.set(x, y, mist[lv])

# ---- mid background trees ----
branch([(36, 88), (33, 76), (37, 64), (34, 54), (37, 44)], 4, trunk_d)
canopy(34, 42, 9, leaf)
canopy(40, 52, 6, leaf)
branch([(92, 88), (95, 76), (91, 64), (94, 52), (91, 44)], 4, trunk_d)
canopy(90, 42, 9, leaf)
canopy(94, 52, 6, leaf)

# ---- cottage ----
# walls
c.rect(48, 88, 40, 22, stone[1])
for i in range(60):
    sx = rng.randint(48, 86)
    sy = rng.randint(90, 108)
    sw = rng.randint(3, 6)
    sh = rng.randint(2, 3)
    c.rect(sx, sy, sw, sh, rng.choice(stone[2:5]))
for yy in (91, 94, 97, 100, 103, 106):
    c.rect(48, yy, 40, 1, stone[0])
for xx in range(51, 88, 5):
    c.line(xx, 90, xx, 108, stone[0])
c.rect(48, 88, 3, 22, stone[3])
c.rect(85, 88, 3, 22, stone[3])

# roof
c.poly([(50, 88), (67, 54), (84, 88)], roofc[1])
c.poly([(67, 54), (84, 88), (68, 88)], roofc[2])
c.line(66, 54, 68, 54, roofc[0])
c.rect(45, 86, 38, 3, roofc[0])
c.rect(45, 89, 38, 2, roofc[0])

# chimney
c.rect(74, 58, 7, 13, stone[2])
c.rect(72, 56, 11, 3, stone[3])
c.rect(73, 55, 9, 1, stone[4])
c.rect(75, 58, 5, 2, well_d)
c.circle(75, 53, 2, mist[2])
c.circle(73, 48, 3, mist[1])
c.circle(76, 43, 3, mist[3])
c.circle(74, 37, 2, mist[2])
c.circle(76, 32, 2, mist[1])

# attic window
c.circle(67, 70, 5, wood[2])
c.circle(67, 70, 3, win[0])
c.line(64, 70, 70, 70, wood[0])
c.line(67, 67, 67, 73, wood[0])

# moss on roof
for k in range(12):
    t = k / 11.0
    c.circle(round(67 - 17 * t), round(54 + 34 * t), rng.choice([1, 2]), rng.choice(moss[:3]))
    c.circle(round(67 + 17 * t), round(54 + 34 * t), rng.choice([1, 2]), rng.choice(moss[:3]))
for k in range(18):
    c.circle(52, 84, 3, moss[1])
    c.circle(80, 85, 3, moss[2])
    c.circle(62, 60, 2, moss[0])
    c.circle(74, 62, 2, moss[2])
c.circle(58, 70, 3, moss[1])
c.circle(70, 66, 2, moss[0])
c.circle(64, 58, 2, moss[2])
c.circle(78, 74, 3, moss[1])

# windows
def window(x):
    c.rect(x - 3, 89, 14, 3, glowc[2])
    c.rect(x - 2, 92, 12, 2, wood[0])
    c.rect(x - 2, 106, 12, 2, wood[0])
    c.rect(x, 93, 10, 12, win[0])
    c.rect(x, 93, 10, 5, win[1])
    c.rect(x, 98, 10, 7, win[2])
    c.rect(x + 4, 93, 2, 12, wood[0])
    c.rect(x, 97, 10, 2, wood[0])
    c.rect(x - 2, 107, 12, 2, glowc[0])

window(52)
window(74)

# door
c.rect(63, 98, 10, 11, wood[2])
c.rect(63, 98, 10, 2, wood[3])
for px in (65, 68, 71):
    c.line(px, 100, px, 108, wood[0])
c.rect(61, 96, 2, 13, wood[0])
c.set(70, 105, firef[1])
c.rect(61, 109, 14, 3, glowc[2])

# ---- stone well ----
c.rect(20, 90, 27, 12, stone[1])
c.rect(20, 90, 27, 2, stone[3])
for xx in range(23, 47, 5):
    c.line(xx, 93, xx, 101, stone[0])
c.rect(20, 101, 27, 3, stone[0])
c.ellipse(33, 92, 14, 6, stone[4])
c.ellipse(33, 92, 10, 4, stone[2])
c.ellipse(33, 93, 7, 3, well_d)
c.circle(22, 80, 1, wood[1])
c.rect(22, 80, 3, 13, wood[2])
c.rect(40, 80, 3, 13, wood[2])
c.rect(22, 78, 21, 3, wood[1])
c.rect(26, 82, 14, 4, wood[3])
c.line(41, 83, 46, 81, wood[2])
c.circle(47, 81, 1, wood[3])
c.rect(29, 86, 9, 3, wood[0])
c.line(33, 88, 33, 95, ropec)

# ---- stone path ----
c.rect(52, 106, 26, 22, glowc[2])
slab(60, 107, 12, 5)
slab(53, 112, 17, 6)
slab(44, 118, 23, 7)
slab(30, 123, 30, 5)

# small side stones
for (sx, sy, sw, sh) in [(49, 112, 5, 3), (71, 116, 5, 4), (42, 122, 6, 3), (66, 119, 7, 4), (26, 118, 5, 3), (22, 124, 7, 4)]:
    c.rect(sx, sy, sw, sh, pathc[1])

# ---- front twisted trees ----
# left giant
branch([(2, 128), (7, 112), (9, 94), (6, 76), (3, 60), (8, 42), (13, 30)], 12, trunk)
branch([(8, 74), (28, 58), (30, 50)], 5, trunk)
branch([(8, 58), (26, 44), (24, 38)], 4, trunk)
branch([(8, 46), (20, 32)], 4, trunk)
branch([(8, 42), (2, 40), (3, 34)], 3, trunk)
branch([(20, 46), (32, 40)], 2, trunk)
branch([(13, 30), (16, 22)], 2, trunk)
branch([(4, 98), (14, 90), (13, 82)], 4, trunk)
branch([(5, 118), (18, 114), (20, 108)], 3, trunk)
# right giant
branch([(126, 128), (121, 110), (119, 92), (122, 76), (125, 60), (120, 44), (116, 32)], 12, trunk)
branch([(122, 74), (102, 60), (104, 52)], 5, trunk)
branch([(120, 60), (104, 48)], 4, trunk)
branch([(121, 46), (110, 30)], 4, trunk)
branch([(118, 52), (130, 42)], 3, trunk)
branch([(120, 30), (112, 22)], 2, trunk)
branch([(116, 32), (120, 26)], 2, trunk)
branch([(124, 96), (112, 88), (113, 80)], 4, trunk)
branch([(123, 118), (110, 112), (112, 104)], 3, trunk)

# ---- bushes ----
canopy(44, 113, 6, leaf, 10)
canopy(90, 114, 6, leaf, 10)
canopy(36, 118, 5, leaf, 8)
canopy(94, 120, 6, leaf, 8)

# ---- canopies ----
canopy(24, 26, 11, leaf)
canopy(16, 34, 8, leaf)
canopy(30, 38, 7, leaf)
canopy(20, 17, 7, leaf)
canopy(32, 22, 6, leaf)
canopy(104, 36, 8, leaf)
canopy(113, 40, 7, leaf)
canopy(117, 46, 6, leaf)
canopy(96, 42, 6, leaf)
canopy(108, 30, 5, leaf)
canopy(100, 22, 4, leaf)
canopy(26, 50, 7, leaf)

# ---- ground herbs / grass tufts ----
for i in range(26):
    gx = rng.randint(0, 126)
    gy = rng.randint(84, 126)
    c.circle(gx, gy, 1, rng.choice(moss[1:4]))
for i in range(24):
    gx = rng.randint(2, 125)
    gy = rng.randint(90, 126)
    c.set(gx, gy, rng.choice(leaf))
    c.set(gx + 1, gy, rng.choice(leaf))
for i in range(10):
    c.circle(rng.randint(4, 123), rng.randint(110, 125), 1, firef[1])

# ---- fireflies ----
fire_pos = [(30, 88), (34, 121), (60, 117), (80, 113), (20, 100), (103, 121),
           (12, 62), (116, 70), (68, 120), (46, 124), (90, 119), (56, 114),
           (24, 45), (40, 28), (110, 38), (8, 58)]
for (fx, fy) in fire_pos:
    c.circle(fx, fy, 2, glowc[1])
for (fx, fy) in fire_pos:
    c.circle(fx, fy, 1, firef[0])
c.circle(96, 96, 3, glowc[1])
c.circle(30, 96, 3, glowc[1])

print(c.stats_text())
finish(c)
