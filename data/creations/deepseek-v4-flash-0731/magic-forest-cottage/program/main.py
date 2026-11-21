from pixelbench_api import new_canvas, finish, save, view
import random

W = H = 128
c = new_canvas(W, H, name="magic_forest_cottage")

def col(hexc):
    return c.color(hexc)

def shade(hexc, f):
    r = int(hexc[1:3], 16); g = int(hexc[3:5], 16); b = int(hexc[5:7], 16)
    if f >= 0:
        r = int(r + (255 - r) * f); g = int(g + (255 - g) * f); b = int(b + (255 - b) * f)
    else:
        f = -f
        r = int(r * (1 - f)); g = int(g * (1 - f)); b = int(b * (1 - f))
    return "#%02x%02x%02x" % (r, g, b)

rng = random.Random(13)

# ---------------------------------------------------------------- sky ----
sky_top = "#0a0520"; sky_bot = "#33255c"
N = 16
skycols = []
for i in range(N):
    t = i / (N - 1)
    r = int(int(sky_top[1:3], 16) + (int(sky_bot[1:3], 16) - int(sky_top[1:3], 16)) * t)
    g = int(int(sky_top[3:5], 16) + (int(sky_bot[3:5], 16) - int(sky_top[3:5], 16)) * t)
    b = int(int(sky_top[5:7], 16) + (int(sky_bot[5:7], 16) - int(sky_top[5:7], 16)) * t)
    skycols.append((r, g, b))
for y in range(H):
    i = min(N - 1, int(y / (H - 1) * N))
    c.rect(0, y, W, 1, col("#%02x%02x%02x" % skycols[i]))

# ---------------------------------------------------------------- stars ---
star_cols = [col("#f6f2e6"), col("#ffffff"), col("#d6d0ff"), col("#ffeabb")]
for _ in range(130):
    x = rng.randint(0, 127); y = rng.randint(0, 80)
    c.set(x, y, rng.choice(star_cols))
for _ in range(5):
    x = rng.randint(2, 124); y = rng.randint(0, 44)
    sc = rng.choice(star_cols)
    c.set(x, y, sc); c.set(x + 1, y, sc); c.set(x, y + 1, sc)

# ---------------------------------------------------------------- moon ---
mx, my = 84, 26
for rr, gc in [(25, "#31225e"), (21, "#3f2e70"), (18, "#503c84"), (15, "#644c98")]:
    c.circle(mx, my, rr, col(gc))
core = col("#fdf4d0")
c.circle(mx, my, 13, core)
crater = col("#e8d6a8")
c.circle(mx + 3, my + 5, 7, crater)
c.set(mx - 5, my - 4, crater); c.set(mx + 6, my - 2, crater); c.set(mx + 1, my + 6, crater)
c.set(mx - 6, my + 1, crater); c.set(mx + 3, my + 8, crater)

# ------------------------------------------------------- back treeline ----
tl = col("#140b26")
for x0 in range(0, 128, 5):
    h = rng.randint(5, 13)
    c.poly([(x0, 88), (x0 + 2, 88 - h), (x0 + 5, 88)], tl)

# --------------------------------------------------------------- ground --
g1 = col("#1a1130"); g2 = col("#221840")
c.rect(0, 92, W, 36, g1)
c.rect(0, 108, W, 20, g2)
# ground texture specks
for _ in range(160):
    c.set(rng.randint(0, 127), rng.randint(94, 127), g1 if rng.random() < 0.5 else g2)

# ------------------------------------------------------ twisted trees ----
trunk = col("#160c1f"); trunk2 = col("#221333")
# left tree trunk
c.poly([(4, 100), (17, 100), (19, 90), (15, 80), (11, 70), (9, 60), (11, 50),
        (16, 42), (14, 34), (11, 26), (6, 22), (0, 18), (0, 26), (3, 36),
        (2, 48), (3, 60), (1, 72), (3, 84)], trunk)
# left branches (rightward)
c.poly([(14, 40), (32, 32), (38, 28), (30, 36), (14, 44)], trunk)
c.poly([(12, 58), (28, 54), (31, 50), (11, 53)], trunk)
c.poly([(10, 70), (26, 72), (28, 68), (9, 66)], trunk)
c.poly([(10, 84), (22, 88), (24, 84), (9, 82)], trunk)
c.poly([(8, 92), (18, 98), (20, 94), (7, 90)], trunk)
# trunk edge light
c.line(11, 30, 4, 96, trunk2)

