c = new_canvas(128, 128, name="output")
import random

# ---------------- palette ----------------
SKY = ["#2b1a4a", "#3d2159", "#53296a", "#6d3273", "#8a3c74", "#a8486f",
       "#c25a66", "#d8705e", "#e88a56", "#f2a85c", "#f8c470"]
HORIZON = 75

# ---------------- sky gradient ----------------
bands = [0, 5, 11, 18, 25, 32, 39, 46, 53, 61, 68, HORIZON]
for i in range(11):
    c.rect(0, bands[i], 128, bands[i + 1] - bands[i], SKY[i])
for i in range(10):
    y = bands[i + 1]
    c.dither(0, y - 1, 128, 1, [SKY[i], SKY[i + 1]], pattern="checker")
    c.dither(0, y, 128, 1, [SKY[i + 1], SKY[i]], pattern="checker")

# ---------------- sun ----------------
SUNX, SUNY = 42, 69
c.circle(SUNX, SUNY, 19, "#ffcf7a")
c.circle(SUNX, SUNY, 16, "#ffe9a0")
c.circle(SUNX, SUNY, 12, "#fff6cf")

# ---------------- clouds ----------------
def cloud(cx, cy, bumps, dark, light, rim=None):
    shape = [(cx + dx, cy - ry, rx, ry) for dx, rx, ry in bumps]
    for x, y, rx, ry in shape:
        c.ellipse(x, y, rx, ry, light)
    for x, y, rx, ry in shape:
        c.ellipse(x, y - 2, rx - 1, ry, dark)
    if rim:
        for x, y, rx, ry in shape:
            c.ellipse(x, y - 4, max(1, rx - 3), max(1, ry - 1), rim)

B1 = [(-11, 6, 2), (-3, 8, 4), (7, 6, 3), (14, 4, 2)]
B2 = [(-13, 7, 2), (-4, 9, 3), (6, 7, 4), (15, 5, 2)]
B3 = [(-8, 6, 2), (0, 7, 3), (8, 5, 2)]
B4 = [(-6, 5, 2), (1, 6, 3), (8, 4, 2)]

cloud(24, 16, B2, "#2b1a4a", "#4a2563", "#5c2d6d")
cloud(97, 13, B1, "#2b1a4a", "#4a2563", "#5c2d6d")
cloud(64, 24, B3, "#3d2159", "#6d3273", "#7b3673")
cloud(12, 30, B4, "#53296a", "#7b3673", "#8a3c74")
cloud(106, 32, B2, "#53296a", "#8a3c74", "#9a4272")
cloud(42, 40, B1, "#6d3273", "#a8486f", "#bb5069")
cloud(110, 47, B4, "#8a3c74", "#c25a66", "#d8705e")
cloud(16, 50, B3, "#8a3c74", "#c25a66", "#d8705e")
cloud(70, 56, B2, "#a8486f", "#e88a56", "#f8c470")
cloud(28, 63, B4, "#c25a66", "#f2a85c", "#ffcf7a")
cloud(56, 70, [(-7, 7, 1), (2, 6, 2)], "#d8705e", "#ffcf7a", "#ffe9a0")

# ---------------- sea ----------------
SEA = ["#f2a85c", "#d8705e", "#b4556a", "#8f4068", "#6d335f", "#4e2750", "#361d3f"]
sb = [HORIZON, 78, 83, 89, 96, 104, 114, 128]
for i in range(7):
    c.rect(0, sb[i], 128, sb[i + 1] - sb[i], SEA[i])
for i in range(6):
    c.dither(0, sb[i + 1] - 1, 128, 1, [SEA[i], SEA[i + 1]], pattern="checker")

random.seed(7)
glint = ["#fff6cf", "#ffe9a0", "#ffcf7a", "#f2a85c"]
for y in range(HORIZON, 118):
    t = (y - HORIZON) / 43.0
    half = int(3 + 15 * t)
    for _ in range(max(1, int(4 - 3 * t))):
        x = SUNX + random.randint(-half, half)
        c.rect(x, y, random.randint(1, 3), 1, glint[min(3, int(t * 4))])

for y, x0, x1, col in [(76, 0, 127, "#ffcf7a"), (81, 66, 127, "#e88a56"),
                       (87, 84, 120, "#b4556a"), (95, 0, 20, "#8f4068"),
                       (103, 94, 127, "#6d335f")]:
    c.line(x0, y, x1, y, col)

