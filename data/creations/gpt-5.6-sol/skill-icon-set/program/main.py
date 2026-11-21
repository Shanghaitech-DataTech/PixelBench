from pixelbench_api import new_canvas, view, finish

# 2x2 skill icon sheet, each skill occupying one 32x32 quadrant.
c = new_canvas(64, 64, background=None, name="skill_icon_set")

INK = "#17152b"
INK2 = "#292343"
WHITE = "#fff4d6"

# FIREBALL (top-left): broad flame silhouette and compact hot core.
c.poly([(3,22),(6,16),(6,10),(11,12),(14,5),(17,10),(21,4),(22,12),(28,15),(29,21),(27,26),(23,30),(12,30),(6,27)], INK)
c.poly([(6,22),(9,17),(9,13),(13,15),(15,9),(18,15),(21,9),(20,16),(25,17),(27,21),(24,26),(21,28),(12,27),(8,25)], "#d74728")
c.poly([(9,22),(12,17),(13,20),(17,12),(19,19),(22,16),(24,21),(22,25),(18,28),(13,26)], "#ff7b24")
c.circle(16,22,6, "#ffad2f")
c.circle(16,23,4, "#ffd95a")
c.rect(13,20,3,3, WHITE)
c.rect(11,23,2,2, "#ffef9a")
c.rect(22,20,2,3, "#a92c2d")
c.set(25,23,"#76243a")

# ICE SHIELD (top-right): faceted shield with a crystalline snow mark.
c.poly([(48,2),(62,7),(60,20),(57,26),(48,31),(39,26),(36,20),(34,7)], INK)
c.poly([(48,5),(59,9),(58,19),(54,24),(48,28),(42,24),(39,19),(37,9)], "#2476a8")
c.poly([(48,6),(57,10),(56,17),(48,26)], "#53bddd")
c.poly([(39,10),(48,6),(48,26),(43,23),(40,18)], "#2f97c5")
c.poly([(50,7),(57,10),(56,14),(50,12)], "#8be6ed")
c.rect(40,11,2,6,"#64d5e7")
# Snowflake, dark under-stroke then pale inset.
for pts in [((48,11),(48,22)),((43,16),(53,16)),((44,12),(52,20)),((52,12),(44,20))]:
    c.line(*pts[0],*pts[1], INK2)
c.line(48,12,48,21,WHITE).line(44,16,52,16,WHITE)
c.line(45,13,51,19,WHITE).line(51,13,45,19,WHITE)
c.set(48,16,"#ffffff")

# HEALING (bottom-left): emerald heart with a luminous medical cross.
c.poly([(16,62),(12,59),(5,53),(2,47),(2,41),(5,36),(10,34),(14,36),(16,39),(18,36),(22,34),(27,36),(30,41),(30,47),(27,53),(20,59)], INK)
c.poly([(16,59),(11,56),(6,51),(5,47),(5,41),(8,38),(11,37),(14,39),(16,43),(18,39),(21,37),(25,38),(27,41),(27,47),(24,51),(19,56)], "#15965e")
c.poly([(16,57),(9,50),(7,46),(7,41),(10,39),(14,41),(16,46),(18,41),(22,39),(25,42),(25,47),(22,51)], "#29c878")
c.rect(9,40,3,3,"#73e8a0")
c.rect(11,43,2,2,"#50dc8d")
# Cross has a dark keyline and warm-white center.
c.rect(13,45,7,12,INK2)
c.rect(10,48,13,6,INK2)
c.rect(15,46,3,10,WHITE)
c.rect(11,50,11,2,WHITE)
c.rect(16,47,2,2,"#ffffff")

# LIGHTNING (bottom-right): sharp bolt, electric arcs, and hot core.
# Small peripheral sparks with the shared dark keyline.
c.rect(36,39,2,7,INK).rect(37,40,1,5,"#45cfe0")
c.rect(58,49,4,2,INK).rect(59,49,3,1,"#45cfe0")
c.line(38,56,41,59,INK).line(39,56,41,58,"#45cfe0")
c.line(58,37,61,34,INK).line(59,37,61,35,"#45cfe0")
# Main bolt.
c.poly([(49,33),(39,49),(46,49),(42,63),(60,43),(53,43),(58,33)],INK)
c.poly([(50,36),(43,47),(49,47),(46,58),(56,45),(50,45),(54,36)],"#f0a91f")
c.poly([(51,38),(46,46),(51,46),(49,52),(54,44),(52,44),(55,38)],"#ffe052")
c.rect(50,39,2,4,"#fff3a1")
c.set(47,47,WHITE)

view(c, scale=8, margin=0)
finish(c)
