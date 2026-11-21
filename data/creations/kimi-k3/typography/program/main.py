from pixelbench_api import *

c = new_canvas(64, 64, background="#16162e", name="pixel_quest")

# ---------- palette ----------
BG0, BG1, BG2, BG3 = "#16162e", "#1b1b3a", "#20204a", "#292659"
BORDER = "#4a3a8c"
GOLD = "#ffb03a"
GOLD_LT = "#ffd75e"
BROWN = "#7a4a22"
BLADE_HI, BLADE, BLADE_SH = "#eef2ff", "#c9d2ee", "#8f9ac0"
STAR_A, STAR_B = "#8fa3e8", "#cfd8ff"
WHITE = "#ffffff"
SPARK = "#fff6c9"
PXL_OUT = "#0e2a4a"
PXL_SH = "#0a0a18"
Q_OUT = "#4a2408"
Q_SH = "#0d0a20"
PIXEL_COLS = ["#eafaff", "#cfefff", "#9fd8f2", "#9fd8f2", "#6fb7e8", "#4a96d0", "#3a7cb8"]
QUEST_COLS = ["#fff7c2", "#ffe36b", "#ffd23e", "#ffb03a", "#f79226", "#e0731d", "#c95a14"]
GEM = ["#ffc2cc", "#ff8a96", "#ff6b80", "#e8405a", "#c22c46", "#a02640", "#7c1a2e"]

FONT = {
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
}

def each_px(s, x, y, scale, tracking):
    cx = x
    for ch in s:
        g = FONT[ch]
        for gy, row in enumerate(g):
            for gx, v in enumerate(row):
                if v == '#':
                    yield cx + gx * scale, y + gy * scale, gy
        cx += (len(g[0]) + tracking) * scale

def draw_word(s, x, y, scale, tracking, rowcolors, outline=None, shadow=None, glow=None):
    if glow:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            for px, py, gy in each_px(s, x + dx, y + dy, scale, tracking):
                c.rect(px, py, scale, scale, glow)
    if shadow:
        dx, dy, col = shadow
        for px, py, gy in each_px(s, x + dx, y + dy, scale, tracking):
            c.rect(px, py, scale, scale, col)
    if outline:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)):
            for px, py, gy in each_px(s, x + dx, y + dy, scale, tracking):
                c.rect(px, py, scale, scale, outline)
    for px, py, gy in each_px(s, x, y, scale, tracking):
        c.rect(px, py, scale, scale, rowcolors[gy])

def sparkle(x, y, col=SPARK, r=2):
    for d in range(1, r + 1):
        c.set(x, y - d, col)
        c.set(x, y + d, col)
        c.set(x - d, y, col)
        c.set(x + d, y, col)
    c.set(x, y, WHITE)

# ---------- background bands + dithered transitions ----------
c.rect(0, 16, 64, 16, BG1)
c.rect(0, 32, 64, 16, BG2)
c.rect(0, 48, 64, 16, BG3)
c.dither(0, 15, 64, 2, [BG0, BG1], "bayer4")
c.dither(0, 31, 64, 2, [BG1, BG2], "bayer4")
c.dither(0, 47, 64, 2, [BG2, BG3], "bayer4")

# ---------- stars ----------
for sx, sy, col in [(9, 6, STAR_A), (44, 5, STAR_A), (56, 8, STAR_B), (35, 3, STAR_A),
                    (6, 26, STAR_A), (58, 25, STAR_A), (8, 50, STAR_B), (55, 51, STAR_A),
                    (14, 59, STAR_A), (50, 60, STAR_B), (26, 57, STAR_A), (40, 58, STAR_A)]:
    c.set(sx, sy, col)
# one small cross star
c.set(24, 4, STAR_B); c.set(24, 3, STAR_B); c.set(24, 5, STAR_B)
c.set(23, 4, STAR_B); c.set(25, 4, STAR_B)

# ---------- border & corner brackets ----------
c.rect(0, 0, 64, 1, BORDER)
c.rect(0, 63, 64, 1, BORDER)
c.rect(0, 0, 1, 64, BORDER)
c.rect(63, 0, 1, 64, BORDER)
c.rect(2, 2, 4, 1, GOLD); c.rect(2, 2, 1, 4, GOLD)
c.rect(58, 2, 4, 1, GOLD); c.rect(61, 2, 1, 4, GOLD)
c.rect(2, 61, 4, 1, GOLD); c.rect(2, 58, 1, 4, GOLD)
c.rect(58, 61, 4, 1, GOLD); c.rect(61, 58, 1, 4, GOLD)

# ---------- PIXEL (small, icy) ----------
draw_word("PIXEL", 15, 10, 1, 2, PIXEL_COLS, outline=PXL_OUT, shadow=(1, 1, PXL_SH), glow=(1, 1, 1, 80))

# ---------- sword divider ----------
c.rect(22, 21, 1, 3, GOLD_LT)          # pommel
c.rect(23, 22, 4, 1, BROWN)            # grip
c.set(24, 22, GOLD_LT)                 # grip band
c.rect(27, 20, 1, 5, GOLD)             # guard
c.rect(28, 21, 13, 1, BLADE_HI)        # blade highlight
c.rect(28, 22, 13, 1, BLADE)           # blade
c.rect(28, 23, 13, 1, BLADE_SH)        # blade shade
c.set(41, 22, BLADE_HI)                # tip

# ---------- QUEST (big, gold) ----------
draw_word("QUEST", 3, 33, 2, 1, QUEST_COLS, outline=Q_OUT, shadow=(2, 2, Q_SH))
# dark inner counters (negative space for readability)
c.rect(13, 39, 3, 4, "#1c1030")
c.rect(39, 39, 3, 2, "#1c1030")
c.set(47, 45, "#1c1030")

# ---------- sparkles above QUEST ----------
sparkle(7, 28)
sparkle(56, 28)

# ---------- gem ornament below ----------
gx, gy = 32, 55
for dy in range(-3, 4):
    half = 3 - abs(dy)
    c.rect(gx - half, gy + dy, 2 * half + 1, 1, GEM[dy + 3])
c.set(gx - 1, gy - 2, WHITE)           # glint
c.set(gx - 2, gy - 1, "#ffd9de")
# gem halo pixels
for hx, hy in [(32, 52), (29, 55), (35, 55), (32, 58)]:
    c.set(hx, hy, (255, 107, 128, 110))
for fx in (22, 42):
    c.set(fx, gy - 1, GOLD_LT)
    c.set(fx - 1, gy, GOLD)
    c.set(fx + 1, gy, GOLD)
    c.set(fx, gy + 1, GOLD)

view(c)
finish(c)
