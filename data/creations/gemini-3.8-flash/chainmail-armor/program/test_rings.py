from pixelbench_api import *

c = new_canvas(32, 32)

# Interlocking rings test:
# Grid of ring centers:
# For row r = 0, 1, 2, ...
# y_center = r * 2 + 2
# if r is even: x_centers = 2, 6, 10, 14, 18, 22, 26
# if r is odd:  x_centers = 4, 8, 12, 16, 20, 24, 28

# Fill background with dark under-armor / void
c.rect(0, 0, 32, 32, "#181c24")

centers = []
for r in range(12):
    cy = r * 2 + 2
    offset = 4 if (r % 2 == 1) else 2
    for cx in range(offset, 30, 4):
        centers.append((cx, cy, r))

# Each ring has:
# top: cx, cy-1
# bottom: cx, cy+1
# left: cx-1, cy
# right: cx+1, cy
# hole: cx, cy

# Let's draw each ring:
# If top-left lighting:
# Top rim is brightest: #f8fafc or #e2e8f0
# Left rim is light: #cbd5e1
# Right rim is mid: #94a3b8
# Bottom rim is shadow: #475569
# Hole is dark: #0f172a or #181c24

# Let's paint them:
for cx, cy, r in centers:
    # hole
    c.set(cx, cy, "#111622")
    # top
    c.set(cx, cy - 1, "#f1f5f9")
    # left
    c.set(cx - 1, cy, "#cbd5e1")
    # right
    c.set(cx + 1, cy, "#94a3b8")
    # bottom
    c.set(cx, cy + 1, "#475569")

view(c)
