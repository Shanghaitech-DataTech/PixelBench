result = new_canvas(32, 32, name='green_pear')
# Seven opaque colours; the surrounding canvas stays transparent.
ink = '#30432c'
shade = '#527b32'
green = '#80ad3c'
light = '#b1d452'
glow = '#deea8b'
wood = '#795236'
woodlight = '#b28a50'
# Curved stem and a pointed leaf.
result.poly([(15,10),(15,6),(17,2),(19,2),(18,5),(17,10)], ink)
result.line(16,7,18,3,wood)
result.set(18,2,woodlight)
result.poly([(17,6),(19,3),(23,3),(25,2),(24,5),(21,7),(18,7)],ink)
result.poly([(18,6),(21,4),(24,3),(22,6),(19,6)],shade)
result.line(19,5,22,4,light)
# Continuous stepped silhouette: narrow neck and broad, rounded base.
result.poly([(13,8),(17,8),(19,10),(19,13),(21,16),(24,20),(25,23),(25,26),(23,29),(20,30),(11,30),(7,28),(5,25),(5,22),(7,18),(10,14),(11,10)],ink)
result.poly([(13,9),(16,9),(18,11),(18,14),(20,17),(23,21),(24,24),(23,27),(20,29),(11,29),(8,27),(6,24),(7,21),(9,17),(12,13),(12,11)],shade)
result.poly([(13,9),(16,9),(17,11),(17,14),(19,18),(21,21),(22,24),(21,27),(18,28),(11,28),(8,26),(7,23),(8,20),(10,17),(12,14),(12,11)],green)
result.poly([(13,10),(15,10),(16,12),(15,15),(16,18),(18,21),(18,24),(16,26),(11,26),(9,24),(9,21),(11,17),(13,14)],light)
result.poly([(13,12),(14,12),(14,15),(12,18),(11,20),(10,20),(11,17),(13,14)],glow)
result.line(9,22,9,23,glow)
# Sparse fruit texture and reflected light, kept in deliberate pixel clusters.
result.set(19,23,light)
result.set(17,27,light)
result.set(20,20,shade)
result.set(22,24,green)
result.set(12,27,green)
result.set(15,22,green)
result.line(14,29,17,29,ink)
result.set(15,28,shade)
view(result)
finish(result)
