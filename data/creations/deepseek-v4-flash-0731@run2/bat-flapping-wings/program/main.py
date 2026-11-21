from pixelbench_api import *

src = input_canvas
w, h = src.stats()['size']  # 27x22

# ---- Frame 1: original picture content (pixel-exact copy) ----
f1 = src.copy(name='f1')

# ---- Frame 2: wings raised and spread ----
f2 = src.copy(name='f2')

# Remove the drooping wings (side regions) so only face/body/legs area stays.
f2.clear(0, 6, 8, 16)      # left wing region, rows 6-21
f2.clear(8, 11, 2, 11)     # left inner, rows 11-21
f2.clear(17, 11, 2, 11)    # right inner, rows 11-21
f2.clear(19, 6, 8, 16)     # right wing region, rows 6-21

# Raised left wing: colour indices used are those already in the shared palette
# (0=bg/transparent, 1=dark outline, 8=deep purple, 4=body purple).
L = [
    (2, 1, 1), (3, 1, 4), (4, 1, 4), (5, 1, 4),
    (1, 2, 1), (2, 2, 4), (3, 2, 4), (4, 2, 4), (5, 2, 4), (6, 2, 4),
    (0, 3, 4), (1, 3, 8), (2, 3, 4), (3, 3, 4), (4, 3, 4), (5, 3, 4),
    (0, 4, 1), (1, 4, 4), (2, 4, 4), (3, 4, 4), (4, 4, 4), (5, 4, 4),
    (0, 5, 1), (1, 5, 4), (2, 5, 4), (3, 5, 4), (4, 5, 4), (5, 5, 4), (6, 5, 4),
    (0, 6, 1), (1, 6, 4), (2, 6, 4), (3, 6, 4), (4, 6, 4), (5, 6, 4), (6, 6, 4),
    (1, 7, 4), (2, 7, 4), (3, 7, 4), (4, 7, 4), (5, 7, 4), (6, 7, 4),
    (1, 8, 4), (2, 8, 4), (3, 8, 4), (4, 8, 4), (5, 8, 4), (6, 8, 4),
    (2, 9, 4), (3, 9, 4), (4, 9, 4), (5, 9, 4), (6, 9, 4),
    (2, 10, 4), (3, 10, 4), (4, 10, 4), (5, 10, 4), (6, 10, 4),
    (6, 11, 4), (7, 11, 1),
    (6, 12, 4), (7, 12, 1),
]
for (x, y, col) in L:
    f2.set(x, y, col)
    f2.set(26 - x, y, col)  # mirror for the right wing

# Sanity check: frame 1 is a pixel-exact copy of the input.
same = all(f1.get(x, y) == src.get(x, y) for x in range(w) for y in range(h))
print("f1 identical to input:", same)
print("f1:", f1.stats())
print("f2:", f2.stats())

finish([f1, f2])
