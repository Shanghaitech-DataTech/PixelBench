from generate_treant import build_treant_art

grid, palette = build_treant_art()

c = new_canvas(256, 256)
for y in range(256):
    for x in range(256):
        c.set(x, y, palette[grid[y, x]])

print("Canvas stats:", c.stats_text())
view(c)
finish(c)
