# Blue-cloak girl mage — 64 px RPG sprite
result = new_canvas(64, 64, name='blue_cloak_girl_mage')
c = result
# A compact palette, with cool shadows and warm magical accents.
ink = '#171c32'
navy0 = '#20283f'
navy1 = '#283757'
navy2 = '#344b73'
navy3 = '#45628c'
navy4 = '#6682a5'
cream = '#f5eddb'
white = '#fff8eb'
silver = '#cbd5df'
silver2 = '#93a7bf'
skin0 = '#b97972'
skin1 = '#e6a28b'
skin2 = '#ffd0ac'
skin3 = '#ffe4c4'
hair0 = '#797a93'
hair1 = '#adb0c1'
hair2 = '#dcdbd6'
hair3 = '#fff0d4'
gold0 = '#6a4140'
gold1 = '#ad713e'
gold2 = '#e4a64c'
gold3 = '#ffd17a'
gold4 = '#fff3be'

def p(points, fill, edge=None):
    c.poly(points, fill)
    if edge:
        c.poly(points, edge, fill=False)

def line(a, b, color):
    c.line(a[0], a[1], b[0], b[1], color)

# Small, stepped light around the staff's suspended amber stone.
p([(51,3),(55,6),(58,10),(58,14),(55,18),(50,20),(45,17),(43,13),(44,8),(48,5)], '#efad3c14')
p([(50,5),(54,7),(56,10),(56,14),(53,17),(49,17),(45,14),(45,9)], '#ffc65c25')
# Staff shaft, ferrule and a small cap. Its straight contour reads at 1x.
p([(50,18),(52,18),(52,57),(51,59),(49,58),(49,22)], gold0, ink)
c.line(50,22,50,56,gold2)
c.line(51,22,51,56,gold1)
c.rect(49,54,3,2,gold3)
c.rect(50,57,2,1,gold1)
# Crescent-shaped cradle: open around the luminous gemstone.
p([(47,9),(46,10),(45,14),(46,18),(49,21),(52,21),(55,18),(56,13),(55,10),(54,10),(54,15),(52,18),(49,18),(47,15)], gold1, gold0)
line((46,12),(46,16),gold3)
line((47,17),(49,19),gold2)
line((50,19),(52,19),gold3)
line((54,15),(54,17),gold2)
c.rect(49,21,4,2,gold2)
c.rect(50,21,2,1,gold4)
# Angular amber crystal, clean bright core and a dark lower facet.
p([(50,6),(52,6),(54,10),(54,12),(51,16),(48,13),(48,10)], '#e58a34', gold1)
p([(50,7),(52,7),(53,10),(51,14),(49,12),(49,10)], '#ffc75d')
p([(50,8),(51,8),(52,10),(51,12),(50,11)], '#fff6c7')
c.set(50,7,white)
c.set(52,13,gold2)
c.set(43,7,gold2)
c.set(44,6,gold3)
c.set(57,8,gold3)
c.set(58,15,gold2)

# Legs under the open cloak, with a relaxed, slightly staggered stance.
p([(24,42),(29,43),(29,51),(27,55),(23,54),(23,49)], navy1, ink)
p([(33,42),(38,42),(38,52),(34,54),(32,51)], navy1, ink)
c.rect(25,45,3,5,navy3)
c.rect(34,45,3,5,navy2)
# Left white boot angles out; the other remains planted forward.
p([(23,49),(29,49),(29,56),(28,58),(22,58),(21,57),(22,54)], silver, ink)
p([(24,50),(28,50),(27,56),(23,56)], cream)
c.rect(24,50,3,2,white)
c.line(22,57,27,57,silver2)
c.set(22,56,cream)
c.line(23,49,28,49,navy4)
p([(33,49),(38,49),(38,55),(40,57),(40,59),(33,59),(32,57)], silver, ink)
p([(34,50),(37,50),(37,56),(39,57),(34,57)], cream)
c.rect(34,50,3,2,white)
c.line(34,58,39,58,silver2)
c.line(33,49,37,49,navy4)

