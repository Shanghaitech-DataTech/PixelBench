from pixelbench_api import *

f1 = input_canvas.copy(name='f1')
f2 = input_canvas.copy(name='f2')

black = f2.color('#020202', name='slash_black')

# Slash trail: gentle arc sweeping from lower-left up to upper-right,
# ending exactly at the sword tip (~x51,y38). Three stacked Bresenham
# polylines give a ~3px streak.
pts = [(2, 67), (9, 63), (17, 57), (26, 51), (35, 46), (44, 41), (51, 38)]
for off in (-1, 0, 1):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        f2.line(x0, y0 + off, x1, y1 + off, black)

# thin tapering start tip of the streak
for off in (-1, 0, 1):
    f2.line(1, 68, 6, 64, black)

print("f1:", f1.stats())
print("f2:", f2.stats())

finish([f1, f2])
