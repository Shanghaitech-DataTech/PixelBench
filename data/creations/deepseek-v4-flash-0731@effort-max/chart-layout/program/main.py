from pixelbench_api import new_canvas, finish

W, H = 128, 64
c = new_canvas(W, H)

PANEL = "#fdf9ee"
BORDER = "#6b5a3f"
GRID = "#e9ddc7"
AXIS = "#4a3b28"

# --- background panel + frame ---
c.rect(0, 0, W, H, PANEL)
c.rect(0, 0, W, H, BORDER, fill=False)
c.line(14, 1, 14, 62, AXIS)
for u in range(15):
    c.line(14 + u * 7, 1, 14 + u * 7, 62, GRID)


def icon(x, y, rows, cmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            col = cmap.get(ch)
            if col:
                c.set(x + i, y + j, col)


apple_rows = [
    "............",
    "....b.......",
    "...gGg......",
    "..rRRRRr....",
    ".rRRRRRRr...",
    ".RRRRRRRRR..",
    ".RRRdRRRRR..",
    ".RRRRRRRRR..",
    ".rRRRRRRr...",
    ".rRRRRRRr...",
    "..rRRRRr....",
    "............",
]
apple_cm = {"r": "#a01320", "R": "#e0262f", "d": "#f0656f",
            "b": "#6b3a1f", "g": "#2e8b2e", "G": "#54c456"}

banana_rows = [
    "............",
    "......Yy....",
    "....yYYYy...",
    "...yYYYYy..",
    "..yYYYYYy..",
    "..yYYYYYYy.",
    "..yYYYYYYy.",
    "...yYYYYy..",
    "....yyyy...",
    "............",
    "............",
    "............",
]
banana_cm = {"Y": "#ffd93d", "y": "#d8a800"}

orange_rows = [
    "............",
    ".....Gg.....",
    "....OOOO....",
    "...OOOOOO...",
    "..OOOOOOOO..",
    ".OOOOOOOOOO.",
    ".OODOOOOOOO.",
    ".OOOOOOOOOO.",
    "..OOOOOOOO..",
    "...OOOOOO...",
    "....OOOO....",
    "............",
]
orange_cm = {"O": "#ff8c1a", "D": "#ffb060", "g": "#2e8b2e", "G": "#54c456"}

lemon_rows = [
    "............",
    ".....LL.....",
    "....LLLL....",
    "...LLLLLL...",
    "..LLLLLLLL..",
    ".wLLLLLLLLw.",
    "..LLLLLLLL..",
    "...LLLLLL...",
    "....LLLL....",
    ".....LL.....",
    "............",
    "............",
]
lemon_cm = {"L": "#fff23f", "w": "#ffffff"}

grape_rows = [
    ".....gG.....",
    "....gGG.....",
    "...uuuu.....",
    "..uuuuuu....",
    "..uWuuWu....",
    "..uuuuuu....",
    "...uuuu.....",
    "...uuuu.....",
    "....uu......",
    "....g.......",
    "............",
    "............",
]
grape_cm = {"u": "#7b2d9e", "W": "#a86ac0",
            "g": "#2e8b2e", "G": "#54c456"}

data = [
    (apple_rows, apple_cm, 10, "#e0262f", "#b01b23"),
    (banana_rows, banana_cm, 5, "#f0b400", "#c69500"),
    (orange_rows, orange_cm, 7, "#ff8c1a", "#d96f00"),
    (lemon_rows, lemon_cm, 14, "#f5e93d", "#cdbd1e"),
    (grape_rows, grape_cm, 2, "#8e44ad", "#6e2f8a"),
]

UNIT = 7
BAR_X = 15

for i, (rows, cmap, val, main, dark) in enumerate(data):
    y = 1 + i * 13
    icon(2, y, rows, cmap)
    bw = val * UNIT
    c.rect(BAR_X, y + 1, bw, 8, main)
    c.rect(BAR_X, y + 9, bw, 2, dark)

print(c.stats_text())
finish(c)
