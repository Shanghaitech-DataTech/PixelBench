from pixelbench_api import *

c = new_canvas(16, 16, name="base")
edge  = c.color("#4a3208", "edge")
mid   = c.color("#d9a521", "mid")

c.ellipse(7.5, 7.5, 6.5, 6.5, edge, fill=True)
c.ellipse(7.5, 7.5, 5.5, 5.5, mid, fill=True)

print(c.matrix_text())
