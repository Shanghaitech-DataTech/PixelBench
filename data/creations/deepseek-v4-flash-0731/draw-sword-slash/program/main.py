from pixelbench_api import *
import math

c = input_canvas
f1 = c.copy(name="f1")
f2 = c.copy(name="f2")
BLACK = (0, 0, 0, 255)

# Completed slash trail on frame 2: quadratic Bezier sweeping from the
# lower-left up to the upper right (left-to-right motion), ending exactly
# on the drawn sword blade (the completed slash).
p0 = (1.0, 66.0)
p1 = (25.0, 50.0)
p2 = (53.0, 15.0)

N = 240
for i in range(N + 1):
    t = i / N
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    w = 1 + 1.2 * (math.sin(math.pi * t)) ** 1.4
    r = int(round(w))
    if r < 1:
        r = 1
    f2.circle(int(round(x)), int(round(y)), r, BLACK)

print("f1:", f1.stats_text())
print("f2:", f2.stats_text())
finish([f1, f2])
