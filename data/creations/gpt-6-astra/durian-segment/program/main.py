output = input_canvas.copy(name='output')
# The lower pod lies left of the diagonal pith ridge. Keep the ridge
# and both upper pods exactly as drawn; reveal the cream inner rind.
right_edge = {35:23,36:23,37:24,38:24,39:24,40:24,41:24,42:26,43:26,44:28,45:27,46:28,47:31,48:31,49:34,50:34}
for y, xmax in right_edge.items():
    for x in range(xmax+1):
        if input_canvas.get(x,y) in (7,8):
            output.set(x,y,6)
view(output,scale=8)
finish(output)
