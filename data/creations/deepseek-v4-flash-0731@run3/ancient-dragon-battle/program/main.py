from pixelbench_api import new_canvas, finish, save
import random

W = H = 256
c = new_canvas(W, H, name="battle")
rng = random.Random(2026)

def lerp(a, b, f):
    return (round(a[0] + (b[0] - a[0]) * f),
            round(a[1] + (b[1] - a[1]) * f),
            round(a[2] + (b[2] - a[2]) * f))

# ---------------- sky gradient ----------------
stops = [
    (0.00, (18, 8, 30)),
    (0.15, (32, 14, 52)),
    (0.30, (56, 24, 76)),
    (0.44, (92, 38, 94)),
    (0.56, (134, 52, 100)),
    (0.66, (176, 68, 96)),
    (0.75, (214, 88, 86)),
    (0.83, (240, 112, 70)),
    (0.90, (252, 148, 58)),
    (0.97, (255, 182, 62)),
    (1.00, (255, 198, 84)),
]
M = 36
skycols = []
for i in range(M):
    t = i / (M - 1.0)
    col = stops[-1][1]
    for j in range(len(stops) - 1):
        if t <= stops[j + 1][0]:
            a0, a1 = stops[j][1], stops[j + 1][1]
            col = lerp(a0, a1, (t - stops[j][0]) / (stops[j + 1][0] - stops[j][0]))
            break
    skycols.append(col)

bayer = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))
for y in range(0, 201):
    pos = (y / 200.0) * (M - 1)
    i = min(int(pos), M - 2)
    f = pos - i
    a = skycols[i]
    b = skycols[i + 1]
    for x in range(W):
        thr = (bayer[y & 3][x & 3] + 0.5) / 16.0
        c.set(x, y, b if f > thr else a)

# ---------------- clouds ----------------
def clouds():
    for (cx, cy, rx, ry, col) in [
        (30, 20, 55, 5, (52, 26, 64)),
        (96, 14, 44, 4, (52, 26, 64)),
        (152, 30, 60, 5, (52, 26, 64)),
        (60, 52, 70, 4, (96, 44, 72)),
        (30, 86, 50, 4, (96, 44, 72)),
        (150, 66, 46, 3, (96, 44, 72)),
        (196, 96, 40, 5, (196, 92, 80)),
        (120, 116, 60, 4, (196, 92, 80)),
        (60, 140, 70, 4, (240, 150, 76)),
        (228, 70, 30, 4, (52, 26, 64)),
        (10, 110, 30, 4, (96, 44, 72)),
        (250, 150, 40, 3, (196, 92, 80)),
    ]:
        c.ellipse(cx, cy, rx, ry, col)
    # sun glow
    c.circle(212, 120, 46, (234, 98, 64))
    c.circle(212, 120, 40, (242, 116, 66))
    c.circle(212, 120, 34, (250, 140, 76))
    c.circle(212, 120, 28, (254, 170, 92))
    c.circle(212, 120, 22, (255, 204, 122))
    c.circle(212, 120, 13, (255, 238, 196))

# ---------------- mountains ----------------
def mountains():
    c.poly([(0, 204), (10, 158), (28, 150), (46, 154), (66, 144), (86, 152),
            (108, 142), (130, 150), (152, 138), (174, 146), (196, 133),
            (216, 127), (236, 133), (250, 140), (256, 204)], (44, 30, 58))
    c.poly([(0, 212), (22, 170), (56, 162), (90, 168), (124, 158), (158, 166),
            (192, 158), (226, 150), (244, 158), (256, 212)], (28, 18, 38))

# ---------------- ground ----------------
def ground():
    c.poly([(0, 206), (30, 198), (70, 202), (110, 194), (150, 200), (196, 194),
            (232, 199), (256, 204), (256, 256), (0, 256)], (30, 20, 16))
    c.ellipse(128, 214, 96, 22, (42, 27, 20))
    c.ellipse(128, 226, 80, 16, (72, 46, 30))
    c.ellipse(128, 196, 60, 9, (46, 30, 26))
    for (rx, ry, rxr, ryr) in [(14, 240, 10, 5), (246, 236, 12, 5),
                              (8, 252, 14, 6), (238, 248, 12, 5), (120, 250, 40, 4)]:
        c.ellipse(rx, ry, rxr, ryr, (20, 12, 10))

# ---------------- castle ----------------
def flames(cx, by, w, h, col1, col2, col3, lean=0):
    c.poly([(cx - w, by), (cx + w, by), (cx + lean, by - int(h * 0.72))], col1)
    c.poly([(cx - int(w * 0.62), by), (cx + int(w * 0.62), by), (cx + lean, by - h)], col2)
    c.poly([(cx - int(w * 0.3), by), (cx + int(w * 0.3), by), (cx + lean, by - int(h * 0.52))], col3)

