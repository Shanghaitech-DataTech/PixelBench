from pixelbench_api import new_canvas, finish, save, view

# Wooden key, 16x16, 5 colours (limit 6).
c = new_canvas(16, 16, background=None, name="wooden_key")

PAL = {
    "o": "#4a2c17",  # dark outline
    "w": "#8b5a2b",  # mid wood
    "d": "#6b3f1f",  # dark wood shade
    "l": "#b07a45",  # light wood
    "g": "#d9a55f",  # golden shine / grain knot
}
IDX = {k: c.color(v, name=k) for k, v in PAL.items()}

ROWS = [
    "................",
    "......ooooo.....",
    ".....oglwwdo....",
    ".....ow...wo....",
    ".....ow...do....",
    ".....owwwdwo....",
    "......owwwo.....",
    ".......lwd......",
    ".......lwd......",
    ".......lgd......",
    ".......lwd......",
    ".......lwdoooo..",
    ".......lwdwwwo..",
    ".......lwdooo...",
    ".......lwdwwo...",
    ".......oooooo...",
]

for y, row in enumerate(ROWS):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, IDX[ch])

print(c.stats_text())
print(c.matrix_text())

finish(c)
