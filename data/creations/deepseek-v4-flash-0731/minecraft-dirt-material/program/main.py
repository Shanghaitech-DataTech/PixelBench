from pixelbench_api import new_canvas, finish
import random

W = H = 16
c = new_canvas(W, H)

# Minecraft-style dirt palette (<= 10 colors)
BASE   = "#79553A"  # mid brown
DARK1  = "#65432A"  # darker brown
DARK2  = "#523620"  # darkest brown
DEEP   = "#432A16"  # very dark organic speck
LIGHT1 = "#8F6A45"  # lighter tan
LIGHT2 = "#A5825B"  # light tan
GRAY1  = "#787878"  # stone pebble dark
GRAY2  = "#909090"  # stone pebble light

c.rect(0, 0, W, H, BASE)

rng = random.Random(20240407)

def paint(fx, fy, shape, color):
    # every feature wraps modulo 16 => the tile is seamless on all four edges
    for dx, dy in shape:
        c.set((fx + dx) % W, (fy + dy) % H, color)

# 1) fine grain over the whole tile
for y in range(H):
    for x in range(W):
        r = rng.random()
        if r < 0.07:
            c.set(x, y, DARK1)
        elif r < 0.13:
            c.set(x, y, LIGHT1)

# 2) small clumps of darker earth
blobs = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
]
for _ in range(10):
    paint(rng.randrange(16), rng.randrange(16), rng.choice(blobs), rng.choice([DARK1, DARK2]))

# 3) sparse very dark organic speckles
for _ in range(6):
    paint(rng.randrange(16), rng.randrange(16), [(0, 0)], DEEP)

# 4) light tan speckles / grit
for _ in range(10):
    paint(rng.randrange(16), rng.randrange(16),
          rng.choice([[(0, 0)], [(0, 0), (1, 0)], [(0, 0), (0, 1)]]),
          rng.choice([LIGHT1, LIGHT2]))

# 5) a few 2x2 stone pebbles
for _ in range(3):
    paint(rng.randrange(16), rng.randrange(16),
          [(0, 0), (1, 0), (0, 1), (1, 1)],
          rng.choice([GRAY1, GRAY2]))

print(c.stats_text())
print(c.matrix_text())
finish(c)
