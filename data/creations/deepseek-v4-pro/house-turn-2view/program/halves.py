import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
for idx in [5,6,7,8,9,10,1,2,3,4]:
    ys,xs = np.where(inds==idx)
    if len(xs)==0: continue
    l = xs < W//2
    r = xs >= W//2
    print(f"idx {idx}: left_count={l.sum()} left_bbox x[{xs[l].min() if l.sum() else '-'},{xs[l].max() if l.sum() else '-'}] y[{ys[l].min() if l.sum() else '-'},{ys[l].max() if l.sum() else '-'}] | right_count={r.sum()} right_bbox x[{xs[r].min() if r.sum() else '-'},{xs[r].max() if r.sum() else '-'}] y[{ys[r].min() if r.sum() else '-'},{ys[r].max() if r.sum() else '-'}]")
