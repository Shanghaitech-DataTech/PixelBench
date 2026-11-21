result = new_canvas(32,32,name='factory')
c=result
ink='#222a35'
shadow='#343c46'
brick='#a45e4b'
lightbrick='#c77a59'
darkbrick='#75483f'
mortar='#633e39'
roof='#667778'
rim='#a1ada0'
# compact isometric foundation
c.poly([(3,16),(21,12),(29,17),(29,26),(11,30),(2,25)],ink)
c.poly([(3,24),(11,27),(28,23),(28,26),(11,29),(3,25)],shadow)
c.line(11,28,27,25,'#566069')
# brick building walls
c.poly([(3,15),(11,19),(11,27),(3,23)],brick)
c.poly([(11,19),(28,15),(28,24),(11,28)],darkbrick)
c.poly([(12,20),(27,16),(27,24),(12,27)],brick)
# left wall mortar courses
c.line(3,18,10,21,mortar)
c.line(3,21,10,24,mortar)
c.line(5,17,5,18,darkbrick)
c.line(8,20,8,22,darkbrick)
c.line(5,22,5,24,darkbrick)
c.set(4,19,lightbrick)
c.line(7,23,9,24,lightbrick)
# broad wall brick courses
for x,y in [(12,22),(18,21),(24,19),(12,25),(18,24),(24,22)]:
    c.line(x,y,min(x+4,27),y-1,mortar)
    c.set(x+2,y-1,lightbrick)
c.line(17,20,17,21,darkbrick)
c.line(23,18,23,19,darkbrick)
c.line(14,23,14,24,darkbrick)
c.line(25,23,25,24,darkbrick)
# loading shutter
c.poly([(17,22),(23,20),(23,25),(17,27)],ink)
c.poly([(18,22),(22,21),(22,25),(18,26)],'#596669')
c.line(18,23,22,22,'#89958b')
c.line(18,25,22,24,'#394850')
c.set(21,24,'#c0b57b')
# front small ventilation grille
c.poly([(4,18),(8,20),(8,23),(4,21)],ink)
c.line(5,19,7,20,'#95a7a3')
c.line(5,21,7,22,'#52666c')
# flat slab roof, outline and elevated coping
c.poly([(2,13),(20,9),(29,13),(29,16),(11,20),(2,16)],ink)
c.poly([(3,14),(11,18),(28,14),(28,16),(11,19),(3,16)],'#526267')
c.poly([(2,13),(20,9),(29,13),(11,18)],rim)
c.poly([(5,13),(20,10),(26,13),(11,16)],roof)
c.line(4,14,11,17,'#c0c7ad')
c.line(11,17,27,13,'#899b92')
# rooftop box vent
c.poly([(18,11),(22,10),(25,12),(25,14),(21,15),(18,13)],ink)
c.poly([(19,11),(22,11),(24,12),(21,13)],'#a5b4ae')
c.line(21,14,24,13,'#54686c')
c.set(20,12,'#55676b')
c.set(22,12,'#55676b')
# tall square brick chimney, deliberately rising above roof
c.poly([(7,4),(12,3),(16,5),(16,13),(11,15),(7,13)],ink)
c.poly([(8,5),(11,7),(11,14),(8,12)],lightbrick)
c.poly([(12,7),(15,6),(15,13),(12,14)],brick)
c.line(8,8,10,9,mortar)
c.line(8,11,10,12,mortar)
c.line(12,10,15,9,mortar)
c.line(12,13,15,12,mortar)
c.set(13,7,lightbrick)
c.set(14,11,darkbrick)
c.set(9,6,'#e39b6b')
# broad cap and dark open flue
c.poly([(6,4),(12,2),(17,4),(17,6),(11,8),(6,6)],ink)
c.poly([(7,4),(12,3),(16,4),(11,6)],'#b6b5a0')
c.poly([(9,4),(12,4),(14,4),(11,5)],'#343c46')
c.line(7,5,11,7,'#d0c4a5')
c.line(12,7,16,5,'#788a85')
view(result,scale=10)
finish(result)
