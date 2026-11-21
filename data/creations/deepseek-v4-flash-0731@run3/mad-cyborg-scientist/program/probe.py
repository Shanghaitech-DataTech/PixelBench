import math
from pixelbench_api import new_canvas

c = new_canvas(64, 64, background=None)
c.color('#0d1022', name='bg')
c.color('#a8aeb8', name='metal')

def half(side, rx=17, ry=19, cy=29):
    pts = [(32, cy - ry)]
    for y in range(cy - ry + 1, cy + ry):
        dx = int(round(rx * math.sqrt(max(0.0, 1 - ((y - cy) / ry) ** 2))))
        pts.append((32 + (dx if side == 'r' else -dx), y))
    pts.append((32, cy + ry))
    return pts

c.poly(half('r'), c.color('metal'))
m = c.matrix_text(region=(30, 14, 50, 24), indices=False)
print(m)
