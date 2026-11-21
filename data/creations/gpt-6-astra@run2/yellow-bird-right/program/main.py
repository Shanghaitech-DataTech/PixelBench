output = input_canvas.copy(name='output')
for y in range(64):
    for x in range(32,64):
        original = input_canvas.get(x,y)
        if original == 3:
            output.set(x,y,'#f4c526')
        elif original == 8:
            output.set(x,y,'#ffe776')
view(output)
finish(output)
