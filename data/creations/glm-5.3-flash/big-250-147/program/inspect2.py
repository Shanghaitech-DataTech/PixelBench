from collections import Counter

w, h, rgba = input_canvas.to_rgba()
cnt = Counter()
for i in range(0, len(rgba), 4):
    cnt[(rgba[i], rgba[i+1], rgba[i+2], rgba[i+3])] += 1
print("distinct colours:", len(cnt))
for c, n in cnt.most_common(30):
    print(c, n)

# where does each of the top colours live? print bbox + sample positions
def bbox_of(col):
    xs, ys = [], []
    for y in range(h):
        for x in range(w):
            i = (y*w + x)*4
            if (rgba[i], rgba[i+1], rgba[i+2], rgba[i+3]) == col:
                xs.append(x); ys.append(y)
    if not xs: return None
    return (min(xs), min(ys), max(xs), max(ys))

tops = [c for c, n in cnt.most_common(12)]
for c in tops:
    print(c, "count", cnt[c], "bbox", bbox_of(c))
