from pixelbench_api import *

c = new_canvas(16, 16, background="#3f9142", name="grass")

DARK = "#2e6b30"
LIGHT = "#63b356"
YEL = "#f2d94e"
DIRT = "#8a6b3f"
DIRT2 = "#a5824f"

# base
c.rect(0, 0, 16, 16, "#3f9142")

# light/dark speckles (interleaved)
for (x, y, col) in [
    (1,0,LIGHT),(5,0,DARK),(9,1,LIGHT),(13,0,DARK),(3,2,LIGHT),
    (7,3,DARK),(11,2,LIGHT),(15,2,LIGHT),(0,4,DARK),(4,5,LIGHT),
    (8,5,DARK),(12,5,LIGHT),(2,7,DARK),(6,7,LIGHT),(10,8,DARK),
    (14,7,LIGHT),(1,9,LIGHT),(5,10,DARK),(9,10,LIGHT),(13,10,DARK),
    (3,12,LIGHT),(7,13,DARK),(11,13,LIGHT),(15,12,DARK),(0,14,LIGHT),
    (4,15,DARK),(8,15,LIGHT),(12,15,DARK),
]:
    c.set(x, y, col)

# grass tufts (small darker V shapes)
def tuft(x, y):
    c.set(x, y-1, DARK)
    c.set(x-1, y, DARK)
    c.set(x+1, y, DARK)
    c.set(x, y, DARK)

tuft(3, 3)
tuft(11, 6)
tuft(6, 11)
tuft(14, 13)
tuft(0, 8)

# tiny yellow flowers
def flower(x, y):
    c.set(x, y, YEL)
    c.set(x-1, y, YEL)
    c.set(x+1, y, YEL)
    c.set(x, y-1, YEL)
    c.set(x, y+1, DARK)  # stem hint

flower(6, 2)
flower(13, 11)
flower(2, 13)

# bare dirt patches
c.rect(9, 8, 2, 2, DIRT)
c.set(10, 8, DIRT2)
c.rect(1, 5, 2, 1, DIRT)
c.set(2, 5, DIRT2)
c.rect(14, 3, 2, 2, DIRT)
c.set(14, 4, DIRT2)

# seamless: wrap edges — copy edge-adjacent features
# make left/right edges match
for y in range(16):
    c.set(0, y, c.get(16 if False else 0, y))
# simple approach: mirror border columns
for y in range(16):
    c.set(15, y, c.get(0, y))
for x in range(16):
    c.set(x, 15, c.get(x, 0))

print(c.stats_text())
c.matrix_text()
save("rpg-grass-material", c)
finish(c)
