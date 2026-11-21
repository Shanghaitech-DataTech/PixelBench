# Green pear, 32x32 pixel art
result = new_canvas(32, 32, background=None, name="green-pear")

OUTLINE = "#173b27"
SHADOW = "#2f6934"
GREEN = "#63a93e"
LIGHT = "#9bc94a"
GLINT = "#d7e66b"
STEM = "#704823"

# Stem, tilted slightly to the right.
result.rect(15, 2, 3, 6, OUTLINE)
result.rect(16, 2, 2, 5, STEM)
result.set(18, 2, OUTLINE)

# Small leaf behind the fruit.
result.rect(18, 4, 4, 1, OUTLINE)
result.rect(18, 5, 6, 2, OUTLINE)
result.rect(19, 7, 4, 1, OUTLINE)
result.rect(19, 5, 3, 1, GREEN)
result.rect(20, 6, 3, 1, SHADOW)

# Dark stepped silhouette.
for x, y, w in [
    (14, 6, 5), (12, 7, 9), (11, 8, 11),
    (10, 9, 13), (10, 10, 13), (9, 11, 15),
    (9, 12, 15), (8, 13, 17), (8, 14, 17),
    (7, 15, 19), (7, 16, 19), (6, 17, 21),
    (6, 18, 21), (6, 19, 21), (6, 20, 21),
    (6, 21, 21), (6, 22, 21), (6, 23, 21),
    (7, 24, 19), (7, 25, 19), (8, 26, 17),
    (9, 27, 15), (11, 28, 11), (13, 29, 7)
]:
    result.rect(x, y, w, 1, OUTLINE)

# Main fruit body inset from the outline.
for x, y, w in [
    (14, 7, 5), (12, 8, 9), (11, 9, 11),
    (11, 10, 11), (10, 11, 13), (10, 12, 13),
    (9, 13, 15), (9, 14, 15), (8, 15, 17),
    (8, 16, 17), (7, 17, 19), (7, 18, 19),
    (7, 19, 19), (7, 20, 19), (7, 21, 19),
    (7, 22, 19), (7, 23, 19), (8, 24, 17),
    (8, 25, 17), (9, 26, 15), (10, 27, 13),
    (12, 28, 9)
]:
    result.rect(x, y, w, 1, GREEN)

# Broad light-facing plane.
result.rect(12, 9, 6, 2, LIGHT)
result.rect(11, 11, 9, 3, LIGHT)
result.rect(10, 14, 10, 3, LIGHT)
result.rect(9, 17, 11, 5, LIGHT)
result.rect(10, 22, 10, 3, LIGHT)
result.rect(12, 25, 8, 2, LIGHT)

# Pixel highlight.
result.rect(12, 11, 3, 2, GLINT)
result.rect(10, 14, 3, 4, GLINT)
result.rect(9, 18, 2, 3, GLINT)
result.set(11, 13, GLINT)

# Weight and curvature on the right and along the base.
result.rect(22, 11, 1, 3, SHADOW)
result.rect(23, 14, 1, 3, SHADOW)
result.rect(24, 17, 2, 7, SHADOW)
result.rect(22, 24, 3, 2, SHADOW)
result.rect(20, 26, 3, 1, SHADOW)
result.rect(18, 27, 4, 1, SHADOW)
result.rect(13, 28, 7, 1, SHADOW)

# A few transition pixels keep the shading intentionally blocky.
result.rect(20, 12, 2, 4, GREEN)
result.rect(20, 16, 3, 7, GREEN)
result.rect(20, 23, 2, 3, GREEN)

view(result, scale=16, margin=0)
finish(result)
