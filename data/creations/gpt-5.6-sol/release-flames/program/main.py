# Two-frame fire-release animation on a shared, widened canvas.
W, H = 96, 63
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 8, 0)

f2 = new_canvas(W, H, name="frame_2_release")
f2.blit(input_canvas, 8, 0)

# Existing palette aliases.
black = "c5"
near_black = "c2"
hair_dark = "c1"
coat_dark = "c9"
coat = "c4"
coat_light = "c11"
slate_dark = "c6"
slate = "c7"
slate_light = "c10"
ash = "c3"
fire_red = "c12"
fire_orange = "c13"
fire_yellow = "c14"

# Remove the old upper body, arm, flame, and lower stance while retaining the
# trailing coat edge at the far left. Rebuild the upper body from source pixels
# three pixels forward to create a pronounced lean.
f2.clear(16, 0, 47, 35)
f2.clear(9, 29, 28, 34)
upper = input_canvas.select(8, 0, 21, 35)
upper.copy_to(19, 0, f2, mode="over")

# Join the shifted torso back into the trailing coat with stepped folds.
f2.poly([(17,18),(22,15),(28,17),(32,25),(29,34),(21,38),(14,37)], coat)
f2.poly([(14,37),(18,27),(22,20),(24,34),(19,43),(11,43)], coat)
f2.poly([(12,39),(19,39),(17,44),(10,44)], coat_dark)
f2.line(22,19,30,30,coat_light)
f2.set(23,21,coat)
f2.set(24,23,coat)

# Reassert head and shoulders above the new coat join, preserving facial detail.
head = input_canvas.select(13, 0, 16, 17)
head.copy_to(24, 0, f2, mode="over")
f2.poly([(25,14),(31,13),(37,17),(39,23),(34,26),(28,22)], coat)
f2.poly([(32,16),(37,18),(39,23),(36,24)], coat_light)

# Back leg remains braced behind the body.
f2.poly([(22,31),(30,33),(27,43),(21,51),(15,58),(10,61),(9,57),(14,50),(17,40)], slate_dark)
f2.poly([(19,34),(25,34),(22,43),(17,51),(14,51),(16,43)], slate)
f2.poly([(10,55),(16,52),(18,56),(14,59),(9,62),(6,62),(6,59)], near_black)
f2.set(12,54,slate_light)
f2.set(10,57,slate)

# Left/front leg steps decisively toward the spell direction.
f2.poly([(27,29),(35,31),(37,39),(40,47),(48,53),(47,58),(39,58),(33,51),(29,45),(24,40)], slate_dark)
f2.poly([(31,33),(35,34),(35,40),(40,48),(46,52),(42,54),(36,49),(32,42)], slate)
f2.poly([(44,51),(50,53),(56,56),(57,60),(54,62),(45,61),(39,58),(40,54)], near_black)
f2.poly([(48,54),(55,57),(55,59),(48,58),(43,56)], slate)
f2.set(53,60,black)
f2.set(56,61,black)

# Extended shoulder and casting arm, nearly horizontal from the forward lean.
f2.poly([(34,19),(41,18),(47,21),(51,23),(48,27),(41,25),(36,24)], coat)
f2.poly([(39,20),(47,21),(51,23),(49,25),(42,24)], coat_light)
f2.poly([(49,22),(58,22),(63,24),(59,27),(50,26)], coat_dark)
f2.poly([(57,22),(64,23),(67,25),(63,28),(58,26)], hair_dark)
f2.rect(64,24,4,3,coat_light)
f2.set(67,23,coat_light)
f2.set(68,25,coat_light)

# Released projectile: a broken, tapering trail behind a distinct airborne
# flame head, with square sparks emphasizing forward speed.
f2.poly([(67,23),(72,20),(76,22),(80,20),(83,23),(78,25),(83,27),(76,28),(72,26),(67,27)], fire_red)
f2.poly([(68,24),(74,22),(78,23),(82,22),(80,25),(84,26),(78,27),(73,26)], fire_orange)
f2.line(69,25,78,25,fire_yellow)
# Small transparent gaps keep the trail from reading as a solid beam.
f2.clear(76,20,2,2)
f2.clear(81,27,2,2)
# Flame head points forward and has a hot core.
f2.poly([(82,20),(86,16),(90,18),(94,16),(92,21),(95,24),(92,28),(87,27),(83,30),(84,26),(81,24)], fire_red)
f2.poly([(84,21),(88,18),(91,20),(94,19),(93,23),(95,24),(91,27),(87,26),(85,28),(86,24)], fire_orange)
f2.poly([(87,21),(91,20),(94,22),(94,25),(91,26),(88,25),(85,24)], fire_yellow)
f2.set(92,23,"#fff09a")
f2.set(89,24,"#fff09a")
f2.rect(72,17,2,2,fire_orange)
f2.set(77,14,fire_red)
f2.set(84,16,fire_orange)
f2.set(88,31,fire_red)
f2.set(79,31,fire_orange)
f2.set(70,30,fire_red)

view(f1, scale=7, margin=1, edges="all")
view(f2, scale=7, margin=1, edges="all")
finish([f1, f2])
