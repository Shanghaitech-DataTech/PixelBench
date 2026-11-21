from pixelbench_api import new_canvas, finish, save

c = new_canvas(16, 16)
dark = c.color("#1C1813")
gold = c.color("#E3B04E")
glass = c.color("#D9EDF6")
shine = c.color("#FFFFFF")
ink = c.color("#2A3A5C")

# Lens: dark outline, gold frame, light glass interior
c.circle(7, 6, 5, dark)
c.circle(7, 6, 4, gold)
c.circle(7, 6, 3, glass)

# Magnified fingerprint inside the lens
c.circle(7, 6, 2, ink, fill=False)
c.circle(7, 6, 1, ink, fill=False)

# Handle: 2px-thick 45-degree staircase of gold blocks
gold_cells = set()
for i in range(5):
    for dx in (0, 1):
        for dy in (0, 1):
            gold_cells.add((10 + i + dx, 9 + i + dy))
for (x, y) in gold_cells:
    c.set(x, y, gold)

# Outline the handle with dark on every side (8-neighbour silhouette)
for (x, y) in list(gold_cells):
    for nx in (x - 1, x, x + 1):
        for ny in (y - 1, y, y + 1):
            if (nx, ny) not in gold_cells and 0 <= nx < 16 and 0 <= ny < 16:
                c.set(nx, ny, dark)

# Redraw glint on the glass after handle work
c.line(4, 3, 6, 3, shine)
c.line(4, 3, 4, 5, shine)

print(c.stats_text())
print(c.matrix_text())
save("magnifying_glass", c)
finish(c)
