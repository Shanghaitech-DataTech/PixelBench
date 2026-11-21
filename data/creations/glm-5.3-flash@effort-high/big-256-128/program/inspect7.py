import numpy as np
c = input_canvas
w, h, rgba = c.to_rgba()
arr = np.array(rgba, dtype=np.uint8).reshape(h, w, 4)
pal = {p['index']: tuple(p['rgba']) for p in c.palette()}
idx = np.zeros((h, w), dtype=int)
for i, col in pal.items():
    mask = np.all(arr == np.array(col, dtype=np.uint8), axis=-1)
    idx[mask] = i

def bbox(i):
    m = idx == i
    if not m.any():
        return None
    ys, xs = np.where(m)
    return (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()), int(m.sum()))

for name, i in [("black",6),("white",12),("lightblue",5),("teal_bright",40),
                ("cyan1",15),("cyan2",16),("cyan3",51),("magenta",44),
                ("yellow",19),("tan",39),("brown",26),("grey",33),("grey2",30)]:
    print(name, i, bbox(i))

print()
print("black count per row (every 4):")
for y in range(0, 128, 4):
    print(y, int((idx[y] == 6).sum()))
