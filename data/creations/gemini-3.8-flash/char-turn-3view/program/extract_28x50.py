# Extract the 28x50 grid
grid = []
for gy in range(50):
    row = []
    # find y on input_canvas: center of gy
    # (y + 0.5) * 50 / 119 = gy + 0.5  => y + 0.5 = (gy + 0.5) * 119 / 50
    # Let's just use ys boundaries: middle of ys[gy] and ys[gy+1]
    y = int(np.floor((gy + 0.5) * 119 / 50))
    for gx in range(28):
        x = int(np.floor((gx + 0.5) * 66 / 28))
        row.append(input_canvas.get(x, y))
    grid.append(row)

# Let's print the grid as characters or indices
symbols = ".0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("28x50 grid:")
for r, row in enumerate(grid):
    chars = "".join(f"{symbols[c]}" for c in row)
    print(f"{r:2d}: {chars}")
