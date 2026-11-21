# 16x16 seamless Minecraft-style dirt material.
result = new_canvas(16, 16, background="#795033", name="minecraft-dirt")

# Palette: warm soil base with granular highlights and compacted dark grains.
light = "#a87348"
mid_light = "#91603d"
mid_dark = "#68442d"
dark = "#513522"
deep = "#3f2a1d"
tan = "#b27c50"
red = "#835038"

# Broad, irregular soil clumps. Shapes crossing an edge are continued on the opposite edge.
for x, y in [(1,0),(2,0),(8,0),(9,0),(14,0),(3,3),(4,3),(5,3),(11,4),(12,4),
             (0,7),(1,7),(7,7),(8,7),(9,7),(14,8),(15,8),(4,11),(5,11),(10,12),
             (11,12),(1,15),(2,15),(8,15),(9,15),(14,15)]:
    result.set(x, y, mid_light)

# Highlight chips and small sandy flecks.
for x, y in [(3,0),(10,1),(6,2),(2,4),(13,5),(8,6),(1,8),(5,9),(11,9),
             (15,10),(3,12),(12,13),(7,14),(0,15)]:
    result.set(x, y, light)
for x, y in [(7,1),(4,5),(14,6),(9,10),(2,13),(13,15)]:
    result.set(x, y, tan)

# Dark compacted clods, including matched edge fragments for seamless repetition.
for x, y in [(5,0),(6,0),(12,0),(0,2),(1,2),(9,2),(10,2),(14,3),(5,6),(6,6),
             (11,7),(12,7),(2,9),(3,9),(15,11),(0,12),(7,12),(8,12),(13,14),
             (5,15),(6,15),(12,15)]:
    result.set(x, y, mid_dark)
for x, y in [(15,2),(9,3),(6,7),(12,8),(3,10),(4,10),(0,13),(8,13),(14,14)]:
    result.set(x, y, dark)
for x, y in [(10,4),(1,5),(13,10),(6,13)]:
    result.set(x, y, deep)

# A few muted clay-colored grains keep the dirt earthy rather than monochrome.
for x, y in [(4,1),(12,2),(7,4),(15,6),(0,9),(10,11),(3,14)]:
    result.set(x, y, red)

finish(result)
