result = new_canvas(32,32,name='leather_spellbook')
c=result
ink='#211e2b'
dark='#49303a'
leather='#824637'
light='#b36a43'
metal='#9a794b'
gold='#e6bd70'
paper='#e4d4af'
shade='#aa967a'
# Back board and page block, in three-quarter perspective
c.poly([(5,7),(22,3),(27,6),(27,25),(10,29),(5,25)],ink)
c.poly([(8,10),(25,6),(25,24),(10,27),(8,25)],dark)
c.poly([(10,12),(25,8),(25,23),(10,27)],shade)
c.poly([(11,13),(24,9),(24,22),(11,25)],paper)
c.line(13,23,23,21,shade)
c.line(15,25,24,23,shade)
# Front leather cover
c.poly([(4,6),(21,2),(26,5),(26,21),(9,26),(4,23)],ink)
c.poly([(6,7),(21,4),(24,6),(24,20),(9,24),(6,22)],leather)
# Rounded spine
c.poly([(5,7),(8,8),(8,23),(5,22)],dark)
c.line(6,9,6,20,light)
c.line(8,8,8,23,ink)
# raised cover rim
c.line(9,7,21,4,light)
c.line(10,22,23,19,dark)
c.line(23,8,23,19,dark)
c.line(10,8,10,20,dark)
c.line(11,8,20,6,dark)
# metal corner plates
c.poly([(9,6),(13,5),(12,7),(9,9)],metal)
c.line(9,6,12,5,gold)
c.set(10,7,gold)
c.poly([(20,4),(24,5),(24,9),(22,8),(22,6)],metal)
c.line(21,4,24,5,gold)
c.set(23,6,gold)
c.poly([(9,20),(11,21),(13,22),(9,24)],metal)
c.line(9,22,11,22,gold)
c.poly([(21,19),(24,17),(24,20),(20,21)],metal)
c.line(22,20,24,19,gold)
# spine binding bands
c.line(5,10,7,11,metal)
c.line(5,11,7,12,gold)
c.line(5,19,7,20,metal)
c.line(5,20,7,21,gold)
# embossed arcane diamond
c.poly([(16,8),(20,12),(17,18),(13,14)],dark)
c.poly([(16,9),(19,12),(17,17),(14,14)],gold)
c.poly([(16,11),(18,12),(17,15),(15,14)],metal)
c.line(16,12,17,13,gold)
c.set(17,19,light)
# clasp along fore edge
c.poly([(22,12),(26,11),(27,12),(27,15),(23,16),(22,15)],ink)
c.poly([(23,13),(26,12),(26,14),(23,15)],metal)
c.line(23,13,25,12,gold)
c.set(24,14,dark)
view(result)
finish(result)
