from pixelbench_api import *

c = input_canvas.copy(name='output')

CHOCO = 18   # palette index 18 = #95524c (chocolate scoop body)
LITE  = 24   # palette index 24 = #99544d (chocolate highlight)

# Each drip: (x0, [(y0,y1,x1), ...], highlight_rows). Runs go from the scoop's
# bottom edge down over the cone; later rows may get a narrower x1 as the drip
# tapers. The LITE pixel is placed on the left column of the drip.
drips = [
    # left stream
    (24, [(30, 33, 25), (34, 35, 24)], [31, 33]),
    # front-left stream
    (27, [(30, 34, 28), (35, 36, 27)], [32, 35]),
    # long centre stream, tapers down the middle of the cone
    (30, [(30, 36, 32), (37, 39, 31), (40, 40, 30)], [32, 35, 38]),
    # centre-right stream
    (34, [(30, 32, 35), (33, 38, 34)], [33, 36]),
    # right stream over the cone's right side
    (37, [(31, 37, 38), (38, 40, 37)], [33, 36, 39]),
    # drips running down the outside of the right flank
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

# a small bead left by the long centre drip
c.set(31, 43, CHOCO)

print(c.stats_text())
print(c.matrix_text(region=(22, 27, 47, 47), indices=False))
finish(c)
