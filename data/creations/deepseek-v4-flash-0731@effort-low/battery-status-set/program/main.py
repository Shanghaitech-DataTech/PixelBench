from pixelbench_api import *

c = new_canvas(64, 64)

outline = "#2a2e33"
interior = "#eef2f6"
green   = "#3baf4d"
red     = "#e2473b"
bolt    = "#ffd33d"

def battery(x, y, pct, charging=False):
    # terminal nub
    c.rect(x + 5, y, 4, 4, outline)
    # body outline (thick, single fill giving 1px border)
    c.rect(x, y + 4, 14, 36, outline)
    # interior
    c.rect(x + 2, y + 6, 10, 32, interior)
    # charge fill (interior bottom row = y+6+31 = y+37)
    ib = y + 37
    if charging:
        h = 14  # partial fill while charging
        c.rect(x + 2, ib - h + 1, 10, h, green)
        pts = [(x + 3, y + 14), (x + 11, y + 14), (x + 8, y + 21),
               (x + 12, y + 21), (x + 4, y + 32), (x + 7, y + 32),
               (x + 5, y + 24), (x + 2, y + 24)]
        c.poly(pts, bolt)
    else:
        h = int(32 * pct / 100.0)
        col = green if pct >= 60 else red
        c.rect(x + 2, ib - h + 1, 10, h, col)

top = 6
battery(2,  top, 100)
battery(18, top, 60)
battery(34, top, 20)
battery(50, top, 20, charging=True)

result = c
finish(result)
