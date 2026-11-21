result = new_canvas(32, 32, name='leather_spellbook')
c = result
ink = '#211c2b'
shadow = '#493044'
leather = '#7c4143'
light = '#b06450'
goldshade = '#94704e'
gold = '#d4a85e'
shine = '#f4d992'
paper = '#c1b5a0'
# Closed book, offset boards and the page block at the bottom.
c.poly([(5,7),(21,3),(26,6),(28,24),(25,28),(10,30),(5,26)],ink)
c.poly([(8,10),(24,7),(26,24),(23,27),(10,29),(7,25)],shadow)
c.poly([(10,24),(25,21),(26,24),(23,26),(10,28)],paper)
c.line(12,26,24,23,goldshade)
c.line(12,28,23,26,shadow)
# Lower leather board.
c.line(10,29,25,26,leather)
c.line(25,26,27,24,leather)
# Spine has a rounded silhouette and raised bands.
c.poly([(4,7),(7,5),(10,7),(12,25),(10,28),(6,26),(4,22)],ink)
c.poly([(5,8),(7,7),(9,8),(11,24),(9,26),(7,25),(5,21)],shadow)
c.line(6,9,8,21,leather)
c.line(5,10,9,12,goldshade)
c.line(5,11,9,13,gold)
c.line(7,21,10,22,goldshade)
c.line(7,22,10,23,gold)
# Top cover, angled slightly to show the spine and closed pages.
c.poly([(8,6),(23,3),(25,5),(28,22),(26,24),(11,27),(8,24),(6,9)],ink)
c.poly([(9,7),(23,4),(24,6),(27,22),(25,23),(11,26),(9,23),(7,9)],leather)
c.poly([(10,8),(22,6),(25,21),(12,24)],shadow)
c.poly([(11,9),(21,7),(24,20),(13,23)],leather)
c.line(9,8,11,22,light)
c.line(11,7,21,5,light)
c.line(13,24,24,22,light)
# Gilt corner protectors, each following the board perspective.
c.poly([(8,7),(12,6),(12,8),(10,9),(10,12),(8,11)],goldshade)
c.line(8,7,11,6,shine)
c.line(8,8,9,11,gold)
c.poly([(20,4),(23,4),(24,6),(24,9),(22,8),(22,6),(20,6)],gold)
c.line(21,4,23,4,shine)
c.set(23,5,shine)
c.poly([(10,21),(12,22),(12,24),(15,24),(15,25),(11,26)],goldshade)
c.line(11,23,11,25,gold)
c.line(12,25,14,25,shine)
c.poly([(24,19),(26,18),(27,22),(25,23),(22,24),(22,22),(25,21)],gold)
c.line(25,22,26,21,shine)
# Central embossed diamond and small magical jewel-like rune.
c.poly([(16,11),(21,15),(18,21),(13,16)],ink)
c.poly([(16,12),(20,15),(18,20),(14,16)],goldshade)
c.poly([(16,13),(19,15),(18,18),(15,16)],gold)
c.line(16,13,15,15,shine)
c.poly([(17,14),(18,16),(17,18),(16,16)],shadow)
c.set(17,15,shine)
# A leather fastening tab and its small metal clasp on the fore-edge.
c.poly([(23,12),(27,11),(28,15),(24,16)],ink)
c.poly([(24,13),(26,12),(27,14),(24,15)],shadow)
c.line(25,13,26,13,gold)
c.set(26,14,shine)
view(result)
finish(result)
