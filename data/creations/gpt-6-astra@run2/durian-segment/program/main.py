output = input_canvas.copy(name='output')
# The diagonal orange partition is the edge of the middle piece.
# Only the yellow pixels on its lower-left side belong to the removed piece.
limits = {37:23,38:23,39:23,40:23,41:23,42:26,43:26,44:28,45:27,46:27,47:30,48:30,49:28,50:27}
removed = set()
for y, xmax in limits.items():
    for x in range(6,xmax+1):
        if input_canvas.get(x,y) in (7,8) and not (y==49 and x<10):
            output.set(x,y,6)
            removed.add((x,y))
# A thin warm inner-rind shadow follows the bottom of the empty chamber.
shade = '#e8dba8'
for x,y in removed:
    if y>=48 and (x,y+1) not in removed:
        output.set(x,y,shade)
view(output, scale=8)
finish(output)
