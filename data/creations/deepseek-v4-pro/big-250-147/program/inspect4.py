from pixelbench_api import *
from collections import Counter

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}
name_by_idx = {p['index']: p['name'] for p in pal}

# For each row group (5 rows), dominant color categories and avg RGB
for y0 in range(0, h, 10):
    y1 = min(y0+10, h)
    cnt = Counter()
    tot = [0,0,0]
    n = 0
    for y in range(y0, y1):
        for x in range(w):
            idx = c.get(x,y)
            r,g,b,a = rgba_by_idx[idx]
            cnt[(r//32*32, g//32*32, b//32*32)] += 1
            tot[0]+=r; tot[1]+=g; tot[2]+=b; n+=1
    avg = tuple(t//n for t in tot)
    tops = ', '.join(f"{rgb}:{n}" for rgb,n in cnt.most_common(4))
    print(f"y {y0:3d}-{y1-1:3d} avg={avg} top={tops}")

print("\n--- columns (10 px groups) ---")
for x0 in range(0, w, 10):
    x1 = min(x0+10, w)
    cnt = Counter()
    tot=[0,0,0]; n=0
    for y in range(h):
        for x in range(x0, x1):
            idx = c.get(x,y)
            r,g,b,a = rgba_by_idx[idx]
            cnt[(r//32*32, g//32*32, b//32*32)] += 1
            tot[0]+=r; tot[1]+=g; tot[2]+=b; n+=1
    avg = tuple(t//n for t in tot)
    tops = ', '.join(f"{rgb}:{n}" for rgb,n in cnt.most_common(3))
    print(f"x {x0:3d}-{x1-1:3d} avg={avg} top={tops}")
