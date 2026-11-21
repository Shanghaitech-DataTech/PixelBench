from pixelbench_api import new_canvas, finish

W = H = 64

c = new_canvas(W, H, background="#141133")

SHADOW = "#0a0820"

BIG = {
    "P": ["#########", "#       #", "#       #", "#       #", "#########",
          "#       #", "#       #", "#       #", "#       #", "#       #", "#       #"],
    "I": ["  #####  ", "    #    ", "    #    ", "    #    ", "    #    ",
          "    #    ", "    #    ", "    #    ", "    #    ", "    #    ", "  #####  "],
    "X": ["#       #", " #     # ", "  #   #  ", "   # #   ", "    #    ",
          "   # #   ", "  #   #  ", " #     # ", "#       #", "#       #", "#       #"],
    "E": ["#########", "#       #", "#       #", "#       #", "#########",
          "#       #", "#       #", "#       #", "#########", "#       #", "#########"],
    "L": ["#      ", "#      ", "#      ", "#      ", "#      ",
          "#      ", "#      ", "#      ", "#      ", "#      ", "#######"],
}

SMALL = {
    "Q": [" ##### ", "#     #", "#     #", "#     #", "#     #", "#     #",
          "#  #   ", " #  #  ", "  ###  "],
    "U": ["#     #", "#     #", "#     #", "#     #", "#     #", "#     #",
          "#     #", "#     #", " ##### "],
    "E": ["#######", "#      ", "#      ", "#######", "#      ", "#      ",
          "#######", "#      ", "#######"],
    "S": ["#######", "#      ", "#      ", "#######", "      #", "      #",
          "      #", "#      ", "#######"],
    "T": ["#######", "   #   ", "   #   ", "   #   ", "   #   ", "   #   ",
          "   #   ", "   #   ", "   #   "],
}


def pts(g):
    return [(i, j) for j, r in enumerate(g) for i, ch in enumerate(r) if ch == "#"]


def word(x, y, text, f, fill, outline, spacing):
    fw = len(f[text[0]][0])
    sets = [(x + k * (fw + spacing), i, j) for k, ch in enumerate(text) for (i, j) in pts(f[ch])]
    assert all(0 <= gx + i < W and 0 <= y + j < H for (gx, i, j) in sets), (text, max(gx + i for gx, i, j in sets))
    for gx, i, j in sets:
        c.set(gx + i + 2, y + j + 2, SHADOW)
    for gx, i, j in sets:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    c.set(gx + i + dx, y + j + dy, outline)
    for gx, i, j in sets:
        c.set(gx + i, y + j, fill)


def sparkle(x, y, col):
    for (i, j) in [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (2, 3), (2, 4)]:
        c.set(x + i, y + j, col)


# --- border frame ---
c.rect(2, 2, 60, 60, "#3b3474", fill=False)
CORN = "#9890de"
c.rect(2, 2, 7, 1, CORN)
c.rect(2, 2, 1, 7, CORN)
c.rect(55, 2, 7, 1, CORN)
c.rect(61, 2, 1, 7, CORN)
c.rect(2, 55, 1, 7, CORN)
c.rect(2, 61, 7, 1, CORN)
c.rect(55, 61, 7, 1, CORN)
c.rect(61, 55, 1, 7, CORN)

# --- starfield dots ---
for (x, y, col) in [
    (14, 3, "#4b4485"), (30, 4, "#6b64ad"), (49, 3, "#8f88d0"), (58, 10, "#4b4485"),
    (60, 14, "#8f88d0"), (6, 24, "#8f88d0"), (60, 27, "#4b4485"), (58, 36, "#6b64ad"),
    (6, 43, "#8f88d0"), (4, 18, "#6b64ad"), (22, 57, "#4b4485"), (43, 58, "#6b64ad"),
    (57, 57, "#8f88d0"), (40, 60, "#4b4485"),
]:
    c.set(x, y, col)

# --- sparkles ---
sparkle(9, 6, "#ffe98a")
sparkle(53, 6, "#ffe98a")
sparkle(9, 52, "#ffe98a")
sparkle(53, 52, "#ffe98a")

# --- small center gems ---
for (x, y) in [(31, 51), (30, 52), (31, 52), (32, 52), (31, 53)]:
    c.set(x, y, "#ffe98a")

for (x, y) in [
    (31, 28), (30, 29), (31, 29), (32, 29), (29, 30), (30, 30), (31, 30), (32, 30),
    (33, 30), (28, 31), (29, 31), (30, 31), (31, 31), (32, 31), (33, 31), (34, 31),
    (30, 32), (31, 32), (32, 32), (31, 33),
]:
    c.set(x, y, "#ffd23f")
for (x, y) in [(31, 28), (30, 29), (31, 29), (32, 29)]:
    c.set(x, y, "#fff0b0")

# --- title words ---
word(6, 12, "PIXEL", BIG, "#ffd23f", "#4a2f04", 2)
word(12, 40, "QUEST", SMALL, "#6fe3ff", "#0d3f5c", 1)

print(c.stats_text())
print(c.matrix_text((2, 2, 61, 24)))
print(c.matrix_text((2, 38, 61, 50)))

finish(c)
