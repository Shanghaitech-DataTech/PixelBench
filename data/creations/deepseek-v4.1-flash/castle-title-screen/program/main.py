import math, random

rng = random.Random(7)

W = H = 128
HZ = 78  # sea horizon
c = new_canvas(W, H, name="output")


def sh(pts, dx=0, dy=0):
    return [(x + dx, y + dy) for x, y in pts]


def seg_i(stops, t):
    for i in range(len(stops) - 1):
        if t <= stops[i + 1][0] or i == len(stops) - 2:
            return i
    return len(stops) - 2


def vgrad(stops, y0, y1, x0=0, x1=W):
    for y in range(y0, y1):
        t = (y - y0) / max(1, (y1 - y0 - 1))
        i = seg_i(stops, t)
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        f = (t - t0) / max(1e-6, (t1 - t0))
        f = max(0.0, min(1.0, f))
        if f < 0.33:
            c.rect(x0, y, x1 - x0, 1, c0)
        elif f > 0.67:
            c.rect(x0, y, x1 - x0, 1, c1)
        else:
            for x in range(x0, x1):
                c.set(x, y, c0 if (x + y) % 2 == 0 else c1)


# ---------------- 1. SKY ----------------
SKY_STOPS = [
    (0.00, "#0d0726"), (0.08, "#160d38"), (0.16, "#221246"), (0.24, "#301857"),
    (0.32, "#431d5c"), (0.40, "#5a2359"), (0.48, "#722a56"), (0.56, "#8c3451"),
    (0.64, "#a5424a"), (0.71, "#bd5242"), (0.78, "#d1663e"), (0.86, "#e48343"),
    (0.94, "#f0a04e"), (1.00, "#f7b45c"),
]
vgrad(SKY_STOPS, 0, HZ)

# ---------------- 2. SUN ----------------
SX, SY, SR = 90, 62, 30
SUN = ["#fa9440", "#fdb055", "#ffcd7d", "#ffedb8"]
for y in range(max(0, SY - SR - 5), min(H, SY + SR + 6)):
    for x in range(max(0, SX - SR - 5), min(W, SX + SR + 6)):
        d = math.hypot(x - SX, y - SY)
        if d <= 7:
            c.set(x, y, SUN[3])
        elif d <= 14:
            c.set(x, y, SUN[3] if (d > 12.8 and (x + y) % 2 == 0) else SUN[2])
        elif d <= 21:
            c.set(x, y, SUN[2] if (d > 19.8 and (x + y) % 2 == 0) else SUN[1])
        elif d <= SR:
            c.set(x, y, SUN[1] if (d > SR - 2 and (x + y) % 2 == 0) else SUN[0])
        elif d <= SR + 2.5:
            if (x + y) % 2 == 0:
                c.set(x, y, SUN[0])

# ---------------- 3. CLOUDS ----------------
def cloud(parts, body, lit, dy=1):
    for cx, cy, rx, ry in parts:
        c.ellipse(cx, cy + dy, rx, ry, lit)
    for cx, cy, rx, ry in parts:
        c.ellipse(cx, cy, rx, ry, body)


cloud([(20, 32, 17, 2), (40, 30, 15, 2), (58, 33, 11, 2)], "#2c1240", "#c9603c")
cloud([(66, 45, 16, 3), (88, 42, 20, 3), (110, 45, 12, 2)], "#36174a", "#e8734a")
cloud([(104, 58, 11, 2), (118, 56, 7, 2)], "#3f1c4c", "#f5904e")
cloud([(74, 71, 19, 3), (98, 69, 15, 2), (116, 72, 11, 2), (56, 73, 9, 2)],
      "#4a2150", "#ffbe6e")

# ---------------- 4. BIRDS ----------------
BIRD = "#3a1636"
for bx, by in [(70, 58), (82, 52), (94, 54)]:
    c.set(bx, by, BIRD)
    c.set(bx + 1, by + 1, BIRD)
    c.set(bx + 2, by, BIRD)

