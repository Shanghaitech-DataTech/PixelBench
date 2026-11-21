for y in range(22):
    row = ""
    for x in range(27):
        c = input_canvas.get(x, y)
        if c == 0:
            row += "."
        else:
            row += f"{c}"
    print(f"{y:2d}: {row}")
