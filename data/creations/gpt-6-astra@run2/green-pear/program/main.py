result = new_canvas(32, 32, name='green_pear')
# Seven opaque colors; the surrounding canvas stays transparent.
ink = '#30452b'
shadow = '#4e742e'
base = '#7fa83a'
light = '#afce50'
glint = '#e0e989'
wood = '#805335'
woodlight = '#b58a50'
# Stem bends gently to the right.
result.poly([(15,9),(15,5),(17,2),(19,2),(19,4),(17,6),(17,10)], ink)
result.line(16,7,17,4,wood)
result.set(18,3,woodlight)
# A pointed leaf growing to the left.
result.poly([(16,6),(13,3),(9,3),(10,6),(13,7),(16,7)], ink)
result.poly([(14,5),(11,4),(12,6),(15,6)], shadow)
result.line(11,4,14,5,light)
# Pear silhouette: narrow shoulder and a heavy rounded base.
result.poly([(14,8),(18,8),(20,10),(20,13),(22,17),(25,21),(26,24),(25,27),(22,29),(11,29),(8,28),(6,25),(6,22),(8,18),(11,14),(12,10)], ink)
result.poly([(14,9),(18,9),(19,11),(19,14),(21,18),(24,21),(25,24),(24,26),(21,28),(11,28),(8,26),(7,24),(7,22),(9,18),(12,14),(13,11)], shadow)
result.poly([(14,9),(17,9),(18,11),(18,14),(20,18),(22,21),(23,24),(21,26),(18,27),(11,27),(8,25),(8,22),(10,18),(13,14),(13,11)], base)
result.poly([(14,10),(16,10),(17,12),(16,15),(18,18),(20,21),(20,23),(18,25),(12,25),(10,24),(10,21),(12,18),(14,14)], light)
# Deliberately stepped highlight cluster.
result.rect(14,11,2,3,glint)
result.line(13,15,12,17,glint)
result.poly([(12,19),(13,19),(12,22),(11,23),(11,21)],glint)
# Sparse skin speckles, with no extra colors.
for x,y in [(16,20),(18,23),(14,24),(20,19),(10,25)]:
    result.set(x,y,base)
for x,y in [(21,24),(18,26),(23,23),(10,20)]:
    result.set(x,y,light)
result.line(15,28,17,28,ink)
view(result, scale=12)
finish(result)
