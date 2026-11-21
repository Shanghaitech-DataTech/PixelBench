from pixelbench_api import new_canvas, finish

# 16x16 mushroomling - 4 visible colours:
#   O = dark outline, R = red cap, W = white spots/eyes, T = tan body
ROWS = [
    "...." + "O" * 8 + "....",
    "..O" + "R" * 10 + "O..",
    ".O" + "R" * 5 + "W" + "R" * 6 + "O.",
    ".O" + "R" * 3 + "W" + "R" * 4 + "W" + "R" * 3 + "O.",
    "O" + "R" * 14 + "O",
    "O" + "R" * 3 + "W" + "R" * 6 + "W" + "R" * 3 + "O",
    "O" * 16,
    "..." + "O" + "T" * 8 + "O" + "...",
    ".OT" + "O" + "T" + "WW" + "TT" + "WW" + "T" + "O" + "TO.",
    ".OT" + "O" + "T" + "W" + "O" + "TT" + "O" + "W" + "T" + "O" + "TO.",
    ".OTO" + "T" * 8 + "OTO.",
    ".OTO" + "T" * 8 + "OTO.",
    "..." + "O" * 10 + "...",
    "..." + "O" + "T" * 3 + ".." + "T" * 3 + "O" + "...",
    "..." + "O" + "T" * 3 + ".." + "T" * 3 + "O" + "...",
    "..." + "O" * 3 + "...." + "O" * 3 + "...",
]
assert len(ROWS) == 16
for row in ROWS:
    assert len(row) == 16, (len(row), row)

c = new_canvas(16, 16, name="mushroomling")

PAL = {"O": "#141414", "R": "#d9403f", "W": "#f6f1e0", "T": "#e8c287"}
for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, c.color(PAL[ch]))

print(c.stats_text())
print(c.matrix_text(indices=False))
finish(c)
