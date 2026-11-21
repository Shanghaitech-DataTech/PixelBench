from pixelbench_api import *

input_canvas = canvas("input")
pal = input_canvas.palette()
for p in pal:
    print(f"Index {p['index']}: {p['name']} - {p['rgba']}")

# Let's create frame 2 by shifting top part down
f2 = input_canvas.copy(name="f2")
# shift y=0 to 39 down by 1
sel = f2.select(0, 0, 58, 40)
sel.move_to(0, 1, f2)

# create frame 3 by shifting top part down by 2
f3 = input_canvas.copy(name="f3")
sel2 = f3.select(0, 0, 58, 40)
sel2.move_to(0, 2, f3)

view(f2, margin=4)
view(f3, margin=4)
