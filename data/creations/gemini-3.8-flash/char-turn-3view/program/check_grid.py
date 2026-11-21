# Check if pixels are grouped in blocks (e.g. 2x2 or 1x1)
# Let's check diffs between adjacent pixels
same_x = 0
diff_x = 0
for y in range(119):
    for x in range(65):
        if input_canvas.get(x, y) == input_canvas.get(x+1, y):
            same_x += 1
        else:
            diff_x += 1

print(f"Adjacent x: same={same_x}, diff={diff_x}")

# Let's inspect small regions, e.g. the eyes or outline
for y in range(35, 45):
    row = "".join(f"{input_canvas.get(x, y):2d} " for x in range(20, 46))
    print(f"y={y:2d}: {row}")
