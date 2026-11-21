from pixelbench_api import *

w, h = input_canvas.stats()['size']
diff = []
for y in range(h):
    for x in range(w):
        if input_canvas.get(x, y) != output.get(x, y):
            diff.append((x, y))
xs = [p[0] for p in diff]
ys = [p[1] for p in diff]
print('changed pixels:', len(diff), 'bbox', min(xs), min(ys), max(xs), max(ys))
print(output.stats_text())
print(view(output, scale=8, margin=0))
save('durian-segment-edit', output)
finish(output)
