# Two-frame draw-sword slash animation.
# Frame 1 preserves every original pixel, only adding transparent stage space.
W, H = 96, 88
OX, OY = 17, 8
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, OX, OY)

# Build the completed action from an editable copy of the supplied character.
actor = input_canvas.copy(name="completed_pose_actor")

# Palette sampled from the original artwork plus dedicated effect colours.
black = actor.color("#07070b", name="slash_black")
black2 = actor.color("#101019", name="slash_edge")
ink = actor.color("#1a1929", name="outline_ink")
skin_dark = actor.color("#a86f69", name="skin_shadow")
skin = actor.color("#d88961", name="skin")
steel_dark = actor.color("#6f7180", name="steel_dark")
steel = actor.color("#b9bbc0", name="steel")
shine = actor.color("#e6e3d8", name="steel_shine")
grip = actor.color("#4a292b", name="grip")

# Remove the old forward left forearm/hand and its short horizontal weapon.
# The torso remains intact; this region is rebuilt as the raised finishing pose.
actor.clear(39, 29, 23, 14)

# Reconstruct the image-right torso edge under the raised arm.
actor.poly([(39,29),(45,28),(46,35),(42,42),(38,40)], ink)
actor.rect(39, 31, 5, 8, "#44445f")
actor.rect(42, 33, 3, 5, "#35344d")

# Left arm drives upward and right, ending with the gripping fist high.
actor.poly([(42,29),(46,27),(51,22),(54,24),(49,31),(45,36),(41,34)], ink)
actor.poly([(44,29),(47,28),(51,23),(53,25),(49,31),(46,34),(43,33)], skin_dark)
actor.poly([(48,25),(51,22),(55,22),(57,25),(55,28),(51,28)], ink)
actor.rect(51,23,5,4,skin)
actor.set(55,24,skin_dark)

# Guard and wrapped hilt are firmly enclosed by the left fist.
actor.line(51, 28, 58, 21, black)
actor.line(52, 29, 59, 22, grip)
actor.line(49, 22, 57, 30, steel_dark)
actor.line(50, 21, 58, 29, steel)

# Finished sword points to the upper right; dark outline keeps it readable.
actor.poly([(55,22),(59,18),(61,19),(58,23)], black)
actor.poly([(57,20),(60,17),(61,18),(59,21)], steel)
actor.poly([(59,18),(61,14),(62,15),(61,19)], black)
actor.poly([(60,16),(61,14),(62,15),(61,17)], shine)

f2 = new_canvas(W, H, name="frame_2_completed_slash")

# Black trailing sweep: a tapered, rising band with broken speed accents.
# It sits behind the character and converges on the raised sword.
f2.poly([(3,79),(8,70),(21,61),(38,49),(55,35),(72,20),(94,2),
         (90,11),(76,25),(59,40),(42,54),(24,67),(10,76)], black)
f2.poly([(7,76),(18,67),(35,55),(52,41),(69,26),(88,8),
         (82,17),(65,32),(48,47),(30,60),(14,71)], black2)
# Hard black core and separated streaks emphasize left-to-right travel.
f2.poly([(4,80),(20,68),(39,53),(57,38),(75,21),(93,5),
         (78,25),(60,42),(42,57),(23,71)], black)
f2.line(2,72,27,54,black)
f2.line(11,83,42,60,black)
f2.line(57,31,90,1,black)
f2.line(67,34,94,10,black2)
# Pixel breaks along the lower-left tail.
f2.rect(1,81,5,2,black)
f2.rect(9,74,4,2,black2)
f2.rect(16,69,3,2,black)
f2.rect(6,85,3,1,black2)

# The full blade continues from the left fist to the upper-right endpoint.
# Draw it before the actor so the gripping hand and guard stay in front.
f2.poly([(70,31),(89,6),(95,2),(92,9),(74,33)], black)
f2.poly([(72,30),(90,7),(94,4),(91,9),(73,32)], steel_dark)
f2.poly([(73,29),(91,7),(93,5),(91,10),(74,31)], steel)
f2.line(75,29,92,7,shine)
f2.set(93,5,shine)

# Composite the completed pose over the trail and blade root.
f2.blit(actor, OX, OY)

view(f1, scale=6, margin=1, edges="all")
view(f2, scale=6, margin=1, edges="all")
finish([f1, f2])
