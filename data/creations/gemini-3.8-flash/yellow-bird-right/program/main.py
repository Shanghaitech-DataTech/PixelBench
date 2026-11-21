output = input_canvas.copy(name="output")

# Register light yellow highlight for plumage
light_yellow = output.color((255, 240, 112), name="light_yellow")
yellow = output.color("c3")

# In the right-hand parrot (x >= 32), change blue plumage to yellow
# c2 (index 3) -> yellow
# c7 (index 8) -> light_yellow
for y in range(64):
    for x in range(32, 64):
        val = output.get(x, y)
        if val == 3:  # c2 blue [0, 151, 224]
            output.set(x, y, yellow)
        elif val == 8:  # c7 light blue [46, 205, 245]
            output.set(x, y, light_yellow)

view(output)
finish(output)
