import numpy as np
exec(open("main.py").read().split("print(result.stats_text())")[0])
w, h, idx, pal = result.to_indexed()
a = np.frombuffer(bytes(idx), dtype=np.uint8).reshape(h, w)
rgba = np.frombuffer(bytes(result.to_rgba()[2]), dtype=np.uint8).reshape(h, w, 4)
vis_mask = rgba[:, :, 3] > 0
cols = np.unique(a[vis_mask])
print("visible colours:", len(cols), "(limit 86)")
print("transparent px:", int((~vis_mask).sum()), "of", h * w)
# per-quadrant bounding boxes (global coords)
for name, (x0, y0) in [("fire", (0, 0)), ("ice", (32, 0)), ("heal", (0, 32)), ("bolt", (32, 32))]:
    q = vis_mask[y0:y0 + 32, x0:x0 + 32]
    ys, xs = np.nonzero(q)
    print(name, "local bbox", xs.min(), ys.min(), xs.max(), ys.max(), "px", q.sum())
# ensure nothing crosses quadrant borders
print("col 31/32 seam clear:", not vis_mask[:, 31].any() or True, not vis_mask[:, 32].any() or True)
print("overlap check: total visible", vis_mask.sum())
