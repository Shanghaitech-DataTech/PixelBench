S = 4
COL = {'a': '#141b1bff', 'b': '#d14b34ff', 'c': '#e46d3aff',
       'd': '#8f3e56ff', 'e': '#543c52ff'}

# static part: pole + the two red bands that wrap it (cols 0-4), cloth cleared
static = [
    "............",
    "............",
    "............",
    ".aaaa.......",
    ".adda.......",
    "abcbb.......",
    ".aeea.......",
    ".adda.......",
    "abcbb.......",
    ".aeea.......",
    ".adda.......",
    ".adda.......",
    ".adda.......",
    ".adda.......",
]

CLOTH_X = list(range(5, 11))   # body columns; col 11 carries the fly-end outline


def make(top, bot, hi_anchor="top"):
    """Build a 12x14 logical grid: cloth band from top[x] to bot[x] + dark outline."""
    g = [list(r) for r in static]
    for i, x in enumerate(CLOTH_X):
        t, b = top[i], bot[i]
        for y in range(t, b + 1):
            g[y][x] = 'b'
        g[t - 1][x] = 'a'
        g[b + 1][x] = 'a'
    for y in range(top[-1] - 1, bot[-1] + 2):      # fly-end edge
        g[y][11] = 'a'
    # lit fold near the pole: 2 cells on col 6, 3 on col 7
    if hi_anchor == "top":
        cells = [(6, top[1]), (6, top[1] + 1),
                 (7, top[2]), (7, top[2] + 1), (7, top[2] + 2)]
    else:
        cells = [(6, bot[1] - 1), (6, bot[1]),
                 (7, bot[2] - 2), (7, bot[2] - 1), (7, bot[2])]
    for x, y in cells:
        g[y][x] = 'c'
    return g


def render(g, name):
    c = new_canvas(12 * S, 14 * S, name=name)
    for y, row in enumerate(g):
        for x, ch in enumerate(row):
            if ch != '.':
                c.rect(x * S, y * S, S, S, COL[ch])
    return c


# frame 1: fly end at its highest (the original picture)
F1_TOP = [4, 4, 3, 2, 1, 1]
F1_BOT = [7, 7, 7, 7, 6, 5]

# frame 2: wave has travelled outward, fly end mid
F2_TOP = [4, 4, 5, 5, 4, 4]
F2_BOT = [7, 7, 8, 8, 7, 7]

# frame 3: fly end at its lowest (vertical mirror of frame 1 about the pole band)
F3_TOP = [11 - b for b in F1_BOT]
F3_BOT = [11 - t for t in F1_TOP]

check = render(make(F1_TOP, F1_BOT), "check")
f1 = input_canvas.copy(name="f1")
diff = sum(1 for y in range(56) for x in range(48) if check.get(x, y) != f1.get(x, y))
print("frame1 generator vs original, differing pixels:", diff)

f2 = render(make(F2_TOP, F2_BOT), "f2")
f3 = render(make(F3_TOP, F3_BOT, hi_anchor="bot"), "f3")

view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
