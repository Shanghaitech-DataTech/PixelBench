from pixelbench_api import new_canvas, finish
import random

c = new_canvas(32, 32, name="retro-film-camera")

OUT = "#101014"   # dark outline
LEA = "#4a3422"   # leather base
LEAD = "#382814"  # leather dark speckle
LEAL = "#5d452c"  # leather light speckle
MET = "#d9d9d9"   # bright metal
METD = "#9a9a9a"  # mid metal
METX = "#6b6b6b"  # dark metal
GL1 = "#101c2c"   # glass mid
GL2 = "#22344e"   # glass blue
GLA = "#0a0f18"   # glass dark
GLC = "#04070c"   # glass core
HL = "#eaf4ff"    # hot highlight
HL2 = "#7fb3d9"   # soft reflection
RED = "#d8453a"   # shutter red
REDD = "#96231a"  # shutter shade

# ---- camera body (dark outline) ----
c.rect(4, 8, 24, 21, OUT)   # x4..27, y8..28
c.set(4, 8, None); c.set(27, 8, None)
c.set(4, 28, None); c.set(27, 28, None)
c.rect(5, 9, 22, 19, LEA)   # leather panel x5..26, y9..27

# ---- leather texture speckle ----
rng = random.Random(2024)
for y in range(9, 28):
    for x in range(5, 27):
        r = rng.random()
        if r < 0.09:
            c.set(x, y, LEAD)
        elif r < 0.16:
            c.set(x, y, LEAL)

# ---- rewind knob (top left) ----
c.circle(8, 8, 2, OUT)
c.circle(8, 8, 1, MET)
c.set(7, 7, METD)

# ---- shutter button (top right) ----
c.circle(24, 6, 2, OUT)
c.circle(24, 6, 1, RED)
c.set(23, 5, HL2)
c.set(25, 7, REDD)

# ---- viewfinder window ----
c.rect(20, 10, 4, 3, OUT)
c.rect(21, 11, 2, 1, GL2)
c.set(21, 11, HL2)

# ---- lens ----
c.circle(13, 19, 7, OUT)          # outer barrel
c.circle(13, 19, 6, METX)         # barrel ring
c.circle(13, 19, 5, MET)          # metal ring
c.circle(13, 19, 5, OUT, fill=False)  # bevel line
c.circle(13, 19, 4, GL2)          # glass
c.circle(13, 19, 3, GL1)
c.circle(13, 19, 2, GLA)
c.circle(13, 19, 1, GLC)
# lens screws / knurling on metal ring
c.set(13, 14, METD)
c.set(18, 19, METD)
c.set(13, 24, METD)
# glass highlights
c.set(10, 16, HL)
c.set(11, 15, HL)
c.set(12, 15, HL)
c.set(9, 17, HL2)
c.set(16, 22, HL2)
c.set(17, 21, HL2)

print(c.stats_text())
print(c.matrix_text())
finish(c)
