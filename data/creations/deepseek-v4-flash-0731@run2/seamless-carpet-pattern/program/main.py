from pixelbench_api import new_canvas, finish, save

W = H = 32
c = new_canvas(W, H, name="carpet")

CREAM_L = c.color("#F4E7C8", "cream_l")
CREAM_D = c.color("#E6D2A6", "cream_d")
MAROON  = c.color("#7E2B28", "maroon")
RED     = c.color("#A63D2E", "red")
TERRA   = c.color("#C9633C", "terra")
GOLD   = c.color("#D9A441", "gold")
BROWN  = c.color("#4A2A1C", "brown")
OLIVE  = c.color("#66703C", "olive")


def weave(x0, y0, x1, y1, a, b):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            c.set(x, y, a if (x + y) % 2 == 0 else b)


def diamond(cx, cy, rx, ry, col, fill=True):
    c.poly([(cx, cy - ry), (cx + rx, cy), (cx, cy + ry), (cx - rx, cy)], col, fill=fill)


def blossom(cx, cy):
    # 5x5 floral blossom: center, petals, leaves, tips
    for dx, dy in [(0, -2), (2, 0), (0, 2), (-2, 0)]:
        c.set(cx + dx, cy + dy, GOLD)
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        c.set(cx + dx, cy + dy, OLIVE)
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        c.set(cx + dx, cy + dy, TERRA)
    c.set(cx, cy, BROWN)


# --- woven ground ---
weave(0, 0, 31, 31, CREAM_L, CREAM_D)

# --- border bands (woven red/maroon frame) ---
weave(0, 2, 31, 4, MAROON, RED)
weave(0, 27, 31, 29, MAROON, RED)
weave(2, 0, 4, 31, MAROON, RED)
weave(27, 0, 29, 31, MAROON, RED)

# --- gold guard lines ---
c.line(0, 5, 31, 5, GOLD)
c.line(0, 26, 31, 26, GOLD)
c.line(5, 0, 5, 31, GOLD)
c.line(26, 0, 26, 31, GOLD)

# --- diamond chain along the border (period 4 -> seamless) ---
for x in range(0, 32, 4):
    diamond(x, 3, 2, 1, GOLD)
    c.set(x, 3, RED)
    diamond(x, 28, 2, 1, GOLD)
    c.set(x, 28, RED)
for y in range(0, 32, 4):
    diamond(3, y, 1, 2, GOLD)
    c.set(3, y, RED)
    diamond(28, y, 1, 2, GOLD)
    c.set(28, y, RED)

# --- wrap the border diamonds that straddle the tile seam (seamless tiling) ---
for wx in [(30, 3), (31, 3), (30, 28), (31, 28), (3, 30), (3, 31), (28, 30), (28, 31)]:
    c.set(wx[0], wx[1], GOLD)

# --- central diamond medallion ---
diamond(16, 16, 6, 6, MAROON)
diamond(16, 16, 5, 5, RED)
diamond(16, 16, 4, 4, GOLD)
diamond(16, 16, 2, 2, TERRA)
diamond(16, 16, 1, 1, BROWN)
c.set(16, 16, GOLD)

# --- floral blossoms at the field corners ---
for px, py in [(8, 8), (24, 8), (8, 24), (24, 24)]:
    blossom(px, py)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
save("carpet", c)
finish(c)
