from pixelbench_api import *

t = new_canvas(25, 25, name="test")
cx, cy, rx, ry = 12, 12, 12, 11
d = f"M {cx-rx} {cy} A {rx} {ry} 0 1 1 {cx+rx} {cy} A {rx} {ry} 0 1 1 {cx-rx} {cy} Z"
t.path(d, "#00ff00", fill=False)
print(t.matrix_text(region=(0, 0, 24, 24), indices=True))
