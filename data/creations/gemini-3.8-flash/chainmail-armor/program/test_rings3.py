from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#14171f")

# Test with spacing 4, ry step 2, ox alternating 0 and 2:
def draw_ring(c, rx, ry, col_hi="#e6edf8", col_mid="#8fa4be", col_shad="#485c74", col_hole="#18202c"):
    c.set(rx + 1, ry, col_hi)
    c.set(rx + 2, ry, col_hi)
    c.set(rx, ry + 1, col_mid)
    c.set(rx + 3, ry + 1, col_shad)
    c.set(rx + 1, ry + 2, col_shad)
    c.set(rx + 2, ry + 2, col_shad)
    c.set(rx + 1, ry + 1, col_hole)
    c.set(rx + 2, ry + 1, col_hole)

for r in range(6):
    ry = 2 + r * 2
    ox = 2 if (r % 2 == 1) else 0
    for cx in range(-1, 8):
        rx = cx * 4 + ox
        draw_ring(c, rx, ry)

# Let's also test spacing 3 with offset:
for r in range(6):
    ry = 16 + r * 2
    ox = 1 if (r % 2 == 1) else 0
    for cx in range(-1, 10):
        rx = cx * 3 + ox
        draw_ring(c, rx, ry)

view(c)
