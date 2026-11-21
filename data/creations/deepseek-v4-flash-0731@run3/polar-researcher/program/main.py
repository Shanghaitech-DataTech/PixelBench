from pixelbench_api import new_canvas, finish

W = H = 48
COL = {
    'o': '#10101a',   # outline
    'W': '#f4efe4',   # white parka
    'S': '#d8d0bf',   # parka shadow
    'k': '#d9a06a',   # skin
    'g': '#14141e',   # goggle frame
    'L': '#a9daf2',   # pale blue lens
    'l': '#e2f4fc',   # lens highlight
    'r': '#c94a2e',   # scarf red
    'd': '#a63a22',   # scarf dark
    'O': '#e85d2f',   # orange sleeve
    'C': '#9a6630',   # case brown
    'D': '#6f4520',   # case dark
    'M': '#c8ccd4',   # metal
    'P': '#42536b',   # pants
    'B': '#23232e',   # boots / gloves
    'c': '#cfe0ec',   # wind streak
}

c = new_canvas(W, H, name="polar-researcher")
grid = [['.'] * W for _ in range(H)]

def hfill(y, x0, x1, ch):
    x0 = max(0, x0)
    x1 = min(W - 1, x1)
    if x1 < x0:
        return
    for x in range(x0, x1 + 1):
        grid[y][x] = ch

def rchars(y, x0, chars):
    for i, ch in enumerate(chars):
        grid[y][x0 + i] = ch

# ---------------- wind streaks (pale blue) ----------------
hfill(3, 34, 38, 'c')
hfill(5, 2, 6, 'c')
hfill(6, 34, 39, 'c')
hfill(9, 2, 6, 'c')
hfill(10, 33, 39, 'c')
hfill(12, 3, 7, 'c')
hfill(13, 34, 38, 'c')
hfill(15, 2, 5, 'c')
hfill(17, 34, 39, 'c')
hfill(20, 2, 7, 'c')
hfill(24, 35, 40, 'c')
hfill(26, 2, 6, 'c')
hfill(29, 2, 8, 'c')
hfill(32, 3, 7, 'c')
hfill(36, 38, 43, 'c')
hfill(40, 2, 6, 'c')
hfill(44, 3, 6, 'c')
dots = [(45, 4), (44, 8), (47, 12), (3, 22), (46, 26), (44, 31), (2, 38), (45, 42), (43, 45), (46, 10), (45, 46)]
for (x, y) in dots:
    grid[y][x] = 'c'

# ---------------- scarf tail streaming behind (left) ----------------
hfill(11, 9, 13, 'r')
grid[11][12] = 'd'
hfill(12, 8, 12, 'd')
hfill(13, 8, 12, 'd')
hfill(14, 7, 11, 'r')
hfill(15, 8, 10, 'd')
hfill(16, 9, 11, 'r')

# ---------------- hood ----------------
hfill(2, 16, 29, 'o')
for y in range(3, 16):
    hfill(y, 15, 30, 'W')
    grid[y][14] = 'o'
    grid[y][31] = 'o'
for y in range(4, 10):
    grid[y][15] = 'S'

# face opening (rows 9-13) with goggles
for y in (9, 10):
    grid[y][22] = 'o'
    hfill(y, 23, 28, 'k')
    grid[y][29] = 'o'
# goggles
grid[11][22] = 'o'
grid[11][23] = 'g'
hfill(11, 24, 27, 'L')
grid[11][28] = 'g'
grid[11][29] = 'o'
grid[12][22] = 'o'
grid[12][23] = 'g'
grid[12][24] = 'l'
hfill(12, 25, 27, 'L')
grid[12][28] = 'g'
grid[12][29] = 'o'
# chin / scarf wrap
grid[13][22] = 'o'
hfill(13, 23, 28, 'k')
grid[13][29] = 'o'
grid[14][21] = 'o'
hfill(14, 22, 28, 'r')
grid[14][29] = 'o'
grid[15][21] = 'o'
hfill(15, 22, 28, 'r')
grid[15][29] = 'o'
grid[16][17] = 'o'
hfill(16, 18, 27, 'r')
grid[16][28] = 'o'

