for y in range(36, 48):
    row = []
    for x in range(34, 56):
        c = input_canvas.get(x, y)
        row.append(f"{c:2d}")
    print(f"{y:2d}: " + " ".join(row))
