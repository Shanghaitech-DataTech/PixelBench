# A gnarled ash-wood crook holding an amethyst spell.
result = new_canvas(48, 48, name="amethyst_crook")
c = result
ink = '#281c32'
wood_dark = '#50303a'
wood_shadow = '#774335'
wood = '#a56843'
wood_light = '#d39759'
wood_glint = '#efc27f'
reflected = '#a477b7'
purple_dark = '#513278'
purple = '#8a4fc7'
bright = '#be7df2'
pink = '#e9b7ff'
white = '#fff0ff'

# A few detached motes and four-point sparks, all on transparency.
def spark(x,y,shade=bright):
    c.set(x,y-2,purple).set(x,y+2,purple)
    c.line(x-1,y,x+1,y,shade)
    c.line(x,y-1,x,y+1,shade)
    c.set(x,y,white)

spark(41,8)
spark(16,12)
spark(36,26)
c.set(39,20,purple).set(40,19,pink)
c.set(14,23,bright).set(14,24,purple_dark)
c.set(21,2,bright)
c.set(43,14,bright)
c.set(31,29,purple)
c.set(19,20,purple).set(20,19,bright)

# Continuous, hand-shaped silhouette: the shaft grows into the curled crown.
outline = [(8,43),(10,46),(13,45),(16,39),(20,34),(24,29),
           (28,25),(32,22),(35,20),(37,17),(38,12),(37,8),
           (35,5),(31,2),(26,2),(22,4),(19,7),(18,11),
           (19,15),(22,18),(25,18),(27,16),(27,14),(25,13),
           (24,14),(23,13),(22,11),(23,9),(26,7),(29,7),
           (32,9),(33,12),(32,15),(30,18),(27,19),
           (24,23),(21,28),(17,34),(13,39)]
c.poly(outline,ink).poly(outline,ink,fill=False)

# Longitudinal wood planes; the dark edge remains uninterrupted.
c.poly([(10,43),(14,38),(18,33),(22,27),(25,23),(28,20),
        (31,20),(29,23),(25,27),(22,31),(18,36),(14,42),(12,44)],wood_shadow)
c.poly([(10,43),(14,37),(18,32),(22,26),(25,22),(28,20),
        (29,21),(25,25),(23,28),(19,33),(15,39),(12,44)],wood)
c.line(10,43,14,37,wood_light)
c.line(15,36,19,30,wood_light)
c.line(20,29,24,23,wood_light)
c.line(25,22,27,21,wood_glint)
c.line(14,40,18,35,wood_dark)
c.line(21,31,25,26,wood_dark)
c.set(17,35,wood_glint).set(20,30,wood_shadow)

# Faceted, irregular wood around the curl.
c.poly([(27,20),(31,18),(34,14),(34,10),(32,7),(29,5),
        (25,6),(22,8),(21,11),(22,14),(25,16),(24,17),
        (22,16),(20,14),(19,10),(21,7),(24,4),(27,3),
        (30,3),(34,6),(36,9),(37,13),(36,17),(33,20),(30,22)],wood_shadow)
c.poly([(20,10),(22,7),(25,5),(28,4),(31,5),(34,7),
        (35,10),(35,14),(33,18),(31,20),(28,21),(28,20),
        (31,17),(33,14),(33,10),(31,8),(29,6),(26,6),
        (23,8),(21,11),(22,14),(24,16),(22,15),(20,13)],wood)
c.poly([(20,9),(22,6),(26,4),(29,3),(31,4),(33,6),
        (29,5),(26,5),(23,7),(21,10)],wood_light)
c.line(23,5,26,4,wood_glint)
c.line(20,10,20,12,wood_light)
c.line(21,13,23,15,wood_light)
c.set(24,16,wood_glint)
c.line(34,9,35,12,wood_light)
c.line(34,15,32,18,wood_light)
c.set(31,19,wood_glint)
c.line(36,12,35,16,wood_dark)
c.line(34,18,32,20,wood_dark)
# Fine splits, a whorl and violet reflected light along the inner rim.
c.line(28,4,30,4,wood_dark)
c.line(31,5,32,6,wood_dark)
c.set(26,5,wood_shadow)
c.line(22,7,21,9,wood_shadow)
c.set(21,11,reflected)
c.set(23,14,reflected).set(25,15,reflected)
c.set(32,10,reflected).set(32,12,purple_dark)
c.line(31,15,30,17,reflected)
c.set(28,19,reflected)

# A suspended crystal, with stepped facets and a pale magical core.
c.poly([(28,7),(30,9),(31,11),(29,14),(27,15),(25,12),(25,10)],purple_dark)
c.poly([(28,7),(30,10),(28,14),(26,12),(26,10)],purple)
c.poly([(28,8),(29,10),(27,13),(26,11)],bright)
c.line(28,8,27,10,pink)
c.set(27,10,white)
c.line(29,11,28,13,pink)
c.set(27,14,bright)

# Ochre leather binding, shaded around the neck of the staff.
c.line(24,24,27,26,ink)
c.line(23,26,25,28,ink)
c.line(22,28,24,30,ink)
c.line(24,24,26,25,wood_glint)
c.set(27,26,wood_shadow)
c.line(23,26,25,27,wood_light)
c.set(25,28,wood_shadow)
c.line(22,28,24,29,wood_glint)
c.set(24,30,wood_shadow)
# A small violet charm hangs from the knot.
c.line(27,27,28,30,wood_dark)
c.set(28,30,ink)
c.poly([(28,30),(30,32),(28,35),(26,33)],ink)
c.poly([(28,31),(29,32),(28,34),(27,33)],purple)
c.set(28,32,pink)

# End grain and a worn ferrule at the foot.
c.line(10,41,13,43,wood_dark)
c.line(10,42,12,43,wood_glint)
c.set(10,44,wood_light).set(11,45,wood_shadow)

view(result, scale=10, margin=0)
save('amethyst_crook', result)
finish(result)
