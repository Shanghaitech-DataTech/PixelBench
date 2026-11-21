from pixelbench_api import new_canvas, finish

W, H = 128, 64
c = new_canvas(W, H)

BG = c.color("#faf5e9")
FRAME = c.color("#d8cdad")
GRID = c.color("#e7dfc8")
AXIS = c.color("#55503f")

APPLE = c.color("#e8434e")
APPLE_L = c.color("#f2787f")
APPLE_D = c.color("#b12d40")
BANANA = c.color("#f2c531")
BANANA_L = c.color("#f8de72")
BANANA_D = c.color("#c79a1d")
ORANGE = c.color("#f59e2e")
ORANGE_L = c.color("#f9bf68")
ORANGE_D = c.color("#d67c16")
LEMON = c.color("#f2dd3e")
LEMON_L = c.color("#f8eb78")
LEMON_D = c.color("#d1b91f")
GRAPE = c.color("#9b59b6")
GRAPE_L = c.color("#bd82d4")
GRAPE_D = c.color("#773c92")
STEM = c.color("#7a4a21")
LEAF = c.color("#4f9e46")

c.rect(0, 0, W, H, BG)
c.rect(0, 0, W, H, FRAME, fill=False)

for gy in (24, 39):
    c.line(12, gy, 116, gy, GRID)

bars = [
    (22, 24, APPLE, APPLE_L, APPLE_D),
    (40, 39, BANANA, BANANA_L, BANANA_D),
    (58, 33, ORANGE, ORANGE_L, ORANGE_D),
    (76, 12, LEMON, LEMON_L, LEMON_D),
    (94, 48, GRAPE, GRAPE_L, GRAPE_D),
]
for x, top, main, light, dark in bars:
    c.rect(x, top, 11, 54 - top, main)
    c.rect(x + 11, top, 1, 54 - top, dark)
    c.rect(x, top, 1, 54 - top, light)

c.line(10, 54, 118, 54, AXIS)


def icon(cv, x, y, rows, cmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            col = cmap.get(ch)
            if col is not None:
                cv.set(x + i, y + j, col)


apple_rows = [
    "......S.....",
    ".....LS.....",
    "....LSS.....",
    "...AAAAAA...",
    "..AAAAAAAA..",
    ".AAAAAAAAAA.",
    ".AAAAAAAAAA.",
    "..AAAAAAAA..",
]
banana_rows = [
    "............",
    ".....BYYY....",
    "....BYYYY...",
    "...YYYYYY...",
    "..YYYYY.....",
    ".YYYYY......",
    ".YYB........",
    "............",
]
orange_rows = [
    "......L.....",
    ".....LLL....",
    ".....LLL....",
    "...OOOOOO...",
    "..OOOOOOOO..",
    ".OOOOOOOOOO.",
    ".OOOOOOOOOO.",
    "..OOOOOOOO..",
]
lemon_rows = [
    ".....LL.....",
    "....LLLL....",
    "...LLLLLL...",
    "..LLLLLLLL..",
    "..LLLLLLLL..",
    "...LLLLLL...",
    "....LLLL....",
    ".....LL.....",
]
grape_rows = [
    ".....G......",
    "....PPP.....",
    "...PPPPP....",
    "..PPPPPPP...",
    ".PPPPPPPPP..",
    ".PPPPPPPPP..",
    "..PPPPPPP...",
    "...PPPPP....",
]

icon(c, 22, 55, apple_rows, {"S": STEM, "L": LEAF, "A": APPLE})
icon(c, 40, 55, banana_rows, {"B": BANANA_D, "Y": BANANA})
icon(c, 58, 55, orange_rows, {"L": LEAF, "O": ORANGE})
icon(c, 76, 55, lemon_rows, {"L": LEMON})
icon(c, 94, 55, grape_rows, {"G": STEM, "P": GRAPE})

print("ICONS:")
print(c.matrix_text(region=(20, 55, 110, 63)))
print("BARS:")
print(c.matrix_text(region=(20, 10, 100, 55)))

finish(c)
