from pixelbench_api import new_canvas, finish
import random

W = H = 16
c = new_canvas(W, H)

# palette
base   = (0x6E, 0xA8, 0x3E)  # medium grass
dark   = (0x52, 0x86, 0x30)  # dark green speckle
light  = (0x84, 0xBE, 0x4E)  # light green speckle
tuft   = (0x3C, 0x6A, 0x22)  # darker grass tuft
tuft2  = (0x46, 0x7A, 0x28)
dirt   = (0x92, 0x6A, 0x42)  # bare dirt
dirt2  = (0x7A, 0x56, 0x32)
yellow = (0xF8, 0xD6, 0x42)
orange = (0xE0, 0xA4, 0x2C)

c.rect(0, 0, W, H, base)

# interleaved dark/light green speckles (scattered, organic)
rng = random.Random(7)
for y in range(H):
    for x in range(W):
        r = rng.random()
        if r < 0.20:
            c.set(x, y, dark)
        elif r < 0.42:
            c.set(x, y, light)

def put(x, y, col):
    c.set(x % W, y % H, col)  # wrap -> seamless tiling

def patch(cx, cy, pts, col):
    for dx, dy in pts:
        put(cx + dx, cy + dy, col)

# sparse bare-dirt patches
patch(3, 3,  [(0, 0), (1, 0), (0, 1)], dirt)
patch(13, 12, [(0, 0), (1, 1), (0, -1)], dirt)
patch(11, 14, [(0, 0)], dirt2)

# small darker grass tufts (3-5 px blades, wrap-aware)
patch(8, 4,  [(0, 0), (-1, 0), (0, -1), (0, 1)], tuft)
patch(5, 12, [(0, 0), (1, 1), (0, 2), (1, 0)], tuft)
patch(13, 7, [(0, 0), (0, -1), (-1, -1), (1, -1)], tuft2)
patch(1, 13, [(0, 0), (0, 1)], tuft2)

# tiny yellow flowers (plus-shape petals)
flower = [(0, -1), (0, 1), (-1, 0), (1, 0)]
patch(3, 8, flower, yellow)
patch(10, 2, flower, yellow)
patch(15, 9, flower, yellow)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))

finish(c)
