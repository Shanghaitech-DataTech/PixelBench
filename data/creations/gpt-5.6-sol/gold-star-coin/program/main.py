from pixelbench_api import new_canvas, view, finish

# Six-colour metallic palette on a transparent 16x16 canvas.
result = new_canvas(16, 16, background=None, name="gold-star-coin")
outline = "#6b3511"
shadow = "#a95712"
bronze = "#d68118"
gold = "#f5b82e"
light = "#ffd85a"
shine = "#fff0a0"

# Pixel-stepped circular silhouette.
rows = {
    1: (6, 4),
    2: (4, 8),
    3: (3, 10),
    4: (2, 12),
    5: (1, 14),
    6: (1, 14),
    7: (1, 14),
    8: (1, 14),
    9: (1, 14),
    10: (1, 14),
    11: (2, 12),
    12: (3, 10),
    13: (4, 8),
    14: (6, 4),
}
for y, (x, w) in rows.items():
    result.rect(x, y, w, 1, outline)

# Raised rim and warm lower-right shadow.
result.rect(6, 2, 4, 1, light)
result.rect(4, 3, 8, 1, gold)
result.rect(3, 4, 10, 1, gold)
result.rect(2, 5, 12, 6, gold)
result.rect(3, 11, 10, 1, bronze)
result.rect(4, 12, 8, 1, bronze)
result.rect(6, 13, 4, 1, shadow)
result.rect(13, 6, 1, 5, bronze)
result.rect(12, 11, 1, 1, shadow)
result.rect(11, 12, 1, 1, shadow)
result.rect(2, 7, 1, 3, light)
result.rect(3, 5, 1, 2, light)
result.rect(4, 4, 4, 1, light)
result.set(5, 3, shine)
result.set(3, 6, shine)

# Dark five-point silhouette, stamped into the face.
star_outline = {
    4: [(7, 2)],
    5: [(7, 2)],
    6: [(3, 10)],
    7: [(4, 8)],
    8: [(5, 6)],
    9: [(5, 6)],
    10: [(4, 3), (9, 3)],
    11: [(4, 2), (10, 2)],
}
for y, spans in star_outline.items():
    for x, w in spans:
        result.rect(x, y, w, 1, outline)

# Bright inset preserves a one-pixel dark contour and suggests embossing.
result.rect(7, 5, 2, 1, shine)
result.rect(5, 6, 6, 1, shine)
result.rect(5, 7, 6, 1, light)
result.rect(6, 8, 4, 2, light)
result.rect(5, 10, 2, 1, light)
result.rect(9, 10, 2, 1, gold)

view(result, scale=24, margin=1, edges="all")
finish(result)
