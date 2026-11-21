from pixelbench_api import *

# palette indices from input: 1=body outline, 3=pink, 4=dark purple, 5=gray-purple, 8=mid purple
O, P, D, G, M = 1, 3, 4, 5, 8

f1 = input_canvas.copy(name="frame1")   # original picture content, untouched
f2 = input_canvas.copy(name="frame2")

# --- erase drooping wings (rows 6-21, cols 0-9 and mirrored 17-26),
#     then restore body outline pixels that live on x=9 / x=17
f2.clear(0, 6, 10, 16)
f2.clear(17, 6, 10, 16)
for (x, y) in [(9, 8), (9, 9), (9, 10), (17, 8), (17, 9), (17, 10)]:
    f2.set(x, y, O)

# --- raised, spread left wing: membrane interior ...
interior = [
    (2, 1, P), (3, 1, G),
    (2, 2, P), (3, 2, G), (4, 2, M),
    (1, 3, P), (2, 3, P), (3, 3, G), (4, 3, M), (5, 3, M),
    (2, 4, P), (3, 4, G), (4, 4, M), (5, 4, M), (6, 4, M),
    (3, 5, P), (4, 5, G), (5, 5, M), (6, 5, M), (7, 5, M),
    (4, 6, P), (5, 6, G), (6, 6, M), (7, 6, M), (8, 6, M), (9, 6, M),
    (5, 7, P), (6, 7, G), (7, 7, M), (8, 7, M), (9, 7, M),
    (6, 8, P), (7, 8, G), (8, 8, M),
    (7, 9, P), (8, 9, M),
    (8, 10, M),
]
# ... and its dark-purple outline
edge = [
    (2, 0), (3, 0),
    (1, 1), (4, 1),
    (1, 2), (5, 2),
    (0, 3), (6, 3),
    (1, 4), (7, 4),
    (2, 5), (8, 5),
    (3, 6), (4, 7), (5, 8), (6, 9), (7, 10), (8, 11),
]
for (x, y, c) in interior:
    f2.set(x, y, c)
    f2.set(26 - x, y, c)   # mirrored right wing
for (x, y) in edge:
    f2.set(x, y, D)
    f2.set(26 - x, y, D)

print(f2.stats_text())
view(f1)
view(f2)
finish([f1, f2])
