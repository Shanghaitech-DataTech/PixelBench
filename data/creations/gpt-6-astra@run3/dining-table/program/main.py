# Warm family dining set, drawn at native 64 x 64 resolution.
result = new_canvas(64, 64, name='family_dining_table')
c = result
ink = '#302126'
dark = '#56302d'
shade = '#784235'
wood = '#a55d3b'
mid = '#c47a47'
gold = '#dfa05b'
light = '#f2bd76'
cream = '#ffe0a0'

# Four matching ladder-back chairs, seen from above. North is the master.
chair = new_canvas(17, 19, name='chair_master')
# Supports and rear legs.
chair.rect(2, 1, 3, 17, ink)
chair.rect(12, 1, 3, 17, ink)
chair.rect(3, 2, 1, 14, mid)
chair.rect(13, 2, 1, 14, shade)
# Broad curved top rail.
chair.poly([(2,0),(14,0),(16,2),(16,5),(0,5),(0,2)], ink)
chair.rect(2,1,13,3, wood)
chair.rect(3,1,10,1, gold)
chair.rect(2,4,13,1, shade)
# Ladder rung; open gaps show through the back.
chair.rect(3,7,11,3, ink)
chair.rect(4,7,9,1, gold)
chair.rect(4,8,9,1, wood)
# Seat with an upholstered warm sage pad.
chair.poly([(2,10),(14,10),(16,12),(16,17),(14,19),(2,19),(0,17),(0,12)], ink)
chair.rect(2,11,13,6, wood)
chair.rect(3,11,11,1, gold)
chair.rect(2,17,13,1, shade)
chair.rect(4,12,9,4, '#758461')
chair.rect(4,12,8,1, '#a5af78')
chair.rect(4,15,9,1, '#4c654d')
chair.set(12,13,'#8e9a6c')
# Seats tuck slightly beneath the table.
c.blit(chair,24,1)
c.blit(chair.select(0,0,17,19).rotate(180).preview(),24,44)
c.blit(chair.select(0,0,17,19).rotate(270).preview(),1,24)
c.blit(chair.select(0,0,17,19).rotate(90).preview(),44,24)

# Table feet and under-frame visible below the edge.
for x in (18,42):
    c.rect(x,42,4,9,ink)
    c.rect(x+1,44,2,6,shade)
    c.set(x+1,49,mid)
# Thick tabletop silhouette and lower bevel.
c.poly([(18,15),(45,15),(49,19),(49,44),(46,48),(18,48),(14,44),(14,19)],ink)
c.poly([(18,18),(45,18),(48,21),(48,43),(45,46),(18,46),(15,43),(15,21)],shade)
c.line(18,46,44,46,dark)
c.line(48,25,48,42,wood)
c.line(18,45,44,45,wood)
# The top is rounded at the corners, with a bright carved rim.
c.poly([(18,14),(45,14),(49,18),(49,40),(45,44),(18,44),(14,40),(14,18)],ink)
c.poly([(18,15),(45,15),(48,18),(48,39),(45,42),(18,42),(15,39),(15,18)],mid)
c.line(18,15,44,15,light)
c.line(16,17,16,38,gold)
c.line(18,41,44,41,shade)
c.line(47,19,47,38,shade)
# Inset planked dining surface.
c.poly([(19,17),(44,17),(46,19),(46,38),(44,40),(19,40),(17,38),(17,19)],gold)
c.rect(18,24,28,7,'#d99551')
c.rect(18,32,28,6,'#d18b4b')
for y in (23,31,38):
    c.line(18,y,45,y,wood)
    c.line(19,y+1,44,y+1,'#e7a65d')
# Small, controlled wood grain clusters.
for x,y,w in [(21,19,8),(35,20,7),(19,27,5),(37,26,7),(20,35,6),(35,36,8)]:
    c.line(x,y,x+w,y,'#bf7b43')
    c.line(x+1,y+1,x+w-2,y+1,'#edb16a')
c.line(24,20,27,20,wood)
c.line(38,35,41,35,wood)
c.set(42,34,wood)

# Two small woven linen place mats leave the fruit as the focal point.
for x in (19,38):
    c.rect(x,26,7,9,'#ad6a40')
    c.rect(x,25,7,9,'#f1d29a')
    c.line(x,25,x+6,25,'#ffdfaa')
    c.line(x,33,x+6,33,'#d2ad75')
    for yy in (27,29,31):
        c.set(x,yy,'#d2ad75')
        c.set(x+6,yy,'#d2ad75')
# Tiny ceramic plates.
for x in (22,41):
    c.ellipse(x,29,2,3,'#b78360')
    c.ellipse(x,28,2,2,'#fff0c4')
    c.set(x,28,'#e4cfaa')
    c.set(x+1,29,'#e4cfaa')

# Fruit bowl shadow, pottery body, and dark rim.
c.ellipse(32,34,7,3,'#a5643e')
c.ellipse(32,31,7,5,ink)
c.ellipse(32,32,6,3,'#64867c')
c.line(28,34,36,34,'#385b5c')
c.line(30,35,34,35,'#385b5c')
c.line(28,33,31,33,'#a6c3a1')
c.ellipse(32,29,7,3,ink)
c.ellipse(32,29,6,2,'#c3c89b')
c.ellipse(32,29,5,2,'#68785b')
# A green pear, red apple, orange, and golden bananas.
c.poly([(33,26),(34,23),(35,22),(36,25),(37,27),(36,29),(33,29),(32,27)],'#405735')
c.poly([(34,26),(35,24),(36,26),(36,28),(34,28),(33,27)],'#95ac50')
c.set(34,25,'#c5d475')
c.line(35,23,36,21,dark)
c.line(36,22,38,22,'#577c41')
c.circle(29,27,3,dark)
c.circle(29,27,2,'#ca5140')
c.set(28,26,'#ffad77')
c.set(30,29,'#9b3d36')
c.line(29,25,30,24,dark)
c.circle(34,29,2,'#b26631')
c.circle(34,28,2,'#ed963e')
c.set(33,27,'#ffd173')
# Curved banana bunch along the near lip.
c.path('M 27 29 L 29 31 L 33 32 L 37 30 L 38 28 L 37 28 L 35 30 L 31 30 L 28 28 Z',dark)
c.line(28,29,30,31,'#f2c35c')
c.line(30,31,34,31,'#f2c35c')
c.line(34,31,37,29,'#f2c35c')
c.line(30,30,34,30,'#ffe49a')
c.set(37,28,dark)

view(result)
save('dining-table',result)
finish(result)
