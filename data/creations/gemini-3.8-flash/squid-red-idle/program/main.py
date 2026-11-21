# Squid Red Idle Animation - 3 Frames
import numpy as np

# Canvas settings
w, h = 58, 57
cw, ch = 58, 60
pad_y = 2

# Palette colors mapping
pal_colors = {}
for p in input_canvas.palette():
    pal_colors[p['index']] = tuple(p['rgba'])

# Extract input pixel grid
grid = np.zeros((h, w), dtype=int)
for y in range(h):
    for x in range(w):
        grid[y, x] = input_canvas.get(x, y)

# Define head mask:
# The head consists of the mantle, crests, horns, eyes, mouth, and chin.
# The base consists of the outer and inner tentacles and the collar.
head_mask = np.zeros((h, w), dtype=bool)
for y in range(h):
    for x in range(w):
        if grid[y, x] == 0:
            continue
        # Outer tentacle tips curling up on sides
        if (x <= 5 or x >= 52) and y >= 34:
            continue
        # Inner tentacles and belly
        if y >= 40:
            continue
        # Row 39: chin is part of head
        if y == 39:
            if 26 <= x <= 31:
                head_mask[y, x] = True
            continue
        head_mask[y, x] = True

# Base mask is all sprite pixels that are not head, plus collar backing
base_grid = np.zeros((h, w), dtype=int)
for y in range(h):
    for x in range(w):
        if grid[y, x] != 0 and not head_mask[y, x]:
            base_grid[y, x] = grid[y, x]

# Collar backing under the chin/neck for seamless upward bobbing
# Under chin at row 39: dark red shadow (color 3)
for x in range(26, 32):
    base_grid[39, x] = 3

# At row 38 behind mouth: purple (color 6) and grey (color 7) collar
for x in range(22, 36):
    if 24 <= x <= 33:
        base_grid[38, x] = 7  # grey
    else:
        base_grid[38, x] = 6  # purple

# Frame 1: Exact original picture content
f1 = new_canvas(cw, ch, name="f1")
f1.blit(input_canvas, 0, pad_y)

# Helper function to construct bobbed frame
def make_bob_frame(name, dy):
    frame = new_canvas(cw, ch, name=name)
    # 1. Draw base (tentacles and collar) at neutral pad_y
    for y in range(h):
        for x in range(w):
            c = base_grid[y, x]
            if c != 0:
                frame.set(x, y + pad_y, pal_colors[c])
    # 2. Draw head shifted by dy
    for y in range(h):
        for x in range(w):
            if head_mask[y, x]:
                c = grid[y, x]
                frame.set(x, y + pad_y + dy, pal_colors[c])
    return frame

# Frame 2: Bob gently UP by 1 pixel (inhale)
f2 = make_bob_frame("f2", dy=-1)

# Frame 3: Bob gently DOWN by 1 pixel (exhale)
f3 = make_bob_frame("f3", dy=+1)

# Preview all frames
view(f1)
view(f2)
view(f3)

# Submit the 3 frames in order
finish([f1, f2, f3])
