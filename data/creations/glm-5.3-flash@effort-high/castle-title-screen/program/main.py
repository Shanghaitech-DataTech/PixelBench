# Fantasy RPG title screen: castle on seaside cliff at sunset
W = H = 128
c = new_canvas(W, H, background=None, name="title")

# ---------- palette ----------
SKY = [
    (0, 8,   "#241540"),
    (8, 20,  "#3d1f55"),
    (20, 34, "#6b2a5c"),
    (34, 48, "#a03e55"),
    (48, 60, "#cf5f3d"),
    (60, 70, "#ef8a3c"),
    (70, 78, "#ffc061"),
]
for y0, y1, col in SKY:
    c.rect(0, y0, W, y1 - y0, col)

# dithered transitions between sky bands
BAND_COLS = [s[2] for s in SKY]
for i in range(len(SKY) - 1):
    y = SKY[i][1]  # first row of next band
    c.dither(0, y - 2, W, 2, [BAND_COLS[i], BAND_COLS[i + 1]], pattern="checker")
    c.dither(0, y, W, 1, [BAND_COLS[i], BAND_COLS[i + 1]], pattern="bayer4")

# ---------- sun ----------
SUN = "#ffdf8a"
SUN2 = "#ffb14e"
c.circle(58, 64, 16, SUN)
c.circle(58, 64, 13, SUN2)
c.circle(58, 64, 9, SUN)
# sun glow rings (subtle, semi into sky)
c.circle(58, 64, 20, "#f9a54a", fill=False)
c.circle(58, 64, 24, "#e07a44", fill=False)

# ---------- sea ----------
SEA_BANDS = [
    (78, 84, "#ffb85e"),
    (84, 90, "#e07a44"),
    (90, 97, "#8f3f52"),
    (97, 104, "#4a2450"),
]
for y0, y1, col in SEA_BANDS:
    c.rect(0, y0, W, y1 - y0, col)
for i in range(len(SEA_BANDS) - 1):
    y = SEA_BANDS[i][1]
    c.dither(0, y - 1, W, 2, [SEA_BANDS[i][2], SEA_BANDS[i + 1][2]], pattern="checker")

# sun reflection on water: shimmering column under the sun
import random
random.seed(7)
for y in range(78, 104):
    wdt = 2 + (y - 78) // 5
    x0 = 58 - wdt
    for x in range(x0, x0 + 2 * wdt):
        if random.random() < 0.55 - (y - 78) * 0.012:
            col = "#ffdf8a" if y < 88 else "#f2953f"
            c.set(x, y, col)
# horizontal wave glints
for y in [80, 83, 86, 89, 92, 95, 98, 101]:
    for k in range(6):
        x = random.randrange(0, W - 8)
        ln = random.randrange(2, 6)
        col = "#ffc061" if y < 90 else "#6b2f55"
        c.line(x, y, x + ln, y, col)

