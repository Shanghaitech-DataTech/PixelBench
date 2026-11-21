from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#14171f")

# 4x3 ring loop
# Let's draw rings at various (rx, ry)
# For each ring:
# (rx+1, ry): Top highlight
# (rx+2, ry): Top highlight
# (rx, ry+1): Left midtone
# (rx+3, ry+1): Right midtone
# (rx+1, ry+2): Bottom shadow
# (rx+2, ry+2): Bottom shadow
# (rx+1, ry+1): hole
# (rx+2, ry+1): hole

def draw_ring(c, rx, ry, col_hi="#e2e8f0", col_mid="#8da0b6", col_shad="#475569", col_hole="#1e2430"):
    c.set(rx + 1, ry, col_hi)
    c.set(rx + 2, ry, col_hi)
    c.set(rx, ry + 1, col_mid)
    c.set(rx + 3, ry + 1, col_shad)
    c.set(rx + 1, ry + 2, col_shad)
    c.set(rx + 2, ry + 2, col_shad)
    c.set(rx + 1, ry + 1, col_hole)
    c.set(rx + 2, ry + 1, col_hole)

# Pattern A: offset x by 3, y by 2
# Odd rows offset by 1 or 2
for r in range(5):
    ry = 2 + r * 2
    ox = 1 if (r % 2 == 1) else 0
    for cx in range(0, 7):
        rx = 1 + cx * 3 + ox
        draw_ring(c, rx, ry)

# Let's also test a 3x3 ring on the bottom half
def draw_ring3(c, rx, ry, col_hi="#e2e8f0", col_mid="#8da0b6", col_shad="#475569", col_hole="#1e2430"):
    c.set(rx + 1, ry, col_hi)
    c.set(rx, ry + 1, col_mid)
    c.set(rx + 2, ry + 1, col_shad)
    c.set(rx + 1, ry + 2, col_shad)
    c.set(rx + 1, ry + 1, col_hole)

for r in range(6):
    ry = 16 + r * 2
    ox = 1 if (r % 2 == 1) else 0
    for cx in range(0, 10):
        rx = 1 + cx * 2 + ox
        draw_ring3(c, rx, ry)

view(c)
