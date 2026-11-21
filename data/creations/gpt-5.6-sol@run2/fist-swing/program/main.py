# Two matching animation frames, widened to give the punch room.
f1 = new_canvas(40, 44, name="frame_1_original")
f1.blit(input_canvas, 3, 0)
f2 = f1.copy(name="frame_2_left_jab")

# Palette indices inherited from the source sprite.
outline, skin, orange, shadow = 1, 3, 5, 6

# Remove the old bent arm on the image-right side. The shoulder and torso stay.
f2.clear(19, 10, 8, 6)
f2.clear(21, 9, 3, 1)

# Repair the torso edge underneath the old pose.
f2.set(19, 14, outline)
f2.set(19, 15, outline)
f2.set(19, 16, outline)
f2.set(18, 15, orange)

# Straight, light left jab: dark silhouette first, then sleeve, forearm and fist.
f2.poly([(16, 9), (20, 9), (23, 10), (34, 10), (34, 9),
         (38, 9), (39, 10), (39, 14), (38, 15), (34, 15),
         (33, 14), (22, 14), (19, 13), (16, 13)], outline)
f2.poly([(17, 10), (20, 10), (23, 11), (27, 11),
         (27, 13), (22, 13), (19, 12), (17, 12)], orange)
f2.poly([(27, 11), (34, 11), (34, 14), (27, 13)], skin)
f2.rect(34, 10, 4, 5, skin)
f2.set(35, 10, shadow)
f2.set(38, 11, skin)
f2.set(38, 12, shadow)
f2.set(37, 14, shadow)
# Sleeve fold and knuckle accents keep the new limb consistent with the source.
f2.set(21, 11, shadow)
f2.set(22, 12, shadow)
f2.line(29, 13, 33, 13, shadow)
f2.set(35, 11, outline)
f2.set(37, 11, outline)

view(f2, scale=10, margin=1, edges="all")
finish([f1, f2])
