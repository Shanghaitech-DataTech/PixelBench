output = input_canvas.copy(name='output')
# Recolor only the blue plumage of the right-hand bird.
colors = {3: '#f3c526', 8: '#ffe878'}
for y in range(64):
    for x in range(32, 64):
        original = input_canvas.get(x, y)
        if original in colors:
            output.set(x, y, colors[original])
view(output)
finish(output)
