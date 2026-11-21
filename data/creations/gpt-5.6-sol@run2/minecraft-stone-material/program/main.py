# 16x16 seamless cracked stone material
result = new_canvas(16, 16, background="#747876", name="minecraft_stone")

# Broad, blocky stone planes. Shapes that cross an edge are continued on the
# opposite side so adjacent copies do not reveal a hard texture boundary.
mid_light = "#858986"
light = "#969a96"
mid_dark = "#646866"
dark = "#535755"
crack = "#353937"

# Edge-wrapped formations.
result.rect(0, 2, 3, 2, mid_light)
result.rect(14, 2, 2, 2, mid_light)
result.set(0, 4, mid_light)
result.set(15, 4, mid_light)
result.rect(0, 11, 2, 2, mid_dark)
result.rect(15, 11, 1, 2, mid_dark)
result.set(0, 10, mid_dark)
result.set(15, 10, mid_dark)
result.rect(5, 0, 3, 1, mid_dark)
result.rect(5, 15, 3, 1, mid_dark)

# Interior stone clusters, deliberately stepped rather than smoothly shaded.
result.poly([(3,1),(5,1),(5,3),(7,3),(7,5),(4,5),(4,4),(2,4),(2,2),(3,2)], mid_dark)
result.rect(3, 2, 2, 1, "#747876")
result.poly([(9,1),(13,1),(13,3),(12,3),(12,5),(9,5),(10,3),(9,3)], mid_light)
result.rect(11, 1, 2, 1, light)
result.poly([(1,6),(4,6),(4,8),(6,8),(6,10),(3,10),(3,9),(1,9)], mid_light)
result.set(2, 6, light)
result.poly([(10,6),(14,6),(14,8),(13,8),(13,10),(10,10),(10,9),(8,9),(8,7),(10,7)], mid_dark)
result.rect(11, 7, 2, 1, dark)
result.poly([(2,12),(5,12),(5,11),(8,11),(8,14),(6,14),(6,15),(3,15),(3,14),(2,14)], mid_dark)
result.set(3, 12, dark)
result.poly([(10,11),(14,11),(14,14),(12,14),(12,15),(9,15),(9,13),(10,13)], mid_light)
result.set(13, 12, light)

# Sparse chips prevent the broad fields from looking mechanically flat.
for x, y, color in [
    (1,1,light),(8,1,mid_dark),(14,5,dark),(6,6,light),
    (1,14,mid_light),(7,10,dark),(14,9,light),(11,15,light),
    (4,7,light),(12,5,mid_light),(2,10,dark)
]:
    result.set(x, y, color)

# Branching fissure: dark core plus a few lower-edge chips for readable depth.
for x, y in [
    (7,2),(7,3),(8,4),(8,5),(7,6),(7,7),(8,8),(8,9),
    (9,10),(9,11),(10,12),(10,13),(11,14),
    (6,5),(5,5),(5,6),
    (9,9),(10,9),(11,8),
    (8,12),(7,13)
]:
    result.set(x, y, crack)
for x, y in [(8,3),(9,5),(8,6),(9,8),(10,10),(11,12),(12,14),(6,6),(11,9),(8,13)]:
    result.set(x, y, light)

view(result, scale=24, margin=0)
finish(result)
