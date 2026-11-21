# 64px public transportation pictogram set
result = new_canvas(64, 64, '#0b1928', name='public_transport_icons')
c = result
bg = '#0b1928'
border = '#294558'
card = '#152d3e'
shadow = '#102333'
teal = '#6bd5c2'
light = '#c1f1dc'
cream = '#ffe3a0'
glass = '#244c5b'
# Identical stepped, rounded tile frames.
for x,y in [(2,2),(34,2),(2,34),(34,34)]:
    c.poly([(x+3,y),(x+24,y),(x+27,y+3),(x+27,y+24),(x+24,y+27),(x+3,y+27),(x,y+24),(x,y+3)],border)
    c.poly([(x+3,y+1),(x+24,y+1),(x+26,y+3),(x+26,y+24),(x+24,y+26),(x+3,y+26),(x+1,y+24),(x+1,y+3)],card)
# Bus: straight coach silhouette, mirrors, twin panes and separate tires.
c.rect(9,23,4,4,shadow)
c.rect(20,23,4,4,shadow)
c.rect(6,12,2,5,teal)
c.rect(25,12,2,5,teal)
c.poly([(10,7),(22,7),(24,9),(24,24),(9,24),(9,9)],teal)
c.rect(11,7,11,2,light)
c.rect(11,10,12,8,glass)
c.rect(16,10,2,8,teal)
c.rect(11,10,4,2,light)
c.rect(18,10,5,2,light)
c.rect(11,20,3,2,cream)
c.rect(20,20,3,2,cream)
c.rect(15,22,4,1,glass)
c.rect(10,24,3,3,light)
c.rect(21,24,3,3,light)
# Subway: arched car, single panoramic windshield and tracks.
c.poly([(41,27),(44,22),(52,22),(55,27),(52,27),(50,24),(46,24),(44,27)],glass)
c.rect(43,25,10,1,glass)
c.poly([(44,7),(52,7),(55,10),(55,21),(52,24),(44,24),(41,21),(41,10)],teal)
c.rect(45,7,7,2,light)
c.rect(46,9,4,1,glass)
c.poly([(44,11),(52,11),(53,12),(53,17),(43,17),(43,12)],glass)
c.rect(44,11,8,2,light)
c.rect(43,20,3,2,cream)
c.rect(50,20,3,2,cream)
c.rect(47,22,2,1,glass)
# Bicycle: two equal wheels with a two-pixel rim, geometric diamond frame.
for x in [9,23]:
    c.circle(x,52,4,teal)
    c.circle(x,52,2,card)
# Parallel offset strokes keep all the diagonals substantial at native scale.
def stroke(x0,y0,x1,y1,col):
    c.line(x0,y0,x1,y1,col)
    c.line(x0,y0+1,x1,y1+1,col)
stroke(9,51,14,44,light)
stroke(14,44,18,51,light)
stroke(9,51,18,51,light)
stroke(18,51,22,44,light)
stroke(14,44,22,44,light)
stroke(21,41,24,51,teal)
c.rect(19,40,5,2,cream)
c.rect(11,41,6,2,cream)
c.rect(13,43,2,2,teal)
c.rect(17,51,3,2,cream)
# Pedestrian: round head and clear, open walking pose.
c.circle(49,40,3,light)
# Connected angular limbs share the bicycle's two-pixel visual weight.
c.poly([(47,45),(50,45),(52,48),(56,48),(56,50),(51,50),(49,48),(48,51),(51,54),(53,57),(50,57),(47,53),(44,57),(41,57),(45,51)],teal)
c.poly([(47,45),(45,45),(42,48),(40,48),(40,50),(43,50),(47,47)],light)
c.rect(46,45,3,5,light)
view(result)
finish(result)
