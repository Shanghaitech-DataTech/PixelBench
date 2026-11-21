from pixelbench_api import *

# Let's inspect where pixels are
w, h = 64, 76
for y in range(h):
    row = [input_canvas.get(x, y) for x in range(w)]
    non_zero = [(x, row[x]) for x in range(w) if row[x] != 0]
    if non_zero:
        print(f"y={y}: min_x={non_zero[0][0]}, max_x={non_zero[-1][0]}, count={len(non_zero)}")
