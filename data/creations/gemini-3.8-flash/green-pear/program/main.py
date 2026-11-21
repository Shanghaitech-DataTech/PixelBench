# Green Pear - 32x32 Pixel Art (7 colors)

C_DARK = "#18300f"        # 1. Dark outline / shadow rim
C_SHADOW = "#355e16"      # 2. Rich shaded green
C_MID = "#6ea826"         # 3. Juicy pear green midtone
C_LIGHT = "#a7dc38"       # 4. Bright yellow-green
C_SPEC = "#e9fb8f"        # 5. Creamy highlight
C_STEM_DARK = "#382010"   # 6. Dark stem brown
C_STEM_LIGHT = "#7a461e"  # 7. Light stem brown

color_map = {
    'D': C_DARK,
    'S': C_SHADOW,
    'M': C_MID,
    'L': C_LIGHT,
    'H': C_SPEC,
    'B': C_STEM_DARK,
    'T': C_STEM_LIGHT,
}

canvas_map = [['.' for _ in range(32)] for _ in range(32)]

# Pear profile row by row (y, xl, xr)
body_profile = [
    # Top shoulders
    (8,  12, 19),
    (9,  11, 20),
    (10, 11, 20),
    (11, 11, 20),
    (12, 10, 21),
    (13, 10, 21),
    # Waist
    (14, 9, 22),
    (15, 9, 22),
    (16, 8, 23),
    (17, 7, 24),
    # Belly
    (18, 6, 25),
    (19, 5, 26),
    (20, 5, 26),
    (21, 5, 26),
    (22, 5, 26),
    (23, 6, 25),
    # Bottom
    (24, 6, 25),
    (25, 7, 24),
    (26, 8, 23),
    (27, 10, 21),
    (28, 12, 19),
]

# Fill body with midtone
for y, xl, xr in body_profile:
    for x in range(xl, xr + 1):
        canvas_map[y][x] = 'M'

# Pear outline
for y, xl, xr in body_profile:
    canvas_map[y][xl] = 'D'
    canvas_map[y][xr] = 'D'

# Top outline (shoulders curve down to stem)
canvas_map[8][12] = 'D'; canvas_map[8][13] = 'D'; canvas_map[8][14] = 'D'
canvas_map[8][17] = 'D'; canvas_map[8][18] = 'D'; canvas_map[8][19] = 'D'
# Dent depression at (15, 9) and (16, 9)
canvas_map[9][15] = 'D'; canvas_map[9][16] = 'D'

# Bottom outline
for x in range(12, 20):
    canvas_map[28][x] = 'D'
canvas_map[27][15] = 'D'; canvas_map[27][16] = 'D' # bottom dimple

# Stem:
stem_pixels = [
    (12, 2, 'B'), (13, 2, 'T'), (14, 2, 'B'),
    (13, 3, 'B'), (14, 3, 'T'),
    (14, 4, 'B'), (15, 4, 'T'),
    (14, 5, 'B'), (15, 5, 'T'),
    (15, 6, 'B'), (16, 6, 'T'),
    (15, 7, 'B'), (16, 7, 'B'),
    (15, 8, 'B'), (16, 8, 'B'),
]
for x, y, col in stem_pixels:
    canvas_map[y][x] = col

# Leaf:
leaf_pixels = [
    # Outline D
    (19, 3, 'D'), (20, 3, 'D'), (21, 3, 'D'), (22, 3, 'D'), (23, 3, 'D'),
    (17, 4, 'D'), (24, 4, 'D'),
    (16, 5, 'D'), (25, 5, 'D'),
    (17, 6, 'D'), (23, 6, 'D'), (24, 6, 'D'),
    (18, 7, 'D'), (19, 7, 'D'), (20, 7, 'D'), (21, 7, 'D'), (22, 7, 'D'),
    # Fill
    # Row 4:
    (18, 4, 'L'), (19, 4, 'L'), (20, 4, 'H'), (21, 4, 'H'), (22, 4, 'L'), (23, 4, 'L'),
    # Row 5:
    (17, 5, 'M'), (18, 5, 'L'), (19, 5, 'L'), (20, 5, 'L'), (21, 5, 'M'), (22, 5, 'M'), (23, 5, 'S'), (24, 5, 'S'),
    # Row 6:
    (18, 6, 'M'), (19, 6, 'M'), (20, 6, 'S'), (21, 6, 'S'), (22, 6, 'S'),
]
for x, y, col in leaf_pixels:
    canvas_map[y][x] = col

