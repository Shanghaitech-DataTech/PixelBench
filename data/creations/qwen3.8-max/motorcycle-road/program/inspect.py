from pixelbench_api import *

c = input_canvas
print(c.stats_text())
print(c.matrix_text())
print("palette:")
for p in c.palette():
    print(p)
