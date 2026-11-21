import random

W = H = 128
c = new_canvas(W, H, background="#0b0b16", name="cyberpunk-alley")
rnd = random.Random(20261107)

# ---------------- consolidated palette (60 colours) ----------------
SKY, HAZE, HAZE2 = "#0b0b16", "#141126", "#191430"
DARK = "#080711"
WIN1, WIN2, WIN3, WIN4, WIN5 = "#1b2938", "#31203a", "#2c2410", "#11283a", "#241a30"
GLOW1, GLOW2, GLOW3 = "#1e3244", "#2a4560", "#3a5f80"
RED = "#ff3b3b"
WALL, LINE, FRAME, WARM, COOL = "#161226", "#1b1630", "#221b3a", "#5a4420", "#1d3d4d"
PINKBG, PINK, PINKT = "#3a1030", "#ff2d95", "#ffb8dc"
CYANBG, CYAN, CYANT = "#0f4a56", "#29f3ff", "#dffbff"
VBODY, VINNER, VTOP, VGLASS = "#0a1e26", "#123844", "#e8fbff", "#bfeafc"
ITEMS = ["#ff4d4d", "#ffb03a", "#37e0ff", "#ff5fb0", "#7dff8a", "#ffe95c", "#5c9dff", "#c05cff"]
COOLD = "#0e3d4a"
ORGBG, ORG, ORGT = "#4a2c10", "#ff9f2e", "#ffc46a"
GROUND, GLINE, GLINE2 = "#0e0f18", "#1e2030", "#111220"
POOLP, POOLP2, POOLC, POOLC2 = "#1c0f1c", "#2a1428", "#0f242c", "#143540"
STRP, STRP2, STRC = "#4a1230", "#63184a", "#155264"
PEDG = "#262c40"
RIMC, RIMP = "#1d5f70", "#5a1838"
CANA, CANA2, CRIB, CRIB2 = "#a5c8da", "#dff0f8", "#9db4c4", "#5f8498"
RAIN1, RAIN2, RAIN3 = "#2c3a55", "#3d4f6e", "#5a6f96"

# ============================ SKY ============================
c.rect(0, 0, 128, 128, SKY)
c.rect(48, 16, 37, 24, HAZE)
c.rect(48, 34, 37, 8, HAZE2)

# ======================= FAR BUILDINGS =======================
c.rect(48, 30, 37, 66, DARK)
c.rect(52, 40, 30, 56, DARK)
for _ in range(40):
    x = rnd.randrange(50, 82)
    y = rnd.randrange(34, 92)
    if 52 <= x <= 74 and y >= 60:
        continue
    c.rect(x, y, rnd.choice([1, 1, 2]), 1,
           rnd.choice([WIN1, WIN2, WIN3, WIN4, WIN5]))

# glowing alley end (light behind the figure)
c.rect(53, 62, 18, 34, GLOW1)
c.rect(56, 66, 12, 30, GLOW2)
c.rect(59, 70, 6, 26, GLOW3)
c.rect(61, 74, 2, 22, GLOW2)

# rooftop antennas
c.line(66, 30, 66, 20, DARK)
c.set(66, 19, RED)
c.set(66, 18, RED)
c.line(58, 34, 58, 27, DARK)
c.set(58, 26, RED)

# ======================= LEFT BUILDING =======================
c.rect(0, 6, 48, 90, WALL)
c.rect(0, 6, 3, 90, DARK)
c.rect(45, 6, 3, 90, LINE)
for y in (24, 40, 58, 76):
    c.line(3, y, 44, y, LINE)
for x in (20, 27, 34, 41):
    c.rect(x, 9, 4, 1, FRAME)
    c.rect(x, 10, 4, 5, DARK)
    c.rect(x, 61, 4, 1, FRAME)
    c.rect(x, 62, 4, 5, DARK)
