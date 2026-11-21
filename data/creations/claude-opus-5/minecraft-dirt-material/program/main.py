import random

W = H = 16
c = new_canvas(W, H, name="dirt")

# Minecraft-ish dirt browns, dark -> light (7 visible colours)
D0 = "#49331f"
D1 = "#5a4027"
D2 = "#6b4c2f"
BA = "#7b5a3a"
L1 = "#8b6845"
L2 = "#9b7752"
L3 = "#ab8a64"

TONES = [D0, D1, D2, BA, L1, L2, L3]
WEIGHT = [5, 13, 22, 26, 19, 11, 4]

rng = random.Random(7)

# 1. granular static base
for y in range(H):
    for x in range(W):
        c.set(x, y, rng.choices(TONES, weights=WEIGHT)[0])


def stamp(cells, colour, ox, oy):
    """Place a small clump, wrapping at the tile edges (keeps it seamless)."""
    for dx, dy in cells:
        c.set((ox + dx) % W, (oy + dy) % H, colour)


CLUMPS = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0)],
    [(0, 0), (0, 1)],
]

# 2. coherent clumps: dark pits and light grit, so it is not pure static
for colour, n in ((D0, 5), (D1, 6), (L2, 6), (L3, 4)):
    for _ in range(n):
        stamp(rng.choice(CLUMPS), colour, rng.randrange(W), rng.randrange(H))

# 3. single-pixel speckles for the gravelly feel
for colour, n in ((D0, 10), (L3, 8)):
    for _ in range(n):
        c.set(rng.randrange(W), rng.randrange(H), colour)

print(c.stats_text())
view(c)
save("dirt", c)
finish(c)
