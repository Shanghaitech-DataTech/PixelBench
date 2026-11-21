from pixelbench_api import new_canvas, finish

W, H = 128, 64
c = new_canvas(W, H, background="#17141f")

# ---- palette ----
FRAME = "#3a3550"   # outer border
GRID  = "#26223a"   # faint value gridlines
AXIS  = "#554e70"   # category axis

fruits = [
    # name, value, bar colour, highlight, shade
    ("apple",  10, "#e0393b", "#ff6f71", "#a92a2e"),
    ("banana",  5, "#f4b400", "#ffd24d", "#b88a00"),
    ("orange",  7, "#f57c00", "#ffa83d", "#c25d00"),
    ("lemon",  14, "#e8e22e", "#f9f565", "#b5b01f"),
    ("grape",   2, "#9b4dca", "#c58fe0", "#743799"),
]

BAR_X = 20
SCALE = 7          # px per unit -> 14 units = 98 px
ROWS  = [2, 14, 26, 38, 50]   # top row of each category band

# ---- frame + value grid ----
c.rect(0, 0, W, H, FRAME, fill=False)
for v in range(0, 15):
    x = BAR_X - 1 + v * SCALE
    c.line(x, 2, x, 61, GRID)
c.line(BAR_X - 1, 1, BAR_X - 1, 62, AXIS)

# ---- 10x10 mini pixel icons ----
APPLE = [
    "..G.......",
    ".GG.......",
    "..S.......",
    ".RRRR.....",
    "RRRRRR....",
    "RRRRRRRR..",
    "RRRRRRRR..",
    ".RRRRRR...",
    "..RRRR....",
    "...RR.....",
]
BANANA = [
    "..YY......",
    ".YYYY.....",
    "YY.YY.....",
    "YY..YY....",
    "Y....YY...",
    "......YY..",
    ".......Y..",
    "..........",
    "..........",
    "..........",
]
ORANGE = [
    "..GG......",
    ".GG.......",
    "..........",
    ".OOOO.....",
    "OOOOOO....",
    "OOOOOOOO..",
    "OOOOOOOO..",
    ".OOOOOO...",
    "..OOOO....",
    "..........",
]
LEMON = [
    "....Y.....",
    "...YYY....",
    "..YYYYY...",
    ".YYYYYYY..",
    "YYYYYYYYY.",
    ".YYYYYYY..",
    "..YYYYY...",
    "...YYY....",
    "....Y.....",
    "..........",
]
GRAPE = [
    "..s.......",
    ".PP.PP....",
    "PPP.PPP...",
    ".PPPPPP...",
    "..PPPP....",
    "...PP.....",
    "..........",
    "..........",
    "..........",
    "..........",
]

PALS = [
    {"R": "#e0393b", "G": "#43a047", "S": "#795548"},
    {"Y": "#f4b400"},
    {"O": "#f57c00", "G": "#43a047"},
    {"Y": "#e8e22e"},
    {"P": "#9b4dca", "s": "#43a047"},
]
BITMAPS = [APPLE, BANANA, ORANGE, LEMON, GRAPE]


def draw_icon(x, y, bmp, pal):
    for j, row in enumerate(bmp):
        for i, ch in enumerate(row):
            if ch != ".":
                c.set(x + i, y + j, pal[ch])


# ---- bars + icons ----
for (name, val, col, hi, sh), ry, bmp, pal in zip(fruits, ROWS, BITMAPS, PALS):
    draw_icon(2, ry + 1, bmp, pal)
    w = val * SCALE
    c.rect(BAR_X, ry + 8, w, 1, sh)          # bottom shade
    c.rect(BAR_X, ry + 3, w, 5, col)         # body
    c.rect(BAR_X, ry + 3, w, 1, hi)          # top highlight

print(c.stats_text())
finish(c)
