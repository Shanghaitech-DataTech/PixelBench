# Sky pirate girl, 64x64 pixel portrait
c = new_canvas(64, 64, background=None, name="sky-pirate-girl")

# Palette
outline = "#171827"
deep = "#24233a"
navy = "#24354f"
navy2 = "#304967"
navy_hi = "#496783"
red_dark = "#7f2530"
red = "#bd3540"
red_hi = "#e2554e"
skin_shadow = "#b96e63"
skin = "#e79a7f"
skin_hi = "#ffc29a"
hair_dark = "#513442"
hair = "#895044"
hair_hi = "#c07855"
gold_dark = "#79512e"
gold = "#c58a3d"
gold_hi = "#f1c55c"
lens = "#82bfd0"
lens_hi = "#d4f4ea"
white = "#fff1db"

# Wind-swept rear hair, extending left for a readable silhouette
c.poly([(6,20),(12,17),(9,14),(20,15),(25,10),(37,11),(43,17),(39,27),(28,32),(17,29)], outline)
c.poly([(7,20),(16,18),(12,16),(24,17),(28,12),(36,13),(39,19),(35,26),(25,29),(16,26)], hair_dark)
c.poly([(4,27),(15,23),(27,24),(31,31),(20,33),(10,31)], outline)
c.poly([(7,27),(17,25),(26,26),(27,29),(18,31),(11,29)], hair)
c.poly([(2,34),(14,28),(25,30),(27,35),(16,38),(7,37)], outline)
c.poly([(6,34),(15,31),(23,32),(23,34),(15,36)], hair_dark)
c.poly([(8,40),(20,34),(29,36),(29,41),(19,43)], outline)
c.poly([(12,40),(21,36),(26,38),(25,40),(18,41)], hair)
# Hair shine streaks
c.line(12,20,25,17,hair_hi); c.line(9,28,19,27,hair_hi); c.line(8,34,17,33,hair_hi)

# Neck behind jaw
c.poly([(35,39),(46,40),(48,50),(34,51)], outline)
c.poly([(37,39),(44,41),(44,49),(36,49)], skin_shadow)
c.rect(38,40,6,8,skin)

# Face in three-quarter view
c.poly([(25,17),(35,13),(45,16),(51,23),(52,30),(57,34),(52,38),(49,45),(42,48),(33,44),(27,37),(23,27)], outline)
c.poly([(27,18),(35,15),(43,17),(48,21),(49,29),(54,34),(49,36),(47,42),(41,45),(34,42),(29,37),(26,29)], skin)
# Lit planes and ear/nose
c.poly([(31,18),(38,16),(44,19),(47,24),(47,30),(43,32),(44,38),(40,43),(34,40),(29,34),(28,26)], skin_hi)
c.set(48,29,skin); c.set(49,30,skin); c.set(50,31,skin); c.set(51,32,skin)
c.set(52,34,skin_hi); c.set(51,35,skin_hi)
c.rect(25,29,3,7,skin_shadow); c.set(26,31,skin_hi)

# Front hair mass and fringe
c.poly([(21,20),(24,13),(31,8),(42,9),(48,14),(49,21),(45,19),(42,24),(39,18),(34,25),(31,18),(27,28),(24,27)], outline)
c.poly([(24,19),(27,13),(33,10),(41,11),(46,15),(47,18),(43,17),(41,21),(39,15),(34,22),(32,15),(27,25),(25,25)], hair)
c.poly([(28,14),(34,11),(41,12),(44,15),(37,14),(32,18)], hair_hi)
c.poly([(21,20),(25,16),(28,17),(26,27),(23,31)], hair_dark)
# Long side lock
c.poly([(24,27),(29,28),(31,39),(28,47),(22,45),(26,39)], outline)
c.poly([(26,29),(28,30),(29,39),(27,44),(24,43),(28,38)], hair)
c.set(27,32,hair_hi); c.set(28,33,hair_hi)

# Goggles resting on head: strap and two lenses
c.line(23,14,45,11,outline); c.line(23,15,45,12,gold_dark)
c.poly([(25,10),(33,8),(37,11),(35,16),(27,17),(23,14)], outline)
c.poly([(27,11),(32,10),(35,12),(33,15),(28,15),(25,13)], gold)
c.poly([(28,11),(32,11),(34,12),(32,14),(27,14),(26,13)], lens)
c.set(28,11,lens_hi); c.set(29,11,lens_hi)
c.poly([(37,8),(45,9),(49,13),(46,17),(38,16),(35,12)], outline)
c.poly([(39,10),(44,11),(47,13),(45,15),(39,14),(37,12)], gold)
c.poly([(40,10),(44,11),(46,13),(44,14),(39,13),(38,12)], lens)
c.set(40,10,lens_hi); c.set(41,10,lens_hi)
c.rect(34,11,4,3,gold_dark)

# Eye, brow, and confident expression
c.line(34,27,42,25,hair_dark)
c.poly([(34,29),(38,27),(43,28),(40,32),(36,32)], white)
c.poly([(38,28),(42,28),(41,32),(38,31)], navy2)
c.rect(40,29,2,3,outline); c.set(40,29,lens_hi)
c.line(34,33,38,34,skin_shadow)
# Far eye hint
c.line(47,26,49,27,outline); c.set(48,27,white)
# Nose and smirk
c.line(44,32,43,36,skin_shadow); c.line(43,36,46,36,skin_shadow)
c.line(41,39,48,39,red_dark); c.line(43,40,47,40,red)
c.set(47,39,skin_hi)

# Torso / navy coat silhouette
c.poly([(22,45),(31,42),(38,48),(47,46),(56,50),(62,63),(9,63),(12,53)], outline)
c.poly([(24,47),(31,44),(37,50),(47,48),(54,51),(59,62),(13,62),(15,54)], navy)
# Left lapel and shoulder highlights
c.poly([(22,47),(31,45),(35,51),(29,59),(18,61),(15,55)], navy2)
c.poly([(47,49),(53,52),(57,61),(47,61),(42,53)], navy2)
c.line(17,54,26,48,navy_hi); c.line(51,52,56,59,navy_hi)
# Coat lapels and shirt gap
c.poly([(31,44),(39,50),(34,62),(27,53)], outline)
c.poly([(32,46),(37,50),(33,58),(29,52)], navy_hi)
c.poly([(39,49),(46,47),(44,61),(35,61)], outline)
c.poly([(40,51),(44,49),(42,59),(36,59)], deep)
# Gold trim and button
c.line(17,61,31,61,gold_dark); c.line(46,61,57,61,gold_dark)
c.circle(50,57,2,gold_dark); c.circle(50,56,1,gold_hi)

# Red scarf wrapped at neck and flying left
c.poly([(29,43),(36,45),(45,43),(49,48),(44,53),(33,51),(27,47)], outline)
c.poly([(31,44),(36,47),(44,45),(47,48),(43,51),(34,50),(29,47)], red)
c.line(33,46,43,48,red_hi)
# Wind-blown scarf tails
c.poly([(31,49),(24,49),(18,45),(6,46),(15,51),(7,54),(22,55),(34,52)], outline)
c.poly([(30,50),(23,51),(17,48),(10,48),(18,51),(12,53),(23,53),(32,51)], red)
c.poly([(18,48),(11,47),(17,50),(24,51)], red_hi)
c.set(28,50,red_dark); c.set(29,51,red_dark)

# A few intentional single-pixel accents
c.set(30,20,hair_hi); c.set(46,21,skin_hi); c.set(31,36,skin_hi)
c.set(58,60,navy_hi); c.set(14,59,navy_hi)

view(c, scale=8, margin=0)
finish(c)
