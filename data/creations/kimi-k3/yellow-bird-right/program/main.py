# Edit: make the right-hand parrot yellow.
output = input_canvas.copy(name="output")

blue  = output.color("#0097e0")   # main body blue
lblue = output.color("#2ecdf5")   # light-blue highlights
yellow  = output.color("#ffd21a", name="parrot_yellow")
lyellow = output.color("#ffed8a", name="parrot_yellow_light")

w, h = output.size if hasattr(output, "size") else (64, 64)
for y in range(64):
    for x in range(32, 64):       # right-hand parrot only
        idx = output.get(x, y)
        if idx == blue:
            output.set(x, y, yellow)
        elif idx == lblue:
            output.set(x, y, lyellow)

view(output)
finish(output)
