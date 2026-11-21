from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
# ids: gold set {10,22,25,32,40}, brown weapon {7}, white {31}
gold = {10,22,25,32,40}
for y in range(h):
    row = []
    for x in range(w):
        idx = c.get(x,y)
        if idx in gold:
            row.append('$')
        elif idx == 7:
            row.append('g')
        elif idx == 31:
            row.append('W')
        else:
            row.append('.')
    print(f"{y:02d} {''.join(row)}")
