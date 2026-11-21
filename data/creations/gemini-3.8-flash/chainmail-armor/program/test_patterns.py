from pixelbench_api import *

# Let's test a few chainmail ring pattern ideas on a small patch
c = new_canvas(32, 32)

# Pattern 1: 3x2 staggered rings
# Pattern 2: 2x2 staggered rings
# Pattern 3: Arc/loop shaped rings (3x3 or 4x3)

# Let's inspect them side by side
# Ring colors:
c_hi = "#f0f4f8"   # bright highlight on ring top
c_mid = "#9ab0c4"  # ring midtone
c_shad = "#4d5f75" # ring shadow
c_hole = "#1e2633" # hole inside/behind ring

# Idea A: 2x2 staggered
# (0,0)=hi, (1,0)=mid, (0,1)=shad, (1,1)=hole
for y in range(2, 12):
    for x in range(2, 12):
        ox = (y % 2)
        if (x + ox) % 2 == 0:
            c.set(x, y, c_hi if y % 2 == 0 else c_mid)
        else:
            c.set(x, y, c_hole if y % 2 == 0 else c_shad)

# Idea B: Distinct overlapping open loops (3x2)
# Row 0: . H M . H M
# Row 1: S D S S D S
# Staggered by 1 or 2
for y in range(2, 12):
    for x in range(16, 28):
        shift = (y % 2) * 2
        col = (x + shift) % 4
        if y % 2 == 0:
            if col == 0: c.set(x, y, c_hi)
            elif col == 1: c.set(x, y, c_mid)
            elif col == 2: c.set(x, y, c_shad)
            else: c.set(x, y, c_hole)
        else:
            if col == 0: c.set(x, y, c_hole)
            elif col == 1: c.set(x, y, c_shad)
            elif col == 2: c.set(x, y, c_hi)
            else: c.set(x, y, c_mid)

view(c)