# Neck lighting:
neck_lights = [
    (10, [12, 13, 14], 'L'),
    (11, [12, 14], 'L'), (11, [13], 'H'),
    (12, [11, 12, 13], 'L'), (12, [14], 'M'),
    (13, [11, 12, 13], 'L'),
]
for y, xs, col in neck_lights:
    for x in xs:
        if canvas_map[y][x] != 'D':
            canvas_map[y][x] = col

# Belly lighting (L):
belly_light = [
    (14, range(10, 16)),
    (15, range(10, 17)),
    (16, range(9, 17)),
    (17, range(8, 17)),
    (18, range(7, 17)),
    (19, range(6, 17)),
    (20, range(6, 17)),
    (21, range(6, 16)),
    (22, range(6, 15)),
    (23, range(7, 14)),
    (24, range(7, 12)),
    (25, range(8, 11)),
]
for y, xs in belly_light:
    for x in xs:
        if canvas_map[y][x] != 'D':
            canvas_map[y][x] = 'L'

# Belly specular highlight (H):
spec_pixels = [
    (18, [9, 10, 11]),
    (19, [8, 9, 10, 11, 12]),
    (20, [8, 9, 10, 11, 12]),
    (21, [9, 10, 11]),
]
for y, xs in spec_pixels:
    for x in xs:
        canvas_map[y][x] = 'H'

# Center of specular
canvas_map[19][10] = 'H'; canvas_map[20][10] = 'H'

# Shadow side (S):
shadow_pixels = [
    (16, range(20, 23)),
    (17, range(20, 24)),
    (18, range(20, 25)),
    (19, range(20, 25)),
    (20, range(19, 25)),
    (21, range(18, 25)),
    (22, range(17, 24)),
    (23, range(16, 24)),
    (24, range(15, 23)),
    (25, range(14, 22)),
    (26, range(12, 21)),
    (27, range(11, 20)),
]
for y, xs in shadow_pixels:
    for x in xs:
        if canvas_map[y][x] != 'D':
            canvas_map[y][x] = 'S'

# Reflected bounce light along lower right rim:
bounce_rim = [
    (19, 25), (20, 25), (21, 25), (22, 25), (23, 24), (24, 24), (25, 23), (26, 22), (27, 20)
]
for y, x in bounce_rim:
    if canvas_map[y][x] == 'S':
        canvas_map[y][x] = 'M'

# Dithering / texture transitions between L and M:
dither_pixels = [
    (17, 17, 'M'), (17, 18, 'L'),
    (18, 17, 'L'), (18, 18, 'M'),
    (19, 17, 'M'), (19, 18, 'L'),
    (20, 17, 'L'), (20, 18, 'M'),
    (21, 16, 'M'), (21, 17, 'L'),
    (22, 15, 'M'), (22, 16, 'L'),
    (23, 14, 'M'), (23, 15, 'L'),
]
for y, x, col in dither_pixels:
    if canvas_map[y][x] not in ('D', 'B', 'T'):
        canvas_map[y][x] = col

c = new_canvas(32, 32)
for y in range(32):
    for x in range(32):
        ch = canvas_map[y][x]
        if ch in color_map:
            c.set(x, y, color_map[ch])

view(c)
stats = c.stats()
print(stats)
assert stats['colors_used'] <= 7, f"Too many colors: {stats['colors_used']}"
assert stats['size'] == [32, 32], f"Wrong size: {stats['size']}"

finish(c)
