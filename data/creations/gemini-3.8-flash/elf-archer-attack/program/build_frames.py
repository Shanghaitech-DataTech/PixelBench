from pixelbench_api import *

W, H = 48, 48
dx, dy = 5, 0

# Frame 1: input canvas placed on 48x48
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, dx, dy)

# Frame 2: start from a copy of f1 as base, or build from scratch
f2 = new_canvas(W, H, name="frame2")
f2.blit(input_canvas, dx, dy)

# Create a side-by-side comparison canvas to view both frames
comp = new_canvas(W * 2 + 4, H, name="comp")
comp.blit(f1, 0, 0)
comp.blit(f2, W + 4, 0)

view(comp)
print("Canvas created successfully")
