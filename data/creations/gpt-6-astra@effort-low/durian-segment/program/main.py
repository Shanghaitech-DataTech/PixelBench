output = input_canvas.copy(name='output')
cream='#fbf4c9'
# The lower chamber ends at the diagonal partition beside the middle lobe.
limits={35:23,36:23,37:24,38:24,39:23,40:23,41:23,42:26,43:26,44:28,45:27,46:27,47:30,48:31,49:29,50:28}
yellow={input_canvas.color('#ffda45'),input_canvas.color('#ffc830')}
for y,right in limits.items():
    for x in range(6,right+1):
        if input_canvas.get(x,y) in yellow:
            if (y==49 and x<19) or (y==50 and x<19):
                continue
            output.set(x,y,cream)
# Pale fibrous shading follows the floor of the emptied rind.
output.poly([(9,44),(13,46),(20,47),(26,47),(29,48),(26,50),(20,50),(16,48),(11,47)],'#e8dca9')
output.line(14,46,20,48,'#f2e8bb')
output.line(20,48,26,48,'#f2e8bb')
view(output)
finish(output)
