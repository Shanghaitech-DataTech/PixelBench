from pixelbench_api import new_canvas, finish

W, H = 128, 64

c = new_canvas(W, H, background="#0d1117", name="fruit_bar_chart")

BG = "#0d1117"
PANEL = "#141c2c"
GRID = "#1f2b42"
BORDER = "#33415e"
APPLE = "#e0434a"
APPLE_L = "#ff8a80"
BANANA = "#f0c330"
BANANA_L = "#ffdf6e"
ORANGE = "#ef7d26"
ORANGE_L = "#ffa95e"
LEMON = "#eed93f"
LEMON_L = "#fff07a"
GRAPE = "#9d55d8"
GRAPE_L = "#bf86f0"
GREEN = "#3f9e4f"


def draw_icon(c, x, y, rows, colmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            col = colmap.get(ch)
            if col is not None:
                c.set(x + i, y + j, col)


icons = {
    "apple": (
        ["......G.......",
         ".....GG......",
         "....RRRRR.....",
         "...RRRRRRR....",
         "..RRRLRRRRR...",
         "..RRRRRRRRRR..",
         ".RRRRRRRRRRR..",
         ".RRRRRRRRRRR..",
         "..RRRRRRRRR...",
         "...RRRRRRR...."],
        {"R": APPLE, "L": APPLE_L, "G": GREEN}),
    "banana": (
        ["..............",
         "....YYYYYY....",
         "...YYYYYYY....",
         "..YYYYYYYY...",
         "..YYYYYYY.....",
         ".YYYYYYY......",
         ".YYYYYY......",
         "..YYYY.......",
         "..............",
         ".............."],
        {"Y": BANANA}),
    "orange": (
        ["..............",
         ".....GG.......",
         "...OOOOOO....",
         "..OOOOOOOO...",
         "..OOOOOOOOO..",
         ".OOOOOOOOOO..",
         ".OOOOOOOOOO..",
         "..OOOOOOOO...",
         "...OOOOOO....",
         ".............."],
        {"O": ORANGE, "G": GREEN}),
    "lemon": (
        ["..............",
         "......YYYY....",
         "....YYYYYYY..",
         "...YYYYYYYY..",
         "..YYYYYYYYY..",
         "..YYYYYYYYY..",
         "...YYYYYYYY..",
         "....YYYYYY...",
         ".....YYY.....",
         ".............."],
        {"Y": LEMON}),
    "grape": (
        ["..............",
         "......G.......",
         "...PPPP......",
         "..PPPPPP.....",
         "..PPPPLP.....",
         "..PP.PP......",
         "...PPP.......",
         "..............",
         "..............",
         ".............."],
        {"P": GRAPE, "L": GRAPE_L, "G": GREEN}),
}

# panel
c.rect(2, 2, W - 4, H - 4, PANEL)

# grid
for x in range(20, 127, 28):
    c.line(x, 2, x, H - 3, GRID)
for y in range(2, H - 1, 12):
    c.line(20, y, W - 2, y, GRID)

# rows: apple 10, banana 5, orange 7, lemon 14, grape 2
rows = [
    (2, APPLE, 10, APPLE_L, "apple"),
    (14, BANANA, 5, BANANA_L, "banana"),
    (26, ORANGE, 7, ORANGE_L, "orange"),
    (38, LEMON, 14, LEMON_L, "lemon"),
    (50, GRAPE, 2, GRAPE_L, "grape"),
]

for y, col, val, light, name in rows:
    map_rows, colmap = icons[name]
    draw_icon(c, 2, y, map_rows, colmap)
    w = val * 7
    c.rect(20, y, w, 10, col)
    c.rect(20, y, w, 1, light)

# border
c.rect(0, 0, W, 1, BORDER)
c.rect(0, H - 1, W, 1, BORDER)
c.rect(0, 0, 1, H, BORDER)
c.rect(W - 1, 0, 1, H, BORDER)

print(c.stats_text())
finish(c)