# right tree trunk
c.poly([(110, 100), (123, 100), (121, 88), (116, 78), (119, 66), (113, 56),
        (117, 46), (112, 36), (108, 40), (110, 50), (105, 58), (107, 68),
        (103, 78), (106, 90)], trunk)
c.poly([(112, 44), (98, 38), (94, 34), (110, 38)], trunk)
c.poly([(116, 58), (102, 54), (99, 50), (115, 53)], trunk)
c.poly([(118, 70), (104, 68), (102, 64), (117, 66)], trunk)
c.poly([(120, 84), (108, 82), (106, 78), (119, 80)], trunk)
c.line(116, 44, 108, 94, trunk2)

# -------------------------------------------------------------- foliage --
f1 = col("#341624"); f2 = col("#3d1c2e"); f3 = col("#3a1e3e"); f4 = col("#4a2440"); f5 = col("#582a50")
# left canopy
c.ellipse(15, 32, 22, 15, f1)
c.ellipse(9, 27, 15, 11, f2)
c.ellipse(22, 25, 12, 9, f3)
c.ellipse(12, 20, 9, 7, f4)
c.ellipse(24, 19, 9, 6, f5)
# right canopy
c.ellipse(114, 36, 19, 13, f1)
c.ellipse(120, 31, 14, 10, f2)
c.ellipse(109, 29, 11, 8, f3)
c.ellipse(118, 26, 8, 6, f4)
for (ex, ey, rx, ry, fc) in [(33, 30, 6, 4, f3), (28, 22, 5, 4, f4), (96, 33, 6, 4, f3), (102, 27, 5, 4, f4)]:
    c.ellipse(ex, ey, rx, ry, fc)

