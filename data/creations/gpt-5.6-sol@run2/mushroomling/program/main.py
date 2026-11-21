from pixelbench_api import new_canvas, view, finish

# Four visible colors; transparency is the fifth, free state.
result = new_canvas(16, 16, background=None, name="mushroomling")
outline = "#211a24"
red = "#d83b3b"
white = "#fff2d8"
body = "#d9a66f"

# Cap silhouette.
for y, x, w in [
    (1, 6, 4),
    (2, 4, 8),
    (3, 3, 10),
    (4, 2, 12),
    (5, 1, 14),
    (6, 1, 14),
    (7, 2, 12),
]:
    result.rect(x, y, w, 1, outline)

# Cap fill, deliberately leaving a heavy lower rim.
for y, x, w in [
    (2, 6, 4),
    (3, 4, 8),
    (4, 3, 10),
    (5, 2, 12),
    (6, 2, 12),
]:
    result.rect(x, y, w, 1, red)

# Irregular white spots.
result.rect(5, 3, 2, 2, white)
result.set(4, 4, white)
result.rect(10, 4, 2, 2, white)
result.set(11, 3, white)
result.rect(7, 6, 2, 1, white)
result.set(2, 5, white)
result.set(13, 6, white)

# Body, arms, and standing legs as one dark silhouette.
for y, x, w in [
    (7, 5, 6),
    (8, 4, 8),
    (9, 3, 10),
    (10, 1, 14),
    (11, 2, 12),
    (12, 4, 8),
    (13, 4, 8),
    (14, 3, 6),
    (14, 8, 5),
    (15, 3, 4),
    (15, 9, 4),
]:
    result.rect(x, y, w, 1, outline)

# Face and torso fill.
result.rect(6, 8, 4, 1, body)
result.rect(5, 9, 6, 3, body)
result.rect(5, 12, 6, 1, body)
result.rect(6, 13, 4, 1, body)

# Stubby arm highlights keep the silhouette readable.
result.set(3, 10, body)
result.set(12, 10, body)

# Round, bright eyes with dark pupils.
result.rect(5, 9, 2, 2, white)
result.rect(9, 9, 2, 2, white)
result.set(6, 10, outline)
result.set(9, 10, outline)

# Tiny feet interior, separated by a dark central gap.
result.rect(4, 14, 3, 1, body)
result.rect(9, 14, 3, 1, body)
result.set(4, 15, body)
result.set(11, 15, body)

view(result, scale=28, margin=1, edges="all")
finish(result)
