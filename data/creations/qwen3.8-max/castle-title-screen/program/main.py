import math

W = H = 128
HORIZON = 88

# ---------------------------------------------------------------- dither utils
BAYER = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))


def b4(x, y):
    return BAYER[y & 3][x & 3] / 16.0


def ramp(colors, t, x, y):
    """Ordered-dithered sample of a colour ramp at 0<=t<=1."""
    n = len(colors)
    f = max(0.0, min(1.0, t)) * (n - 1)
    i = int(f)
    if i >= n - 1:
        return colors[-1]
    frac = f - i
    return colors[i] if b4(x, y) >= frac else colors[i + 1]


# ------------------------------------------------------------------- palette
SKY = ["#100a20", "#180f31", "#221341", "#2e184f", "#3d1f5c", "#4e2566",
       "#622c6c", "#78356d", "#90406b", "#a94d68", "#c15c62", "#d6705a",
       "#e68551", "#f29a4d", "#f9b255", "#fdc96b", "#ffe39b"]

SEA = ["#9a5468", "#7c4165", "#5a2e5c", "#452353", "#351b48", "#291540",
       "#1f1036", "#170c2c", "#110a22"]

GLOW = ["#ffe39b", "#ffd07a", "#ffb457", "#f79a4e", "#e88452"]

SUN = {"core": "#fff8d6", "c2": "#ffeaa8", "c3": "#ffd477",
       "c4": "#ffb451", "c5": "#ff9438"}

CLOUD = {
    "hi_body": "#2b1a44", "hi_rim": "#4d2c5e",
    "mid_body": "#5b2f5e", "mid_rim": "#a94f64",
    "low_body": "#3d2043", "low_rim": "#ffab4f",
    "dark_body": "#2a1536", "dark_rim": "#f08a4b",
}

ROCK = {"front": "#0d0819", "mid": "#1a1130", "back": "#261b3f",
        "lite": "#3a2a52", "rim": "#5c4068", "warm": "#7c4e66",
        "hot": "#a06464"}

CASTLE = {"shadow": "#191129", "body": "#251a3a", "lite": "#332549",
          "rim": "#7d4a5c", "hot": "#a8605f", "roof": "#2c1c3c",
          "rooflite": "#4a2c4c"}

WIN = ["#ffd97a", "#ff9d3d"]
FLAG = ["#c0404c", "#8e2a3a", "#e0a13c"]

# ------------------------------------------------------------------- helpers


def cloud(c, cx, base_y, bumps, body, rim, rim_dy=2):
    minx = min(cx + dx - rx for dx, rx, ry in bumps)
    maxx = max(cx + dx + rx for dx, rx, ry in bumps)
    for dx, rx, ry in bumps:
        c.ellipse(cx + dx, base_y - ry + rim_dy, rx, ry, rim)
    c.rect(minx, base_y - 1, maxx - minx + 1, rim_dy + 1, rim)
    for dx, rx, ry in bumps:
        c.ellipse(cx + dx, base_y - ry, rx, ry, body)
    c.rect(minx, base_y - 2, maxx - minx + 1, 3, body)


def merlons(c, xs, y, h, w, col):
    for px in xs:
        c.rect(px, y, w, h, col)


def bird(c, x, y, col, s=1):
    if s == 1:
        for dx, dy in ((0, 0), (1, 1), (2, 0)):
            c.set(x + dx, y + dy, col)
    else:
        for dx, dy in ((0, 0), (1, 1), (2, 2), (3, 1), (4, 0)):
            c.set(x + dx, y + dy, col)


# ============================================================== build scene
c = new_canvas(W, H, name="result")

# --- sky -------------------------------------------------------------------
for y in range(HORIZON):
    t = y / float(HORIZON - 1)
    for x in range(W):
        c.set(x, y, ramp(SKY, t, x, y))

# faint stars in the upper sky
for (sx, sy) in ((12, 6), (34, 11), (58, 5), (77, 14), (101, 7), (119, 17),
                 (46, 19), (89, 4), (5, 21), (66, 12)):
    c.set(sx, sy, "#4b3a72")
for (sx, sy) in ((23, 4), (95, 11), (112, 6), (40, 8)):
    c.set(sx, sy, "#6a5694")

# --- sun glow (ordered dither, radial) -------------------------------------
SCX, SCY, SR = 88, 61, 23
GOUT = 46.0
for y in range(HORIZON):
    for x in range(W):
        d = math.hypot(x - SCX, (y - SCY) * 1.0)
        if d <= SR or d >= GOUT:
            continue
        t = (GOUT - d) / (GOUT - SR)
        t = t ** 2.1
        gi = 0 if d < 28 else (1 if d < 33 else (2 if d < 39 else 3))
        if b4(x, y) < t:
            c.set(x, y, GLOW[gi])

