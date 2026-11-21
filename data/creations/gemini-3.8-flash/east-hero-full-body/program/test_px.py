from pixelbench_api import *
c = new_canvas(10, 10)
print("type of px:", type(c.px), getattr(c.px, 'shape', None))
