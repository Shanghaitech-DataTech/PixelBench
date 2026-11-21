from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
print("size", w, h)

# list pixels per color index for interesting colors
for idx in range(len(c.palette())):
    name = c.color_name(idx)
    rgba = c.palette()[idx]['rgba']
    px = [(x,y) for y in range(h) for x in range(w) if c.get(x,y)==idx]
    if px:
        xs = [p[0] for p in px]; ys=[p[1] for p in px]
        print(f"idx{idx} {name} {rgba} n={len(px)} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)})")
