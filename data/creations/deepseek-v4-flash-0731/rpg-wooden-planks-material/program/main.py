from pixelbench_api import new_canvas, finish, view, save

# Palette (8 colours)
PAL = {
    '#': "#241207",  # dark seam groove
    'A': "#c99a63",  # light board base
    'a': "#9f7140",  # light board grain
    'o': "#d9ab72",  # chamfer highlight
    'B': "#9c6f41",  # dark board base
    'b': "#77502a",  # dark board grain
    'R': "#5c3a1c",  # knot ring
    'C': "#3b2410",  # knot core
}

# 16 rows x 16 cols; boards: 3px wide, 1px grooves at x=0,4,8,12
# Row 0 == Row 15 -> seamless vertical tiling; grooves at x=0/15 edge -> seamless horizontal tiling
ROWS = [
    "#aAA#BbB#AaA#bBB",
    "#aAA#BbB#AaA#bBB",
    "#AaA#BbB#AaA#bBB",
    "#AoA#bBB#AaA#BbB",
    "#AAa#bBB#aAA#BbB",
    "#AAa#RRB#aAA#BbB",
    "#AAa#RCR#aAA#BbB",
    "#AaA#RRB#AoA#BbB",
    "#AaA#BbB#AaA#BbB",
    "#AaA#BbB#AAa#BbB",
    "#aAA#BbB#AAa#BbB",
    "#aAA#BbB#AAa#RRB",
    "#aAA#BbB#AAa#RCR",
    "#aAA#BbB#AAa#RRB",
    "#aAA#BbB#AAa#BbB",
    "#aAA#BbB#AaA#bBB",
]

assert all(len(r) == 16 for r in ROWS)
assert ROWS[0] == ROWS[15]

c = new_canvas(16, 16)
for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text())
save("rpg-wooden-planks-material", c)
print("saved preview")
finish(c)
