DISC = {
    0: (5, 10), 1: (3, 12), 2: (2, 13), 3: (1, 14), 4: (1, 14),
    5: (0, 15), 6: (0, 15), 7: (0, 15), 8: (0, 15), 9: (0, 15), 10: (0, 15),
    11: (1, 14), 12: (1, 14), 13: (2, 13), 14: (3, 12), 15: (5, 10),
}

STAR = [
    "....#....",
    "...###...",
    "...###...",
    "#########",
    ".#######.",
    "..#####..",
    "..##.##..",
    ".##...##.",
]
STAR_X, STAR_Y = 3, 4

DARK = "#5e3508"
RIM = "#ffe9a3"
MID = "#eda521"
SHADOW = "#b4700d"
STARC = "#fff8d8"


def erode(px):
    """4-connected erosion: keep pixels whose N/S/E/W neighbours are all inside."""
    return {
        (x, y) for (x, y) in px
        if (x - 1, y) in px and (x + 1, y) in px
        and (x, y - 1) in px and (x, y + 1) in px
    }


disc = {(x, y) for y, (x0, x1) in DISC.items() for x in range(x0, x1 + 1)}
inner1 = erode(disc)          # inside the dark outline
field = erode(inner1)         # inside the light rim
core = erode(field)

c = new_canvas(16, 16, name="coin")

for (x, y) in sorted(disc):
    c.set(x, y, DARK)
for (x, y) in sorted(inner1):
    c.set(x, y, RIM)
for (x, y) in sorted(field):
    c.set(x, y, MID)

# thin shadow crescent hugging the lower-right of the inner field
for (x, y) in sorted(field - core):
    if (x - 7.5) + (y - 7.5) > 2.5:
        c.set(x, y, SHADOW)

# glint: short diagonal sparkle on the upper-left of the inner field
for (x, y) in [(4, 4), (3, 5)]:
    c.set(x, y, RIM)

# star
for j, row in enumerate(STAR):
    for i, ch in enumerate(row):
        if ch == "#":
            c.set(STAR_X + i, STAR_Y + j, STARC)

print(c.stats_text())
print(c.matrix_text())
view(c)
finish(c)
