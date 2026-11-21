c = new_canvas(32, 32, name="chainmail_armor")

ink = "#171d28"
edge = "#273544"
steel_dark = "#465b6b"
steel = "#718b98"
steel_light = "#a9c0c4"
steel_glint = "#d5e0d8"

# One-piece mail shirt silhouette, with short sleeves and a tapered hem.
outer = [(7,4),(11,3),(14,5),(18,5),(21,3),(25,4),(28,9),(26,12),(25,14),(26,21),(24,27),(22,29),(10,29),(8,27),(6,21),(7,14),(6,12),(4,9)]
c.poly(outer, ink)
shirt = [(8,5),(11,4),(14,6),(18,6),(21,4),(24,5),(27,9),(25,12),(24,14),(25,21),(23,26),(21,28),(11,28),(9,26),(7,21),(8,14),(7,12),(5,9)]
c.poly(shirt, steel_dark)

# Dark inset collar opening and the raised mail collar rim.
c.poly([(12,5),(14,6),(18,6),(20,5),(21,8),(19,10),(13,10),(11,8)], edge)
c.poly([(13,6),(14,7),(18,7),(19,6),(20,8),(18,9),(14,9),(12,8)], ink)

# Tiny interlocking ring marks on a staggered grid. Each ring uses a bright
# leading edge and a dark inner edge to remain legible at native resolution.
def inside(poly, x, y):
    hit = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            hit = not hit
        j = i
    return hit

for row, y in enumerate(range(11, 27, 4)):
    offset = 0 if row % 2 == 0 else 2
    for x in range(5 + offset, 28, 4):
        cx, cy = x + 1, y + 1
        if not inside(shirt, cx, cy) or (11 <= cx <= 20 and 5 <= cy <= 10):
            continue
        # Four-pixel ring loop, with a small interlocking connector.
        c.set(cx, cy-1, steel_light)
        c.set(cx+1, cy, steel)
        c.set(cx, cy+1, steel_dark)
        c.set(cx-1, cy, steel_light)
        c.set(cx+1, cy+1, edge)

# Shoulder and hem accents establish the garment construction.
c.line(7,8,10,6, steel_light)
c.line(21,6,24,8, steel_light)
c.line(8,22,10,26, steel)
c.line(24,22,22,26, steel)
c.line(11,28,21,28, steel_light)
c.line(9,13,8,20, edge)
c.line(23,13,24,20, edge)

print(c.stats_text())
finish(c)
