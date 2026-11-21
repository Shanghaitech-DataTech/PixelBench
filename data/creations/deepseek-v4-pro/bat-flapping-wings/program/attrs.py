from pixelbench_api import *
c = input_canvas
print([a for a in dir(c) if not a.startswith('_')])
