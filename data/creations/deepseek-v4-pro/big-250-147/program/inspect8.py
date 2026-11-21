from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}

def ch(r,g,b):
    lum=(r+g+b)//3
    if lum>=200:
        return 'S'
    if lum>=150:
        if r>b+30: return 'R'
        if b>r+20: return 'B'
        return '.'
    if lum>=100:
        if r>b+30: return 'r'
        if b>r+20: return 'b'
        return ':'
    if lum>=60:
        return '='
    return '#'

for y in range(0,70,2):
    line=''
    for x in range(0,w,2):
        r,g,b,a=rgba_by_idx[c.get(x,y)]
        line += ch(r,g,b)
    print(f"{y:3d} {line}")
