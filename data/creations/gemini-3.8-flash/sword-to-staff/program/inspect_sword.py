output = input_canvas.copy(name="output")

for y in range(12, 36):
    line = f"y={y:2d}: "
    for x in range(41, 48):
        c = output.get(x, y)
        line += f"{c:2d} "
    print(line)
