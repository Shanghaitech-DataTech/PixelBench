# Cover the pine tree with a layer of snow.
# Snow settles on every upward-facing surface of the green canopy:
# each canopy pixel that has transparent sky directly above becomes snow,
# and the pixel immediately below it is also snowed to give the layer thickness.
# The brown trunk is left untouched.

c = input_canvas.copy(name='output')
W, H = c.stats()['size']
SNOW = c.color('#ffffff', name='snow')

def is_canopy(i):
    # input palette: 0 transparent, 1..4 are the green/teal canopy shades
    return i is not None and 1 <= i <= 4

def is_transparent(i):
    return i is None or i == 0

# Find upward-facing canopy edges (transparent directly above).
edges = []
for y in range(H):
    for x in range(W):
        i = c.get(x, y)
        if not is_canopy(i):
            continue
        above = c.get(x, y - 1) if y > 0 else 0
        if is_transparent(above):
            edges.append((x, y))

# Paint a two-pixel-thick snow layer from each edge downward.
for (x, y) in edges:
    c.set(x, y, SNOW)
    if y + 1 < H and is_canopy(c.get(x, y + 1)):
        c.set(x, y + 1, SNOW)

print(c.stats_text())
finish(c)
