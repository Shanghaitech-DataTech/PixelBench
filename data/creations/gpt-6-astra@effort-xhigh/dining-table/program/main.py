# A small family dining set, viewed from above at a gentle angle.
result = new_canvas(64, 64, name="family_dining_table")
c = result
INK = '#30232b'
DEEP = '#523039'
DARK = '#764336'
WOOD = '#a6603d'
MID = '#c17a47'
LIGHT = '#df9e59'
GLOW = '#f4c477'
GRAIN = '#b36b3e'
CREAM = '#f5dba0'
CLOTH = '#d9b77a'
CLOTHSH = '#b98a59'
TEAL = '#4c8580'
TEALD = '#31575d'
TEALL = '#9dc3a4'

# Small contact shadows keep the furniture grounded without a backdrop.
c.ellipse(32, 54, 23, 3, '#30233222')
c.ellipse(32, 59, 12, 2, '#30233222')

# The north chair: tall back, two open slats and a warm inset seat.
c.rect(25, 5, 3, 22, INK)
c.rect(37, 5, 3, 22, INK)
c.rect(26, 6, 1, 19, LIGHT)
c.rect(38, 6, 1, 19, WOOD)
c.rect(26, 3, 13, 6, INK)
c.rect(27, 4, 11, 3, MID)
c.line(28, 4, 37, 4, GLOW)
c.line(27, 7, 38, 7, DARK)
c.rect(29, 8, 3, 9, INK)
c.rect(30, 8, 1, 8, LIGHT)
c.rect(33, 8, 3, 9, INK)
c.rect(34, 8, 1, 8, MID)
c.rect(26, 16, 13, 3, INK)
c.line(27, 17, 38, 17, MID)
c.poly([(26,18),(38,18),(41,25),(23,25)], INK)
c.poly([(27,19),(37,19),(39,23),(25,23)], MID)
c.line(26,22,38,22,LIGHT)

# Side chairs, rendered as matching angled wooden frames.
def side_chair(mirror=False):
    def p(x,y):
        return (63-x,y) if mirror else (x,y)
    def poly(points,col):
        c.poly([p(x,y) for x,y in points],col)
    def line(x1,y1,x2,y2,col):
        a,b=p(x1,y1),p(x2,y2)
        c.line(*a,*b,col)
    def rect(x,y,w,h,col):
        c.rect(64-x-w if mirror else x,y,w,h,col)
    # Rear and front legs are visible below the seat.
    poly([(6,36),(9,37),(9,47),(6,46)],INK)
    line(7,38,7,45,DARK)
    poly([(13,36),(16,35),(16,45),(13,47)],INK)
    line(14,38,14,45,WOOD)
    # Seat and its thick front lip.
    poly([(5,33),(13,29),(19,34),(12,41),(5,39)],INK)
    poly([(6,33),(13,30),(17,34),(11,38),(6,37)],MID)
    line(7,33,13,31,LIGHT)
    line(7,36,11,37,LIGHT)
    poly([(6,38),(11,39),(16,35),(16,38),(12,42),(6,40)],DARK)
    line(7,39,11,40,WOOD)
    # Side-facing backrest. The small spaces between its bars stay open.
    poly([(2,24),(5,23),(6,39),(3,40)],INK)
    line(3,25,4,38,LIGHT)
    poly([(10,27),(13,27),(13,42),(10,43)],INK)
    line(11,28,11,40,WOOD)
    poly([(6,26),(9,27),(10,37),(7,36)],INK)
    line(7,27,8,35,MID)
    poly([(2,23),(5,21),(13,26),(13,30),(10,30),(2,26)],INK)
    poly([(3,23),(5,22),(12,26),(11,28),(3,25)],MID)
    line(4,23,10,26,GLOW if not mirror else LIGHT)
    line(3,26,10,29,DARK)
    poly([(4,36),(11,39),(11,42),(4,39)],INK)
    line(5,37,10,39,MID)
side_chair()
side_chair(True)

# Four table legs. Rear legs peek through beneath the broad tabletop.
c.poly([(20,35),(24,35),(24,48),(21,49)],INK)
c.line(22,38,22,47,DARK)
c.poly([(40,35),(44,35),(43,49),(40,48)],INK)
c.line(41,39,41,47,DARK)
c.poly([(14,39),(19,39),(19,54),(15,54)],INK)
c.rect(15,42,2,10,MID)
c.line(17,43,17,52,WOOD)
c.line(15,53,18,53,DEEP)
c.poly([(45,39),(50,39),(49,54),(45,54)],INK)
c.rect(46,42,2,10,WOOD)
c.line(46,44,46,51,MID)
c.line(46,53,48,53,DEEP)

