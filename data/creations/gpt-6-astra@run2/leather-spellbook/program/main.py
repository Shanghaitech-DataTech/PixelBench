result = new_canvas(32, 32, name='leather_spellbook')
c=result
ink='#211d2b'
shadow='#4a2834'
leather='#804336'
light='#b66a43'
gold='#a77b47'
shine='#e7bc72'
pages='#e0cba1'
page_shadow='#9a856b'
# Bottom cover and page block, seen below the front cover.
c.poly([(5,7),(10,3),(26,6),(28,9),(28,25),(23,29),(6,26),(3,23),(3,10)],ink)
c.poly([(6,20),(25,22),(26,25),(23,27),(7,24)],page_shadow)
c.poly([(7,20),(25,22),(25,24),(22,26),(7,23)],pages)
c.line(9,23,22,25,page_shadow)
c.line(24,23,26,21,page_shadow)
c.poly([(4,22),(7,24),(23,27),(26,25),(27,25),(24,28),(6,25),(4,24)],shadow)
c.line(7,25,23,28,light)
# Main leather binding: diagonal top and right edges.
c.poly([(4,8),(9,3),(26,6),(27,8),(27,22),(23,26),(6,23),(3,21),(3,10)],ink)
c.poly([(7,8),(10,5),(25,8),(25,21),(22,24),(7,21)],leather)
# Dark rounded spine on left.
c.poly([(4,10),(6,8),(8,8),(7,21),(6,22),(4,20)],shadow)
c.line(5,10,5,19,leather)
c.line(8,9,8,20,light)
# Cover bevel and inset tooling.
c.line(10,5,24,8,light)
c.line(25,9,25,21,shadow)
c.line(23,22,22,24,shadow)
c.line(9,21,21,23,shadow)
c.poly([(11,8),(22,10),(22,20),(20,21),(11,19)],shadow,fill=False)
c.line(12,9,21,11,light)
c.line(12,10,12,17,light)
# Antique brass metal corners with warm specular edges.
c.poly([(8,5),(11,5),(11,7),(9,7),(8,9),(6,9),(6,7)],gold)
c.line(8,5,10,5,shine)
c.set(7,6,shine)
c.set(8,7,ink)
c.poly([(22,6),(26,7),(26,11),(24,11),(24,9),(22,9)],gold)
c.line(23,7,25,8,shine)
c.set(25,9,shine)
c.set(24,8,ink)
c.poly([(23,20),(26,20),(26,22),(23,25),(20,24),(20,22),(23,23)],gold)
c.line(24,21,25,21,shine)
c.line(22,24,24,22,shine)
c.set(23,23,ink)
c.poly([(7,19),(10,20),(10,22),(12,22),(12,24),(7,23),(6,21)],gold)
c.line(7,20,7,22,shine)
c.line(8,23,10,23,shine)
c.set(9,21,ink)
# Raised spine bands.
c.line(4,11,6,12,gold)
c.set(4,11,shine)
c.line(4,17,6,18,gold)
c.set(4,17,shine)
# Embossed arcane diamond seal, deliberately compact and legible.
c.poly([(17,10),(21,15),(17,20),(13,15)],ink)
c.poly([(17,11),(20,15),(17,19),(14,15)],gold)
c.line(17,11,14,15,shine)
c.line(14,15,17,18,shine)
c.poly([(17,13),(18,15),(17,17),(16,15)],shadow)
c.set(17,14,shine)
view(result)
finish(result)
