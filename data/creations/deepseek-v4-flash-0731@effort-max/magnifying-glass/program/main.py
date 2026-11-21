from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16)

OUTLINE = (32, 36, 44)        # dark outline
RIM = (152, 160, 172)         # silver rim
GLASS = (164, 208, 238)       # light glass
CLUE = (84, 128, 176)         # magnified "?" mark
WHITE = (244, 250, 255)       # glare
HANDLE = (190, 140, 88)       # wooden handle
HANDLE_DARK = (104, 68, 40)   # handle shading

# Lens built from concentric filled discs -> clean 1px rings
c.circle(7, 6, 5, OUTLINE)    # outer dark ring
c.circle(7, 6, 4, RIM)        # silver rim
c.circle(7, 6, 3, GLASS)      # pale glass

# Detective "?" inside the lens
for p in [(7, 4), (8, 4), (8, 5), (7, 6), (7, 7), (7, 8)]:
    c.set(p[0], p[1], CLUE)

# Top-left glare glint
for p in [(5, 4), (6, 4), (5, 5)]:
    c.set(p[0], p[1], WHITE)

# Wooden handle sweeping down-right from the rim
c.line(11, 9, 14, 12, HANDLE)
c.line(11, 10, 14, 13, HANDLE)
c.line(12, 12, 14, 14, HANDLE_DARK)

print(c.stats_text())
print(c.matrix_text())
finish(c)
