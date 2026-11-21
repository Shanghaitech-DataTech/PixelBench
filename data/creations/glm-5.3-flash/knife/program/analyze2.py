import numpy as np

w, h = input_canvas.stats()["size"]
print("input size", w, h)
rgba = input_canvas.to_rgba()
arr = np.frombuffer(rgba[2], dtype=np.uint8).reshape(h, w, 4)
vis = arr[:, :, 3] > 0

# ---- spine (upper-right boundary) line fit: rightmost visible pixel per row ----
rows = list(range(13, 71))
X = np.array([np.nonzero(vis[y])[0].max() for y in rows], float)
Y = np.array(rows, float)
a, b = np.polyfit(Y, X, 1)
print("spine fit: x = %.4f*y + %.4f" % (a, b))
theta_spine = np.degrees(np.arctan2(1.0, a))       # tip->heel direction, screen cw from +x
print("spine dir angle = %.2f deg ; axis(handle->tip) = %.2f ; DELTA(cw after mirror) = %.2f"
      % (theta_spine, theta_spine + 180, (theta_spine + 180 - 180) % 360))

# ---- PCA of whole sprite ----
ys, xs = np.nonzero(vis)
pts = np.stack([xs, ys], 1).astype(float)
m = pts.mean(0)
c = np.cov((pts - m).T)
ev, evec = np.linalg.eigh(c)
v = evec[:, -1]
if v[0] > 0:
    v = -v
pca_ang = np.degrees(np.arctan2(v[1], v[0]))
print("PCA axis angle = %.2f ; DELTA = %.2f ; evals" % (pca_ang, (pca_ang - 180) % 360), ev)

# ---- which side is the cutting edge?  b = palette idx 2 (light), d = idx 4 ----
print("\nrow: left,right,width | offsets of light(b) and dark-line(d) from LEFT boundary")
for y in range(14, 78, 4):
    row = np.nonzero(vis[y])[0]
    if len(row) == 0:
        continue
    l, r = int(row.min()), int(row.max())
    bs = [x - l for x in range(l, r + 1) if vis[y, x] and input_canvas.get(x, y) == 2]
    ds = [x - l for x in range(l, r + 1) if vis[y, x] and input_canvas.get(x, y) == 4]
    print("y=%3d l=%3d r=%3d wd=%2d | b:%s d:%s" % (y, l, r, r - l + 1, bs, ds))
