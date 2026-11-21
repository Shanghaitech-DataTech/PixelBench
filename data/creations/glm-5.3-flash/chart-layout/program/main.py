# ============================================================
#  Fruit bar chart - 128x64 pixel art
#  apple 10 | banana 5 | orange 7 | lemon 14 | grape 2
#  Mini pixel-art fruit icons stand beside the chart
#  instead of text labels.
# ============================================================

W, H = 128, 64
c = new_canvas(W, H, background="#1a1c2c", name="fruit_chart")

# ---------------- palette ----------------
C_BG   = c.color("#1a1c2c", "bg")
C_GRID = c.color("#333c57", "grid")
C_MID  = c.color("#566c86", "mid")
C_AXIS = c.color("#94b0c2", "axis")
C_STEM = c.color("#7a4a2b", "stem")
C_LEAF = c.color("#38b764", "leaf")

# ---------------- 9x9 fruit icons ----------------
APPLE = [
    "....t....",
    "....t....",
    "....tgg..",
    "...rrr...",
    "..rRrrr..",
    ".rRrrrrr.",
    ".rrrrrrr.",
    "..rrrrr..",
    "...ddd...",
]
BANANA = [
    ".........",
    "......yk.",
    ".....Yyy.",
    "....Yyy..",
    "...Yyy...",
    "..Yyy....",
    ".Yyy.....",
    "kyy......",
    ".........",
]
ORANGE = [
    ".....gg..",
    "....w....",
    "..ooooo..",
    ".ooOOooo.",
    "ooOOooooo",
    "ooooooooo",
    "ooooooooo",
    ".ooooooo.",
    "..ddddd..",
]
LEMON = [
    ".........",
    ".........",
    "..lllll..",
    ".lLLllll.",
    "lllllllll",
    ".lllllll.",
    "..ddddd..",
    ".........",
    ".........",
]
GRAPE = [
    "....wgg..",
    "....w....",
    ".Pp.Pp.Pp",
    ".pp.pp.pp",
    "..Pp.pp..",
    "..pp.pp..",
    "...Pp....",
    "...pp....",
    ".........",
]

# name, value, icon, colours (m = main, h = highlight, s/d = shade)
FRUITS = [
    ("apple", 10, APPLE,
     {"m": c.color("#e43b44", "apple"),
      "r": c.color("#e43b44", "apple"),
      "R": c.color("#ff7678", "apple_hi"),
      "d": c.color("#ab2334", "apple_lo"),
      "s": c.color("#ab2334", "apple_lo"),
      "g": C_LEAF,
      "t": C_STEM,
      "h": c.color("#ff7678", "apple_hi")}),
    ("banana", 5, BANANA,
     {"m": c.color("#ffcd75", "banana"),
      "y": c.color("#ffcd75", "banana"),
      "Y": c.color("#ffe6a3", "banana_hi"),
      "k": c.color("#8a5a2b", "banana_tip"),
      "s": c.color("#d99a3d", "banana_lo"),
      "h": c.color("#ffe6a3", "banana_hi")}),
    ("orange", 7, ORANGE,
     {"m": c.color("#f77622", "orange"),
      "o": c.color("#f77622", "orange"),
      "O": c.color("#ffa044", "orange_hi"),
      "d": c.color("#bf5315", "orange_lo"),
      "s": c.color("#bf5315", "orange_lo"),
      "g": C_LEAF,
      "w": C_STEM,
      "h": c.color("#ffa044", "orange_hi")}),
    ("lemon", 14, LEMON,
     {"m": c.color("#f4ef5e", "lemon"),
      "l": c.color("#f4ef5e", "lemon"),
      "L": c.color("#fbf9a5", "lemon_hi"),
      "d": c.color("#c9bd2e", "lemon_lo"),
      "s": c.color("#c9bd2e", "lemon_lo"),
      "h": c.color("#fbf9a5", "lemon_hi")}),
    ("grape", 2, GRAPE,
     {"m": c.color("#9b4a9e", "grape"),
      "p": c.color("#9b4a9e", "grape"),
      "P": c.color("#c479c9", "grape_hi"),
      "d": c.color("#6d2c72", "grape_lo"),
      "s": c.color("#6d2c72", "grape_lo"),
      "g": C_LEAF,
      "w": C_STEM,
      "h": c.color("#c479c9", "grape_hi")}),
]

# ---------------- geometry ----------------
X0     = 11      # bars start here (axis line sits at x=10)
SCALE  = 8       # pixels per unit  -> lemon (14) spans 112 px
BAR_H  = 7
ROWS   = [6, 17, 28, 39, 50]   # top row of each bar


def stamp(cv, ox, oy, rows, cmap):
    """Draw a little character-grid sprite."""
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            col = cmap.get(ch)
            if col is not None:
                cv.set(ox + i, oy + j, col)


# ---------------- gridlines (behind the bars) ----------------
for k in range(1, 8):                      # every 2 units = 16 px
    gx = X0 + SCALE * 2 * k
    for gy in range(5, 59):
        if gy % 2 == 0:                    # dotted
            c.set(gx, gy, C_GRID)

# ---------------- axes and ticks ----------------
c.rect(10, 4, 1, 56, C_AXIS)               # vertical axis  x=10, y=4..59
c.rect(10, 59, 115, 1, C_AXIS)             # horizontal axis y=59
for k in range(1, 8):
    c.rect(X0 + SCALE * 2 * k, 60, 1, 2, C_MID)

# ---------------- bars + icon labels ----------------
for (name, val, icon, cmap), y in zip(FRUITS, ROWS):
    w = val * SCALE
    c.rect(X0, y, w, BAR_H, cmap["m"])                 # body
    c.rect(X0, y, w, 1, cmap["h"])                     # lit top edge
    c.rect(X0, y + BAR_H - 1, w, 1, cmap["s"])         # shaded bottom
    c.rect(X0 + 2, y + 2, 2, 2, cmap["h"])             # shine block
    c.rect(X0 + w - 1, y + 1, 1, BAR_H - 2, cmap["s"]) # shaded end
    stamp(c, 1, y - 1, icon, cmap)                     # icon label

# ---------------- tiny "chart" glyph, top-left ----------------
c.rect(1, 4, 8, 1, C_MID)                  # baseline
c.rect(2, 2, 1, 2, C_AXIS)
c.rect(4, 1, 1, 3, C_AXIS)
c.rect(6, 0, 1, 4, C_AXIS)

# ---------------- report ----------------
print(c.stats_text())
for (name, val, icon, cmap), y in zip(FRUITS, ROWS):
    print("--- icon:", name, "---")
    print(c.matrix_text(region=(0, y - 1, 10, y + 7)))

print("=== corner glyph ===")
print(c.matrix_text(region=(0, 0, 12, 6)))
print("=== bar right ends ===")
print(c.matrix_text(region=(110, 5, 127, 58)))

save("fruit_bar_chart", c)
finish(c)
