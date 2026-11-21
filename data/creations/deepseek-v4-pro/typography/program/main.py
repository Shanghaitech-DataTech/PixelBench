from pixelbench_api import *

# ---------- palette ----------
BG      = (18, 20, 40)      # deep indigo background
PANEL   = (28, 30, 58)      # banner panel
BORDER  = (70, 74, 116)     # panel border
GOLD    = (255, 204, 0)     # main title
GOLD_OL = (74, 42, 4)       # main title outline
SHADOW  = (7, 8, 18)        # drop shadow
CYAN    = (128, 224, 255)   # subtitle
CYAN_OL = (10, 42, 66)      # subtitle outline
STAR_A  = (255, 255, 255)
STAR_B  = (255, 214, 120)

# ---------- 5x7 pixel font ----------
GLYPHS = {
    'P': [
        ".###.",
        "#...#",
        "#...#",
        "####.",
        "#....",
        "#....",
        "#....",
    ],
    'I': [
        ".###.",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        ".###.",
    ],
    'X': [
        "#...#",
        "#...#",
        ".#.#.",
        "..#..",
        ".#.#.",
        "#...#",
        "#...#",
    ],
    'E': [
        "#####",
        "#....",
        "#....",
        "####.",
        "#....",
        "#....",
        "#####",
    ],
    'L': [
        "#....",
        "#....",
        "#....",
        "#....",
        "#....",
        "#....",
        "#####",
    ],
    'Q': [
        ".###.",
        "#...#",
        "#...#",
        "#...#",
        "#.#.#",
        ".##.#",
        "..##.",
    ],
    'U': [
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        ".###.",
    ],
    'S': [
        ".###.",
        "#...#",
        "#....",
        ".###.",
        "....#",
        "#...#",
        ".###.",
    ],
    'T': [
        "#####",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
    ],
}

# ---------- drawing helpers ----------
def draw_glyph(c, x, y, g, scale, color):
    for row, line in enumerate(g):
        for col, ch in enumerate(line):
            if ch == '#':
                c.rect(x + col * scale, y + row * scale, scale, scale, color, fill=True)


def draw_string(c, x, y, text, scale, color, spacing, outline_color=None, shadow_color=None, shadow_off=(2, 2)):
    pos = x
    for ch in text:
        g = GLYPHS[ch]
        if shadow_color is not None:
            draw_glyph(c, pos + shadow_off[0], y + shadow_off[1], g, scale, shadow_color)
        if outline_color is not None:
            for ox, oy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                draw_glyph(c, pos + ox, y + oy, g, scale, outline_color)
        draw_glyph(c, pos, y, g, scale, color)
        pos += 5 * scale + spacing


def text_width(text, scale, spacing):
    n = len(text)
    return n * 5 * scale + (n - 1) * spacing


def draw_diamond(c, cx, cy, r, color):
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if abs(dx) + abs(dy) <= r:
                c.set(cx + dx, cy + dy, color)


# ---------- canvas ----------
c = new_canvas(64, 64, background=BG, name="title")

# background stars
stars = [
    (5, 4, STAR_A), (20, 2, STAR_B), (38, 5, STAR_A), (55, 3, STAR_B),
    (8, 8, STAR_B), (60, 8, STAR_A), (30, 6, STAR_B), (48, 2, STAR_A),
    (4, 58, STAR_A), (59, 56, STAR_B),
]
for sx, sy, sc in stars:
    c.set(sx, sy, sc)

# banner behind the main title
c.rect(2, 12, 60, 20, PANEL, fill=True)
c.rect(2, 12, 60, 20, BORDER, fill=False)

# main title: PIXEL (large, 2x scale)
main_text = "PIXEL"
main_scale = 2
main_spacing = 2
main_x = (64 - text_width(main_text, main_scale, main_spacing)) // 2
draw_string(c, main_x, 15, main_text, main_scale, GOLD, main_spacing,
            outline_color=GOLD_OL, shadow_color=SHADOW, shadow_off=(2, 2))

# subtitle: QUEST (smaller, 1x scale)
sub_text = "QUEST"
sub_scale = 1
sub_spacing = 1
sub_x = (64 - text_width(sub_text, sub_scale, sub_spacing)) // 2
draw_string(c, sub_x, 45, sub_text, sub_scale, CYAN, sub_spacing,
            outline_color=CYAN_OL, shadow_color=SHADOW, shadow_off=(1, 1))

# small decorative diamonds flanking the subtitle
draw_diamond(c, 10, 48, 2, GOLD)
draw_diamond(c, 53, 48, 2, GOLD)
c.set(10, 46, STAR_A)
c.set(53, 46, STAR_A)

# ---------- report ----------
print(c.stats_text())
print(c.matrix_text(region=(0, 10, 63, 52)))

finish(c)
