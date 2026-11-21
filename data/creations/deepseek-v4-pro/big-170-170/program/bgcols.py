from pixelbench_api import *

c = input_canvas
for y in range(60, 114):
    cols=[]
    for x in range(60, 81):
        idx = c.get(x,y)
        cols.append(c.color_name(idx) if idx is not None else 'None')
    print(y, cols)
