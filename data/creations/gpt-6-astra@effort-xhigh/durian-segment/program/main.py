output = input_canvas.copy(name='output')
# The bottom flesh lies to the left of the ochre contour of the middle lobe.
# Keep that contour, the two upper lobes and the outer shell pixel-exact.
right_edges = {37:24, 38:24, 39:24, 40:24, 41:24, 42:26, 43:26,
               44:28, 45:27, 46:28, 47:31, 48:31, 49:28, 50:27}
for y, right in right_edges.items():
    for x in range(6, right + 1):
        if input_canvas.get(x, y) in (7, 8):
            # The two pixels below the left rim belong to the shell itself.
            if y == 49 and x < 20:
                continue
            output.set(x, y, 6)
view(output, scale=8)
finish(output)
