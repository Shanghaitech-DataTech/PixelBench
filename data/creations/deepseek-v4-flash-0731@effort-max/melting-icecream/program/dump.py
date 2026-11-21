from pixelbench_api import *

c = input_canvas
W, H = c.stats()['size']
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#'
pals = c.palette()
# map palette index -> glyph
glyph = {}
for idx in range(64):
    glyph[idx] = chars[idx]
rows = []
for y in range(H):
    row = ''.join(glyph[c.get(x, y)] for x in range(W))
    rows.append(row)
print('     ' + ''.join(str((x//10)%10) for x in range(W)))
print('     ' + ''.join(str(x%10) for x in range(W)))
for y, r in enumerate(rows):
    print('%02d  %s' % (y, r))
print()
print('legend:')
for p in pals:
    if p['index'] in glyph:
        print('  %s = idx%02d %s %s' % (glyph[p['index']], p['index'], p['name'] or '', p['rgba']))
