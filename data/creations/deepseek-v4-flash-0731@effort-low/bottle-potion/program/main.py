from pixelbench_api import *

c = canvas(-1).copy(name='output')
pal = {p['index']: (p['rgba'][0], p['rgba'][1], p['rgba'][2]) for p in c.palette()}

# water colour -> purple map (rgba -> hex)
water_map = {
    (0x2f, 0x75, 0x98): '#4a1a8a',   # dark blue -> deep purple
    (0x74, 0xb8, 0xcf): '#8b3bd8',   # main light blue -> rich purple
    (0x77, 0xb7, 0xce): '#a05ae0',
    (0x76, 0xb7, 0xd1): '#b878e8',
    (0x7b, 0xb5, 0xcb): '#9a4ad8',
}

# replace water colours and record their bbox
minx, miny, maxx, maxy = 64, 64, -1, -1
for y in range(64):
    for x in range(64):
        idx = c.get(x, y)
        rgb = pal[idx]
        if rgb in water_map:
            c.set(x, y, water_map[rgb])
            if x < minx: minx = x
            if x > maxx: maxx = x
            if y < miny: miny = y
            if y > maxy: maxy = y

W = maxx - minx + 1
H = maxy - miny + 1

# bubble positions as relative fractions within the water bbox
bubbles = [
    (0.22, 0.62, 2), (0.40, 0.45, 3), (0.62, 0.55, 2),
    (0.50, 0.30, 2), (0.30, 0.38, 1), (0.68, 0.38, 1),
    (0.55, 0.20, 1), (0.36, 0.18, 1), (0.70, 0.70, 1),
    (0.18, 0.75, 1), (0.80, 0.48, 1), (0.62, 0.86, 1),
    (0.30, 0.55, 2), (0.74, 0.24, 1),
]

ring = '#cf9ff2'
hl = '#f4e4ff'

for fx, fy, r in bubbles:
    bx = int(minx + fx * (W - 1))
    by = int(miny + fy * (H - 1))
    if r >= 2:
        c.circle(bx, by, r, ring, fill=False)
        c.set(bx, by - r, hl)          # top highlight
    else:
        c.set(bx, by, ring)
        c.set(bx - 1, by - 1, hl)

finish(c)
