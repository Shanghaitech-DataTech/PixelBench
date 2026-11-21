# Bamboo steamer, hand placed at native 32 x 32 resolution.
result = new_canvas(32, 32, name='bamboo_steamer')
c = result
ink = '#62422f'
shade = '#946034'
bamboo = '#c58c49'
gold = '#e4b667'
light = '#f6d38c'
inner = '#795234'
fold = '#c8a77b'
dough = '#f5e3ba'
cream = '#fff4d6'

# A low, round bamboo basket.
c.ellipse(16, 24, 13, 5, ink)
c.rect(3, 19, 27, 6, ink)
c.ellipse(16, 24, 12, 4, bamboo)
c.rect(4, 19, 25, 6, bamboo)
c.poly([(4,22),(7,24),(12,25),(25,24),(28,22),(28,26),(25,28),(9,28),(5,26)], bamboo)
c.poly([(24,23),(28,21),(28,25),(26,27),(23,28),(23,25)], shade)
# Slender vertical stave joints, with sunlit edges.
for x, y0, y1 in [(6,23,26),(10,24,27),(15,25,27),(20,25,27),(25,23,26)]:
    c.line(x,y0,x,y1,shade)
    c.line(x+1,y0,x+1,y1,gold)
c.line(8,28,23,28,shade)
c.line(10,27,21,27,gold)
c.set(5,25,gold)
c.set(27,25,bamboo)

# Back rim and the shaded hollow of the open steamer.
c.ellipse(16, 19, 13, 5, ink)
c.ellipse(16, 19, 12, 4, gold)
c.ellipse(16, 19, 10, 3, inner)
c.line(10,16,22,16,shade)
c.line(8,16,13,15,light)
c.line(24,17,26,18,light)

# Raised lid: the lower edge adds thickness beneath a sloping woven face.
c.poly([(2,7),(4,5),(8,5),(16,7),(22,10),(25,13),(24,15),(20,15),(12,13),(5,11),(2,9)], ink)
c.poly([(3,8),(8,7),(17,10),(24,13),(23,14),(20,14),(12,12),(5,10)], shade)
c.line(5,10,12,12,bamboo)
c.line(12,12,20,14,bamboo)
c.poly([(2,6),(5,4),(9,4),(16,6),(21,8),(24,11),(23,13),(19,13),(11,11),(5,9),(2,8)], ink)
c.poly([(3,6),(6,5),(9,5),(16,7),(21,9),(23,11),(22,12),(19,12),(11,10),(5,8),(3,8)], gold)
c.poly([(5,6),(8,5),(14,7),(20,9),(22,11),(18,11),(11,9),(5,7)], bamboo)
# Woven diagonal bamboo strips.
c.line(6,6,19,10,light)
c.line(5,7,18,11,gold)
c.line(10,6,7,8,shade)
c.line(14,7,11,9,shade)
c.line(18,9,15,10,shade)
c.line(21,10,19,11,shade)
c.set(9,7,gold)
c.set(13,8,gold)
c.set(17,9,gold)
c.line(4,6,6,5,light)
c.line(5,9,11,11,gold)
c.line(12,11,19,13,gold)
# Small arched bamboo handle on top.
c.poly([(9,5),(9,3),(10,2),(12,2),(14,3),(14,6),(12,6)], ink)
c.line(10,3,12,3,light)
c.set(13,4,gold)
c.set(13,5,bamboo)
c.set(10,4,bamboo)
c.set(11,5,gold)

# The back dumpling, pinched at the crown with soft pleated sides.
c.poly([(15,13),(17,13),(18,14),(19,16),(20,17),(20,19),(18,21),(14,21),(12,19),(12,17),(14,14)], shade)
c.poly([(15,14),(17,14),(18,16),(19,17),(19,19),(17,20),(14,20),(13,18),(14,16)], dough)
c.poly([(15,14),(17,14),(18,16),(18,18),(14,18),(14,16)], cream)
c.line(15,15,14,17,fold)
c.line(17,15,18,18,fold)
c.set(16,14,light)
c.line(14,19,17,19,cream)

# Left dumpling.
c.poly([(8,16),(10,16),(11,17),(12,19),(13,20),(13,21),(11,23),(7,23),(5,21),(5,20),(6,18)], shade)
c.poly([(8,17),(10,17),(11,19),(12,20),(12,21),(10,22),(7,22),(6,21),(6,19)], dough)
c.poly([(8,17),(9,17),(11,20),(10,21),(7,21),(6,20),(7,18)], cream)
c.line(8,18,7,20,fold)
c.line(10,18,10,20,fold)
c.set(9,17,light)
c.set(11,21,fold)

# Right dumpling.
c.poly([(22,16),(24,16),(25,17),(26,19),(27,20),(27,21),(25,23),(21,23),(20,21),(20,19),(21,17)], shade)
c.poly([(22,17),(24,17),(25,19),(26,20),(26,21),(24,22),(22,22),(21,21),(21,19)], dough)
c.poly([(22,17),(23,17),(25,20),(24,21),(22,21),(21,20),(22,18)], cream)
c.line(22,18,22,20,fold)
c.line(24,18,25,20,fold)
c.set(23,17,light)
c.set(25,21,fold)

# Continuous front lip wraps in front of the dumplings.
c.path('M 3 19 L 3 21 L 5 23 L 9 24 L 14 25 L 20 25 L 25 24 L 28 22 L 29 20', ink, fill=False)
c.path('M 4 20 L 5 22 L 9 23 L 14 24 L 20 24 L 25 23 L 27 22 L 28 20', gold, fill=False)
c.path('M 6 22 L 10 23 L 15 23 L 20 23 L 24 22', light, fill=False)
c.set(28,19,light)
c.set(4,19,light)

# Two small, airy wisps of steam against transparency.
c.line(26,11,26,10,'#cedbd8')
c.line(26,9,27,8,'#e8eeDF')
c.line(27,7,26,6,'#e8eedf')
c.set(26,5,'#cedbd8')
c.set(27,4,'#e8eedf')
c.set(22,5,'#cedbd8')
c.line(22,4,23,3,'#e8eedf')
c.set(23,2,'#cedbd8')

view(result, scale=12, margin=0)
save('bamboo_steamer', result)
finish(result)
