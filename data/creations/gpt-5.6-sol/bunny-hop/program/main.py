# Shared 40x32 stage gives the hop room to read while preserving frame 1.
f1 = new_canvas(40, 32, name="frame_1_original")
f1.blit(input_canvas, 7, 4)

f2 = new_canvas(40, 32, name="frame_2_mid_leap")
ink, mid, shadow, fur, inner, inner_dark, gold = 1, 2, 3, 4, 5, 6, 7

# Airborne rabbit facing left. Dark under-shapes provide a consistent one-pixel outline.
# Ears swept back by the forward motion.
f2.poly([(8,12),(9,7),(12,1),(15,1),(16,3),(14,10),(13,13)], ink)
f2.poly([(11,12),(14,7),(19,2),(22,3),(22,5),(17,12)], ink)
f2.poly([(10,10),(11,6),(13,2),(14,2),(14,5),(12,11)], fur)
f2.poly([(14,11),(16,7),(20,3),(21,4),(19,8),(17,12)], fur)
f2.poly([(12,9),(13,4),(14,3),(14,7),(13,10)], inner)
f2.poly([(16,9),(19,5),(20,4),(19,7),(17,10)], inner_dark)

# Trailing hind legs and forward-reaching forelegs.
f2.poly([(23,19),(29,19),(32,22),(38,23),(39,26),(37,29),(31,28),(27,25),(22,24)], ink)
f2.poly([(25,20),(29,21),(32,24),(37,24),(38,26),(36,27),(31,26),(28,23),(24,23)], fur)
f2.poly([(15,20),(13,23),(9,25),(5,29),(1,29),(0,27),(3,24),(9,21),(12,18)], ink)
f2.poly([(14,20),(12,23),(8,25),(5,28),(2,28),(4,25),(10,22),(12,19)], fur)
f2.poly([(18,21),(16,24),(13,26),(9,29),(5,29),(4,27),(8,24),(13,21)], ink)
f2.poly([(17,22),(15,24),(12,26),(9,28),(6,28),(9,25),(14,22)], mid)

# Main body, tail and head silhouette.
f2.poly([(11,12),(15,9),(22,9),(28,11),(31,14),(32,19),(29,23),(25,25),(18,25),(12,22),(9,18)], ink)
f2.poly([(12,13),(16,10),(22,10),(27,12),(30,15),(30,19),(27,22),(23,24),(18,24),(13,21),(10,18)], fur)
f2.circle(32,14,4,ink)
f2.circle(32,14,3,gold)
f2.set(30,12,fur).set(30,13,fur)

# Head and muzzle overlap the body at the front.
f2.poly([(4,11),(8,8),(13,9),(16,12),(16,17),(13,20),(8,21),(4,19),(1,16),(1,13)], ink)
f2.poly([(5,11),(8,9),(12,10),(15,12),(15,16),(12,19),(8,20),(5,18),(2,16),(2,13)], fur)
f2.poly([(2,14),(5,12),(7,13),(7,17),(4,18),(2,16)], mid)
# Cheek, eye, nose and speed-facing highlights.
f2.rect(8,17,5,2,mid)
f2.set(7,12,ink).set(6,12,ink)
f2.set(1,15,inner_dark)
f2.set(10,10,mid).set(14,14,mid).set(15,15,mid)
# Body shading emphasizes the tucked arc and leg joins.
f2.poly([(18,21),(23,22),(27,20),(29,18),(29,21),(26,23),(22,24),(18,23)], mid)
f2.rect(26,22,3,2,shadow)
f2.set(28,21,shadow).set(12,20,shadow).set(13,21,shadow)

# Match the original rabbit's right-facing direction of travel.
f2.mirror("h")

view(flatten([f1], name="preview_frame_1"), scale=12, margin=1, edges="all")
view(flatten([f2], name="preview_frame_2"), scale=12, margin=1, edges="all")
finish([f1, f2])
