import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
# check vertical symmetry around center x=56 (0-indexed center between 55 and 56)
# mirror x -> W-1-x
diff = 0
for y in range(H):
    for x in range(W//2):
        a = inds[y,x]
        b = inds[y,W-1-x]
        if a != b:
            diff += 1
print("pixels differing under vertical mirror:", diff, "out of", H*(W//2))
# show a few rows where asymmetry occurs, with row diffs
for y in range(0, H, 5):
    d = sum(1 for x in range(W//2) if inds[y,x] != inds[y,W-1-x])
    if d:
        print("row", y, "diff", d)
