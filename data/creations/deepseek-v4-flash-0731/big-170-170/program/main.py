from pixelbench_api import *

# NOTE: this is just an inspection; will overwrite with final program next (last edit).
c = input_canvas
pal = c.palette()

def hexc(idx):
    r, g, b = pal[idx]['rgba'][0], pal[idx]['rgba'][1], pal[idx]['rgba'][2]
    return f"{r:02x}{g:02x}{b:02x}"

print("vending machine x117-155, y57-145")
for y in range(57, 146):
    print(f"{y:3d} " + ' '.join(hexc(c.get(x, y)) for x in range(117, 156)))

print()
print("ground y141-169 x0-169 sample colors")
from collections import Counter
cnt = Counter()
for y in range(141, 170):
    for x in range(170):
        rgb = tuple(pal[c.get(x, y)]['rgba'])
        cnt[rgb] += 1
print(cnt.most_common(12))
