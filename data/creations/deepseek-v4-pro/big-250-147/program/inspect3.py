from pixelbench_api import *
from collections import Counter

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}
name_by_idx = {p['index']: p['name'] for p in pal}

thresholds = [160, 180, 200, 220, 240]
for t in thresholds:
    xs=[]; ys=[]
    for y in range(h):
        for x in range(w):
            r,g,b,a = rgba_by_idx[c.get(x,y)]
            lum = (r+g+b)//3
            if lum >= t:
                xs.append(x); ys.append(y)
    if xs:
        print(f"lum>={t}: count={len(xs)} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)})")
    else:
        print(f"lum>={t}: none")

cnt=Counter()
for y in range(h):
    for x in range(w):
        idx=c.get(x,y)
        r,g,b,a=rgba_by_idx[idx]
        if (r+g+b)//3>=180:
            cnt[(idx, r,g,b)] += 1
print("bright colors (lum>=180):")
for (idx, r,g,b), n in cnt.most_common(30):
    print(idx, name_by_idx[idx], (r,g,b), n)

cnt2=Counter()
for y in range(h):
    for x in range(w):
        idx=c.get(x,y)
        r,g,b,a=rgba_by_idx[idx]
        if r>180 and g>120 and b<160:
            cnt2[(idx, r,g,b)] += 1
print("warm bright colors:")
for (idx, r,g,b), n in cnt2.most_common(30):
    print(idx, name_by_idx[idx], (r,g,b), n)
