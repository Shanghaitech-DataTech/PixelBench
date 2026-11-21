result = input_canvas.copy(name='output')
edge = '#5e363e'
choc = '#95524c'
light = '#ba6d5b'
glint = '#c3715b'
# Melt hangs from the existing chocolate collar, with three unequal rivulets.
result.poly([(19,30),(25,30),(27,32),(28,33),(29,32),(29,30),(35,30),(36,32),(38,31),(41,30),(41,36),(40,36),(40,39),(39,40),(37,40),(36,39),(36,35),(35,35),(34,36),(34,43),(33,43),(33,47),(32,49),(30,49),(29,47),(29,39),(28,38),(28,35),(26,35),(26,38),(25,38),(25,41),(24,43),(22,43),(21,41),(21,36),(20,35),(19,35)],edge)
# Warm body colour is kept inside the dark single-pixel silhouettes.
result.poly([(20,31),(24,31),(24,33),(26,33),(26,34),(24,35),(24,40),(23,42),(22,40),(22,35),(21,34),(20,34)],choc)
result.poly([(30,31),(34,31),(34,34),(33,35),(33,42),(32,43),(32,47),(31,48),(30,46),(30,38),(29,37),(29,34)],choc)
result.poly([(38,32),(40,31),(40,35),(39,36),(39,39),(38,39),(37,38),(37,34)],choc)
# Narrow reflected light and rounded glints describe glossy liquid.
result.line(23,34,23,38,light)
result.set(23,40,glint)
result.line(32,34,32,40,light)
result.line(31,41,31,45,light)
result.set(31,47,glint)
result.line(39,33,39,35,light)
result.set(38,38,glint)
# A shallow glossy fold where the central stream spills over the rim.
result.line(30,32,33,32,light)
print(result.stats_text())
print(result.matrix_text(region=(18,29,42,50)))
save('melting-icecream',result)
finish(result)
