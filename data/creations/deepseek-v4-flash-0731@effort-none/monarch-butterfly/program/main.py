from pixelbench_api import *

c = new_canvas(32, 32, name="monarch")

# Colors
ORANGE = c.color("#e8701a")
ORANGE2 = c.color("#c9520d")   # darker orange for depth
BLACK = c.color("#181818")
WHITE = c.color("#f8f8f8")

# ---- Body (center columns 15,16) ----
# Head
c.rect(14, 3, 4, 2, BLACK)
c.rect(15, 2, 2, 1, BLACK)
# Thorax
c.rect(14, 5, 4, 3, BLACK)
# Abdomen (tapered)
c.rect(14, 8, 4, 5, BLACK)
c.rect(15, 13, 2, 2, BLACK)
c.rect(15, 15, 2, 2, BLACK)
c.rect(15, 17, 2, 2, BLACK)
c.rect(15, 19, 2, 2, BLACK)
c.rect(15, 21, 2, 2, BLACK)
c.rect(15, 23, 2, 2, BLACK)
# Antennae
c.line(16, 3, 13, 0, BLACK)
c.set(13, 0, BLACK)
c.line(15, 3, 18, 0, BLACK)
c.set(18, 0, BLACK)

# ---- Upper wings ----
# Left upper wing: broad rounded fill
c.ellipse(10, 10, 7, 5, ORANGE)     # main blob
c.ellipse(31-10, 10, 7, 5, ORANGE)
# Extend outward to reach near edge
c.ellipse(7, 9, 4, 4, ORANGE)
c.ellipse(31-7, 9, 4, 4, ORANGE)
# Inner depth shade
c.ellipse(10, 11, 4, 3, ORANGE2)
c.ellipse(31-10, 11, 4, 3, ORANGE2)

# ---- Lower wings ----
c.ellipse(10, 21, 6, 4, ORANGE)
c.ellipse(31-10, 21, 6, 4, ORANGE)
c.ellipse(7, 22, 3, 3, ORANGE)
c.ellipse(31-7, 22, 3, 3, ORANGE)
c.ellipse(10, 22, 3, 2, ORANGE2)
c.ellipse(31-10, 22, 3, 2, ORANGE2)

# ---- Black wing borders / outlines ----
# Upper wing outline (left)
c.ellipse(10, 10, 7, 5, BLACK, fill=False)
c.ellipse(31-10, 10, 7, 5, BLACK, fill=False)
# Outer extension outline
c.ellipse(7, 9, 4, 4, BLACK, fill=False)
c.ellipse(31-7, 9, 4, 4, BLACK, fill=False)
# Lower wing outline
c.ellipse(10, 21, 6, 4, BLACK, fill=False)
c.ellipse(31-10, 21, 6, 4, BLACK, fill=False)
c.ellipse(7, 22, 3, 3, BLACK, fill=False)
c.ellipse(31-7, 22, 3, 3, BLACK, fill=False)

# ---- Black veins ----
# Upper wing veins (left)
c.line(14, 7, 8, 7, BLACK)
c.line(14, 10, 5, 9, BLACK)
c.line(14, 12, 7, 13, BLACK)
# Upper wing veins (right, mirror)
c.line(17, 7, 23, 7, BLACK)
c.line(17, 10, 26, 9, BLACK)
c.line(17, 12, 24, 13, BLACK)
# Lower wing veins
c.line(14, 19, 7, 20, BLACK)
c.line(14, 22, 5, 22, BLACK)
c.line(14, 24, 8, 25, BLACK)
c.line(17, 19, 24, 20, BLACK)
c.line(17, 22, 26, 22, BLACK)
c.line(17, 24, 23, 25, BLACK)

# ---- White spots (edge dots) ----
# Upper wing outer edge (left)
for (x,y) in [(5,7),(4,9),(4,11),(5,12),(7,14),(6,6),(8,6)]:
    c.set(x, y, WHITE)
    c.set(31-x, y, WHITE)
# Lower wing outer edge
for (x,y) in [(4,21),(4,23),(6,25),(7,19)]:
    c.set(x, y, WHITE)
    c.set(31-x, y, WHITE)

print(c.stats_text())
print(c.matrix_text(region=(0,0,31,31)))
finish(c)
