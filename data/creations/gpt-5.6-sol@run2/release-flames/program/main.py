W, H = 84, 63
f1 = new_canvas(W, H, name="frame_1_original")
f2 = new_canvas(W, H, name="frame_2_release")

# Frame 1 retains every original pixel, with added room in front for the motion.
f1.blit(input_canvas, 8, 0)

# Existing palette colors.
black = 6
ink = 3
deep = 9
plum = 10
cloak_dark = 2
cloak = 5
blue_dark = 7
blue = 8
metal = 1
metal_hi = 11
skin = 12
orange = 13
gold = 14
yellow = 15

# New hot fire shades, registered into the shared palette.
red = f2.color("#c93b12", "fire_red")
hot_orange = f2.color("#ff6a0a", "fire_hot_orange")
hot_gold = f2.color("#ffb20b", "fire_hot_gold")
white_hot = f2.color("#fff29a", "fire_white_hot")
smoke = f2.color("#55303a", "ember_smoke")

# Reassemble source regions with the upper body shifted forward into a lean.
# Lower half keeps the source texture and silhouette as the base.
input_canvas.select(0, 28, 34, 35).copy_to(8, 28, f2, mode="over")
# Cloak and torso move right/down slightly.
input_canvas.select(9, 11, 29, 22).copy_to(20, 12, f2, mode="over")
# Head follows farther forward to sell the lean.
input_canvas.select(14, 0, 20, 16).copy_to(25, 1, f2, mode="over")

# Close the waist and sharpen the forward-sloping cloak.
f2.poly([(24,24),(30,16),(39,17),(45,27),(38,34),(26,32)], ink)
f2.poly([(26,23),(31,15),(38,17),(43,27),(36,32),(27,30)], cloak)
f2.poly([(29,17),(35,14),(40,20),(39,24),(32,22)], cloak_dark)
f2.rect(28, 27, 9, 4, cloak)
f2.rect(36, 27, 4, 3, plum)

# Redraw the head's leading edge and face after the torso overlap.
f2.rect(31, 3, 10, 4, cloak)
f2.rect(35, 7, 6, 6, cloak_dark)
f2.rect(39, 8, 4, 3, skin)
f2.set(42, 9, ink)
f2.rect(27, 2, 5, 2, metal)
f2.rect(32, 2, 8, 2, ink)

# Lunge: back leg braces left; front leg steps decisively toward the cast.
# Dark outlines first, then blue-gray lit planes.
f2.poly([(27,29),(34,30),(31,38),(24,46),(18,57),(10,61),(11,55),(18,44),(23,36)], ink)
f2.poly([(27,31),(31,32),(28,38),(22,45),(18,53),(13,56),(18,45),(24,37)], blue_dark)
f2.poly([(20,43),(24,38),(27,37),(24,44),(19,51),(16,51)], blue)
f2.rect(8, 57, 12, 4, cloak_dark)
f2.rect(8, 61, 15, 2, ink)

f2.poly([(32,29),(39,31),(42,39),(49,46),(53,55),(48,60),(43,54),(38,47),(32,42),(27,37)], ink)
f2.poly([(34,31),(38,33),(39,39),(46,45),(50,54),(46,56),(42,50),(37,45),(31,40)], blue)
f2.poly([(37,34),(39,39),(45,44),(47,49),(43,49),(38,44),(34,40)], blue_dark)
f2.poly([(48,54),(57,55),(61,59),(60,62),(47,62),(44,59)], ink)
f2.rect(50, 56, 8, 3, blue_dark)
f2.rect(55, 59, 7, 3, cloak_dark)

# Forward arm: shoulder, sleeve, wrist and open casting hand.
f2.poly([(37,16),(43,16),(48,19),(57,19),(60,23),(56,27),(47,25),(41,23),(36,22)], ink)
f2.poly([(39,17),(43,18),(47,21),(55,21),(56,24),(48,23),(43,21),(39,21)], cloak)
f2.rect(47, 20, 9, 4, blue_dark)
f2.rect(50, 20, 6, 2, blue)
f2.rect(56, 20, 5, 5, skin)
f2.rect(59, 19, 3, 2, skin)
f2.set(61, 18, skin)
f2.set(61, 25, skin)

# Projectile silhouette and ragged, tapered trail.
f2.poly([(59,19),(63,16),(66,18),(69,14),(73,16),(77,13),(81,17),(83,22),(81,27),(77,30),(72,29),(68,32),(65,28),(61,29),(63,25),(58,23)], red)
f2.poly([(58,20),(65,18),(68,20),(72,16),(77,16),(80,19),(82,23),(79,27),(74,28),(70,26),(66,29),(65,25),(59,24)], hot_orange)
# Inner rolling flame mass.
f2.poly([(65,20),(69,18),(71,20),(75,17),(79,20),(79,24),(76,27),(72,25),(69,27),(67,24)], gold)
f2.rect(72, 20, 6, 5, hot_gold)
f2.rect(73, 21, 4, 3, yellow)
f2.rect(74, 21, 2, 2, white_hot)
# Backward tongues read as a fiery trail rather than a held fireball.
f2.poly([(60,21),(55,18),(56,21),(49,18),(52,22),(44,23),(52,25),(56,24),(61,25)], hot_orange)
f2.poly([(58,22),(52,21),(54,23),(48,24),(55,25),(61,24)], gold)
f2.rect(57, 22, 5, 2, yellow)
f2.set(52, 19, gold)
f2.set(47, 20, hot_orange)
f2.set(44, 17, red)
f2.set(66, 13, hot_orange)
f2.set(70, 10, gold)
f2.set(78, 11, red)
f2.set(81, 29, hot_orange)
f2.set(63, 31, red)
f2.set(55, 28, smoke)

view(f1, scale=7, margin=1, edges="all")
view(f2, scale=7, margin=1, edges="all")
finish([f1, f2])
