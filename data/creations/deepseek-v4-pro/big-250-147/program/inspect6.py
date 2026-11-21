from pixelbench_api import *
from collections import Counter

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}
name_by_idx = {p['index']: p['name'] for p in pal}

def region_stats(x0,y0,x1,y1,label):
    cnt=Counter()
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            idx=c.get(x,y)
            cnt[idx]+=1
    print(f"\n{label} region x{x0}-{x1} y{y0}-{y1}:")
    for idx,n in cnt.most_common(15):
        r,g,b,a=rgba_by_idx[idx]
        print(f"  idx{idx} {name_by_idx[idx]} rgba={(r,g,b,a)} count={n}")

region_stats(80,50,170,110,"horizon area")
region_stats(0,0,249,70,"sky area")
region_stats(0,100,249,146,"bottom area")
region_stats(0,60,249,100,"mid area")

print("\ncrop x80-170 y60-110 (every 2 px), showing lum & warm category:")
for y in range(60,111,2):
    line=''
    for x in range(80,171,2):
        idx=c.get(x,y)
        r,g,b,a=rgba_by_idx[idx]
        lum=(r+g+b)//3
        if lum>=200: ch='S'
        elif lum>=150:
            ch='R' if r>b+30 else '.'
        elif lum>=100:
            ch='r' if r>b+30 else ':'
        elif lum>=60: ch='='
        else: ch='#'
        line+=ch
    print(f"{y:3d} {line}")
