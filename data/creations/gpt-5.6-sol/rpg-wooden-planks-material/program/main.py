# 16x16 seamless RPG wooden-plank material tile
result = new_canvas(16, 16, background="#8f542c", name="rpg_wooden_planks")

# Palette: warm, slightly varied boards with deep grooves and crisp pixel accents.
dark = "#321b16"
seam = "#4a281b"
shadow = "#63351f"
mid_a = "#9d6033"
mid_b = "#7f4728"
mid_c = "#a96838"
mid_d = "#89502c"
light = "#c17a40"
high = "#d08b4c"
knot = "#4f2a1b"

# Four vertical boards; the seam at x=15 joins cleanly to the next tile's x=0.
result.rect(0, 0, 3, 16, mid_a)
result.rect(4, 0, 3, 16, mid_b)
result.rect(8, 0, 3, 16, mid_c)
result.rect(12, 0, 3, 16, mid_d)
for x in (3, 7, 11, 15):
    result.rect(x, 0, 1, 16, dark)

# Staggered plank ends: dark butt groove plus a warm lower-edge glint.
for x0, y, base in ((0, 9, mid_a), (4, 5, mid_b), (8, 12, mid_c), (12, 7, mid_d)):
    result.rect(x0, y, 3, 1, seam)
    result.set(x0, y + 1, shadow)
    result.set(x0 + 1, y + 1, light)
    result.set(x0 + 2, y + 1, base)

# Slightly dark board-end caps make the alternating segments distinct.
result.set(0, 8, light); result.set(1, 8, high); result.set(2, 8, shadow)
result.set(4, 4, shadow); result.set(5, 4, light); result.set(6, 4, shadow)
result.set(8, 11, high); result.set(9, 11, light); result.set(10, 11, shadow)
result.set(12, 6, shadow); result.set(13, 6, light); result.set(14, 6, high)

# Fine vertical grain, broken and offset board by board.
for x, y0, y1, color in (
    (1, 0, 3, light), (1, 5, 7, shadow), (2, 11, 14, light),
    (5, 0, 2, shadow), (6, 7, 10, light), (5, 12, 15, shadow),
    (9, 1, 5, light), (10, 7, 10, shadow), (9, 14, 15, high),
    (13, 0, 3, shadow), (14, 9, 12, light), (13, 13, 15, shadow),
):
    result.line(x, y0, x, y1, color)

# Tiny bends imply natural grain rather than straight scratches.
result.set(0, 4, shadow); result.set(1, 4, shadow); result.set(2, 3, light)
result.set(4, 11, light); result.set(5, 10, light); result.set(6, 11, shadow)
result.set(8, 6, shadow); result.set(9, 6, shadow); result.set(10, 5, light)
result.set(12, 4, light); result.set(13, 5, light); result.set(14, 4, shadow)

# Compact knots with one dark core and a highlighted rim.
result.set(1, 12, knot); result.set(0, 12, shadow); result.set(2, 12, shadow)
result.set(1, 11, light); result.set(1, 13, shadow)
result.set(9, 8, knot); result.set(8, 8, shadow); result.set(10, 8, shadow)
result.set(9, 7, high); result.set(9, 9, shadow)
result.set(13, 14, knot); result.set(12, 14, shadow); result.set(14, 14, shadow)
result.set(13, 13, light)

# Groove highlights give the seams a shallow, carved profile.
for x, y in ((3, 2), (3, 13), (7, 1), (7, 9), (11, 4), (11, 15), (15, 6), (15, 12)):
    result.set(x, y, seam)

view(result, scale=24, margin=1, edges="all")
finish(result)
