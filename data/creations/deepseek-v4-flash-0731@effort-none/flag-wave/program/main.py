from pixelbench_api import *

# Get input dimensions
stats = input_canvas.stats()
w = stats['size'][0]  # 48
h = stats['size'][1]  # 56

# Frame 1: original content
f1 = input_canvas.copy(name='f1')

# The pole/hoist is on the right side (~x=40). The flag extends left.
# Frame 2: fly end (left) at highest → shift columns up
# Frame 3: fly end at lowest → shift columns down

pole_x = 40
max_shift = 4

def make_sheared(direction, name):
    """Create a sheared copy where the flag columns shift vertically.
    direction=1: fly end UP (highest)
    direction=-1: fly end DOWN (lowest)"""
    out = new_canvas(w, h, name=name)
    for x in range(w):
        if x >= pole_x:
            col_shift = 0
        else:
            col_shift = direction * round(max_shift * (pole_x - x) / pole_x)
        for y in range(h):
            src_y = y + col_shift
            if 0 <= src_y < h:
                colour = input_canvas.get(x, src_y)
                out.set(x, y, colour)
    return out

f2 = make_sheared(1, 'f2')
f3 = make_sheared(-1, 'f3')

finish([f1, f2, f3])
