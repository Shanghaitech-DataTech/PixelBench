from pixelbench_api import *

c = input_canvas
pal = c.palette()
by_idx = {p['index']: p['rgba'] for p in pal}
print("palette:", {p['index']: p['name'] for p in pal})

# Print per-row segments of each color with exact x ranges, for rows 0..63
for y in range(0, 64):
    runs = []
    prev = None
    start = 0
    for x in range(64):
        idx = c.get(x, y)
        if idx != prev:
            if prev is not None:
                runs.append((start, x-1, prev))
            start = x
            prev = idx
    runs.append((start, 63, prev))
    print(y, runs)
