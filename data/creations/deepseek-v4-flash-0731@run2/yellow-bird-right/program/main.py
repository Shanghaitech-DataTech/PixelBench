from pixelbench_api import *

c = input_canvas.copy(name='output')

# Register yellow shades
body_yellow = c.color('#FFD700')   # bright yellow for the body
light_yellow = c.color('#FFEB73')  # pale yellow for light accents
wing_yellow = c.color('#D9A400')  # golden for the wing

# Right parrot occupies x>=35. Recolor its blue feathers to yellow.
for y in range(64):
    for x in range(35, 64):
        idx = c.get(x, y)
        if idx == 3:
            c.set(x, y, body_yellow)
        elif idx == 8:
            c.set(x, y, light_yellow)
        elif idx == 7 and y <= 45:
            c.set(x, y, wing_yellow)  # wing -> golden; feet (y>=46) stay gray

finish(c)