c.rect(28, 11, 2, 3, WARM)
c.rect(42, 11, 2, 3, COOL)
c.rect(35, 63, 2, 3, WARM)
c.rect(21, 63, 2, 3, COOL)
# AC unit + drainpipe
c.rect(30, 31, 8, 5, FRAME)
c.line(30, 33, 37, 33, COOL)
c.line(34, 36, 34, 38, COOL)
c.rect(6, 60, 2, 34, LINE)
c.line(6, 66, 7, 66, DARK)
c.line(6, 80, 7, 80, DARK)

# ---- vertical BAR sign (pink neon) ----
c.rect(0, 20, 19, 42, PINKBG)
c.rect(2, 22, 15, 38, DARK)
c.rect(2, 24, 13, 34, PINK, fill=False)
for i, ch in enumerate("BAR"):
    c.text(6, 29 + i * 9, ch, PINKT, font="5x7")

# ---- RAMEN sign (cyan neon) ----
c.rect(14, 37, 34, 17, CYANBG)
c.rect(16, 39, 30, 13, DARK)
c.rect(16, 39, 30, 13, CYAN, fill=False)
c.text(17, 42, "RAMEN", CYANT, font="5x7")

# ====================== RIGHT BUILDING =======================
c.rect(84, 2, 44, 94, WALL)
c.rect(84, 2, 2, 94, LINE)
c.rect(125, 2, 3, 94, DARK)
for y in (16, 30, 46, 62):
    c.line(86, y, 124, y, LINE)
for y in (8, 18, 28, 38, 48):
    for x in (88, 97, 106, 115):
        c.rect(x, y - 1, 4, 1, FRAME)
        c.rect(x, y, 4, 5, DARK)
for x, y, col in [(97, 18, WARM), (115, 8, COOL), (88, 38, RIMP),
                  (106, 28, WARM), (115, 48, COOL)]:
    c.rect(x + 1, y + 1, 2, 3, col)

# ---- cocktail neon sign ----
c.rect(84, 28, 14, 27, PINKBG)
c.rect(85, 29, 12, 25, DARK)
c.poly([(87, 34), (95, 34), (91, 41)], PINK, fill=False)
c.line(91, 41, 91, 47, PINK)
c.line(88, 48, 94, 48, PINK)
c.set(92, 35, PINKT)
c.set(89, 36, PINKT)

# ---- vending machine ----
c.rect(92, 56, 32, 44, VBODY)
c.rect(94, 58, 28, 40, VINNER)
c.rect(96, 62, 2, 34, VINNER)
c.rect(97, 95, 22, 2, DARK)
c.rect(98, 62, 20, 34, DARK)
c.rect(98, 62, 20, 34, DARK, fill=False)
c.rect(99, 63, 18, 2, VTOP)
c.rect(100, 66, 16, 20, VGLASS)
k = 0
for ry in (68, 73, 78):
    for rx in (101, 105, 109, 113):
        c.rect(rx, ry, 2, 2, ITEMS[k % 8])
        k += 1
    c.line(100, ry + 3, 115, ry + 3, VTOP)
c.rect(100, 87, 16, 6, DARK)
c.rect(103, 89, 8, 2, VINNER)
c.set(114, 88, ITEMS[0])
c.rect(100, 93, 16, 1, VINNER)

# =================== CABLES + HANGING SIGN ===================
c.path("M 0 2 Q 24 10 47 6", DARK, fill=False)
c.path("M 47 6 Q 66 14 85 4", DARK, fill=False)
c.path("M 85 4 Q 106 12 127 4", DARK, fill=False)
c.path("M 47 12 Q 66 21 85 10", DARK, fill=False)
c.path("M 47 18 Q 66 28 85 16", DARK, fill=False)
c.rect(51, 24, 31, 15, ORGBG)
c.line(56, 21, 56, 26, FRAME)
c.line(74, 21, 74, 26, FRAME)
c.rect(53, 26, 25, 11, DARK)
c.rect(53, 26, 25, 11, ORG, fill=False)
c.text(57, 29, "24H", ORGT, font="5x7")

