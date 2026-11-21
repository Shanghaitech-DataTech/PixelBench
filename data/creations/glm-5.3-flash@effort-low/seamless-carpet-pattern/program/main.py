from pixelbench_api import *

c = new_canvas(32, 32, background="#8c2f24", name="carpet")

# woven texture: subtle dither over the whole field
c.dither(0, 0, 32, 32, ["#8c2f24", "#9a3a2c"], pattern="checker")

def diamond(cx, cy, r, colour):
    for i in range(r + 1):
        for (x, y) in ((cx+i, cy-r+i), (cx-i, cy-r+i), (cx+i, cy+r-i), (cx-i, cy+r-i)):
            c.set(x % 32, y % 32, colour)

# diamonds on a 16px period grid -> seamless in x and y
for cx in (0, 16):
    for cy in (0, 16):
        diamond(cx, cy, 7, "#c4552f")      # solid body
        diamond(cx, cy, 7, "#e8c46a")      # gold outline (overwrites edge)
        diamond(cx, cy, 4, "#e8c46a")      # inner gold diamond
        diamond(cx, cy, 2, "#f2e3b3")      # cream core
        c.set(cx % 32, cy % 32, "#7a2418") # dark centre dot

# floral quatrefoil accents at the midpoints between diamonds: (8,0),(0,8),(24,0)...
for fx, fy in ((8, 0), (24, 0), (0, 8), (16, 8), (8, 16), (24, 16), (0, 24), (16, 24)):
    px, py = fx % 32, fy % 32
    c.set(px, py, "#f2e3b3")               # flower centre
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        c.set((px+dx) % 32, (py+dy) % 32, "#e8c46a")  # petals
    for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        c.set((px+dx) % 32, (py+dy) % 32, "#5f7a3a")  # leaves

print(c.stats_text())
save("carpet", c)
finish(c)
