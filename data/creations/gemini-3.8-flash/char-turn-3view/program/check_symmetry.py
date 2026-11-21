grid = []
for gy in range(50):
    row = []
    y = int(np.floor((gy + 0.5) * 119 / 50))
    for gx in range(28):
        x = int(np.floor((gx + 0.5) * 66 / 28))
        row.append(input_canvas.get(x, y))
    grid.append(row)

diffs = []
for y in range(50):
    for x in range(14):
        x_opp = 27 - x
        c1 = grid[y][x]
        c2 = grid[y][x_opp]
        if c1 != c2:
            diffs.append((x, y, c1, c2))

print(f"Total asymmetrical pixels: {len(diffs)}")
# Group diffs by y
diffs_by_y = {}
for x, y, c1, c2 in diffs:
    diffs_by_y.setdefault(y, []).append((x, c1, c2))

for y in sorted(diffs_by_y.keys()):
    print(f"y={y:2d}: {len(diffs_by_y[y])} diffs -> {diffs_by_y[y]}")
