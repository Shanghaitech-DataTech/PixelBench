result = input_canvas.copy(name='output')
# Extend the existing chocolate into a stepped, flowing lower edge.
dark = '#5e363e'
body = '#95524c'
shine = '#c46f5b'
mid = '#7b4344'
result.poly([(21,30),(42,30),(42,36),(41,36),(41,39),(40,40),(37,40),(36,39),(36,35),(34,35),(34,44),(33,44),(33,48),(32,49),(30,49),(29,48),(29,40),(28,40),(28,42),(25,42),(24,41),(24,38),(23,38),(23,35),(21,35)], dark)
# Broad liquid folds merge back into the shaded scoop.
result.poly([(23,31),(29,31),(29,34),(27,34),(27,39),(26,40),(25,39),(25,36),(24,36),(24,34),(23,34)], mid)
result.poly([(28,29),(36,29),(36,32),(34,32),(34,34),(33,34),(33,42),(32,42),(32,47),(30,47),(30,37),(29,37),(29,33),(28,33)], body)
result.rect(30,34,1,10,shine)
result.rect(30,44,2,2,shine)
result.rect(30,32,2,2,'#9b5b52')
result.poly([(36,30),(41,30),(41,34),(40,34),(40,38),(38,38),(38,34),(37,34),(37,32),(36,32)], body)
result.rect(38,34,1,3,shine)
result.rect(25,35,1,4,body)
view(result)
finish(result)
