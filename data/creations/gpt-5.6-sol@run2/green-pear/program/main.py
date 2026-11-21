from pixelbench_api import new_canvas, view, finish

result = new_canvas(32, 32, background=None, name="green-pear")

OUTLINE = "#173827"
SHADOW = "#28633a"
MID = "#4c9b42"
LIGHT = "#78c94c"
GLOW = "#c0e765"
STEM = "#6a4728"

# Stem, tucked behind the leaf and fruit.
result.rect(16, 2, 3, 6, OUTLINE)
result.rect(17, 2, 2, 5, STEM)
result.set(19, 2, STEM)
result.set(16, 6, STEM)

# Upturned leaf with a crisp, dark rim.
result.poly([(18, 5), (21, 2), (27, 3), (26, 5), (23, 8), (18, 8)], OUTLINE)
result.poly([(20, 5), (22, 3), (25, 4), (23, 6), (20, 7)], LIGHT)
result.line(20, 7, 24, 4, SHADOW)

# Pear silhouette, drawn as deliberate pixel-step scanlines.
outer_spans = {
    6: (14, 19), 7: (12, 21), 8: (11, 22), 9: (10, 22),
    10: (10, 22), 11: (9, 23), 12: (8, 24), 13: (7, 25),
    14: (7, 25), 15: (6, 26), 16: (6, 26), 17: (5, 27),
    18: (5, 27), 19: (5, 27), 20: (5, 27), 21: (5, 27),
    22: (6, 26), 23: (6, 26), 24: (7, 25), 25: (7, 25),
    26: (8, 24), 27: (10, 22), 28: (13, 19),
}
for y, (x0, x1) in outer_spans.items():
    result.rect(x0, y, x1 - x0 + 1, 1, OUTLINE)

inner_spans = {
    7: (15, 18), 8: (13, 20), 9: (12, 20), 10: (12, 20),
    11: (11, 21), 12: (10, 22), 13: (9, 23), 14: (8, 24),
    15: (8, 24), 16: (7, 25), 17: (7, 25), 18: (6, 26),
    19: (6, 26), 20: (6, 26), 21: (7, 25), 22: (7, 25),
    23: (8, 24), 24: (8, 24), 25: (9, 23), 26: (10, 22),
    27: (12, 20),
}
for y, (x0, x1) in inner_spans.items():
    result.rect(x0, y, x1 - x0 + 1, 1, MID)

# Rounded shadow mass on the lower-right side.
shadow_spans = {
    12: (21, 22), 13: (22, 23), 14: (22, 24), 15: (23, 24),
    16: (23, 25), 17: (23, 25), 18: (22, 26), 19: (22, 26),
    20: (21, 26), 21: (20, 25), 22: (19, 25), 23: (18, 24),
    24: (17, 24), 25: (16, 23), 26: (15, 22), 27: (15, 20),
}
for y, (x0, x1) in shadow_spans.items():
    result.rect(x0, y, x1 - x0 + 1, 1, SHADOW)

# Broad lit plane on the upper-left of the fruit.
light_spans = {
    9: (13, 16), 10: (12, 17), 11: (12, 18), 12: (11, 19),
    13: (10, 19), 14: (9, 18), 15: (9, 17), 16: (8, 16),
    17: (8, 15), 18: (8, 14), 19: (8, 13), 20: (9, 12),
}
for y, (x0, x1) in light_spans.items():
    result.rect(x0, y, x1 - x0 + 1, 1, LIGHT)

# Tiny hard-edged shine and a few transition pixels.
result.rect(11, 11, 3, 3, GLOW)
result.rect(10, 14, 3, 2, GLOW)
result.set(9, 16, GLOW)
result.set(19, 11, LIGHT)
result.set(20, 13, LIGHT)
result.set(8, 21, LIGHT)
result.set(14, 26, MID)

view(result, scale=16, margin=0)
finish(result)
