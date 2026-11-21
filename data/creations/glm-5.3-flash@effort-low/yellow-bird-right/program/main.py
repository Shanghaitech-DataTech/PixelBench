out = input_canvas.copy(name='output')
# map: blue body -> yellow, light blue highlight -> light yellow (right half only)
mapping = {3: 4, 8: 4}  # placeholder, set below
import pixelbench_api as api  # not needed; just recolor via set
W, H = 64, 64
yellow_body = out.color('#f5c400')
yellow_light = out.color('#ffe873')
for y in range(H):
    for x in range(32, W):
        idx = out.get(x, y)
        if idx == 3:
            out.set(x, y, yellow_body)
        elif idx == 8:
            out.set(x, y, yellow_light)
print(out.stats_text())
finish(out)
