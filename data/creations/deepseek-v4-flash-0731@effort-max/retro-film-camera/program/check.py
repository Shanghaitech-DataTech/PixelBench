from pixelbench_api import new_canvas
import random

c = new_canvas(32, 32, name="retro-film-camera")

OUT = "#101014"
LEA = "#4a3422"
LEAD = "#382814"
LEAL = "#5d452c"
MET = "#d9d9d9"
METD = "#9a9a9a"
METX = "#6b6b6b"
GL1 = "#101c2c"
GL2 = "#22344e"
GLA = "#0a0f18"
GLC = "#04070c"
HL = "#eaf4ff"
HL2 = "#7fb3d9"
RED = "#d8453a"
REDD = "#96231a"

c.rect(4, 8, 24, 21, OUT)
c.set(4, 8, None); c.set(27, 8, None)
c.set(4, 28, None); c.set(27, 28, None)
c.rect(5, 9, 22, 19, LEA)

rng = random.Random(2024)
for y in range(9, 28):
    for x in range(5, 27):
        r = rng.random()
        if r < 0.09:
            c.set(x, y, LEAD)
        elif r < 0.16:
            c.set(x, y, LEAL)

c.circle(8, 8, 2, OUT)
c.circle(8, 8, 1, MET)
c.set(7, 7, METD)

c.circle(24, 6, 2, OUT)
c.circle(24, 6, 1, RED)
c.set(23, 5, HL2)
c.set(25, 7, REDD)

c.rect(20, 10, 4, 3, OUT)
c.rect(21, 11, 2, 1, GL2)
c.set(21, 11, HL2)

for y in range(4, 11):
    print(f"y={y}: " + "".join(str(c.get(x, y) % 10) for x in range(3, 30)))
print()
print(c.matrix_text(region=(4, 4, 26, 9)))
