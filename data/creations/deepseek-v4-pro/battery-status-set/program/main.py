W, H = 64, 64
c = new_canvas(W, H, background=None, name="result")

# Palette
OUTLINE = c.color("#1e293b", name="outline")
GREEN   = c.color("#22c55e", name="green")
AMBER   = c.color("#f59e0b", name="amber")
RED     = c.color("#ef4444", name="red")
BLUE    = c.color("#3b82f6", name="blue")
BOLT    = c.color("#fde047", name="bolt")


def battery(x, fill_level=None, charging=False):
    """Draw one battery icon with a shared 2px outline.

    Body outer:  x..x+11, y=14..53  (12 x 40)
    Body cavity:  x+2..x+9, y=16..51 (8 x 36)
    Terminal nub: x+3..x+8, y=10..13 (6 x 4), sitting on the body
    """
    # Terminal nub (solid cap)
    c.rect(x + 3, 10, 6, 4, OUTLINE)

    # Body: solid block, then carve the inside out to leave a 2px border
    c.rect(x, 14, 12, 40, OUTLINE)
    c.rect(x + 2, 16, 8, 36, None)

    if charging:
        # Partial blue charge at the bottom, lightning bolt above it
        c.rect(x + 2, 42, 8, 10, BLUE)          # rows 42..51
        by = 18                                  # bolt top
        pts = [
            (x + 2 + 5, by + 0),
            (x + 2 + 0, by + 7),
            (x + 2 + 3, by + 7),
            (x + 2 + 1, by + 13),
            (x + 2 + 7, by + 5),
            (x + 2 + 4, by + 5),
        ]
        c.poly(pts, BOLT, fill=True)
    else:
        if fill_level == 1.0:
            c.rect(x + 2, 16, 8, 36, GREEN)      # full, rows 16..51
        elif fill_level == 0.6:
            c.rect(x + 2, 30, 8, 22, AMBER)      # ~61%, rows 30..51
        elif fill_level == 0.2:
            c.rect(x + 2, 45, 8, 7, RED)         # ~19%, rows 45..51


# Four icons in one horizontal row, equal spacing.
battery(2, fill_level=1.0)
battery(18, fill_level=0.6)
battery(34, fill_level=0.2)
battery(50, charging=True)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

finish(c)
