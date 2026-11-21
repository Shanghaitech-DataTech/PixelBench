output = input_canvas.copy(name='output')
edge = '#5e363e'
shade = '#7b4344'
choc = '#95524c'
light = '#c46f5b'
glint = '#fcb58b'
# A melted skirt flows from the existing scoop into three unequal rivulets.
output.poly([(20,30),(27,30),(27,33),(26,33),(26,38),(25,38),(25,41),(22,41),(22,39),(21,39),(21,35),(20,35)], edge)
output.rect(22,32,3,6,shade)
output.rect(23,32,2,5,choc)
output.rect(23,33,1,3,light)
output.rect(23,38,1,2,choc)
# Long, rounded central drip with stepped shoulders and a bulbous end.
output.poly([(27,30),(36,30),(36,34),(35,34),(35,37),(34,37),(34,42),(35,42),(35,46),(34,46),(34,48),(30,48),(30,47),(29,47),(29,43),(30,43),(30,37),(29,37),(29,34),(27,34)],edge)
output.poly([(28,30),(35,30),(35,34),(33,34),(33,42),(34,42),(34,46),(33,46),(33,47),(31,47),(31,45),(30,45),(30,43),(31,43),(31,36),(30,36),(30,33),(28,33)],shade)
output.poly([(27,29),(35,29),(35,32),(33,32),(33,35),(32,35),(32,42),(31,42),(31,35),(30,35),(30,32),(27,32)],choc)
output.rect(30,32,1,4,light)
output.rect(31,36,1,5,light)
output.rect(31,43,2,3,choc)
output.set(31,43,light)
# A shorter run folds over the right edge of the cone.
output.poly([(37,29),(42,29),(42,34),(41,34),(41,39),(40,39),(40,41),(37,41),(37,39),(36,39),(36,36),(37,36)],edge)
output.poly([(37,30),(40,30),(40,34),(39,34),(39,39),(38,39),(38,37),(37,37)],choc)
output.rect(38,32,1,5,light)
output.set(38,31,glint)
# One suspended bead, separated from the right-hand drip.
output.rect(40,44,2,1,edge)
output.rect(39,45,4,3,edge)
output.rect(40,48,2,1,edge)
output.rect(40,45,2,2,choc)
output.set(40,45,light)
view(output)
finish(output)
