# Minecraft-style dirt block material, 16x16, seamless tile, <=10 colors.
import random

W = H = 16
c = new_canvas(W, H, name="dirt")

# Classic Minecraft dirt palette (7 colors, limit is 10)
DARK   = c.color('#4A3220')  # deep crevice speckle
SHADOW = c.color('#5C4028')  # dark brown clod
BASE2  = c.color('#6E4D34')  # darker base variant
BASE   = c.color('#79553A')  # main dirt brown
MID    = c.color('#8A6547')  # mid tone
LIGHT  = c.color('#9C7851')  # light grain
PALE   = c.color('#B08C60')  # dry highlight speckle

rng = random.Random(20261108)

# 1) Granular base: per-pixel weighted random from the base tones.
weights = [(BASE, 46), (BASE2, 25), (MID, 17), (SHADOW, 7), (LIGHT, 5)]
bag = [col for col, w in weights for _ in range(w)]
for y in range(H):
    for x in range(W):
        c.set(x, y, rng.choice(bag))

# 2) Clods and grains drawn with modulo wrapping => seamless tiling.
def blob(cx, cy, cells, col):
    for dx, dy in cells:
        c.set((cx + dx) % W, (cy + dy) % H, col)

shapes = [
    [(0, 0), (1, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 1)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

for _ in range(7):   # dark clods
    blob(rng.randrange(W), rng.randrange(H), rng.choice(shapes), SHADOW)
for _ in range(6):   # light grains
    blob(rng.randrange(W), rng.randrange(H), rng.choice(shapes), LIGHT)
for _ in range(4):   # mid-tone lumps
    blob(rng.randrange(W), rng.randrange(H), [(0, 0), (1, 0)], MID)

# 3) Single-pixel speckles for the gritty, granular feel.
for _ in range(7):
    blob(rng.randrange(W), rng.randrange(H), [(0, 0)], DARK)
for _ in range(5):
    blob(rng.randrange(W), rng.randrange(H), [(0, 0)], PALE)

print(c.stats_text())

# Seam check: tile 3x3 on a scratch canvas (not submitted).
t = new_canvas(48, 48, name="tilecheck")
for ty in range(3):
    for tx in range(3):
        t.blit(c, tx * 16, ty * 16)
view(t)
view(c)

finish(c)
