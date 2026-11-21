from pixelbench_api import input_canvas, finish

out = input_canvas.copy(name='output')

# Remove the bottom durian segment's flesh so the rind underneath is exposed.
# The bottom segment is the fleshy lobe at rows 51-55, x 11-39.
# Replace its flesh (palette 6,7,8,9) with the rind colour (palette 5).
# The other two pieces are untouched.
FLESH = {6, 7, 8, 9}
for y in range(51, 56):
    for x in range(11, 40):
        if out.get(x, y) in FLESH:
            out.set(x, y, 5)

finish(out)
