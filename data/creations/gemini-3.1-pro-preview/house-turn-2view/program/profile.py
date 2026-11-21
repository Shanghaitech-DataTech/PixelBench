from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']

max_x = [-1] * h
for y in range(h):
    for x in range(w-1, -1, -1):
        if c.get(x, y) != 0:
            max_x[y] = x
            break

print("Profile max_x:")
for y in range(0, h, 5):
    print(f"y={y}: {max_x[y]}")

# Let's find the wall part and roof part
# The wall is usually vertical, so max_x should be somewhat constant at the bottom
