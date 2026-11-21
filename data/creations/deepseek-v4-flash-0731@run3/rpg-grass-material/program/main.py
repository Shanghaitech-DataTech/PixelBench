import random
from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H)

# Palette
mid    = c.color((0x5f, 0x99, 0x3a), name="mid")
light  = c.color((0x7c, 0xb5, 0x50), name="light")
dark   = c.color((0x49, 0x7e, 0x2b), name="dark")
tuft   = c.color((0x32, 0x5e, 0x1c), name="tuft")
flower = c.color((0xff, 0xd4, 0x2e), name="flower")
flowhi = c.color((0xff, 0xe9, 0x96), name="flowhi")
dirt   = c.color((0x8d, 0x6d, 0x3e), name="dirt")
dirt2  = c.color((0x6f, 0x54, 0x2c), name="dirt_dark")


def pset(x, y, col):
    c.set(x % W, y % H, col)


# Base grass
c.rect(0, 0, W, H, mid)

rng = random.Random(20240607)

# Interleaved light/dark speckles
for y in range(H):
    for x in range(W):
        r = rng.random()
        if r < 0.18:
            pset(x, y, light)
        elif r < 0.36:
            pset(x, y, dark)

# A few extra small light clumps
for _ in range(7):
    x = rng.randrange(W)
    y = rng.randrange(H)
    pset(x, y, light)
    pset(x + rng.choice([-1, 1]), y + rng.choice([-1, 1]), light)

# Small darker grass tufts (2-3 px sprigs)
tuft_shapes = [
    [(0, 0), (1, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
]
for _ in range(7):
    x = rng.randrange(W)
    y = rng.randrange(H)
    for dx, dy in rng.choice(tuft_shapes):
        pset(x + dx, y + dy, tuft)

# Sparse bare-dirt patches (2-4 px, with a darker edge pixel)
dirt_shapes = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0)],
    [(0, 0), (1, 0), (1, 1)],
]
for _ in range(4):
    x = rng.randrange(W)
    y = rng.randrange(H)
    shape = rng.choice(dirt_shapes)
    for dx, dy in shape:
        pset(x + dx, y + dy, dirt)
    pset(x - 1, y, dirt2)

# A few tiny yellow flowers (1-2 px with a light center)
for _ in range(4):
    x = rng.randrange(W)
    y = rng.randrange(H)
    pset(x, y, flower)
    if rng.random() < 0.6:
        pset(x + rng.choice([-1, 0, 1]), y + rng.choice([-1, 0, 1]), flower)
    pset(x, y, flowhi)

print(c.stats_text())
print(c.matrix_text())

finish(c)
