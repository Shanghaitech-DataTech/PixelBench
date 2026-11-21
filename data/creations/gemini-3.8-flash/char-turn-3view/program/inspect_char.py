import numpy as np

# Let's inspect the input canvas
w, h = input_canvas.size if hasattr(input_canvas, 'size') else (66, 119)
print(f"Canvas size: {w}x{h}")

# Let's find bounding box of non-transparent pixels
pixels = []
for y in range(119):
    for x in range(66):
        c = input_canvas.get(x, y)
        if c != 0:
            pixels.append((x, y, c))

xs = [p[0] for p in pixels]
ys = [p[1] for p in pixels]
print(f"Non-transparent bbox: x in [{min(xs)}, {max(xs)}], y in [{min(ys)}, {max(ys)}]")
print(f"Total non-transparent pixels: {len(pixels)}")
