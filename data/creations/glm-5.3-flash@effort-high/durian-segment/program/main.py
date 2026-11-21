# Edit task: remove the bottom segment of durian flesh so the rind underneath
# is exposed; keep the other two pieces unchanged.
#
# The durian drawing has three flesh pieces:
#   - top piece: flesh around y=12-14
#   - main body: flesh y=15-51
#   - bottom piece: flesh at y=52-53 sitting in its rind cup (y=54-57)
#
# The bottom piece's flesh uses the cream/yellow flesh colours
#   f = c5 (#fbf4c9), g = c6 (#ffc830)
# while the rind underneath uses
#   e = c4 (#be6f48) and i = c8 (#ef9d0e).
#
# Replacing the flesh pixels of the bottom segment with the rind colour
# exposes the rind, as if the segment had been taken away.

result = input_canvas.copy(name='output')

for y in range(52, 54):          # bottom segment flesh rows only
    for x in range(64):
        idx = result.get(x, y)
        if idx in (6, 7, 8):     # f, g, h flesh colours
            result.set(x, y, 5)  # e rind colour

finish(result)