# Broad single cloak silhouette. The inset panels describe only a few folds.
p([(23,25),(35,25),(40,28),(42,33),(42,40),(45,47),(43,49),(38,51),(33,49),(28,50),(24,52),(18,50),(15,47),(17,41),(18,32),(20,28)], navy1, ink)
p([(22,28),(26,28),(24,37),(24,45),(21,50),(17,47),(19,38),(19,32)], navy2)
p([(20,31),(22,29),(23,29),(21,37),(20,43),(18,46),(19,39)], navy3)
p([(37,28),(40,30),(40,39),(44,47),(40,49),(36,47),(34,38)], navy0)
p([(39,33),(40,40),(43,47),(41,47),(38,42),(37,36)], navy2)
line((17,47),(21,49),navy3)
line((22,50),(24,50),navy3)
line((39,49),(43,47),navy3)
# Inner shadow and simple ivory tunic.
p([(26,28),(33,28),(36,37),(36,46),(32,48),(27,47),(23,46),(24,36)], navy0)
p([(27,28),(32,28),(34,33),(34,38),(36,44),(32,46),(25,45),(25,39)], silver2, ink)
p([(28,29),(31,29),(33,34),(32,39),(34,44),(29,44),(27,43),(27,36)], cream)
c.line(28,31,28,37,white)
p([(26,39),(33,39),(34,43),(31,44),(25,43)], silver)
c.line(30,40,30,43,cream)
# Belt and a single metal clasp.
c.rect(25,37,9,3,navy0)
c.line(26,37,32,37,navy3)
c.rect(29,37,3,3,gold1)
c.rect(30,38,1,1,gold3)
# Left hanging sleeve and visible hand.
p([(20,29),(24,30),(23,35),(21,40),(17,39),(17,35)], navy2, ink)
p([(20,31),(22,31),(21,36),(18,37)], navy3)
line((18,38),(21,39),navy4)
p([(18,39),(21,40),(21,43),(20,44),(18,43),(17,41)], skin1, ink)
c.line(18,40,18,42,skin3)
c.line(19,40,20,41,skin2)
c.set(20,42,skin2)
# Right sleeve extends comfortably to a hand wrapped around the staff.
p([(36,29),(39,28),(42,30),(44,33),(48,31),(49,34),(45,37),(42,37),(39,34)], navy2, ink)
p([(39,30),(41,31),(43,34),(45,34),(47,33),(46,35),(43,36)], navy3)
line((46,32),(47,35),navy4)
p([(48,31),(50,30),(52,31),(52,34),(49,35),(47,34)], skin1, ink)
c.line(49,31,51,31,skin3)
c.line(49,32,50,32,skin2)
c.line(49,34,50,34,skin2)
c.set(51,33,skin0)

# Hood: pointed crown and broad dark rim framing the light hair.
p([(28,4),(32,4),(36,6),(39,10),(40,16),(39,23),(36,27),(33,29),(25,28),(21,25),(19,20),(19,14),(21,9),(25,6)], navy1, ink)
p([(28,5),(32,5),(35,7),(37,10),(35,11),(25,11),(22,15),(21,20),(20,18),(21,12),(24,8)], navy2)
line((25,7),(28,6),navy3)
line((29,5),(32,5),navy3)
line((21,12),(22,10),navy3)
p([(25,10),(32,9),(36,11),(38,15),(37,23),(34,27),(27,27),(23,25),(21,20),(22,14)], navy0, ink)
# Silver hair at the sides and behind the face.
p([(25,11),(29,9),(34,10),(37,13),(37,21),(36,26),(33,26),(31,23),(27,26),(23,25),(22,22),(22,16)], hair1, hair0)
p([(23,17),(25,16),(26,21),(25,24),(23,23)], hair2)
p([(35,17),(36,17),(36,23),(34,25),(34,21)], hair2)
c.set(23,24,hair3)
# Neck and face, nearly square to the viewer.
c.rect(28,24,5,4,skin1)
c.rect(29,25,3,2,skin2)
p([(25,15),(27,12),(33,12),(35,15),(35,22),(33,25),(29,26),(26,24),(24,21),(24,17)], skin2, skin0)
p([(27,15),(32,14),(34,16),(34,22),(32,24),(29,24),(26,22),(25,19)], skin3)
c.line(25,21,26,22,skin1)
c.set(33,23,skin2)
# Eyes: dark upper lids, cool irises, one-pixel reflected light.
c.line(25,18,28,18,ink)
c.rect(26,19,2,2,'#427989')
c.set(26,19,white)
c.set(27,20,'#244251')
c.line(31,18,34,18,ink)
c.rect(31,19,2,2,'#427989')
c.set(31,19,white)
c.set(32,20,'#244251')
c.set(25,21,'#eda79b')
c.set(34,21,'#eda79b')
c.set(30,21,skin2)
c.line(29,23,30,23,skin0)
# Fringe, with large quiet clusters instead of individual noisy strands.
p([(24,13),(27,10),(31,10),(34,11),(36,14),(36,18),(34,17),(32,14),(31,17),(29,17),(29,14),(27,17),(24,18),(23,17)], hair2, hair0)
p([(25,13),(28,11),(31,11),(33,12),(33,13),(30,12),(28,14),(26,16),(24,16)], hair3)
p([(33,12),(35,14),(35,16),(34,15)], hair3)
c.set(30,15,hair3)
c.line(23,18,23,21,hair3)
# High cloak collar, tiny gold fastening, and one uncluttered trim line.
p([(23,25),(27,26),(29,28),(27,31),(23,29),(22,27)], navy2, ink)
p([(34,25),(37,25),(38,28),(33,31),(31,28)], navy2, ink)
line((24,26),(27,28),navy4)
line((34,27),(36,26),navy3)
line((25,31),(23,40),gold1)
line((35,31),(37,43),gold1)
c.set(24,34,gold2)
c.set(36,37,gold2)
p([(29,27),(31,27),(32,29),(30,31),(28,29)],gold1, gold0)
c.rect(29,28,2,2,gold3)
c.set(29,28,gold4)

view(result, scale=7, margin=3, edges='all')
save('blue-cloak-girl-mage', result)
finish(result)
