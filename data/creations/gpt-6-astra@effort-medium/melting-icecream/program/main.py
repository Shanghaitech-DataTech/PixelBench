result = input_canvas.copy(name='output')
# Softened chocolate apron and three unequal, rounded streams.
dark = '#61363d'
mid = '#95524c'
light = '#c46f5b'
result.poly([(20,30),(41,30),(41,35),(40,35),(40,39),(39,40),(37,40),(36,39),(36,35),(35,35),(35,44),(36,44),(36,47),(35,49),(33,49),(32,48),(32,39),(31,37),(29,36),(28,37),(28,42),(27,44),(25,44),(24,43),(24,36),(22,35),(20,35)],dark)
# Lit face of the melting edge connects to the existing scoop shading.
result.poly([(27,29),(39,29),(40,31),(39,35),(39,38),(38,39),(37,38),(37,34),(35,33),(33,34),(34,38),(34,44),(35,45),(35,47),(34,48),(33,47),(33,39),(32,36),(30,34),(28,34),(27,36),(27,41),(26,43),(25,42),(25,35),(23,33),(26,32)],mid)
result.rect(25,35,1,6,light)
result.rect(33,38,1,7,light)
result.set(34,46,light)
result.rect(37,33,1,4,light)
# A falling bead below the outside drip.
result.rect(39,43,2,2,dark)
result.rect(38,45,4,2,dark)
result.rect(39,47,2,1,dark)
result.rect(39,45,2,1,mid)
view(result)
finish(result)
