from pixelbench_api import *

c = input_canvas.copy(name="output")
w, h = c.stats()["size"]
SNOW = c.color((230, 235, 242, 255))     # bright snow white
SNOWB = c.color((195, 210, 229, 255))    # pale blue shaded snow

tree = [[c.get(x, y) for x in range(w)] for y in range(h)]

def is_tree(x, y):
    if 0 <= x < w and 0 <= y < h:
        return tree[y][x] != 0
    return False

# top surface pixels: tree pixel with transparency above
caps = set()
for y in range(h):
    for x in range(w):
        if is_tree(x, y) and not is_tree(x, y - 1):
            caps.add((x, y))

# a second snow row (shaded) directly below each cap pixel on the tree
for (x, y) in list(caps):
    if is_tree(x, y + 1):
        caps.add((x, y + 1))

toprow = set()
for (x, y) in caps:
    if is_tree(x, y - 1) or (x, y - 1) in caps:
        c.set(x, y, SNOWB)
    else:
        toprow.add((x, y))
for (x, y) in toprow:
    c.set(x, y, SNOW)

finish(c)
