output = input_canvas.copy(name='output')
# Replace only the flesh in the lowest chamber with the existing cream rind.
# The orange partition and both upper segments remain pixel-for-pixel intact.
right_edges = {37:24, 38:24, 39:24, 40:24, 41:24, 42:26, 43:26,
               44:28, 45:27, 46:28, 47:31, 48:31, 49:28, 50:27}
for y, right in right_edges.items():
    left = 20 if y >= 49 else (12 if y == 46 else 8)
    for x in range(left, right + 1):
        if input_canvas.get(x, y) in (7, 8):
            output.set(x, y, 6)
view(output, scale=8)
finish(output)
