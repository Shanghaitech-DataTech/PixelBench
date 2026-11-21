import numpy as np

c = new_canvas(16, 16, name="probe")
c.rect(0, 0, 8, 8, "#ff0000")
c.circle(10, 10, 4, "#00ff00")

print("TYPE:", type(c))
pub = [a for a in dir(c) if not a.startswith('_')]
priv = [a for a in dir(c) if a.startswith('_')]
print("PUBLIC:", pub)
print("PRIVATE:", priv)

for attr in priv + ['pixels', 'data', 'width', 'height', 'name']:
    if hasattr(c, attr):
        v = getattr(c, attr)
        if not callable(v):
            print("ATTR", attr, type(v), getattr(v, 'shape', None), getattr(v, 'dtype', None),
                  (v if isinstance(v, (int, str, float)) else ''))

w, h, data = c.to_rgba()
print("to_rgba:", w, h, len(data), type(data))
arr = np.frombuffer(bytes(data), np.uint8).reshape(h, w, 4)
print(arr[0, 0], arr[10, 10])
iw, ih, idx, pal = c.to_indexed()
print("indexed:", iw, ih, type(idx), getattr(idx, 'shape', None), len(pal), pal[:4])
print(c.stats())

import pixelbench_api as P
print("MODULE:", [a for a in dir(P) if not a.startswith('_')][:60])
finish(c)
