import math

W = H = 256
c = new_canvas(W, H, background="#0a0a13", name="arcane-instrument")

CX, CY = 128.0, 108.0
OUT = "#07070d"

# ---- palette ----
BG      = "#0a0a13"
WALL    = "#0e0e18"
WALL_S  = "#10101b"
PIL     = "#141422"
PIL_L   = "#1c1c2e"
FLOOR   = "#0c0c15"

ST_TOP1 = "#90909c"; ST_FR1 = "#565662"
ST_TOP2 = "#868692"; ST_FR2 = "#4c4c57"
ST_TOP3 = "#7e7e8a"; ST_FR3 = "#44444f"
ST_TOP4 = "#6e6e7a"; ST_FR4 = "#3c3c46"
ST_LINE = "#33333d"

BRASS_L = "#f4d98c"
BRASS   = "#c99a3f"
BRASS_D = "#8a6224"
BRASS_DD= "#4a330e"

GOLD_L  = "#ffe9a8"
GOLD    = "#ffd25e"
ORANGE  = "#ff9d2e"

CORE_W  = "#fffbe8"
CORE_Y  = "#ffe27a"

TEAL_L  = "#aef7ea"
TEAL    = "#46d8c8"
TEAL_D  = "#14655e"
TEAL_G  = "#0e3a37"

BLUE_L  = "#d6ecff"; BLUE = "#6fb4ff"; BLUE_D = "#1e4e8e"; BLUE_G = "#122c4e"
MAG_L   = "#ffd6f2"; MAG  = "#f08ad0"; MAG_D  = "#7c2a68"; MAG_G  = "#43173a"
VIO_L   = "#e2d2ff"; VIO  = "#a678ff"; VIO_D  = "#4a2a8e"; VIO_G  = "#241244"

GLOW1 = "#3a2a10"
GLOW2 = "#221808"
HAZE  = "#151009"

# ---- helpers ----
def P(x, y, col):
    xi, yi = int(round(x)), int(round(y))
    if 0 <= xi < W and 0 <= yi < H:
        c.set(xi, yi, col)

def disc(cx, cy, r, col):
    c.circle(int(round(cx)), int(round(cy)), int(round(r)), col, fill=True)

def ring(cx, cy, rx, ry, col, t=1):
    for i in range(t):
        c.ellipse(int(round(cx)), int(round(cy)), int(round(rx)) - i,
                  int(round(ry)) - i, col, fill=False)

def arc(cx, cy, r, a0, a1, col, ry=None):
    ry = r if ry is None else ry
    n = max(10, int(abs(a1 - a0) * max(r, ry) / 2))
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        P(cx + r * math.cos(a), cy + ry * math.sin(a), col)

def annulus_dither(cx, cy, r0, r1, col, phase=0):
    for y in range(int(cy - r1) - 1, int(cy + r1) + 2):
        for x in range(int(cx - r1) - 1, int(cx + r1) + 2):
            d = math.hypot(x - cx, y - cy)
            if r0 <= d < r1 and (x + y + phase) % 2 == 0:
                P(x, y, col)

def ray(cx, cy, deg, r0, r1, col, step=1):
    a = math.radians(deg)
    r = float(r0)
    while r <= r1:
        if step <= 1 or int(r) % step == 0:
            P(cx + r * math.cos(a), cy + r * math.sin(a), col)
        r += 1

RUNES = [
    [(1,0),(0,1),(2,1),(1,2),(1,3),(0,4),(2,4)],
    [(0,0),(2,0),(1,1),(0,2),(2,2),(0,3),(2,3),(1,4)],
    [(1,0),(1,1),(0,2),(1,2),(2,2),(0,3),(2,4)],
    [(0,0),(0,1),(1,1),(2,1),(2,2),(1,3),(0,4),(2,4)],
    [(2,0),(1,1),(0,2),(1,2),(1,3),(0,4),(2,4)],
    [(1,0),(0,1),(1,1),(2,1),(1,2),(1,3),(1,4)],
]

