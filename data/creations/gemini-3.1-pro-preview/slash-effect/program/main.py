from pixelbench_api import *

c = new_canvas(48, 48)

white = c.color("#ffffff")
cyan = c.color("#00ffff")
blue = c.color("#0080ff")

# Frame 1: Left half (0-23)
path1 = "M 18 12 Q 4 24 10 36 Q 12 24 18 12 Z"
c.path(path1, white, fill=True)

# Frame 2: Right half (24-47)
# Trailing streak (Blue)
path2_blue = "M 44 6 Q 24 24 28 42 Q 46 24 44 6 Z"
c.path(path2_blue, blue, fill=True)

# Cyan middle
path2_cyan = "M 43 7 Q 24 24 28 42 Q 38 24 43 7 Z"
c.path(path2_cyan, cyan, fill=True)

# White leading edge
path2_white = "M 42 8 Q 24 24 28 42 Q 30 24 42 8 Z"
c.path(path2_white, white, fill=True)

# Add some trailing particles / streaks
c.line(44, 16, 46, 14, blue)
c.line(42, 28, 45, 26, blue)
c.line(38, 36, 41, 34, blue)
c.set(45, 20, cyan)
c.set(43, 32, cyan)

finish(c)
