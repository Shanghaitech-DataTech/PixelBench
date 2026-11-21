import math
from pixelbench_api import *
exec(open('main.py').read().split("frames = {}")[0])

th = -90
for lbl, p in [('ridgeF', (-3, -9, 84)), ('ridgeTopC', (0, 40, 84)), ('eaveE', (EX, 40, EZ)),
               ('walltopE', (W/2, 40, H)), ('baseE', (W/2, 40, 0)), ('roofridge', (0, 40, H+R))]:
    print(lbl, [round(v, 1) for v in proj(p, th)])

cv = new_canvas(120, 129, name='dbg')
items = build_frame(th)
x0, y0, x1, y1 = bbox_of(items)
ox = (120 - (x1 - x0)) / 2 - x0
oy = (129 - (y1 - y0)) / 2 - y0
for _, _, op in items:
    if op[0] == 'fill':
        cv.poly([(round(x + ox), round(y + oy)) for (x, y) in op[1]], op[2], True)
    elif op[0] == 'oline':
        oline(cv, [(round(x + ox), round(y + oy)) for (x, y) in op[1]], op[2], op[3])
    else:
        tline(cv, (round(op[1][0] + ox), round(op[1][1] + oy)), (round(op[2][0] + ox), round(op[2][1] + oy)), op[3], op[4])
col = 60
prev = None
for y in range(129):
    i = cv.get(col, y)
    if i != prev:
        print(y, cv.color_name(i))
        prev = i
