"""mushroomling -- 16x16 RPG enemy: small mushroom monster.

4 colours: dark outline, cap red, cap shade, cream (spots + stem + feet).
Transparent background. Silhouette is filled first, then a 4-connected dark
outline is generated on the shape boundary, then features are painted.
"""

W = H = 16
CHAR_TO_HEX = {
    "O": "#2a161c",  # dark outline / eyes / mouth
    "R": "#d63c2a",  # cap red
    "S": "#a0261c",  # cap underside shade
    "W": "#f6ead0",  # cream: spots, stem, feet
}

grid = [["."] * W for _ in range(H)]


def span(y, x0, x1, ch):
    for x in range(x0, x1 + 1):
        grid[y][x] = ch


# ---------------------------------------------------------------- silhouette
# cap dome, one-pixel steps so the generated outline stays one pixel thick
span(1, 5, 10, "R")
span(2, 4, 11, "R")
span(3, 3, 12, "R")
span(4, 2, 13, "R")
span(5, 1, 14, "R")
span(6, 2, 13, "S")   # underside rim, stepped in
# stem / face
span(7, 3, 12, "W")
span(8, 3, 12, "W")
span(9, 2, 13, "W")   # stubby arms
span(10, 2, 13, "W")  # stubby arms
span(11, 3, 12, "W")
span(12, 3, 12, "W")
# stubby feet
span(13, 3, 6, "W")
span(13, 9, 12, "W")
span(14, 3, 6, "W")
span(14, 9, 12, "W")

# ------------------------------------------------- dark outline (4-connected)
for y in range(H):
    for x in range(W):
        if grid[y][x] == ".":
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H) or grid[ny][nx] == ".":
                grid[y][x] = "O"
                break

# ------------------------------------------------------------------- details
# white spots on the cap (kept clear of the silhouette edge)
for x, y in [
    (7, 2), (8, 2), (6, 3), (7, 3), (8, 3), (9, 3),   # top spot
    (3, 4), (4, 4), (3, 5), (4, 5),                   # left spot
    (11, 4), (12, 4), (11, 5), (12, 5),               # right spot
]:
    grid[y][x] = "W"
# round eyes
for x, y in [(5, 8), (6, 8), (5, 9), (6, 9), (9, 8), (10, 8), (9, 9), (10, 9)]:
    grid[y][x] = "O"
# little mouth
for x, y in [(7, 11), (8, 11)]:
    grid[y][x] = "O"
# cap shadow on the stem
for x, y in [(4, 7), (5, 7), (10, 7), (11, 7)]:
    grid[y][x] = "S"

print("\n".join("".join(row) for row in grid))

# -------------------------------------------------------------------- canvas
c = new_canvas(W, H, background=None, name="mushroomling")
for y in range(H):
    for x in range(W):
        ch = grid[y][x]
        if ch != ".":
            c.set(x, y, CHAR_TO_HEX[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
