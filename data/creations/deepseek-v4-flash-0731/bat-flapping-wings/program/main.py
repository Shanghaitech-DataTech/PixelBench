from pixelbench_api import input_canvas, finish, new_canvas

src = input_canvas
W, H = 27, 22

# Frame 1: original picture content, exact copy
f1 = src.copy(name="f1")

# Frame 2: bat flapping - wings open up into a spread, raised position.
# Keep head/ears (rows 0..5) and the centre body seam; flip each wing
# vertically about the body's mid-height so the drooping wing tips rise
# up outward to the top corners while the body stays in place.
f2 = new_canvas(W, H, name="f2")

def set_idx(c, x, y, idx):
    if idx is not None and idx != 0:
        c.set(x, y, idx)

for y in range(6):
    for x in range(W):
        set_idx(f2, x, y, src.get(x, y))
for y in range(6, H):
    set_idx(f2, 13, y, src.get(13, y))
for y in range(6, H):
    for x in range(W):
        if x <= 12 or x >= 14:
            set_idx(f2, x, 26 - y, src.get(x, y))

print(f1.stats_text())
print(f2.stats_text())

finish([f1, f2])
