from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H)

def col(h):
    return c.color(h)

# ------------------------- sky -------------------------
sky_bands = ["#0a0f33", "#101743", "#162052", "#1d2c66", "#243a7c",
            "#2c4a8f", "#34518f", "#3f5f96"]
for i, hx in enumerate(sky_bands):
    c.rect(0, i * 8, W, 8, col(hx))

# ------------------------- stars -------------------------
for (sx, sy) in [(5, 5), (12, 3), (24, 5), (34, 3), (44, 4), (58, 14),
                (18, 15)]:
    c.set(sx, sy, col("#bcd2ff") if (sx + sy) % 3 else col("#ffffff"))
for sx, sy in [(10, 9), (28, 2), (8, 14), (19, 20)]:
    for dx, dy in [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]:
        c.set(sx + dx, sy + dy, col("#ffe9a8"))

# ------------------------- moon -------------------------
c.circle(55, 7, 5, col("#f8ecc8"))
c.set(53, 5, col("#e7cf9a"))
c.set(56, 8, col("#e7cf9a"))
c.set(54, 10, col("#e7cf9a"))
c.set(56, 4, col("#fdf6dd"))

# ------------------------- mountains -------------------------
# back range
c.poly([(0, 43), (14, 24), (28, 43), (28, 63), (0, 63)], col("#3a3370"))
c.poly([(20, 45), (38, 28), (52, 45), (52, 63), (20, 63)], col("#332c66"))
c.poly([(44, 43), (58, 25), (63, 49), (63, 63), (44, 63)], col("#3a3370"))
# snow caps
c.poly([(11, 30), (14, 24), (18, 30)], col("#d9e2ff"))
c.poly([(35, 34), (38, 28), (42, 34)], col("#cfd9f7"))
c.poly([(55, 31), (58, 25), (61, 31)], col("#d9e2ff"))
# near range
c.poly([(0, 52), (10, 40), (22, 52), (22, 63), (0, 63)], col("#251f4e"))
c.poly([(36, 56), (46, 42), (58, 56), (58, 63), (36, 63)], col("#1d173f"))
c.poly([(14, 54), (26, 43), (38, 54), (38, 63), (14, 63)], col("#1a1438"))
# ground
c.rect(0, 58, 64, 6, col("#161238"))
c.rect(0, 61, 64, 3, col("#0e0b24"))

# tiny pines
pine = col("#100c2c")
for (tx, ty) in [(3, 55), (59, 56)]:
    c.poly([(tx, ty), (tx - 1, ty + 2), (tx + 1, ty + 2)], pine)

# ------------------------- lettering -------------------------
SMALL = {
    "P": (".####", ".#..#", "####.", ".#...", ".#..."),
    "I": ("#####", "..#..", "..#..", "..#..", "#####"),
    "X": ("#...#", ".#.#.", "..#..", ".#.#.", "#...#"),
    "E": ("#####", "#....", "####.", "#....", "#####"),
    "L": ("#....", "#....", "#....", "#....", "#####"),
}
BIG = {
    "Q": (".#####.", "#.....#", "#.....#", "#.....#", "#.....#",
          "#..##.#", ".#..#..", "..##..."),
    "U": ("#.....#", "#.....#", "#.....#", "#.....#", "#.....#",
          "#.....#", "#.....#", ".#####."),
    "E": ("#######", "#......", "#......", "#####..", "#......",
          "#......", "#......", "#######"),
    "S": (".#####.", "#.....#", "#......", ".#####.", "......#",
          "......#", "#.....#", ".#####."),
    "T": ("#######",) + ("...#...",) * 7,
}


def stamp(glyph, gx, gy, color):
    for dy, row in enumerate(glyph):
        for dx, ch in enumerate(row):
            if ch == "#":
                c.set(gx + dx, gy + dy, color)


def word(glyphs, x0, y0, gap, fill_top, fill_bot, outline, shadow, split, sh):
    w = len(glyphs[0])
    # drop shadow (plain glyph offset)
    for gi, g in enumerate(glyphs):
        gx = x0 + (w + gap) * gi
        for dy, row in enumerate(g):
            for dx, ch in enumerate(row):
                if ch == "#":
                    c.set(gx + dx + sh[0], y0 + dy + sh[1], shadow)
    # outline: dilation — every glyph pixel plus its 8 neighbours
    for gi, g in enumerate(glyphs):
        gx = x0 + (w + gap) * gi
        for dy, row in enumerate(g):
            for dx, ch in enumerate(row):
                if ch == "#":
                    for ox in (-1, 0, 1):
                        for oy in (-1, 0, 1):
                            c.set(gx + dx + ox, y0 + dy + oy, outline)
    # fill (two-tone depth)
    for gi, g in enumerate(glyphs):
        gx = x0 + (w + gap) * gi
        for dy, row in enumerate(g):
            for dx, ch in enumerate(row):
                if ch == "#":
                    color = fill_bot if (split is not None and dy >= split) else fill_top
                    c.set(gx + dx, y0 + dy, color)


# --- word one: PIXEL (small, cyan) ---
pixel_letters = [SMALL[k] for k in "PIXEL"]
word(pixel_letters, 12, 7, 3,
     col("#45d9ff"), col("#2aa8e8"), col("#0c1a3a"), col((6, 8, 28, 235)),
     split=2, sh=(2, 2))

# --- sparkles flanking the middle ---
spark = col("#ffd24a")
for (dx, dy) in [(9, 17), (54, 17)]:
    for px, py in [(dx, dy - 1), (dx - 1, dy), (dx, dy), (dx + 1, dy), (dx, dy + 1)]:
        c.set(px, py, spark)

# --- word two: QUEST (large, gold) ---
quest_letters = [BIG[k] for k in "QUEST"]
word(quest_letters, 10, 24, 2,
     col("#ffe066"), col("#ffb81c"), col("#3a2008"), col((10, 8, 30, 240)),
     split=4, sh=(2, 3))

print(c.stats_text())
print(c.matrix_text((0, 0, 63, 63)))
print("PIXEL region (5,4)-(60,15):")
print(c.matrix_text((5, 4, 60, 15)))
print("QUEST region (8,21)-(61,36):")
print(c.matrix_text((8, 21, 61, 36)))
finish(c)
