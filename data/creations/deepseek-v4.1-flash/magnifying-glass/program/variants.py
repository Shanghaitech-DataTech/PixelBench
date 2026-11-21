import math
from pixelbench_api import *

GOLD_L = '#f7dd8a'
GOLD   = '#d9a532'
GOLD_D = '#96681a'
GLASS  = '#cfeaf9'
GLASS_D= '#a3d3ee'
SHINE  = '#ffffff'
CX, CY = 6, 6


def build(name, handle_w=2, glass_dark_at=4, shine=None, handle_span=(4, 9)):
    c = new_canvas(16, 16, name=name)
    handle = {}
    for s in range(*handle_span):
        handle[(CX + s, CY + s)] = GOLD
        handle[(CX + s - 1, CY + s)] = GOLD_D
        if handle_w == 3:
            handle[(CX + s + 1, CY + s)] = GOLD_D
    for y in range(16):
        for x in range(16):
            if (x, y) in handle:
                c.set(x, y, handle[(x, y)])
                continue
            dx, dy = x - CX, y - CY
            d = math.hypot(dx, dy)
            if d <= 3.5:
                c.set(x, y, GLASS_D if dx + dy >= glass_dark_at else GLASS)
            elif d <= 5.45:
                v = dx + dy
                c.set(x, y, GOLD_L if v <= -5 else (GOLD if v <= 3 else GOLD_D))
    if shine is None:
        shine = [(5, 3), (4, 4), (4, 5)]
    for (x, y) in shine:
        c.set(x, y, SHINE)
    return c


a = build("A_2px", handle_w=2, glass_dark_at=4)
b = build("B_3px", handle_w=3, glass_dark_at=4)
d = build("D_2px_gd3", handle_w=2, glass_dark_at=3)
e = build("E_3px_gd3", handle_w=3, glass_dark_at=3)

for cc in (a, b, d, e):
    print("=====", cc)
    print(cc.matrix_text())
