result = new_canvas(32,32,name='factory')
c=result
ink='#202632'
shadow='#383b48'
brick='#a65949'
light='#cb7c59'
mortar='#713e3d'
# foundation and building mass
c.poly([(3,15),(22,11),(29,15),(29,27),(10,30),(3,26)],ink)
c.poly([(4,17),(10,20),(10,28),(4,25)],'#88463f')
c.poly([(11,20),(28,16),(28,26),(11,29)],brick)
# brick courses across broad wall
for y in [21,24,27]:
    c.line(11,y,27,y-3,mortar)
for x,y in [(14,20),(22,18),(18,22),(25,21),(14,26),(22,25)]:
    c.line(x,y,x,y+1,mortar)
c.line(4,21,9,23,mortar)
c.line(4,24,9,26,mortar)
c.line(6,19,6,21,mortar)
c.line(8,24,8,25,mortar)
# roof parapet, flat top plane
c.poly([(3,14),(22,10),(29,14),(29,17),(10,21),(3,17)],ink)
c.poly([(4,14),(22,11),(27,14),(10,18)],'#a0aaa8')
c.poly([(5,14),(21,12),(25,14),(10,17)],'#65757b')
c.line(4,16,10,19,'#66777b')
c.line(11,19,28,15,'#c4c6ae')
c.line(11,20,28,16,'#65757b')
# chimney rising at rear left
c.rect(7,4,5,10,ink)
c.rect(8,5,3,9,brick)
c.line(8,5,8,13,light)
c.line(9,7,10,7,mortar)
c.line(8,10,10,10,mortar)
c.rect(6,3,7,3,ink)
c.rect(7,3,5,1,'#db9d70')
c.rect(7,4,4,1,'#713e3d')
# rooftop ventilator
c.poly([(17,10),(21,9),(24,11),(24,14),(19,15),(17,13)],ink)
c.poly([(18,10),(21,10),(23,11),(19,12)],'#c4c6ae')
c.rect(19,12,4,2,'#87999a')
c.line(20,12,20,13,shadow)
c.line(22,12,22,13,shadow)
# small roof exhaust
c.rect(12,12,3,3,ink)
c.rect(12,11,3,2,'#a0aaa8')
c.set(13,11,'#d8d4b9')
# main loading shutter
c.poly([(17,21),(24,19),(24,27),(17,29)],ink)
c.poly([(18,22),(23,21),(23,26),(18,27)],'#66777b')
for y in [23,25]:
    c.line(18,y,23,y-1,'#3e4c58')
c.line(18,22,23,21,'#9aa9a5')
c.line(17,28,24,26,'#b5ada0')
# small lit side window
c.poly([(5,18),(8,19),(8,22),(5,21)],ink)
c.line(6,19,6,20,'#e6bc69')
# wall vent
c.rect(12,22,3,3,ink)
c.line(12,22,14,22,'#d29a6a')
c.line(12,24,14,24,'#839091')
# foundation highlights
c.line(4,26,9,28,'#62626a')
c.line(11,29,16,28,'#838381')
view(result)
finish(result)
