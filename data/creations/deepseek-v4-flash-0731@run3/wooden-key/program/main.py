from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H, name="wooden_key")

OUT = c.color("#2f1a0c", name="outline")
WOOD = c.color("#7c4f24", name="wood")
LIGHT = c.color("#c68e4e", name="light")
SHAD = c.color("#452a11", name="shadow")

shape = set()
# Bow: ring around (7,4), outer radius 4, hole radius 1
for y in range(H):
    for x in range(W):
        d2 = (x - 7) ** 2 + (y - 4) ** 2
        if d2 <= 16:
            shape.add((x, y))
        if d2 <= 1:
            shape.discard((x, y))
# Shaft: rows 8..14, columns 7..9
for y in range(8, 15):
    for x in range(7, 10):
        shape.add((x, y))
# Teeth
for x in range(7, 12):
    shape.add((x, 11))
for x in range(7, 13):
    shape.add((x, 13))

for (x, y) in shape:
    c.set(x, y, WOOD)

light = {(7, 1), (6, 2), (5, 2), (8, 8), (8, 9)}
for (x, y) in light:
    if (x, y) in shape:
        c.set(x, y, LIGHT)

shadow = {(8, 5), (9, 5), (8, 6), (9, 6), (8, 10), (10, 11), (8, 12), (9, 12), (9, 13)}
for (x, y) in shadow:
    if (x, y) in shape:
        c.set(x, y, SHAD)

# Outline: any shape pixel touching transparency gets the dark outline
for (x, y) in list(shape):
    for (nx, ny) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if (nx, ny) not in shape:
            c.set(x, y, OUT)
            break

print(c.stats_text())
print(c.matrix_text())

finish(c)
