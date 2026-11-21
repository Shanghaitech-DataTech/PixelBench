from pixelbench_api import *

# Frame 1: original content unchanged
f1 = input_canvas.copy(name="frame1")

# Frame 2: paladin swings weapon down
f2 = input_canvas.copy(name="frame2")

W = f2.stats()['size'][0]
H = f2.stats()['size'][1]

# Colours (shared palette; use hex to be safe)
GOLD = '#af7a18'    # j - bright gold blade core
BROWN = '#512a13'   # g - dark brown blade edge
TAN = '#d1b563'     # z - tan highlight at blade tip
WHITE = '#ffffff'   # motion trail
DARK = '#101010'    # outline

# ------------------------------------------------------------------
# 1. Erase the old raised weapon (two golden blade segments on right)
# ------------------------------------------------------------------
upper_clear = [
    (24,6),(25,6),(26,6),(27,6),(28,6),
    (24,7),(25,7),(26,7),(27,7),
    (24,8),(25,8),(26,8),(27,8),(28,8),(29,8),
    (25,9),(26,9),(27,9),(28,9),(29,9),(30,9),
    (24,10),(25,10),(26,10),(27,10),(28,10),(29,10),(30,10),(31,10),(32,10),(33,10),
    (26,11),(27,11),(28,11),(29,11),(30,11),(31,11),
    (28,12),(29,12),(30,12),
]

lower_clear = [
    (34,15),(35,15),(36,15),(37,15),
    (35,16),(36,16),(37,16),(38,16),
    (36,17),(37,17),(38,17),(39,17),(40,17),
    (37,18),(38,18),(39,18),(40,18),(41,18),(42,18),
    (38,19),(39,19),(40,19),(41,19),(42,19),
    (39,20),(40,20),(41,20),(42,20),
]

for (x, y) in upper_clear + lower_clear:
    f2.set(x, y, None)

# ------------------------------------------------------------------
# 2. White motion trail arcing from old raised position down to the
#    new downward blade position
# ------------------------------------------------------------------
trail = [
    (24,6),(26,8),(28,10),(30,12),(32,14),(34,16),(36,18),(37,20),
    (36,22),(35,24),(34,26),(34,28),(34,30),(34,32),(34,34),(33,36),(32,38)
]
for i in range(len(trail) - 1):
    x0, y0 = trail[i]
    x1, y1 = trail[i+1]
    f2.line(x0, y0, x1, y1, WHITE)

# ------------------------------------------------------------------
# 3. Draw the new weapon swung down: guard + downward golden blade
# ------------------------------------------------------------------
# crossguard under the hands
for x in range(28, 36):
    f2.set(x, 23, GOLD)

# blade pointing straight down (g edge / gold core / g edge), tapering tip
for y in range(24, 38):
    f2.set(30, y, BROWN)
    f2.set(31, y, GOLD)
    f2.set(32, y, BROWN)
# taper
f2.set(30, 38, BROWN)
f2.set(31, 38, GOLD)
f2.set(31, 39, BROWN)   # point of the blade

# small white glint on the blade
f2.set(31, 27, WHITE)
f2.set(31, 33, WHITE)

# ------------------------------------------------------------------
# 4. Left foot steps forward (shift lower left leg/foot to the right)
# ------------------------------------------------------------------
def shift_region(c, x0, y0, x1, y1, dx, dy):
    px = {}
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            idx = c.get(x, y)
            if idx != 0:
                px[(x, y)] = idx
    for (x, y) in px:
        c.set(x, y, None)
    for (x, y), idx in px.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H:
            c.set(nx, ny, idx)

shift_region(f2, 0, 48, 17, 56, 4, 0)

# ------------------------------------------------------------------
# Inspect the result
# ------------------------------------------------------------------
print("f1 stats:", f1.stats_text())
print("f2 stats:", f2.stats_text())
print("=== f2 upper/right (swing + trail) ===")
print(f2.matrix_text(region=(18, 4, 42, 42)))
print("=== f2 feet ===")
print(f2.matrix_text(region=(0, 44, 40, 52)))

finish([f1, f2])
