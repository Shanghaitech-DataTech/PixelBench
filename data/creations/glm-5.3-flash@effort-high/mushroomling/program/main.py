from pixelbench_api import new_canvas, finish

# 16x16 mushroom monster sprite, 4 colours + transparency
# legend: . = transparent, o = dark outline, r = red cap, w = white spot, c = cream body

ROWS = [
    ".....oooooo.....",
    "...oorrrrrroo...",
    "..orrrrwwrrrro..",
    ".orrwwrrrrwwrro.",
    "..orrrwwrrrrro..",
    "..orrrrrrrrrro..",
    "..oooooooooooo..",
    "...occcccccco...",
    "...ocooccooco...",
    ".ocooccooccooco.",
    ".ococccoocccoco.",
    ".ococcccccccoco.",
    "..oooooooooooo..",
    "....oo....oo....",
    "....oo....oo....",
    "................",
]

COLORS = {
    "o": "#2a1a16",  # dark outline / eyes / mouth / legs
    "r": "#d8352a",  # red cap
    "w": "#f7f3e8",  # white spots
    "c": "#f2d8a8",  # cream body
}

for row in ROWS:
    assert len(row) == 16, row

c = new_canvas(16, 16, background=None, name="mushroomling")

idx = {ch: c.color(hexv, name=name) for ch, hexv, name in [
    ("o", "#2a1a16", "outline"),
    ("r", "#d8352a", "cap_red"),
    ("w", "#f7f3e8", "spot_white"),
    ("c", "#f2d8a8", "body_cream"),
]}

for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, idx[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
