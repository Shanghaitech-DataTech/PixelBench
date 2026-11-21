from pixelbench_api import *

white = input_canvas.color('#ffffffff')
xs=[]; ys=[]
for y in range(64):
    for x in range(64):
        if input_canvas.get(x,y) != white:
            xs.append(x); ys.append(y)
print('bbox', min(xs), min(ys), max(xs), max(ys), 'count', len(xs))
# print col ranges per row
for y in range(min(ys), max(ys)+1):
    cols=[x for x in range(64) if input_canvas.get(x,y)!=white]
    if cols:
        print(y, min(cols), max(cols), len(cols))
