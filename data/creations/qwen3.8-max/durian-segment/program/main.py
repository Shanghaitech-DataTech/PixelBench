from pixelbench_api import *
from collections import deque

output = input_canvas.copy(name='output')

FLESH = {7, 8}      # yellow flesh tones
RIND = 6            # cream inner rind (251,244,201)

w, h = output.stats()['size']

# flood the bottom flesh segment (lower-left lobe)
seed = (19, 44)
assert output.get(*seed) in FLESH
seen = {seed}
q = deque([seed])
while q:
    x, y = q.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen and output.get(nx, ny) in FLESH:
            seen.add((nx, ny))
            q.append((nx, ny))

xs = [p[0] for p in seen]
ys = [p[1] for p in seen]
print('removed flesh pixels:', len(seen), 'bbox', min(xs), min(ys), max(xs), max(ys))

# expose the rind underneath: inner-rind cream surface
for (x, y) in seen:
    output.set(x, y, RIND)

diff = [(x, y) for y in range(h) for x in range(w)
        if input_canvas.get(x, y) != output.get(x, y)]
dxs = [p[0] for p in diff]
dys = [p[1] for p in diff]
print('changed pixels:', len(diff), 'bbox', min(dxs), min(dys), max(dxs), max(dys))
print(output.stats_text())
print(view(output, scale=8, margin=0))
save('durian-segment-edit', output)
finish(output)
