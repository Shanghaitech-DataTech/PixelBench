# Seamless carpet pattern, 32x32, warm geometric motifs
# Approach: draw a 96x96 periodic field and crop the central 32x32 tile.

bg_dark = "#7A2F1A"
bg_light = "#8F4226"
cream = "#F0D4A2"
gold = "#D9A23F"
gold_light = "#F1CE85"
deep = "#5E1E12"
coral = "#C2603A"

M = 32
B = 96

big = new_canvas(B, B)

# Woven diagonal twill background, periodic with period 32.
for x in range(B):
    lx = (x - M) % 32
    for y in range(B):
        ly = (y - M) % 32
        t = ((lx + ly) // 2) % 2
        col = bg_light if t == 0 else bg_dark
        big.set(x, y, col)


def dpts(cx, cy, r):
    return [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]


def flower(c, x, y):
    # 8-petal rosette: coral orthogonal petals, pale-gold diagonal petals.
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        c.set(x + dx, y + dy, coral)
    for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        c.set(x + dx, y + dy, gold_light)
    c.set(x, y, deep)


def draw_corner(c, cx, cy):
    c.poly(dpts(cx, cy, 6), deep)
    c.poly(dpts(cx, cy, 4), cream)
    c.poly(dpts(cx, cy, 2), gold)
    c.set(cx, cy, deep)


def perimeter_point(cx, cy, R, t):
    # t in [0, 1), starting at the top vertex and moving clockwise.
    seg = t * 4.0
    i = int(seg)
    f = seg - i
    if i == 0:
        return (cx + R * f, cy - R + R * f)
    if i == 1:
        return (cx + R - R * f, cy + R * f)
    if i == 2:
        return (cx - R * f, cy + R - R * f)
    return (cx - R + R * f, cy - R * f)


def rnd(v):
    return int(v + 0.5)


def draw_main(c, cx, cy):
    R = 10
    # Concentric diamond bands: deep border, cream, gold, cream, deep center.
    c.poly(dpts(cx, cy, 10), deep)
    c.poly(dpts(cx, cy, 8), cream)
    c.poly(dpts(cx, cy, 6), gold)
    c.poly(dpts(cx, cy, 4), cream)
    c.poly(dpts(cx, cy, 2), deep)
    # Floral border: 8 rosettes around the diamond outline.
    for k in range(8):
        x, y = perimeter_point(cx, cy, R, k / 8.0)
        flower(c, rnd(x), rnd(y))
    # Small beaded dots halfway between the rosettes.
    for k in range(8):
        x, y = perimeter_point(cx, cy, R, (k + 0.5) / 8.0)
        c.set(rnd(x), rnd(y), gold_light)


# Draw all motifs that can touch the central crop tile.
for i in range(2):
    for j in range(2):
        draw_corner(big, M + 32 * i, M + 32 * j)
        draw_main(big, M + 16 + 32 * i, M + 16 + 32 * j)

# Crop the central 32x32 tile (periodic, so edges tile seamlessly).
sel = big.select(M, M, 32, 32)
result = new_canvas(32, 32)
sel.copy_to(0, 0, result)

print(result.stats_text())
print(result.matrix_text(region=(0, 0, 31, 31)))

finish(result)
