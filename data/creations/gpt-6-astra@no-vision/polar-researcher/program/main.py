result = new_canvas(48, 48, name='polar_researcher')
c = result
ink = '#172735'
navy = '#293f51'
slate = '#4b6574'
light = '#81969e'
orange = '#c76b43'
shade = '#914534'
bright = '#ed9b60'
cream = '#e7dfbf'
furshade = '#b1b7a6'
furlight = '#fff1d3'
ice = '#b9edf3'
blue = '#639fae'
# Scarf ends pulled straight back by the wind.
c.poly([(24,16),(33,17),(42,15),(40,18),(46,19),(43,22),(35,21),(26,22)], ink)
c.poly([(27,18),(34,18),(40,17),(37,19),(43,20),(36,20),(28,21)], blue)
c.line(35,19,40,20,ice)
# Braced legs, with one boot planted far behind the body.
c.poly([(22,29),(29,29),(33,34),(34,38),(37,41),(37,44),(30,44),(28,39),(25,36),(23,38),(21,42),(17,44),(12,44),(12,41),(16,38),(18,32)], ink)
c.poly([(21,31),(25,32),(23,36),(20,41),(16,41),(19,36)], navy)
c.line(21,33,19,38,slate)
c.poly([(26,32),(29,32),(31,35),(31,39),(34,42),(31,42),(28,38),(25,36)], slate)
c.line(29,35,29,38,light)
# Thick, dark soles and snow gaiters.
c.poly([(16,39),(21,40),(20,43),(14,44),(10,44),(10,42),(14,42)], ink)
c.line(14,42,18,41,slate)
c.line(11,44,19,44,navy)
c.poly([(31,40),(35,40),(36,42),(40,42),(42,44),(41,45),(30,45),(29,43)], ink)
c.line(32,42,35,42,slate)
c.line(32,44,40,44,navy)
# Parka silhouette leans towards the left, into the wind.
c.poly([(17,17),(24,16),(28,19),(31,24),(32,30),(30,34),(23,35),(18,32),(14,26),(14,21)], ink)
c.poly([(18,19),(24,18),(27,21),(29,26),(30,31),(28,33),(23,33),(19,30),(16,25),(16,22)], orange)
c.poly([(24,19),(27,21),(28,25),(30,30),(28,33),(25,33),(24,28)], shade)
c.poly([(18,20),(21,19),(23,22),(23,28),(20,28),(17,24)], bright)
c.line(19,21,23,30,ink)
c.line(20,21,24,30,cream)
c.poly([(19,29),(24,31),(29,30),(30,32),(27,34),(22,33)], shade)
c.line(21,32,27,33,bright)
# Stitched patch pocket and a small research insignia.
c.poly([(24,25),(27,24),(29,28),(25,29)], ink)
c.line(25,26,27,26,bright)
c.set(26,28,orange)
c.rect(23,21,3,3,cream)
c.set(24,22,blue)
# The leading arm is tucked in, mitten against the gale.
c.poly([(16,20),(20,22),(19,26),(16,29),(17,31),(15,33),(11,32),(9,29),(11,25),(12,22)], ink)
c.poly([(14,22),(17,23),(17,26),(13,29),(11,28),(12,25)], orange)
c.line(13,24,12,27,bright)
c.line(12,29,15,30,cream)
c.poly([(12,30),(15,30),(16,32),(13,32)], navy)
c.set(13,30,slate)
# Rear sleeve reaches down to the specimen case.
c.poly([(25,19),(28,19),(31,22),(33,26),(35,28),(34,31),(30,31),(28,27),(26,25)], ink)
c.poly([(27,21),(29,22),(31,26),(31,28),(29,27),(27,24)], orange)
c.line(28,22,30,25,bright)
c.line(30,27,32,27,cream)
# Hard sample case, handle and recessed lid.
c.rect(35,26,7,5,ink)
c.rect(37,27,3,3,slate)
c.rect(37,28,3,2,None)
c.poly([(34,29),(44,29),(46,31),(46,40),(44,42),(33,42),(32,40),(32,31)], ink)
c.rect(34,31,10,9,slate)
c.rect(35,32,8,7,light)
c.rect(43,31,2,9,navy)
c.line(34,33,43,33,ink)
c.line(35,31,42,31,'#bbcac8')
c.rect(35,33,2,2,cream)
c.rect(41,33,2,2,cream)
c.rect(37,36,4,3,cream)
c.set(38,37,blue)
c.set(39,37,blue)
c.set(34,40,light)
c.set(44,40,slate)
# Mitten overlaps the near end of the handle.
c.poly([(31,28),(33,28),(35,29),(36,30),(35,32),(32,32),(30,30)], ink)
c.line(32,29,34,30,slate)
# Deep hood with a broken, plush fur rim.
c.poly([(15,2),(22,2),(26,5),(28,10),(27,16),(24,20),(18,21),(13,19),(9,16),(8,10),(10,5)], ink)
c.poly([(16,3),(22,3),(25,6),(26,11),(25,16),(23,18),(17,19),(12,16),(10,11),(11,6)], orange)
c.poly([(22,4),(25,7),(26,11),(25,16),(22,18),(21,15),(23,11)], shade)
c.line(16,3,20,3,bright)
c.line(12,5,14,4,bright)
c.poly([(13,5),(18,4),(22,6),(23,9),(24,13),(22,17),(19,19),(14,18),(10,15),(9,11),(10,7)], furshade)
c.poly([(12,5),(17,4),(20,5),(22,7),(22,11),(21,15),(19,17),(14,17),(11,14),(10,10),(11,7)], cream)
c.rect(11,6,2,3,furlight)
c.line(13,5,17,5,furlight)
c.set(10,10,furlight)
c.rect(12,15,2,2,furlight)
c.set(17,18,cream)
c.set(22,15,cream)
# Shadowed balaclava and a single broad wraparound goggle lens.
c.poly([(14,7),(19,7),(21,9),(21,13),(19,16),(15,16),(12,13),(11,10)], ink)
c.rect(12,9,10,2,navy)
c.poly([(11,9),(19,8),(21,9),(21,12),(18,14),(12,13),(10,11)], ink)
c.poly([(12,9),(18,9),(20,10),(19,12),(16,13),(12,12),(11,11)], blue)
c.line(12,9,17,9,ice)
c.line(12,10,14,12,ice)
c.line(16,10,18,11,'#e5ffff')
c.set(19,10,ice)
c.line(15,14,19,14,slate)
c.line(16,16,18,16,navy)
print(c.stats_text())
print(c.matrix_text(region=(8,2,28,21)))
save('polar_researcher', result)
finish(result)
