output = input_canvas.copy(name='output')

# palette indices in the input
BLUE = input_canvas.color('#0097e0')        # c2 body blue
LIGHTBLUE = input_canvas.color('#2ecdf5')   # c7 highlight blue
YELLOW = input_canvas.color('#ffcf1a')      # c3 beak / accent yellow

BODY = '#ffc800'    # main yellow plumage
LIGHT = '#ffe14d'   # lighter yellow highlight
ORANGE = '#ff9900'  # beak / shoulder accent, contrasts with yellow body

for y in range(64):
    for x in range(32, 64):  # right-hand parrot only
        idx = output.get(x, y)
        if idx == BLUE:
            output.set(x, y, BODY)
        elif idx == LIGHTBLUE:
            output.set(x, y, LIGHT)
        elif idx == YELLOW:
            output.set(x, y, ORANGE)

print(output.stats_text())
view(output)
finish(output)
