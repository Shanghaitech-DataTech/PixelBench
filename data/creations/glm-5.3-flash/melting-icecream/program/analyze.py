from pixelbench_api import *

BG = 1  # white background index

# For each row, print runs of non-background pixels
for y in range(0, 64):
    row = [input_canvas.get(x, y) for x in range(64)]
    runs = []
    start = None
    for x in range(64):
        if row[x] != BG and start is None:
            start = x
        elif row[x] == BG and start is not None:
            runs.append((start, x - 1))
            start = None
    if start is not None:
        runs.append((start, 63))
    if runs:
        print(y, runs)
