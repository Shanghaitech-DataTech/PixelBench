from pixelbench_api import *

c = input_canvas
names = {p['index']: p['name'] for p in c.palette()}
sym = {'c0': '.', 'c1': '#', 'c2': 'C', 'c3': 'D', 'c4': '4', 'c5': '5',
       'c6': '6', 'c7': '7', 'c8': '8', 'c9': '9'}
rows = []
for ly in range(32):
    row = [sym[names[c.get(lx * 2, ly * 2)]] for lx in range(32)]
    rows.append(row)
    liq = [lx for lx in range(32) if row[lx] in '456789']
    print(f'{ly:2d} liq={liq}'.ljust(40) + ''.join(row))
