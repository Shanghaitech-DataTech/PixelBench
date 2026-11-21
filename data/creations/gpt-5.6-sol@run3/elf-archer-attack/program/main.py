# Elf archer attack: original frame plus a maximum-draw key pose.
# Palette indices refer to the supplied sprite palette.
W, H = 47, 47
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 6, 0)

f2 = new_canvas(W, H, name="frame_2_full_draw")
f2.blit(input_canvas, 6, 0)

# Remove the original bow and forward arm from the copied sprite.
f2.clear(31, 0, 16, 47)
f2.clear(25, 18, 12, 9)
# Remove the loose rear arm / decorative flourish so it can become a drawn arm.
f2.clear(6, 9, 14, 20)

# Palette shortcuts.
outline = 20      # near-black
brown_d = 1
brown = 2
wood = 27
wood_hi = 19
skin_d = 16
skin = 3
skin_hi = 12
cream = 14
magenta_d = 9
magenta = 8
pink = 11
green_d = 24
green = 22
cloth_d = 28
cloth = 31
cloth_hi = 32
boot = 36
boot_hi = 40
yellow = 7

# Rear/drawing arm: high elbow at left, forearm folds sharply to cheek.
# Dark silhouette first, then sleeve and skin facets.
f2.poly([(17,18),(12,15),(9,17),(12,21),(18,23),(21,20)], outline)
f2.poly([(10,16),(8,17),(11,22),(15,23),(18,20),(15,18)], brown_d)
f2.poly([(9,17),(11,16),(15,19),(13,21),(11,20)], magenta)
f2.set(10,18,pink).set(11,19,pink).set(12,20,magenta_d)
# Exposed forearm runs back toward the face.
f2.poly([(15,18),(18,14),(22,12),(24,14),(21,17),(18,21)], outline)
f2.poly([(16,18),(19,14),(22,13),(23,14),(20,17),(18,20)], skin)
f2.line(17,18,21,14,skin_hi)
f2.set(18,19,skin_d).set(19,18,skin_d)
# Draw hand anchors at cheek; fingers are visibly curled, but hold no arrow.
f2.rect(22,12,3,4,outline)
f2.set(23,12,skin_hi).set(24,13,skin).set(23,14,skin).set(22,15,skin_d)
f2.set(24,15,brown_d)

# Rebuild shoulder and straight, braced bow arm toward the grip.
f2.poly([(25,19),(30,19),(36,21),(40,21),(40,25),(35,25),(29,23),(25,23)], outline)
f2.poly([(25,20),(29,20),(34,22),(37,22),(37,24),(34,24),(29,22),(25,22)], cloth_hi)
f2.set(26,20,cream).set(27,20,skin_hi).set(28,21,skin)
f2.set(30,21,cloth).set(31,22,cloth).set(32,22,cloth_hi)
# Wrist and clenched bow hand.
f2.rect(36,21,4,4,skin_d)
f2.rect(37,21,3,3,skin)
f2.set(38,21,skin_hi).set(39,22,brown_d).set(39,23,brown)

# Fully bent bow: tips pull left while the grip is driven right.
# Heavy dark edging makes the silhouette crisp against transparency.
f2.line(34,2,39,7,outline)
f2.line(39,7,43,15,outline)
f2.line(43,15,44,21,outline)
f2.line(44,21,40,23,outline)
f2.line(40,23,44,25,outline)
f2.line(44,25,43,32,outline)
f2.line(43,32,39,39,outline)
f2.line(39,39,34,44,outline)
f2.line(35,2,40,7,wood)
f2.line(40,7,43,15,wood)
f2.line(43,15,44,21,wood_hi)
f2.line(44,25,43,32,wood_hi)
f2.line(43,32,39,39,wood)
f2.line(39,39,34,44,wood)
# Gold bindings and grip.
f2.set(36,3,yellow).set(40,8,yellow).set(43,16,yellow)
f2.set(43,30,yellow).set(40,37,yellow).set(36,42,yellow)
f2.rect(40,21,2,5,brown_d)
f2.set(41,22,wood_hi).set(41,23,yellow).set(41,24,wood_hi)

# Taut string: both tips meet at the cheek draw point. No arrow shaft is drawn.
# A muted cord stays subordinate to the brighter wooden bow.
cord = 5
f2.line(34,2,24,14,cord)
f2.line(24,14,34,44,cord)
f2.set(34,2,cream).set(34,44,cream)
f2.set(24,14,skin_hi).set(23,14,skin)

# Shift weight into a wider attack stance by rebuilding the feet at the bottom.
f2.clear(8, 40, 31, 7)
# Rear leg/boot angled left.
f2.poly([(18,38),(17,42),(11,43),(8,46),(18,46),(22,43),(22,39)], outline)
f2.poly([(17,40),(16,42),(12,43),(10,45),(17,45),(20,43),(20,40)], boot)
f2.set(12,44,boot_hi).set(13,43,skin_d).set(16,44,skin_hi).set(18,42,brown)
# Front leg/boot planted to the right.
f2.poly([(27,38),(28,43),(31,44),(34,46),(43,46),(40,43),(35,41),(34,38)], outline)
f2.poly([(29,39),(30,42),(34,43),(36,45),(41,45),(39,43),(34,41),(33,39)], boot)
f2.set(35,43,boot_hi).set(36,44,skin_hi).set(38,44,cream).set(31,41,brown)
# Ground shadow retained across both planted feet.
f2.rect(7,46,37,1,"#17003599")

view(f2, scale=10, margin=1, edges="all")
print(f2.stats_text())
finish([f1, f2])
