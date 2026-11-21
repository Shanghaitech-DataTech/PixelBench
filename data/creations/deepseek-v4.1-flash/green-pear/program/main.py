W = H = 32
c = new_canvas(W, H, name="pear")

OUT = c.color("#17301c", "outline")
DARK = c.color("#2c5c2d", "dark")
MID = c.color("#4e943e", "mid")
LIGHT = c.color("#7cc24f", "light")
HI = c.color("#b7e87a", "highlight")
STEM = c.color("#7a5232", "stem")

# Body silhouette: y -> inclusive (x0, x1).  One pixel shift down for framing.
spans = {
    5: (15, 17),
    6: (14, 18), 7: (14, 18),
    8: (13, 19), 9: (13, 19),
    10: (12, 20), 11: (12, 20),
    12: (11, 21), 13: (11, 21),
    14: (10, 22), 15: (10, 22),
    16: (9, 23), 17: (9, 23),
    18: (8, 24), 19: (8, 24),
    20: (7, 25), 21: (7, 25), 22: (7, 25), 23: (7, 25),
    24: (8, 24), 25: (8, 24),
    26: (9, 23), 27: (10, 22),
    28: (12, 20), 29: (14, 18),
}

# specular highlight columns (offsets "d" from the left edge) per row
hi_cols = {17: (1, 2), 18: (1, 2), 19: (1, 2, 3),
           20: (1, 2), 21: (1, 2), 22: (1,)}


def shade(y, d, e):
    if d == 0 or e == 0:
        return OUT
    if y >= 27:
        return DARK
    if e <= 2 and d > 2:
        return DARK
    if d in hi_cols.get(y, ()):
        return HI
    if d <= 3:
        return LIGHT
    if e <= 3:
        return DARK
    return MID


for y in sorted(spans):
    x0, x1 = spans[y]
    for x in range(x0, x1 + 1):
        c.set(x, y, shade(y, x - x0, x1 - x))

# stem
for (x, y) in [(16, 2), (17, 2), (16, 3), (17, 3), (16, 4)]:
    c.set(x, y, STEM)

# leaf
leaf = {
    (22, 1): LIGHT, (23, 1): LIGHT, (24, 1): MID,
    (20, 2): LIGHT, (21, 2): LIGHT, (22, 2): MID, (23, 2): MID,
    (18, 3): LIGHT, (19, 3): MID, (20, 3): MID, (21, 3): MID, (22, 3): DARK,
    (18, 4): MID, (19, 4): DARK,
}
for (x, y), col in leaf.items():
    c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text(region=(5, 0, 28, 31)))

save("pear", c)
finish(c)
