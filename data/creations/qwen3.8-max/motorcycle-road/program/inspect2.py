from pixelbench_api import *

c = input_canvas
print(view(c, scale=6))

sp = c.copy(name="sprite")
sp.fill_at(0, 0, None)
print(sp.stats_text())
print(view(sp, scale=6))
print(sp.matrix_text())