# ================= castle (drawn before the cliff; the cliff buries its base) =================
ST_D = "#2b2140"
ST_M = "#453354"
ST_L = "#6b4a63"
ST_R = "#c4725f"
ROOF_D = "#3a2340"
ROOF_L = "#7a3b58"
WIN = "#ffe0a0"
FLAG = "#d8484f"
FLAG_D = "#9a2f3e"

def crenel(x, y, w, col, rim=None):
    for i in range(0, w - 1, 3):
        c.rect(x + i, y, 2, 2, col)
    if rim:
        c.rect(x, y, 1, 2, rim)

# curtain wall
c.rect(85, 54, 20, 22, ST_M)
c.rect(85, 54, 3, 22, ST_L)
c.rect(101, 54, 4, 22, ST_D)
c.rect(85, 54, 20, 1, ST_D)
crenel(85, 51, 20, ST_M, ST_R)
c.line(85, 54, 85, 70, ST_R)

# gatehouse rising from the wall
c.rect(90, 46, 11, 30, ST_M)
c.rect(90, 46, 3, 30, ST_L)
c.rect(98, 46, 3, 30, ST_D)
crenel(90, 43, 11, ST_M, ST_R)
c.rect(90, 46, 11, 1, ST_D)
c.line(90, 46, 90, 70, ST_R)
# gate arch
c.path("M93 65 L93 58 Q95.5 54 98 58 L98 65 Z", "#1e1730")
c.rect(94, 60, 3, 2, "#3a2340")
c.line(92, 57, 92, 65, ST_L)

# left tower
c.rect(74, 42, 11, 34, ST_M)
c.rect(74, 42, 3, 34, ST_L)
c.rect(82, 42, 3, 34, ST_D)
c.rect(73, 39, 13, 3, ST_M)
c.rect(73, 39, 3, 3, ST_L)
crenel(73, 36, 13, ST_M, ST_R)
c.poly([(79, 23), (86, 37), (72, 37)], ROOF_D)
c.poly([(79, 23), (79, 37), (72, 37)], ROOF_L)
c.line(79, 23, 72, 37, "#a8505f")
c.line(74, 42, 74, 72, ST_R)
c.line(73, 39, 73, 41, ST_R)
c.rect(77, 47, 2, 3, WIN)
c.rect(80, 56, 2, 3, WIN)
c.rect(77, 64, 2, 3, WIN)

# right tower, taller
c.rect(105, 34, 13, 42, ST_M)
c.rect(105, 34, 3, 42, ST_L)
c.rect(115, 34, 3, 42, ST_D)
c.rect(104, 31, 15, 3, ST_M)
c.rect(104, 31, 3, 3, ST_L)
crenel(104, 28, 15, ST_M, ST_R)
c.poly([(111, 12), (119, 27), (103, 27)], ROOF_D)
c.poly([(111, 12), (111, 27), (103, 27)], ROOF_L)
c.line(111, 12, 103, 27, "#a8505f")
c.line(105, 34, 105, 68, ST_R)
c.line(104, 31, 104, 33, ST_R)
c.rect(108, 39, 2, 3, WIN)
c.rect(112, 47, 2, 3, WIN)
c.rect(108, 55, 2, 3, WIN)

# flags
c.line(79, 23, 79, 15, ST_D)
c.poly([(80, 16), (89, 18), (80, 21)], FLAG)
c.line(80, 20, 88, 18, FLAG_D)
c.line(111, 12, 111, 4, ST_D)
c.poly([(112, 5), (122, 7), (112, 10)], FLAG)
c.line(112, 9, 121, 7, FLAG_D)

# ================= cliff =================
ROCK_D = "#241a33"
ROCK_M = "#3a2a47"
ROCK_L = "#55395a"
ROCK_R = "#8a4f63"
GRASS_D = "#2d3340"
GRASS_L = "#5c5a4c"

top = [(66, 80), (70, 75), (76, 72), (84, 70), (92, 67), (102, 64),
       (112, 61), (127, 58)]
cliff = top + [(127, 122), (108, 119), (90, 117), (76, 112),
               (68, 104), (64, 92)]
c.poly(cliff, ROCK_M)
# receding right half in shadow
c.poly([(92, 67), (102, 64), (112, 61), (127, 58), (127, 122), (108, 119),
        (96, 117), (92, 100)], ROCK_D)
# lit left shoulder
c.poly([(66, 80), (70, 75), (76, 72), (84, 70), (88, 84), (84, 102),
        (74, 108), (68, 100), (64, 90)], ROCK_L)

