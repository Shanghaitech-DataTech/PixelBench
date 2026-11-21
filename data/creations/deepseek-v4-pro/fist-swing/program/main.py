from pixelbench_api import *

# Frame 1: keep the original picture content.
f1 = input_canvas.copy(name='frame1')

# Frame 2: the character throws a light punch with the left fist.
# The left fist is the arm that extends horizontally to the right.
# Keep the same 29x44 canvas and extend that front arm by 3 px to the right.
f2 = f1.copy(name='frame2')

# Remove the forearm + fist part of the extended arm (x=14..21, y=10..14)
# and redraw it longer, with the fist shifted from x=19..21 to x=22..24.
f2.clear(14, 10, 8, 5)

colmap = {
    14: 14, 15: 15, 16: 16, 17: 17, 18: 18,
    19: 18, 20: 18, 21: 18,          # stretched forearm
    22: 19, 23: 20, 24: 21,          # fist shifted right
}

for new_x, old_x in colmap.items():
    for y in range(10, 15):
        idx = f1.get(old_x, y)
        if idx != 0:
            f2.set(new_x, y, idx)

finish([f1, f2])
