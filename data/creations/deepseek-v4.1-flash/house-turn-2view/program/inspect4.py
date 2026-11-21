c = input_canvas
lum = {}
for p in c.palette():
    r, g, b, a = p['rgba']
    lum[p['index']] = None if a == 0 else int(round((0.299 * r + 0.587 * g + 0.114 * b) / 255 * 9))
w, h = 112, 157
step = 2
print('    ' + ''.join(str((x//step) % 10) for x in range(0, w, step)))
for y in range(0, h, step):
    row = ''
    for x in range(0, w, step):
        v = lum.get(c.get(x, y))
        row += '.' if v is None else str(min(v, 9))
    print('%3d %s' % (y, row))
