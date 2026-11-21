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

dxs = [xs[i+1] - xs[i] for i in range(len(xs)-1)]
dys = [ys[j+1] - ys[j] for j in range(len(ys)-1)]
print("dxs:", dxs)
print("dys:", dys)
