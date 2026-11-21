from collections import Counter
c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
x0, x1, y0, y1 = 112, 170, 8, 120
cnt = Counter()
for y in range(y0, y1):
    for x in range(x0, x1):
        cnt[c.get(x, y)] += 1
top = [i for i, n in cnt.most_common(16)]
sym = "0123456789ABCDEF"
def near(i):
    r, g, b, a = pal[i]
    best = 0; bd = 1e9
    for k, t in enumerate(top):
        r2, g2, b2, a2 = pal[t]
        d = (r-r2)**2 + (g-g2)**2 + (b-b2)**2
        if d < bd: bd = d; best = k
    return sym[best]
print("legend:", ", ".join("%s=#%02x%02x%02x(%d)" % (sym[k], pal[t][0], pal[t][1], pal[t][2], cnt[t]) for k, t in enumerate(top)))
print("    " + "".join(str((x//10)%10) for x in range(x0, x1)))
print("    " + "".join(str(x%10) for x in range(x0, x1)))
for y in range(y0, y1):
    print("%3d " % y + "".join(near(c.get(x, y)) for x in range(x0, x1)))
