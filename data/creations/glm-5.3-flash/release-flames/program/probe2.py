from pixelbench_api import *

def dump(c, x0, x1, y0, y1, label=''):
    print(label)
    print('     ' + ''.join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ''
        for x in range(x0, x1 + 1):
            v = c.get(x, y)
            row += '.' if v == 0 else ('%x' % v)
        print(f'{y:3d}  ' + row)

dump(input_canvas, 26, 46, 16, 27, 'ORIGINAL x26-46, y16-27 (idx hex)')
print()
dump(input_canvas, 26, 46, 0, 15, 'ORIGINAL x26-46, y0-15 (idx hex)')
