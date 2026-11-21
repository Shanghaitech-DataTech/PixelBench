result = input_canvas.copy(name='output')
dark = '#5e363e'
mid = '#95524c'
shade = '#7b4344'
light = '#ba6d5b'
# Chocolate flowing from the scoop's lower edge, with stepped round ends.
result.poly([(20,31),(26,31),(26,34),(25,34),(25,38),(24,38),(24,41),(21,41),(21,39),(20,39)],dark)
result.rect(21,33,3,5,shade)
result.rect(21,33,2,4,mid)
result.rect(22,38,2,2,shade)
# Long front rivulet, widening into a heavy rounded bead at the end.
result.poly([(26,30),(33,30),(33,34),(32,34),(32,39),(31,39),(31,44),(32,44),(32,47),(31,47),(31,48),(28,48),(28,47),(27,47),(27,43),(28,43),(28,36),(27,36),(27,34),(26,34)],dark)
result.poly([(27,30),(32,30),(32,34),(31,34),(31,38),(30,38),(30,44),(31,44),(31,46),(28,46),(28,44),(29,44),(29,35),(28,35),(28,33),(27,33)],shade)
result.rect(28,31,3,4,mid)
result.rect(29,35,2,6,mid)
result.rect(29,43,2,3,mid)
result.rect(28,32,1,3,light)
result.rect(29,36,1,4,light)
result.set(29,44,light)
# A second stream wraps over the right lip of the cone.
result.poly([(36,29),(41,29),(41,34),(40,34),(40,38),(41,38),(41,41),(40,41),(40,42),(37,42),(37,41),(36,41),(36,38),(37,38),(37,34),(36,34)],dark)
result.poly([(36,29),(40,29),(40,33),(39,33),(39,38),(40,38),(40,40),(37,40),(37,38),(38,38),(38,33),(36,33)],mid)
result.rect(37,31,2,2,light)
result.rect(38,34,1,4,light)
result.set(38,39,light)
# Detached drop, below the right-hand drip.
result.rect(38,45,2,1,dark)
result.rect(37,46,4,3,dark)
result.rect(38,49,2,1,dark)
result.rect(38,46,2,2,mid)
result.set(38,46,light)
view(result,scale=8,margin=0)
finish(result)
