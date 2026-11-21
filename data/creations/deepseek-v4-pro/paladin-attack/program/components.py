from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']

# non-transparent pixels
nontrans = set()
for y in range(h):
    for x in range(w):
        idx = c.get(x,y)
        if idx != 0:
            nontrans.add((x,y))

seen = set()
comps = []
for (x,y) in sorted(nontrans):
    if (x,y) in seen:
        continue
    stack = [(x,y)]
    seen.add((x,y))
    comp = []
    while stack:
        px,py = stack.pop()
        comp.append((px,py))
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = px+dx, py+dy
            if (nx,ny) in nontrans and (nx,ny) not in seen:
                seen.add((nx,ny))
                stack.append((nx,ny))
    comps.append(comp)

comps.sort(key=len, reverse=True)
print("num components:", len(comps))
for i, comp in enumerate(comps[:15]):
    xs=[p[0] for p in comp]; ys=[p[1] for p in comp]
    # color composition
    from collections import Counter
    colc = Counter(c.get(x,y) for x,y in comp)
    top = colc.most_common(5)
    print(f"comp{i}: n={len(comp)} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)}) colors={top}")
