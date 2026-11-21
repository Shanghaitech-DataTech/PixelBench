from pixelbench_api import *

W, H = 58, 60
base_y = 2  # place original content rows 0..56 at y=base_y..base_y+56

def place_at(dy):
    c = new_canvas(W, H)
    c.blit(input_canvas, 0, base_y + dy)
    return c

# Frame 1: original picture content (unmodified), at base position.
f1 = place_at(0)
# Frame 2: idle - bobs up gently.
f2 = place_at(-1)
# Frame 3: idle - bobs down gently.
f3 = place_at(1)

for c in (f1, f2, f3):
    print(c.stats_text())

finish([f1, f2, f3])
