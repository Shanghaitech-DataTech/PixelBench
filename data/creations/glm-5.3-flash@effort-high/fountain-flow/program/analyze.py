c = input_canvas

def dump(x0, y0, x1, y1, label):
    print("=== %s ===" % label)
    print(c.matrix_text(region=(x0, y0, x1, y1)))

dump(10, 42, 54, 52, "below tier2 / bowl wall")
