# 16x16 detective-game magnifying glass icon
result = new_canvas(16, 16, background=None, name="magnifying-glass")

# Compact noir palette.
ink = result.color("#17202b", "ink")
deep = result.color("#273747", "deep")
steel_dark = result.color("#526779", "steel_dark")
steel = result.color("#91a6b5", "steel")
steel_light = result.color("#d5e3e7", "steel_light")
glass = result.color("#5f9aaa", "glass")
glass_light = result.color("#9fd3d5", "glass_light")
glass_shadow = result.color("#3f7384", "glass_shadow")
wood_dark = result.color("#5b3025", "wood_dark")
wood = result.color("#a65e35", "wood")
wood_light = result.color("#d88a4c", "wood_light")

# Handle and metal neck, tucked behind the lens.
result.poly([(8, 8), (10, 8), (12, 10), (12, 11), (15, 14),
             (15, 15), (13, 15), (10, 12), (9, 12), (7, 10)], ink)
result.poly([(10, 10), (11, 10), (15, 14), (15, 15), (14, 15), (10, 11)], wood_dark)
result.poly([(11, 11), (14, 14), (13, 14), (10, 11)], wood)
result.set(12, 12, wood_light)
result.rect(8, 8, 3, 3, steel_dark)
result.set(8, 8, steel)
result.set(9, 9, steel_light)

# Dark, deliberately stepped outer silhouette of the lens.
outer_rows = {
    0: (3, 7), 1: (1, 9), 2: (0, 10), 3: (0, 10),
    4: (0, 11), 5: (0, 11), 6: (0, 11), 7: (0, 10),
    8: (1, 10), 9: (2, 9), 10: (4, 7),
}
for y, (x0, x1) in outer_rows.items():
    result.rect(x0, y, x1 - x0 + 1, 1, ink)

# Steel rim inside the outline.
rim_rows = {
    1: (3, 7), 2: (2, 9), 3: (1, 9), 4: (1, 10),
    5: (1, 10), 6: (1, 10), 7: (1, 9), 8: (2, 9), 9: (4, 7),
}
for y, (x0, x1) in rim_rows.items():
    result.rect(x0, y, x1 - x0 + 1, 1, steel_dark)

# Pale upper-left rim catches the light.
result.line(3, 1, 7, 1, steel)
result.line(2, 2, 2, 3, steel)
result.line(1, 4, 1, 6, steel)
result.set(3, 2, steel_light)
result.set(2, 3, steel_light)
result.set(8, 2, deep)
result.line(10, 4, 10, 7, deep)
result.line(8, 9, 9, 8, deep)

# Blue-green glass interior.
glass_rows = {
    3: (4, 7), 4: (3, 8), 5: (2, 8),
    6: (2, 8), 7: (3, 8), 8: (4, 7),
}
for y, (x0, x1) in glass_rows.items():
    result.rect(x0, y, x1 - x0 + 1, 1, glass)

# Lens depth and a small hard-edged reflection.
result.set(3, 4, glass_light)
result.rect(4, 3, 2, 1, glass_light)
result.set(2, 5, glass_light)
result.set(4, 4, glass_light)
result.line(8, 5, 8, 7, glass_shadow)
result.line(6, 8, 7, 8, glass_shadow)
result.set(7, 7, glass_shadow)

view(result, scale=24, margin=1, edges="all")
finish(result)
