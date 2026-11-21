exec(compile(open('main.py').read(), 'main.py', 'exec'), globals())

pal = {p['index']: p for p in f2.palette()}
def hexs(v):
    r = pal[v]['rgba']
    return r.lower() if isinstance(r, str) else '#%02x%02x%02x%02x' % tuple(r[:4])

CLS = {'#b0300eff': 'p', '#f27219ff': 'm', '#f4a30cff': 'n',
       '#fed32cff': 'o', '#fff3b0ff': 'Q'}

def classmap(c, x0, y0, x1, y1, label):
    print("### " + label)
    print("    " + ''.join(str((x // 10) % 10) for x in range(x0, x1 + 1)))
    print("    " + ''.join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        line = ''
        for x in range(x0, x1 + 1):
            v = c.get(x, y)
            if v is None:
                line += '.'
                continue
            h = hexs(v)
            line += '.' if h[-2:] == '00' else CLS.get(h, '#')
        print('%2d  %s' % (y, line))

classmap(f2, 0, 0, 99, 71, 'frame2 final')
print()
print('sizes', f1.stats()['size'], f2.stats()['size'])
print('palette:', [(p['index'], p['rgba']) for p in f2.palette()])
