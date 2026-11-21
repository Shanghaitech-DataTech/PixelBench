import math

# Shared palette: midnight outlines, cool steel, antique gold, oiled leather.
C = {
    'ink':'#171d2c', 'edge':'#2c394e', 'steel_dark':'#45617b',
    'steel':'#7699b1', 'steel_light':'#bbd8df', 'glint':'#eff4e4',
    'gold_dark':'#744631', 'gold':'#b57b3c', 'gold_light':'#e7b95f',
    'gold_glint':'#ffe6a0', 'leather_dark':'#472e32', 'leather':'#835044',
    'leather_light':'#bc8060', 'teal_dark':'#254955', 'teal':'#327a80',
    'teal_light':'#58aaa3', 'gem_dark':'#793f42', 'gem':'#dc7759',
    'gem_light':'#ffc898'
}
result = new_canvas(64, 64, name='weapon_set')
def poly(points,col):
    result.poly(points,C.get(col,col))
def line(x0,y0,x1,y1,col):
    result.line(x0,y0,x1,y1,C.get(col,col))
def rect(x,y,w,h,col):
    result.rect(x,y,w,h,C.get(col,col))
def dot(x,y,col):
    result.set(x,y,C.get(col,col))

# SWORD -- upper left, rising on a clean diagonal.
# Leather grip beneath the quillons.
poly([(9,20),(13,24),(7,30),(3,26)], 'ink')
poly([(9,22),(11,24),(6,28),(4,26)], 'leather_dark')
line(9,23,5,27,'leather_light')
line(10,24,7,27,'leather')
line(8,24,10,26,'ink')
line(6,26,8,28,'ink')
# Tapered, bevelled steel blade.
poly([(10,17),(23,4),(28,2),(27,8),(14,21)], 'ink')
poly([(11,17),(24,4),(26,4),(13,19)], 'steel_light')
poly([(13,19),(26,6),(26,8),(15,19)], 'steel')
line(13,19,26,6,'glint')
line(15,19,25,9,'steel_dark')
line(12,16,22,6,'glint')
# Swept brass crossguard.
poly([(7,16),(10,18),(10,19),(14,23),(16,23),(18,25),(16,27),(13,25),(7,19),(6,18)], 'ink')
poly([(8,17),(9,18),(9,20),(14,25),(16,26),(17,25),(15,24),(14,24),(8,18)], 'gold')
line(8,18,15,25,'gold_light')
line(8,17,9,18,'gold_glint')
dot(16,25,'gold_glint')
# Guard's little red inset and diamond pommel.
poly([(11,20),(13,20),(14,22),(12,24),(10,22)], 'ink')
dot(12,21,'gem_light')
rect(11,22,2,1,'gem')
poly([(4,25),(7,28),(5,30),(2,27)], 'ink')
poly([(4,26),(6,28),(5,29),(3,27)], 'gold')
dot(4,27,'gold_glint')
dot(5,28,'gold_light')

# BOW -- upper right. Curved wooden limbs, a taut string, and a nocked arrow.
# String is subdued so the weapon's curved silhouette stays dominant.
line(44,5,44,27,'ink')
line(45,6,45,26,'steel_light')
poly([(43,3),(47,4),(51,6),(54,9),(57,13),(58,17),(57,21),(54,25),(50,28),(45,29),(43,28),(44,25),(47,25),(50,22),(52,19),(53,16),(52,13),(50,10),(47,7),(44,7)], 'ink')
poly([(45,4),(48,6),(51,8),(54,12),(56,16),(55,21),(52,25),(48,27),(45,28),(45,26),(48,25),(51,22),(53,19),(54,16),(53,12),(50,8),(47,6),(45,6)], 'gold')
line(47,5,50,7,'gold_light')
line(50,7,54,12,'gold_light')
line(54,12,55,15,'gold_light')
line(55,20,52,24,'gold_light')
line(52,24,48,27,'gold_light')
line(48,27,45,27,'gold_light')
line(52,11,53,14,'gold_dark')
line(53,20,51,23,'gold_dark')
rect(44,4,2,2,'gold_glint')
rect(44,26,2,2,'gold_glint')
# Dark wrapped handgrip.
poly([(53,13),(57,14),(58,17),(57,20),(53,20),(54,16)], 'ink')
rect(54,14,2,5,'leather')
dot(54,14,'leather_light')
line(54,16,56,17,'leather_dark')
line(54,18,56,19,'leather_dark')
# Arrow, fletching, and silver broadhead.
line(38,16,60,16,'ink')
line(41,15,57,15,'ink')
line(41,17,57,17,'ink')
line(40,16,57,16,'gold_light')
poly([(37,13),(40,13),(43,16),(40,19),(37,19),(39,16)], 'ink')
line(38,14,40,14,'steel_light')
line(39,15,41,16,'steel')
line(38,18,40,18,'steel')
dot(40,17,'steel_dark')
line(39,16,44,16,'gold_light')
poly([(56,12),(62,16),(56,20),(57,16)], 'ink')
poly([(57,14),(60,16),(57,18),(58,16)], 'steel')
line(57,14,60,16,'glint')
dot(58,17,'steel_light')

