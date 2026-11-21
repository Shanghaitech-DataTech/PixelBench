from pixelbench_api import *

out = input_canvas.copy(name='output')
# replicate only the y60 fill for quick check
from collections import Counter
def bg_color_for(y):
    cnt = Counter()
    for x in range(60, 75):
        idx = out.get(x,y)
        if idx is not None:
            cnt[idx] += 1
    idx = cnt.most_common(1)[0][0]
    return out.color_name(idx)
col = bg_color_for(60)
for x in range(75, 86):
    out.set(x, 60, col)
print('col', col)
for x in range(75, 95):
    idx = out.get(x,60)
    print(x, out.color_name(idx), out.palette()[idx]['rgba'])
