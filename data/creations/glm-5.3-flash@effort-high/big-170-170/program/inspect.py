import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.array(rgba).reshape(h,w,4)
print(w,h)

# coarse map: block of 10x10, dominant color
step=10
codes = {}
rows=[]
for by in range(0,h,step):
    row=[]
    for bx in range(0,w,step):
        block = a[by:by+step, bx:bx+step].reshape(-1,4)
        # dominant color
        colors, counts = np.unique(block, axis=0, return_counts=True)
        dom = colors[counts.argmax()]
        key = tuple(dom)
        if key not in codes:
            codes[key] = chr(ord('A')+len(codes)) if len(codes)<26 else chr(ord('a')+len(codes)-26)
        row.append(codes[key])
    rows.append(''.join(row))
print('legend:')
for k,v in codes.items():
    print(v, '#%02x%02x%02x%02x'%k)
for r in rows:
    print(r)
