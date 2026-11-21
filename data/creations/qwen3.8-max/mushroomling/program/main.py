# Mushroomling - 16x16 RPG enemy sprite
# Palette (4 colours): K = dark outline, R = red cap, W = white spots, C = cream body

W_, H_ = 16, 16
grid = [['.'] * W_ for _ in range(H_)]


def h(y, x0, x1, ch):
    """Paint a horizontal run inclusive of both ends."""
    for x in range(x0, x1 + 1):
        if 0 <= x < W_ and 0 <= y < H_:
            grid[y][x] = ch


# ---------------------------------------------------------------- cap (rows 0-8)
h(0, 5, 10, 'K')
h(1, 3, 3, 'K'); h(1, 4, 11, 'R'); h(1, 12, 12, 'K')
h(2, 2, 2, 'K'); h(2, 3, 12, 'R'); h(2, 13, 13, 'K')
h(3, 1, 1, 'K'); h(3, 2, 13, 'R'); h(3, 14, 14, 'K')
h(4, 1, 1, 'K'); h(4, 2, 13, 'R'); h(4, 14, 14, 'K')
h(5, 0, 0, 'K'); h(5, 1, 14, 'R'); h(5, 15, 15, 'K')
h(6, 0, 0, 'K'); h(6, 1, 14, 'R'); h(6, 15, 15, 'K')
h(7, 0, 0, 'K'); h(7, 1, 14, 'R'); h(7, 15, 15, 'K')
h(8, 0, 15, 'K')                      # cap rim / underside

# white spots
h(2, 6, 8, 'W'); h(3, 6, 8, 'W'); h(4, 6, 8, 'W')                   # big centre blob
h(5, 2, 3, 'W'); h(6, 2, 3, 'W')                                     # left
h(5, 12, 13, 'W'); h(6, 12, 13, 'W')                                 # right

# ------------------------------------------------------- body / face (rows 9-13)
h(9, 4, 4, 'K'); h(9, 5, 10, 'C'); h(9, 11, 11, 'K')

# row 10: arm-top outline + eye highlights
h(10, 2, 3, 'K'); h(10, 12, 13, 'K')
h(10, 4, 4, 'K')
h(10, 5, 5, 'W'); h(10, 6, 6, 'C')
h(10, 7, 8, 'C')
h(10, 9, 9, 'W'); h(10, 10, 10, 'C')
h(10, 11, 11, 'K')

# row 11: eyes bottom, arms merge into body
h(11, 1, 1, 'K'); h(11, 2, 4, 'C')
h(11, 5, 6, 'K'); h(11, 7, 8, 'C'); h(11, 9, 10, 'K')
h(11, 11, 13, 'C'); h(11, 14, 14, 'K')

# row 12: mouth + arms
h(12, 1, 1, 'K'); h(12, 2, 6, 'C')
h(12, 7, 8, 'K')
h(12, 9, 13, 'C'); h(12, 14, 14, 'K')

# row 13: bottom outline of body and arms
h(13, 2, 13, 'K')

# ------------------------------------------------------------- legs (rows 14-15)
h(14, 4, 4, 'K'); h(14, 5, 6, 'C'); h(14, 7, 8, 'K')
h(14, 9, 10, 'C'); h(14, 11, 11, 'K')
h(15, 4, 6, 'K'); h(15, 9, 11, 'K')

# ------------------------------------------------------------------- paint it out
COLOURS = {
    'K': '#2b1d2e',   # dark outline
    'R': '#d93b3b',   # red cap
    'W': '#f7f4ea',   # white spots / eye glint
    'C': '#edc688',   # cream body
}

result = new_canvas(W_, H_, name="mushroomling")
for y in range(H_):
    for x in range(W_):
        ch = grid[y][x]
        if ch != '.':
            result.set(x, y, COLOURS[ch])

print(result.stats_text())
for row in grid:
    print(''.join(row))
print(view(result, scale=16, margin=1))

save("mushroomling", result, indexed=True)
finish(result)
