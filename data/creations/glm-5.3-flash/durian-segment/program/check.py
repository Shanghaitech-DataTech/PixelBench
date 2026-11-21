print("reference_frames:", reference_frames)
print("mask:", mask.shape if mask is not None else None)
if mask is not None:
    import numpy as np
    ys, xs = np.nonzero(mask)
    print("mask true pixels:", mask.sum(), "bbox:", (xs.min(), ys.min(), xs.max(), ys.max()))
    w, h = mask.shape[1], mask.shape[0]
    print("    " + "".join(str(x % 10) for x in range(w)))
    for y in range(h):
        print(f"{y:3d} " + "".join('X' if mask[y, x] else '.' for x in range(w)))
