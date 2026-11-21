from pixelbench_api import new_canvas, view, finish

# 32x32 closed leather spellbook, transparent background.
result = new_canvas(32, 32, background=None, name="leather-spellbook")

OUTLINE = "#21181b"
DEEP = "#3a1f1d"
LEATHER = "#6b3528"
LIGHT = "#a85a38"
HILITE = "#d0824e"
METAL_DARK = "#8b6735"
GOLD = "#d4a64a"
PAGES = "#d5b77a"

# Overall book silhouette and visible page block.
result.poly([(7, 3), (23, 4), (27, 7), (28, 24), (25, 27),
             (10, 30), (5, 27), (4, 8)], OUTLINE)
result.poly([(9, 7), (24, 7), (26, 9), (27, 23), (24, 25),
             (10, 28), (7, 26), (7, 10)], PAGES)
# Page-edge shadows and individual page lines.
result.line(10, 26, 24, 23, METAL_DARK)
result.line(10, 28, 24, 25, METAL_DARK)
result.line(25, 10, 26, 22, METAL_DARK)
result.set(15, 26, PAGES).set(20, 25, PAGES)
result.line(13, 27, 20, 26, DEEP)
result.line(22, 25, 24, 24, DEEP)

# Front leather cover.
result.poly([(7, 3), (23, 4), (26, 7), (27, 22), (24, 24),
             (9, 27), (5, 24), (5, 8)], DEEP)
result.poly([(9, 5), (22, 6), (24, 8), (25, 21), (23, 22),
             (10, 25), (8, 23), (8, 8)], LEATHER)
# Warm worn center panel.
result.poly([(11, 7), (21, 8), (23, 10), (23, 19), (21, 21),
             (11, 23), (10, 21), (10, 10)], LIGHT)
result.line(12, 8, 20, 9, HILITE)
result.set(11, 10, HILITE).set(11, 11, HILITE)
result.line(12, 22, 20, 20, LEATHER)
result.set(22, 19, LEATHER)

# Thick raised spine on the left.
result.poly([(6, 5), (10, 6), (11, 8), (11, 22), (9, 25),
             (6, 24), (5, 22), (5, 8)], OUTLINE)
result.poly([(7, 6), (9, 7), (9, 23), (7, 23)], LEATHER)
result.line(8, 8, 8, 21, LIGHT)
# Spine bands.
for y in (9, 20):
    result.rect(5, y, 6, 2, METAL_DARK)
    result.line(6, y, 9, y, GOLD)
result.set(6, 11, DEEP).set(9, 11, DEEP)
result.set(6, 19, DEEP).set(9, 19, DEEP)

# Metal corner protectors on the cover.
# Upper-right bracket.
result.poly([(20, 5), (23, 5), (26, 8), (26, 12), (23, 12),
             (23, 9), (20, 8)], METAL_DARK)
result.poly([(21, 6), (23, 6), (25, 8), (25, 10), (24, 10),
             (24, 8), (21, 7)], GOLD)
result.set(23, 7, PAGES)
# Lower-right bracket.
result.poly([(22, 19), (26, 19), (27, 22), (24, 24), (20, 25),
             (20, 22), (23, 21)], METAL_DARK)
result.poly([(24, 20), (25, 20), (26, 22), (24, 23), (22, 24),
             (22, 23), (24, 22)], GOLD)
result.set(24, 21, PAGES)
# Small upper-left corner cap beside spine.
result.poly([(9, 5), (13, 5), (13, 8), (11, 8), (10, 10), (9, 9)], METAL_DARK)
result.line(10, 6, 12, 6, GOLD)
result.set(10, 7, GOLD)

# Central arcane clasp/emblem: dark mount, gold diamond and bright rune.
result.poly([(15, 11), (18, 10), (21, 13), (20, 17),
             (17, 20), (14, 17), (13, 14)], OUTLINE)
result.poly([(16, 12), (18, 11), (20, 13), (19, 17),
             (17, 19), (15, 17), (14, 14)], METAL_DARK)
result.poly([(17, 12), (19, 14), (18, 17), (17, 18),
             (15, 16), (15, 14)], GOLD)
result.set(17, 13, PAGES)
result.line(17, 14, 17, 16, PAGES)
result.set(16, 16, PAGES)

# Sparse leather wear and binding stitch detail.
result.set(12, 12, HILITE).set(21, 11, HILITE)
result.set(12, 19, LEATHER).set(21, 18, DEEP)
result.set(6, 14, METAL_DARK).set(6, 16, METAL_DARK)

view(result, scale=16, margin=0)
finish(result)
