import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
for ylim in [116, 130, 157]:
    diff = 0
    n = 0
    for y in range(0, min(H, ylim)):
        for x in range(W//2):
            a = inds[y,x]
            b = inds[y,W-1-x]
            if a != b:
                diff += 1
            n += 1
    print(f"y<{ylim}: diff={diff}/{n} = {diff/n:.3f}")
