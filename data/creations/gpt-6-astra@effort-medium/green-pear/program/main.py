result = new_canvas(32,32)
outline='#29482c'
shadow='#4f782f'
mid='#7fa83b'
light='#aed34b'
high='#d9e77a'
brown='#735037'
stemlight='#ac8050'
# Bent woody stem
result.poly([(15,9),(15,5),(17,2),(19,2),(18,5),(17,9)],brown)
result.line(17,3,16,6,stemlight)
# Leaf silhouette and folded faces
result.poly([(16,6),(12,2),(8,2),(9,6),(12,8),(16,8)],outline)
result.poly([(10,3),(13,4),(15,6),(12,6)],mid)
result.line(10,3,14,6,light)
# Pear's taper and rounded base
result.poly([(14,7),(18,7),(20,9),(21,14),(23,17),(25,20),(26,23),(26,26),(24,29),(21,30),(11,30),(7,28),(5,25),(5,22),(7,18),(10,15),(11,10)],outline)
result.poly([(14,8),(18,8),(19,10),(20,15),(22,18),(24,21),(25,24),(24,27),(21,29),(11,29),(8,27),(6,24),(7,21),(9,18),(12,14),(12,11)],shadow)
result.poly([(14,8),(17,8),(19,11),(19,15),(22,19),(23,22),(23,25),(21,27),(17,28),(11,27),(8,25),(7,22),(9,19),(12,15),(13,10)],mid)
result.poly([(14,9),(17,9),(18,11),(18,16),(20,20),(20,23),(17,26),(12,26),(9,24),(9,21),(12,17),(14,13)],light)
result.poly([(14,11),(16,10),(16,14),(14,17),(13,17),(13,14)],high)
result.line(10,21,10,23,high)
result.set(11,20,high)
# Sparse skin flecks and bottom dimple
result.set(17,22,mid)
result.set(14,25,mid)
result.set(21,21,light)
result.set(19,18,mid)
result.line(15,28,17,28,shadow)
result.set(16,29,outline)
view(result)
finish(result)
