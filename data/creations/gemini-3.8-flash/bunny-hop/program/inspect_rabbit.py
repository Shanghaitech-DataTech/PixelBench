# Let's inspect the pixels of input_canvas in detail
for y in range(input_canvas.height):
    row = "".join([f"{input_canvas.get(x, y):2d}" if input_canvas.get(x, y) is not None else " ." for x in range(input_canvas.width)])
    print(f"{y:2d}: {row}")
