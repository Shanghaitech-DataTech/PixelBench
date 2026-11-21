# minecraft-stone-material : 16x16 seamless cracked stone tile
from pixelbench_api import *

W = H = 16
c = new_canvas(W, H, background=None, name="stone")

BASE  = c.color("#7f7f7f", name="base")
LIGHT = c.color("#949494", name="light")
MIDLT = c.color("#8a8a8a", name="midlt")
DARK  = c.color("#6b6b6b", name="dark")
CRACK = c.color("#585858", name="crack")
CORE  = c.color("#3e3e3e", name="core")

c.rect(0, 0, W, H, BASE)


def put(px, col):
    for (x, y) in px:
        c.set(x % W, y % H, col)


# ---- clustered stone grain (blotches, not uniform static) -----------
GRAIN_MID = [(5, 0), (7, 0), (11, 2), (0, 2), (3, 2), (9, 3), (12, 4),
             (15, 4), (8, 5), (4, 7), (1, 9), (5, 10), (11, 10), (15, 8),
             (15, 12), (6, 14), (9, 15), (5, 13), (14, 6), (0, 10)]
GRAIN_LIGHT = [(2, 0), (3, 0), (2, 1), (8, 1), (9, 1), (14, 3), (15, 3),
               (6, 4), (7, 4), (3, 5), (4, 5), (12, 10), (3, 11), (4, 11),
               (10, 13), (11, 13), (0, 13)]
GRAIN_DARK = [(12, 0), (13, 0), (6, 2), (7, 2), (0, 4), (1, 4), (10, 5),
              (10, 2), (11, 15), (7, 11), (13, 11), (14, 11), (1, 14),
              (2, 14), (13, 14), (14, 14)]

put(GRAIN_MID, MIDLT)
put(GRAIN_LIGHT, LIGHT)
put(GRAIN_DARK, DARK)

# ---- crack network ---------------------------------------------------
# main fissure wanders across the tile and rejoins itself over the seam
MAIN = [(0, 6), (1, 6), (2, 7), (3, 7), (4, 8), (5, 8), (6, 7), (7, 7),
        (8, 7), (9, 8), (10, 9), (11, 9), (12, 8), (13, 8), (14, 7), (15, 6)]
FORK_UP = [(8, 6), (9, 5), (9, 4)]                     # splinter to the top
FORK_DN = [(10, 10), (11, 11), (11, 12)]               # splinter to the base
SMALL   = [(2, 11), (3, 12), (4, 12), (5, 13), (6, 13)]  # second fissure
WIDE    = [(4, 7), (11, 8)]                            # thicker at the turns

# carved relief: shadowed groove wall below, lit lip above (light from top)
put([(1, 7), (2, 8), (6, 8), (9, 9), (12, 9), (13, 9), (3, 13), (4, 13)], DARK)
put([(0, 5), (2, 6), (6, 6), (9, 7), (13, 7), (15, 5)], LIGHT)

for path in (MAIN, FORK_UP, FORK_DN, SMALL, WIDE):
    put(path, CRACK)

# deepest pits of the fissure
put([(4, 8), (10, 9), (11, 12)], CORE)

print(c.stats_text())
print(c.matrix_text())

save("minecraft-stone", c)
finish(c)
