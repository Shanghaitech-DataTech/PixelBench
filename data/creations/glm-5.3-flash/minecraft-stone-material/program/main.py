"""Minecraft-style cracked stone block, 16x16, seamless tile, 7 colours."""

import random

try:
    from pixelbench_api import new_canvas, finish
except Exception:  # preloaded globals fallback
    new_canvas = globals()["new_canvas"]
    finish = globals()["finish"]

SIZE = 16
rng = random.Random(90210)

# ---------------------------------------------------------------- palette
PALETTE = {
    "shadow": "#5A5A5A",
    "dark":   "#686868",
    "base":   "#7C7C7C",
    "light":  "#8B8B8B",
    "bright": "#9A9A9A",
    "crack":  "#474747",
    "core":   "#383838",
}
IDX = {}


def wrap(x, y):
    return x % SIZE, y % SIZE


# ---------------------------------------------------------------- canvas
c = new_canvas(SIZE, SIZE, background=None, name="stone_cracked")
for name, hexv in PALETTE.items():
    IDX[name] = c.color(hexv, name=name)

# ------------------------------------------------------------- the body --
for y in range(SIZE):
    for x in range(SIZE):
        c.set(x, y, IDX["base"])

# blob stamps (wrap around the edges, so no feature is cut by the seam)
BLOBS = [
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
]


def stamp(colour, count):
    for _ in range(count):
        blob = rng.choice(BLOBS)
        ax, ay = rng.randrange(SIZE), rng.randrange(SIZE)
        for dx, dy in blob:
            c.set(*wrap(ax + dx, ay + dy), colour)


stamp(IDX["dark"], 11)
stamp(IDX["light"], 5)

# fine grain
for _ in range(12):
    x, y = rng.randrange(SIZE), rng.randrange(SIZE)
    c.set(x, y, IDX["dark"] if rng.random() < 0.6 else IDX["light"])

# the brightest pixels sit inside the light patches
light_px = [(x, y) for y in range(SIZE) for x in range(SIZE)
            if c.get(x, y) == IDX["light"]]


def light_neighbours(x, y):
    n = 0
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = wrap(x + dx, y + dy)
        if c.get(nx, ny) == IDX["light"]:
            n += 1
    return n


light_px.sort(key=lambda p: (-light_neighbours(*p), p))
for x, y in light_px[:4]:
    c.set(x, y, IDX["bright"])

# ------------------------------------------------- the crack network -----
# hand-placed, 8-connected, and every edge crossing has a matching stub
CRACK_ROWS = {
    0: [4, 11],
    1: [4, 5, 12],
    2: [5, 13, 14],
    3: [5, 14],
    4: [2, 6, 8, 9],
    5: [1, 6, 10, 11],
    6: [6, 7, 12, 13],
    7: [0, 7, 14, 15],
    8: [1, 2, 8, 9],
    9: [7, 8],
    10: [5, 6, 7],
    11: [3, 4, 8],
    12: [0, 1, 2, 8, 15],
    13: [9, 14],
    14: [10],
    15: [4, 11],
}
CORES = [(5, 2), (6, 6), (8, 8), (9, 13)]

crack_pixels = [(x, y) for y in range(SIZE) for x in CRACK_ROWS[y]]
crack_set = set(crack_pixels)
for x, y in crack_pixels:
    c.set(x, y, IDX["crack"])
for x, y in CORES:
    c.set(x, y, IDX["core"])

# --------------------------------------------------- chipped crack lips --
# upper/left lip catches the light, lower/right lip falls into shadow
LIGHT_LIPS = [(3, 0), (3, 1), (4, 2), (5, 4), (6, 7), (7, 8), (6, 9), (5, 9),
              (4, 10), (2, 11), (7, 12), (10, 12), (10, 0), (11, 1), (12, 2),
              (8, 3), (10, 4), (12, 5), (14, 6), (1, 7)]
SHADOW_LIPS = [(5, 0), (6, 2), (7, 4), (8, 6), (9, 9), (8, 10), (9, 11),
               (10, 13), (12, 15), (3, 12), (10, 6), (12, 7), (14, 8), (0, 13)]
PITS = [(2, 2), (11, 2), (14, 5), (13, 9)]

for x, y in LIGHT_LIPS:
    assert (x, y) not in crack_set, f"lip on crack {(x, y)}"
    c.set(x, y, IDX["light"])
for x, y in SHADOW_LIPS + PITS:
    assert (x, y) not in crack_set, f"lip/pit on crack {(x, y)}"
    c.set(x, y, IDX["shadow"])

# --------------------------------------------------------------- checks --
lonely = []
for x, y in crack_set:
    n = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:
                nx, ny = wrap(x + dx, y + dy)
                if (nx, ny) in crack_set:
                    n += 1
    if n == 0:
        lonely.append((x, y))

seen, components = set(), 0
for start in crack_set:
    if start in seen:
        continue
    components += 1
    stack = [start]
    while stack:
        px, py = stack.pop()
        if (px, py) in seen:
            continue
        seen.add((px, py))
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = wrap(px + dx, py + dy)
                if (nx, ny) in crack_set and (nx, ny) not in seen:
                    stack.append((nx, ny))

print("lonely crack pixels:", lonely)
print("crack components:", components)

comps, seen2 = [], set()
for start in sorted(crack_set):
    if start in seen2:
        continue
    comp, stack = [], [start]
    while stack:
        p = stack.pop()
        if p in seen2:
            continue
        seen2.add(p)
        comp.append(p)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    q = wrap(p[0] + dx, p[1] + dy)
                    if q in crack_set and q not in seen2:
                        stack.append(q)
    comps.append(sorted(comp))
for i, comp in enumerate(comps):
    print(f"  component {i}: {len(comp)} px {comp}")

# ------------------------------------------- quantitative seam smoothness
TONE = {IDX["core"]: 0, IDX["crack"]: 1, IDX["shadow"]: 2, IDX["dark"]: 3,
        IDX["base"]: 4, IDX["light"]: 5, IDX["bright"]: 6}


def tone(x, y):
    return TONE[c.get(*wrap(x, y))]


hd = [abs(tone(15, y) - tone(0, y)) for y in range(16)]
vd = [abs(tone(x, 15) - tone(x, 0)) for x in range(16)]
interior = []
for x in range(1, 15):
    for y in range(16):
        interior.append(abs(tone(x, y) - tone(x + 1, y)))
for y in range(1, 15):
    for x in range(16):
        interior.append(abs(tone(x, y) - tone(x, y + 1)))
print(f"H seam avg tone diff: {sum(hd)/16:.2f} (max {max(hd)})")
print(f"V seam avg tone diff: {sum(vd)/16:.2f} (max {max(vd)})")
print(f"interior avg tone diff: {sum(interior)/len(interior):.2f} "
      f"(max {max(interior)})")

# --------------------------------------------------- seamless-tiling check
save("stone_cracked", c)
print(c.stats_text())
print(c.matrix_text())
finish(c)
