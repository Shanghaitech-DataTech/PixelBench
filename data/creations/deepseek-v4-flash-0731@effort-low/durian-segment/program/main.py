from pixelbench_api import *
import numpy as np

c = input_canvas.copy(name="output")
W, H = 64, 64
flesh = {6, 7, 8, 9}   # durian flesh (cream/yellow/orange)
rind = c.color((190,111,72))  # color 5, the rind brown

# Remove the bottom segment of durian flesh so the rind underneath is exposed.
# The bottom lobe is the lower portion of the flesh (y >= 44); replace it with rind.
for y in range(44, 64):
    for x in range(64):
        if c.get(x, y) in flesh:
            c.set(x, y, rind)

finish(c)
