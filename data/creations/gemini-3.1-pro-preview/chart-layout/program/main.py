from pixelbench_api import *

c = new_canvas(128, 64)

# Background
c.rect(0, 0, 128, 64, "#1e1e2e")

# Grid and Axis
grid_col = "#313244"
axis_col = "#cdd6f4"
text_col = "#a6adc8"

# Title
title = "FRUIT DATA"
w = len(title) * 6 - 1
c.text(64 - w//2, 2, title, text_col, font="5x7")

# Y-axis
c.line(16, 10, 16, 52, axis_col)
# X-axis
c.line(16, 52, 120, 52, axis_col)

# Grid lines
for val in [5, 10, 15]:
    y = 52 - val * 3
    c.line(14, y, 120, y, grid_col)
    c.line(14, y, 16, y, axis_col) # tick
    # Label
    s_val = str(val)
    w = len(s_val) * 6 - 1
    c.text(13 - w, y - 3, s_val, text_col, font="5x7")

# Label 0
c.text(13 - 5, 52 - 3, "0", text_col, font="5x7")

# Data
data = [
    ("Apple", 10, "#ff4444"),
    ("Banana", 5, "#ffdd00"),
    ("Orange", 7, "#ff8800"),
    ("Lemon", 14, "#ffff44"),
    ("Grape", 2, "#aa44ff")
]

for i, (name, val, col) in enumerate(data):
    cx = 26 + i * 22
    h = val * 3
    # Main bar
    c.rect(cx - 5, 52 - h, 11, h, col)
    # Shading
    c.rect(cx + 1, 52 - h, 5, h, "#00000033")
    # Highlight
    c.line(cx - 5, 52 - h, cx - 5, 52 - 1, "#ffffff55")
    # Top edge
    c.line(cx - 5, 52 - h, cx + 5, 52 - h, "#ffffffaa")

# Icons
# Apple
cx, cy = 26, 58
c.circle(cx, cy, 2, "#ff4444")
c.set(cx, cy-3, "#885533") # stem
c.set(cx+1, cy-3, "#44aa44") # leaf

# Banana
cx, cy = 48, 58
banana_pts = [(0,-2), (-1,-1), (-2,0), (-2,1), (-1,2), (0,2), (1,1), (2,0), (3,-1)]
for dx, dy in banana_pts:
    c.set(cx+dx, cy+dy, "#ffdd00")
c.set(cx, cy-2, "#88aa22")
c.set(cx+3, cy-1, "#88aa22")

# Orange
cx, cy = 70, 58
c.circle(cx, cy, 2, "#ff8800")
c.set(cx, cy-3, "#44aa44") # leaf
c.set(cx+1, cy-3, "#44aa44")

# Lemon
cx, cy = 92, 58
c.ellipse(cx, cy, 3, 2, "#ffff44")
c.set(cx-3, cy, "#ddcc22")
c.set(cx+3, cy, "#ddcc22")

# Grape
cx, cy = 114, 58
grape_pts = [(0,-1), (1,-1), (-1,0), (0,0), (1,0), (2,0), (-1,1), (0,1), (1,1), (0,2)]
for dx, dy in grape_pts:
    c.set(cx+dx, cy+dy, "#aa44ff")
c.set(cx, cy-2, "#44aa44") # stem/leaf

finish(c)
