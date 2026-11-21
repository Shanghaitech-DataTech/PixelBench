from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
pal = c.palette()
rgba_by_idx = {p['index']: tuple(p['rgba']) for p in pal}

# Build coarse ascii by brightness and hue category.
# Sample every 5 px -> 50 x 30 cells approx.
sx, sy = 5, 5
rows = []
for y in range(0, h, sy):
    line = ''
    for x in range(0, w, sx):
        idx = c.get(x, y)
        r, g, b, a = rgba_by_idx[idx]
        lum = (r+g+b)//3
        # classify
        if lum < 40:
            ch = '#'
        elif lum < 80:
            ch = '='
        elif lum < 120:
            ch = '-'
        elif lum < 160:
            ch = '.'
        elif lum < 200:
            ch = ':'
        else:
            ch = ' '
        # hue-ish: if red > blue + 30 -> warm
        if r > b + 30 and lum >= 40:
            ch = 'r'
        if b > r + 20 and lum >= 40:
            ch = 'b'
        line += ch
    rows.append(f"{y:3d} {line}")
print('\n'.join(rows))
