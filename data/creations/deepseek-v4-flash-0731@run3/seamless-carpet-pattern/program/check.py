from pixelbench_api import *
import main

c = main.draw_carpet()
print(c.matrix_text(region=(4, 4, 12, 12), indices=True))
print("---- seam corner (0,0)-(7,7) ----")
print(c.matrix_text(region=(0, 0, 7, 7), indices=True))
