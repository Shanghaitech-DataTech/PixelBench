c = input_canvas
W, H = c.stats()['size']
pal = {p['index']: p['rgba'] for p in c.palette()}

def hexv(idx):
    rgba = pal.get(idx)
    return None if rgba is None else '#%02x%02x%02x%02x' % tuple(rgba)

WATER = {'#1d8baaff', '#2ec7dcff'}

# print exact colours along the planned stream paths
paths = {
    'S2L (bowl1->2)': [(x, y) for y in range(10, 16) for x in (21, 22, 23, 24, 25)],
    'S3L (bowl2->3)': [(x, y) for y in range(16, 25) for x in (15, 16, 17, 18, 19, 20)],
    'S4L (bowl3->basin)': [(x, y) for y in range(25, 47) for x in (12, 13, 14, 15, 16, 17, 18)],
}
for name, pts in paths.items():
    print('==', name)
    for (x, y) in pts:
        idx = c.get(x, y)
        hv = hexv(idx)
        tag = 'WATER' if hv in WATER else ('none' if idx is None else 'stone/gold')
        print(f"  ({x:2d},{y:2d}) {hv} {tag}")
