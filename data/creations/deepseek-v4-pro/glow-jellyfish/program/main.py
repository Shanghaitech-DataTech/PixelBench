W, H = 16, 16
c = new_canvas(W, H, name="glow-jellyfish")

# Deep-water bioluminescent palette. The bell interior uses semi-transparent
# glowing colours so it reads as translucent; the outline stays opaque.
palette = {
    '#': c.color("#0b1e33", name="outline"),
    'W': c.color((216, 250, 255, 235), name="glow_white"),
    'C': c.color((95, 212, 240, 205), name="glow_cyan"),
    'B': c.color((42, 127, 196, 190), name="glow_blue"),
    'D': c.color((26, 77, 125, 165), name="glow_deep"),
    'P': c.color((160, 106, 224, 190), name="glow_purple"),
    'c': c.color((111, 216, 242, 205), name="tentacle"),
}

rows = [
    "................",
    "......####......",
    ".....######.....",
    "....#WWCCWW#....",
    "...#DBCWWCBD#...",
    "..#DDBPWWPBDD#..",
    "..#DDBPCCPBDD#..",
    "..############..",
    "....#.#..#.#....",
    "....c.c..c.c....",
    "...c.c....c.c...",
    "...W.W....W.W...",
    "...W........W...",
    "................",
    "................",
    "................",
]

assert len(rows) == H
for y, row in enumerate(rows):
    assert len(row) == W, (y, row, len(row))
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, palette[ch])

# Nudge the sprite down one pixel so it floats centred in the 16x16 frame.
c.shift(0, 1, fill=None)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))
save("glow-jellyfish", c)
finish(c)
