from pixelbench_api import *

c = input_canvas.copy(name='output')
# rebuild drips (same as main run)
CHOCO = 18
LITE = 24
drips = [
    (24, [(30, 33, 25), (34, 35, 24)], [31, 33]),
    (27, [(30, 34, 28), (35, 36, 27)], [32, 35]),
    (30, [(30, 36, 32), (37, 39, 31), (40, 40, 30)], [32, 35, 38]),
    (34, [(30, 32, 35), (33, 38, 34)], [33, 36]),
    (37, [(31, 37, 38), (38, 40, 37)], [33, 36, 39]),
    (40, [(31, 34, 41), (34, 35, 41)], [32, 34]),
    (43, [(29, 33, 44), (34, 34, 43)], [30, 32]),
]
for x0, segs, hl in drips:
    for y0, y1, x1 in segs:
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                c.set(x, y, CHOCO)
            if y in hl:
                c.set(x0, y, LITE)
c.set(31, 43, CHOCO)

print(c.matrix_text(region=(22, 27, 51, 38), indices=False))
