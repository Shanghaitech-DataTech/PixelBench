import numpy as np

out = input_canvas.copy(name="output")
out.mirror(axis="h")
rot = out.select(0, 0, 93, 128).rotate(53, algorithm="rotsprite").preview()
W, H = rot.stats()["size"]
arr = np.frombuffer(rot.to_rgba()[2], dtype=np.uint8).reshape(H, W, 4)
vis = arr[:, :, 3] > 0

print("column: top,bottom | offsets of bright(idx2) and dark-line(idx4) from TOP boundary")
for x in range(3, 157, 6):
    col = np.nonzero(vis[:, x])[0]
    if len(col) == 0:
        continue
    t, b = int(col.min()), int(col.max())
    b2 = [y - t for y in range(t, b + 1) if vis[y, x] and rot.get(x, y) == 2]
    d4 = [y - t for y in range(t, b + 1) if vis[y, x] and rot.get(x, y) == 4]
    print("x=%3d t=%3d b=%3d h=%2d | bright:%s darkline:%s" % (x, t, b, b - t + 1, b2, d4))
