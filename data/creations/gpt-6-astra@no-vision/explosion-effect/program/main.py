# Two-frame explosion sprite sheet, 64 x 64, transparent.
# Each frame occupies a 32 x 64 cell; the shared blast origin is y=32.
result = new_canvas(64, 64, name="explosion_2_frames")
c = result
P = {
    'wine': '#a62936',
    'red': '#dc3c30',
    'hot': '#f45d26',
    'orange': '#ff8f24',
    'gold': '#ffbd32',
    'yellow': '#ffe34b',
    'lemon': '#fff385',
    'white': '#fffbd0',
}

def poly(pts, col, offset=0):
    c.poly([(x+offset,y) for x,y in pts], P[col])

def line(x0,y0,x1,y1,col,offset=0):
    c.line(x0+offset,y0,x1+offset,y1,P[col])

def dot(x,y,col,offset=0):
    c.set(x+offset,y,P[col])

def rect(x,y,w,h,col,offset=0):
    c.rect(x+offset,y,w,h,P[col])

# FRAME 01. A compact, incandescent ignition with a yellow-white heart.
poly([(13,19),(16,20),(18,23),(21,22),(21,25),(25,25),
      (24,29),(28,31),(25,33),(27,36),(23,36),(23,40),
      (20,39),(18,44),(16,41),(12,43),(11,40),(7,40),
      (8,37),(4,36),(6,33),(3,30),(7,29),(6,25),
      (10,25),(11,22),(13,23)], 'hot')
# A broken orange rim, brighter on the upper-left side.
poly([(13,20),(16,21),(17,24),(20,23),(20,26),(24,26),
      (23,30),(26,31),(23,33),(25,35),(22,35),(22,38),
      (19,38),(18,42),(16,39),(12,41),(12,38),(9,39),
      (9,36),(6,35),(8,32),(5,30),(9,29),(8,26),
      (11,26),(12,24),(13,25)], 'gold')
poly([(13,23),(16,23),(17,26),(20,25),(20,28),(23,28),
      (22,31),(24,32),(21,34),(22,36),(19,36),(18,39),
      (15,37),(13,39),(12,36),(9,37),(10,34),(7,33),
      (9,31),(8,29),(12,28),(11,26),(13,26)], 'yellow')
poly([(13,25),(16,25),(17,28),(19,27),(19,30),(21,31),
      (20,33),(17,34),(17,37),(14,35),(12,36),(12,33),
      (9,33),(11,31),(10,29),(13,29),(12,27)], 'lemon')
poly([(14,28),(16,28),(16,30),(18,30),(18,32),(16,33),
      (15,35),(13,33),(12,33),(13,31),(12,30),(14,30)], 'white')
# Light breaks and deliberately stepped tongues, not a uniform outline.
line(7,27,8,28,'yellow')
line(15,21,16,23,'yellow')
line(21,27,22,27,'yellow')
dot(24,31,'lemon')
line(10,37,11,38,'orange')
line(20,38,19,40,'orange')
dot(25,35,'red')
dot(17,42,'red')
# Only a few small ejecta in the ignition frame.
line(7,20,8,22,'orange')
dot(7,19,'gold')
line(23,19,22,21,'yellow')
dot(26,23,'orange')
line(4,41,5,40,'gold')
line(24,43,25,44,'hot')
dot(12,46,'orange')

# FRAME 02. Expansion: a ragged red shell and orange turbulence.
o=32
poly([(14,17),(17,19),(17,22),(20,21),(21,24),(25,23),
      (24,27),(28,28),(27,31),(30,33),(26,35),(28,38),
      (24,38),(24,42),(21,41),(19,46),(16,42),(14,44),
      (12,41),(8,42),(9,38),(5,39),(7,35),(3,34),
      (6,31),(4,28),(8,27),(7,23),(11,24),(11,20),(14,22)], 'red',o)
# The deepest colour is reserved for the undersides of a few fragments.
poly([(5,36),(8,36),(8,39),(5,39),(7,37)],'wine',o)
poly([(9,40),(13,39),(14,44),(12,41),(8,42)],'wine',o)
poly([(18,42),(21,40),(20,44),(19,46)],'wine',o)
poly([(24,36),(28,38),(24,38),(24,42),(22,41)],'wine',o)
# Large lobes of live orange flame, separated by red clefts.
poly([(13,21),(16,22),(17,25),(20,23),(20,26),(24,25),
      (23,28),(26,29),(25,32),(27,34),(24,35),(25,37),
      (22,36),(22,40),(19,39),(18,43),(16,40),(14,42),
      (12,38),(9,40),(10,37),(7,36),(8,33),(5,32),
      (8,30),(7,28),(11,28),(9,25),(12,26)], 'hot',o)
poly([(13,23),(15,24),(15,27),(18,26),(19,28),(22,27),
      (22,30),(24,31),(22,33),(24,35),(20,35),(20,38),
      (17,37),(16,40),(14,37),(11,38),(12,35),(9,35),
      (10,32),(8,31),(11,30),(10,28),(13,29)], 'orange',o)
# The centre is still hot, but visibly smaller relative to the expanded shell.
poly([(14,26),(16,28),(18,27),(18,30),(21,30),(20,33),
      (18,33),(19,36),(16,35),(14,37),(13,34),(11,35),
      (12,32),(10,31),(13,30),(12,28),(14,29)], 'gold',o)
poly([(14,29),(16,29),(16,31),(18,31),(17,33),(15,33),
      (14,35),(13,32),(12,31),(14,31)], 'yellow',o)
# Fractured orange curls across the shell: asymmetry makes the motion feel organic.
line(11,22,11,24,'orange',o)
dot(14,20,'hot',o)
line(20,24,20,25,'gold',o)
line(25,28,26,29,'orange',o)
line(27,33,28,33,'hot',o)
line(23,38,22,39,'hot',o)
line(18,40,18,41,'orange',o)
line(10,38,11,37,'orange',o)
line(7,33,8,34,'orange',o)
# Red incursions interrupt the nested bands.
poly([(20,29),(23,28),(23,30),(21,31)],'hot',o)
poly([(17,35),(20,36),(20,38),(18,37)],'hot',o)
line(11,34,10,36,'hot',o)
# Transparent cuts at the edge separate small flying pieces from the main mass.
c.set(38,34,None)
c.set(57,37,None)

# Accelerating embers: short stepped, tapered strokes directed away from the origin.
line(8,14,10,17,'red',o)
line(8,13,9,15,'orange',o)
dot(8,12,'gold',o)
line(19,12,19,15,'hot',o)
line(20,10,19,12,'yellow',o)
line(27,18,25,21,'red',o)
line(28,17,27,18,'gold',o)
line(3,22,5,24,'hot',o)
dot(2,21,'orange',o)
line(29,25,30,24,'orange',o)
dot(31,22,'gold',o)
line(2,38,3,37,'orange',o)
line(2,44,5,41,'red',o)
line(1,45,2,44,'gold',o)
line(9,46,7,49,'hot',o)
dot(7,50,'orange',o)
line(20,48,20,51,'red',o)
dot(20,52,'orange',o)
line(26,45,28,48,'red',o)
line(26,44,27,45,'orange',o)
dot(30,42,'gold',o)
dot(4,16,'red',o)
dot(25,9,'hot',o)
dot(12,52,'red',o)

print(result.stats_text())
print(result.matrix_text(region=(0,8,63,53)))
save('explosion_2_frames', result)
finish(result)
