output = input_canvas.copy(name='output')

blue = input_canvas.color('#0097e0')
cyan = input_canvas.color('#2ecdf5')
yellow = output.color('#f2c230', name='parrot_yellow')
yellow_highlight = output.color('#ffe66b', name='parrot_yellow_highlight')

for y in range(64):
    for x in range(32, 64):
        pixel = output.get(x, y)
        if pixel == blue:
            output.set(x, y, yellow)
        elif pixel == cyan:
            output.set(x, y, yellow_highlight)

view(output, scale=8, margin=0)
finish(output)
