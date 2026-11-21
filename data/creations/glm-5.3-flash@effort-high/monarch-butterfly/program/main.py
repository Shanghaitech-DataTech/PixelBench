# Monarch butterfly, 32x32, transparent background, wings spread
# Left wing designed as explicit per-row spans; span() mirrors to the right.
# Body is centred on x=15/16.
c = new_canvas(32, 32, name="monarch")

ORANGE = "#E87A10"
BLACK  = "#1A1A1A"
DARK   = "#3A2415"
WHITE  = "#FFF6E8"

g = [[None] * 32 for _ in range(32)]


def span(y, x0, x1, col=BLACK):
    """Horizontal run on the left side, mirrored to the right."""
    for x in range(x0, x1 + 1):
        g[y][x] = col
        g[y][31 - x] = col


def px(x, y, col=BLACK):
    g[y][x] = col
    g[y][31 - x] = col


def line(x0, y0, x1, y1, col=BLACK):
    """1 px Bresenham vein, mirrored."""
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        g[y][x] = col
        g[y][31 - x] = col
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


# ================= HINDWING (painted first, behind the forewing) ============
for y, x0, x1 in [
    (17, 7, 15), (18, 5, 15), (19, 4, 15), (20, 3, 15), (21, 3, 15),
    (22, 3, 15), (23, 4, 15), (24, 5, 15), (25, 6, 15), (26, 8, 15),
    (27, 10, 15),
]:
    span(y, x0, x1)
for y, x0, x1 in [
    (18, 8, 14), (19, 6, 14), (20, 5, 14), (21, 5, 14), (22, 5, 14),
    (23, 6, 14), (24, 7, 14), (25, 8, 14), (26, 10, 14),
]:
    span(y, x0, x1, ORANGE)

# hindwing veins fanning from the root
line(14, 20, 7, 20)
line(14, 23, 8, 23)

# white spots in the hindwing black border
for (x, y) in [(6, 18), (4, 19), (3, 21), (4, 23), (6, 25), (8, 26),
               (11, 27), (13, 27)]:
    px(x, y, WHITE)

# ================= FOREWING (painted on top) ================================
for y, x0, x1 in [
    (4, 4, 6), (5, 2, 13), (6, 1, 14), (7, 1, 14), (8, 1, 14),
    (9, 1, 14), (10, 1, 14), (11, 1, 14), (12, 2, 14), (13, 3, 14),
    (14, 4, 14), (15, 6, 14), (16, 8, 14), (17, 10, 14),
]:
    span(y, x0, x1)
for y, x0, x1 in [
    (5, 8, 11), (6, 5, 13), (7, 4, 13), (8, 3, 13), (9, 3, 13),
    (10, 3, 13), (11, 3, 13), (12, 4, 13), (13, 5, 13), (14, 6, 13),
    (15, 8, 13), (16, 10, 13),
]:
    span(y, x0, x1, ORANGE)

# forewing veins fanning from the root
line(14, 7, 7, 5)
line(14, 11, 4, 11)
line(14, 13, 5, 14)

# white spots: diagonal band across the black apex + dotted outer margin
for (x, y) in [(6, 4), (4, 5), (2, 6), (1, 8), (1, 10), (2, 12),
               (3, 13), (4, 14), (6, 15), (8, 16)]:
    px(x, y, WHITE)

# ================= BODY =====================================================
for y in range(5, 8):
    span(y, 14, 15)              # head, x=14..17
for y in range(8, 26):
    span(y, 15, 15)              # thorax + abdomen, x=15..16
span(26, 15, 15, DARK)           # abdomen tip
span(27, 15, 15, DARK)

# eyes
px(17, 6, WHITE)
# white polka dots down the abdomen
for y in (11, 15, 19, 23):
    px(16, y, WHITE)

# ================= ANTENNAE =================================================
px(17, 4)
px(18, 3)
px(19, 2)
px(20, 1)
px(21, 1)                        # club

# ---- commit ----
for y in range(32):
    for x in range(32):
        if g[y][x] is not None:
            c.set(x, y, g[y][x])

# nudge down 1 px so the 27-row drawing sits centred in the 32-row canvas
c.shift(0, 1)

print(c.stats_text())
save("monarch-butterfly", c)
finish(c)
