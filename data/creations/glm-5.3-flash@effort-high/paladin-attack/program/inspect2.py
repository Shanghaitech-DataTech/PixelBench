c = input_canvas
w, h = 43, 61
fam = {
    'outline': '#101010', 'skin': None, 'pink': None, 'steel': None,
    'gold': None, 'white': None, 'shadow': None, 'dark': None, 'red': None,
}
# classify by rgb
import pixelbench_api as api
pal = {p['index']: p['rgba'] for p in c.palette()}
def famof(idx):
    r, g, b, a = pal[idx]
    if a == 0: return '.'
    if r < 30 and g < 30 and b < 30: return '#'          # black outline
    if a < 255: return '~'                                # shadow alpha
    if r > 230 and g > 230 and b > 230: return 'W'        # white
    if r > 200 and g > 180 and b > 150: return 'P'        # pale cream/gold light
    if r > 180 and b > 120 and g < r - 40 and b > g: return 'p'  # pink/magenta
    if r > 100 and g < 80 and b < 90 and r > b: return 'r'  # dark red/maroon
    if r > 140 and g > 90 and b < 110: return 'G'         # gold/orange/brown
    if abs(r-g) < 40 and abs(g-b) < 40: return 's'        # steel gray
    return '?'
rows = []
for y in range(h):
    row = ''
    for x in range(w):
        idx = c.get(x, y)
        row += famof(idx) if idx != 0 else '.'
    rows.append('%2d %s' % (y, row))
print('\n'.join(rows))
print('legend: #=outline W=white P=pale p=pink r=red G=gold s=steel ~=shadow ?=other')
