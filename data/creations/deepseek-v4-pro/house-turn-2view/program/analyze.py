import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
print("size", W,H)
for idx in range(0, 16):
    ys,xs = np.where(inds==idx)
    if len(xs)==0:
        continue
    print(f"index {idx}: count={len(xs)} bbox x[{xs.min()},{xs.max()}] y[{ys.min()},{ys.max()}]")
