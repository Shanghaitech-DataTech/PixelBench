import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.array(rgba).reshape(h,w,4)

codes = {}
rows=[]
x0,x1,y0,y1,step = 50,125,55,145,2
for by in range(y0,y1,step):
    row=''
    for bx in range(x0,x1,step):
        block = a[by:by+step, bx:bx+step].reshape(-1,4)
        colors, counts = np.unique(block, axis=0, return_counts=True)
        dom = colors[counts.argmax()]
        key = tuple(dom)
        if key not in codes:
            codes[key] = chr(ord('A')+len(codes)) if len(codes)<60 else '?'
        row += codes[key]
    rows.append('%3d %s'%(by,row))
print('legend:')
for k,v in codes.items():
    print(v, '#%02x%02x%02x%02x'%k)
for r in rows: print(r)