# ---------- clouds (layered, back to front) ----------
def cloud_band(y, xs, w, h, col):
    c.ellipse(xs + w // 2, y, w // 2, h, col)

# high thin clouds (dark purple, behind sun)
cloud_band(12, 6, 40, 3, "#2c1a4a")
cloud_band(15, 70, 52, 3, "#2c1a4a")
cloud_band(22, 30, 46, 4, "#43205a")
cloud_band(26, 96, 30, 3, "#43205a")
# mid clouds crossing the sun (dark silhouettes with warm undersides)
cloud_band(40, -6, 56, 5, "#5c2450")
cloud_band(44, 84, 48, 5, "#5c2450")
cloud_band(52, 34, 62, 6, "#7a2f4e")
cloud_band(56, 100, 34, 4, "#7a2f4e")
# warm-lit lower clouds
cloud_band(64, 8, 44, 5, "#b04a45")
cloud_band(68, 92, 40, 5, "#b04a45")
cloud_band(72, 40, 52, 4, "#d96a3f")
# thin bright streaks near horizon
c.line(20, 75, 52, 75, "#ffd98a")
c.line(88, 74, 122, 74, "#ffd98a")
c.line(4, 71, 26, 71, "#f9b45c")

# ---------- cliff (right side) ----------
CLIFF_DARK = "#1c1128"
CLIFF_MID = "#2b1a38"
CLIFF_LIT = "#4a2a44"
# cliff mass
c.poly([(78, 128), (80, 96), (84, 84), (90, 76), (100, 72), (114, 70),
        (128, 70), (128, 128)], CLIFF_DARK)
# lit left edge of cliff (facing the sunset)
c.line(84, 84, 90, 76, CLIFF_LIT)
c.line(90, 76, 100, 72, CLIFF_LIT)
c.line(100, 72, 114, 70, CLIFF_LIT)
c.line(80, 96, 84, 84, CLIFF_MID)
# rocky facets
c.poly([(92, 128), (96, 100), (104, 92), (112, 96), (118, 110), (120, 128)], CLIFF_MID)
c.poly([(104, 128), (108, 108), (116, 104), (124, 116), (126, 128)], "#241530")
c.line(86, 90, 92, 82, "#33203f")
c.line(96, 104, 104, 96, "#33203f")

# ---------- castle ----------
STONE = "#3a2444"
STONE_D = "#241530"
STONE_L = "#5a3452"
ROOF = "#1a0f24"
FLAG = "#e0483c"
FLAG_D = "#a02c30"
WIN = "#ffcf6e"

CLIFF_TOP = 70  # ground line of castle

def tower(cx, w, top, body_col=STONE):
    # w wide tower from top to cliff top
    c.rect(cx, top, w, CLIFF_TOP - top, body_col)
    # shading: left lit, right dark
    c.rect(cx, top, 1, CLIFF_TOP - top, STONE_L)
    c.rect(cx + w - 1, top, 1, CLIFF_TOP - top, STONE_D)
    # crenellations
    for i in range(cx, cx + w, 3):
        c.rect(i, top - 2, 2, 2, body_col)
    c.rect(cx, top - 2, w, 1, STONE_D)

def flag(cx, top):
    # pole
    c.line(cx, top - 9, cx, top - 2, STONE_D)
    # pennant
    c.poly([(cx + 1, top - 9), (cx + 8, top - 7), (cx + 1, top - 5)], FLAG)
    c.poly([(cx + 1, top - 5), (cx + 5, top - 6), (cx + 1, top - 4)], FLAG_D)

# left tower
tower(88, 8, 40)
flag(91, 40)
# right tower (taller)
tower(112, 9, 32)
flag(116, 32)
# central keep between towers
c.rect(97, 48, 13, CLIFF_TOP - 48, STONE)
c.rect(97, 48, 1, CLIFF_TOP - 48, STONE_L)
c.rect(109, 48, 1, CLIFF_TOP - 48, STONE_D)
for i in range(97, 110, 3):
    c.rect(i, 46, 2, 2, STONE)
c.rect(97, 46, 13, 1, STONE_D)
# gatehouse / gate
c.rect(101, 62, 6, 8, STONE_D)
c.rect(102, 63, 4, 7, "#120a1c")
# windows (warm lit)
for wx, wy in [(90, 46), (90, 54), (91, 60), (115, 38), (115, 46), (116, 54),
               (100, 52), (104, 52), (107, 52), (100, 58), (107, 58), (103, 44)]:
    c.set(wx, wy, WIN)
# wall base merging into cliff
c.rect(86, 68, 38, 2, STONE_D)
# tiny banner line on keep
c.line(99, 50, 99, 56, FLAG_D)

# ---------- foreground rocks (dark, bottom) ----------
ROCK = "#120a1c"
ROCK2 = "#1d1128"
ROCK3 = "#2a1838"
c.poly([(0, 128), (0, 108), (10, 102), (22, 106), (34, 100), (48, 106),
        (60, 102), (74, 108), (88, 104), (100, 110), (112, 106), (128, 112),
        (128, 128)], ROCK)
# facet highlights
c.poly([(8, 128), (12, 108), (20, 106), (26, 116), (24, 128)], ROCK2)
c.poly([(40, 128), (44, 106), (54, 104), (60, 114), (58, 128)], ROCK2)
c.poly([(66, 128), (70, 110), (80, 108), (86, 118), (84, 128)], ROCK2)
c.poly([(96, 128), (100, 112), (110, 110), (118, 120), (116, 128)], ROCK3)
c.line(10, 102, 22, 106, "#33203f")
c.line(34, 100, 48, 106, "#33203f")
c.line(60, 102, 74, 108, "#33203f")

# ---------- title text ----------
GOLD = "#ffd27a"
GOLD_D = "#b0783a"
TITLE = "EMBERCOAST"
tw = len(TITLE) * 6 - 1
tx = (W - tw) // 2
c.text(tx + 1, 106, TITLE, GOLD_D, font="5x7")
c.text(tx, 105, TITLE, GOLD, font="5x7")
SUB = "- CHAPTER I -"
sw = len(SUB) * 6 - 1
c.text((W - sw) // 2, 115, SUB, "#e8a55c", font="5x7")

# ---------- birds ----------
for bx, by in [(30, 30), (36, 34), (24, 36), (70, 22), (76, 26)]:
    c.line(bx - 2, by, bx, by - 1, "#241530")
    c.line(bx, by - 1, bx + 2, by, "#241530")

# ---------- close any remaining holes ----------
w_, h_, rgba_ = c.to_rgba()
import numpy as np
arr = np.frombuffer(bytes(rgba_), dtype=np.uint8).reshape(h_, w_, 4)
holes = np.argwhere(arr[:, :, 3] == 0)
for y, x in holes:
    c.set(int(x), int(y), ROCK)

finish(c)

print(c.stats_text())
