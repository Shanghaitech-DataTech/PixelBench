from pixelbench_api import *

pal = input_canvas.palette()
# count usage
from collections import Counter
cnt = Counter()
W, H = input_canvas.size if hasattr(input_canvas, 'size') else (250, 147)
print("size", W, H)
for y in range(H):
    for x in range(W):
        cnt[input_canvas.get(x, y)] += 1
top = cnt.most_common(40)
idx2rgba = {p['index']: p['rgba'] for p in pal}
for i, c in top:
    name = None
    for p in pal:
        if p['index'] == i:
            name = p.get('name')
    print(i, name, idx2rgba[i], c)

# sample points
pts = {
    'sky_top': (20, 5), 'sky_mid': (20, 40), 'sky_low': (20, 70), 'sky_horizon': (20, 85),
    'sun_center': (132, 42), 'sun_edge': (120, 30),
    'cloud_top': (60, 20), 'cloud_horiz': (60, 72),
    'mtn_left': (60, 100), 'mtn_mid_pink': (120, 90), 'mtn_right': (180, 95), 'mtn_far_right': (230, 100),
    'forest': (20, 135), 'tree_hi': (115, 125),
}
for k, (x, y) in pts.items():
    i = input_canvas.get(x, y)
    print(k, (x, y), i, idx2rgba.get(i))
