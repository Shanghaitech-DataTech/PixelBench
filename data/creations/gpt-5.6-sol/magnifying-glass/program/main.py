from pixelbench_api import new_canvas, view, finish

# 16x16 detective-game magnifying glass icon.
result = new_canvas(16, 16, background=None, name="magnifying-glass")

INK = "#182033"
SHADOW = "#56343a"
BRASS = "#c17832"
GOLD = "#e8aa45"
GLASS_DARK = "#2e7180"
GLASS = "#56b6b2"
GLINT = "#bcebd5"

# Handle and neck, drawn behind the lens.
result.poly([(8, 8), (10, 8), (12, 10), (12, 11), (15, 13),
             (15, 15), (13, 15), (10, 12), (9, 12), (8, 10)], INK)
result.set(10, 9, SHADOW)
result.set(11, 10, BRASS)
result.set(10, 10, BRASS)
result.set(11, 11, GOLD)
result.set(12, 11, BRASS)
result.set(12, 12, GOLD)
result.set(13, 12, BRASS)
result.set(13, 13, GOLD)
result.set(14, 13, BRASS)
result.set(14, 14, GOLD)
result.set(13, 14, BRASS)

# Dark, stepped outer silhouette of the circular lens.
for x0, x1, y in [
    (4, 7, 1), (2, 9, 2), (1, 10, 3), (1, 10, 4),
    (0, 11, 5), (0, 11, 6), (1, 10, 7), (1, 10, 8),
    (2, 9, 9), (4, 7, 10),
]:
    result.rect(x0, y, x1 - x0 + 1, 1, INK)

# Brass rim.
for x0, x1, y in [
    (4, 7, 2), (2, 9, 3), (2, 9, 4), (1, 10, 5),
    (1, 10, 6), (2, 9, 7), (2, 9, 8), (4, 7, 9),
]:
    result.rect(x0, y, x1 - x0 + 1, 1, BRASS)

# Warm rim highlights and deeper lower-right rim shade.
result.rect(4, 2, 4, 1, GOLD)
result.set(2, 3, GOLD)
result.set(3, 3, GOLD)
result.set(1, 5, GOLD)
result.set(1, 6, GOLD)
result.set(2, 7, GOLD)
result.set(9, 7, SHADOW)
result.set(8, 8, SHADOW)
result.set(7, 9, SHADOW)

# Cool glass interior.
for x0, x1, y in [
    (4, 7, 3), (3, 8, 4), (2, 9, 5),
    (2, 9, 6), (3, 8, 7), (4, 7, 8),
]:
    result.rect(x0, y, x1 - x0 + 1, 1, GLASS_DARK)

result.rect(4, 4, 3, 1, GLASS)
result.rect(3, 5, 5, 1, GLASS)
result.rect(3, 6, 4, 1, GLASS)
result.rect(4, 7, 2, 1, GLASS)

# Hard-edged reflected glint.
result.set(4, 4, GLINT)
result.set(5, 4, GLINT)
result.set(3, 5, GLINT)
result.set(8, 7, "#245464")
result.set(7, 8, "#245464")

view(result, scale=28, margin=1, edges="all")
finish(result)
