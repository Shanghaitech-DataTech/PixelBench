import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
vis = (inds!=0)&(inds!=11)
for y in range(0,H):
    print(f"{y:3d} " + ''.join('#' if v else '.' for v in vis[y]))
