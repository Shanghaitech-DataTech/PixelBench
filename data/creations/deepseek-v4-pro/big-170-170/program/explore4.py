from pixelbench_api import *

c = input_canvas
W,H = 170,170

def sym(idx):
    if idx is None:
        return ' '
    p = c.palette()[idx]['rgba']
    r,g,b,a = p
    if a == 0:
        return ' '
    mx = max(r,g,b); mn = min(r,g,b)
    sat = mx-mn
    # bright cyan/white/blue light
    if b >= 150 and g >= 100 and b >= r:
        return 'C'
    # bright warm / skin / product
    if r >= 150 and g >= 100 and r >= b:
        return 'H'
    # purple/pink
    if r >= 90 and b >= 80 and g < r and g < b and b > 60:
        return 'P'
    # warm brown/red mid
    if r >= 70 and g < r and b < r and sat >= 20:
        return 'S'
    # olive / brown dark
    if r < 80 and g < 80 and b < 50 and g >= r and b < g:
        return '|'
    # green dark
    if g > r and g >= b and g < 120 and b < 120:
        return 'G'
    # very dark
    if mx < 45:
        return '#'
    # dark blue/teal (background)
    if b >= r and b > g and b < 150:
        return '.'
    # light gray
    if r >= 120 and g >= 120 and b >= 120:
        return 'W'
    # fallback
    return '?'

for y in range(H):
    row=[]
    for x in range(W):
        row.append(sym(c.get(x,y)))
    print(f'{y:3d} '+''.join(row))
