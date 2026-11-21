# Four elemental skills, drawn on a shared pixel grid.
INK = '#191c33'
DEEP = '#343047'

def shape(c, points, color, edge=INK):
    c.poly(points, color)
    if edge:
        c.poly(points, edge, fill=False)

def sparkle(c, x, y, color, core):
    c.set(x,y-2,INK)
    c.line(x-1,y-1,x+1,y-1,INK)
    c.line(x-2,y,x+2,y,INK)
    c.line(x-1,y+1,x+1,y+1,INK)
    c.set(x,y+2,INK)
    c.set(x,y-1,color)
    c.line(x-1,y,x+1,y,color)
    c.set(x,y+1,color)
    c.set(x,y,core)

result = new_canvas(64,64,name='skill_icon_set')
fire = new_canvas(32,32,name='fireball')
ice = new_canvas(32,32,name='ice_shield')
heal = new_canvas(32,32,name='healing')
bolt = new_canvas(32,32,name='lightning')

# FIRE -- a flame-tailed orb travelling down and right.
red_dark='#8b304b'
red='#d7473d'
orange='#f77a35'
gold='#ffba48'
yellow='#ffe67a'
cream='#fff5cc'
shape(fire,[(3,3),(7,5),(10,9),(11,9),(11,4),(15,7),(18,12),(19,12),(18,8),(22,11),(24,16),(27,19),(29,23),(28,26),(25,29),(19,30),(15,28),(11,25),(9,21),(6,18),(6,14),(4,11),(4,7)],red_dark)
fire.poly([(4,5),(8,8),(11,13),(13,12),(12,7),(15,10),(17,15),(20,16),(20,12),(22,15),(23,18),(26,20),(27,23),(26,26),(23,28),(18,28),(14,25),(11,20),(8,18),(8,14),(5,10)],red)
fire.poly([(5,7),(8,10),(10,14),(13,17),(14,15),(14,11),(17,17),(21,18),(23,18),(26,21),(27,24),(25,27),(21,28),(17,26),(14,24),(12,20),(10,18),(9,14),(6,11)],orange)
fire.poly([(9,13),(12,16),(15,20),(17,19),(17,16),(20,20),(23,20),(25,22),(26,24),(24,26),(21,27),(18,25),(16,24),(14,20),(11,18)],gold)
fire.poly([(18,20),(21,21),(23,20),(25,23),(24,25),(22,26),(19,24),(18,22),(15,19)],yellow)
fire.poly([(20,21),(22,22),(23,21),(24,23),(23,25),(21,24)],cream)
fire.line(18,28,22,29,red)
fire.set(26,27,orange)
# Detached ember follows the flow.
shape(fire,[(5,21),(7,22),(7,24),(5,24),(4,22)],red)
fire.set(5,22,gold)
fire.set(24,10,red_dark)
fire.set(25,11,orange)

# ICE -- heavy bevelled rim, a blue faceted field and a snowflake seal.
navy='#254470'
blue='#286b9c'
cyan='#459fc5'
frost='#84d9e6'
light='#c6f5ee'
white='#f1fff4'
shape(ice,[(16,2),(21,5),(27,6),(27,14),(26,20),(23,24),(16,29),(9,24),(6,20),(5,14),(5,6),(11,5)],navy)
ice.poly([(16,4),(21,7),(25,8),(25,15),(24,20),(21,24),(16,27),(11,23),(8,19),(7,13),(7,8),(12,7)],frost)
ice.poly([(16,4),(21,7),(25,8),(24,11),(20,10),(16,8)],light)
ice.poly([(16,8),(20,10),(23,10),(23,16),(22,20),(19,23),(16,25),(12,22),(10,19),(9,14),(9,10),(12,10)],navy)
ice.poly([(16,9),(20,11),(22,11),(22,17),(20,20),(16,24),(16,20),(12,20),(10,16),(10,11),(13,11)],blue)
ice.poly([(16,9),(16,22),(12,19),(10,14),(10,11),(13,11)],cyan)
# A subdued diagonal facet under the emblem.
ice.poly([(18,10),(22,11),(22,13),(18,17),(16,17)],'#347fad')
ice.line(7,9,7,14,white)
ice.line(8,17,9,20,light)
ice.line(11,23,15,26,light)
ice.line(17,26,21,23,cyan)
ice.line(24,16,23,20,cyan)
ice.line(12,7,16,5,white)
# Six crystalline spokes and notched tips.
ice.line(16,11,16,21,light)
ice.line(12,13,20,19,light)
ice.line(12,19,20,13,light)
ice.line(15,11,17,11,light)
ice.line(15,21,17,21,frost)
ice.line(12,13,12,15,light)
ice.line(20,13,20,15,light)
ice.line(12,17,12,19,light)
ice.line(20,17,20,19,light)
ice.rect(15,15,3,3,white)
ice.set(16,14,white)
ice.set(16,18,white)
sparkle(ice,3,23,cyan,white)
sparkle(ice,29,4,frost,white)

