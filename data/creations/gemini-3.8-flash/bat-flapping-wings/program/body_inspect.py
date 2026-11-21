# Print row by row of input_canvas with indices
for y in range(22):
    s = ""
    for x in range(27):
        val = input_canvas.get(x, y)
        if val == 0:
            s += "."
        elif x in (9, 10, 16, 17):
            s += f"[{val}]"
        else:
            s += f" {val} "
    print(f"{y:2d}: {s}")
