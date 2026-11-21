output = input_canvas.copy(name='output')
# Recolour only the blue plumage of the right-hand bird.
yellow = output.color('#ffcf1a')
yellow_highlight = output.color('#fff080')
for y in range(64):
    for x in range(32, 64):
        original = input_canvas.get(x, y)
        if original == 3:
            output.set(x, y, yellow)
        elif original == 8:
            output.set(x, y, yellow_highlight)
view(output, scale=8)
finish(output)
