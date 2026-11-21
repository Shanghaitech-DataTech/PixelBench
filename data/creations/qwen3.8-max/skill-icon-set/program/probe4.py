import numpy as np

def arr(c):
    w, h, rgba = c.to_rgba()
    return np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(h, w, 4).copy()

t = new_canvas(12, 12, name="ot")
t.circle(6, 6, 4, "#ff0000")
a = arr(t)
v = a[:, :, 3] > 0
h, w = v.shape
pad = np.zeros((h + 2, w + 2), dtype=bool)
pad[1:-1, 1:-1] = v
nb = (pad[0:-2, 1:-1] | pad[2:, 1:-1] | pad[1:-1, 0:-2] | pad[1:-1, 2:])
edge = v & ~nb
print("edge count", edge.sum())
ys, xs = np.nonzero(edge)
for x, y in zip(xs.tolist(), ys.tolist()):
    t.set(int(x), int(y), "#101420")
print(t.matrix_text(region=(0, 0, 11, 11)))
