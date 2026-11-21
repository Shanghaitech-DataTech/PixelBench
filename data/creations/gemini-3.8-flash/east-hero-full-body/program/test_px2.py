from pixelbench_api import *
c = new_canvas(10, 10)
c.set(3, 4, "#ff0000")
idx = c.get(3, 4)
print("len px:", len(c.px), "px[4*10+3]:", c.px[4*10+3], "idx:", idx)
