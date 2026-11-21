result = new_canvas(32, 32, name='green_pear')
# Seven-color palette: dark outline, wood, and five greens.
dark = '#293d25'
wood = '#80603b'
shade = '#467334'
mid = '#6b9e39'
base = '#95bd43'
light = '#c4db64'
glint = '#e5ed9a'
# Bent stem and a leaf sweeping to the right.
result.poly([(14,9),(14,5),(16,2),(18,2),(17,5),(16,9)], dark)
result.line(15,6,17,3,wood)
result.poly([(17,6),(19,3),(23,2),(26,3),(24,6),(20,7)],dark)
result.poly([(18,5),(21,3),(24,3),(22,5),(19,6)],mid)
result.line(19,5,23,3,light)
# Stepped pear silhouette, narrow shoulders and a generous round base.
result.poly([(13,7),(17,7),(19,9),(19,12),(21,15),(24,18),(26,22),(26,25),(24,28),(21,30),(10,30),(7,28),(5,25),(5,22),(6,19),(9,15),(11,12),(11,9)],dark)
result.poly([(13,8),(17,8),(18,10),(18,13),(20,16),(23,19),(25,22),(25,25),(23,27),(20,29),(11,29),(8,27),(6,24),(7,20),(10,16),(12,12),(12,10)],mid)
# Lower-right shadow follows the bulging fruit.
result.poly([(18,12),(20,16),(23,19),(25,22),(25,25),(23,27),(20,29),(11,29),(8,27),(16,28),(21,26),(23,23),(22,20),(19,17)],shade)
result.poly([(13,8),(16,8),(17,10),(17,14),(19,18),(21,21),(21,24),(19,26),(15,27),(10,26),(8,24),(8,21),(10,17),(12,13),(12,10)],base)
result.poly([(13,9),(15,9),(15,13),(13,17),(11,21),(11,24),(9,23),(9,20),(11,16),(13,12)],light)
result.line(13,11,13,13,glint)
result.line(10,19,10,21,glint)
# Sparse skin freckles and a tiny blossom scar.
result.set(16,22,light)
result.set(14,25,mid)
result.set(19,20,mid)
result.set(8,25,base)
result.set(21,25,mid)
result.line(14,28,16,28,dark)
result.set(15,27,shade)
view(result, scale=12)
finish(result)
