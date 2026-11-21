from pixelbench_api import *

c = new_canvas(16, 16, name="magnifier")

ink = c.color("#1b1e23")      # dark rim
glass = c.color("#b9ddf4")    # light blue glass
deep = c.color("#8cc0e6")     # deeper blue (inner shadow)
shine = c.color("#ffffff")   # glint
handle = c.color("#7a5230")  # wooden handle
handle_dark = c.color("#5a3a20")

# handle first (rim sits in front of its start)
c.line(9, 9, 14, 14, handle)
c.line(10, 9, 14, 13, handle_dark)  # shaded edge

# lens rim (1 px) and glass
c.circle(6, 6, 4, ink, fill=False)
c.circle(6, 6, 3, glass, fill=True)

# inner shadow crescent at the bottom-left of the glass
c.set(4, 7, deep)
c.set(5, 8, deep)
c.set(6, 8, deep)

# glint (inside the glass, top-left)
c.set(4, 4, shine)
c.set(5, 4, shine)
c.set(4, 5, shine)

print(c.stats_text())
print(c.matrix_text())
finish(c)