def rune(x, y, col, i=0):
    for dx, dy in RUNES[i % len(RUNES)]:
        P(x + dx - 1, y + dy - 2, col)

def ring_runes(r, step, col, ry=None, start=0):
    ry = r if ry is None else ry
    k = 0
    a = start
    while a < 360:
        rad = math.radians(a)
        rune(CX + r * math.cos(rad), CY + ry * math.sin(rad), col, k)
        k += 1
        a += step

def orb(x, y, r, base, light, dark, glow=None):
    if glow:
        annulus_dither(x, y, r + 1, r + 3, glow)
    disc(x, y, r, base)
    for yy in range(-r, r + 1):
        for xx in range(-r, r + 1):
            if xx * xx + yy * yy <= r * r and (xx + yy) >= r + 1:
                P(x + xx, y + yy, dark)
    P(x - r // 2 - 1, y - r // 2 - 1, light)
    P(x - r // 2, y - r // 2 - 1, light)
    P(x - r // 2, y - r // 2, light)
    c.circle(int(round(x)), int(round(y)), int(r), OUT, fill=False)

def gear(cx, cy, r, teeth, col, dark, hub=3):
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        x1 = cx + (r + 1) * math.cos(a)
        y1 = cy + (r + 1) * math.sin(a)
        P(x1, y1, col)
        P(x1 + 0.7 * math.cos(a), y1 + 0.7 * math.sin(a), col)
    disc(cx, cy, r, col)
    c.circle(int(round(cx)), int(round(cy)), int(r), OUT, fill=False)
    c.circle(int(round(cx)), int(round(cy)), max(1, int(r) - 1), dark, fill=False)
    for i in range(4):
        a = math.pi / 4 + i * math.pi / 2
        for t in range(hub + 1, int(r) - 1):
            P(cx + t * math.cos(a), cy + t * math.sin(a), dark)
    disc(cx, cy, hub, dark)
    disc(cx, cy, 1, BRASS_L)

def dial(x, y, r, needle_deg):
    c.rect(int(x) - r - 1, int(y) - r - 1, 2 * r + 3, 2 * r + 3, OUT, fill=True)
    disc(x, y, r, "#23232d")
    c.circle(int(round(x)), int(round(y)), int(r), BRASS, fill=False)
    a = math.radians(needle_deg)
    for t in range(1, r):
        P(x + t * math.cos(a), y + t * math.sin(a), GOLD)
    P(x, y, GOLD_L)
    for deg in range(0, 360, 90):
        aa = math.radians(deg)
        P(x + (r - 1) * math.cos(aa), y + (r - 1) * math.sin(aa), BRASS_D)

def step(x, y, w, h, top_h, front_col, top_col):
    c.rect(x - 1, y - 1, w + 2, h + 2, OUT, fill=True)
    c.rect(x, y + top_h, w, h - top_h, front_col, fill=True)
    c.rect(x, y, w, top_h, top_col, fill=True)

# ================= BACKGROUND: DARK HALL =================
c.rect(28, 0, 200, 238, WALL, fill=True)
for yy in (58, 118, 178):
    c.line(30, yy, 226, yy, WALL_S)
# pilasters
c.rect(30, 0, 14, 238, PIL, fill=True)
c.rect(30, 0, 2, 238, PIL_L, fill=True)
c.rect(212, 0, 14, 238, PIL, fill=True)
c.rect(224, 0, 2, 238, PIL_L, fill=True)
# floor
c.rect(0, 238, W, 18, FLOOR, fill=True)
c.line(0, 238, 255, 238, "#181826")

# haze halo behind the instrument
annulus_dither(CX, CY, 74, 92, HAZE)

# ================= PEDESTAL =================
disc(128, 252, 70, "#040407")
c.ellipse(128, 252, 70, 6, "#040407", fill=True)
annulus_dither(128, 248, 46, 66, "#0f2a28")
step(84, 236, 88, 16, 4, ST_FR1, ST_TOP1)
step(96, 224, 64, 12, 4, ST_FR2, ST_TOP2)
step(106, 212, 44, 12, 4, ST_FR3, ST_TOP3)
step(114, 198, 28, 14, 2, ST_FR4, ST_TOP4)
# stone seams
c.line(86, 246, 170, 246, ST_LINE)
for xx in (104, 122, 140, 158):
    c.line(xx, 240, xx, 245, ST_LINE)
    c.line(xx + 8, 247, xx + 8, 251, ST_LINE)
c.line(98, 230, 158, 230, ST_LINE)
c.line(108, 218, 148, 218, ST_LINE)
# magic circle on plinth top
c.ellipse(128, 199, 12, 2, TEAL, fill=False)
c.ellipse(128, 199, 7, 1, TEAL_D, fill=False)
rune(116, 199, TEAL_D, 2)
rune(140, 199, TEAL_D, 4)
# dials + alchemical triangle on platform front
dial(118, 219, 3, 210)
dial(138, 219, 3, 330)
c.poly([(128, 216), (131, 222), (125, 222)], GOLD, fill=False)
P(128, 219, GOLD_L)

# ================= LEVITATION BEAM =================
for y in range(120, 198):
    P(128, y, TEAL if y < 150 else TEAL_D)
    if y % 2 == 0:
        P(127, y, TEAL_D if y < 170 else TEAL_G)
        P(129, y, TEAL_D if y < 170 else TEAL_G)
for k, y in enumerate(range(132, 192, 12)):
    rune(134, y, TEAL, k)

# ================= ORRERY =================
# warm glow around the core
annulus_dither(CX, CY, 12, 22, GLOW1)
annulus_dither(CX, CY, 22, 34, GLOW2)

# faint light shafts
for deg in (208, 332):
    ray(CX, CY, deg, 24, 78, "#191207", step=3)
for deg in (28, 152):
    ray(CX, CY, deg, 24, 52, "#191207", step=3)

# --- outer graduated ring (astrolabe limb) ---
ring(CX, CY, 71, 71, BRASS_DD, 1)
ring(CX, CY, 70, 70, BRASS, 2)
ring(CX, CY, 67, 67, BRASS_D, 1)
# degree ticks
a = 0
while a < 360:
    rad = math.radians(a)
    major = (a % 30 == 0)
    r1 = 76 if major else 74
    col = GOLD if major else BRASS_D
    for t in range(71, r1 + 1):
        P(CX + t * math.cos(rad), CY + t * math.sin(rad), col)
    a += 6
arc(CX, CY, 70, 185, 255, BRASS_L)
arc(CX, CY, 70, 5, 75, BRASS_D)

# --- ring 3 with runes ---
ring(CX, CY, 57, 57, BRASS_DD, 1)
ring(CX, CY, 56, 56, BRASS, 2)
ring(CX, CY, 53, 53, BRASS_D, 1)
arc(CX, CY, 56, 185, 255, BRASS_L)
ring_runes(56, 45, VIO, start=22)

# --- ring 2 with runes ---
ring(CX, CY, 43, 43, BRASS_DD, 1)
ring(CX, CY, 42, 42, BRASS, 2)
ring(CX, CY, 39, 39, BRASS_D, 1)
arc(CX, CY, 42, 185, 255, BRASS_L)
ring_runes(42, 40, TEAL, start=10)

# --- inner ring ---
ring(CX, CY, 28, 28, BRASS, 1)
ring(CX, CY, 26, 26, BRASS_D, 1)
arc(CX, CY, 28, 185, 255, BRASS_L)

# --- equatorial band (horizontal, perspective) ---
ring(CX, CY, 58, 15, BRASS_DD, 1)
ring(CX, CY, 58, 15, BRASS, 1)
ring(CX, CY, 58, 12, BRASS_D, 1)
arc(CX, CY, 58, 190, 260, BRASS_L, ry=15)
ring_runes(58, 60, GOLD, ry=15, start=30)

# --- meridian band (vertical) ---
ring(CX, CY, 20, 62, BRASS_DD, 1)
ring(CX, CY, 20, 62, BRASS, 1)
ring(CX, CY, 17, 59, BRASS_D, 1)
arc(CX, CY, 20, 200, 250, BRASS_L, ry=62)

# --- orbiting crystal spheres ---
orb(CX + 42 * math.cos(math.radians(30)), CY + 42 * math.sin(math.radians(30)),
    4, TEAL, TEAL_L, TEAL_D, TEAL_G)
orb(CX + 42 * math.cos(math.radians(150)), CY + 42 * math.sin(math.radians(150)),
    4, MAG, MAG_L, MAG_D, MAG_G)
orb(CX + 42 * math.cos(math.radians(265)), CY + 42 * math.sin(math.radians(265)),
    4, BLUE, BLUE_L, BLUE_D, BLUE_G)
orb(CX + 70 * math.cos(math.radians(75)), CY + 70 * math.sin(math.radians(75)),
    5, VIO, VIO_L, VIO_D, VIO_G)
orb(CX + 70 * math.cos(math.radians(205)), CY + 70 * math.sin(math.radians(205)),
    5, BLUE, BLUE_L, BLUE_D, BLUE_G)
orb(CX + 70 * math.cos(math.radians(330)), CY + 70 * math.sin(math.radians(330)),
    5, MAG, MAG_L, MAG_D, MAG_G)
orb(CX + 58, CY, 5, BLUE, BLUE_L, BLUE_D, BLUE_G)
orb(CX - 58, CY, 5, TEAL, TEAL_L, TEAL_D, TEAL_G)
for deg in (45, 135, 225, 315):
    orb(CX + 28 * math.cos(math.radians(deg)), CY + 28 * math.sin(math.radians(deg)),
        2, GOLD, CORE_W, BRASS_D)

# --- gear mechanism ---
gear(110, 186, 8, 8, BRASS, BRASS_DD)
gear(146, 190, 10, 10, BRASS_D, BRASS_DD)
gear(128, 177, 6, 6, BRASS, BRASS_DD)
gear(165, 179, 5, 6, BRASS_D, BRASS_DD)
gear(93, 177, 4, 5, BRASS, BRASS_DD)
gear(57, 126, 6, 7, BRASS_D, BRASS_DD)
gear(199, 130, 7, 8, BRASS_D, BRASS_DD)
# connecting rods for the side gears
c.line(57, 126, 63, 119, BRASS_DD)
c.line(199, 130, 193, 123, BRASS_DD)

# --- radiant core ---
for deg in range(0, 360, 45):
    ray(CX, CY, deg, 12, 17, GOLD if deg % 90 == 0 else ORANGE)
for deg in (20, 70, 110, 160, 200, 250, 290, 340):
    ray(CX, CY, deg, 12, 15, BRASS_D)
disc(CX, CY, 11, ORANGE)
disc(CX, CY, 9, "#ffb347")
disc(CX, CY, 7, CORE_Y)
disc(CX, CY, 4, CORE_W)
c.circle(int(CX), int(CY), 11, BRASS_DD, fill=False)
P(CX - 3, CY - 3, CORE_W)
P(CX - 4, CY - 3, CORE_W)

# ================= FLOATING RUNES =================
floaters = [(58, 58, TEAL), (198, 66, VIO), (46, 140, GOLD), (210, 152, TEAL),
            (88, 34, VIO), (172, 30, GOLD), (36, 96, VIO), (222, 100, GOLD),
            (70, 200, TEAL), (190, 208, VIO)]
for k, (fx, fy, fc) in enumerate(floaters):
    rune(fx, fy, fc, k)
    P(fx, fy + 4, TEAL_G if fc == TEAL else (VIO_G if fc == VIO else GLOW1))

# ================= VIGNETTE =================
for (vx, vy) in ((0, 0), (230, 0), (0, 230), (230, 230)):
    c.dither(vx, vy, 26, 26, [BG, "#050509"], pattern="bayer4")

print(c.stats_text())
print(c.matrix_text(region=(48, 28, 208, 76)))
finish(c)
