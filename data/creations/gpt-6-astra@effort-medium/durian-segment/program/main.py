output = input_canvas.copy(name='output')
# Clear the lowest pod back to the pale inner rind, up to its dividing seam.
ranges = {35:(15,24),36:(15,24),37:(14,25),38:(14,25),39:(13,25),40:(12,25),41:(11,27),42:(10,27),43:(9,27),44:(8,29),45:(8,30),46:(8,30),47:(9,31),48:(14,32),49:(19,28),50:(19,27)}
for y,(left,right) in ranges.items():
    for x in range(left,right+1):
        if output.get(x,y) in [input_canvas.color('#ffda45'),input_canvas.color('#ffc830'),input_canvas.color('#e08c37')]:
            output.set(x,y,'#fbf4c9')
output.set(6,46,'#fbf4c9')
# A narrow warm shadow in the empty rind recess follows the lower pod bed.
shade='#e7d8a2'
for y,left,right in [(44,10,11),(45,11,14),(46,14,18),(47,18,26),(48,21,29),(49,23,27)]:
    output.line(left,y,right,y,shade)
view(output,scale=8)
finish(output)