def castle():
    # wall
    for x in range(62, 198, 8):
        c.rect(x, 144, 4, 6, (46, 30, 42))
    c.rect(62, 148, 136, 48, (46, 30, 42))
    for yy in (158, 168, 178, 188):
        c.line(62, yy, 198, yy, (20, 12, 22))
    # gate
    c.circle(129, 170, 9, (14, 9, 15))
    c.rect(120, 170, 18, 26, (14, 9, 15))
    for bx in (123, 126, 129, 132, 135):
        c.line(bx, 168, bx, 196, (20, 12, 22))
    # left tower
    c.rect(84, 120, 22, 76, (46, 30, 42))
    for x in (84, 90, 96, 102):
        c.rect(x, 116, 4, 5, (46, 30, 42))
    c.line(105, 120, 105, 196, (74, 44, 52))
    # right tower
    c.rect(150, 120, 22, 76, (46, 30, 42))
    for x in (150, 156, 162, 168):
        c.rect(x, 116, 4, 5, (46, 30, 42))
    c.line(169, 120, 169, 196, (74, 44, 52))
    # keep
    c.rect(114, 100, 30, 96, (46, 30, 42))
    for x in (114, 120, 126, 132, 138):
        c.rect(x, 96, 6, 8, (46, 30, 42))
    c.line(143, 100, 143, 196, (74, 44, 52))
    # roofs
    c.poly([(80, 122), (108, 122), (94, 98)], (22, 14, 26))
    c.poly([(146, 122), (174, 122), (160, 100)], (22, 14, 26))
    # flags
    c.line(94, 98, 94, 84, (20, 10, 14))
    c.poly([(94, 84), (104, 87), (94, 92)], (146, 30, 44))
    c.line(160, 100, 160, 86, (20, 10, 14))
    c.poly([(160, 86), (170, 89), (160, 94)], (146, 30, 44))
    # windows
    for wx in (92, 102, 121, 129, 137, 152, 162):
        c.rect(wx, 124, 4, 9, (14, 9, 15))
        c.rect(wx + 1, 126, 2, 4, (232, 84, 32))
    # flames on the castle
    flames(126, 108, 15, 30, (232, 84, 32), (250, 140, 56), (255, 196, 96), 3)
    flames(142, 110, 12, 24, (232, 84, 32), (250, 140, 56), (255, 240, 180), 4)
    flames(96, 124, 10, 18, (250, 140, 56), (255, 196, 96), (255, 240, 180))
    flames(162, 124, 10, 16, (250, 140, 56), (255, 196, 96), (255, 240, 180))

# ---------------- siege towers ----------------
def siege():
    # left siege tower
    c.rect(20, 140, 38, 116, (40, 24, 18))
    c.rect(22, 138, 34, 5, (58, 36, 26))
    for x in (22, 32, 42, 52):
        c.rect(x, 136, 5, 6, (40, 24, 18))
    c.rect(20, 140, 6, 116, (20, 12, 12))
    c.rect(50, 140, 6, 116, (20, 12, 12))
    for yy in (158, 180, 202, 224):
        c.rect(20, yy, 38, 5, (58, 36, 26))
    for yy in (166, 188, 210):
        c.line(26, yy, 48, yy + 8, (20, 12, 12))
        c.line(48, yy, 26, yy + 8, (20, 12, 12))
    c.circle(31, 248, 6, (20, 12, 12))
    c.circle(47, 250, 6, (20, 12, 12))
    c.circle(31, 248, 2, (58, 36, 26))
    c.circle(47, 250, 2, (58, 36, 26))
    # right siege tower
    c.rect(206, 152, 36, 104, (40, 24, 18))
    c.rect(208, 150, 32, 5, (58, 36, 26))
    for x in (208, 218, 228, 238):
        c.rect(x, 148, 5, 6, (40, 24, 18))
    c.rect(206, 152, 6, 104, (20, 12, 12))
    c.rect(234, 152, 6, 104, (20, 12, 12))
    for yy in (172, 194, 216):
        c.rect(206, yy, 36, 5, (58, 36, 26))
    c.circle(216, 248, 6, (20, 12, 12))
    c.circle(231, 250, 6, (20, 12, 12))
    c.circle(216, 248, 2, (58, 36, 26))
    c.circle(231, 250, 2, (58, 36, 26))
    # burning beams against the wall
    for (lx, by, lw, hh) in [(68, 150, 148, 96), (126, 152, 88, 92)]:
        c.line(lx, by, lx + lw, by + hh, (20, 12, 12))
        c.line(lx + 4, by, lx + lw - 4, by + hh, (20, 12, 12))

