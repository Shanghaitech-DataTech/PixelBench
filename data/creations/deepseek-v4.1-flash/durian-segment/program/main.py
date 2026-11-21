from pixelbench_api import *
import math

src = input_canvas
pal = src.palette()
HEX = ['#%02x%02x%02x' % tuple(p['rgba'][:3]) for p in pal]

out = src.copy(name='output')

def ch(x, y):
    return HEX[out.get(x, y)]

def och(x, y):
    return HEX[src.get(x, y)]

BG = '#ffffff'
BLACK = '#000000'

O = out.color('#ef9d0e')   # bright orange  (inner rind)
E = out.color('#be6f48')   # rind brown
C = out.color('#a65537')   # dark rind brown (shadow)

FLESH = {'#fbf4c9', '#ffda45', '#ffc830'}          # flesh tones
RIND = {'#be6f48', '#a65537', '#e08c37', '#ef9d0e'}  # rind tones

W, H = src.stats()['size']

# bottom silhouette of the pod, column by column
bot = {}
for x in range(W):
    ys = [y for y in range(H) if och(x, y) != BG]
    if ys:
        bot[x] = max(ys)

def cut_top(x):
    """Top edge of the newly exposed rind (where the bottom flesh piece was)."""
    t = min(1.0, max(0.0, (x - 5) / 45.0))
    return int(round(43.5 + 3.6 * math.sin(math.pi * (t ** 0.9))))

for x in sorted(bot):
    top = cut_top(x)
    ys = [y for y in range(top, bot[x] + 1) if och(x, y) not in (BG, BLACK)]
    h = len(ys)
    if h == 0:
        continue
    for i, y in enumerate(ys):
        orig = och(x, y)
        if orig in RIND:
            continue                      # existing rind stays untouched
        # flesh pixel -> replace with shell
        if i == 0:
            col = O                       # bright inner rind under the cut
        elif i == 1 and h >= 6:
            col = O
        elif i == h - 1 and h >= 9:
            col = C
        else:
            col = E
        out.set(x, y, col)

# ---- verification -----------------------------------------------------
diffs = bad = flesh_left = 0
for y in range(H):
    for x in range(W):
        if src.get(x, y) != out.get(x, y):
            diffs += 1
            if y < cut_top(x):
                bad += 1
        if ch(x, y) in FLESH and y >= cut_top(x) + 2:
            flesh_left += 1
print('pixels changed:', diffs, '| changes above the cut:', bad,
      '| flesh left below the cut:', flesh_left)
print(out.stats_text())

NAMES = {BG: '.', BLACK: 'K', '#a65537': 'C', '#e08c37': 'D', '#be6f48': 'E',
         '#fbf4c9': 'p', '#ffda45': 'Y', '#ffc830': 'G', '#ef9d0e': 'O'}
print('   ' + ''.join(str(x % 10) for x in range(64)))
for y in range(H):
    print('%2d %s' % (y, ''.join(NAMES.get(ch(x, y), '?') for x in range(64))))

save('durian-segment', out)
finish(out)
