output = input_canvas.copy(name='output')
for y in range(0, 48):
    row = "".join(['#' if output.get(x, y) in [10, 11, 12, 5, 27, 36, 37] else '.' for x in range(115, 160)])
    if '#' in row:
        print(f"{y:2d}: {row}")