# ========================== GROUND ===========================
c.rect(0, 92, 48, 4, WALL)
c.rect(84, 92, 44, 4, WALL)
c.rect(0, 96, 128, 32, GROUND)
c.rect(0, 96, 128, 1, GLINE)
c.line(0, 101, 127, 101, GLINE2)
c.line(0, 109, 127, 109, GLINE2)
c.line(0, 119, 127, 119, GLINE2)
# light pools
c.rect(14, 96, 36, 7, POOLP)
c.rect(18, 96, 26, 4, POOLP2)
c.rect(94, 96, 30, 9, POOLC)
c.rect(98, 96, 22, 5, POOLC2)
c.rect(52, 96, 20, 11, GLINE2)


def streak(x, y0, y1, col):
    y = y0
    y1 = min(y1, 127)
    while y < y1:
        seg = min(rnd.choice([2, 3, 4]), y1 - y)
        c.rect(x, y, 1, seg, col)
        y += seg + rnd.choice([1, 2, 2, 3])


for x in (6, 10):
    streak(x, 97, 112 + x, STRP)
for x in (20, 26, 33, 40, 45):
    streak(x, 97, 108 + x // 2, rnd.choice([STRP, STRP2, STRP]))
for x in (99, 104, 110, 115):
    streak(x, 97, 118 + (x - 99), rnd.choice([COOLD, STRC]))
for x in (57, 62, 67):
    streak(x, 97, 116, GLINE2)
for x in (60, 68):
    streak(x, 97, 106, ORGBG)

# puddles
c.ellipse(30, 114, 20, 6, GLINE)
c.ellipse(30, 114, 20, 6, PEDG, fill=False)
c.rect(24, 110, 3, 8, STRP)
c.rect(28, 112, 2, 5, STRP2)
c.rect(34, 111, 3, 7, COOLD)
c.ellipse(104, 120, 18, 5, GLINE)
c.ellipse(104, 120, 18, 5, PEDG, fill=False)
c.rect(98, 117, 3, 6, COOLD)
c.rect(104, 118, 4, 5, STRC)
c.rect(111, 117, 2, 6, COOLD)
c.ellipse(78, 108, 9, 3, GLINE)
c.ellipse(78, 108, 9, 3, PEDG, fill=False)
c.rect(75, 106, 3, 4, ORGBG)

# =================== FIGURE + UMBRELLA =======================


def person(col, dx=0, dy=0):
    c.circle(60 + dx, 64 + dy, 3, col)
    c.rect(58 + dx, 66 + dy, 4, 3, col)
    c.rect(54 + dx, 68 + dy, 12, 9, col)
    c.rect(55 + dx, 76 + dy, 10, 9, col)
    c.rect(55 + dx, 84 + dy, 4, 17, col)
    c.rect(60 + dx, 84 + dy, 4, 17, col)
    c.rect(54 + dx, 100 + dy, 6, 3, col)
    c.rect(60 + dx, 100 + dy, 6, 3, col)
    c.line(63 + dx, 71 + dy, 66 + dx, 69 + dy, col)
    c.rect(65 + dx, 68 + dy, 3, 3, col)


person(RIMC, dx=1)     # cyan rim light (vending machine side)
person(RIMP, dx=-1)    # pink rim light (sign side)
person(DARK)

# reflection in the wet ground
c.rect(48, 103, 28, 2, GLINE)
c.rect(52, 105, 20, 1, GLINE2)
c.rect(56, 105, 9, 9, DARK)
c.line(54, 108, 68, 108, GLINE)
c.line(53, 112, 69, 112, GLINE)

# transparent canopy: 2px ring, interior left open
cx, cy, rx, ry, t = 62, 52, 18, 10, 2
d = (f"M {cx-rx} {cy} A {rx} {ry} 0 1 0 {cx+rx} {cy} A {rx} {ry} 0 1 0 {cx-rx} {cy} Z "
     f"M {cx-rx+t} {cy} A {rx-t} {ry-t} 0 1 0 {cx+rx-t} {cy} A {rx-t} {ry-t} 0 1 0 {cx-rx+t} {cy} Z")
c.path(d, CANA, fill=True)
c.path("M 50 46 Q 62 40 74 46", CANA2, fill=False)     # top sheen
c.path("M 48 56 Q 62 63 76 56", CRIB2, fill=False)     # inner underside
for ex, ey in [(44, 52), (53, 59), (62, 61), (71, 59), (80, 52)]:
    c.line(62, 43, ex, ey, CRIB2)                       # ribs
c.line(52, 47, 55, 45, CANA2)
c.line(56, 50, 59, 48, CANA2)
c.rect(61, 38, 2, 5, CRIB)
c.set(62, 37, CANA2)
for dx_, dy_ in [(46, 55), (54, 60), (70, 60), (78, 55)]:
    c.set(dx_, dy_, CRIB)
c.line(78, 56, 78, 59, CRIB)
c.line(62, 44, 66, 69, CRIB)                            # shaft
c.rect(65, 68, 3, 3, DARK)                              # hand over shaft

# ---- doorway with warm light (left building) ----
c.rect(8, 74, 12, 18, FRAME)
c.rect(9, 75, 10, 17, ORGBG)
c.rect(10, 76, 8, 15, "#6b4a2a")
c.rect(12, 78, 4, 11, "#8a6a3a")
c.rect(6, 96, 18, 5, "#1c140c")
c.rect(8, 96, 14, 3, ORGBG)

# ---- crates against the right wall ----
c.rect(84, 90, 8, 6, "#241c10")
c.rect(84, 90, 8, 6, "#3a2e1a", fill=False)
c.line(84, 93, 91, 93, "#3a2e1a")
c.rect(86, 84, 6, 6, "#241c10")
c.rect(86, 84, 6, 6, "#3a2e1a", fill=False)
c.line(86, 87, 91, 87, "#3a2e1a")

# ---- wall vent + steam ----
c.rect(24, 89, 8, 4, FRAME)
c.line(25, 90, 30, 90, DARK)
c.line(25, 92, 30, 92, DARK)
for sx, sy, sl in [(27, 86, 3), (25, 82, 4), (28, 78, 3), (25, 74, 4), (27, 70, 3)]:
    c.line(sx, sy, sx + sl, sy, RAIN1)
    c.set(sx + 1, sy - 1, RAIN2)

# ---- vertical CJK sign ----
c.rect(71, 46, 13, 17, DARK)
c.rect(71, 46, 13, 17, "#3a5a3a", fill=False)
c.text(72, 48, "酒", "#7dff8a", font="12px")

# =========================== RAIN ============================
for _ in range(100):
    x = rnd.randrange(-2, 126)
    y = rnd.randrange(-6, 120)
    ln = rnd.choice([3, 4, 5, 6, 7])
    r = rnd.random()
    col = RAIN1 if r < 0.62 else (RAIN2 if r < 0.85 else RAIN3)
    c.line(x, y, x + 1, y + ln, col)
for _ in range(12):
    x = rnd.randrange(-4, 124)
    y = rnd.randrange(-6, 114)
    c.line(x, y, x + 2, y + rnd.randrange(8, 12), RAIN3)
for _ in range(26):
    x = rnd.randrange(2, 126)
    y = rnd.randrange(97, 126)
    c.set(x, y, RAIN2)
    if rnd.random() < 0.4:
        c.line(x - 1, y, x + 1, y, RAIN1)
# rain ticking on the canopy
c.line(56, 45, 58, 44, CANA2)
c.line(68, 47, 70, 46, CANA2)

print(c.stats_text())
print(c.stats_text())
finish(c)
