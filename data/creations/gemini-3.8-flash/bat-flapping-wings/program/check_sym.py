is_sym = True
for y in range(22):
    for x in range(14):
        if input_canvas.get(x, y) != input_canvas.get(26 - x, y):
            print(f"Mismatch at y={y}, x={x} vs {26-x}: {input_canvas.get(x, y)} vs {input_canvas.get(26-x, y)}")
            is_sym = False
print("Is horizontally symmetric:", is_sym)
