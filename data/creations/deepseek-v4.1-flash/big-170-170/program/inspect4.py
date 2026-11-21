c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
from collections import defaultdict
stats = defaultdict(lambda: [0, 999, 999, -1, -1, 0, 0])
for y in range(170):
    for x in range(170):
        i = c.get(x, y)
        s = stats[i]
        s[0] += 1
        s[1] = min(s[1], x); s[2] = min(s[2], y)
        s[3] = max(s[3], x); s[4] = max(s[4], y)
        s[5] += x; s[6] += y
rows = []
for i, s in stats.items():
    rows.append((s[0], i, s))
rows.sort(reverse=True)
for n, i, s in rows:
    if n < 12: continue
    r, g, b, a = pal[i]
    print("id%-4d #%02x%02x%02x n=%-4d bbox=(%d,%d)-(%d,%d) ctr=(%d,%d)" % (i, r, g, b, n, s[1], s[2], s[3], s[4], s[5]//n, s[6]//n))
