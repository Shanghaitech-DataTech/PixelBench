result = new_canvas(32,32,name='leather_spellbook')
o='#211e2c'; dark='#482d36'; leather='#784438'; light='#ae6546'; gold='#c29554'; shine='#f0cf86'; page='#c4ad8b'; shadow='#81715f'
# thickness and bottom silhouette
result.poly([(5,7),(22,3),(27,6),(27,25),(10,29),(5,25)],o)
result.poly([(8,23),(24,20),(26,22),(26,25),(10,28),(8,26)],dark)
# parchment block visible on lower and right edges
result.poly([(10,23),(25,20),(25,24),(10,27),(8,25)],page)
result.line(11,25,24,22,shadow)
result.line(12,26,24,24,shadow)
result.line(25,9,25,21,shadow)
# closed upper leather cover
result.poly([(5,7),(22,3),(26,5),(26,21),(10,25),(5,22)],o)
result.poly([(9,8),(23,5),(24,6),(24,20),(10,23)],leather)
result.line(10,8,22,5,light)
result.line(10,9,10,21,light)
# spine rounded ridge
result.poly([(6,8),(8,8),(9,10),(9,23),(6,21)],dark)
result.line(6,9,6,20,leather)
result.line(8,10,8,21,light)
# inset tooling
result.line(12,10,21,8,dark)
result.line(21,8,21,18,dark)
result.line(12,21,21,19,dark)
result.line(12,11,12,20,dark)
# corner caps
result.poly([(9,7),(14,6),(14,7),(11,8),(11,11),(9,11)],gold)
result.line(10,7,13,6,shine)
result.poly([(20,5),(23,4),(25,5),(25,9),(23,9),(23,6),(20,7)],gold)
result.set(23,5,shine)
result.poly([(10,20),(11,20),(11,22),(14,22),(14,23),(10,24)],gold)
result.set(10,22,shine)
result.poly([(22,18),(24,18),(24,21),(20,22),(20,20),(22,20)],gold)
result.set(23,19,shine)
# spine bands
result.line(6,12,8,13,gold)
result.line(6,18,8,19,gold)
# embossed arcane diamond
result.poly([(17,10),(20,13),(17,18),(14,15)],dark)
result.poly([(17,11),(19,14),(17,17),(15,14)],gold)
result.line(17,12,17,15,shine)
result.set(17,14,leather)
# metal side clasp
result.rect(23,12,4,4,o)
result.rect(23,13,4,2,gold)
result.set(24,13,shine)
result.set(25,14,shadow)
view(result)
finish(result)
