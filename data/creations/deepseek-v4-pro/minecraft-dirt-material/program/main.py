from pixelbench_api import *
import random

random.seed(7)

c = new_canvas(16, 16, name="dirt")

# Minecraft-style dirt palette (browns, granular)
base     = c.color((134, 96, 67),  name="base")
mid_dark = c.color((116, 79, 50),  name="mid_dark")
dark     = c.color((96, 61, 37),   name="dark")
light    = c.color((153, 115, 80), name="light")
lighter  = c.color((172, 135, 97), name="lighter")

# solid dirt base
c.rect(0, 0, 16, 16, base)

# Wrapped pixel writer -> guaranteed seamless tiling
def p(x, y, col):
    c.set(x % 16, y % 16, col)

def grain(x, y, col, w=1, h=1):
    for dy in range(h):
        for dx in range(w):
            p(x + dx, y + dy, col)

# scatter granular speckles of several brown tones
tones = [mid_dark, dark, light, lighter]
for _ in range(64):
    x = random.randrange(16)
    y = random.randrange(16)
    col = random.choice(tones)
    w = random.choice([1, 1, 1, 2])
    h = random.choice([1, 1, 1, 2])
    grain(x, y, col, w, h)

# a few larger dark clods with a light edge, like packed dirt lumps
clods = [(3, 2), (10, 6), (6, 12), (14, 1), (1, 9)]
for cx, cy in clods:
    grain(cx, cy, dark, 2, 2)
    grain(cx - 1, cy - 1, mid_dark, 1, 1)
    grain(cx + 2, cy, light, 1, 1)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))

finish(c)
