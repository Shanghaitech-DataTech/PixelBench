# 32x32 forest slime RPG enemy sprite
result = new_canvas(32, 32, name="forest-slime-monster")

# Palette
outline = "#17291f"
deep = "#244632"
shadow = "#315b3b"
body = "#477a47"
light = "#659955"
moss_dark = "#3a672f"
moss = "#5f913d"
moss_light = "#86ad4d"
shine = "#91bd70"
antler_dark = "#533d2b"
antler = "#87623a"
cap_dark = "#702d2b"
cap = "#b84638"
cap_light = "#dd6650"
stem_dark = "#8d7853"
stem = "#c3a873"
eye_outer = "#304526"
eye_glow = "#d7e95b"
eye_core = "#fff69a"
mouth = "#193026"

# Tiny branching antlers, behind the slime.
result.line(10, 8, 10, 3, antler_dark)
result.line(10, 4, 8, 2, antler_dark)
result.set(8, 1, antler)
result.line(10, 6, 12, 4, antler_dark)
result.set(12, 3, antler)
result.set(10, 3, antler)
result.set(9, 3, antler)
result.line(21, 8, 21, 3, antler_dark)
result.line(21, 4, 23, 2, antler_dark)
result.set(23, 1, antler)
result.line(21, 6, 19, 4, antler_dark)
result.set(19, 3, antler)
result.set(21, 3, antler)
result.set(22, 3, antler)

# Mushroom growing from the creature's back.
result.rect(24, 7, 3, 5, cap_dark)
result.rect(25, 9, 2, 4, stem_dark)
result.rect(25, 9, 1, 3, stem)
result.poly([(21, 8), (22, 6), (24, 5), (27, 5), (29, 7), (29, 9), (21, 9)], cap_dark)
result.rect(22, 7, 7, 2, cap)
result.rect(23, 6, 5, 2, cap)
result.rect(24, 6, 2, 1, cap_light)
result.set(22, 8, cap_light)

# Main compact slime silhouette.
result.poly([(11, 7), (14, 6), (17, 7), (19, 6), (22, 8),
             (23, 10), (25, 12), (25, 15), (27, 18), (27, 22),
             (29, 24), (27, 27), (23, 28), (20, 28), (18, 30),
             (14, 30), (12, 29), (8, 29), (6, 27), (3, 27),
             (4, 24), (3, 22), (5, 19), (5, 15), (6, 12),
             (8, 11), (8, 8)], outline)
# Body interior.
result.poly([(11, 9), (14, 8), (17, 9), (19, 8), (21, 10),
             (21, 12), (24, 14), (23, 17), (26, 19), (25, 23),
             (27, 24), (25, 26), (21, 26), (19, 28), (15, 28),
             (12, 27), (8, 27), (7, 25), (5, 25), (6, 22),
             (5, 20), (7, 18), (7, 14), (9, 13), (9, 10)], body)

# Lower volume shadows and rounded lobes.
result.rect(7, 23, 4, 4, shadow)
result.rect(9, 26, 4, 2, shadow)
result.rect(20, 25, 5, 2, deep)
result.rect(23, 21, 3, 4, deep)
result.set(6, 24, light)
result.rect(14, 27, 4, 2, light)
result.set(18, 26, light)

# Moss blanket and dangling tufts.
result.rect(9, 9, 4, 3, moss_dark)
result.rect(12, 8, 4, 4, moss)
result.rect(16, 9, 5, 3, moss_dark)
result.rect(18, 8, 3, 3, moss)
result.rect(8, 11, 3, 3, moss)
result.rect(21, 11, 2, 4, moss_dark)
result.set(10, 12, moss_light)
result.rect(13, 8, 2, 1, moss_light)
result.rect(17, 9, 2, 1, moss_light)
result.set(20, 8, moss_light)
result.set(9, 14, moss_dark)
result.set(14, 12, moss_dark)
result.set(19, 13, moss_dark)
result.set(22, 15, moss_dark)

# Soft slime highlights and forest speckles.
result.rect(8, 16, 2, 4, light)
result.set(9, 15, shine)
result.set(8, 20, shine)
result.rect(10, 14, 2, 2, light)
result.set(7, 22, moss_light)
result.set(11, 24, deep)
result.set(21, 19, moss_dark)
result.set(24, 20, moss)
result.set(20, 23, light)
result.set(9, 26, moss_dark)

# Glowing, slightly tilted eyes with dark upper rims.
result.rect(9, 17, 6, 5, eye_outer)
result.rect(18, 17, 6, 5, eye_outer)
result.rect(10, 18, 4, 3, eye_glow)
result.rect(19, 18, 4, 3, eye_glow)
result.rect(11, 18, 2, 2, eye_core)
result.rect(20, 18, 2, 2, eye_core)
result.set(13, 21, body)
result.set(19, 21, body)
# Brows make the expression alert but cute.
result.line(9, 16, 14, 17, outline)
result.line(18, 17, 23, 16, outline)

# Tiny mouth and cheek accents.
result.set(15, 23, mouth)
result.set(17, 23, mouth)
result.rect(16, 24, 1, 1, mouth)
result.set(12, 23, moss)
result.set(21, 23, moss)

view(result, scale=16, margin=0)
finish(result)