# SHIELD -- lower left. Riveted steel rim and an enamel face.
poly([(5,36),(11,36),(16,34),(21,36),(27,36),(27,47),(25,53),(21,57),(16,61),(11,57),(7,53),(5,47)], 'ink')
poly([(6,37),(11,37),(16,35),(21,37),(26,37),(26,47),(24,52),(20,56),(16,59),(12,56),(8,52),(6,47)], 'steel')
poly([(16,35),(21,37),(26,37),(26,47),(24,52),(20,56),(16,59),(16,56),(21,52),(23,47),(23,39),(20,39)], 'steel_dark')
line(6,37,11,37,'glint')
line(11,37,16,35,'glint')
line(6,38,6,46,'steel_light')
line(7,48,9,52,'steel_light')
line(10,53,15,58,'steel_light')
line(17,58,23,52,'steel')
line(21,37,25,37,'steel_light')
# Inset field with a dark separation from the rim.
poly([(8,39),(12,39),(16,37),(20,39),(24,39),(24,47),(22,51),(19,54),(16,57),(13,54),(10,51),(8,47)], 'ink')
poly([(9,40),(12,40),(16,38),(20,40),(23,40),(23,47),(21,51),(16,55),(11,51),(9,47)], 'teal')
poly([(16,38),(20,40),(23,40),(23,47),(21,51),(16,55)], 'teal_dark')
line(9,40,9,46,'teal_light')
line(10,47,12,50,'teal_light')
line(12,40,15,39,'teal_light')
# A compact gold cross, worked around a faceted red boss.
poly([(14,40),(18,40),(18,44),(21,44),(21,47),(18,47),(18,52),(16,54),(14,52),(14,47),(11,47),(11,44),(14,44)], 'ink')
rect(15,41,2,11,'gold')
rect(12,45,8,1,'gold_light')
line(15,41,15,51,'gold_light')
dot(16,52,'gold_light')
dot(15,41,'gold_glint')
poly([(16,43),(19,46),(16,49),(13,46)], 'gold_dark')
poly([(16,44),(18,46),(16,48),(14,46)], 'gold_light')
dot(16,45,'gem_light')
rect(15,46,2,1,'gem')
dot(16,47,'gem_dark')
# Rim rivets.
for x,y in [(7,38),(25,38),(9,51),(23,51)]:
    dot(x,y,'ink')
    dot(x,y-1,'gold_light')

# BATTLE AXE -- lower right. Local coordinates rotate the head and haft 45 degrees.
cx,cy = 50,44
q = math.sqrt(0.5)
def pt(u,v):
    return (round(cx+(u-v)*q), round(cy+(u+v)*q))
def ap(points,col):
    poly([pt(u,v) for u,v in points],col)
def al(u0,v0,u1,v1,col):
    a,b=pt(u0,v0),pt(u1,v1)
    line(*a,*b,col)
# Long wrapped wooden haft and brass end-cap.
ap([(-2,-8),(2,-8),(2,22),(-2,22)], 'ink')
ap([(-1,-6),(1,-6),(1,21),(-1,21)], 'leather')
al(-1,5,-1,20,'leather_light')
al(1,5,1,20,'leather_dark')
for v in [10,13,16,19]:
    al(-1,v,1,v,'ink')
    al(-1,v+1,0,v+1,'gold')
ap([(-2,20),(2,20),(2,23),(-2,23)], 'ink')
ap([(-1,21),(1,21),(1,22),(-1,22)], 'gold_light')
# Upper spike.
ap([(-2,-5),(-1,-10),(0,-12),(2,-7),(2,-5)], 'ink')
ap([(0,-10),(1,-7),(0,-6),(-1,-6)], 'steel_light')
# Crescent blades. Silver cutting edges remain continuous around both faces.
blade=[(2,-3),(6,-4),(8,-7),(10,-6),(12,-2),(12,2),(10,6),(8,7),(6,4),(2,3)]
for sign in [-1,1]:
    def side(points):
        return [(sign*u,v) for u,v in points]
    ap(side(blade),'ink')
    ap(side([(3,-2),(7,-3),(8,-5),(9,-5),(11,-2),(11,2),(9,5),(8,5),(7,3),(3,2)]),'steel')
    ap(side([(8,-5),(9,-5),(11,-2),(11,2),(9,5),(8,5),(9,1),(9,-2)]),'steel_light')
    ap(side([(3,0),(8,0),(9,2),(8,5),(7,3),(3,2)]),'steel_dark')
    al(sign*9,-4,sign*10,-2,'glint')
    al(sign*11,-1,sign*11,1,'glint')
    al(sign*10,2,sign*9,4,'steel_light')
    al(sign*4,-2,sign*7,-3,'steel_light')
# Brass socket with a square pin.
ap([(-2,-5),(2,-5),(2,5),(-2,5)],'ink')
ap([(-1,-4),(1,-4),(1,4),(-1,4)],'gold')
al(-1,-4,-1,4,'gold_light')
al(-1,-4,1,-4,'gold_glint')
al(-1,3,1,3,'gold_dark')
x,y=pt(0,0)
rect(x-1,y-1,3,3,'ink')
dot(x,y,'gem')
dot(x,y-1,'gem_light')

view(result, scale=8, margin=0)
save('weapon-set-icons', result)
finish(result)
