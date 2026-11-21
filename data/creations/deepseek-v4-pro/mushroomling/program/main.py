from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16, name="mushroomling")

OUT = c.color("#241a1a", name="outline")
RED = c.color("#d04030", name="red")
WHITE = c.color("#f8f8f8", name="white")
TAN = c.color("#e8c898", name="tan")

grid = [
    "....OOOOOOOO....",
    "...ORRRRRRRRO...",
    "..ORRRRWWRRRRO..",
    "..ORRRRRRRRRRO..",
    "..ORWWRRRRWWRO..",
    "..ORRRRRRRRRRO..",
    "..ORRRRRRRRRRO..",
    "..OOOOOOOOOOOO..",
    "...OTTTTTTTTO...",
    ".OTOTOOTTOOTOTO.",
    ".OTOTOOTTOOTOTO.",
    "...OTTTOOTTTO...",
    "...OTTTTTTTTO...",
    "...OTTTO.OTTTO..",
    "...OTTTO.OTTTO..",
    "...OOOOO.OOOOO..",
]

colors = {"O": OUT, "R": RED, "W": WHITE, "T": TAN}

for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, colors[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
