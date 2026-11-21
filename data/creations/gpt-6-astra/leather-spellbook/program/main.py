result = new_canvas(32, 32, name='leather_spellbook')
c=result
ink='#241e2b'
shade='#57313b'
leather='#884738'
light='#b56c45'
metalshade='#97703e'
gold='#d6aa5b'
shine='#f4d995'
pages='#b6a18a'
# Lower cover and exposed page block.
c.poly([(3,21),(7,19),(26,23),(25,28),(23,29),(4,26),(2,24)],ink)
c.poly([(4,23),(24,26),(23,28),(4,25)],shade)
c.line(5,25,23,28,leather)
c.poly([(6,20),(25,23),(24,26),(5,23)],pages)
c.line(7,22,23,25,shine)
c.line(9,24,22,26,metalshade)
# Rounded leather spine, tucked below the front cover.
c.poly([(7,3),(10,3),(7,21),(5,25),(3,24),(3,8),(4,5)],ink)
c.poly([(6,5),(8,4),(6,20),(4,23),(4,8)],shade)
c.line(5,8,4,19,leather)
# Front board, dark bevel, and warm leather field.
c.poly([(8,2),(28,6),(25,25),(5,21),(6,6)],ink)
c.poly([(9,3),(27,6),(24,24),(6,20),(7,7)],shade)
c.poly([(10,4),(26,7),(23,22),(7,19),(8,7)],leather)
c.line(10,4,25,7,light)
c.line(8,8,7,18,light)
# Inset tooling on the leather.
c.poly([(11,7),(24,9),(22,20),(9,18)],shade,fill=False)
c.line(12,8,22,10,light)
c.line(10,17,20,19,light)
# Reinforced spine bands.
c.line(4,9,6,10,metalshade)
c.line(4,8,6,9,gold)
c.line(4,19,5,20,gold)
c.set(4,20,metalshade)
# Four fitted brass corner plates, with folded edges.
c.poly([(8,3),(13,4),(12,6),(10,6),(9,9),(7,8)],metalshade)
c.line(8,3,12,4,shine)
c.poly([(8,4),(11,5),(9,6),(8,8)],gold)
c.set(9,5,shine)
c.poly([(23,5),(27,6),(27,11),(25,10),(25,8),(22,7)],metalshade)
c.line(24,6,27,6,shine)
c.line(26,7,26,10,gold)
c.set(25,7,gold)
c.poly([(6,16),(8,17),(8,19),(11,20),(10,22),(6,21)],metalshade)
c.line(6,17,6,20,gold)
c.line(7,20,10,21,gold)
c.set(7,19,shine)
c.poly([(22,20),(25,19),(25,24),(20,23),(20,21)],metalshade)
c.line(24,20,24,23,gold)
c.line(21,22,23,23,gold)
c.set(24,21,shine)
# Central embossed arcane seal.
c.poly([(17,9),(21,14),(16,18),(12,13)],ink)
c.poly([(17,10),(20,14),(16,17),(13,13)],metalshade)
c.line(17,10,13,13,gold)
c.line(13,13,16,16,gold)
c.line(17,11,19,14,shine)
c.line(19,14,16,16,gold)
c.poly([(17,12),(18,14),(16,15),(15,13)],shade)
c.set(17,12,shine)
c.set(16,13,gold)
c.set(16,14,gold)
# Restrained leather wear.
c.set(11,10,light)
c.line(12,19,14,19,light)
view(result)
save('leather_spellbook',result)
finish(result)
