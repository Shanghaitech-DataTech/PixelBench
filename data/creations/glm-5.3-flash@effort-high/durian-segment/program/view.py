result = input_canvas.copy(name='output')
for y in range(52, 58):
    for x in range(64):
        idx = result.get(x, y)
        if idx in (6, 7, 8):
            result.set(x, y, 5)

p = view(result, scale=6)
print(p)
p2 = view(input_canvas, scale=6)
print(p2)
