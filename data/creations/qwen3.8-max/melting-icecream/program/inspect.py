w, h = input_canvas.size if hasattr(input_canvas, 'size') else (64, 64)
bg = input_canvas.get(0, 0)
for y in range(32, 62):
    xs = [x for x in range(64) if input_canvas.get(x, y) != bg]
    print(y, min(xs), max(xs))
