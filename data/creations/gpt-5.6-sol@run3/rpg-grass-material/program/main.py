# 16x16 seamless RPG grass material tile
result = new_canvas(16, 16, background="#4f8f3a", name="rpg_grass_material")

# Palette: deep blades, cool shadow grass, bright tips, dirt, and flowers.
dark = "#28602f"
shadow = "#397a34"
light = "#72ad3f"
highlight = "#91c94a"
dirt = "#80613a"
dirt_light = "#a17a45"
yellow = "#f2cf45"
flower_core = "#fff078"

# Dark grass speckles and compact tufts.
for x, y in [
    (0,1),(5,0),(11,0),(15,1),
    (3,3),(10,2),(13,4),
    (1,7),(7,5),(8,6),(14,8),
    (4,10),(10,9),(12,11),
    (0,14),(6,13),(9,15),(15,14)
]:
    result.set(x, y, dark)

# Small darker grass tufts: paired pixels read as short blades.
for x, y in [(2,5),(9,3),(5,12),(13,13)]:
    result.set(x, y, dark)
    result.set(x-1, y+1, shadow)
    result.set(x+1, y+1, dark)

# Lighter interleaved grass tips.
for x, y in [
    (2,0),(8,0),(14,0),(0,4),(5,3),(12,2),(15,4),
    (4,6),(11,6),(2,9),(8,8),(15,10),
    (1,12),(8,12),(11,14),(3,15),(14,15)
]:
    result.set(x, y, light)

for x, y in [(6,1),(14,6),(6,9),(2,14),(10,5)]:
    result.set(x, y, highlight)

# Sparse irregular bare-dirt patches.
for x, y in [(5,7),(6,7),(5,8),(6,8),(7,8),(6,9),
             (12,15),(13,15),(12,0),(13,0),(13,1)]:
    result.set(x, y, dirt)
for x, y in [(5,7),(7,8),(13,0)]:
    result.set(x, y, dirt_light)

# Two tiny yellow flowers with bright centers.
for cx, cy in [(3,2),(11,11)]:
    result.set(cx, cy-1, yellow)
    result.set(cx-1, cy, yellow)
    result.set(cx+1, cy, yellow)
    result.set(cx, cy+1, yellow)
    result.set(cx, cy, flower_core)

finish(result)
view(result, scale=24, margin=1, edges="all")
