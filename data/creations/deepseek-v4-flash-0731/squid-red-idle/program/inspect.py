from pixelbench_api import *

c = input_canvas
print("size:", c.stats()["size"])
print(c.stats_text())
print(c.palette())