# ---------------- torso (leaning forward to the right) ----------------
for y in range(17, 33):
    x0 = 14 + (y - 17) // 2
    x1 = 30 + (y - 17) // 2
    hfill(y, x0, x1, 'W')
    grid[y][x0] = 'o'
    grid[y][x1] = 'o'
# coat hem
hfill(33, 22, 37, 'o')
hfill(33, 23, 36, 'W')
hfill(34, 23, 36, 'o')
hfill(34, 24, 35, 'W')
hfill(35, 24, 34, 'o')
hfill(35, 25, 33, 'W')
hfill(36, 25, 32, 'o')
hfill(36, 26, 31, 'W')
hfill(37, 24, 30, 'o')
hfill(37, 25, 29, 'P')

# ---------------- arms (orange sleeves) ----------------
# back arm swinging back-left
for i, y in enumerate(range(20, 26)):
    a = 13 - i
    grid[y][a] = 'o'
    hfill(y, a + 1, a + 2, 'O')
    grid[y][a + 3] = 'o'
    hfill(y, a + 1, a + 1, 'O')
# back glove
hfill(26, 9, 10, 'B')
grid[26][10] = 'B'
# front arm toward the case
for i, y in enumerate(range(21, 27)):
    a = 30 + i
    grid[y][a] = 'o'
    hfill(y, a + 1, a + 2, 'O')
    grid[y][a + 3] = 'o'
# front glove gripping the case
hfill(26, 33, 36, 'B')
hfill(27, 34, 36, 'B')

# ---------------- sample case ----------------
rchars(27, 35, 'oMMMMMMo')   # handle
rchars(28, 34, 'oCCCCCCCo')
rchars(29, 34, 'oCCCCCCCo')
rchars(30, 34, 'oCCCCCCCo')
rchars(31, 34, 'oCCCCCCCo')
rchars(32, 34, 'oCCCCCCCo')
grid[32][36] = 'M'
grid[32][37] = 'M'
grid[32][38] = 'M'
rchars(33, 35, 'oCCCCCo')
rchars(34, 35, 'oCCCCCo')
rchars(35, 36, 'oCCCo')
rchars(36, 37, 'oCo')
grid[37][38] = 'o'

# ---------------- legs (pants) ----------------
for i, y in enumerate(range(38, 42)):
    x0 = 24 - i
    grid[y][x0] = 'o'
    hfill(y, x0 + 1, x0 + 2, 'P')
# back boot
grid[42][19] = 'o'
hfill(42, 20, 24, 'B')
grid[42][25] = 'o'
grid[43][18] = 'o'
hfill(43, 19, 24, 'B')
grid[43][25] = 'o'
grid[44][18] = 'o'
hfill(44, 19, 23, 'B')
grid[44][24] = 'o'
grid[45][19] = 'o'
hfill(45, 20, 22, 'B')
grid[45][23] = 'o'
grid[46][20] = 'o'
hfill(46, 21, 22, 'B')
grid[46][23] = 'o'
grid[47][22] = 'o'
grid[47][23] = 'B'
# front leg
for i, y in enumerate(range(38, 42)):
    x0 = 30 + i
    grid[y][x0] = 'o'
    hfill(y, x0 + 1, x0 + 2, 'P')
# front boot
grid[42][34] = 'o'
hfill(42, 35, 38, 'B')
grid[42][39] = 'o'
grid[43][35] = 'o'
hfill(43, 36, 39, 'B')
grid[43][40] = 'o'
grid[44][36] = 'o'
hfill(44, 37, 39, 'B')
grid[44][40] = 'o'
grid[45][37] = 'o'
hfill(45, 38, 39, 'B')
grid[45][40] = 'o'
grid[46][37] = 'o'
hfill(46, 38, 39, 'B')
grid[46][40] = 'o'
grid[47][38] = 'o'
hfill(47, 39, 40, 'B')
grid[47][41] = 'o'

# ---------------- commit grid ----------------
for y in range(H):
    for x in range(W):
        ch = grid[y][x]
        if ch != '.':
            c.set(x, y, COL[ch])

print(c.stats_text())
result = c
finish(result)
