import numpy as np

w, h, rgba = input_canvas.to_rgba()
rgba = np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(h, w, 4)
for y in range(h):
    for x in range(w):
        r, g, b, a = rgba[y, x]
        if a:
            print(f'{x:2d},{y:2d} #{r:02x}{g:02x}{b:02x}')