# ---------------- smoke ----------------
def smoke():
    puffs = [
        (140, 92, 16, 10, (34, 32, 42)),
        (128, 78, 15, 9, (34, 32, 42)),
        (122, 64, 14, 8, (34, 32, 42)),
        (126, 52, 15, 9, (46, 44, 56)),
        (136, 42, 17, 10, (46, 44, 56)),
        (152, 38, 19, 11, (46, 44, 56)),
        (170, 42, 20, 11, (34, 32, 42)),
        (188, 50, 20, 12, (22, 20, 26)),
        (204, 56, 21, 13, (22, 20, 26)),
        (216, 64, 20, 12, (22, 20, 26)),
        (96, 98, 12, 8, (34, 32, 42)),
        (88, 84, 12, 9, (34, 32, 42)),
        (84, 70, 14, 9, (34, 32, 42)),
        (166, 96, 12, 8, (34, 32, 42)),
        (176, 84, 14, 9, (34, 32, 42)),
        (120, 44, 13, 8, (46, 44, 56)),
        (140, 100, 13, 7, (96, 58, 62)),
        (92, 106, 10, 6, (96, 58, 62)),
    ]
    for (cx, cy, rx, ry, col) in puffs:
        c.ellipse(cx, cy, rx, ry, col)

# ---------------- dragon (big, rim-lit) ----------------
DARK = (16, 10, 22)
MID = (24, 15, 30)
RIM = (255, 120, 66)
RIM2 = (232, 84, 40)

def dragon():
    # tail sweep lower-left
    c.ellipse(78, 66, 11, 6, DARK)
    c.ellipse(62, 72, 8, 5, DARK)
    c.ellipse(48, 77, 6, 4, DARK)
    c.poly([(48, 74), (38, 70), (33, 75), (40, 80), (48, 80)], DARK)
    # far wing (behind body, slightly lighter for depth)
    c.poly([(134, 56), (124, 14), (96, 2), (112, 30), (88, 16), (106, 38), (100, 56), (126, 60)], MID)
    # far wing rim
    c.line(122, 34, 104, 12, (40, 26, 46))
    # body
    c.ellipse(112, 62, 30, 11, DARK)
    c.ellipse(142, 56, 11, 7, DARK)
    c.ellipse(100, 56, 9, 7, DARK)
    # neck + head
    c.poly([(148, 46), (162, 42), (174, 38), (186, 40), (190, 48), (178, 54), (160, 56)], DARK)
    c.poly([(150, 54), (168, 54), (164, 62), (146, 60)], DARK)
    # horns
    c.poly([(176, 40), (182, 30), (186, 40)], (40, 28, 40))
    c.poly([(166, 42), (170, 34), (174, 42)], (40, 28, 40))
    # eye
    c.set(182, 44, (255, 170, 60))
    c.set(183, 43, (255, 220, 120))
    # folds on body
    c.line(120, 54, 138, 56, MID)
    c.line(96, 58, 112, 62, (10, 6, 14))
    c.line(105, 63, 130, 67, (10, 6, 14))
    # legs
    c.poly([(128, 66), (134, 66), (137, 74), (129, 74)], DARK)
    c.poly([(104, 64), (110, 64), (112, 70), (104, 70)], DARK)
    # near wing (over body, dark, with orange rim on top edge facing the sun)
    c.poly([(124, 60), (112, 10), (78, 0), (96, 28), (70, 16), (88, 42), (82, 58), (108, 64), (122, 66)], DARK)
    # wing rim lit by sunset
    c.line(108, 26, 88, 12, RIM)
    c.line(86, 42, 74, 30, RIM)
    c.line(76, 38, 66, 26, RIM2)
    c.line(118, 16, 102, 6, (96, 40, 60))
    # fire breath toward the keep
    c.poly([(188, 44), (212, 40), (214, 52), (190, 54)], (150, 40, 30))
    c.poly([(188, 47), (206, 44), (207, 51), (189, 53)], RIM2)
    c.poly([(192, 47), (200, 46), (201, 51), (190, 51)], (255, 204, 96))

# ---------------- figures ----------------
def foot(x, by, spear=True, shield=False):
    c.rect(x - 1, by - 6, 3, 5, (18, 13, 20))
    c.circle(x, by - 8, 2, (34, 24, 32))
    if shield:
        c.circle(x + 3, by - 5, 2, (18, 13, 20))
        c.circle(x + 3, by - 5, 1, (96, 54, 40))
    if spear:
        c.line(x + 2, by - 13, x + 2, by - 2, (176, 150, 116))
        c.line(x + 2, by - 13, x + 3, by - 10, (176, 150, 116))

