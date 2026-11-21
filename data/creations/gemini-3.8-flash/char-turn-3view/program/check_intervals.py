x_changes = set()
for y in range(119):
    for x in range(65):
        if input_canvas.get(x, y) != input_canvas.get(x+1, y):
            x_changes.add(x+1)

y_changes = set()
for y in range(118):
    for x in range(66):
        if input_canvas.get(x, y) != input_canvas.get(x, y+1):
            y_changes.add(y+1)

xs = [0] + sorted(list(x_changes)) + [66]
ys = [0] + sorted(list(y_changes)) + [119]

print(f"Number of x intervals: {len(xs)-1}")
print(f"Number of y intervals: {len(ys)-1}")

# Check if every interval is uniform color
grid = []
uniform = True
for j in range(len(ys)-1):
    row = []
    for i in range(len(xs)-1):
        c0 = input_canvas.get(xs[i], ys[j])
        for y in range(ys[j], ys[j+1]):
            for x in range(xs[i], xs[i+1]):
                if input_canvas.get(x, y) != c0:
                    uniform = False
        row.append(c0)
    grid.append(row)

print("Is every interval completely uniform?", uniform)
