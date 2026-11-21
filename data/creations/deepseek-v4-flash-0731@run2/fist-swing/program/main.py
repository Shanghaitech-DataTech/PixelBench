from pixelbench_api import *

src = input_canvas

f1 = src.copy(name='f1')
f2 = src.copy(name='f2')
f2.clear(0, 15, 9, 6)

A = '#222034'
C = '#eec39a'
E = '#df7126'
F = '#8f563b'

punch = [
    (15, 5, A), (15, 6, E), (15, 7, A), (15, 8, A),
    (16, 0, A), (16, 1, A), (16, 2, A), (16, 3, A), (16, 4, F),
    (16, 5, E), (16, 6, A), (16, 7, A), (16, 8, A),
    (17, 0, F), (17, 1, A), (17, 2, C), (17, 3, F), (17, 4, A),
    (17, 5, F), (17, 6, E), (17, 7, E), (17, 8, A),
    (18, 0, A), (18, 1, A), (18, 2, C), (18, 3, E), (18, 4, F),
    (18, 5, A), (18, 6, E), (18, 7, F), (18, 8, A),
    (19, 0, A), (19, 1, A), (19, 2, C), (19, 3, E), (19, 4, A),
    (19, 5, A), (19, 6, A), (19, 7, A),
    (20, 0, A), (20, 1, A), (20, 2, A),
]
for y, x, col in punch:
    f2.set(x, y, col)

changed = []
for y in range(44):
    for x in range(29):
        if f1.get(x, y) != f2.get(x, y):
            changed.append((x, y))
print("changed coords:", changed)
print("f2 arm close-up:")
print(f2.matrix_text(region=(0, 13, 22, 22)))
finish([f1, f2])