# --- sun disc --------------------------------------------------------------
for y in range(SCY - SR - 1, SCY + SR + 2):
    for x in range(SCX - SR - 1, SCX + SR + 2):
        if not (0 <= x < W and 0 <= y < HORIZON):
            continue
        d = math.hypot(x - SCX, y - SCY)
        if d > SR:
            continue
        if d < 6:
            col = SUN["core"]
        elif d < 11:
            col = SUN["c2"]
        elif d < 16:
            col = SUN["c3"]
        elif d < 20.5:
            col = SUN["c4"]
        else:
            col = SUN["c5"]
        c.set(x, y, col)

# --- clouds ----------------------------------------------------------------
# high wisps
cloud(c, 28, 22, [(-12, 14, 4), (2, 16, 6), (17, 12, 4)],
      CLOUD["hi_body"], CLOUD["hi_rim"])
cloud(c, 100, 15, [(-20, 16, 3), (0, 20, 5), (20, 15, 3)],
      CLOUD["hi_body"], CLOUD["hi_rim"])
cloud(c, 62, 31, [(-11, 12, 3), (5, 14, 4)],
      CLOUD["hi_body"], CLOUD["hi_rim"])
# mid banks
cloud(c, 18, 47, [(-16, 16, 6), (2, 18, 9), (19, 14, 6)],
      CLOUD["mid_body"], CLOUD["mid_rim"])
cloud(c, 108, 43, [(-16, 14, 5), (0, 16, 7), (16, 12, 4)],
      CLOUD["mid_body"], CLOUD["mid_rim"])
cloud(c, 58, 56, [(-13, 14, 5), (4, 16, 7), (19, 10, 4)],
      CLOUD["mid_body"], CLOUD["mid_rim"])
# low thin bands crossing the sun
cloud(c, 88, 68, [(-26, 16, 2), (-6, 20, 3), (16, 14, 2), (32, 10, 2)],
      CLOUD["low_body"], CLOUD["low_rim"], rim_dy=1)
cloud(c, 82, 79, [(-30, 18, 3), (-8, 22, 4), (16, 16, 3), (36, 12, 2)],
      CLOUD["dark_body"], CLOUD["dark_rim"], rim_dy=1)
cloud(c, 22, 68, [(-16, 15, 4), (2, 18, 5), (20, 12, 3)],
      CLOUD["low_body"], "#e8845a", rim_dy=1)
cloud(c, 120, 74, [(-10, 12, 2), (6, 12, 3)],
      CLOUD["dark_body"], "#f08a4b", rim_dy=1)

# --- birds -----------------------------------------------------------------
bird(c, 34, 36, "#241442", 2)
bird(c, 45, 30, "#241442", 1)
bird(c, 52, 41, "#2b1a44", 1)
bird(c, 26, 44, "#2b1a44", 1)

# --- sea -------------------------------------------------------------------
for y in range(HORIZON, 112):
    t = (y - HORIZON) / float(112 - HORIZON)
    for x in range(W):
        c.set(x, y, ramp(SEA, t, x, y))

# distant headland on the right horizon
c.poly([(98, 88), (106, 84), (113, 83), (121, 85), (127, 88)], "#3d2148")
c.line(106, 84, 121, 85, "#54305a")

# --- sun reflection: shimmering column of horizontal dashes ----------------
for y in range(HORIZON, 108):
    depth = y - HORIZON
    if depth % 4 == 3:
        continue  # gap row lets the sea show through
    w = max(1, int(10 - depth * 0.5) + (1 if depth % 2 == 0 else 0))
    j = ((y * 13) % 7) - 3
    if depth < 3:
        col = "#fff0b8"
    elif depth < 7:
        col = "#ffe39b"
    elif depth < 12:
        col = "#ffb457"
    elif depth < 16:
        col = "#e07a55"
    else:
        col = "#c66a58"
    c.line(SCX - w + j, y, SCX + w + j, y, col)
    # stray glints beside the column
    if depth % 3 == 1:
        c.line(SCX - w + j - 4, y, SCX - w + j - 3, y, "#e07a55")
        c.line(SCX + w + j + 3, y, SCX + w + j + 4, y, "#e07a55")

