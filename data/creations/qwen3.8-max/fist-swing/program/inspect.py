from pixelbench_api import *

c = input_canvas
for p in c.palette():
    print(p)
print(view(c, scale=8, margin=2, edges="all"))
