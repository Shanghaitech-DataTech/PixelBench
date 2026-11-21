# 32px RTS factory, drawn as a single transparent sprite.
result = new_canvas(32, 32, name="factory")
c = result
P = {
 'outline':'#202832', 'shadow':'#303944', 'base':'#424b53',
 'brickDark':'#643f3e', 'brickSide':'#815047', 'brick':'#ac6752',
 'brickLight':'#cb8462', 'brickHi':'#e0a177', 'mortar':'#854f44',
 'roofDark':'#4c5c66', 'roof':'#71828a', 'roofLight':'#92a1a5',
 'rim':'#b7b8ac', 'rimShade':'#788b90', 'metalDark':'#364a55',
 'metal':'#607781', 'metalLight':'#8ca4aa', 'glass':'#6cabb4',
 'glassHi':'#b3d4cf', 'amber':'#efbc6b'
}
for name, value in P.items(): c.color(value, name)
# Low foundation makes the icon sit firmly on a terrain tile.
c.poly([(2,26),(8,21),(29,22),(30,25),(24,30),(3,30),(2,29)], 'outline')
c.rect(3,27,21,2,'base')
c.line(24,28,29,23,'base')
c.line(4,29,22,29,'shadow')
# Masonry block: broad front face and shaded right return.
c.poly([(3,14),(23,14),(29,9),(29,24),(23,29),(3,29)], 'outline')
c.rect(4,16,19,12,'brick')
c.poly([(24,15),(28,11),(28,23),(24,27)], 'brickSide')
c.line(23,16,23,28,'brickDark')
c.line(4,27,22,27,'brickDark')
# Horizontal mortar and staggered brick highlights.
for y in [18,22,26]:
    c.line(4,y,22,y,'mortar')
for x,y in [(8,17),(16,17),(12,19),(20,19),(7,21),(16,21),(11,23),(19,23),(7,25),(16,25)]:
    c.line(x,y,x,y+1,'mortar')
for x,y,w in [(5,17,3),(10,17,5),(18,17,4),(4,23,3),(9,23,3),(4,25,2),(9,25,3)]:
    c.rect(x,y,w,1,'brickLight')
c.line(4,17,4,26,'brickLight')
# Side wall courses follow the perspective.
for y in [17,21,25]:
    c.line(24,y,28,y-4,'brickDark')
c.set(26,16,'brickLight')
c.set(27,20,'brick')
c.set(25,24,'brick')
# Flat roof, with a continuous raised parapet and an inset surface.
c.poly([(2,14),(8,8),(29,8),(30,9),(30,11),(24,17),(2,17)], 'outline')
c.poly([(4,14),(9,9),(28,9),(23,14)], 'roofLight')
c.poly([(6,13),(10,10),(27,10),(23,14)], 'roof')
c.line(8,13,22,13,'roofDark')
c.line(11,10,26,10,'roofLight')
c.rect(3,15,20,1,'rim')
c.line(24,15,29,10,'rimShade')
c.rect(3,16,20,1,'roofDark')
c.line(24,16,29,11,'roofDark')
# Loading bay: deep frame, steel roller door, and a bright latch.
c.rect(13,19,9,9,'outline')
c.rect(14,20,7,7,'metal')
c.line(14,20,20,20,'metalLight')
for y in [22,24,26]:
    c.line(14,y,20,y,'metalDark')
c.rect(13,18,9,1,'brickHi')
c.rect(16,25,3,1,'rim')
c.line(13,28,22,28,'rimShade')
# Two joined factory windows in a dark inset frame.
c.rect(5,19,7,4,'outline')
c.rect(6,20,2,2,'glass')
c.rect(9,20,2,2,'glass')
c.set(6,20,'glassHi')
c.set(9,20,'glassHi')
c.line(5,23,11,23,'brickHi')
# Front wall ventilation grille.
c.rect(6,25,5,2,'brickDark')
c.line(7,25,10,25,'metalDark')
c.line(7,26,10,26,'metalLight')
# A recessed vent on the side face.
c.poly([(25,18),(27,16),(27,21),(25,23)],'outline')
c.line(25,19,27,17,'metal')
c.line(25,21,27,19,'metal')
# Rooftop machinery, seated on a dark plinth.
c.poly([(16,12),(18,10),(23,10),(23,13),(21,15),(16,15)], 'roofDark')
c.poly([(16,10),(18,8),(22,8),(22,12),(20,14),(16,14)], 'outline')
c.poly([(17,10),(18,9),(21,9),(20,10)], 'metalLight')
c.rect(17,11,3,2,'metal')
c.line(21,10,21,12,'metalDark')
c.line(17,11,19,11,'outline')
c.line(17,13,19,13,'rimShade')
# Tall brick chimney, including a metal flashing at its foot.
c.poly([(6,12),(8,10),(13,10),(14,12),(12,14),(6,14)], 'roofDark')
c.rect(7,4,6,9,'outline')
c.rect(8,4,3,8,'brickLight')
c.rect(11,4,1,8,'brickSide')
for y in [6,9]:
    c.line(8,y,10,y,'mortar')
    c.set(11,y,'brickDark')
c.set(9,5,'brickHi')
c.set(9,8,'brickHi')
c.set(8,11,'brickHi')
c.line(11,11,11,12,'brickDark')
# Broad coping and open flue make the stack recognizable at native scale.
c.rect(6,2,8,3,'outline')
c.line(7,2,12,2,'rim')
c.line(7,4,12,4,'brickHi')
c.line(8,3,11,3,'shadow')
c.set(13,3,'brickSide')
view(result, scale=12, margin=0)
save('rts-factory-icon', result)
finish(result)