# Apron and bevel beneath the tabletop.
c.poly([(13,34),(50,34),(52,40),(49,46),(15,46),(11,40)],INK)
c.poly([(13,39),(50,39),(48,44),(16,44)],DARK)
c.line(16,42,48,42,WOOD)
c.line(18,43,46,43,MID)
c.line(17,45,47,45,DEEP)
# Broad wooden top, clipped corners and a single-pixel silhouette.
c.poly([(18,18),(45,18),(48,20),(53,38),(51,41),(12,41),(10,38),(15,20)],INK)
c.poly([(18,19),(45,19),(47,21),(51,37),(50,39),(13,39),(12,37),(17,21)],MID)
c.poly([(18,19),(45,19),(47,21),(51,37),(13,37),(17,21)],LIGHT)
c.poly([(18,20),(45,20),(47,23),(16,23)],'#d38b4d')
c.line(18,19,45,19,GLOW)
c.line(17,20,13,35,GLOW)
c.line(13,38,50,38,GLOW)
c.line(13,40,50,40,DARK)
c.line(15,39,49,39,WOOD)
# Plank joints and quiet broken grain, never noisy dithering.
c.line(16,25,48,25,WOOD)
c.line(16,26,48,26,'#edb369')
c.line(14,32,50,32,WOOD)
c.line(14,33,50,33,'#edb369')
c.line(20,22,25,22,GRAIN)
c.line(38,22,43,22,GRAIN)
c.line(19,28,23,28,GRAIN)
c.line(18,29,21,29,'#edb369')
c.line(42,29,47,29,GRAIN)
c.line(16,35,23,35,GRAIN)
c.line(19,36,25,36,GLOW)
c.line(41,35,47,35,GRAIN)
c.set(40,36,WOOD)

# Two small ceramic plates suggest a table being set for dinner.
for px in (20,44):
    c.ellipse(px,29,4,3,DARK)
    c.ellipse(px,28,4,2,'#f6e7bf')
    c.line(px-2,28,px+2,28,'#c7bb94')
    c.line(px-2,29,px+2,29,'#e1d5ac')
    c.line(px-1,27,px+1,27,'#fff0d0')

# A short linen runner brings warmth to the center of the family table.
c.poly([(28,20),(36,20),(40,39),(24,39)],CLOTHSH)
c.poly([(29,20),(35,20),(38,38),(26,38)],CREAM)
c.line(28,25,26,37,CLOTH)
c.line(36,25,38,37,CLOTH)
c.rect(25,39,15,3,CLOTHSH)
c.rect(26,39,13,3,CLOTH)
c.line(27,39,38,39,CREAM)
for x in range(26,40,2):
    c.line(x,42,x,43,CREAM)
c.line(28,36,36,36,CLOTHSH)
c.line(28,37,36,37,CLOTH)

# Centerpiece: a glazed blue-green bowl, apples, pear, orange and grapes.
c.ellipse(32,33,9,2,CLOTHSH)
c.ellipse(32,29,8,3,INK)
c.poly([(24,29),(40,29),(38,34),(35,36),(29,36),(26,34)],INK)
c.poly([(25,30),(39,30),(37,34),(29,34),(27,33)],TEAL)
c.poly([(33,31),(39,30),(37,34),(33,35)],TEALD)
c.line(28,34,32,35,TEALD)
c.line(26,31,28,33,TEALL)
c.line(29,33,31,33,'#6aa094')
c.line(25,29,39,29,TEALL)
c.line(27,30,36,30,'#d7dfb0')
# Golden banana behind the round fruit.
c.poly([(28,23),(29,20),(30,23),(33,24),(36,22),(36,25),(33,27),(29,26)],INK)
c.poly([(29,23),(29,22),(31,24),(34,24),(35,23),(35,25),(32,26),(30,25)],'#ecc35b')
c.line(30,24,33,25,'#fff096')
# Pear on the right with a leaf and thin stem.
c.line(36,21,37,19,DEEP)
c.poly([(36,21),(34,23),(34,26),(36,28),(39,27),(40,25),(38,23),(38,21)],INK)
c.poly([(36,22),(37,22),(37,24),(39,25),(38,27),(35,26),(35,24)],'#e9bc4d')
c.line(36,23,36,25,'#fff08b')
c.line(37,20,39,20,'#5f863e')
# Red apple, a warm orange and a few purple grapes.
c.poly([(27,24),(29,23),(32,24),(33,26),(31,29),(27,29),(25,27),(25,25)],INK)
c.poly([(27,24),(29,24),(31,25),(31,27),(30,28),(27,28),(26,26)],'#bd4b3c')
c.line(27,25,28,25,'#ffab75')
c.set(30,27,'#8c3540')
c.line(29,24,29,22,DEEP)
c.line(28,22,27,22,'#6a914c')
c.circle(33,27,2, '#ad6436')
c.line(32,26,34,26,'#f7aa48')
c.line(32,27,33,28,'#e88b3d')
c.set(32,26,'#ffcf6b')
for x,y in [(37,27),(39,28),(36,29),(38,30)]:
    c.set(x,y, '#67465f')
    c.set(x,y-1, '#a3788a')

# South chair: the seat tucks under the table; the slatted back faces us.
c.poly([(26,44),(38,44),(41,51),(23,51)],INK)
c.poly([(27,45),(37,45),(39,49),(25,49)],MID)
c.line(27,45,37,45,GLOW)
c.line(25,49,39,49,LIGHT)
c.line(24,51,40,51,DARK)
c.rect(24,50,3,11,INK)
c.rect(38,50,3,11,INK)
c.line(25,52,25,59,MID)
c.line(39,52,39,59,DARK)
c.rect(28,51,3,7,INK)
c.rect(34,51,3,7,INK)
c.line(29,52,29,56,LIGHT)
c.line(35,52,35,56,MID)
c.rect(24,56,17,3,INK)
c.line(26,57,38,57,WOOD)
c.rect(23,47,19,6,INK)
c.rect(24,48,17,3,MID)
c.line(25,48,39,48,GLOW)
c.line(24,51,40,51,DARK)
c.line(26,50,37,50,LIGHT)

view(result, scale=8, margin=0)
save('family_dining_table', result)
finish(result)