# mid mist band (behind cottage)
mm = col("#473b74")
for x in range(0, 128, 3):
    c.rect(x, 90 + ((x * 5) // 13) % 2, 3, 3, mm)

# ------------------------------------------------------------- cottage --
wood = col("#3a2014"); wood2 = col("#28160e"); wood3 = col("#4a2c1c")
stone1 = col("#3a3548"); stone2 = col("#4d4760"); stone3 = col("#2e2a3c")
roofc = col("#2a1810"); roof2 = col("#3a2418"); roof3 = col("#4a3020")
moss1 = col("#2c4826"); moss2 = col("#385c30"); moss3 = col("#46703c")
win_wall = col("#6e3416")
win_core = col("#ff9630"); win_bright = col("#ffc464")
doorc = col("#20100c"); doorw = col("#382012")
drk = col("#120a18")

# chimney (behind roof)
c.rect(72, 40, 10, 26, stone1)
c.rect(70, 38, 14, 5, stone2)
sm = col("#5e4e86")
for (sx, sy) in [(71, 35), (69, 32), (72, 29), (67, 26)]:
    c.set(sx, sy, sm)

# walls
c.rect(48, 68, 32, 34, wood)
for x in range(50, 78, 8):
    c.line(x, 70, x, 101, wood2)
# stone base
c.rect(48, 88, 32, 14, stone1)
c.rect(48, 96, 32, 6, stone2)
c.line(48, 94, 80, 94, stone3)
for x in (54, 62, 70):
    c.line(x, 88, x, 101, stone3)

# roof
c.poly([(65, 44), (40, 76), (90, 76)], roofc)
c.poly([(65, 50), (44, 75), (86, 75)], roof2)
c.rect(40, 76, 50, 3, roof3)
c.line(63, 46, 67, 46, roof3)
for (ex, ey, rx, ry) in [(47, 70, 6, 3), (57, 64, 5, 3), (72, 62, 5, 3), (82, 71, 6, 3),
                        (66, 56, 4, 2), (51, 62, 4, 2)]:
    c.ellipse(ex, ey, rx, ry, moss1)
c.rect(42, 76, 9, 2, moss2)
c.rect(80, 76, 9, 2, moss2)
c.ellipse(64, 73, 6, 3, moss2)
c.rect(60, 76, 8, 2, moss3)
c.rect(46, 78, 3, 2, moss3)

# doorway
c.rect(58, 80, 12, 22, doorc)
c.rect(59, 84, 10, 18, win_core)
c.circle(63, 82, 4, win_core)
c.rect(58, 80, 12, 2, doorw)
c.rect(58, 80, 2, 22, doorw)
c.rect(68, 80, 2, 22, doorw)
c.rect(63, 88, 4, 4, win_bright)
c.rect(63, 96, 4, 4, win_bright)

# windows
for wx in (49, 73):
    c.rect(wx, 76, 6, 7, win_wall)      # glow on wall
    c.rect(wx, 77, 6, 8, win_core)
    c.rect(wx + 1, 78, 4, 5, win_bright)
    c.rect(wx + 2, 77, 2, 8, wood2)     # mullion

# vine on the wall
c.line(46, 62, 44, 100, wood2)
c.line(82, 64, 82, 96, wood2)
c.line(44, 70, 40, 74, moss1)
c.line(82, 78, 84, 82, moss1)
c.ellipse(83, 88, 2, 1, moss2)

# light pools on the ground
for gx in (52, 76):
    c.ellipse(gx, 103, 8, 3, win_wall)
c.ellipse(64, 105, 10, 3, col("#8a4a20"))

# ---------------------------------------------------------------- path --
ps1 = col("#4c4660"); ps2 = col("#5e5876"); ps3 = col("#716a8c")
slabs = [(64, 102, 8, 3), (60, 107, 7, 3), (67, 111, 9, 3), (63, 116, 7, 3), (67, 121, 8, 3)]
for (sx, sy, srx, sry) in slabs:
    c.ellipse(sx, sy, srx, sry, ps2)
    c.line(sx - srx + 1, sy - sry, sx + srx - 1, sy - sry, ps3)
    c.rect(sx - 3, sy, srx * 2 - 4, 1, ps3)
c.ellipse(66, 101, 4, 2, ps1)
c.ellipse(50, 106, 4, 2, ps1)
c.ellipse(77, 110, 4, 2, ps1)

# ---------------------------------------------------------------- well --
c.ellipse(103, 102, 12, 7, stone2)
c.ellipse(103, 102, 8, 5, drk)
c.ellipse(103, 104, 10, 4, stone1)
c.ellipse(96, 99, 3, 2, moss2)
c.rect(94, 82, 5, 20, wood2)
c.rect(107, 82, 5, 20, wood2)
c.poly([(94, 82), (103, 72), (112, 82)], roofc)
c.rect(94, 82, 18, 2, roof2)
c.ellipse(99, 79, 3, 2, moss1)
c.rect(98, 86, 10, 3, wood3)
c.line(101, 89, 101, 102, wood2)
c.rect(100, 102, 4, 5, wood3)
c.rect(101, 103, 2, 3, win_wall)

# ---------------------------------------------------------------- mist --
mist1 = col("#554682"); mist2 = col("#695a96"); mist3 = col("#7d6eaa")
def mistrow(y0, thick, mc, seed):
    r2 = random.Random(seed)
    for x in range(0, 128, 2):
        c.rect(x, y0 + r2.randint(0, 2), 2, thick, mc)
mistrow(103, 5, mist1, 21)
mistrow(109, 6, mist2, 22)
mistrow(116, 7, mist3, 23)
c.rect(0, 124, 128, 4, mist3)
c.ellipse(36, 96, 8, 3, mist1)
c.ellipse(96, 97, 6, 3, mist1)
c.ellipse(16, 100, 9, 3, mist2)
# warm light kissing the mist
c.ellipse(64, 106, 9, 2, col("#7c5a54"))

# front foliage overhang
c.ellipse(30, 62, 7, 4, f2)
c.ellipse(33, 66, 5, 3, f3)
c.ellipse(92, 60, 7, 4, f2)
c.ellipse(89, 64, 5, 3, f4)
c.ellipse(24, 104, 8, 4, f2)

# fireflies
ff1 = col("#ffe488"); ff2 = col("#ffd058")
for (fx, fy) in [(30, 52), (22, 44), (36, 60), (24, 70), (40, 84), (96, 58),
                (104, 50), (92, 84), (100, 88), (80, 92), (46, 96), (86, 108),
                (34, 100), (74, 112), (58, 118)]:
    c.set(fx, fy, ff2)
    c.set(fx, fy, ff1)
c.set(96, 92, ff1); c.set(28, 66, ff1)

# tiny glowing mushrooms
for (mxx, myy) in [(82, 109), (50, 112)]:
    c.ellipse(mxx, myy, 3, 2, col("#e07038"))
    c.set(mxx, myy - 1, ff2)
    c.set(mxx - 1, myy - 1, ff1)

# a few floating leaves
leaves = col("#5a2440")
for (lx, ly) in [(70, 56), (58, 64), (76, 60)]:
    c.set(lx, ly, leaves)

print(c.stats_text())
print("colors_used =", c.stats()["colors_used"])

save("preview", c)

finish(c)
