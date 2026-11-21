result = new_canvas(32,32,name='farm_chicken')
c=result
outline='#735346'
cream='#f1dfad'
light='#fff0c9'
shade='#d9bc86'
dark='#b99468'
red='#b85b50'
# little ochre feet
c.line(13,24,13,28,outline)
c.line(22,24,22,28,outline)
c.line(10,29,14,29,outline)
c.line(19,29,24,29,outline)
c.line(13,26,13,28,'#d49b51')
c.line(22,26,22,28,'#d49b51')
c.line(11,28,14,28,'#d49b51')
c.line(20,28,23,28,'#d49b51')
# tail and full rounded silhouette
c.poly([(8,12),(5,9),(3,9),(3,12),(2,12),(3,16),(4,19),(6,21),(7,23),(10,25),(16,26),(22,25),(26,22),(28,17),(28,11),(26,8),(22,7),(19,9),(17,12),(13,11)],outline)
c.poly([(8,14),(5,11),(4,11),(5,16),(4,16),(6,20),(8,22),(11,24),(17,25),(22,24),(25,21),(27,17),(27,11),(25,9),(22,8),(20,10),(18,14),(13,12),(10,13)],cream)
# underside shading
c.poly([(6,19),(10,22),(16,23),(22,22),(26,19),(25,22),(22,24),(17,25),(11,24),(8,22)],shade)
c.line(12,24,18,24,dark)
# back and head light
c.poly([(8,15),(10,13),(14,13),(17,14),(19,13),(20,10),(23,9),(25,10),(26,12),(24,14),(21,15),(19,18),(14,17)],light)
c.line(5,12,7,15,light)
# comb, three round lobes
c.poly([(20,8),(19,6),(19,4),(21,4),(22,6),(22,3),(24,3),(25,6),(26,5),(27,6),(27,9),(24,9)],outline)
c.poly([(20,7),(20,5),(21,6),(22,7),(23,4),(24,4),(24,7),(26,6),(26,8),(23,8)],red)
c.set(23,4,'#de8870')
c.set(20,5,'#de8870')
# hanging wattle
c.rect(25,15,3,4,outline)
c.rect(25,15,2,3,red)
c.set(25,15,'#de8870')
# golden beak
c.poly([(27,12),(29,12),(31,14),(29,16),(27,16)],outline)
c.poly([(28,13),(29,13),(30,14),(28,15)],'#dba252')
c.line(28,13,29,13,'#f2c675')
# eye and cheek
c.rect(24,11,2,2,'#493e38')
c.set(24,11,'#fff4d5')
c.set(25,14,'#e4b58a')
# softly scalloped wing
c.path('M 10 16 Q 13 14 17 16 Q 20 18 18 21 L 16 22 L 13 22 L 10 20 Z',dark)
c.path('M 10 16 Q 14 15 17 17 L 18 19 L 16 21 L 13 21 L 10 19 Z',shade)
c.line(11,16,14,16,cream)
c.line(11,17,12,18,cream)
c.set(14,19,cream)
c.set(16,20,cream)
view(result)
finish(result)
