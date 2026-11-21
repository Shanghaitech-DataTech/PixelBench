# ============================================================
#  PIXEL QUEST - 64x64 pixel-art game title screen
#  Hierarchy:  big two-line outlined title  >  small subtitle
# ============================================================
try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 64

# ---------------- palette ----------------
BG         = "#23234a"   # deep indigo night
BAND       = "#1b1b3c"   # dark ground silhouette
BAND_EDGE  = "#44448a"   # horizon highlight
INK        = "#000000"   # outline + drop shadow
CYAN_HI    = "#d8f6ff"
CYAN       = "#59c8f5"
CYAN_SH    = "#2b86c8"
GOLD_HI    = "#fff3bd"
GOLD       = "#ffc93c"
GOLD_SH    = "#d1861f"
WHITE      = "#ffffff"
BLUE       = "#7fb4ff"
BRACKET    = "#7d7dc9"
BRACKET_HI = "#c3c3f5"
SUB        = "#e9e9ff"

# ---------------- 5x7 title glyphs ----------------
FONT5 = {
    'P': ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    'I': [".###.", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    'X': ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    'E': ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    'L': ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    'Q': [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    'U': ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    'S': [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    'T': ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
}

# ---------------- 3x5 subtitle glyphs ----------------
FONT3 = {
    'P': ["##.", "#.#", "##.", "#..", "#.."],
    'R': ["##.", "#.#", "##.", "#.#", "#.#"],
    'E': ["###", "#..", "##.", "#..", "###"],
    'S': [".##", "#..", ".#.", "..#", "##."],
    'T': ["###", ".#.", ".#.", ".#.", ".#."],
    'A': [".#.", "#.#", "###", "#.#", "#.#"],
    ' ': ["...", "...", "...", "...", "..."],
}

# ---------------- helpers ----------------
def plot(cv, glyph, x, y, s, colfn):
    """Stamp a glyph with s*s blocks, colour chosen per glyph row."""
    for ry, row in enumerate(glyph):
        col = colfn(ry)
        for rx, ch in enumerate(row):
            if ch == '#':
                cv.rect(x + rx * s, y + ry * s, s, s, col)

def draw_letter(cv, glyph, x, y, s, colfn, sdx=3, sdy=3):
    plot(cv, glyph, x + sdx, y + sdy, s, lambda r: INK)      # drop shadow
    for dx in (-1, 0, 1):                                     # 1px outline ring
        for dy in (-1, 0, 1):
            if dx or dy:
                plot(cv, glyph, x + dx, y + dy, s, lambda r: INK)
    plot(cv, glyph, x, y, s, colfn)                           # face

def draw_word5(cv, word, x, y, s, sp, colfn):
    cx = x
    for ch in word:
        draw_letter(cv, FONT5[ch], cx, y, s, colfn)
        cx += 5 * s + sp
    return cx - sp

def draw_word3(cv, word, x, y, colfn, sp=1):
    cx = x
    for ch in word:
        g = FONT3[ch]
        plot(cv, g, cx + 1, y + 1, 1, lambda r: INK)          # tiny shadow
        plot(cv, g, cx, y, 1, colfn)
        cx += 3 + sp
    return cx - sp

# ---------------- canvas ----------------
c = new_canvas(W, H, background=BG, name="pixel_quest_title")

# ground band (horizon at the bottom)
c.rect(0, 59, 64, 1, BAND_EDGE)
c.rect(0, 60, 64, 4, BAND)

# scattered stars
STARS = [(9, 4, WHITE), (17, 2, BLUE), (25, 5, WHITE), (38, 3, BLUE),
         (46, 5, WHITE), (54, 2, BLUE), (5, 45, BLUE), (58, 45, WHITE),
         (8, 56, WHITE), (16, 54, BLUE), (26, 57, GOLD), (40, 55, BLUE),
         (50, 57, WHITE), (57, 54, GOLD)]
for x, y, col in STARS:
    c.set(x, y, col)

# corner brackets (viewfinder frame)
def bracket(x0, y0, sx, sy):
    for i in range(5):
        c.set(x0 + sx * i, y0, BRACKET)
        c.set(x0, y0 + sy * i, BRACKET)
    c.set(x0, y0, BRACKET_HI)
bracket(2, 2, 1, 1)
bracket(61, 2, -1, 1)
bracket(2, 61, 1, -1)
bracket(61, 61, -1, -1)

# sparkle above the title
tx, ty = 31, 4
for dx, dy in ((0, -2), (0, 2), (-2, 0), (2, 0), (0, -1), (0, 1), (-1, 0), (1, 0)):
    c.set(tx + dx, ty + dy, WHITE)
c.set(tx, ty, GOLD)

# ---------------- the lettering ----------------
cyanfn = lambda r: CYAN_HI if r < 2 else (CYAN if r < 5 else CYAN_SH)
goldfn = lambda r: GOLD_HI if r < 2 else (GOLD if r < 5 else GOLD_SH)

draw_word5(c, "PIXEL", 5, 8, 2, 1, cyanfn)     # face x=5-58, outline 4-59
draw_word5(c, "QUEST", 5, 28, 2, 1, goldfn)    # face x=5-58, outline 4-59

subfn = lambda r: SUB
draw_word3(c, "PRESS START", 10, 48, subfn)    # rows 48-52

# small gold diamonds flanking the subtitle
for dx in (5, 58):
    c.set(dx, 49, GOLD); c.set(dx, 51, GOLD)
    c.set(dx - 1, 50, GOLD); c.set(dx + 1, 50, GOLD)
    c.set(dx, 50, GOLD_HI)

# ---------------- report ----------------
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 64, 32)))
print(c.matrix_text(region=(0, 32, 64, 64)))

finish(c)
