output = input_canvas.copy(name='output')
for y in range(64):
    for x in range(32,64):
        p = input_canvas.get(x,y)
        if p == 3:
            output.set(x,y,'#f5c928')
        elif p == 8:
            output.set(x,y,'#ffe975')
view(output)
finish(output)
