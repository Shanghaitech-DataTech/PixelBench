c = input_canvas
for y in [0, 5, 10, 20, 30, 38, 42, 46, 50]:
    row = "".join(str(c.get(x, y)) for x in range(0, 256, 2))
    print(f"y={y:3d} {row}")
print()
for y in [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 127]:
    row = "".join(str(c.get(x, y)) for x in range(0, 256, 2))
    print(f"y={y:3d} {row}")