# ---------------- 5. SEA ----------------
SEA_STOPS = [
    (0.00, "#d4704a"), (0.10, "#b8583f"), (0.22, "#984740"), (0.36, "#7a3a44"),
    (0.52, "#5c2e44"), (0.68, "#42233c"), (0.84, "#2c1830"), (1.00, "#1a1222"),
]
vgrad(SEA_STOPS, HZ, H)

# wave dashes
for wy, wcol in [(82, "#e08550"), (86, "#d1764c"), (92, "#b0603f"),
                 (99, "#8a4a42"), (107, "#6a3a44"), (116, "#4a2a3a")]:
    x = rng.randint(0, 5)
    while x < W:
        ln = rng.randint(2, 6)
        c.rect(x, wy, min(ln, W - x), 1, wcol)
        x += ln + rng.randint(3, 9)

# sun reflection
for y in range(HZ + 1, 124):
    t = (y - HZ - 1) / 45.0
    if t < 0.18:
        rc = ["#ffedb8", "#ffcd7d"]
    elif t < 0.40:
        rc = ["#ffcd7d", "#f09a4e"]
    elif t < 0.65:
        rc = ["#f09a4e", "#d4704a"]
    else:
        rc = ["#b8583f", "#984740"]
    half = 2 + int(t * 13)
    for k in range(-2, 3):
        if rng.random() < 0.85 - t * 0.4:
            cx = 90 + int(k * half / 2.4) + rng.randint(-1, 1)
            ln = max(1, int(3 - t * 2 + rng.randint(0, 1)))
            col = rc[0] if abs(k) < 2 else rc[1]
            for x in range(cx, cx + ln):
                if abs(x - 90) <= half + 1:
                    c.set(x, y, col)

# ---------------- 6. CLIFF ----------------
CLIFF = [(-1, 66), (3, 63), (9, 64), (15, 61), (21, 63), (27, 61), (33, 63),
         (39, 61), (44, 63), (48, 68), (52, 74), (55, 82), (57, 91), (57, 102),
         (55, 112), (53, 121), (51, 129), (-1, 129)]
c.poly(CLIFF, "#8a5648")
c.poly(sh(CLIFF, -2), "#4e3742")
c.poly(sh(CLIFF, -5), "#362840")
c.poly(sh(CLIFF, -11), "#241a2c")

# rock texture
for (x0, y0, x1, y1) in [(20, 78, 26, 88), (34, 84, 40, 96), (12, 94, 18, 106),
                         (28, 102, 33, 114), (44, 80, 47, 90), (8, 114, 14, 124),
                         (38, 110, 44, 120)]:
    c.line(x0, y0, x1, y1, "#241a2c")
for (x0, y0, x1, y1) in [(46, 76, 46, 86), (50, 90, 50, 102), (22, 74, 22, 80),
                         (30, 90, 30, 98)]:
    c.line(x0, y0, x1, y1, "#4e3742")

FACETS = [
    [(0, 86), (9, 82), (17, 88), (11, 97)],
    [(18, 92), (28, 86), (36, 94), (30, 104), (20, 102)],
    [(0, 104), (10, 100), (18, 108), (12, 118)],
    [(22, 110), (34, 106), (42, 114), (36, 124), (24, 122)],
    [(-1, 70), (6, 68), (12, 74), (4, 80)],
]
for f in FACETS:
    c.poly(f, "#362840")
    for i in range(len(f) - 1):
        c.line(f[i][0], f[i][1], f[i + 1][0], f[i + 1][1], "#4e3742")

# ---------------- 7. CASTLE ----------------
ST_D = "#1e1730"
ST = "#2a2140"
ST_L = "#3d3152"
ROOF = "#5e2640"
ROOF_L = "#b2544c"
RIMC = "#a85e50"
WIN = "#ffd98a"
WIN2 = "#e0a05e"
FLAG = "#c33a4d"
FLAG_L = "#e8606c"

# curtain wall + merlons
c.rect(8, 52, 34, 16, ST)
for mx in range(8, 42, 5):
    c.rect(mx, 48, 3, 5, ST)
    c.rect(mx, 48, 3, 1, ST_L)
