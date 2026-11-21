from pixelbench_api import *
import main as m
c = m.c
pal = c.palette()
names = {p['index']: p['name'] for p in pal}
def dump(x0, y0, x1, y1):
    print("=== region (%d,%d)-(%d,%d) ===" % (x0, y0, x1, y1))
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            i = c.get(x, y)
            row.append(names.get(i, str(i))[:1])
        print("%3d| %s" % (y, " ".join(row)))
dump(0, 90, 135, 210)
