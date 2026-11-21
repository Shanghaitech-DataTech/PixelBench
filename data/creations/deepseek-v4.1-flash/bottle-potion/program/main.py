from pixelbench_api import *

SRC = input_canvas
out = SRC.copy(name='output')
name_of = {p['index']: p['name'] for p in SRC.palette()}

# ---- palette for the potion ----
P_DEEP   = out.color('#2a0d47', name='potion_deep')    # deepest shadow
P_DARK   = out.color('#40186f', name='potion_dark')    # upper liquid
P_MID    = out.color('#6428ab', name='potion_mid')     # lower liquid
P_BRIGHT = out.color('#7739c7', name='potion_bright')  # sheen / highlights
BUBBLE   = out.color('#c2a0f2', name='bubble')
BUB_HI   = out.color('#efe4ff', name='bubble_hi')
SPARK    = out.color('#d7bfff', name='spark')
WHITE    = 1

def blk(lx, ly, col):
    for dy in (0, 1):
        for dx in (0, 1):
            out.set(lx * 2 + dx, ly * 2 + dy, col)

def cur(lx, ly):
    return out.get(lx * 2, ly * 2)

# ---- recolour every liquid blue into purple potion ----
remap = {'c4': P_DARK, 'c5': P_MID, 'c6': P_BRIGHT, 'c7': P_BRIGHT,
         'c9': P_BRIGHT, 'c8': P_DEEP, 'c3': P_DEEP}
liquid_names = {'c4', 'c5', 'c6', 'c7', 'c8', 'c9'}
mask = [[False] * 32 for _ in range(32)]

for ly in range(32):
    for lx in range(32):
        nm = name_of[SRC.get(lx * 2, ly * 2)]
        if nm in liquid_names:
            mask[ly][lx] = True
        if nm in remap:
            blk(lx, ly, remap[nm])

# ---- bubbles inside the potion ----
def disc(r, t):
    return [(dx, dy) for dy in range(-r, r + 1) for dx in range(-r, r + 1)
            if dx * dx + dy * dy <= t]

def bubble(cx, cy, r):
    pts = disc(r, 6 if r == 2 else 1)
    bad = [(cx + dx, cy + dy) for dx, dy in pts
           if not (0 <= cy + dy < 32 and 0 <= cx + dx < 32 and mask[cy + dy][cx + dx])]
    if bad:
        print('WARN bubble spills at', (cx, cy), bad)
        return
    for dx, dy in pts:
        blk(cx + dx, cy + dy, BUBBLE)
    shine = [(-1, -1), (-2, -1)] if r == 2 else [(0, 0)]
    for dx, dy in shine:
        if (dx, dy) in pts:
            blk(cx + dx, cy + dy, BUB_HI)

BUBBLES = [
    (10, 18, 2),   # big bubble, left of centre
    (16, 25, 2),   # big bubble low centre
    (12, 14, 1),   # small rise
    (19, 15, 1),
    (22, 17, 1),
    (6, 22, 1),
    (21, 22, 1),
    (13, 29, 1),
]
for cx, cy, r in BUBBLES:
    bubble(cx, cy, r)

# ---- magic sparkles in the background ----
def sparkle(cx, cy, vlen, hlen):
    spots = []
    for d in range(1, vlen + 1):
        spots += [(cx, cy - d, SPARK), (cx, cy + d, SPARK)]
    for d in range(1, hlen + 1):
        spots += [(cx - d, cy, SPARK), (cx + d, cy, SPARK)]
    spots.append((cx, cy, BUB_HI))
    for x, y, col in spots:
        if 0 <= x < 32 and 0 <= y < 32 and cur(x, y) == WHITE:
            blk(x, y, col)
        else:
            print('skip sparkle px', x, y)

sparkle(8, 3, 2, 2)
sparkle(29, 15, 1, 1)
sparkle(28, 24, 1, 1)

# ---- report ----
sym = {P_DEEP: 'D', P_DARK: 'u', P_MID: 'U', P_BRIGHT: 'P',
       BUBBLE: 'o', BUB_HI: 'O', SPARK: '*', WHITE: '.', 2: '#'}
print('     ' + ''.join(str((x // 2) // 10) for x in range(0, 64, 2)))
print('     ' + ''.join(str((x // 2) % 10) for x in range(0, 64, 2)))
for ly in range(32):
    print(f'{ly:3d}  ' + ''.join(sym.get(cur(lx, ly), '?') for lx in range(32)))
hi = [(x // 2, y // 2) for y in range(64) for x in range(64) if out.get(x, y) == BUB_HI]
print('bubble highlights at', sorted(set(hi)))
print(out.stats_text())
save('potion', out)
finish(out)
