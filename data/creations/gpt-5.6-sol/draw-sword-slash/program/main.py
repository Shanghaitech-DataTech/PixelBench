# Two-frame completed draw-sword slash animation.
# Palette indices from the source are reused to preserve its visual language.
W, H = 104, 96
OX, OY = 18, 12

black = input_canvas.color("#020202", "slash_black")
ink = input_canvas.color("c1")
deep = input_canvas.color("c4")
cloth = input_canvas.color("c3")
cloth_hi = input_canvas.color("c2")
leather = input_canvas.color("c6")
leather_dark = input_canvas.color("c8")
skin = input_canvas.color("c10")
skin_shadow = input_canvas.color("c5")
steel = input_canvas.color("c11")
steel_mid = input_canvas.color("c13")
steel_dark = input_canvas.color("c12")
blue = input_canvas.color("c14")

# Frame 1: exact original content, staged with room for the full action.
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, OX, OY)

# Build the final frame in layers: trail, edited fighter, then weapon highlights.
trail = new_canvas(W, H, name="slash_trail")
# A hard, tapered rising arc from lower-left to upper-right.
trail.path("M 3 83 Q 27 72 45 58 Q 68 39 93 13 L 95 20 Q 72 44 50 62 Q 29 78 7 89 Z", black)
# Broken trailing edge and speed fragments keep the arc energetic and pixel-clean.
trail.poly([(1,88),(17,80),(28,76),(19,84),(5,92)], ink)
trail.poly([(14,75),(29,68),(38,62),(30,72)], black)
trail.poly([(55,48),(68,35),(84,21),(73,38)], black)
trail.line(23,82,38,72,deep)
trail.line(67,38,87,18,deep)
trail.set(11,87,deep).set(12,86,deep).set(33,72,deep).set(88,17,black)

fighter = new_canvas(W, H, name="final_fighter")
fighter.blit(input_canvas, OX, OY)
# Remove the old horizontal scabbard/blade extensions while retaining the body.
fighter.clear(OX, OY+40, 28, 9)
fighter.clear(OX+49, OY+36, 29, 8)
# Patch garment areas opened by removing the old weapon and arm pixels.
fighter.poly([(46,49),(57,46),(67,49),(70,62),(64,69),(49,69),(45,61)], cloth)
fighter.poly([(46,49),(53,46),(57,47),(52,68),(46,67)], cloth_hi)
fighter.poly([(55,48),(62,47),(67,50),(66,54),(58,53)], deep)
fighter.line(48,55,48,65,ink)
fighter.line(52,48,57,48,deep)
# Tunic contour and belt details restored over the patch.
fighter.poly([(48,67),(68,67),(69,72),(47,72)], ink)
fighter.rect(53,68,15,3, leather_dark)
fighter.rect(58,68,4,3, leather)
fighter.set(50,69,cloth_hi).set(66,69,skin_shadow)

# Free RIGHT arm: pulled back and down, terminating in a visible empty hand.
fighter.poly([(49,52),(45,55),(43,64),(47,69),(51,66),(51,58)], ink)
fighter.poly([(47,55),(44,58),(44,64),(47,66),(49,63),(49,57)], cloth)
fighter.poly([(46,65),(43,69),(44,73),(49,73),(52,69),(49,66)], skin_shadow)
fighter.rect(45,68,6,4, skin)
fighter.set(44,70,skin).set(45,73,skin_shadow).set(48,73,skin_shadow)

# LEFT arm drives the completed rising strike across the chest to upper-right.
fighter.poly([(63,50),(67,46),(73,40),(78,38),(81,41),(78,46),(72,53),(68,58),(63,56)], ink)
fighter.poly([(65,51),(69,47),(73,42),(77,40),(79,42),(76,46),(71,53),(67,56)], cloth)
fighter.poly([(72,41),(77,37),(81,38),(83,42),(79,46),(75,45)], skin_shadow)
fighter.poly([(76,38),(80,38),(83,40),(81,44),(77,44),(74,42)], skin)
# Closed gripping fingers around the hilt, unmistakably separate from the free hand.
fighter.rect(79,37,5,7, skin_shadow)
fighter.rect(80,38,4,5, skin)
fighter.line(81,39,84,39,leather_dark)
fighter.line(81,42,84,42,leather_dark)

# Sword at the completed upper-right endpoint: hilt, guard and bright blade.
weapon = new_canvas(W, H, name="completed_sword")
weapon.line(76,47,86,35,black)
weapon.line(77,47,87,36,leather)
weapon.line(78,46,87,37,leather_dark)
# Guard crosses the hand/hilt only, confirming a single grip.
weapon.line(75,38,87,47,black)
weapon.line(76,38,87,46,steel_dark)
weapon.line(78,39,85,45,steel)
# Long blade aimed to the upper-right with a sharp outlined tip.
weapon.poly([(84,36),(94,8),(101,2),(98,15),(88,38)], black)
weapon.poly([(86,35),(95,9),(99,5),(96,17),(87,37)], steel_mid)
weapon.poly([(88,34),(97,8),(100,4),(97,16),(89,35)], steel)
weapon.line(90,29,99,7,"#ffffff")
weapon.set(100,3,steel).set(101,2,black).set(86,37,blue)

f2 = flatten([trail, fighter, weapon], name="frame_2_completed_slash")
print(f1.stats_text())
print(f2.stats_text())
view(f1, scale=5, margin=1, edges="all")
view(f2, scale=5, margin=1, edges="all")
finish([f1, f2])