def soldiers():
    # attackers in formation (spears + shields)
    rows = [(56, 100, 5, 216), (112, 150, 5, 214), (152, 226, 5, 214)]
    for (x0, x1, step, y0) in rows:
        i = 0
        for xx in range(x0, x1, step):
            for r in range(3):
                bx = xx + ((i + r) % 3) - 1
                foot(bx, y0 + r * 10 + (i % 2), spear=True, shield=(r == 0))
            i += 1
    # defenders on the wall
    for kx in (68, 76, 72, 156, 160, 164, 168, 172, 176, 180, 184, 188):
        foot(kx, 150, spear=True, shield=True)
    # standard bearers
    for (bx, by) in [(116, 216), (148, 214), (52, 218)]:
        c.line(bx, by - 3, bx, by, (18, 13, 20))
        c.poly([(bx, by - 3), (bx + 8, by + 1), (bx, by + 5)], (146, 30, 44))
    # archers on siege tops
    for (bx, by) in [(26, 138), (36, 138), (46, 140)]:
        foot(bx, by, spear=False)
    for (bx, by) in [(212, 150), (222, 150), (230, 152)]:
        foot(bx, by, spear=False)
    # fallen on the field
    c.ellipse(88, 240, 4, 3, (18, 13, 20))
    c.ellipse(178, 242, 4, 2, (18, 13, 20))
    c.ellipse(138, 238, 3, 2, (18, 13, 20))

# ---------------- arrows / embers ----------------
def arrow(x, y, dx, dy, L, col):
    tx, ty = x + dx * L, y + dy * L
    c.line(x, y, tx - dx, ty - dy, col)
    c.line(tx, ty, tx - dx - dy, ty - dy + dx, col)
    c.line(tx, ty, tx - dx + dy, ty - dy - dx, col)
    c.line(x + dx, y + dy, x - dy, y + dx, col)

def arrows():
    light = [(24, 150, 1, -2, 10), (46, 158, 2, -3, 8), (16, 122, 1, -2, 9),
            (40, 96, 2, -3, 8), (28, 88, 1, -1, 11), (66, 152, 3, -2, 8)]
    dark = [(168, 138, 2, -1, 11), (150, 122, 1, -1, 10), (186, 134, 3, -1, 8),
           (196, 148, 2, -1, 9), (122, 150, 3, -1, 8), (206, 146, 1, -1, 8)]
    for (x, y, dx, dy, L) in light:
        arrow(x, y, dx, dy, L, (216, 188, 158))
    for (x, y, dx, dy, L) in dark:
        arrow(x, y, dx, dy, L, (32, 18, 26))
    # more falling arrows mid-air
    for (x, y, dx, dy, L) in [(30, 170, 1, -3, 8), (18, 96, 0, -2, 8), (228, 160, 0, -1, 9),
                             (200, 120, -1, -1, 8), (60, 90, 1, -2, 8)]:
        arrow(x, y, dx, dy, L, (28, 16, 24))

def embers():
    for _ in range(220):
        x = rng.randint(30, 255)
        y = rng.randint(40, 238)
        col = rng.choice([(232, 84, 32), (250, 140, 56), (255, 196, 96), (255, 240, 180), (96, 58, 62)])
        c.set(x, y, col)
    c.rect(0, 244, 256, 12, (18, 11, 9))
    for rx in range(0, 256, 8):
        c.rect(rx, 250, 8, 6, (14, 8, 8))

# ---------------- render ----------------
clouds()
mountains()
ground()
castle()
siege()
smoke()
dragon()
soldiers()
arrows()
embers()

# ---- verification: count dragon pixels ----
def count_color(col):
    idx = c.color(col)
    n = 0
    for yy in range(14, 92):
        for xx in range(20, 215):
            if c.get(xx, yy) == idx:
                n += 1
    return n

for name, col in [("dragon-dark", DARK), ("dragon-mid", MID),
                 ("rim", RIM), ("rim2", RIM2),
                 ("fire-outer", (150, 40, 30))]:
    print(name, count_color(col))

# ---- verification: count dragon pixels ----
def count_color(col):
    idx = c.color(col)
    n = 0
    for yy in range(14, 92):
        for xx in range(20, 215):
            if c.get(xx, yy) == idx:
                n += 1
    return n

def count_in(col, x0, y0, x1, y1):
    idx = c.color(col)
    n = 0
    for yy in range(y0, y1):
        for xx in range(x0, x1):
            if c.get(xx, yy) == idx:
                n += 1
    return n

print("dragon-head dark px:", count_in(DARK, 146, 32, 196, 66))
print(c.stats_text())
save("battle", c)
finish(c)
