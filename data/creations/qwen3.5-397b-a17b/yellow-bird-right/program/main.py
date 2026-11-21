# Create output canvas as a copy of input
output = input_canvas.copy(name='output')

# Register yellow color
yellow = output.color('#FFD700', name='yellow')  # Gold yellow

# The right parrot is on the right side of the canvas
# I need to change the blue pixels (c2, which is #0097e0ff) to yellow in the right parrot region

# Get the palette indices
blue_idx = 2  # c2 is the blue color

# Scan through the right parrot region and change blue to yellow
# The right parrot is roughly from x=32 to x=63
for y in range(64):
    for x in range(32, 64):  # Right half of canvas
        idx = output.get(x, y)
        if idx == blue_idx:
            output.set(x, y, yellow)

print("Output canvas stats:")
print(output.stats_text())

finish(output)
