from pixelbench_api import *

# diagnostic: how do ellipses / paths rasterize?
a = new_canvas(32, 32, name="diag")
a.ellipse(14, 20, 10, 6, '#ff0000')
a.circle(23, 9, 4, '#00ff00')
print("ellipse(14,20,10,6) + circle(23,9,4)")
print(a.matrix_text())
