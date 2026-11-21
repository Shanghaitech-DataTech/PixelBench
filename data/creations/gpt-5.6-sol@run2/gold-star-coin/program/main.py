# 16x16 gold coin with an embossed star emblem.
result = new_canvas(16, 16, background=None, name="gold-star-coin")

outline = "#6b3514"
shadow = "#a95416"
mid = "#d7831b"
gold = "#f2b52d"
highlight = "#ffd766"
star = "#fff0a3"

# Crisp circular silhouette: dark rim first, then nested face bands.
spans = {
    1: (6, 4), 2: (4, 8), 3: (3, 10), 4: (2, 12),
    5: (1, 14), 6: (1, 14), 7: (1, 14), 8: (1, 14),
    9: (1, 14), 10: (1, 14), 11: (2, 12), 12: (2, 12),
    13: (3, 10), 14: (5, 6),
}
for y, (x, w) in spans.items():
    result.rect(x, y, w, 1, outline)

# Rim and face shading, brightest toward the upper-left.
for y, x, w in [
    (2, 6, 4), (3, 4, 8), (4, 3, 10), (5, 2, 12),
    (6, 2, 12), (7, 2, 12), (8, 2, 12), (9, 2, 12),
    (10, 2, 12), (11, 3, 10), (12, 3, 10), (13, 5, 6),
]:
    result.rect(x, y, w, 1, shadow)
for y, x, w in [
    (3, 6, 5), (4, 4, 8), (5, 3, 9), (6, 3, 10),
    (7, 3, 10), (8, 3, 10), (9, 3, 10), (10, 3, 9),
    (11, 4, 8), (12, 5, 6),
]:
    result.rect(x, y, w, 1, mid)
for y, x, w in [
    (4, 6, 5), (5, 5, 7), (6, 4, 8), (7, 4, 8),
    (8, 4, 8), (9, 4, 8), (10, 5, 7), (11, 6, 5),
]:
    result.rect(x, y, w, 1, gold)

# Specular glints and subtle rim breakup.
for x, y in [(5,3), (3,5), (3,6), (2,7), (4,4), (11,5)]:
    result.set(x, y, highlight)
for x, y in [(12,10), (11,12), (4,12), (3,10)]:
    result.set(x, y, shadow)

# Complete five-point star with a one-pixel lower-right stamp shadow.
star_shape = {
    4: [7], 5: [7], 6: [6,7,8],
    7: [4,5,6,7,8,9,10], 8: [5,6,7,8,9],
    9: [6,7,8], 10: [5,6,7,8,9],
    11: [5,9],
}
for y, xs in star_shape.items():
    for x in xs:
        result.set(x, y + 1, outline)
# A tiny reflected edge keeps the engraving tied to the warm metal.
result.set(7, 7, shadow)
result.set(7, 8, shadow)

finish(result)
view(result, scale=24, margin=1, edges="all")
