# Inspect the parrots
import numpy as np

# Let's inspect where pixels differ from background (c0 is white, index 1)
# What is the background color? (255, 255, 255)
w, h = input_canvas.size
pixels = np.zeros((h, w), dtype=int)
for y in range(h):
    for x in range(w):
        pixels[y, x] = input_canvas.get(x, y)

print("Background index:", input_canvas.get(0, 0)) # index 1

# Let's see non-white pixels
non_bg = (pixels != 1)
ys, xs = np.where(non_bg)
print(f"Non-bg x range: {xs.min()}..{xs.max()}, y range: {ys.min()}..{ys.max()}")

# Left bird vs right bird x split:
mid_x = 32
left_bird = pixels[:, :mid_x]
right_bird = pixels[:, mid_x:]

print("Left bird non-bg x:", np.where(left_bird != 1)[1].min(), np.where(left_bird != 1)[1].max())
print("Right bird non-bg x:", np.where(right_bird != 1)[1].min() + mid_x, np.where(right_bird != 1)[1].max() + mid_x)

# Check if right bird is mirrored left bird
left_mirrored = np.fliplr(left_bird)
print("Is right bird exactly flipped left bird?", np.array_equal(left_mirrored, right_bird))
if not np.array_equal(left_mirrored, right_bird):
    diff = (left_mirrored != right_bird)
    print(f"Diff count: {np.sum(diff)}")
    for y, x in zip(*np.where(diff)):
        print(f"y={y}, x_right={x+mid_x}, right_val={right_bird[y, x]}, left_mirrored_val={left_mirrored[y, x]}")

# Print colors used in right bird
unique_r, counts_r = np.unique(right_bird, return_counts=True)
for u, c in zip(unique_r, counts_r):
    print(f"Right bird color {u} ({input_canvas.color_name(u)}): {c} pixels")
