from pixelbench_api import *
c = new_canvas(4, 4)
print(repr(c.get(0, 0)))
c.set(1, 1, "#ff0000")
print(repr(c.get(0, 0)), repr(c.get(1, 1)))
