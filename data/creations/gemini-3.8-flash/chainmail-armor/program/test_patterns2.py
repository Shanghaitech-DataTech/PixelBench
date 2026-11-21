from pixelbench_api import *

c = new_canvas(32, 32)

# Test 1: Scalloped rings / C-rings (3x2)
# Ring shape:
# Row 0:  [H] [H] [.]
# Row 1:  [S] [.] [M]
# Staggered by 2 on next row:
for y in range(2, 14):
    row_offset = (y % 2) * 2
    for x in range(2, 14):
        p = (x + row_offset) % 3
        if y % 2 == 0:
            if p == 0: c.set(x, y, "#f1f5f9") # highlight
            elif p == 1: c.set(x, y, "#94a3b8") # midtone
            else: c.set(x, y, "#1e293b") # dark hole
        else:
            if p == 0: c.set(x, y, "#64748b") # shadow
            elif p == 1: c.set(x, y, "#1e293b") # dark hole
            else: c.set(x, y, "#cbd5e1") # light mid

# Test 2: Diagonal interlocking links (leaning rings)
# Like \ / \ /
# Let's test rings as little loops:
# e.g., 4x3 loop:
# . H H .
# S . . S
# . S S .
# With staggering
for y in range(2, 14):
    for x in range(18, 30):
        # A 4x2 loop weave
        # If we place ring centers at (x_c, y_c):
        # Even rows: centers at 0, 4, 8...
        # Odd rows: centers at 2, 6, 10...
        x_rel = (x - (y % 2) * 2) % 4
        y_rel = y % 2
        # In a 4x2 cell:
        # y_rel 0: 0:dark, 1:high, 2:high, 3:mid
        # y_rel 1: 0:mid,  1:dark, 2:dark, 3:shad
        # Let's see how that looks
        if y_rel == 0:
            cols = ["#1e293b", "#ffffff", "#cbd5e1", "#64748b"]
        else:
            cols = ["#64748b", "#334155", "#1e293b", "#94a3b8"]
        c.set(x, y, cols[x_rel])

# Test 3: Little circular link motif:
# Ring size 3x3 with spacing:
# Centers at (x0, y0):
#   H H
# H . . H
#   S S
# Staggered:
for y in range(18, 30):
    for x in range(2, 14):
        # Let's try 3x2 weave:
        # Ring top:
        # (x + y)%2 etc.
        pass

# Test 4: Another classic pixel art chainmail technique:
# Alternating rows of light arc and dark gap:
# Row 0: H H . H H . H H .
# Row 1: S D S S D S S D S
# Staggered by 1 or 2:
for y in range(18, 30):
    sh = ((y // 2) % 2) * 2
    if y % 2 == 0:
        for x in range(18, 30):
            p = (x + sh) % 3
            if p == 0: c.set(x, y, "#ffffff")
            elif p == 1: c.set(x, y, "#94a3b8")
            else: c.set(x, y, "#1e293b")
    else:
        for x in range(18, 30):
            p = (x + sh) % 3
            if p == 0: c.set(x, y, "#475569")
            elif p == 1: c.set(x, y, "#1e293b")
            else: c.set(x, y, "#64748b")

view(c)
