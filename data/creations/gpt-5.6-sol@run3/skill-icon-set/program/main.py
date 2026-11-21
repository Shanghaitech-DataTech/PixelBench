# 64x64 elemental skill icon sheet on transparency.
result = new_canvas(64, 64, background=None, name="skill-icon-set")

INK = "#171727"
INK2 = "#29243b"
WHITE = "#fff7df"

# FIREBALL - top left, streaking up and right.
result.poly([(2,28),(5,20),(8,18),(7,14),(12,16),(15,10),(17,11),(20,7),(25,7),(29,10),(31,15),(30,20),(27,24),(23,27),(17,28),(12,27),(7,31)], INK)
result.poly([(6,26),(8,21),(13,18),(11,23),(16,19),(17,14),(20,11),(25,11),(28,14),(28,19),(25,23),(21,25),(15,24),(11,27)], "#d83b31")
result.poly([(8,27),(12,22),(16,21),(15,24),(20,23),(17,27),(12,27)], "#f06a2b")
result.circle(22,17,6,"#f06a2b")
result.circle(23,16,4,"#ffad32")
result.poly([(19,14),(22,12),(26,13),(27,16),(25,18),(23,16),(20,18)], "#ffd65a")
result.rect(22,12,3,2,WHITE)
result.set(26,15,"#fff3a0")
result.rect(4,27,3,2,"#9d2c39")
result.rect(8,18,2,2,"#ff8a30")

# ICE SHIELD - top right, angular and crystalline.
result.poly([(35,7),(40,7),(43,4),(48,6),(53,3),(56,6),(61,7),(61,18),(58,25),(49,31),(40,26),(35,18)], INK)
result.poly([(38,9),(42,9),(44,7),(48,9),(53,6),(55,9),(58,9),(58,18),(55,23),(49,27),(43,24),(38,17)], "#277ca9")
result.poly([(41,10),(46,10),(49,12),(53,8),(56,10),(56,17),(53,22),(49,25),(44,22),(40,17)], "#45b8d9")
result.poly([(41,10),(47,11),(49,23),(44,21),(40,17)], "#70d7e6")
result.poly([(47,11),(53,8),(56,11),(55,16),(49,23)], "#b9f2ed")
# Snowflake crest.
result.rect(47,12,3,10,WHITE)
result.rect(43,16,11,3,WHITE)
result.set(45,14,WHITE); result.set(44,15,WHITE); result.set(51,14,WHITE); result.set(52,15,WHITE)
result.set(45,20,WHITE); result.set(44,21,WHITE); result.set(51,20,WHITE); result.set(52,21,WHITE)
result.rect(39,11,2,4,"#dffcff")
result.set(56,19,"#1b638f")

# HEALING - bottom left, lush heart with medical cross.
result.poly([(3,43),(5,39),(9,37),(13,38),(16,41),(19,38),(23,37),(27,39),(30,43),(30,49),(27,54),(18,62),(15,63),(6,55),(2,49)], INK)
result.poly([(6,43),(9,40),(13,41),(16,45),(19,41),(23,40),(27,43),(27,48),(24,52),(16,59),(8,53),(5,48)], "#269b62")
result.poly([(7,43),(10,41),(13,42),(16,47),(16,56),(9,51),(7,47)], "#43c66f")
result.poly([(19,42),(23,40),(27,43),(27,47),(23,51),(18,56),(18,47)], "#79df72")
result.rect(13,45,7,12,INK2)
result.rect(10,48,13,6,INK2)
result.rect(15,46,4,10,WHITE)
result.rect(11,50,12,4,WHITE)
result.rect(8,42,3,2,"#b7f28a")
result.set(24,44,"#e7ffb0")
# Tiny restorative motes.
result.rect(2,36,2,4,"#5de080"); result.rect(1,37,4,2,"#5de080")
result.rect(27,35,2,4,"#d9f57b"); result.rect(26,36,4,2,"#d9f57b")

# LIGHTNING - bottom right, charged zig-zag strike.
result.poly([(48,34),(61,34),(55,44),(61,44),(45,63),(46,52),(37,52)], INK)
result.poly([(50,37),(57,37),(51,46),(56,46),(48,56),(49,49),(42,49)], "#e09e22")
result.poly([(51,37),(55,37),(49,46),(53,46),(49,51),(49,48),(45,48)], "#ffd83f")
result.poly([(52,37),(55,37),(51,43),(49,43)], "#fff48a")
result.rect(56,36,2,2,WHITE)
# Electric arcs and sparks, each backed by dark pixels.
result.poly([(38,39),(42,41),(39,43),(45,45)], INK, fill=False)
result.poly([(39,39),(42,41),(40,42),(44,44)], "#62dbea", fill=False)
result.poly([(57,53),(61,55),(59,58),(63,59)], INK, fill=False)
result.poly([(57,54),(60,55),(59,57),(62,58)], "#62dbea", fill=False)
result.rect(35,45,3,3,INK); result.set(36,46,"#d9ffff")
result.rect(59,39,3,3,INK); result.set(60,40,"#fff48a")

finish(result)
view(result, scale=8, margin=1, edges="all")
