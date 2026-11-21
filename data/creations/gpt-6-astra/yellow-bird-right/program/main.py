output = input_canvas.copy(name='output')
# Preserve all outlines, facial details and the left bird; change only blue plumage.
yellow = output.color('#f4cd32', name='yellow_plumage')
light_yellow = output.color('#fff18a', name='yellow_highlight')
blue = input_canvas.color('c2')
cyan = input_canvas.color('c7')
for y in range(64):
    for x in range(32,64):
        original = input_canvas.get(x,y)
        if original == blue:
            output.set(x,y,yellow)
        elif original == cyan:
            output.set(x,y,light_yellow)
view(output, scale=8)
finish(output)
