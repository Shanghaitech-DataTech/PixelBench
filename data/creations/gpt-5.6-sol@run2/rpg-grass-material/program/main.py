# 16x16 seamless RPG grass material tile
result = new_canvas(16, 16, background="#4f9b45", name="rpg_grass_material")

# Palette
light = "#68b84f"
bright = "#7bc75a"
dark = "#347a3b"
deep = "#286534"
dirt = "#8d6a3f"
dirt_light = "#a9824e"
flower = "#f2d65c"
flower_hi = "#fff09a"

# Interleaved grass speckles; several continue naturally at opposing edges.
light_pixels = [
    (1,0),(5,0),(11,0),(15,0), (3,1),(8,1),(13,1),
    (0,3),(6,2),(10,3),(15,4), (2,4),(8,4),(12,5),
    (4,6),(9,6),(14,7),(0,8), (6,8),(11,8),
    (2,10),(7,10),(15,10), (4,12),(10,12),(13,11),
    (0,14),(6,14),(12,14),(15,15),(3,15),(9,15)
]
for x, y in light_pixels:
    result.set(x, y, light)

bright_pixels = [
    (2,0),(9,2),(4,3),(14,2),(1,6),(7,5),(13,6),
    (3,8),(9,9),(15,8),(5,11),(11,10),(1,12),
    (8,13),(14,13),(5,15)
]
for x, y in bright_pixels:
    result.set(x, y, bright)

dark_pixels = [
    (0,1),(7,0),(12,1),(5,2),(15,3),(1,4),(11,4),
    (6,6),(15,6),(2,7),(10,7),(0,10),(6,9),(13,9),
    (3,11),(9,11),(14,12),(7,14),(11,15),(1,15)
]
for x, y in dark_pixels:
    result.set(x, y, dark)

# Small dark grass tufts: paired blades with occasional deep roots.
for pixels in [
    [(3,5),(4,4),(4,5),(5,5)],
    [(11,2),(12,2),(12,3),(13,2)],
    [(7,12),(8,11),(8,12),(9,12)],
    [(14,15),(15,14),(15,15),(0,15),(0,14)],
]:
    for x, y in pixels:
        result.set(x, y, dark)
for x, y in [(4,5),(12,3),(8,12),(15,15)]:
    result.set(x, y, deep)

# Sparse irregular bare-dirt chips.
for x, y in [(1,9),(2,9),(1,10),(2,11),(12,13),(13,13),(13,14)]:
    result.set(x, y, dirt)
for x, y in [(2,10),(12,14)]:
    result.set(x, y, dirt_light)

# Two tiny yellow flowers with bright centres.
for x, y in [(6,3),(5,4),(7,4),(6,5),(13,7),(12,8),(14,8),(13,9)]:
    result.set(x, y, flower)
for x, y in [(6,4),(13,8)]:
    result.set(x, y, flower_hi)

finish(result)
view(result, scale=24, margin=1, edges="all")
