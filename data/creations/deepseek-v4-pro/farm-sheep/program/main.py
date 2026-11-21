from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="result")

# Warm muted Stardew-like palette
colors = {
    '.': None,
    'W': '#F6EFE3',  # body/head wool cream
    'S': '#E0D2BE',  # wool shadow
    'L': '#FCF9F2',  # highlight
    'F': '#F1CDB8',  # face cream (warmer)
    'E': '#44352D',  # eye
    'N': '#C89B8C',  # nose
    'B': '#F4C4BE',  # blush
    'P': '#F2B8C8',  # ear pink
    'p': '#DE9FB2',  # ear pink shadow
    'G': '#E9DAC6',  # leg cream
    'H': '#B49B86',  # hoof
}

rows = [
    "................................",
    "................................",
    "................................",
    "................................",
    "........PP......................",
    ".......PPPP.....................",
    "..WWWWWPPPPWW...................",
    "..WWWWWPPppWWW..................",
    ".LLLWWWWWWWWWW.LLLLLL...........",
    "LLLWWWWWWWWWWWWLLLLWWWWWWW......",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWW....",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWW...",
    "FFFFFFFWWWWWWWWWWWWWWWWWWWWWWW..",
    "FFFEEFFWWWWWWWWWWWWWWWWWWWWWWW..",
    "NFFFBFWWWWWWWWWWWWWWWWWWWWWWW...",
    ".FFFFFWWWWWWWWWWWWWWWWWWWWWWW...",
    ".WWWWWWWWWWWWWWWWWWWWWWWWWWWW...",
    ".WWWWWWWWWWWWWWWWWWWWWWWWWWSS...",
    ".WWWWWWWWWWWWWWWWWWWWWWWWWSS....",
    ".WWWWWWWWWWWWWWWWWWWWWWWWWSS....",
    ".SSSSSSSSGGGSSSSSSSGGGSSSSSS....",
    ".SSSSSSSSGGGSSSSSSSGGGSSSSSS....",
    ".........GGG.......GGG..........",
    ".........GGG.......GGG..........",
    ".........GGG.......GGG..........",
    ".........GGG.......GGG..........",
    ".........HHH.......HHH..........",
    ".........HHH.......HHH..........",
    "................................",
    "................................",
    "................................",
    "................................",
]

for y, row in enumerate(rows):
    assert len(row) == 32, (y, len(row), row)
    for x, ch in enumerate(row):
        col = colors[ch]
        if col is not None:
            c.set(x + 1, y, col)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

finish(c)