# wave-crest dashes give the sea its structure
WAVES = [
    ((2, 89, 5), "#9a5468"), ((20, 89, 6), "#9a5468"), ((44, 89, 5), "#9a5468"),
    ((10, 90, 6), "#9a5468"), ((30, 91, 5), "#9a5468"), ((104, 90, 7), "#9a5468"),
    ((118, 91, 5), "#9a5468"), ((52, 90, 4), "#9a5468"),
    ((6, 94, 5), "#7c4165"), ((40, 94, 6), "#7c4165"), ((106, 94, 6), "#7c4165"),
    ((64, 95, 4), "#7c4165"), ((120, 95, 4), "#7c4165"), ((22, 93, 4), "#7c4165"),
    ((14, 98, 4), "#613260"), ((48, 98, 5), "#613260"), ((102, 98, 6), "#613260"),
    ((118, 99, 4), "#613260"), ((2, 97, 4), "#613260"),
    ((8, 102, 5), "#4b2657"), ((36, 102, 4), "#4b2657"), ((104, 102, 5), "#4b2657"),
    ((66, 103, 4), "#4b2657"), ((24, 101, 4), "#4b2657"),
    ((20, 106, 4), "#3a1d4c"), ((58, 106, 5), "#3a1d4c"), ((96, 106, 4), "#3a1d4c"),
]
for (x, y, ln), col in WAVES:
    c.line(x, y, x + ln - 1, y, col)

# --- cliff -----------------------------------------------------------------
CLIFF = [(0, 72), (10, 74), (24, 76), (40, 78), (52, 80), (58, 82),
         (62, 88), (64, 96), (62, 104), (56, 112), (48, 120), (40, 127),
         (0, 127)]
c.poly(CLIFF, ROCK["back"])
# shadowed left face
c.poly([(0, 72), (10, 74), (24, 76), (26, 127), (0, 127)], ROCK["mid"])
# lit top edge
for (x0, y0, x1, y1) in [(0, 72, 10, 74), (10, 74, 24, 76), (24, 76, 40, 78)]:
    c.line(x0, y0, x1, y1, ROCK["warm"])
    c.line(x0, y0 + 1, x1, y1 + 1, ROCK["rim"])
for (x0, y0, x1, y1) in [(40, 78, 52, 80), (52, 80, 58, 82)]:
    c.line(x0, y0, x1, y1, ROCK["hot"])
    c.line(x0, y0 + 1, x1, y1 + 1, ROCK["warm"])
c.line(58, 82, 62, 88, ROCK["hot"])
c.line(62, 88, 64, 96, ROCK["warm"])
c.line(63, 89, 65, 96, ROCK["rim"])
# rock texture
for (x0, y0, x1, y1) in [(4, 84, 18, 88), (8, 96, 26, 100), (2, 108, 20, 112),
                         (30, 88, 46, 92), (34, 100, 52, 106), (28, 116, 44, 122),
                         (46, 84, 56, 88), (50, 96, 60, 102)]:
    c.line(x0, y0, x1, y1, ROCK["lite"])
for (x0, y0, x1, y1) in [(14, 78, 12, 92), (32, 80, 30, 96), (48, 82, 50, 98),
                         (22, 90, 20, 106), (40, 94, 42, 110)]:
    c.line(x0, y0, x1, y1, ROCK["mid"])

# --- castle ----------------------------------------------------------------
# keep (behind)
c.poly([(24, 53), (32, 40), (40, 53)], CASTLE["roof"])
c.poly([(32, 40), (40, 53), (32, 53)], CASTLE["rooflite"])
c.line(32, 40, 40, 53, CASTLE["rim"])
c.rect(26, 52, 12, 22, CASTLE["shadow"])
c.rect(32, 52, 6, 22, CASTLE["body"])
c.line(37, 52, 37, 73, CASTLE["rim"])
c.rect(29, 58, 2, 3, WIN[1])
c.rect(34, 58, 2, 3, WIN[0])

# curtain wall
c.rect(18, 70, 26, 14, CASTLE["shadow"])
c.rect(30, 70, 14, 14, CASTLE["body"])
merlons(c, [18, 23, 28, 33, 38, 42], 67, 3, 3, CASTLE["body"])
c.rect(18, 67, 3, 3, CASTLE["shadow"])
c.rect(23, 67, 3, 3, CASTLE["shadow"])
c.line(18, 70, 43, 70, CASTLE["lite"])

# gate
c.rect(29, 76, 6, 8, "#120c1e")
c.path("M29 84 V79 A3 3 0 0 1 35 79 V84 Z", "#0d0817")
c.rect(31, 79, 2, 5, WIN[1])

# left tower
c.rect(6, 44, 13, 40, CASTLE["shadow"])
c.rect(13, 44, 6, 40, CASTLE["body"])
merlons(c, [6, 11, 16], 41, 3, 3, CASTLE["body"])
c.rect(6, 41, 3, 3, CASTLE["shadow"])
c.line(18, 41, 18, 83, CASTLE["rim"])
c.line(6, 44, 18, 44, CASTLE["lite"])
c.rect(9, 52, 2, 3, WIN[1])
c.rect(14, 52, 2, 3, WIN[0])
c.rect(9, 63, 2, 3, WIN[1])
c.rect(14, 63, 2, 3, WIN[0])

