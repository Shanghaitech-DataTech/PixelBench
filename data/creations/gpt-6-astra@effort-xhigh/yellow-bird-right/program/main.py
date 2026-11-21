print(input_canvas.matrix_text(region=(32,14,61,47)))
output = input_canvas.copy(name='output')
blue = input_canvas.color('#0097e0')
cyan = input_canvas.color('#2ecdf5')
for y in range(64):
    for x in range(32, 64):
        original = input_canvas.get(x,y)
        if original == blue:
            output.set(x,y,'#f5c928')
        elif original == cyan:
            output.set(x,y,'#ffeb70')
view(output, scale=8, margin=0)
finish(output)
