import numpy as np

arr = np.zeros((135, 82), dtype=int)
for y in range(135):
    for x in range(82):
        arr[y, x] = input_canvas.get(x, y)

print("Pine tree vertical extents:")
rows_with_pixels = np.where(np.any(arr > 0, axis=1))[0]
print("Min row:", rows_with_pixels[0], "Max row:", rows_with_pixels[-1])

# For each row, print min x, max x, width, and color counts
for y in range(rows_with_pixels[0], min(rows_with_pixels[0] + 40, 135)):
    cols = np.where(arr[y] > 0)[0]
    if len(cols) > 0:
        c_counts = {c: int(np.sum(arr[y] == c)) for c in np.unique(arr[y]) if c > 0}
        print(f"Row {y:3d} (x: {cols[0]:2d}..{cols[-1]:2d}, w={len(cols):2d}): {c_counts}")
