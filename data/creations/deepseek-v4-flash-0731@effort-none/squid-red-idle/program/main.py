from pixelbench_api import *

c = input_canvas
W, H = c.stats()['size']  # 58 x 57

# Use a taller canvas to give room for the bob.
CW, CH = 58, 60

f1 = new_canvas(CW, CH, name='f1')
f2 = new_canvas(CW, CH, name='f2')
f3 = new_canvas(CW, CH, name='f3')

# Split point: head is rows 0..43, tentacles rows 44..56.
cut = 44

# Frame 1: whole original at y=1
f1.blit(c, 0, 1)

head_sel = c.select(0, 0, W, cut)          # rows 0..44
tent_sel = c.select(0, cut, W, H - cut)     # rows 44..56

# Tentacles stay fixed at y=45 for frames 2 & 3.
# Head bobs: frame 2 at y=0, frame 3 at y=2.
# Copy tentacles first so head overwrites on overlap.
tent_sel.copy_to(0, 45, f2)
head_sel.copy_to(0, 0, f2)

tent_sel.copy_to(0, 45, f3)
head_sel.copy_to(0, 2, f3)

finish([f1, f2, f3])

print("Frame 1 stats:", f1.stats())
print("Frame 2 stats:", f2.stats())
print("Frame 3 stats:", f3.stats())
