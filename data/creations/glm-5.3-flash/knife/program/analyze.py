import numpy as np

w, h = input_canvas.stats()["size"]
print("size", w, h)
rgba = input_canvas.to_rgba()
arr = np.array(rgba[2], dtype=np.uint8).reshape(rgba[1], rgba[0], 4)  # h,w,4

# legend by palette index
pal = {p["index"]: p["rgba"] for p in input_canvas.palette()}
names = {p["index"]: p.get("name") for p in input_canvas.palette()}
print(pal)

def rle_rows(y0, y1, x0=0, x1=None):
    if x1 is None:
        x1 = w
    idx = arr[:, :, 3] > 0
    for y in range(y0, y1):
        runs = []
        cur = None
        start = x0
        for x in range(x0, x1):
            v = idx[y, x]
            if v != cur:
                if cur is not None:
                    runs.append((cur, start, x - 1))
                cur = v
                start = x
        if cur is not None:
            runs.append((cur, start, x1 - 1))
        s = []
        for v, a, b in runs:
            if v:
                # dominant colour in run
                seg = arr[y, a:b+1, 3]
                cols = {}
                for x2 in range(a, b+1):
                    if idx[y, x2]:
                        ci = input_canvas.get(x2, y)
                        cols[ci] = cols.get(ci, 0) + 1
                dom = max(cols.items(), key=lambda kv: kv[1])[0]
                s.append(f"{a}-{b}:{names.get(dom,dom)}")
        if s:
            print(f"y={y:3d}  " + "  ".join(s))

rle_rows(0, 128)
