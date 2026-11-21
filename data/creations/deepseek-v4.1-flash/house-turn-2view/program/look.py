import runpy
# re-run main to build frames? Instead inspect saved canvases by name
targets = ['frame45', 'frame90']
for nm in targets:
    c = canvas(nm)
    print('=====', nm, c.stats_text())
    pal = c.palette()
    sym = {}
    chars = '.#ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    used = {}
    for p in pal:
        used[p['index']] = p
    legend = []
    for p in pal:
        sym[p['index']] = '.'
    # assign symbols to non transparent
    k = 0
    letters = '#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for p in pal:
        if p['rgba'][3] == 0:
            continue
        sym[p['index']] = letters[k]
        legend.append((letters[k], p['index'], p['name'], p['rgba']))
        k += 1
    W, H = 112, 157
    step = 3
    print('    ' + ''.join(str((x // step) % 10) for x in range(0, W, step)))
    for y in range(0, H, step):
        row = ''
        for x in range(0, W, step):
            row += sym.get(c.get(x, y), '?')
        print('%3d %s' % (y, row))
    for L in legend:
        print(L)
