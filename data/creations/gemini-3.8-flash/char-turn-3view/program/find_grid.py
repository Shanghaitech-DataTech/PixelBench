# Let's find horizontal and vertical run-lengths of identical pixels
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

print("x_changes:", sorted(list(x_changes)))
print("y_changes:", sorted(list(y_changes)))
