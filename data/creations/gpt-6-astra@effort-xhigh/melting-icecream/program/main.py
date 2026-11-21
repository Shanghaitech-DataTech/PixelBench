# Melt the existing chocolate over the rim and onto the cone.
result = input_canvas.copy(name='output')
edge = '#5e363e'
shade = '#7b4344'
choc = '#95524c'
light = '#c46f5b'

# The dark chocolate rim sags into three distinct, round-ended streams.
result.poly([(20,29),(41,29),(41,35),(40,35),(40,41),(39,41),(39,43),(37,43),(37,41),(36,41),(36,36),(34,36),(34,35),(32,35),(32,40),(31,40),(31,44),(32,44),(32,48),(31,48),(31,50),(28,50),(28,48),(27,48),(27,44),(28,44),(28,38),(26,38),(26,36),(25,36),(25,40),(24,40),(24,41),(22,41),(22,39),(21,39),(21,35),(20,35)],edge)
# Broad, flowing body connects naturally to the brown side of the scoop.
result.poly([(25,28),(34,29),(39,28),(41,29),(40,33),(38,34),(35,33),(33,32),(30,33),(29,36),(26,35),(25,33),(23,33),(22,31)],shade)
result.poly([(28,28),(34,29),(39,28),(39,31),(38,33),(36,33),(34,32),(31,32),(29,34),(27,34),(26,32),(25,31),(25,30)],choc)
# Short left run, with its rounded end still hanging over the cone rim.
result.rect(22,33,3,4,shade)
result.rect(23,35,2,4,shade)
result.rect(22,33,2,3,choc)
result.set(23,37,choc)
# The principal stream narrows, then gathers into a weighted tip.
result.poly([(27,32),(31,32),(31,38),(30,38),(30,44),(31,44),(31,47),(30,49),(29,49),(28,47),(28,45),(29,43),(29,36),(27,36)],shade)
result.poly([(27,32),(30,32),(30,36),(29,36),(29,42),(30,44),(30,47),(29,47),(28,46),(29,43),(29,35),(27,35)],choc)
# A smaller flow hugs the right of the cone.
result.poly([(37,32),(39,32),(39,39),(38,42),(37,40)],shade)
result.rect(37,33,2,5,choc)
result.rect(37,38,1,2,choc)
# Restrained warm reflections emphasize the liquid surface.
result.rect(27,32,2,2,light)
result.line(29,35,29,39,light)
result.set(29,45,light)
result.rect(37,33,1,3,light)

# One falling drop below the shorter side stream completes the melting motion.
result.set(40,46,edge)
result.rect(39,47,3,3,edge)
result.set(40,50,edge)
result.rect(40,47,1,3,choc)
result.set(40,48,light)

view(result, scale=8)
finish(result)
