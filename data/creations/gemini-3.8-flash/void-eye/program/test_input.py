from pixelbench_api import input_canvas, view

print("input_canvas stats:", input_canvas.stats_text())
print("non-transparent pixels in input_canvas:")
for y in range(64):
    for x in range(64):
        col = input_canvas.get(x, y)
        if col is not None:
            print(f"({x}, {y}): {col}")
