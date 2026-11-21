from pixelbench_api import *

c = new_canvas(16, 16, name="stone")

colors = {
    'base': c.color('#7f7f7f', 'base'),
    'light': c.color('#8e8e8e', 'light'),
    'lighter': c.color('#9f9f9f', 'lighter'),
    'dark': c.color('#6e6e6e', 'dark'),
    'darker': c.color('#5c5c5c', 'darker'),
    'crack': c.color('#3c3c3c', 'crack'),
    'highlight': c.color('#b0b0b0', 'highlight'),
    'deep': c.color('#4a4a4a', 'deep'),
}

def hash2(x, y):
    h = (x * 374761393 + y * 668265263) & 0xFFFFFFFF
    h = (h ^ (h >> 13)) * 1274126177
    h = h & 0xFFFFFFFF
    return (h ^ (h >> 16)) & 0xFFFF

def smooth(t):
    return t * t * (3 - 2 * t)

def vnoise(x, y, L):
    gx = x * L / 16.0
    gy = y * L / 16.0
    i = int(gx) % L
    j = int(gy) % L
    tx = smooth(gx - int(gx))
    ty = smooth(gy - int(gy))
    v00 = hash2(i, j) / 65535.0
    v10 = hash2((i + 1) % L, j) / 65535.0
    v01 = hash2(i, (j + 1) % L) / 65535.0
    v11 = hash2((i + 1) % L, (j + 1) % L) / 65535.0
    a = v00 * (1 - tx) + v10 * tx
    b = v01 * (1 - tx) + v11 * tx
    return a * (1 - ty) + b * ty

def stone_color(n):
    v = n - 0.5
    if v < -0.30:
        return colors['darker']
    elif v < -0.10:
        return colors['dark']
    elif v < 0.10:
        return colors['base']
    elif v < 0.20:
        return colors['light']
    elif v < 0.30:
        return colors['lighter']
    else:
        return colors['highlight']

for y in range(16):
    for x in range(16):
        n = vnoise(x, y, 8) * 0.55 + vnoise(x, y, 16) * 0.45
        c.set(x, y, stone_color(n))

# 4-connected crack paths that wrap (top<->bottom at x=6, left<->right at y=3)
crack_v = [
    (6, 0), (6, 1), (6, 2), (7, 2), (7, 3), (7, 4), (6, 4), (5, 4), (5, 5),
    (5, 6), (6, 6), (6, 7), (6, 8), (7, 8), (7, 9), (6, 9), (6, 10), (6, 11),
    (6, 12), (6, 13), (6, 14), (6, 15),
]
crack_h = [
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (7, 4),
    (8, 4), (9, 4), (9, 3), (10, 3), (11, 3), (12, 3), (12, 2), (13, 2),
    (14, 2), (14, 3), (15, 3),
]
branches = [
    [(7, 5), (7, 6)],
    [(11, 4), (11, 5)],
    [(4, 4), (3, 4)],
]

core = set(crack_v + crack_h)
for br in branches:
    core.update(br)

for (x, y) in core:
    c.set(x, y, colors['crack'])

occupied = set(core)

def put(x, y, col):
    if 0 <= x < 16 and 0 <= y < 16 and (x, y) not in occupied:
        c.set(x, y, col)
        occupied.add((x, y))

for (x, y) in sorted(core):
    up = (x, y - 1) in core
    down = (x, y + 1) in core
    left = (x - 1, y) in core
    right = (x + 1, y) in core
    vertical = up or down
    horizontal = left or right
    if vertical and not horizontal:
        put(x + 1, y, colors['deep'])
    elif horizontal and not vertical:
        put(x, y + 1, colors['deep'])
    else:
        put(x + 1, y + 1, colors['deep'])

charmap = {}
chars = {'base': ' ', 'light': 'b', 'lighter': 'c', 'dark': 'd',
         'darker': 'e', 'crack': 'f', 'highlight': 'g', 'deep': 'h'}
for name, idx in colors.items():
    charmap[idx] = chars[name]

for y in range(16):
    row = ''
    for x in range(16):
        row += charmap[c.get(x, y)]
    print(row)

print(c.stats_text())
finish(c)
