from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}

def ch(r,g,b):
    lum=(r+g+b)//3
    # warmness: red excess over blue
    if lum>=200:
        return 'S'      # sun/cream
    if r > b + 40:
        base = 'r'      # warm pink/red
    elif b > r + 20:
        base = 'b'
    else:
        base = 'n'      # neutral/purple
    if lum>=150:
        return base.upper() if base!='n' else '.'
    if lum>=100:
        return base if base!='n' else ':'
    if lum>=60:
        return '='
    return '#'

# sample every 3 px -> 84 cols x 49 rows
for y in range(0, h, 3):
    line=''
    for x in range(0, w, 3):
        idx=c.get(x,y)
        r,g,b,a=rgba_by_idx[idx]
        line += ch(r,g,b)
    print(f"{y:3d} {line}")
