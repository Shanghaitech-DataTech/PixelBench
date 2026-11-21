from pixelbench_api import *

out = input_canvas.copy(name='output')
W, H = 82, 135
FO = (1,2,3,4)

def is_foil(idx):
    return idx in FO

tiers = [
    (0, 6),
    (7, 19),
    (20, 38),
    (39, 57),
    (58, 77),
    (78, 98),
    (99, 121),
]

snow = out.color((236, 241, 245, 255), name='snow')

for (t0, t1) in tiers:
    ext = [x for x in range(W) for y in range(t0, t1+1) if is_foil(out.get(x,y))]
    if not ext:
        continue
    xs = range(min(ext), max(ext)+1)
    # compute topmost and second rows per column
    rows_per_x = {}
    for x in xs:
        cols = [y for y in range(t0, t1+1) if is_foil(out.get(x,y))]
        rows_per_x[x] = cols
    # paint snow on top 3 rows of each column's foliage in tier
    for x, cols in rows_per_x.items():
        for yy in cols[:3]:
            out.set(x, yy, snow)

print(out.stats_text())
print(out.stats_text())
finish(out)
