from pixelbench_api import *

c_out = input_canvas.copy(name='output')

choc = '#5e363e'          # main chocolate (matches scoop fill c4)
chocdark = '#613942'      # darker chocolate (c1)
hi = '#95524c'            # highlight brown

# Each drip: (x, top, bottom, midwidth, bottomwidth)
# Rounded drip ends: widen at the bottom into a blob.
drips = [
    (24, 31, 42, 2, 3),
    (28, 31, 36, 2, 3),
    (31, 30, 39, 2, 2),
    (34, 30, 46, 3, 4),
    (38, 31, 54, 3, 5),
    (42, 31, 44, 3, 3),
    (45, 30, 39, 2, 3),
    (48, 33, 50, 2, 3),
    (39, 30, 34, 2, 2),
    (18, 31, 38, 1, 2),
    (21, 31, 33, 1, 2),
    (30, 31, 34, 1, 2),
    (43, 30, 36, 1, 2),
    (50, 34, 42, 1, 2),
    (36, 31, 41, 1, 2),
]

for (x, top, bot, w, bw) in drips:
    # main vertical column (chocolate)
    c_out.rect(x, top, w, bot - top + 1, choc)
    # rounded widening at the hanging tip
    c_out.rect(x - 1, bot, bw + 2, 1, choc)
    c_out.rect(x, top, 1, bot - top + 1, hi)          # glossy highlight on one side
    # small darker shadow on the right edge of wide drips
    if w >= 3:
        c_out.rect(x + w - 1, top + 2, 1, bot - top - 1, chocdark)

# A couple of drops that already reached the lower cone.
drops = [(36, 49), (40, 52), (46, 46), (30, 45), (49, 48), (33, 42), (26, 43), (44, 49), (38, 51)]
for (dx, dy) in drops:
    c_out.circle(dx, dy, 1, choc)
    c_out.set(dx, dy, hi)

print(c_out.stats_text())

finish(c_out)
