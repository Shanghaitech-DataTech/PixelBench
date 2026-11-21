# Let's inspect the entire front view grid in detail
grid = []
for gy in range(50):
    row = []
    y = int(np.floor((gy + 0.5) * 119 / 50))
    for gx in range(28):
        x = int(np.floor((gx + 0.5) * 66 / 28))
        row.append(input_canvas.get(x, y))
    grid.append(row)

print("FRONT_GRID = [")
for r in range(50):
    print(f"    {grid[r]},  # y={r}")
print("]")
