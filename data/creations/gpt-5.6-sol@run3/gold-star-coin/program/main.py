# 16x16 gold coin with an inset star emblem.
result = new_canvas(16, 16, background=None, name="gold-star-coin")

EDGE = "#5a2b08"
SHADOW = "#a94f08"
GOLD = "#e58a10"
BRIGHT = "#ffc431"
GLINT = "#ffe783"

# Pixel-rounded coin silhouette: dark outer rim.
for y, x0, x1 in [
    (1, 6, 9), (2, 4, 11), (3, 3, 12), (4, 2, 13),
    (5, 1, 14), (6, 1, 14), (7, 1, 14), (8, 1, 14),
    (9, 1, 14), (10, 1, 14), (11, 2, 13), (12, 3, 12),
    (13, 4, 11), (14, 6, 9),
]:
    result.rect(x0, y, x1 - x0 + 1, 1, EDGE)

# Inner metal, with the lower-right half in bronze shadow.
for y, x0, x1 in [
    (2, 6, 9), (3, 4, 11), (4, 3, 12), (5, 2, 13),
    (6, 2, 13), (7, 2, 13), (8, 2, 13), (9, 2, 13),
    (10, 2, 13), (11, 3, 12), (12, 4, 11), (13, 6, 9),
]:
    result.rect(x0, y, x1 - x0 + 1, 1, SHADOW)

# Main gold face, offset up-left to give the rim thickness.
for y, x0, x1 in [
    (2, 6, 8), (3, 4, 10), (4, 3, 11), (5, 2, 12),
    (6, 2, 12), (7, 2, 12), (8, 2, 12), (9, 2, 12),
    (10, 3, 11), (11, 4, 10), (12, 6, 8),
]:
    result.rect(x0, y, x1 - x0 + 1, 1, GOLD)

# Bright upper-left edge glints, kept clear of the emblem.
result.rect(5, 3, 5, 1, BRIGHT)
result.set(3, 4, BRIGHT)
result.set(2, 5, BRIGHT)
result.set(2, 6, BRIGHT)
result.set(4, 3, GLINT)
result.set(3, 4, GLINT)
result.set(2, 5, GLINT)

# Small dark offset beneath the star gives it a stamped edge.
for x, y in [(9, 5), (11, 7), (10, 8), (10, 9), (11, 10), (10, 11), (6, 11)]:
    result.set(x, y, EDGE)

# Compact solid five-point star.
for y, spans in {
    4: [(7, 8)],
    5: [(7, 8)],
    6: [(4, 11)],
    7: [(5, 10)],
    8: [(6, 9)],
    9: [(6, 9)],
    10: [(5, 6), (9, 10)],
}.items():
    for x0, x1 in spans:
        result.rect(x0, y, x1 - x0 + 1, 1, GLINT)

view(result, scale=24, margin=1, edges="all")
finish(result)
