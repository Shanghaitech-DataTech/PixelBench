# 16x16 mushroomling - RPG enemy, 4 colors + transparent
result = new_canvas(16, 16, name="mushroomling")

OUTLINE = "#26181d"
RED     = "#d23a31"
WHITE   = "#f7f1e3"
TAN     = "#e9c285"

colors = {"O": OUTLINE, "R": RED, "W": WHITE, "T": TAN}

art = [
    "................",
    "......OOOO......",
    "....ORRRRRRO....",
    "...ORRRWWRRRO...",
    "..ORWWRRRRWWRO..",
    "..ORWWRRRRWWRO..",
    "...ORRRRRRRRO...",
    "...OOOOOOOOOO...",
    "....OTTTTTTO....",
    "....OTWTTWTO....",
    "...TOTOTTOTOT...",
    "...OORTTTTROO...",
    "....OTTTTTTO....",
    "....OTOOOOTO....",
    "....OOO..OOO....",
    "................",
]

for y, row in enumerate(art):
    for x, ch in enumerate(row):
        if ch in colors:
            result.set(x, y, colors[ch])

view(result)
finish(result)