ROCKSET = {c.color(ROCK_M), c.color(ROCK_D), c.color(ROCK_L)}
def tex(x, y, col):
    if 0 <= x < 128 and 0 <= y < 128 and c.get(x, y) in ROCKSET:
        c.set(x, y, col)

# strata: shallow runs following the bedding, broken into short dashes
random.seed(23)
for _ in range(40):
    x0 = random.randint(66, 122)
    y0 = random.randint(72, 118)
    col = ROCK_D if random.random() < 0.62 else ROCK_L
    ln = random.randint(4, 9)
    for i in range(ln):
        if (i + x0) % 7 != 6:
            tex(x0 + i, y0 - i // 6, col)
# ledge shelves, horizontal and well separated
for x0, y0, ln, col in [(96, 82, 26, ROCK_D), (102, 96, 24, ROCK_D),
                        (88, 108, 30, ROCK_D), (68, 88, 14, ROCK_L),
                        (70, 100, 12, ROCK_L)]:
    for i in range(ln):
        tex(x0 + i, y0, col)

# rim light down the seaward silhouette
for a, b in [((66, 80), (70, 75)), ((64, 92), (66, 80)), ((68, 104), (64, 92))]:
    c.line(a[0], a[1], b[0], b[1], ROCK_R)
c.line(70, 75, 76, 72, ROCK_R)
c.line(76, 73, 84, 71, "#6d4260")
c.line(68, 105, 76, 112, "#6d4260")

# grass crown
for (x0, y0), (x1, y1) in zip(top, top[1:]):
    c.line(x0, y0, x1, y1, GRASS_L)
    c.line(x0, y0 + 1, x1, y1 + 1, GRASS_D)
    c.line(x0, y0 + 2, x1, y1 + 2, GRASS_D)
c.line(66, 80, 70, 75, ROCK_R)

# cliff reflection smeared into the water
for y in range(118, 128):
    c.line(66, y, 127, y, "#2a1a33")

# ================= foreground rocks =================
FG_D = "#140f1f"
FG_M = "#201829"
FG_L = "#39283c"
FG_R = "#6b3f50"

c.poly([(0, 128), (0, 110), (7, 104), (16, 108), (25, 101), (34, 107),
        (43, 113), (54, 108), (64, 115), (78, 112), (94, 118), (110, 114),
        (122, 119), (127, 116), (127, 128)], FG_M)
c.poly([(0, 128), (0, 118), (14, 116), (30, 120), (48, 121), (70, 123),
        (96, 121), (127, 125), (127, 128)], FG_D)

FGSET = {c.color(FG_M), c.color(FG_D)}
random.seed(5)
for _ in range(60):
    x0 = random.randint(0, 126)
    y0 = random.randint(102, 127)
    for i in range(random.randint(2, 6)):
        x, y = x0 + i, y0 + i // 2
        if 0 <= x < 128 and 0 <= y < 128 and c.get(x, y) in FGSET:
            c.set(x, y, FG_L)

for a, b in [((7, 104), (16, 108)), ((25, 101), (34, 107)), ((54, 108), (64, 115)),
             ((78, 112), (94, 118)), ((110, 114), (122, 119))]:
    c.line(a[0], a[1], b[0], b[1], FG_L)
c.line(7, 104, 0, 110, FG_R)
c.line(25, 101, 17, 107, FG_R)
c.line(54, 108, 44, 112, FG_L)

# sea stack
c.poly([(16, 128), (13, 98), (18, 89), (24, 96), (25, 128)], FG_M)
c.poly([(19, 128), (19, 93), (24, 97), (25, 128)], FG_D)
c.line(13, 98, 18, 89, FG_R)
c.line(14, 99, 15, 114, FG_L)
c.line(18, 89, 22, 94, FG_L)

# ================= birds =================
BIRD = "#2b1a4a"
for bx, by, s in [(26, 36, 1), (34, 41, 1), (20, 45, 0), (52, 30, 1), (58, 36, 0)]:
    if s:
        c.line(bx - 2, by, bx - 1, by - 1, BIRD)
        c.line(bx + 1, by - 1, bx + 2, by, BIRD)
        c.set(bx, by, BIRD)
    else:
        c.set(bx - 1, by, BIRD)
        c.set(bx, by, BIRD)
        c.set(bx + 1, by, BIRD)

view(c)
save("castle-title-screen", c)
finish(c)