# gate
c.rect(21, 55, 7, 13, "#4a3448")
c.circle(24, 56, 3, "#4a3448")
c.rect(23, 58, 4, 5, WIN2)

# left tower
c.rect(4, 36, 17, 34, ST)
c.rect(3, 58, 19, 12, ST)
c.rect(4, 36, 3, 34, ST_D)
c.rect(18, 36, 2, 34, ST_L)
c.rect(20, 36, 1, 34, RIMC)
c.poly([(2, 36), (12, 24), (23, 36)], ROOF)
c.poly([(12, 24), (23, 36), (19, 36), (12, 29)], ROOF_L)
c.rect(12, 16, 1, 8, ST_L)
c.poly([(13, 17), (21, 20), (13, 23)], FLAG)
c.line(14, 22, 20, 20, FLAG_L)
c.rect(8, 42, 2, 3, WIN)
c.rect(14, 44, 2, 3, WIN2)
c.rect(8, 50, 2, 3, WIN2)

# right tower
c.rect(27, 42, 17, 28, ST)
c.rect(26, 60, 19, 10, ST)
c.rect(27, 42, 3, 28, ST_D)
c.rect(41, 42, 2, 28, ST_L)
c.rect(43, 42, 1, 28, RIMC)
c.poly([(25, 42), (35, 29), (45, 42)], ROOF)
c.poly([(35, 29), (45, 42), (41, 42), (35, 34)], ROOF_L)
c.rect(35, 21, 1, 8, ST_L)
c.poly([(36, 22), (43, 25), (36, 28)], FLAG)
c.line(37, 27, 42, 25, FLAG_L)
c.rect(31, 48, 2, 3, WIN)
c.rect(38, 48, 2, 3, WIN2)
c.rect(31, 54, 2, 3, WIN2)

# ---------------- 7b. ROCK LEDGE in front of castle ----------------
LEDGE_TOP = [(-1, 70), (8, 66), (16, 70), (26, 67), (36, 71), (44, 67), (49, 72)]
LEDGE_BOT = [(49, 85), (40, 79), (33, 86), (24, 80), (15, 87), (6, 82), (-1, 86)]
LEDGE = LEDGE_TOP + LEDGE_BOT
c.poly(LEDGE, "#362840")
for i in range(len(LEDGE_TOP) - 1):
    c.line(LEDGE_TOP[i][0], LEDGE_TOP[i][1], LEDGE_TOP[i + 1][0], LEDGE_TOP[i + 1][1], "#4e3742")

# distant island on the right horizon
c.poly([(111, 78), (114, 76), (117, 77), (120, 74), (123, 76), (126, 75), (128, 77), (128, 78)], "#4a2a30")

# ---------------- 8. FOREGROUND ROCKS ----------------
FG_L = [(-1, 108), (7, 112), (15, 118), (22, 124), (26, 129), (-1, 129)]
FG_R = [(129, 94), (121, 100), (114, 108), (107, 117), (102, 124), (100, 129), (129, 129)]
FG_C = [(42, 129), (50, 124), (58, 120), (67, 122), (74, 127), (77, 129)]
for fg in (FG_L, FG_R, FG_C):
    c.poly(fg, "#4a2c30")
    c.poly(sh(fg, 0, 2), "#170f1e")
    c.poly(sh(fg, 0, 5), "#0d0812")

# ---------------- 9. TITLE ----------------
tw, th = 42, 9
t = new_canvas(tw, th, name="titlelayer")
t.text(1, 1, "ELDORIA", "#160a22")
t.text(0, 0, "ELDORIA", "#ffd98e")
gold = t.color("#ffd98e")
for y in range(5, th):
    for x in range(tw):
        if t.get(x, y) == gold:
            t.set(x, y, "#f2b263")
sel = t.select(0, 0, tw, th).resize(tw * 2, th * 2)
c.blit(sel.preview("titlescaled"), 22, 2)

print(c.stats_text())
view(c)
save("castle_title", c)
finish(c)