# right tower (tallest)
c.rect(44, 32, 15, 52, CASTLE["shadow"])
c.rect(51, 32, 8, 52, CASTLE["body"])
merlons(c, [44, 49, 54], 29, 3, 3, CASTLE["body"])
c.rect(44, 29, 3, 3, CASTLE["shadow"])
c.line(58, 29, 58, 83, CASTLE["hot"])
c.line(44, 32, 58, 32, CASTLE["lite"])
c.rect(47, 40, 2, 3, WIN[1])
c.rect(53, 40, 2, 3, WIN[0])
c.rect(47, 52, 2, 3, WIN[1])
c.rect(53, 52, 2, 3, WIN[0])
c.rect(47, 64, 2, 3, WIN[1])
c.rect(53, 64, 2, 3, WIN[0])

# flags
c.line(12, 26, 12, 44, "#1a1229")
c.poly([(13, 27), (25, 30), (13, 34)], FLAG[0])
c.poly([(13, 27), (25, 30), (13, 30)], FLAG[1])
c.line(51, 12, 51, 32, "#1a1229")
c.poly([(52, 13), (66, 17), (52, 22)], FLAG[2])
c.poly([(52, 13), (66, 17), (52, 17)], "#b87a35")

# --- right sea stack -------------------------------------------------------
c.poly([(98, 127), (102, 112), (108, 102), (114, 97), (120, 99), (126, 106),
        (127, 112), (127, 127)], ROCK["mid"])
c.line(108, 102, 114, 97, ROCK["warm"])
c.line(114, 97, 120, 99, ROCK["hot"])
c.line(107, 103, 113, 98, ROCK["rim"])
c.line(102, 112, 108, 103, ROCK["rim"])
c.line(110, 104, 107, 118, ROCK["front"])
c.line(117, 101, 119, 114, ROCK["front"])
c.line(122, 104, 124, 116, ROCK["lite"])

# small rock in the water
c.poly([(66, 108), (70, 102), (74, 100), (78, 103), (81, 108)], ROCK["mid"])
c.line(70, 102, 74, 100, ROCK["warm"])
for x in (64, 67, 71, 76, 80, 83):
    c.set(x, 108, "#7c4e66")
    c.set(x + 2, 109, "#5c4068")

# --- foam at cliff base ----------------------------------------------------
for (x, y) in ((58, 100), (61, 103), (56, 106), (63, 98), (60, 108), (52, 112),
               (57, 111), (48, 118), (44, 122)):
    c.set(x, y, "#7c4e66")
    c.set(x + 1, y + 1, "#5c4068")

# --- foreground rock layers ------------------------------------------------
MID = [(0, 106), (10, 102), (20, 105), (30, 100), (42, 104), (52, 101),
       (62, 105), (74, 102), (86, 105), (98, 101), (110, 104), (120, 100),
       (127, 103), (127, 127), (0, 127)]
c.poly(MID, ROCK["mid"])
for i in range(len(MID) - 3):
    (x0, y0), (x1, y1) = MID[i], MID[i + 1]
    lit = (x0 + x1) / 2.0 > 60
    if y1 <= y0:
        c.line(x0, y0, x1, y1, ROCK["rim"] if lit else ROCK["lite"])
    else:
        c.line(x0, y0, x1, y1, ROCK["lite"] if lit else ROCK["mid"])

FRONT = [(0, 114), (7, 109), (14, 112), (21, 107), (29, 111), (36, 115),
         (44, 111), (53, 114), (61, 112), (70, 116), (78, 112), (86, 114),
         (94, 110), (103, 113), (112, 109), (120, 112), (127, 108),
         (127, 127), (0, 127)]
c.poly(FRONT, ROCK["front"])
for i in range(len(FRONT) - 3):
    (x0, y0), (x1, y1) = FRONT[i], FRONT[i + 1]
    c.line(x0, y0, x1, y1, ROCK["mid"])

# rock facets / cracks in the foreground
for (x0, y0, x1, y1) in [(6, 116, 18, 122), (30, 118, 44, 124), (60, 120, 76, 126),
                         (92, 116, 106, 122), (112, 118, 124, 124), (40, 112, 50, 116),
                         (78, 116, 88, 120)]:
    c.line(x0, y0, x1, y1, "#100a1c")
for (x, y) in ((12, 112), (26, 116), (48, 118), (68, 120), (88, 116),
               (104, 118), (120, 114), (36, 122), (76, 124), (100, 124)):
    c.set(x, y, ROCK["lite"])
    c.set(x + 1, y + 1, ROCK["mid"])

# scrub tufts on the foreground silhouette
for (x, y) in ((4, 113), (17, 111), (33, 114), (57, 111), (83, 113),
               (97, 109), (117, 111), (126, 107)):
    c.set(x, y - 1, ROCK["front"])
    c.set(x + 1, y - 2, ROCK["front"])
    c.set(x - 1, y - 2, ROCK["front"])

print(c.stats_text())
view(c)
save("castle_title_screen", c)
finish(c)
