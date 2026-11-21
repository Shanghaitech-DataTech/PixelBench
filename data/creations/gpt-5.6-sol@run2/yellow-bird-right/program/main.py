from pixelbench_api import *

output = input_canvas.copy(name="output")
yellow = output.color("#f6c928", name="yellow_feathers")
yellow_highlight = output.color("#ffe86a", name="yellow_highlight")

# Recolor only the two blue feather tones on the right-hand parrot.
for y in range(64):
    for x in range(32, 64):
        source_colour = input_canvas.get(x, y)
        if source_colour == 3:
            output.set(x, y, yellow)
        elif source_colour == 8:
            output.set(x, y, yellow_highlight)

print(output.stats_text())
view(output, scale=8, margin=0)
finish(output)
