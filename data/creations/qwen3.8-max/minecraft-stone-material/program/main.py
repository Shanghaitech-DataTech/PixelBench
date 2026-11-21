"""16x16 seamless cracked-stone material tile, Minecraft style, <=10 colours."""
import random
from pixelbench_api import new_canvas, view, save, finish

W = H = 16

# ---- palette (exactly 10 colours) -------------------------------------
L2 = '#a6a6a6'   # bright chip highlight
L1 = '#949494'   # light stone
M1 = '#8a8a8a'   # mid-light stone
M0 = '#808080'   # base stone
D1 = '#767676'   # mid-dark stone
D2 = '#6b6b6b'   # dark stone
D3 = '#5c5c5c'   # deep grain / speck
C1 = '#4a4a4a'   # crack shoulder
C2 = '#3a3a3a'   # crack core
WM = '#8d8677'   # warm mineral fleck

RAMP = [(0.34, D2), (0.44, D1), (0.58, M0), (0.70, M1), (9.0, L1)]

c = new_canvas(W, H, name="stone")


def wset(x, y, col):
    c.set(x % W, y % H, col)


# ---- seamless value noise (two wrapping octaves) -----------------------
def make_grid(n, seed):
    rnd = random.Random(seed)
    return [[rnd.random() for _ in range(n)] for _ in range(n)]


G4 = make_grid(4, 11)   # 4 px cells
G8 = make_grid(8, 27)   # 2 px cells


def _sm(t):
    return t * t * (3 - 2 * t)


def sample(grid, x, y, cell):
    gx = x / float(cell)
    gy = y / float(cell)
    n = len(grid)
    ix = int(gx)
    iy = int(gy)
    x0 = ix % n
    y0 = iy % n
    x1 = (x0 + 1) % n
    y1 = (y0 + 1) % n
    fx = _sm(gx - ix)
    fy = _sm(gy - iy)
    top = grid[y0][x0] + (grid[y0][x1] - grid[y0][x0]) * fx
    bot = grid[y1][x0] + (grid[y1][x1] - grid[y1][x0]) * fx
    return top + (bot - top) * fy


def shade(x, y):
    n = 0.62 * sample(G4, x, y, 4) + 0.38 * sample(G8, x, y, 2)
    for lim, col in RAMP:
        if n < lim:
            return col
    return L1


for y in range(H):
    for x in range(W):
        c.set(x, y, shade(x, y))

# ---- mineral speckle + warm flecks ------------------------------------
rnd = random.Random(5)
cells = [(x, y) for x in range(W) for y in range(H)]
rnd.shuffle(cells)
for (x, y) in cells[:8]:
    wset(x, y, D3)
for (x, y) in cells[8:14]:
    wset(x, y, L2)
for (x, y) in cells[14:18]:
    wset(x, y, WM)

# small grit pits (2x2 clusters, wrap-safe)
for (px, py) in [(11, 6), (3, 7)]:
    wset(px, py, D3)
    wset(px + 1, py, D2)
    wset(px, py + 1, D2)
    wset(px + 1, py + 1, D3)

# ---- crack network (thin 1px fissures, wrap-safe) ----------------------
CRACKS = [
    # main diagonal fissure
    [(3, 2), (4, 3), (4, 4), (5, 5), (6, 5), (7, 6), (8, 6), (9, 7),
     (10, 8), (11, 9), (12, 10), (12, 11), (13, 12), (14, 13)],
    # branch peeling down-left
    [(7, 6), (7, 7), (6, 8), (6, 9), (5, 10), (5, 11)],
    # top-right crack wrapping across the vertical seam
    [(11, 1), (12, 2), (13, 2), (14, 3), (15, 4), (0, 4), (1, 5)],
    # short bottom-left fissure, wrapping through the horizontal seam
    [(1, 9), (2, 10), (2, 11), (3, 12), (3, 13), (4, 14), (4, 15), (5, 0), (6, 1)],
]

crack = set()
for path in CRACKS:
    for (x, y) in path:
        crack.add((x % W, y % H))

DEEP = {(5, 5), (7, 6), (9, 7), (12, 10), (13, 2), (0, 4), (2, 11), (3, 13)}

for (x, y) in sorted(crack):
    wset(x, y, C2 if (x, y) in DEEP else C1)

# shadow lip below each crack, chipped highlight above a few
for (x, y) in sorted(crack):
    bx, by = x % W, (y + 1) % H
    if (bx, by) not in crack:
        wset(bx, by, D3)
    if (x + y) % 3 == 0:
        tx, ty = x % W, (y - 1) % H
        if (tx, ty) not in crack:
            wset(tx, ty, L2)

print(c.stats_text())
view(c, scale=16, margin=0)

# seam check: 2x2 tiled preview (not submitted)
tiled = new_canvas(32, 32, name="tiled")
for ty in (0, 16):
    for tx in (0, 16):
        tiled.blit(c, tx, ty)
view(tiled, scale=12, margin=0)

save("stone_cracked", c, indexed=True)
finish(c)