# HEALING -- a luminous green cross framed by two new leaves.
green_dark='#215253'
green='#28836b'
emerald='#43bb80'
mint='#8be5a0'
pale='#d8ffd0'
shape(heal,[(12,4),(20,4),(20,10),(26,10),(26,18),(20,18),(20,24),(12,24),(12,18),(6,18),(6,10),(12,10)],green_dark)
heal.poly([(13,5),(19,5),(19,11),(25,11),(25,17),(19,17),(19,23),(13,23),(13,17),(7,17),(7,11),(13,11)],emerald)
heal.rect(14,6,4,16,mint)
heal.rect(8,12,16,4,mint)
heal.rect(14,6,4,3,pale)
heal.rect(8,12,4,2,pale)
heal.rect(14,12,4,4,pale)
heal.line(19,11,24,11,mint)
heal.line(24,15,24,16,green)
heal.line(19,17,19,22,green)
heal.line(13,22,18,22,green)
heal.line(7,17,12,17,green)
heal.set(19,5,mint)
# Curled botanical silhouettes beneath the cross.
shape(heal,[(3,20),(6,21),(10,23),(13,27),(15,29),(10,29),(6,27),(4,24)],green_dark)
heal.poly([(4,22),(8,23),(11,26),(12,28),(8,27),(5,24)],emerald)
heal.line(5,22,10,27,mint)
heal.set(11,28,green)
shape(heal,[(28,20),(27,25),(24,28),(19,29),(17,29),(20,25),(23,22)],green_dark)
heal.poly([(26,22),(25,25),(22,27),(19,28),(22,24)],emerald)
heal.line(26,22,20,27,mint)
sparkle(heal,5,5,mint,pale)
sparkle(heal,26,5,mint,pale)

# LIGHTNING -- a sharp gold zigzag, cream-hot on the upper-left edges.
bronze='#885045'
amber='#cc7935'
sun='#f5b83d'
lemon='#ffe67a'
shape(bolt,[(18,3),(27,3),(21,12),(27,12),(8,29),(11,20),(5,20)],bronze)
bolt.poly([(18,4),(25,4),(19,14),(24,14),(10,26),(14,18),(7,18)],sun)
bolt.poly([(18,4),(24,4),(17,15),(22,15),(12,24),(16,16),(9,17)],lemon)
bolt.poly([(18,4),(21,4),(14,15),(11,16)],cream)
bolt.line(18,16,21,15,cream)
bolt.line(11,24,15,19,lemon)
bolt.line(13,19,10,26,amber)
bolt.line(23,14,16,21,sun)
# Small broken discharges echo the main zigzag.
shape(bolt,[(6,4),(9,4),(7,8),(9,8),(4,13),(5,9),(3,9)],amber)
bolt.line(6,5,5,7,lemon)
bolt.line(5,9,6,9,sun)
shape(bolt,[(27,20),(29,20),(27,24),(29,24),(23,29),(25,25),(23,25)],amber)
bolt.line(27,21,26,23,lemon)
bolt.line(25,25,27,25,sun)
sparkle(bolt,21,28,sun,cream)

result.blit(fire,0,0)
result.blit(ice,32,0)
result.blit(heal,0,32)
result.blit(bolt,32,32)
view(result,scale=8,margin=0)
save('skill_icon_set',result)
finish(result)
