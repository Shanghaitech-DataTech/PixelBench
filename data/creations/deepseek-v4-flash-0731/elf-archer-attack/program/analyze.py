from pixelbench_api import *

c = input_canvas
letters = {}
import string
avail = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
for y in range(47):
    for x in range(35):
        idx = c.get(x, y)
        if idx not in letters:
            letters[idx] = avail[len(letters)]

def show(x0, y0, x1, y1, label):
    print(f'--- {label} ({x0},{y0})-({x1},{y1}) ---')
    print('    ' + ''.join(f'{x%10}' for x in range(x0, x1+1)))
    for y in range(y0, y1+1):
        print(f'{y:2d}  ' + ''.join(letters.get(c.get(x, y), '?') for x in range(x0, x1+1)))
    print()

show(9, 0, 22, 14, 'HEAD+FACE')
show(14, 0, 34, 26, 'BOW SIDE')
show(15, 25, 34, 44, 'LEGS RIGHT')
show(0, 25, 20, 46, 'LEGS LEFT')
