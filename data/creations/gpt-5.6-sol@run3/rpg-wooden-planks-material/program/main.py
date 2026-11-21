# 16x16 seamless vertical wooden-plank RPG material tile
result = new_canvas(16, 16, background="#8f552f", name="rpg_wooden_planks")

# Palette
seam = "#3b211c"
seam_hi = "#5a3022"
dark = "#684029"
mid = "#9d6337"
light = "#bd7b42"
high = "#d3914d"
knot = "#4b2b20"

# Four vertical boards with alternating tones.
result.rect(0, 0, 3, 16, mid)
result.rect(4, 0, 3, 16, light)
result.rect(8, 0, 3, 16, "#88502e")
result.rect(12, 0, 3, 16, "#aa6938")

# Deep one-pixel vertical seams. The x=15 groove closes against x=0 on repeat.
for x in (3, 7, 11, 15):
    result.rect(x, 0, 1, 16, seam)

# Staggered board-end joints, with alternating bright/dark lips.
result.line(0, 7, 2, 7, dark)
result.set(1, 8, "#c78345")
result.line(4, 11, 6, 11, seam_hi)
result.set(5, 12, high)
result.line(8, 5, 10, 5, seam)
result.set(9, 6, "#b56d3a")
result.line(12, 9, 14, 9, dark)
result.set(13, 10, "#d08443")

# Fine, mostly vertical natural grain.
grain_dark = [
    (1,1),(1,2),(2,3),(1,4),(2,10),(2,11),(1,13),(1,14),
    (5,1),(6,2),(5,4),(5,5),(6,7),(5,8),(6,14),
    (9,0),(9,2),(10,3),(9,8),(10,10),(9,12),(9,14),(10,15),
    (13,1),(14,3),(13,5),(14,6),(13,12),(14,14)
]
for x, y in grain_dark:
    result.set(x, y, dark)

grain_light = [
    (2,1),(1,5),(2,6),(2,9),(1,11),
    (5,0),(5,3),(6,4),(5,9),(6,10),(5,14),(6,15),
    (10,1),(9,3),(10,7),(9,9),(10,13),
    (13,0),(14,2),(13,4),(14,7),(13,11),(14,13),(13,15)
]
for x, y in grain_light:
    result.set(x, y, high)

# Small knots with hooked grain around them.
result.set(1, 3, knot)
result.set(2, 4, knot)
result.set(1, 4, "#d08a49")
result.set(13, 6, knot)
result.set(14, 7, knot)
result.set(13, 7, "#d18443")
result.set(9, 11, knot)
result.set(10, 12, knot)
result.set(9, 12, "#b66f3d")

# Tiny seam glints give the grooves depth without weakening the grid.
for y in (1, 8, 13):
    result.set(4, y, "#d18a49")
for y in (3, 10):
    result.set(8, y, "#b66c39")
for y in (2, 12):
    result.set(12, y, "#ca7c40")

view(result, scale=24, margin=1, edges="all")
finish(result)
