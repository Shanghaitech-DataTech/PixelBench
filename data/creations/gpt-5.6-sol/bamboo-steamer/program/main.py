# 32x32 bamboo steamer sprite on transparency
result = new_canvas(32, 32, background=None, name="bamboo-steamer")

# Compact warm palette.
outline = result.color("#4b2718", "outline")
deep = result.color("#6d381d", "deep_bamboo")
shadow = result.color("#8f5127", "bamboo_shadow")
mid = result.color("#bd7735", "bamboo")
light = result.color("#e2a955", "bamboo_light")
high = result.color("#f3ca79", "bamboo_highlight")
inside = result.color("#5b3020", "basket_inside")
cloth = result.color("#754026", "inner_mat")
dump_shadow = result.color("#d7b46f", "dumpling_shadow")
dumpling = result.color("#f1db9a", "dumpling")
dump_hi = result.color("#fff0bd", "dumpling_highlight")
steam = result.color("#e9f1df", "steam")

# Rising steam, kept sparse and clearly separated from the lid.
result.set(11, 1, steam).set(10, 2, steam).set(10, 3, steam).set(11, 4, steam)
result.set(12, 4, steam).set(12, 5, steam)
result.set(21, 0, steam).set(20, 1, steam).set(20, 2, steam).set(21, 3, steam)
result.set(22, 3, steam).set(22, 4, steam)
result.set(26, 3, steam).set(25, 4, steam).set(25, 5, steam)

# Partially raised lid, lifted diagonally toward the right.
# Dark silhouette and stepped ends make the open angle crisp.
result.poly([(3, 12), (5, 9), (21, 4), (27, 6), (29, 8), (27, 11), (9, 16), (4, 14)], outline)
result.poly([(5, 11), (7, 9), (21, 5), (26, 7), (27, 9), (25, 10), (9, 14), (5, 13)], mid)
# Diagonal lid slats and highlighted upper edge.
result.line(7, 9, 22, 5, light)
result.line(5, 11, 26, 7, shadow)
result.line(7, 12, 26, 8, light)
result.line(9, 14, 24, 10, high)
result.set(6, 10, high).set(8, 9, high).set(25, 7, light)
# Dark lower lip emphasizes that the lid floats above the dumplings.
result.line(8, 15, 26, 10, deep)
result.set(4, 13, deep).set(5, 14, deep).set(25, 11, deep).set(27, 9, deep)

# Basket body silhouette and recessed interior.
result.poly([(3, 17), (5, 14), (27, 14), (29, 17), (27, 27), (24, 30), (8, 30), (5, 28)], outline)
result.poly([(4, 17), (6, 15), (26, 15), (28, 17), (26, 20), (6, 20)], deep)
result.poly([(6, 16), (9, 14), (24, 14), (27, 16), (25, 18), (7, 18)], inside)
result.line(8, 17, 25, 17, cloth)

# Three dumplings with different silhouettes and visible pleats.
# Left: rounded pouch.
result.poly([(7, 17), (8, 14), (10, 12), (12, 14), (13, 17), (12, 19), (8, 19)], dump_shadow)
result.poly([(8, 17), (9, 14), (10, 13), (11, 15), (12, 17), (11, 18), (9, 18)], dumpling)
result.set(10, 14, dump_hi).set(9, 15, dump_hi)
result.set(9, 13, outline).set(10, 12, outline).set(11, 13, outline)
# Center: taller pinched dumpling.
result.poly([(13, 18), (14, 14), (15, 13), (15, 11), (16, 12), (17, 11), (17, 14), (19, 16), (19, 19)], dump_shadow)
result.poly([(14, 17), (15, 14), (16, 13), (17, 15), (18, 17), (18, 18), (15, 18)], dumpling)
result.set(15, 15, dump_hi).set(16, 14, dump_hi)
result.set(15, 12, outline).set(16, 11, outline).set(17, 12, outline)
# Right: crescent/half-moon dumpling.
result.poly([(19, 18), (20, 15), (22, 13), (25, 14), (26, 16), (25, 19)], dump_shadow)
result.poly([(20, 17), (21, 15), (23, 14), (25, 16), (24, 18), (21, 18)], dumpling)
result.set(21, 15, dump_hi).set(22, 15, dump_hi)
result.line(21, 14, 24, 15, outline)
result.set(22, 13, outline).set(24, 14, outline)
# Small interior gaps keep all three silhouettes legible.
result.set(13, 17, inside).set(19, 18, inside)

# Thick front rim hides the dumpling bases and establishes the round opening.
result.poly([(3, 18), (5, 17), (8, 19), (24, 19), (27, 17), (29, 18), (28, 22), (26, 23), (6, 23), (4, 22)], outline)
result.poly([(5, 18), (8, 20), (24, 20), (27, 18), (27, 21), (25, 22), (7, 22), (5, 21)], mid)
result.line(8, 20, 24, 20, light)
result.line(8, 22, 24, 22, shadow)
result.set(6, 19, light).set(25, 19, light)

# Lower bamboo wall and individual vertical staves.
result.poly([(6, 23), (27, 23), (26, 27), (24, 29), (8, 29), (6, 27)], mid)
result.rect(7, 23, 2, 5, shadow)
result.rect(10, 23, 2, 6, light)
result.rect(13, 23, 2, 6, shadow)
result.rect(16, 23, 2, 6, light)
result.rect(19, 23, 2, 6, shadow)
result.rect(22, 23, 2, 6, light)
result.rect(25, 23, 1, 5, shadow)
# Woven bands and feet/base.
result.line(6, 25, 26, 25, deep)
result.line(7, 26, 25, 26, high)
result.line(7, 28, 25, 28, deep)
result.line(9, 29, 23, 29, outline)
result.set(8, 28, outline).set(24, 28, outline)

finish(result)
view(result, scale=16, margin=0)
