c = new_canvas(32, 32, name="monarch_butterfly")

BLACK = "#17131a"
ORANGE = "#f58a24"
GOLD = "#ffb52e"
CREAM = "#fff1d1"

# Broad forewings and rounded hindwings, with a dark pixel-art silhouette.
fore = [(15, 8), (12, 6), (8, 3), (4, 2), (2, 4), (3, 8), (2, 12), (4, 16), (7, 18), (11, 17), (15, 14)]
hind = [(15, 14), (11, 17), (8, 19), (6, 22), (7, 25), (10, 27), (13, 26), (15, 23)]
for pts in (fore, hind):
    c.poly(pts, BLACK)
    c.poly([(31-x, y) for x, y in pts], BLACK)

# Orange fields inset from the heavy outer edge.
c.poly([(14, 9), (11, 7), (8, 5), (5, 4), (4, 6), (5, 9), (4, 12), (6, 15), (9, 16), (12, 15), (14, 13)], ORANGE)
c.poly([(17, 9), (20, 7), (23, 5), (26, 4), (27, 6), (26, 9), (27, 12), (25, 15), (22, 16), (19, 15), (17, 13)], ORANGE)
c.poly([(14, 15), (11, 18), (9, 20), (8, 22), (9, 24), (11, 25), (13, 24), (14, 21)], GOLD)
c.poly([(17, 15), (20, 18), (22, 20), (23, 22), (22, 24), (20, 25), (18, 24), (17, 21)], GOLD)

# Veins radiate from the body, separating the orange panels.
for x in (14, 17):
    c.line(x, 10, x, 20, BLACK)
c.line(14, 12, 5, 5, BLACK)
c.line(14, 14, 4, 11, BLACK)
c.line(14, 16, 7, 17, BLACK)
c.line(14, 18, 9, 22, BLACK)
c.line(17, 12, 26, 5, BLACK)
c.line(17, 14, 27, 11, BLACK)
c.line(17, 16, 24, 17, BLACK)
c.line(17, 18, 22, 22, BLACK)

# Light spots along the scalloped wing edges.
for x, y in [(4,5), (3,8), (4,13), (6,16), (8,18), (8,23), (11,26),
             (27,5), (28,8), (27,13), (25,16), (23,18), (23,23), (20,26)]:
    c.set(x, y, CREAM)
    if y in (5, 8, 13):
        c.set(x, y+1, CREAM)

# Segmented body and curved antennae.
c.ellipse(15, 15, 1, 7, BLACK)
c.rect(15, 10, 2, 11, BLACK)
c.line(15, 10, 12, 7, BLACK)
c.line(16, 10, 19, 7, BLACK)
c.set(11, 6, BLACK)
c.set(20, 6, BLACK)
for y in (13, 16, 19):
    c.line(15, y, 16, y, ORANGE)

print(c.stats_text())
finish(c)
