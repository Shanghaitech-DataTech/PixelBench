from pixelbench_api import *

c = input_canvas
w,h = c.size if hasattr(c,'size') else (35,47)
# size is tuple? print
print('size', c.stats()['size'])
ids = [p['index'] for p in c.palette()]
for p in c.palette():
    idx = p['index']
    name = p['name']
    hexv = p['rgba']
    pts = []
    for y in range(47):
        for x in range(35):
            if c.get(x,y) == idx:
                pts.append((x,y))
    if not pts:
        continue
    xs = [x for x,y in pts]; ys=[y for x,y in pts]
    bbox=(min(xs),min(ys),max(xs),max(ys))
    print(f"idx {idx} {name} {hexv} n={len(pts)} bbox={bbox} centroid=({sum(xs)/len(xs):.1f},{sum(ys)/len(ys):.1f})")
