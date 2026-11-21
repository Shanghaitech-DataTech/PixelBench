from pixelbench_api import *

c = input_canvas
names = {p['index']: p['name'] for p in c.palette()}
sym = {'c0': '.', 'c1': '#', 'c2': 'C', 'c3': 'D', 'c4': '4', 'c5': '5',
       'c6': '6', 'c7': '7', 'c8': '8', 'c9': '9', 'transparent': ' '}
print('    ' + ''.join(str((x//2)//10) for x in range(0, 64, 2)))
print('    ' + ''.join(str((x//2) % 10) for x in range(0, 64, 2)))
for y in range(0, 64, 2):
    row = ''.join(sym[names[c.get(x, y)]] for x in range(0, 64, 2))
    print(f'{y//2:3d} ' + row)
