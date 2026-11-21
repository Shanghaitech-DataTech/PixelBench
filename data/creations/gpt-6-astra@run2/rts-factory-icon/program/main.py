result = new_canvas(32,32,name='factory')
c=result
ink='#202935'
shadow='#37404a'
brick='#ac6651'
lightbrick='#d28a64'
darkbrick='#774c48'
steel='#74868b'
bright='#a7b6ae'
# Foundation, three-quarter building footprint
c.poly([(3,17),(20,14),(29,18),(29,27),(12,30),(3,26)],ink)
c.poly([(4,24),(12,27),(28,24),(28,27),(12,29),(4,26)],shadow)
c.line(5,26,12,28,steel)
c.line(13,28,27,26,'#59676d')
# Brick front and shaded right wall
c.poly([(4,17),(20,15),(20,25),(12,27),(4,24)],brick)
c.poly([(20,15),(28,18),(28,25),(20,27)],darkbrick)
# Main front facade rectangular under roof
c.poly([(4,17),(21,18),(21,26),(12,28),(4,25)],brick)
# Brick courses in lit wall
c.line(4,20,20,20,darkbrick)
c.line(4,23,20,23,darkbrick)
c.line(6,26,12,28,darkbrick)
for x,y in [(7,18),(14,18),(10,21),(18,21),(6,24),(15,24)]:
    c.line(x,y,x,y+1,darkbrick)
for x,y in [(5,19),(11,19),(16,22),(8,25)]: c.line(x,y,x+2,y,lightbrick)
c.line(23,20,27,21,'#543e41')
c.line(22,24,27,25,'#543e41')
c.set(25,22,'#543e41')
# Flat roof: thick dark coping and clean planar surface
c.poly([(3,15),(20,12),(29,16),(29,19),(12,22),(3,18)],ink)
c.poly([(4,15),(20,13),(27,16),(12,19)],steel)
c.poly([(5,15),(20,14),(25,16),(12,18)],'#596b75')
c.line(3,15,12,19,bright)
c.line(12,19,28,16,bright)
c.line(12,20,28,17,'#50616b')
# Tall masonry stack at back left
c.poly([(7,5),(12,4),(16,6),(16,15),(12,17),(7,15)],ink)
c.poly([(8,6),(12,6),(12,15),(8,14)],brick)
c.poly([(13,6),(15,6),(15,14),(13,15)],darkbrick)
c.line(8,9,12,9,darkbrick)
c.line(8,12,12,12,darkbrick)
c.set(10,7,lightbrick)
c.set(11,10,lightbrick)
c.set(9,13,lightbrick)
c.set(9,11,darkbrick)
# Chimney cap and dark opening
c.poly([(6,4),(12,3),(17,5),(17,7),(12,9),(6,6)],ink)
c.poly([(7,4),(12,4),(15,5),(12,6)],bright)
c.line(9,5,12,5,'#111e29')
c.line(7,6,12,8,lightbrick)
c.line(13,7,16,6,darkbrick)
# Rooftop ventilator with slatted face
c.poly([(18,12),(22,11),(25,12),(25,15),(20,16),(18,15)],ink)
c.poly([(19,12),(22,12),(24,13),(20,14)],bright)
c.line(20,15,24,14,shadow)
c.set(21,14,steel)
c.set(23,14,steel)
# Front loading door, inset frame
c.rect(11,22,8,6,ink)
c.rect(12,22,6,5,'#55676f')
c.line(12,23,17,23,steel)
c.line(12,25,17,25,steel)
c.line(12,27,18,27,bright)
# Small industrial window and wall vent
c.rect(5,21,4,3,ink)
c.line(6,21,8,21,'#d6c786')
c.set(6,22,'#90a7a0')
c.line(23,21,26,22,ink)
c.line(23,23,26,24,ink)
c.set(23,22,steel)
c.set(25,23,steel)
view(c,scale=12)
finish(result)
