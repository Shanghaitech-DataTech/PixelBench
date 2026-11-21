from pixelbench_api import input_canvas

c = input_canvas
w, h = c.stats()["size"]

def get(x, y):
    return c.get(x, y)

# Print left/right boundary of non-transparent pixels per row
for y in range(h):
    left = None
    right = None
    for x in range(w):
        if get(x, y) != 0:
            if left is None:
                left = x
            right = x
    print(f"y={y:3d} left={left} right={right} width={(right-left+1) if left is not None else 0}")
