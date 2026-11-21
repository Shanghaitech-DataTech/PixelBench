# Battery status set: 100%, 60%, 20%, charging
W = H = 64
c = new_canvas(W, H, background=None, name="battery_status_set")

# Shared outline / metal colours
BLACK      = "#10131c"
RIM        = "#4e566e"
RIM_LIGHT  = "#7b86a2"
RIM_DARK   = "#323848"
CAVITY     = "#1a1e29"
CAVITY_TOP = "#0d1017"
CAVITY_LEFT= "#11151e"
LABEL      = "#10131c"

# Per-state fill palettes: (base, light, dark)
GREEN  = ("#2ecc71", "#8ef7b0", "#1f8f4d")
AMBER  = ("#f5b82e", "#ffe38a", "#b07a12")
RED    = ("#e74c3c", "#ff9b89", "#9e2a20")
CYAN   = ("#19b5e8", "#7fe5ff", "#0b6e8f")
BOLT         = "#ffd84a"
BOLT_LIGHT   = "#fff4b0"
BOLT_OUTLINE = "#0a0c10"

BODY_Y = 13
BODY_H = 32
CAVITY_Y = 15
CAVITY_H = 28
FILL_BOTTOM = 42
LABEL_Y = 49


def rounded_rect(c, x, y, w, h, col):
    # one-pixel corner cuts, filled rounded rectangle
    c.rect(x + 1, y, w - 2, 1, col)
    c.rect(x, y + 1, w, h - 2, col)
    c.rect(x + 1, y + h - 1, w - 2, 1, col)


def draw_battery_common(c, bx):
    """Draw the identical battery shell, nub and dark cavity."""
    # Terminal nub: black outline, metal centre
    c.rect(bx + 4, 9, 6, 4, BLACK)
    c.rect(bx + 5, 10, 4, 2, RIM)
    c.rect(bx + 5, 10, 4, 1, RIM_LIGHT)
    c.rect(bx + 5, 11, 4, 1, RIM_DARK)

    # Body shell
    rounded_rect(c, bx, BODY_Y, 14, BODY_H, BLACK)
    rounded_rect(c, bx + 1, BODY_Y + 1, 12, BODY_H - 2, RIM)

    # Metal rim highlights / shading
    c.rect(bx + 2, BODY_Y + 1, 10, 1, RIM_LIGHT)      # top rim
    c.rect(bx + 1, BODY_Y + 2, 1, BODY_H - 4, RIM_LIGHT)  # left rim
    c.rect(bx + 12, BODY_Y + 2, 1, BODY_H - 4, RIM_DARK)  # right rim
    c.rect(bx + 2, BODY_Y + BODY_H - 1, 10, 1, RIM_DARK)  # bottom rim

    # Dark cavity with a little inner shading
    c.rect(bx + 2, CAVITY_Y, 10, CAVITY_H, CAVITY)
    c.rect(bx + 2, CAVITY_Y, 10, 1, CAVITY_TOP)
    c.rect(bx + 2, CAVITY_Y + 1, 1, CAVITY_H - 1, CAVITY_LEFT)


def draw_fill(c, bx, top, palette):
    """Fill from the bottom up to top (inclusive)."""
    base, light, dark = palette
    x = bx + 2
    h = FILL_BOTTOM - top + 1
    c.rect(x, top, 10, h, base)
    # bright electrolyte line at the current level
    c.rect(x, top, 10, 1, light)
    # glossy left side and shaded right side
    if h > 1:
        c.rect(bx + 3, top + 1, 2, h - 1, light)
        c.rect(bx + 10, top + 1, 1, h - 1, dark)


BOLT_PIXELS = [
    (4, 0), (5, 0),
    (3, 1), (4, 1),
    (2, 2), (3, 2),
    (1, 3), (2, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
    (3, 5), (4, 5), (5, 5),
    (3, 6), (4, 6),
    (2, 7), (3, 7),
    (1, 8), (2, 8),
    (0, 9), (1, 9),
]
BOLT_HIGHLIGHT = [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4), (1, 4), (2, 4), (3, 5)]


BOLT_OUTLINE_PIXELS = sorted({
    (dx + ox, dy + oy)
    for dx, dy in BOLT_PIXELS
    for ox in (-1, 0, 1)
    for oy in (-1, 0, 1)
    if (dx + ox, dy + oy) not in BOLT_PIXELS
})


def draw_bolt(c, x, y):
    # crisp one-pixel dark outline makes the bolt readable over both cavity and fill
    for dx, dy in BOLT_OUTLINE_PIXELS:
        c.set(x + dx, y + dy, BOLT_OUTLINE)
    for dx, dy in BOLT_PIXELS:
        c.set(x + dx, y + dy, BOLT)
    for dx, dy in BOLT_HIGHLIGHT:
        c.set(x + dx, y + dy, BOLT_LIGHT)


FONT4 = {
    "0": ("1111", "1001", "1001", "1001", "1111"),
    "1": ("0100", "1100", "0100", "0100", "1111"),
    "2": ("1111", "0001", "1111", "1000", "1111"),
    "3": ("1111", "0001", "1111", "0001", "1111"),
    "4": ("1001", "1001", "1111", "0001", "0001"),
    "5": ("1111", "1000", "1111", "0001", "1111"),
    "6": ("1111", "1000", "1111", "1001", "1111"),
    "7": ("1111", "0001", "0010", "0100", "0100"),
    "8": ("1111", "1001", "1111", "1001", "1111"),
    "9": ("1111", "1001", "1111", "0001", "1111"),
    "C": ("1111", "1000", "1000", "1000", "1111"),
    "H": ("1001", "1001", "1111", "1001", "1001"),
    "G": ("1111", "1000", "1011", "1001", "1111"),
}


def draw_label(c, x, y, s, col):
    for ch in s:
        glyph = FONT4[ch]
        for row_i, row in enumerate(glyph):
            for col_i, bit in enumerate(row):
                if bit == "1":
                    c.set(x + col_i, y + row_i, col)
        x += 5


# ---------------------------------------------------------------------------
# Four identical batteries, left to right
# ---------------------------------------------------------------------------
positions = [1, 17, 33, 49]

# 100% - full green
bx = positions[0]
draw_battery_common(c, bx)
draw_fill(c, bx, CAVITY_Y, GREEN)
draw_label(c, bx, LABEL_Y, "100", LABEL)

# 60% - 17 of 28 cavity rows
bx = positions[1]
draw_battery_common(c, bx)
draw_fill(c, bx, 26, AMBER)
draw_label(c, bx + 2, LABEL_Y, "60", LABEL)

# 20% - 6 of 28 cavity rows
bx = positions[2]
draw_battery_common(c, bx)
draw_fill(c, bx, 37, RED)
draw_label(c, bx + 2, LABEL_Y, "20", LABEL)

# Charging - partial cyan fill plus a bright lightning bolt
bx = positions[3]
draw_battery_common(c, bx)
draw_fill(c, bx, 32, CYAN)
draw_bolt(c, bx + 4, 24)
draw_label(c, bx, LABEL_Y, "CHG", LABEL)

result = c
print(c.stats_text())

save("battery_status_set", c)
finish(result)
