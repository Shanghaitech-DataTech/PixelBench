from pixelbench_api import *

c = new_canvas(16, 16, background="#7f7f7f", name="stone")

G = "#7f7f7f"   # base gray
D = "#5f5f5f"   # dark speckle
L = "#9a9a9a"   # light speckle
C = "#4a4a4a"   # crack
CL = "#6b6b6b"  # crack highlight edge

# speckle noise (deterministic pattern)
dark = [(1,1),(4,0),(7,2),(10,1),(13,3),(2,5),(6,6),(9,4),(12,7),(0,8),(3,9),
        (5,11),(8,9),(11,12),(14,10),(1,13),(4,14),(7,15),(10,14),(13,13),(15,5),(15,12)]
light = [(3,2),(6,1),(9,0),(12,2),(0,4),(5,5),(8,6),(11,5),(14,7),(2,8),(7,10),
         (10,9),(13,11),(0,12),(3,15),(6,13),(9,12),(12,15),(15,1),(15,9)]
for x,y in dark: c.set(x,y,D)
for x,y in light: c.set(x,y,L)

# crack running diagonally across the tile
crack = [(2,0),(2,1),(3,2),(3,3),(4,4),(4,5),(5,6),(6,7),(6,8),(7,9),(7,10),
         (8,11),(9,12),(9,13),(10,14),(10,15)]
for x,y in crack:
    c.set(x,y,C)
# small branch
for x,y in [(4,4),(5,3),(6,3),(7,2)]:
    c.set(x,y,C)
# highlight along crack edge for depth
for x,y in [(3,1),(4,2),(4,3),(5,4),(5,5),(6,6),(7,7),(7,8),(8,9),(8,10),(9,11),(10,12),(10,13),(11,14)]:
    if c.get(x,y) == c.color(G):
        c.set(x,y,CL)

# make it seamless: crack enters top and exits bottom at matching x offsets
# top entry at (2,0), bottom exit at (10,15) -> also mirror entry/exit continuity
# add a second subtle crack on right side wrapping horizontally
crack2 = [(12,3),(13,4),(14,5),(15,6),(0,7),(1,8),(2,9)]
for x,y in crack2: c.set(x,y,C)
for x,y in [(13,3),(14,4),(15,5),(0,6),(1,7),(2,8)]:
    if c.get(x,y) == c.color(G):
        c.set(x,y,CL)

print(c.stats_text())
save("stone_cracked", c)
finish(c)
