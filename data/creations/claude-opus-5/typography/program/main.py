L = [
    "#######",
    "##...##",
    "##...##",
    "##...##",
    "#######",
    "##.....",
    "##.....",
    "##.....",
    "##.....",
]
GLYPHS = {
    "P": [
        "#######",
        "##...##",
        "##...##",
        "##...##",
        "#######",
        "##.....",
        "##.....",
        "##.....",
        "##.....",
    ],
    "I": [
        "#######",
        "#######",
        "..###..",
        "..###..",
        "..###..",
        "..###..",
        "..###..",
        "#######",
        "#######",
    ],
    "X": [
        "##...##",
        "##...##",
        ".##.##.",
        "..###..",
        "..###..",
        "..###..",
        ".##.##.",
        "##...##",
        "##...##",
    ],
    "E": [
        "#######",
        "#######",
        "##.....",
        "######.",
        "######.",
        "##.....",
        "##.....",
        "#######",
        "#######",
    ],
    "L": [
        "##.....",
        "##.....",
        "##.....",
        "##.....",
        "##.....",
        "##.....",
        "##.....",
        "#######",
        "#######",
    ],
    "Q": [
        ".#####.",
        "##...##",
        "##...##",
        "##...##",
        "##...##",
        "##...##",
        ".#####.",
        "....##.",
        ".....##",
    ],
    "U": [
        "##...##",
        "##...##",
        "##...##",
        "##...##",
        "##...##",
        "##...##",
        "##...##",
        "#######",
        "#######",
    ],
    "S": [
        "#######",
        "#######",
        "##.....",
        "#######",
        "#######",
        ".....##",
        ".....##",
        "#######",
        "#######",
    ],
    "T": [
        "#######",
        "#######",
        "..###..",
        "..###..",
        "..###..",
        "..###..",
        "..###..",
        "..###..",
        "..###..",
    ],
}

ROWCOL = [
    "#fff4c2", "#fff4c2",
    "#ffdc62", "#ffdc62",
    "#ffc234", "#ffc234",
    "#f2a128", "#df8420", "#c56a15",
]

OUTLINE = "#2a1206"
SHADOW = "#120b22"


def word_pixels(word, x0, y0, pitch=9):
    out = {}
    for i, ch in enumerate(word):
        g = GLYPHS[ch]
        gx = x0 + i * pitch
        for ry, row in enumerate(g):
            for rx, cell in enumerate(row):
                if cell == "#":
                    out[(gx + rx, y0 + ry)] = ROWCOL[ry]
    return out


c = new_canvas(64, 64, name="output")

# --- sky ---
for y0, y1, col in [
    (0, 8, "#0a0920"),
    (8, 16, "#111030"),
    (16, 26, "#1a1740"),
    (26, 36, "#232050"),
    (36, 45, "#2e2660"),
    (45, 52, "#3b2c69"),
]:
    c.rect(0, y0, 64, y1 - y0, col)

# --- stars ---
for (sx, sy) in [(3, 3), (9, 8), (17, 2), (26, 6), (34, 3), (43, 9),
                 (50, 2), (60, 6), (2, 14), (6, 24), (3, 33), (57, 17),
                 (61, 27), (58, 36), (7, 40), (56, 44)]:
    c.set(sx, sy, "#ffffff")
for (sx, sy) in [(13, 5), (31, 10), (47, 5), (2, 20), (61, 12), (5, 30), (60, 33)]:
    c.set(sx, sy, "#9fb4ef")

# moon
c.circle(53, 8, 4, "#f6efc6")
c.circle(51, 7, 1, "#e2d9a8")
c.set(55, 10, "#e2d9a8")

# --- mountains ---
c.poly([(0, 50), (9, 41), (16, 48), (25, 39), (34, 48), (42, 42),
        (52, 49), (63, 43), (63, 52), (0, 52)], "#241d4c")
c.poly([(0, 52), (6, 47), (13, 51), (22, 45), (31, 51), (40, 46),
        (49, 51), (58, 46), (63, 51), (63, 53), (0, 53)], "#120e2c")
c.rect(0, 52, 64, 12, "#0a0718")
c.line(0, 52, 63, 52, "#4b3a7d")

# --- title lettering ---
px = word_pixels("PIXEL", 10, 13)
qx = word_pixels("QUEST", 10, 26)
letters = {}
letters.update(px)
letters.update(qx)

# drop shadow
for (x, y) in letters:
    if (x + 2, y + 2) not in letters:
        c.set(x + 2, y + 2, SHADOW)
# outline
for (x, y) in letters:
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            p = (x + dx, y + dy)
            if p not in letters:
                c.set(p[0], p[1], OUTLINE)
# glyphs
for (x, y), col in letters.items():
    c.set(x, y, col)

# --- decorative sparkles beside the title ---
def sparkle(cx, cy, col="#ffe98a"):
    c.set(cx, cy, "#ffffff")
    c.set(cx - 1, cy, col)
    c.set(cx + 1, cy, col)
    c.set(cx, cy - 1, col)
    c.set(cx, cy + 1, col)

sparkle(4, 20)
sparkle(59, 36)
sparkle(43, 7, "#9fe8ff")

# --- divider + prompt ---
for x in list(range(13, 28, 2)) + list(range(36, 51, 2)):
    c.set(x, 40, "#5d4d96")
# centre diamond
c.set(31, 40, "#ffd95e")
c.set(32, 40, "#ffd95e")
c.set(30, 40, "#c56a15")
c.set(33, 40, "#c56a15")
c.set(31, 39, "#ffe98a")
c.set(32, 41, "#ffe98a")
c.set(11, 40, "#9fe8ff")
c.set(52, 40, "#9fe8ff")

c.text(2, 55, "PUSH START", "#a9b3dd", spacing=1)

view(c)
print(c.stats_text())
finish(c)
