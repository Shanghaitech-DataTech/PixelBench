from pixelbench_api import *

output = input_canvas.copy(name='output')

# Register new yellow colors
yellow_body = output.color('#FFD700')
yellow_highlight = output.color('#FFFF66')

for y in range(64):
    for x in range(32, 64):
        c = output.get(x, y)
        if c == 3:
            output.set(x, y, yellow_body)
        elif c == 8:
            output.set(x, y, yellow_highlight)

finish(output)
