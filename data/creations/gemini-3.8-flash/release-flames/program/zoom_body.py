# Print zoomed in view of the lower body
for y in range(30, 63):
    row = "".join(f"{input_canvas.get(x, y):2d} " if input_canvas.get(x, y) != 0 else " . " for x in range(0, 35))
    print(f"{y:2d}: {row}")
