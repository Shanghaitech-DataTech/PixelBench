from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}

def ch(r,g,b):
    lum=(r+g+b)//3
    if r>g+12 and r>b+12:
        base='r'
    elif b>r+8 and b>g+4:
        base='b'
    else:
        base='.'
    if lum<20:
        return '#'
    if lum<40:
        return base.upper()
    if lum<70:
        return base
    return '='

for y in range(90,147,2):
    line=''
    for x in range(0,w,2):
        r,g,b,a=rgba_by_idx[c.get(x,y)]
        line += ch(r,g,b)
    print(f"{y:3d} {line}")
