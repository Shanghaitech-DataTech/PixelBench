c = new_canvas(16, 16, name="rpg-grass-material")

base = "#4F873B"
shadow = "#376B32"
dark = "#28542E"
light = "#70A84A"
dirt = "#80633D"
dirt_hi = "#A0804A"
yellow = "#EACB4E"
pollen = "#F5E77D"

c.rect(0, 0, 16, 16, base)

# Broken, irregular green flecks keep the field lively without forming bands.
for x, y in [
    (0,1),(2,0),(5,1),(8,0),(11,1),(14,0),
    (1,3),(4,2),(7,3),(10,2),(13,3),(15,2),
    (0,5),(3,5),(6,4),(9,5),(12,4),(15,6),
    (2,7),(5,7),(8,6),(11,7),(14,8),
    (0,9),(3,10),(6,9),(9,10),(12,9),(15,11),
    (1,12),(4,13),(7,12),(10,13),(13,12),
    (0,15),(3,14),(6,15),(9,14),(12,15),(15,14),
]:
    c.set(x, y, light if (x * 3 + y * 5) % 4 else shadow)

# Tiny darker tufts, deliberately broken into small pixel clusters.
for x, y in [(4,5),(10,3),(13,6),(2,10),(8,8),(11,11),(5,14),(14,1)]:
    c.set(x, y, dark)
    c.set((x + 1) % 16, y, shadow)
    if (x + y) % 2 == 0:
        c.set(x, (y + 1) % 16, dark)

# Sparse bare-earth chips; the little highlights keep them readable as dirt.
for x, y in [(7,2),(8,2),(7,3),(8,3),(1,8),(2,8),(1,9),
             (13,14),(14,14),(14,15)]:
    c.set(x, y, dirt if (x + y) % 3 else dirt_hi)
for x, y in [(8,2),(2,8),(14,14)]:
    c.set(x, y, dirt_hi)

# Three one-pixel blossoms with a subtle pale pixel beside each.
for x, y in [(3,2),(11,5),(6,11)]:
    c.set(x, y, yellow)
    c.set((x + 1) % 16, y, pollen)

print(c.stats_text())
finish(c)
