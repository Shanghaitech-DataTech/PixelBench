from pixelbench_api import new_canvas, finish

OUTLINE = "#1d4f1c"
BASE = "#6fbf45"
SHADE = "#3d8b2e"
LIGHT = "#a9e06a"
STEM = "#8a5a2b"
STEM_DARK = "#563511"

c = new_canvas(32, 32, name="pear")

# pear silhouette rows: (y, x0, x1) inclusive -> outline
rows = [
    (5, 14, 18), (6, 13, 19), (7, 12, 20), (8, 11, 21), (9, 10, 21),
    (10, 9, 21), (11, 9, 21), (12, 8, 22), (13, 7, 23), (14, 7, 23),
    (15, 6, 24), (16, 6, 24), (17, 6, 24), (18, 6, 24), (19, 6, 24),
    (20, 6, 24), (21, 6, 24), (22, 7, 24), (23, 7, 24), (24, 8, 23),
    (25, 9, 23), (26, 10, 22), (27, 12, 20), (28, 14, 19),
]

# body outline, then inset base
for y, x0, x1 in rows:
    c.rect(x0, y, x1 - x0 + 1, 1, OUTLINE)
for y, x0, x1 in rows:
    if x1 - x0 + 1 >= 3:
        c.rect(x0 + 1, y, x1 - x0 - 1, 1, BASE)

# stem
stem_rows = [(0, 15, 15), (1, 14, 16), (2, 13, 16), (3, 14, 16), (4, 14, 16), (5, 14, 15)]
for y, x0, x1 in stem_rows:
    c.rect(x0, y, x1 - x0 + 1, 1, STEM_DARK)
    if x1 - x0 + 1 >= 3:
        c.rect(x0 + 1, y, x1 - x0 - 1, 1, STEM)

# small leaf to the right of the stem
c.ellipse(19, 3, 2, 2, BASE)
c.ellipse(19, 3, 2, 2, OUTLINE, fill=False)
c.line(20, 2, 18, 4, OUTLINE)

# shade: right side
for y, x0, x1 in rows:
    if 8 <= y <= 25:
        c.rect(x1 - 2, y, 2, 1, SHADE)
# shade: bottom band
for y, x0, x1 in rows:
    if y >= 24:
        c.rect(x0 + 1, y, x1 - x0 - 1, 1, SHADE)

# highlight: left band
for y, x0, x1 in rows:
    if 10 <= y <= 16:
        c.rect(x0 + 2, y, 4, 1, LIGHT)
    if y in (13, 14):
        c.rect(x0 + 3, y, 2, 1, LIGHT)

print(c.stats_text())
for y in range(0, 30):
    xs = [x for x in range(32) if c.get(x, y) != 0]
    if xs:
        print(y, xs[0], xs[-1], len(xs))
finish(c)
