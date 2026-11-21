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
    if r < 45 and b > 60 and b > r:
        return '.'
    if r < 45 and g < 45 and b < 45:
        return '#'
    if g > r and g > b and g < 110:
        return ','
    if r > 90 and g < 110 and b < 110 and r > b:
        return 'S'
    if r > 150 and g > 110 and b < 110:
        return 'H'
    if b > 120 and g > 100 and r < 130:
        return 'C'
    if r > 130 and g > 120 and b > 120 and r < 200:
        return 'w'
    return '?'

# print 2x2 downsampled majority symbol by picking top-left of each block
for by in range(0, H, 3):
    row=[]
    for bx in range(0, W, 3):
        # take color at bx,by
        idx = c.get(bx,by)
        row.append(sym(idx))
    print(f'{by:3d} '+''.join(row))
